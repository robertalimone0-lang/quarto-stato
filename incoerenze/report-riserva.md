# Resoconto: base del riordino, riserva condizionata e regimi sostitutivi

Mercoledì 14 ottobre 2026. Dati: MEF, Rapporto annuale sulle spese fiscali 2025 (giugno 2026); Dipartimento delle Finanze, statistiche delle dichiarazioni 2025, anno d'imposta 2024. File riproducibili in `dati/spese_fiscali/`. Tutte le cifre sono da validare con il Dipartimento delle Finanze prima della pubblicazione.

## 1. Verifica della base di 11 miliardi (D21)

**Esito: la base non si ricostruisce.** Il riordino realistico vale circa 5,1 miliardi. Lo scarto rispetto agli 11 previsti è di circa 5,9 miliardi.

### Metodo

- Estrazione delle 573 misure del Rapporto 2025 (`strumenti/estrai_rapporto_spese_fiscali.py`, risultato in `dati/spese_fiscali/rsf2025_misure.csv`). Totale 2026 ricostruito: 126,7 miliardi, contro 129,7 ufficiali (scarto del 2%, dovuto a righe non lette o non quantificate).
- Il riferimento è il 2028 (84,7 miliardi quantificati), perché la base deve essere strutturale e le rate dei bonus edilizi già avviati si riducono nel tempo.
- Classificazione delle voci che fanno il 97% del valore (`dati/spese_fiscali/base_classificata.csv`).

### Composizione del valore 2028

| Gruppo | Miliardi | Trattamento |
|---|---|---|
| Escluse per decisione (cuneo e detrazioni del lavoro dipendente, Assegno unico, pensioni e indennità esenti, previdenza complementare, disabilità, regime impatriati e art. 44, famiglia) | 27,9 | fuori |
| Rate di bonus edilizi già avviati (superbonus, ecobonus, recupero edilizio, facciate, sismabonus) | 18,0 | fuori per legittimo affidamento |
| Sensibili (prima casa: rendita, registro, catastale e ipotecaria fisse, mutui; spese sanitarie; istruzione; cooperative; premi di produttività; spese funebri) | 15,8 | fuori salvo tua decisione |
| Regimi sostitutivi (forfettario, cedolare, PIR, OICR) | 7,5 | fuori salvo tua decisione |
| Agevolazioni sulle accise | 1,35 | già nei sussidi ambientalmente dannosi: doppio conteggio |
| Bonus mobili | 0,7 | riserva, sulle sole spese nuove |
| Candidate | 11,4 | base |
| Voci minori non classificate (256 misure) | 2,2 | base, per quota |

### Perché le candidate non bastano

Gli 11,4 miliardi di candidate comprendono 3,3 miliardi di effetti di scelte già fatte, che non si possono più cancellare:
- crediti d'imposta già maturati;
- riallineamento dell'avviamento;
- rivalutazioni;
- super e iperammortamento.

Ne restano 8,1 miliardi. Anche abolendole tutte e aggiungendo per intero le voci minori si arriverebbe a 10,3 miliardi, sotto gli 11. Una parte delle candidate sostiene obiettivi del programma (Mezzogiorno, agricoltura, editoria, cinema), e la proposta le tiene fuori.

### Base proposta, voce per voce (`dati/spese_fiscali/base_proposta.csv`)

| N. | Voce | 2028 (milioni) | Quota | Gettito (milioni) |
|---|---|---|---|---|
| 181 | Esenzioni dall'imposta sulle assicurazioni | 1.424 | 50% | 712 |
| 152 | Maggiorazione del costo del lavoro per nuove assunzioni (IRES) | 1.328 | 100% | 1.328 |
| 232 | Fondi sanitari integrativi, coperture che duplicano il SSN | 838 | 70% | 587 |
| 195 | Riduzione forfettaria del reddito dei fabbricati locati | 416 | 100% | 416 |
| 388 | Sostitutiva sulle prestazioni svizzere di prepensionamento | 564 | 50% | 282 |
| 317 | Premi assicurativi vita e infortuni al 19% | 282 | 100% | 282 |
| 425 | Compensi sportivi dilettantistici esenti | 652 | 30% | 196 |
| 412 | Fringe benefit sulle auto aziendali | 170 | 100% | 170 |
| 422 | Intramoenia: reddito al 75% | 160 | 100% | 160 |
| 71 | Tonnage tax | 485 | 30% | 145 |
| 170 | Patent box | 252 | 50% | 126 |
| 78 | Registro internazionale navale | 250 | 30% | 75 |
| — | Voci minori (256 misure), da elencare | 2.190 | 30% | 657 |
| | **Totale** | | | **5.135** |

