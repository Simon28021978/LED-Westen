# Projekt: heyReflect – B2B-Vertrieb für LED-Westen

Stand: 20.11.2026. Diese Datei liest jede neue Session zuerst. Bei neuen Entscheidungen hier nachtragen.

## Wer wir sind
- Wir sind der Hersteller: heyReflect UG (haftungsbeschränkt), Babenkoppel 22, 22927 Großhansdorf. Gegründet 2017 von Lisa (Simons Frau), Vision: Kinder im Straßenverkehr sicherer machen.
- Ansprechpartner Vertrieb: Simon Schirrmacher, **simon@heyreflect.com**. Lisa: lisa@heyreflect.com.
- Ziel: schnell neue Handelspartner gewinnen (Fahrrad, Outdoor, Laufen, Kinderausstattung). Gelistet u. a. bei Globetrotter und Fahrradläden im Raum Hamburg und im Kreis Vechta.

## Produkte und Preise (Broschüre HW 2026/27, EKP netto / UVP brutto)
| Produkt | EKP | UVP |
|---|---|---|
| LED Warnweste Kind (Gr. S–L, 86/92–146) | 23,89 € | 44,90 € |
| LED Warncape Kind (gelb, gelb/pink, gelb/petrol, inkl. Patch) | 23,67 € | 44,90 € |
| LED Sportweste (gelb, schwarz) | 27,67 € | 54,90 € |
| LED Freizeitweste (gelb, schwarz) | 29,89 € | 59,90 € |
| LED Strap (gelb, schwarz) / voll reflektierend | 14,94 € / 16,22 € | 27,90 € / 29,90 € |
| LED Kinderwagenstrap | 16,70 € | 34,90 € |
| Klett-Patch | 1,83 € | 3,90 € |
- Kalkulationsfaktor für Händler nur ca. 1,9–2,1 → Rabatte vorsichtig; lieber Rückgabe/Umtausch, Versandfreiheit, Display als Preisnachlass.
- Bestseller: Kinderwesten und Capes.
- Norm-Angaben laut Broschüre: PSA nach (EU) 2016/425, EN ISO 13688, EN 17353 bzw. EN 13356 (nicht „EN ISO 13356“, nicht „EU Norm“). Nur so behaupten, wie in der Broschüre belegt.
- Broschüre (korrigiert, mit neuem Deckblatt): 5,8 MB – zu groß für den Gmail-Connector (Limit ca. 3 MB). Simon hängt sie in Entwürfen selbst an.
- Mindestmengen, Lieferzeit, Versandkosten: noch nicht festgelegt („reicht Simon bei Interesse nach“).

## Systeme und Links
- **Akquise-Pipeline** (Google Sheet, geteiltes Laufwerk „Vertrieb“): „heyReflect Akquise-Pipeline Händler“, ID `1rQTJ1LH9NKALsuLXtXC_GcP3m-my2wwPm03MEWmuZxU`
  - Blätter: Scorecard (nur Formeln, nicht überschreiben), Inhaber, Mittelgroß, Outdoor, Dashboard-Daten (nur Formeln – führt die drei Listen zusammen).
  - Gebietsschema de_DE: Formeln mit Semikolon. Datums-Spalten sind validiert (TT.MM.JJJJ).
  - Stufen (Auswahlliste): 1 Recherche fertig · 2 Brief versendet (gilt auch für E-Mail) · 3 Im Gespräch · 4 Muster beim Händler · 5 Angebot · 6 Bestellt · 7 Nachorder · X Verloren (Absage oder 2 Kontakte ohne Reaktion).
  - Spalten Mittelgroß: S stufe, T stufe_seit, U brief_am, V naechster_schritt, W faellig_am, AF notiz. Inhaber: M stufe, N brief_am, O naechster_schritt, P faellig_am. Outdoor (seit 25.11. umsortiert): A firma, B stufe, C brief_am, D naechster_schritt, E faellig_am, F segment, G ort, H filialen, I geschaeftsfuehrung, J strasse*, K plz*, L website, M kinder_sortiment, N westen_im_sortiment, O aufhaenger, P quelle*, Q pruefhinweis, R notiz, S auftragswert_eur (* ausgeblendet). Segment „6 Filialist Rad/Lauf/Outdoor/Sport“ = Ricos Filialisten-Liste vom 25.11. Zeilen nicht sortieren (Kalendertermine nennen Zeilennummern) – zum Ordnen den Filter nutzen.
  - Ausgeblendet in Inhaber: G/H (Adresse); in Mittelgroß: G/H (Adresse), K–P (Einzelscores K1–K6). Formeln bleiben unberührt.
  - Fahrrad Rachow steht in Inhaber und Mittelgroß – **nur in Mittelgroß pflegen**.
