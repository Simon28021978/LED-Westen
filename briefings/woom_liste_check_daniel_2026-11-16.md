# Check woom-Händlerliste – Daniel, 16.11.2026

Eingang: `daten/extern/woom_Haendler_Deutschland_Groessenranking.csv` (+ .xlsx, inhaltlich identisch, 0 abweichende Zellen), Methodik-Datei.
Ausgabe: `daten/woom_haendler_firmen_2026-11-16.csv` (144 Firmen). Keine Webrecherche, alle Zahlen per Skript.

## Kernzahlen
- 167 Zeilen = Standorte. Quelle nennt 246 woom-Händler DE, erfasst sind 67,9 % (79 fehlen).
- Nach Zusammenfassen: 144 Firmen (23 Zeilen zusammengeführt, 12 Firmen mit mehr als einem Standort in der Liste).
- Größenklasse (Basis: max. aus Filialen laut Liste und Standorten in Liste): 8 mittelgroß (3–25), 136 klein (1–2), 0 groß.
- Bereits in unseren Listen: 2 (Bikes 'n Boards = Bikesnboards GmbH; radschlag GmbH = Radschlag Fahrradhandel GmbH, Bremen).
- Neu und mittelgroß: 7.

## Neue Kandidaten mittelgroß
| Firma | Standorte in Liste | Filialen laut Liste | Land | Hinweis |
|---|---|---|---|---|
| Zweirad Joos | 6 | 1 (falsch) | BW | 6 Namensvarianten, Quelle zählt jede als Einzelhändler |
| Zweirad-Center Durach | 1 | 3 | BW | 2 Filialen fehlen in der Liste |
| Zweirad-Karberg | 1 | 3 | MV | einziger mittelgroßer im Norden |
| Zweirad-Profi Bernau | 1 | 3 | BB | |
| 2-Rad Dosch | 1 | 3 | BW | |
| TransVelo Fahrräder | 3 | 3 | BW | 3 Namensvarianten |
| 2-Cycle | 2 | 3 | BW | keine Services angegeben |

Alle 7 liegen am unteren Rand (3–6 Standorte). Bei 250 Westen wären das rund 40–80 je Standort – bei Mindestbestellwert 5.000 € eher knapp. Rico muss Filialzahl, Sitz und GF belegen.

## Probleme der Liste
1. **Abdeckung**: Erfasst 9 Länder (BW 53, BY 50, HE 22, NI 22, MV 5, BB 5, BE 5, HH 3, HB 2 Zeilen). Es fehlen u. a. **SH komplett**, NRW, RP, SL, SN, ST, TH (Abruf nach ~50.000 Zeichen abgeschnitten). Norden: nur 32 Firmen (NI 22, MV 5, HH 3, HB 2, SH 0).
2. **Auch in erfassten Ländern lückenhaft**: BIKE Market GmbH (Rostock, laut unserer Liste 81 woom-Produkte im Shop) fehlt. Ob er auf marktplatz.bike gelistet ist, ist offen.
3. **Filialzahlen unzuverlässig**: zu niedrig bei Zweirad Joos (1 statt 6 Zeilen), Fahrbar Bikes und FXsports (je 1 statt 2). Zu hoch bzw. nicht nachvollziehbar bei 9 Firmen, bei denen weniger Zeilen als Filialen vorhanden sind. „Brand“ (Euerdorf BY und Celle NI, je „2 Filialen“) ist vermutlich nur Namensgleichheit – getrennt geführt.
4. **Bikes 'n Boards**: 8 Zeilen, davon 2 in Hessen (Butzbach, Wetzlar). Unsere Liste führt 9 Filialen, nur Region Stuttgart. Möglicherweise ist es eine andere Firma gleichen Namens – prüfen.
5. **Unsichere Namensgleichheiten**, nicht zusammengeführt: Conrad II / CONRAD Fahrradladen (Berlin), Fahrwerk (Lingen) / Fahrwerk Timmer (Meppen), Fahrrad Riebold (München) / Fahrradhandlung Riebold (Bad Hersfeld).
6. **Felder**: PLZ alle 5-stellig, keine Adress- oder Name+Ort-Dubletten. Services leer in 18 Zeilen. Keine Website, keine Kontaktdaten, keine Quelle je Zeile – für die Pipeline muss jede Firma nachbelegt werden. Tippfehler „2Rad Center Bad Waldseee“.

## Taugt der Größen-Score für unser Scoring?
Nein, nur die Filialzahl ist als grober Hinweis brauchbar. Der Score rechnet sich nachvollziehbar (167 von 167 Zeilen stimmen mit der Herleitung überein), misst aber kaum Größe: 134 von 167 Zeilen haben 1 Filiale, dort entsteht die Spreizung nur aus Wörtern im Namen (GmbH, Center, Welt) und angehakten Services. Median 18, Maximum 62 (Bikes 'n Boards). Die Filialkomponente ist wegen Punkt 3 fehlerhaft. Empfehlung: Score nicht übernehmen, Filialzahl nur als Hinweis nutzen und mit eigener Belegung (Website, Handelsregister) in `p_volumen` einfließen lassen. Der eigentliche Wert der Liste: Alle 144 Firmen führen woom und damit Kinderräder – das ist ein belegtes Signal für Kinder- bzw. Familiensortiment (ICP).
