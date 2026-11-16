# Vorschlag: Fit-Scoring und Pipeline-Forecast Mittelgroß

Stand: 16.11.2026 · Daniel · Status: Diskussionsgrundlage, nicht umgesetzt
Basis: `daten/leads_fahrrad_mittelgross_2026-11-16.csv` (10 Leads). Das Google Sheet habe ich nicht geöffnet, Spaltenvorschläge beziehen sich auf die im Auftrag genannten Spalten.

## 1. Fit-Scoring (0–20 Punkte)

| # | Kriterium | Skala | Gewicht | max |
|---|---|---|---|---|
| K1 | Filialen (trägt MBW 5.000 €?) | 3–4 = 1, 5–7 = 2, 8–25 = 3, <3 oder >25 = 0/1 | ×2 | 6 |
| K2 | Kindersortiment | 0 kein Beleg, 1 nur Kinderräder, 2 Kinderräder + Kinderzubehör oder Puky/woom belegt | ×2 | 4 |
| K3 | Westen-/Sicherheitsregal | 2 Westenkategorie belegt, 1 unbekannt/keine Treffer | ×1 | 2 |
| K4 | Entscheidungsweg | 2 inhaber-/familiengeführt, 1 GF bekannt, Eigentum unklar oder Beteiligung, 0 unbekannt | ×2 | 4 |
| K5 | Region | 2 Sitz Nord (SH/HH/HB/NI/MV), 1 Nord-Filialen, Sitz woanders, 0 sonst | ×1 | 2 |
| K6 | Briefadresse belastbar | 1 GF + Anschrift aus Impressum, 0 offen | ×2 | 2 |

Schwellen: **A ≥ 16, B 12–15, C ≤ 11**. Im Sheet: K1–K6 als Zahlenspalten, `fit_score = 2*K1+2*K2+K3+2*K4+K5+2*K6`, Klasse per `IFS`.
Unbekannt: K3 = 1 (neutral), weil „keine Westen im Shop“ sowohl Lücke als auch Desinteresse heißen kann. Bei K2, K4 und K6 ist Unbekannt = 0, weil das echte Lücken sind, die man vor dem Brief schließen kann. Das bisherige Feld `mbw_5000_realistisch` geht nicht ein, weil es fast nur aus der Filialzahl abgeleitet ist (sonst doppelt gezählt).

**Probelauf (Script, nur vorhandene Daten):**

| Neu | Bisher | Firma | Fil. | K1–K6 | Score | Klasse |
|---|---|---|---|---|---|---|
| 1 | 3 | Zweirad-Center Stadler | 22 | 3/2/2/2/1/1 | 19 | A |
| 2 | 2 | BIKE Market | 9 | 3/2/1/1/2/1 | 17 | A |
| 3 | 4 | Das RADhaus | 8 | 3/2/1/2/0/1 | 17 | A |
| 4 | 5 | Fahrrad Rachow | 4 | 1/2/2/2/2/1 | 16 | A |
| 5 | 1 | MEGA Bike | 15 | 3/1/1/2/2/0 | 15 | B |
| 6 | 6 | Bikesnboards | 9 | 3/1/1/2/0/1 | 15 | B |
| 7 | 7 | Hahne | 3 | 1/2/2/1/2/1 | 14 | B |
| 8 | 8 | my Boo (Küstenrad) | 17 | 3/0/1/1/2/1 | 13 | B |
| 9 | 9 | Edelhelfer | 5 | 2/2/1/1/0/1 | 13 | B |
| 10 | 10 | Wollesen | 3 | 1/1/1/2/2/1 | 13 | B |

Lesart: Platz 6–10 bleiben gleich. MEGA Bike fällt nur wegen der unbestätigten Briefadresse (Bot-Schutz); nach Handelsregister-Check 17 Punkte, A. Stadler steigt durch das Westenregal auf Platz 1, dort liegt aber Wowow für 11,99–18,99 € (Wettbewerb). Ohne K3 läge Stadler mit 18 trotzdem vorn. Rachow ist A trotz nur 4 Filialen, der MBW ist dort aber fraglich. Die Unterscheidung ist schwach (sechs Leads zwischen 13 und 15), weil alle 10 vorgefiltert sind und K2/K3 oft auf „unbekannt“ stehen.

## 2. Pipeline für den Forecast

