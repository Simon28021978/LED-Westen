---
name: led-prospect-research
description: Prospect-Recherche für das LED-Westen-B2B-Geschäft – ICP bestimmen und schärfen (Wiederverkäufer und Direktabnehmer getrennt), Zielfirmen per Web-Recherche finden und belegen, gegen das ICP bewerten und Ergebnisse zu Segment-Insights und Top-Leads verdichten; liest und schreibt Leadlisten auch in Google Sheets/Drive. Nutze diesen Skill immer, wenn es um LED-Westen-Leads, Zielkunden, ICP, Zielgruppen, Marktsegmente, Prospect-Listen, „wen sollen wir anschreiben“, Lead-Auswertung oder eine Zusammenfassung bisheriger Recherche geht – auch wenn der Begriff „ICP“ nicht fällt, und auch als Arbeitsgrundlage für die Agenten Tim, Rico und Daniel.
---

# LED-Westen: ICP & Prospect-Recherche

Ziel: Aus einer Hypothese über gute Kunden wird eine belegte, priorisierte Liste von Firmen, die das Team (Rico, Daniel, Simon) direkt anschreiben kann – und aus den Ergebnissen lernt das ICP mit.

Der Skill hat drei Modi. Erkenne aus der Anfrage, welcher gebraucht wird; oft sind es mehrere nacheinander.

| Modus | Auslöser | Ergebnis |
|---|---|---|
| A. ICP | „ICP bestimmen/schärfen“, „wer ist unser Zielkunde“, kein `daten/icp.md` vorhanden | `daten/icp.md` |
| B. Recherche | „finde Leads/Firmen“, Segment + Region genannt | `daten/recherche_<segment>_<region>_YYYY-MM-DD.csv` |
| C. Zusammenfassung | „fasse zusammen“, „was haben wir“, „wen zuerst anschreiben“ | Kurzbericht im Chat (+ optional `daten/zusammenfassung_YYYY-MM-DD.md`) |

Wenn `daten/icp.md` fehlt und Modus B gefragt ist: erst Modus A kurz ausführen (Hypothese anlegen), dann recherchieren. Ohne ICP gibt es keine nachvollziehbare Bewertung.

## Grundsätze (gelten in allen Modi)

- **Beleg vor Menge.** Jede Angabe zu einer Firma braucht eine Quell-URL. Lieber 15 belegte Leads als 50 geratene – eine falsche Ansprache kostet Glaubwürdigkeit, die ein kleines Geschäft nicht übrig hat.
- **Keine erfundenen Kontaktdaten.** Keine geratenen E-Mails (info@…), Telefonnummern oder Namen. Personennamen nur, wenn sie öffentlich auf der Firmen-/Vereinsseite stehen. Keine Privatpersonen.
- **Hypothese ≠ Fakt.** Das ICP ist anfangs eine begründete Annahme. Kennzeichne Annahmen als solche und halte fest, was sie bestätigen oder widerlegen würde.
- **Zahlen per Skript.** Zählungen, Verteilungen und Scores werden mit `scripts/auswertung.py` (oder eigenem Code) berechnet, nie geschätzt.
- **Ehrlich berichten.** Sind Ergebnisse dünn oder ein Segment unergiebig, sag das klar – das ist eine wertvolle Erkenntnis, kein Misserfolg.
- **Kostenfrei.** Recherche nur über Websuche und öffentliche Websites. Keine kostenpflichtigen Datenanbieter (z. B. Lusha), außer der Nutzer verlangt es ausdrücklich.

## Modus A – ICP bestimmen oder schärfen

1. Prüfe, ob `daten/icp.md` existiert.
   - **Nein:** Lege es aus `references/icp-hypothese.md` an (Vorlage mit zwei ICPs: H = Wiederverkäufer, D = Direktabnehmer). Passe an, was der Nutzer an Kontext liefert (Produkt, Preis, Region, Mindestmenge).
   - **Ja:** Lies es und schärfe es mit neuen Belegen (Recherche-Ergebnisse, Antworten von Prospects, Feedback). Erhöhe die Versionsnummer und ergänze das Änderungsprotokoll unten in der Datei.
2. Jedes ICP enthält: Segmente, Firmografie (Größe, Region), Bedarfsauslöser, Kaufrolle, Ausschlusskriterien, Scoring-Kriterien, offene Annahmen mit Prüfweg.
3. Fehlen entscheidende Infos (z. B. Zielregion, Preisniveau/Marge, Mindestabnahme), stelle maximal 2–3 Rückfragen oder triff eine benannte Annahme.
4. Gib im Chat nur die Änderungen bzw. die 5 wichtigsten Punkte aus, nicht die ganze Datei.

