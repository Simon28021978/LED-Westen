#!/usr/bin/env python3
"""Auswertung von LED-Westen-Leadlisten (CSV, Semikolon).

Aufruf: python auswertung.py datei1.csv [datei2.csv ...]
Gibt Kennzahlen als Text aus: Bestand, Dubletten über Dateien, Verteilungen, Datenlücken.
"""
import csv
import re
import sys
from collections import Counter
from urllib.parse import urlparse


def lese(pfad):
    with open(pfad, encoding="utf-8-sig", newline="") as f:
        probe = f.read(4096)
        f.seek(0)
        try:
            dialekt = csv.Sniffer().sniff(probe, delimiters=";,\t")
        except csv.Error:
            dialekt = csv.excel
            dialekt.delimiter = ";"
        return [
            {(k or "").strip().lower(): (v or "").strip() for k, v in zeile.items()}
            for zeile in csv.DictReader(f, dialect=dialekt)
        ]


def domain(url):
    if not url:
        return ""
    if not url.startswith("http"):
        url = "https://" + url
    host = urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def schluessel(z):
    d = domain(z.get("website", ""))
    if d:
        return d
    name = re.sub(r"[^a-z0-9]", "", z.get("firma", "").lower())
    return f"{name}|{z.get('ort', '').lower()}"


def verteilung(titel, zaehler, gesamt):
    print(f"\n{titel}:")
    for wert, n in zaehler.most_common():
        print(f"  {wert or '(leer)'}: {n} ({n / gesamt:.0%})")


def main(pfade):
    alle = []
    for p in pfade:
        zeilen = lese(p)
        for z in zeilen:
            z["_datei"] = p
        alle.extend(zeilen)
        print(f"{p}: {len(zeilen)} Zeilen")

    if not alle:
        print("Keine Daten gefunden.")
        return

    gesehen, eindeutig, dubletten = {}, [], []
    for z in alle:
        k = schluessel(z)
        if k in gesehen:
            dubletten.append((z.get("firma"), z["_datei"], gesehen[k]["_datei"]))
        else:
            gesehen[k] = z
            eindeutig.append(z)

    n = len(eindeutig)
    print(f"\nGesamt: {len(alle)} | Dubletten: {len(dubletten)} | Eindeutige Leads: {n}")
    for firma, d1, d2 in dubletten[:20]:
        print(f"  Dublette: {firma} ({d1} ↔ {d2})")

    for feld, titel in [
        ("icp_typ", "ICP-Typ"),
        ("prioritaet", "Priorität"),
        ("segment", "Segment"),
        ("ort", "Ort (Top 10)"),
    ]:
        if any(feld in z for z in eindeutig):
            c = Counter(z.get(feld, "") for z in eindeutig)
            if feld == "ort":
                c = Counter(dict(c.most_common(10)))
            verteilung(titel, c, n)

    if any("segment" in z and "prioritaet" in z for z in eindeutig):
        print("\nA-Leads je Segment:")
        c = Counter(z.get("segment", "") for z in eindeutig if z.get("prioritaet") == "A")
        for seg, k in c.most_common():
            print(f"  {seg or '(leer)'}: {k}")

    scores = []
    for z in eindeutig:
        try:
            scores.append(float(z.get("fit_score", "").replace(",", ".")))
        except ValueError:
            pass
    if scores:
        print(f"\nFit-Score: Ø {sum(scores) / len(scores):.1f} | min {min(scores):g} | max {max(scores):g} | bewertet {len(scores)}/{n}")

    print("\nDatenlücken (leere Felder):")
    for feld in ["quelle", "website", "ansprechpartner_rolle", "plz", "signal", "segment", "icp_typ"]:
        if any(feld in z for z in eindeutig):
            leer = sum(1 for z in eindeutig if not z.get(feld))
            print(f"  {feld}: {leer} von {n}")

    hinweise = Counter()
    for z in eindeutig:
        for h in re.split(r"[,|]", z.get("pruefhinweis", "")):
            if h.strip():
                hinweise[h.strip()] += 1
    if hinweise:
        verteilung("Prüfhinweise", hinweise, n)

    ohne_begr = [z.get("firma") for z in eindeutig if z.get("prioritaet") == "A" and not z.get("begruendung")]
    if ohne_begr:
        print(f"\nA-Leads ohne Begründung: {len(ohne_begr)} → {', '.join(ohne_begr[:10])}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Aufruf: python auswertung.py datei1.csv [datei2.csv ...]")
    main(sys.argv[1:])