**Un doppio uso da sciogliere.** La voce 152 (nuove assunzioni) è la stessa risorsa che la Riforma 19 usa come "riordino degli incentivi all'assunzione" e che il Piano Lavoro Stabile sostituisce con il bonus-malus. Va assegnata a una sola misura.

### Conseguenze sul quadro di Fase 1

| Grandezza | Base 11,0 | Base 6,1 (con le spese sanitarie sopra la soglia ISEE) | Base 5,1 |
|---|---|---|---|
| Priorità 2 coperta nel 2031 | 11,4 | 7,6 | 6,9 |
| Priorità 2 rinviata in coda | 6,0 | 9,7 | 10,5 |
| Margine prudente | ≥ 0 ogni anno | ≥ 0 ogni anno | ≥ 0 ogni anno |
| Saldo 2027 nello scenario avverso | +0,08 | −0,48 | −0,59 |
| Debito 2031, centrale | 131,5 | 131,8 | 131,8 |
| Debito 2031, prudente | 133,2 | 133,3 | 133,3 |
| Debito 2031, avverso con salvaguardia | 133,6 | 133,6 | 133,6 |
| Priorità 1 coperta senza azzardo e patrimonio pubblico | sì | sì | sì |

**Cosa ne segue**
- La Priorità 1 resta coperta e il debito cambia di pochi decimi.
- Circa 4,5 miliardi di Priorità 2 in più passano in coda.
- Il saldo del 2027 nello scenario avverso torna negativo e va richiuso con un altro slittamento: la regola della D15 non basta più.
- La riserva aggiuntiva del 13,1% sulle spese fiscali non è più disponibile: la base stessa esaurisce le voci aggredibili.

## 2. Riserva condizionata: gradini della D22 anno per anno

Variante senza riconoscimento dell'evasione, scenario prudente, miliardi. Il fabbisogno è lo scarto di spesa netta dopo il riconoscimento prudente della Riforma 1 (circa 3,85 miliardi a regime).

**Con la base a 11 miliardi**

| Anno | Scarto | a) Sussidi dannosi | b) Spending review | c) Cedolare | d) Curva sui bonus | e) Slittamento della Priorità 2 | Residuo |
|---|---|---|---|---|---|---|---|
| 2027 | +2,42 | — | — | — | — | — | 0 |
| 2028 | +1,11 | — | — | — | — | — | 0 |
| 2029 | −1,32 | 0,85 | 0,47 | — | — | — | 0 |
| 2030 | −3,58 | 0,85 | 0,65 | — | 0,16 | 1,92 | 0 |
| 2031 | −4,43 | 0,85 | 0,65 | — | 0,21 | 2,71 | 0 |

**Con la base a 5,1 miliardi**

| Anno | Scarto | a) | b) | c) | d) | e) | Residuo |
|---|---|---|---|---|---|---|---|
| 2027 | +1,12 | — | — | — | — | — | 0 |
| 2028 | −0,90 | — | — | — | 0,05 | 0,85 | 0 |
| 2029 | −1,78 | 0,85 | 0,65 | — | 0,11 | 0,17 | 0 |
| 2030 | −3,98 | 0,85 | 0,65 | — | 0,16 | 2,32 | 0 |
| 2031 | −4,80 | 0,85 | 0,65 | — | 0,21 | 3,09 | 0 |

**Come leggere le tabelle**
- Lo scarto cambia poco con la base: una base più piccola riduce insieme le coperture valide e la spesa di Fase 1.
- I gradini a) e b) sono disponibili dal 2029.
- Il gradino c) non è conteggiato finché non approvi la stima della cedolare (sezione 3).
- Con la cedolare approvata (0,4–0,5 miliardi netti), lo slittamento del 2031 scende a circa 2,6 miliardi.

## 3. Cedolare secca

**Costo ufficiale:** 3.354 milioni l'anno. Le quote per reddito qui sotto sono stime proprie (imponibile per ventile moltiplicato per la differenza tra aliquota marginale e aliquota della cedolare).

| Regime | Imponibile 2024 | Trattamento |
|---|---|---|
| Canone concordato al 10% | 8,0 miliardi | escluso: strumento della politica abitativa (Riforma 8) |
| Libero mercato al 21% | 14,4 miliardi, di cui 5,6 per redditi oltre 60.000 euro | curva verso l'aliquota marginale tra 60.000 e 150.000 euro: gettito statico 0,76 miliardi |
| Al 26% (immobili ulteriori) e redditi diversi | 0,96 miliardi | +5 punti: 0,05 miliardi statici; +7 punti: 0,07 |