## Modus B – Recherche nach ICP

1. **Auftrag klären:** Segment(e), Region, Zielmenge. Fehlt etwas → Annahme treffen und oben im Ergebnis nennen (Default: 15 Leads, ein Segment, Region aus `daten/icp.md`).
2. **Suchen:** Nutze die Suchwege aus `references/suchwege.md` für das Segment. Kombiniere Branchenbegriff + Ort; nutze Verbände, Veranstaltungskalender und Händlerverzeichnisse als Sprungbrett, nicht als Endquelle.
3. **Verifizieren:** Öffne für jeden Kandidaten die eigene Website (Impressum, Über uns, Kontakt, Termine). Nimm nur auf, wer existiert und aktiv ist (aktuelle Angebote/Termine 2025/2026).
4. **ICP-Signale erfassen:** Notiere konkret belegte Bedarfsauslöser (z. B. „Radkurierflotte, Lieferung bis 22 Uhr“, „Nachtlauf im November mit 800 Startern“, „führt Warnwesten-Sortiment“). Diese Signale sind der Kern der späteren Ansprache.
5. **Bewerten:** Fit-Score 0–10 nach den Kriterien in `daten/icp.md`, Priorität A (8–10) / B (5–7) / C (0–4). Jede A-Priorität bekommt einen Satz Begründung.
6. **Dubletten prüfen:** Vor dem Schreiben gegen vorhandene Dateien in `daten/` (und das Google Sheet, falls genutzt) abgleichen – gleiche Domain = Dublette.
7. **Speichern:** CSV im Format aus `references/datenformat.md`. Überschreibe keine bestehende Datei (`_v2`, `_v3` anhängen).

## Modus C – Zusammenfassen

1. Lies alle relevanten CSVs aus `daten/` (bzw. das Google Sheet).
2. Führe `python .claude/skills/led-prospect-research/scripts/auswertung.py daten/<datei>.csv [weitere.csv]` aus. Das Skript liefert Gesamtzahl, Dubletten über Dateien hinweg, Verteilung nach ICP-Typ, Segment, Priorität, Region sowie Datenlücken.
3. Interpretiere die Zahlen. Bericht im Chat, knapp in Bulletpoints:
   - **Bestand:** Leads gesamt, A/B/C, je ICP-Typ und Segment
   - **Top 5–10 zum Anschreiben:** Firma, Segment, konkreter Aufhänger (Signal), Quelle
   - **Erkenntnisse:** welches Segment ergiebig war, welche ICP-Annahme sich bestätigt oder wackelt
   - **Lücken:** fehlende Rollen, unbelegte Felder, unergiebige Suchwege
   - **Nächste Schritte:** max. 3, konkret (z. B. „Segment Lieferdienste Hamburg vertiefen“, „ICP D: Mindestgröße auf 5 Fahrer anheben“)
4. Ergibt sich eine ICP-Erkenntnis, biete an, `daten/icp.md` zu aktualisieren (Modus A).

## Google Sheets / Drive

Nur nutzen, wenn der Nutzer ein Sheet nennt oder darum bittet. Lade die Tools bei Bedarf per ToolSearch (`Google_Sheets`, `Google_Drive`).
- **Lesen:** Datei per Drive-Suche finden, Werte per `get_values` lesen, lokal als CSV ablegen, dann wie gewohnt auswerten.
- **Schreiben:** Nur anhängen (`append_values`), nie bestehende Zeilen überschreiben oder löschen. Spaltenreihenfolge wie in `references/datenformat.md`. Vor dem ersten Schreiben in ein Sheet kurz bestätigen lassen, welches Sheet und welcher Tab.

## Zusammenspiel mit dem Agenten-Team

- **rico-recherche** kann Modus B ausführen; gib ihm Segment, Region, Menge und den Pfad zu `daten/icp.md` mit.
- **daniel-daten** bereinigt und bewertet; das ICP in `daten/icp.md` ersetzt seine groben Segment-Annahmen beim Scoring.
- **tim-teamleiter** nutzt Modus C für seinen Abschlussbericht.
- Für die eigentliche Ansprache (E-Mail-Entwürfe) ist dieser Skill nicht zuständig – er liefert die Aufhänger dafür.
