# Scoring mittelgroße Fahrradhändler – Vorschlag Rico

Stand: 2026-11-16 · Basis: `daten/leads_fahrrad_mittelgross_2026-11-16.csv` (10 Leads), `strategie/icp.md`, Recherche-Erfahrung. Keine neue Webrecherche.

## Merkmale

| Merkmal | Definition | Quelle | Aufwand | Zuverl. | Aussagekraft „kauft 5.000 € und verkauft ab“ |
|---|---|---|---|---|---|
| **Westen je Filiale** | 250 / Anzahl Filialen | Filialseite, pedali.de | gering | hoch | **hoch**: bester Abverkaufs-Indikator, den wir haben. ≤ 30 gut, 31–60 mittel, > 60 schwach |
| Filialanzahl | eigene Standorte mit Verkauf | Filialseite, Impressum | gering | hoch (Ausnahme: Zahlen schwanken zwischen Quellen) | hoch, steckt schon in „Westen je Filiale“ |
| Fläche / Mitarbeitende | m² bzw. MA laut Eigenangabe | Über-uns, Presse, Karriereseite | mittel | mittel (Eigenwerbung) | mittel; nur als Notiz, fehlt meist |
| Kindersortiment | woom/Puky/Kinderräder + Kinderzubehör | Onlineshop, Markenseite, Händlersuche woom/Puky | gering–mittel | hoch, wenn Marke belegt; mittel bei nur Kategorie | **hoch** für Kinderweste/-cape (UVP 44,90 €) |
| Westen-Status | (a) Westenkategorie ohne LED, (b) LED-/Premium-Wettbewerb, (c) keine Westen, (d) unbekannt | Shopsuche „warnweste“, „weste“, Kategorie Sicherheit | mittel | **gering–mittel**: JS-Shops, Bot-Schutz, Filialsortiment ≠ Onlineshop | mittel; (a) belegt Nachfrage, (c) ist nur bedingt „Lücke“ |
| Entscheidungsweg | Inhaber / Familien-GF / Fremd-GF mit Beteiligung / Verbund | Impressum, Handelsregister, Über-uns | gering (GF), hoch (Gesellschafter, Verbund) | hoch für GF, gering für Verbund | hoch: Inhaber entscheidet schnell, Zentraleinkauf/Verbund verlangsamt |
| Verbund (ZEG, BICO, VSF) | Mitgliedschaft, Händlermarke (BIKE&CO, Zweirad-Einkaufs-Genossenschaft) | Logos auf Website, Händlersuche der Verbünde | mittel | mittel | mittel; heißt oft: Listung über Verbund statt Direktkauf |
| Region Nord | Sitz oder ≥ 1/3 Filialen in SH, HH, HB, NI, MV | Filialseite | gering | hoch | mittel (Logistik, Besuchbarkeit, Priorität laut CLAUDE.md) |
| Onlineshop | eigener Shop mit Zubehör | Website | gering | hoch | mittel: zusätzlicher Abverkaufskanal, entlastet Filialbestand |
| Brief-Zustellbarkeit (Gate) | GF-Name + Postanschrift belegt | Impressum, Handelsregister | gering | hoch | keine Score-Wirkung, aber Pflicht vor Versand |
| Wachstum / Bonität | neue Filialen, Bilanz | Presse, Bundesanzeiger (bei Einzelunternehmen nichts) | hoch | gering–mittel | gering; nur Notiz |

Streichen als Score: „Erreichbarkeit GF“ (alle 10 haben GF im Impressum, trennt nicht), Servicetest-Platzierungen (sagt nichts über Zubehörabverkauf), Wachstum (zu teuer zu recherchieren).

## Datenlage der 10 Leads heute

- **Westen-Status**: Nur Stadler mit Marken und Preisen belegt (Wowow, 4-Act). Rachow und Hahne: Kategorie vorhanden, Inhalt nicht auslesbar. Bike Market: 0 Treffer online. **Unbekannt bei 6 von 10** (MEGA Bike, Radhaus, Bikesnboards, Küstenrad, Edelhelfer, Wollesen).
- **Kindersortiment**: Marke belegt bei 3 von 10 (Bike Market, Rachow, Edelhelfer). Nur Kategorie bei 6, MEGA Bike nur über Altliste. Kein Beleg bei 1 (Küstenrad, reiner E-Bike-Händler).
- **Eigentümer/Entscheidungsweg**: klar bei 5, teilweise bei 3 (MEGA, Bikesnboards, Hahne), unbekannt bei 2 (Küstenrad, Edelhelfer).
- **Verbund**: nur bei Wollesen erfasst (BIKE&CO), bei 9 nicht geprüft.
- **Fläche**: belegt bei 2 (Bike Market, Radhaus), Mitarbeitende nur bei 1.
- **Filialen/GF**: 10 von 10 belegt. MEGA Bike: Filialzahl uneinheitlich (14–16), Impressum nur über Suchindex, Registeranschrift offen.

## Was das für das Scoring heißt

1. Ein Score mit vielen gleichgewichteten Merkmalen wäre Scheingenauigkeit: Er misst heute vor allem, wie gut ein Shop auslesbar war.
2. **Unbekannt = neutral** (Mittelwert), nicht 0. Sonst rutschen MEGA Bike und Radhaus allein wegen Bot-Schutz bzw. JavaScript nach unten.
3. Vorschlag: zwei Gates (GF + Anschrift belegt; ≥ 3 Filialen), dann wenige Merkmale gewichtet: Westen je Filiale 35 %, Kindersortiment 25 %, Entscheidungsweg 20 %, Region Nord 10 %, Westen-Status 10 %. Pro Lead eine Spalte „Datenvollständigkeit“ (z. B. 4/5 belegt).
4. Westen-Status gehört nicht ins Scoring, sondern in die Gesprächsvorbereitung: Ob Westen im Laden hängen, klärt ein Anruf, Ladenbesuch oder die Rückmeldung auf den Brief zuverlässiger als die Shopsuche.
5. Vor dem Versand nachholen (mittlerer Aufwand, ca. 15 Min. je Lead): Handelsregister-Auszug für MEGA Bike, Küstenrad, Edelhelfer; woom-/Puky-Händlersuche für alle 10; Verbund-Logos prüfen.
