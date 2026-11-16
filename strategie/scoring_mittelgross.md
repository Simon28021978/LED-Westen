# Scoring und Forecast – Mittelgroße Händler

Stand: 2026-11-16 · Status: beschlossen (Startversion, nach 30 Briefen kalibrieren)
Grundlage: Vorschläge von Rico und Daniel (`briefings/scoring_*`), Entscheidungen Vertrieb vom 16.11.2026.
Umgesetzt im Google Sheet „heyReflect Akquise-Pipeline Händler“, Reiter „Mittelgroß“ und „Scorecard“.

## Entscheidungen
- **Region Nord doppelt gewichtet:** örtlich näher, persönlich erreichbar.
- **Mindestbestellwert gestaffelt:** 2.500 € bei bis zu 5 Filialen, 5.000 € ab 6 Filialen.
- **Reflexwesten im Regal = Plus:** Thema ist beim Händler platziert, LED ist die Stufe darüber.

## Fit-Score (max. 22)
`fit = 2·K1 + 2·K2 + K3 + 2·K4 + 2·K5 + 2·K6`

| | Kriterium | Punkte |
|---|---|---|
| K1 | Filialen (Formel) | 8–25 = 3 · 3–7 = 2 · unter 3 = 0 |
| K2 | Kindersortiment | 2 = Puky/woom oder Kinderräder + Kinderzubehör belegt · 1 = nur Kinderräder · 0 = kein Beleg |
| K3 | Westen im Regal | 2 = Westen/Westenkategorie belegt (auch Reflektor) · 1 = unbekannt/keine |
| K4 | Entscheidungsweg | 2 = inhaber-/familiengeführt · 1 = GF bekannt, Eigentum unklar/Beteiligung · 0 = unbekannt |
| K5 | Region | 2 = Sitz Nord (SH/HH/HB/NI/MV) · 1 = Filialen im Norden, Sitz woanders · 0 = sonst |
| K6 | Briefadresse | 1 = GF und Anschrift aus Impressum/Register belegt · 0 = offen |

Klassen: **A ≥ 18 · B 15–17 · C ≤ 14**

### Ergebnis 16.11.2026
| Rang | Firma | Score | Klasse | MBW | Wert erwartet |
|---|---|---|---|---|---|
| 1 | Fahrrad Rachow | 20 | A | 2.500 € | 2.500 € |
| 2 | Zweirad-Center Stadler | 20 | A | 5.000 € | 11.000 € |
| 3 | BIKE Market | 19 | A | 5.000 € | 5.000 € |
| 4 | Hahne Fahrrad | 18 | A | 2.500 € | 2.500 € |
| 5 | MEGA Bike | 17 | B (A nach Register-Check) | 5.000 € | 7.500 € |
| 6 | Fahrrad Wollesen | 17 | B | 2.500 € | 2.500 € |
| 7 | Das RADhaus | 17 | B | 5.000 € | 5.000 € |
| 8 | Bikesnboards | 17 | B | 5.000 € | 5.000 € |
| 9 | Küstenrad (my Boo) | 15 | B | 5.000 € | 8.500 € |
| 10 | Edelhelfer | 13 | C | 2.500 € | 2.500 € |

## Forecast
- `wert_erwartet = MAX(MBW; Filialen × 25 Westen × 20 €)` – 25 Westen je Filiale und 20 € EK sind Annahmen.
- `forecast = wert_erwartet × p(Stufe)`; p und Restdauer stehen zentral in der Stufentabelle (Scorecard G3:J11).
- `abschluss_erwartet = stufe_seit + Restdauer`. Forecast der Saison zählt nur Abschlüsse bis 31.03.2027.

| Stufe | p (Annahme) | Restdauer | Eintritt, wenn … |
|---|---|---|---|
| 1 Recherche fertig | 2 % | 120 T | GF und Anschrift belegt |
| 2 Brief versendet | 3 % | 60 T | Brief ist raus |
| 3 Im Gespräch | 15 % | 45 T | Entscheider hat reagiert (Anrufversuch reicht nicht) |
| 4 Muster beim Händler | 30 % | 30 T | Zustellung bestätigt |
| 5 Angebot | 50 % | 14 T | Konditionsblatt mit Menge und Wert verschickt |
| 6 Bestellt | 100 % | – | schriftliche Bestellung |
| 7 Nachorder | 100 % | – | zweite Bestellung |
| X Verloren | 0 % | – | Absage oder 2 Kontakte ohne Reaktion |

Stand 16.11.: Pipeline 52.000 €, gewichtet 1.040 €. Vor den ersten Gesprächen ist das eine Rechenhilfe, keine Prognose.

## Pflege im Sheet
- Grün = von Hand: stufe, stufe_seit (Datum jedes Stufenwechsels), brief_am, naechster_schritt, faellig_am, auftragswert_ist, verlustgrund.
- Blau = Bewertung von Hand (K2–K6, 0–2).
- Grau = Formel, nicht überschreiben.

## Kalibrieren (nach 30 Briefen)
- Quoten je Übergang geglättet: `p_neu = (Erfolge + p_alt × 10) / (Versuche + 10)`.
- Restdauer als Median aus stufe_seit.
- Westen je Filiale aus den ersten Angeboten ersetzen.

## Offen vor dem Brief
- MEGA Bike: GF und Anschrift im Handelsregister prüfen (K6).
- woom-/Puky-Händlersuche für alle 10 (K2), Verbund-Zugehörigkeit prüfen (K4).