**Distribuzione del beneficio:** decimo decile 70%, ultimi due decili 84%, primi cinque decili 4%.

**Risposta comportamentale** (evidenze sul 2011, solo da stampa: Il Post, Il Fatto Quotidiano, CGIA):
- l'introduzione della cedolare ha prodotto un'emersione limitata;
- gran parte delle opzioni è venuta da proprietari che già dichiaravano;
- il gettito del primo anno è stato molto inferiore alle previsioni.

**Effetto atteso della curva.** È il percorso inverso: riguarda proprietari che già dichiarano, quindi il rischio di ritorno al nero è contenuto. L'effetto più probabile è lo spostamento verso il canone concordato al 10%, desiderabile per la politica abitativa ma con meno gettito.

**Stima netta:** 0,38–0,53 miliardi, applicando uno sconto del 30–50% per lo spostamento al canone concordato, il ritorno al nero e la riduzione dell'offerta. Va accompagnata dalla registrazione obbligatoria e dalla detrazione per l'inquilino della Riforma 1. Mancano studi primari: la stima resta da validare (V26).

**Affitti brevi.** Il gettito di un'aliquota più alta è trascurabile (meno di 0,1 miliardi): le piattaforme trattengono già l'imposta alla fonte dal 2017. Il tema è di politica abitativa: tetto ai giorni e licenza comunale per le seconde case nei comuni ad alta tensione (Riforma 8). Propongo di distinguere:
- prima casa locata per brevi periodi: invariata al 21%;
- immobili ulteriori: curva crescente con il numero di unità.

Il gettito resta marginale.

## 4. Regime forfettario: curva d'uscita

**Costo ufficiale:** 3.491 milioni l'anno; 2,03 milioni di beneficiari; 1.717 euro a testa.

**Il vincolo europeo.** La soglia IVA di 85.000 euro è il massimo che la direttiva (UE) 2020/285 consente per la franchigia delle piccole imprese, quindi lo scalino IVA resta. La curva può riguardare solo l'imposta sul reddito: tra 85.000 e circa 125.000 euro di ricavi l'aliquota sostitutiva sale in modo continuo dal 15% fino all'aliquota effettiva ordinaria.

**Segno dell'effetto**
- *Breve periodo: costo.* Chi oggi ha tra 85.000 e 125.000 euro di ricavi e paga l'IRPEF ordinaria pagherebbe meno.
- *Medio periodo: gettito incerto.* Viene dall'emersione dei ricavi oggi tenuti sotto la soglia. Lo scalino IVA resta e ne riduce l'effetto.

**Conclusione.** Fino a una microsimulazione sulla distribuzione dei ricavi dei forfettari è una misura con un costo, non una copertura. I dati necessari sono le tavole sul quadro LM e l'Osservatorio sulle partite IVA del Dipartimento delle Finanze (S11).

## 5. Curva sulle agevolazioni edilizie oltre 60.000 euro

| Grandezza | Miliardi |
|---|---|
| Detrazioni 2024 per redditi oltre 60.000 euro (recupero edilizio, ecobonus, arredo) | 4,45 |
| Curva su tutto lo stock (non applicata: le rate in corso non si toccano) | 2,41 |
| Regime sulle sole spese nuove (fattore 55%, forbice 40–70%) | 1,33 |
| Per ogni annualità, al netto del tetto della L. 207/2024 | 0,054 |
| Profilo: 2029 / 2031 / 2035 | 0,11 / 0,21 / 0,43 |

## 6. Decisioni richieste

1. **Base del riordino.** Ridurla a circa 5,1 miliardi (o 6,1 con le spese sanitarie sopra la soglia ISEE), con l'effetto della sezione 1, oppure aprire le voci sensibili (prima casa con curva sui redditi alti, premi di produttività) o i regimi sostitutivi.
2. **Saldo 2027 nello scenario avverso** con la base ridotta: quale ulteriore voce di Priorità 2 slitta al 2028.
3. **Voce 152:** a quale misura va (base del riordino, Riforma 19 o Piano Lavoro Stabile).
4. **Cedolare al 21%:** approvazione della stima netta di 0,38–0,53 miliardi come gradino c).
5. **Forfettario:** curva d'uscita come misura con un costo, da quantificare.

## 7. Classificazione in quattro categorie (aggiornamento del 14 ottobre 2026)

File: `dati/spese_fiscali/base_quattro_categorie.csv`, con il motivo di ogni voce. Valori 2028, voci che fanno il 97% del totale.

