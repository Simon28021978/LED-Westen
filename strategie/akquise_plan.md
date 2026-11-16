# Akquise-Plan Händler – heyReflect

Stand: 2026-11-16 · Status: Entwurf

## Zwei Zielgruppen, zwei Angebote
| Gruppe | Liste | Angebot | Absender |
|---|---|---|---|
| Inhabergeführte Läden (1–5 Filialen) | `daten/top10_erste_welle_2026-11-16.xlsx` | Startpaket [MOQ] Stück, Rohertrag pro Stück | Gründerin |
| Mittelgroße Filialisten (8–25 Filialen) | `daten/leads_fahrrad_mittelgross_2026-11-16.csv` | MBW 5.000 €, Verteilung auf Filialen | Gründerin |

## Ablauf je Lead (Pipeline-Stufen)
| Stufe | Was passiert | Wer | Automatisiert |
|---|---|---|---|
| 1 Recherche | Firma, GF, Anschrift, Sortiment | Rico/Daniel (Claude) | ja |
| 2 Brief | personalisierter Brief + Infoblatt per Post | Claude erzeugt PDF, Versand per Online-Briefdienst | weitgehend |
| 3 Nachfassen | Tag 7–10 nach Versand: Anruf mit Bezug auf den Brief oder zweiter Brief | du | Erinnerung automatisch |
| 4 Muster | kostenlose Musterweste bei Interesse | du | Statuswechsel |
| 5 Angebot | Konditionsblatt, ab hier E-Mail erlaubt (Händler hat reagiert) | du, Entwurf durch Claude | Entwurf |
| 6 Bestellung | Erstorder | – | – |
| 7 Nachorder | Tag 30/60: Abverkauf abfragen | du | Erinnerung automatisch |
| X Verloren | Grund notieren | du | – |

## Werkzeuge ohne CRM
1. **Google Sheet als Mini-CRM**: „heyReflect Akquise-Pipeline Händler“ im geteilten Laufwerk „Vertrieb“ (angelegt 16.11.2026, 20 Leads). Claude kann es direkt lesen und schreiben.
   Spalten: firma, segment, gruppe, geschaeftsfuehrung, anschrift, aufhaenger, stufe, brief_versendet_am, naechster_schritt, faellig_am, ergebnis, grund_verloren, notiz.
2. **Google Kalender**: Nachfass-Termine automatisch aus `faellig_am`.
3. **Wochenbericht** (geplante Aufgabe, z. B. Montag früh): Claude liest das Sheet und meldet: fällige Nachfassaktionen, offene Muster, Quote je Stufe.
4. **Briefe**: Claude erzeugt je Händler ein fertiges PDF aus Vorlage + Adressliste. Versand über einen Online-Briefdienst (Upload PDF → Druck, Kuvertierung, Porto). Anbieter auswählen und testen.
5. **Später CRM** (ab ca. 50 aktiven Leads): z. B. HubSpot Free. Sheet lässt sich importieren.

## Rhythmus
- Pro Woche: 10–15 Briefe raus, Nachfassaktionen der Vorwoche erledigen.
- Woche 1: Top 10 Inhaber + Platz 1–4 Mittelgroß.
- Ab Woche 2: Nachrücker; Rico recherchiert laufend 10–15 neue Leads pro Woche.

## Kennzahlen
- Antwortquote auf Brief, Quote Muster → Bestellung, Ø Erstorder in €, Nachorderquote.
- Nach 30 Briefen auswerten und Brief/Angebot anpassen.

## Recht (Kurzfassung, keine Rechtsberatung)
- Erstkontakt per Post: zulässig.
- Werbe-E-Mail ohne Einwilligung: unzulässig, auch B2B (UWG §7). Nach Antwort des Händlers: E-Mail ok.
- Anruf B2B: nur bei mutmaßlichem Interesse; Bezug auf den Brief hilft, bleibt aber Grauzone.

## Offene Punkte vor Start
- [ ] Konditionen (EK, MOQ, Staffel 2.500 / 5.000 €, Lieferzeit, Nachorder)
- [ ] Produktfotos → Infoblatt v2
- [ ] Brief V1 freigeben, Variante für Mittelgroße
- [ ] Online-Briefdienst wählen
- [x] Google Sheet anlegen
