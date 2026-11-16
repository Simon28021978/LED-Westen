# Check externe woom-Händlerliste (Quellen und Inhalt)
Rico, 16.11.2026. Geprüft: `daten/extern/woom_Haendler_Deutschland_Groessenranking.csv` (167 Zeilen) und `woom_Haendler_Methodik.txt`. Datenstruktur prüft Daniel.
Einschränkung: WebFetch war für marktplatz.bike und woom.com gesperrt (Domain nicht freigegeben). Alles unten stützt sich nur auf WebSearch und Verzeichnisseiten, Händler-Websites konnten nicht direkt geöffnet werden.

## 1. Quelle
- **marktplatz.bike:** Die Suche liefert keinen einzigen Treffer zu dieser Domain. Betreiber, Stand und Vollständigkeit sind **nicht belegt**. Sicher ist nur, dass laut Methodik dort 246 woom-Händler stehen und davon 167 erfasst sind.
- **woom.com:** Die Navigation von woom.com führt eine „Händlersuche“ (laut Snippets auf pedali.de/marke/woom und woom.com/de_AT). Das ist die Primärquelle und der bessere Weg. Ob sie für DE vollständig ist und ob sie Händlerstufen ausweist: **nicht belegt**, weil kein Abruf möglich war.
- Woom verkauft in DE auch über Fahrrad-XXL (fahrrad-xxl.de/marken/woom). Fahrrad-XXL steht nicht in der Liste. Die Liste bildet also offenbar nur die Händler auf dem Marktplatz ab, nicht alle woom-Händler.

## 2. Stichprobe (die Einträge mit den meisten „Filialen“)
| Händler (Liste) | Liste | Befund | Quelle |
|---|---|---|---|
| Bikes 'n Boards | 8 | Existiert. Eigene Angabe laut Snippet: 11 Standorte, dazu die Bikes'n Boards NRW GmbH (Köln) und ein Cube-Store Haiger. Die Butzbach-Adresse weicht ab (Orbea: Philipp-Reis-Str. 9). Böblingen ist nicht bestätigt. GmbH, privat geführt, Inhaber nicht belegt | pedali.de/haendler/bikes-'n-boards; koeln.de/branchen/eintrag/77203; implisense.com (Bikesnboards GmbH) |
| Zweirad Joos | 6 Zeilen à 1 | Ist **ein** Unternehmen (Zweirad Joos GmbH & Co. KG) mit Radolfzell, Konstanz/Reichenau, Gottmadingen, Immenstaad und Ravensburg. Die Liste zählt das als Einzelhändler, der Score ist zu niedrig | ebike-24.com Joos_Magazin_2026.pdf; mileway.com Pressemitteilung; indeed.de |
| Zweirad-Center Durach | 3 | Nur Isny belegt. 2 weitere Filialen nicht belegt | pedali.de |
| Zweirad-Karberg (MV) | 3 | Nur Waren, Lange Str. 46 belegt (Meisterbetrieb seit 1929, Verleih). 3 Filialen nicht belegt | off-to-mv.com; pedali.de |
| Zweirad-Profi Bernau | 3 | Nur ein Laden belegt, Adresse Berliner Str. **69** (Liste: 65). Zusammenhang mit dem Zweirad-Profi Berlin ist offen | bikes.de/haendlerverzeichnis/brandenburg |
| TransVelo | 3 | Passt ungefähr: Reutlingen, Stuttgart und Tübingen, dazu ein Cube Store. GmbH | werkenntdenbesten.de/e/26268186 |
| 2-Rad Dosch | 3 | Nur Buchen belegt | pedali.de |
| 2-Cycle | 3 (2 Zeilen) | 2 Standorte belegt (Freiburg und Todtnau), 2-Cycle GmbH | 2-cycle.de/en/pages/uber-uns |
| Brand | 2 | **Fehler:** Euerdorf (BY) und Celle (NI) sind vermutlich zwei verschiedene Firmen mit gleichem Namen. Celle = Brand GmbH | pedali.de/haendler/brand-celle-neuenhaeusen |

Bewertung: Die Spalte „Filialen“ ist nicht verlässlich. Sie zählt nur Einträge auf dem Marktplatz, teils sogar nur gleiche Namen. Sie ist mal zu hoch (Karberg, Bernau, Dosch, Brand), mal zu niedrig (Joos, Bikes 'n Boards). Echte Ketten oder Verbünde wie Fahrrad-XXL, Megabike oder Küstenrad fehlen. Im Ergebnis gibt es in der Liste **wahrscheinlich nur 2 bis 3 Händler mit 3 bis 25 echten Filialen** (Bikes 'n Boards, Zweirad Joos, eventuell TransVelo), und alle liegen im Süden.

## 3. Lücken SH, HH, MV
- Nord-Einträge in der Liste: HH 3 (Max Lange, Vélo 54, cult.bike), MV 5, HB 2, NI 22, SH 0. Laut Liste haben fast alle 1 Filiale. Ausnahmen sind Karberg mit 3 (nicht belegt) sowie Schriewer und Brand Celle mit je 2 (bei Brand falsch zusammengezählt).
- Wege: (a) woom-Händlersuche nach PLZ-Bereichen 2xxxx und 17xxx–19xxx abfragen. Dafür muss woom.com freigegeben werden oder jemand fragt manuell ab. (b) bikes.de-Händlerverzeichnis SH (17 Händler, bikes.de/haendlerverzeichnis/schleswig-holstein). (c) Für die Zielgröße 3–25 Filialen gar nicht über woom gehen, sondern direkt Filialisten im Norden prüfen, etwa Küstenrad (laut Trek-Storefinder 8+ Standorte in SH) und Megabike (laut pedali.de etwa 15 Standorte in SH/HH). Beides ist **noch nicht** auf den eigenen Websites geprüft.

## 4. Fazit
- Als Basis für **mittelgroße** Prospects taugt die Liste **nicht**. Sie ist ein Verzeichnis kleiner woom-Fachhändler, überwiegend mit einer Filiale und überwiegend aus dem Süden. Der Größen-Score beruht auf fehlerhaften Filialzahlen.
- Brauchbar ist sie höchstens als Ergänzung für den Segment-Fit Kinder/Familie (ICP-Entwurf). Ein woom-Händler hat nachweislich Kindersortiment.
- Vor der Nutzung nachrecherchieren: echte Filialzahl je Händler auf der eigenen Website (Impressum, Standortseite), die Rechtsform und ob inhabergeführt oder Kette/Verbund, die Adressen (2 Abweichungen in 9 Proben) und Gleichnamige trennen (Brand). Zusätzlich die Mindestbestellung von 5.000 € gegen die Ladengröße prüfen. Bei Händlern mit einer Filiale ist das nicht belegt realistisch.
- Für den Norden ist eine eigene Filialisten-Recherche (SH, HH, MV) sinnvoller als die Vervollständigung dieser Liste.