| Categoria | Miliardi | Contenuto |
|---|---|---|
| Escluse per equità o per decisione | 32,4 | lavoro dipendente e pensioni, Assegno unico, disabilità, famiglia, cura, previdenza complementare, impatriati e art. 44, spese sanitarie (sotto la soglia ISEE) |
| Strutturali | 9,5 | prima casa (rendita non tassata, imposte d'acquisto ridotte, mutui in essere); note di variazione IVA; forfait delle spese sui fabbricati locati |
| Vincolate (diritto UE, accordi internazionali, legittimo affidamento) | 18,5 | rate dei bonus edilizi già avviati; prestazioni svizzere di prepensionamento (vincolo convenzionale da verificare) |
| Aggredibili | 22,2 | di cui regimi sostitutivi 7,5 (solo con decisione), sensibili 2,4, già nei sussidi dannosi 1,35, riserva 0,7, base 10,3 |

**Strutturali: tocco o no**
- *Prima casa:* non si tocca. Colpirebbe chi possiede la sola abitazione, cioè anche i redditi medi e bassi.
- *Note di variazione IVA:* non si toccano. Garantiscono la neutralità dell'imposta richiesta dal diritto UE.
- *Forfait delle spese sui fabbricati locati (5%):* si può ridurre, perché rappresenta costi reali. Resta in base al 100% come proposta da confermare, con l'interazione con la Riforma 8.

**Aliquote IVA ridotte su alimentari e beni essenziali:** escluse. Il Rapporto del MEF le considera regole strutturali del tributo e non le censisce tra le 573 spese fiscali, quindi l'esclusione non cambia la base.

**Base proposta aggiornata:** 4,85 miliardi. La voce 388 è tolta finché non si verifica il vincolo convenzionale.

## 8. Confronto storico: quanto hanno prodotto i riordini

| Episodio | Esito | Fonte |
|---|---|---|
| Serie 2017–2026 del Rapporto MEF | Le spese fiscali erariali sono salite da 54,5 a 129,7 miliardi (+138%) e da 468 a 573 misure. In dieci anni non c'è stato un anno di riduzione netta | MEF, Rapporto 2025, Tavola 14 |
| Gruppo di lavoro Ceriani (2011) | 720 misure censite; nessun riordino conseguente | dossier del Senato |
| Legge delega fiscale 2023 | Attese iniziali di 5–6 miliardi, ridotte a circa 1 miliardo | stampa (PMI.it, Il Sole 24 Ore), da validare |
| D.Lgs. 216/2023 | Taglio di 260 euro delle detrazioni al 19% per i redditi oltre 50.000 euro, a copertura parziale del nuovo IRPEF; importo della relazione tecnica non trovato | da validare |
| L. 207/2024 | Detrazioni per i figli fino a 30 anni: +0,32 miliardi; tetto alle detrazioni oltre 75.000 euro: circa 0,08 miliardi per annualità | relazione tecnica RGS |

**Conclusione.** Nessun riordino ha mai prodotto più di circa 1 miliardo l'anno. Gli 11 miliardi superano di circa dieci volte il massimo storico; anche i 4,85 della base proposta lo superano di circa cinque volte.

### Profili realistici e conseguenze sul quadro di Fase 1

| Profilo | Priorità 2 coperta nel 2031 | Rinviata in coda | Margine prudente | Saldo 2027 avverso | Debito 2031 (C / P / A) |
|---|---|---|---|---|---|
| Base 11, a regime nel 2028 (attuale) | 11,4 | 6,0 | ≥ 0 | +0,08 | 131,5 / 133,2 / 133,6 |
| **A.** Base 4,85, +20% l'anno, a regime nel 2031 (circa 1 miliardo l'anno, pari al massimo storico) | 6,7 | 10,7 | ≥ 0 | −0,95 | 131,9 / 133,4 / 133,6 |
| **B.** Base 3,0, a regime nel 2029 (1 miliardo l'anno) | 5,3 | 12,1 | ≥ 0 | −0,95 | 131,9 / 133,3 / 133,6 |

**Effetti comuni ai due profili**
- La Priorità 1 resta coperta nello scenario prudente in ogni anno.
- Nello scenario avverso il buco del 2027 (−0,95) riguarda la Priorità 1 stessa, perché la Priorità 2 del 2027 è già quasi nulla. Va chiuso con il gradino 4 della salvaguardia (rinvio dei nuovi ingressi) o con un avvio più lento della sanità e del welfare nel 2027.
- Il debito cambia di pochi decimi.
- La quota della Priorità 2 in coda sale a 10,7–12,1 miliardi.
