---
name: led-prospect-research
description: Prospect-Recherche für heyReflect (LED-Westen und -Capes, v. a. für Kinder) – ICP anwenden und schärfen (Handel: Fahrrad, Outdoor, Laufsport; Fördervereine von Grundschulen), neue Händler oder Fördervereine per Web-Recherche finden, belegen und nach festem Scoring bewerten, bestehende Leadlisten in Google Sheets auswerten und zu Top-Leads, Erkenntnissen und nächsten Schritten verdichten. Nutze diesen Skill immer, wenn es um heyReflect- oder LED-Westen-Leads, Zielkunden, ICP, Händlerakquise, Fahrradläden, Outdoor-/Laufläden, Fördervereine, Schulvereine, Schulstraßen, Pipeline-Auswertung oder „wen sollen wir als Nächstes anschreiben“ geht – auch wenn „ICP“ nicht fällt, und auch als Arbeitsgrundlage für Tim, Rico und Daniel.
---

# heyReflect: ICP & Prospect-Recherche

Ziel: Neue Händler und Fördervereine finden, die nachweislich ins ICP passen, so belegt und bewertet, dass das Team sie ohne Nacharbeit anschreiben kann – und aus den laufenden Listen lernen, welches ICP-Merkmal wirklich zählt.

**Zuerst lesen:** `references/icp.md` (Produkt, ICP H und F, Scoring, Kontaktregeln). Für Recherche zusätzlich `references/suchwege.md`, für Ein-/Ausgabe `references/datenformat.md`.

## Modus erkennen

| Modus | Auslöser | Ergebnis |
|---|---|---|
| A. ICP schärfen | „ICP anpassen“, neue Erkenntnisse/Antworten von Prospects | aktualisierte `references/icp.md` (neue Version + Protokoll) |
| B. Recherche | „finde Fahrradläden in …“, „mehr Fördervereine in Altona“ | CSV unter `daten/` im Sheet-Format |
| C. Auswertung | „fasse zusammen“, „wie steht die Pipeline“, „wen zuerst anschreiben/nachfassen“ | Kurzbericht im Chat |

## Grundsätze

- **Beleg vor Menge.** Jede Angabe braucht eine Quell-URL. Eine falsche Anrede oder ein falscher Aufhänger im Brief kostet mehr als ein fehlender Lead.
- **Keine erfundenen Kontaktdaten.** Namen und E-Mails nur, wenn sie öffentlich auf der Firmen-, Vereins- oder Schulseite stehen. Unsicheres gehört in `pruefhinweis`.
- **Bestand zuerst.** Vor jeder Recherche die bestehenden Sheets lesen und gegen sie abgleichen (Domain/Firmenname). Bereits aussortierte Firmen nicht erneut vorschlagen.
- **Scoring nach `icp.md`, nicht nach Gefühl.** Rohwerte K1–K6 bzw. die F-Kriterien einzeln ausweisen, damit die Bewertung nachvollziehbar und korrigierbar ist. Zahlen per Code berechnen.
- **Aussortieren ist ein Ergebnis.** Einzelläden, falsche Region, Filialen einer Zentrale: mit Grund dokumentieren statt weglassen.
- **Nur lesen in den Sheets, außer der Nutzer will es anders.** Neue Leads als CSV ablegen; ins Sheet nur anhängen, wenn der Nutzer das ausdrücklich will, und vorher Tab und Zeilen bestätigen lassen. Scorecard/Dashboard-Daten nie anfassen.
- **Kostenfrei.** Websuche und öffentliche Seiten; keine kostenpflichtigen Datenanbieter, außer ausdrücklich gewünscht.
- **Ehrlich berichten.** Dünne Ergebnisse, widersprüchliche Quellen oder ein unergiebiges Segment klar benennen.

## Modus A – ICP schärfen

1. `references/icp.md` lesen.
2. Neue Belege sammeln: Antworten/Stufen aus den Sheets (wer ist „Im Gespräch“, „Verloren“, mit welchem `verlustgrund`), Feedback des Nutzers.
3. Nur ändern, was belegt ist. Jede Änderung: Version hoch, Zeile im Änderungsprotokoll, betroffene „Offene Annahme“ auf bestätigt/widerlegt setzen.
4. Im Chat nur die Änderungen nennen.

## Modus B – Recherche

1. **Auftrag klären:** ICP-Typ (H oder F), Segment, Region, Menge. Fehlt etwas → benannte Annahme (Default H: Norddeutschland, 10 Leads; F: Hamburg, 10 Fördervereine).
2. **Bestand laden:** passende Tabs aus den Sheets lesen (IDs in `datenformat.md`), Firmen/Schulen als Ausschlussliste merken.
3. **Suchen** mit den Wegen aus `suchwege.md`.
4. **Verifizieren auf der eigenen Website:** Impressum (GF, Anschrift), Filialseite (Anzahl, aktuell offen?), Shop (Kindersortiment, Warn-/Reflexwesten). Bei F: Vereinsseite, Vorstand (Jahr!), Vereins-E-Mail, Verkehrsthemen, Schulstraßen-Pläne.
5. **Aufhänger formulieren:** ein Satz, konkret und belegt, so wie er im Brief/der Mail stehen kann (Beispiele: „Sie führen Kinder- und Laufräder von Puky sowie Helme und Beleuchtung …“, „Knauerstraße wird ab 2027 Schulstraße …“).
6. **Bewerten** nach `icp.md` (H: K1–K6 → fit_score/fit_klasse; F: Score 0–100 → Priorität).
7. **Speichern** als CSV gemäß `datenformat.md`, sortiert nach Score. Bestehende Dateien nicht überschreiben (`_v2` …).
8. **Abschluss:** Anzahl je Klasse, aussortiert mit Grund, Unsicherheiten, ergiebige/unergiebige Suchwege.

## Modus C – Auswertung

1. Sheets lesen (`get_values` je Tab), lokal als CSV in den Scratchpad schreiben.
2. `python .claude/skills/led-prospect-research/scripts/auswertung.py <datei.csv> [...]` ausführen – liefert Bestand, Dubletten, Verteilung nach Klasse/Segment/Stufe/Status, fällige Nachfass-Termine und Datenlücken.
3. Bericht, knapp in Bulletpoints:
   - **Pipeline:** Leads je Liste, je Stufe/Status, Rückmeldungen bisher
   - **Fällig:** Nachfassen in den nächsten 7 Tagen (Firma, Datum, Schritt)
   - **Als Nächstes anschreiben:** Top 5 noch nicht kontaktierte A/B-Leads mit Aufhänger
   - **Erkenntnisse:** was Antworten bringt (sobald vorhanden), welche ICP-Annahme wackelt
   - **Lücken:** fehlende Anschriften/Entscheider, unbestätigte E-Mails
   - **Nächste Schritte:** max. 3
4. Ergibt sich eine ICP-Erkenntnis → Modus A anbieten.

## Zusammenspiel mit dem Team

- **rico-recherche** führt Modus B aus; gib ihm `references/icp.md`, Segment, Region, Menge und die Ausschlussliste mit.
- **daniel-daten** bereinigt; für das Scoring gilt `icp.md`, nicht seine allgemeinen Segmentregeln.
- **tim-teamleiter** nutzt Modus C für den Wochenstand.
- Anschreiben und Briefe sind nicht Teil dieses Skills – er liefert Aufhänger und Entscheider dafür.
