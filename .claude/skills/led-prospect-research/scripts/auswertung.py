#!/usr/bin/env python3
"""Auswertung von heyReflect-Leadlisten (CSV-Exporte der Google Sheets oder Recherche-CSVs).

Aufruf: python auswertung.py datei1.csv [datei2.csv ...] [--heute YYYY-MM-DD]
Versteht die Spalten der Händler-Tabs (Inhaber, Mittelgroß, Outdoor) und der
Förderverein-Tabs (Pipeline, Details & Recherche).
"""
import csv
import re
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from urllib.parse import urlparse

# Kanonischer Name -> mögliche Spaltennamen (klein geschrieben)
ALIASE = {
    "firma": ["firma", "förderverein", "foerderverein", "schule"],
    "klasse": ["fit_klasse", "prioritaet", "priorität", "prio"],
    "score": ["fit_score", "score"],
    "segment": ["segment", "schultyp"],
    "region": ["ort", "bezirk"],
    "stufe": ["stufe", "status"],
    "website": ["website"],
    "quelle": ["quelle"],
    "entscheider": ["geschaeftsfuehrung", "ansprechpartner"],
    "anschrift": ["strasse"],
    "email": ["e-mail", "email_haupt", "e-mail (haupt)"],
    "aufhaenger": ["aufhaenger", "aufhaenger_brief", "story-aufhänger", "story_aufhaenger", "aufhänger für die mail"],
    "faellig": ["faellig_am", "nachfass 1", "nachfass 1 fällig"],
    "naechster_schritt": ["naechster_schritt", "to-do"],
    "antwort": ["antwort / ergebnis", "rueckmeldung", "verlustgrund"],
}


def lese(pfad):
    with open(pfad, encoding="utf-8-sig", newline="") as f:
        probe = f.read(4096)
        f.seek(0)
        try:
            trenner = csv.Sniffer().sniff(probe, delimiters=";,\t").delimiter
        except csv.Error:
            trenner = ";"
        roh = list(csv.DictReader(f, delimiter=trenner))
    zeilen = []
    for r in roh:
        r = {(k or "").strip().lower(): (v or "").strip() for k, v in r.items()}
        z = {}
        for kanon, namen in ALIASE.items():
            for n in namen:
                if r.get(n):
                    z[kanon] = r[n]
                    break
            else:
                z[kanon] = ""
        z["_datei"] = pfad
        z["_spalten"] = set(r)
        zeilen.append(z)
    return zeilen


def datum(text):
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    return None


def schluessel(z):
    url = z["website"]
    if url:
        if not url.startswith("http"):
            url = "https://" + url
        host = urlparse(url).netloc.lower()
        return host[4:] if host.startswith("www.") else host
    return re.sub(r"[^a-z0-9]", "", z["firma"].lower())


def zeige(titel, zaehler, n):
    print(f"\n{titel}:")
    for wert, k in sorted(zaehler.items(), key=lambda x: (-x[1], x[0])):
        print(f"  {wert or '(leer)'}: {k} ({k / n:.0%})")


def ist_aussortiert(z):
    text = (z["naechster_schritt"] + " " + z["stufe"] + " " + z["klasse"]).lower()
    return any(w in text for w in ("aussortiert", "nicht anschreiben", "raus", "nicht separat"))


def main(argv):
    heute = date.today()
    if "--heute" in argv:
        i = argv.index("--heute")
        heute = datum(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]

    alle = []
    for p in argv:
        zeilen = [z for z in lese(p) if z["firma"]]
        alle.extend(zeilen)
        print(f"{p}: {len(zeilen)} Leads")
    if not alle:
        print("Keine Daten gefunden.")
        return

    gesehen, leads, dubletten = {}, [], []
    for z in alle:
        k = schluessel(z)
        if k in gesehen:
            dubletten.append((z["firma"], z["_datei"], gesehen[k]["_datei"]))
        else:
            gesehen[k] = z
            leads.append(z)

    n = len(leads)
    raus = [z for z in leads if ist_aussortiert(z)]
    aktiv = [z for z in leads if not ist_aussortiert(z)]
    print(f"\nGesamt: {len(alle)} | Dubletten: {len(dubletten)} | Eindeutig: {n} | aussortiert: {len(raus)} | aktiv: {len(aktiv)}")
    for f, d1, d2 in dubletten[:20]:
        print(f"  Dublette: {f} ({d1} ↔ {d2})")

    zeige("Stufe/Status (alle)", Counter(z["stufe"] for z in leads), n)
    zeige("Klasse/Priorität (aktiv)", Counter(z["klasse"] for z in aktiv), max(len(aktiv), 1))
    zeige("Segment (aktiv)", Counter(z["segment"] for z in aktiv), max(len(aktiv), 1))

    antworten = [z for z in leads if z["antwort"] and z["antwort"].lower() not in ("nein", "-", "–")]
    print(f"\nRückmeldungen/Ergebnisse eingetragen: {len(antworten)}")
    for z in antworten[:15]:
        print(f"  {z['firma']}: {z['antwort']}")

    grenze = heute + timedelta(days=7)
    faellig = sorted(
        (datum(z["faellig"]), z) for z in aktiv if datum(z["faellig"]) and datum(z["faellig"]) <= grenze
    )
    print(f"\nFällig bis {grenze:%d.%m.%Y} (inkl. überfällig): {len(faellig)}")
    for d, z in faellig:
        markierung = " ÜBERFÄLLIG" if d < heute else ""
        print(f"  {d:%d.%m.} {z['firma']} – {z['naechster_schritt'] or 'nachfassen'}{markierung}")

    offen = [
        z for z in aktiv
        if z["stufe"].lower().startswith(("1", "offen")) and z["klasse"].upper() in ("A", "B")
    ]

    def score(z):
        try:
            return float(z["score"].replace(",", "."))
        except ValueError:
            return -1

    offen.sort(key=lambda z: (z["klasse"].upper(), -score(z)))
    print(f"\nNoch nicht kontaktiert, Klasse A/B: {len(offen)}")
    for z in offen[:10]:
        print(f"  [{z['klasse']}/{z['score'] or '-'}] {z['firma']} ({z['region']}) – {z['aufhaenger'][:90]}")

    print("\nDatenlücken (aktive Leads):")
    for feld in ["quelle", "entscheider", "anschrift", "email", "aufhaenger", "website"]:
        relevant = [z for z in aktiv if any(a in z["_spalten"] for a in ALIASE[feld])]
        if relevant:
            leer = sum(1 for z in relevant if not z[feld] or z[feld] in ("–", "-", "nicht gefunden"))
            print(f"  {feld}: {leer} von {len(relevant)} leer/ungeklärt")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Aufruf: python auswertung.py datei1.csv [datei2.csv ...] [--heute YYYY-MM-DD]")
    main(sys.argv[1:])
