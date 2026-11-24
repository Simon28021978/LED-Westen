# Datenformat Leadlisten

UTF-8, Semikolon als Trenner, Kopfzeile. Kompatibel mit daniel-daten (gleiche Spalten, plus `icp_typ`, `signal`, `recherchiert_am` am Ende).

```
firma;ort;plz;segment;website;ansprechpartner_rolle;quelle;fit_score;prioritaet;begruendung;pruefhinweis;icp_typ;signal;recherchiert_am
```

| Spalte | Inhalt |
|---|---|
| firma | Offizieller Name laut Impressum |
| ort, plz | Ort, 5-stellige PLZ (leer, wenn nicht belegt) |
| segment | z. B. Fahrradhandel, Outdoor, Reitsport, Lieferdienst, Event, Verein, Ordnerdienst, Kita/Schule |
| website | https-URL ohne Tracking-Parameter |
| ansprechpartner_rolle | Funktion (Inhaber, Flottenleitung, Vorstand …); Name nur, wenn öffentlich auf der Website |
| quelle | URL, auf der die Angaben belegt sind (Pflicht) |
| fit_score | 0–10 nach `daten/icp.md` |
| prioritaet | A/B/C |
| begruendung | Ein Satz, Pflicht bei A |
| pruefhinweis | keine_quelle, url_ungueltig, plz_pruefen, segment_unklar, … (mehrere mit Komma) |
| icp_typ | H (Wiederverkäufer) oder D (Direktabnehmer) |
| signal | Konkreter, belegter Bedarfsauslöser – der Aufhänger für die Ansprache |
| recherchiert_am | YYYY-MM-DD |

Sortierung: Priorität, dann Fit-Score absteigend.