- **Vertriebs-Dashboard** (claude.ai, angepinnt): https://claude.ai/artifact/JYetdnHdbagqpjmxJvDD1a – Reiter Aktivität und Sales, liest live aus „Dashboard-Daten“. Link auch in Scorecard!E1 und als Doc im Drive „Vertrieb“.
- **Outdoor-Leads** auch als eigene Datei im Drive „Vertrieb“ (Archiv-Kopie) – gepflegt wird nur das Blatt „Outdoor“.
- **Kalender**: Nachfass-Termine als Einzeltermine mit Händlerliste in der Beschreibung.
- **Gmail-Connector**: muss mit **simon@heyreflect.com** verbunden sein (prüfen: `list_drafts` → `sender`). Nie vom privaten googlemail-Konto aus Akquise machen. Der Connector schreibt Links in Entwürfen auf google.com/url um → Simon prüft Links vor dem Versand.

## Ablauf Akquise (verbindlich)
1. Rico recherchiert (nur mit Quelle, ICP beachten) → `recherche/`.
2. Daniel prüft ICP-Fit, Dubletten und Doppelansprache gegen Pipeline und `in:sent` → `daten/`.
3. Claude legt Gmail-Entwürfe an (nie direkt senden ohne Simons ausdrückliches „senden“).
4. Simon hängt Broschüre an und versendet.
5. Nach „raus“: Pipeline-Stufe 2, Datum, nächster Schritt, Fälligkeit +7 Tage, Kalendertermin.
6. Nachfassen per Telefon; 2 Kontakte ohne Reaktion → X Verloren.

## ICP
Verbindlich: `vertrieb/icp.md` (Absatzpotenzial vor Erreichbarkeit; mind. 2 belegte Potenzial-Signale; kleine Nischen-Einzelläden raus). Ältere Fassung: `strategie/icp.md`. Scoring Mittelgroß: `strategie/scoring_mittelgross.md`.

## Regeln
- Keine erfundenen Firmen, Ansprechpartner, E-Mails oder Telefonnummern. Jede Angabe mit Quelle (URL). Keine E-Mail-Adressen raten (z. B. vorname.nachname@).
- E-Mail nur an allgemeine Firmenadressen (info@, shop@ …) oder Adressen, die der Händler selbst genannt hat.
- Recht: E-Mail-Werbung an Firmen braucht nach UWG §7 Abs. 2 Nr. 2 eine vorherige Einwilligung; Simon hat sich bewusst für Mails an info@-Adressen entschieden. Anruf bei Firmen mit mutmaßlicher Einwilligung zulässig, Brief zulässig. Widersprüche sofort in der Pipeline vermerken und nie wieder anschreiben.
- Keine Zugangsdaten oder API-Keys im Repo.
- Ergebnisse im Repo speichern, committen, pushen. Standard-Branch ist `main`.

## Stand 20.11.2026
- Mittelgroß angeschrieben (19./20.11.): Rachow, Stadler, Hahne, MEGA Bike, Wollesen (info@), Das RADhaus, my Boo/Küstenrad (jonas@my-boo.de). Nachfassen 26.11. (6) und 27.11. (Küstenrad).
- Mailaktion inhabergeführte Läden: 14 Mails am 20.11. versendet, Unterwegs-Zentrale am 19.11. – Details `vertrieb/mailaktion_inhaber_uebergabe.md`. Nachfassen 26./27.11.
- Noch offen: 10 alte Entwürfe im googlemail-Konto löschen (Simon).

## Nächste Schritte
1. Nachfassen 26./27.11. per Telefon (Entscheider klären, Muster anbieten).
2. Große Outdoor-Händler: Unterwegs, Bergfreunde, Zippel's – erst Einkauf klären, dann Pilot anbieten (Test in 2–3 Filialen, Vororder 27/28).
3. Nachfass-Mail mit konkretem Angebot: „Testpaket Winter“ (12 Teile, ca. 285 € EK, versandfrei, Umtausch/Rückgabe bis 28.02.27, Frist 12.12.) – Konditionen (Rückgabe, Versandkosten, Lieferzeit) muss Simon noch bestätigen.
4. Später: Sport 2000 / Intersport (Saison 27/28), Reitsport, Hundebedarf, Kitas/Schulen/Verkehrswacht.

## Ordner
- `recherche/` Rohrecherchen (Rico) · `daten/` bewertete Listen, Freigaben (Daniel) · `strategie/` ICP, Scoring, Akquiseplan · `vertrieb/` Anschreiben, Briefe, Flyer, ICP, Mailaktionen · `briefings/` Notizen · `.claude/agents/` Tim, Rico, Daniel, Gabi

## Stil
Deutsch, kurz, Stichpunkte, norddeutsch-nüchtern, keine Floskeln, ehrlich bei Lücken und Risiken. Maximal 2–3 Rückfragen.