| Stufe | Eintritt: was muss passiert sein | Austritt | p (Annahme) |
|---|---|---|---|
| 1 Recherche fertig | GF und Anschrift belegt (K6 = 1), Fit ≥ 12 | Brief ist raus | 2 % |
| 2 Brief versendet | Versanddatum `brief_am` | Reaktion oder 2. Kontakt ohne Antwort → X | 3 % |
| 3 Im Gespräch (statt „Nachgefasst“) | Entscheider hat reagiert oder Gespräch geführt (nur Anrufversuch reicht nicht) | Muster angefragt | 15 % |
| 4 Muster beim Händler | Zustellung bestätigt | Feedback + Mengen-/Preisfrage | 30 % |
| 5 Angebot | schriftliches Konditionsblatt mit Menge und Wert verschickt | Bestellung oder Absage | 50 % |
| 6 Bestellt | schriftliche Bestellung | – | 100 % |
| 7 Nachorder | zweite Bestellung (zählt eigener Wert, nicht in Erstorder-Forecast) | – | – |
| X Verloren | Absage oder 2 Kontakte ohne Reaktion | Grund in `verlustgrund` | 0 % |

Die Werte für p sind geschätzt und nicht gemessen, es gibt bisher null Briefe.

**Erwarteter Auftragswert:** `wert_erwartet = MAX(5000; filialen × westen_je_filiale × 20)`. Die Startannahme ist 25 Westen je Filiale (geschätzt). Nach dieser Formel liegen 7 von 10 Leads bei 5.000 €, MEGA Bike bei 7.500 €, my Boo bei 8.500 € und Stadler bei 11.000 €. Pipeline gesamt: 62.000 €. Gewichtet ergibt das in Stufe 1 1.240 €, wenn alle 10 in Stufe 2 sind 1.860 €. Ehrlich gesagt: Vor den ersten Gesprächen kommt kein belastbarer Forecast zustande.

**Erwartetes Abschlussdatum:** `abschluss_erwartet = stufe_seit + Restdauer` mit Restdauer Stufe 2 = 60 Tage, 3 = 45, 4 = 30, 5 = 14 (Annahme). Saisonalität: Das Akquisefenster ist Nov–Feb, Vororder im Frühjahr. Fällt das Datum nach dem 31.03.2027, wird es als „nächste Saison“ markiert und geht nicht in den Forecast 2027 ein.

**Spalten ins Sheet:** `filialen` (Zahl), K1–K6, `fit_score`, `fit_klasse`, `westen_je_filiale`, `wert_erwartet`, `p_stufe` (SVERWEIS auf eine Stufentabelle im Reiter Scorecard, damit die Werte zentral änderbar sind), `forecast_gewichtet`, `stufe_seit` (Datum des letzten Stufenwechsels, nötig für Durchlaufzeiten), `abschluss_erwartet`, `verlustgrund`.
**Ändern bzw. weg:** `auftragswert_eur` aufteilen in `wert_erwartet` (Plan) und `auftragswert_ist` (erst ab Stufe 6). Freitext in `notiz` nicht für Stufenlogik nutzen.

**Kalibrieren nach 10–20 Briefen:** 10–20 Fälle reichen für Quoten noch nicht. Deshalb geglättet: `p_neu = (Erfolge + p_alt × 10) / (Versuche + 10)`, also zählt die Annahme wie 10 fiktive Fälle. Je Übergang (2→3, 3→4, 4→5, 5→6) getrennt rechnen, Durchlaufzeiten aus `stufe_seit` als Median, `westen_je_filiale` aus den ersten Angeboten ersetzen. Fester Termin: nach 30 Briefen (wie im Akquise-Plan).

## 3. Entscheidungsfragen
1. **Region gegen Volumen:** Soll Nord (K5) stärker gewichtet werden (z. B. ×2)? Probelauf mit ×2 (max 22): Stadler bleibt mit 20 vorn, dahinter BIKE Market 19 und Rachow 18. Hahne steigt auf 16, Bikesnboards fällt auf Platz 7. Wer Nord klar vorziehen will, braucht mehr als ×2 oder einen festen Regionsfilter je Welle.
2. **MBW bei 3–4 Filialen:** Bleibt der MBW von 5.000 € fest, sodass Rachow, Hahne und Wollesen höchstens B werden, oder gibt es eine Staffel von 2.500 €, die den K1-Malus aufhebt?
3. **Wettbewerb im Regal:** Gilt ein vorhandenes Westenregal mit Billigware (Stadler: Wowow) als Plus (Kategorie etabliert) oder als Minus (Preisvergleich 18,99 € gegen 44,90 €)? Davon hängt K3 ab.
