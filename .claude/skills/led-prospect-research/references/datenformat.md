# Datenquellen und Formate

## Bestehende Google Sheets (Hauptquelle)

| Sheet | ID | Tabs |
|---|---|---|
| heyReflect Akquise-Pipeline Händler | `1rQTJ1LH9NKALsuLXtXC_GcP3m-my2wwPm03MEWmuZxU` | Scorecard, Inhaber, Mittelgroß, Outdoor, Dashboard-Daten |
| Leads – Fördervereine Grundschulen Hamburg | `1Hq4N1wW_ArexoiA8PI53aJtlcn8satLBaqKTbaZcce0` | Pipeline, Details & Recherche |

Die Scorecard und Dashboard-Daten werden automatisch aus den Listen berechnet – dort nie schreiben.

**Pipeline-Stufen (Händler):** 1 Recherche fertig · 2 Brief versendet · 3 Im Gespräch · 4 Muster beim Händler · 5 Angebot · 6 Bestellt · 7 Nachorder · X Verloren
**Status (Fördervereine):** offen · angeschrieben · (Antwort) · raus

## Neue Recherche-Ergebnisse (CSV im Repo)

Datei: `daten/recherche_<segment>_<region>_YYYY-MM-DD.csv`, UTF-8, Semikolon, Kopfzeile. Spalten so gewählt, dass sie 1:1 in den passenden Tab kopiert werden können.

**Händler (H)**
```
firma;segment;ort;filialen;geschaeftsfuehrung;strasse;plz;website;kinder_sortiment;westen_im_sortiment;K1_filialen;K2_kinder;K3_westen;K4_entscheider;K5_nord;K6_adresse;fit_score;fit_klasse;aufhaenger;quelle;pruefhinweis;stufe
```
`stufe` = „1 Recherche fertig“. Aussortierte Leads mit Grund in `pruefhinweis` behalten (z. B. „aussortiert: Einzelladen – zu wenig Volumen“), damit niemand sie erneut recherchiert.

**Fördervereine (F)**
```
foerderverein;schule;schultyp;bezirk;schulstrasse;ansprechpartner;email_haupt;email_alternativ;story_aufhaenger;pruefhinweis;website;quelle;score;prioritaet;status
```
`status` = „offen“.

## Regeln
- `quelle` ist Pflicht (URL, mehrere mit ` | `).
- Namen und E-Mails nur, wenn öffentlich auf der Firmen-/Vereins-/Schulseite. Privatadressen als solche kennzeichnen.
- Unsicheres in `pruefhinweis`, nicht im Aufhänger.
