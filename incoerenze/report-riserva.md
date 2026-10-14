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

## 9. Correzioni e verifiche richieste (secondo controllo)

**Riconciliazione dei totali.** Le voci classificate (70) valgono 82,49 miliardi, le voci minori (256) 2,19: insieme 84,68, il totale 2028 delle sole misure quantificate. I "2 miliardi mancanti" erano le voci minori, omesse nella tabella in quattro categorie. Il confronto va fatto con questi 84,7 miliardi, non con i 129,7 del totale 2026 (che comprende le rate decrescenti dei bonus edilizi).

**Quattro categorie corrette (2028, miliardi)**

| Categoria | Miliardi |
|---|---|
| Escluse per equità o decisione | 32,4 |
| Strutturali | 9,5 |
| Vincolate | 19,2 (comprende ora il bonus mobili) |
| Aggredibili | 21,5 |
| Voci minori, da classificare una per una | 2,2 |
| **Totale** | **84,7** |

**La "riserva 0,7".** Era la voce 215, cioè le rate del bonus mobili già avviate. La riserva colpisce solo le spese nuove, quindi quelle rate sono vincolate per legittimo affidamento e ora stanno in quella categoria. La riserva del 13,1% sulle spese fiscali non esiste più.

**Sussidi dannosi.** Le voci 64 e 461 (agevolazioni sulle accise, 1,35 miliardi) sono fuori dalla base del riordino, quindi con la base non c'è doppio conteggio. Il rischio esiste però dentro i sussidi dannosi: la copertura di base (6 miliardi netti) e il gradino a) (+1 miliardo) attingono allo stesso catalogo del Ministero dell'Ambiente, che non ha ancora un elenco nominativo. Finché non c'è, il controllo automatico non può escludere che la stessa accisa finanzi entrambi (V29).

**Prima casa (D23 riaperta).** La classificazione "non si tocca" valeva per un taglio generalizzato. Una curva che renda imponibile in modo graduale la rendita dell'abitazione principale per i redditi tra 60.000 e 150.000 euro (piena oltre 150.000) riguarda 1,37 milioni di contribuenti e vale circa 0,37 miliardi statici: rendita non imponibile oltre 60.000 euro pari a 1,56 miliardi, all'aliquota marginale con le addizionali. Una curva sui valori catastali alti non si può stimare con le tavole delle dichiarazioni: servono i dati del catasto. Le imposte d'acquisto sulla prima casa (registro, ipotecaria, catastale) non hanno dati per reddito. La scelta resta all'autrice.

**Confronto storico integrato**
- *Superbonus:* è una spesa fiscale censita dal Rapporto (voce 211). La riduzione dell'aliquota dal 110% al 90% (DL 176/2022), poi al 70% e al 65%, e lo stop alla cessione dei crediti (DL 11/2023, poi DL 39/2024) sono tagli di ordine miliardario a una singola agevolazione. Le relazioni tecniche con gli importi non sono state reperite in questa sessione (V30). Sono interventi d'emergenza su una misura fuori controllo e producono effetti soprattutto sulle spese future.
- *ACE:* non è tra le spese fiscali del Rapporto 2023 (verificato sul testo). La sua abrogazione (D.Lgs. 216/2023) è un ampliamento di base di ordine miliardario ma fuori dal perimetro; importo da validare.

**Conclusione.** Il "massimo storico di 1 miliardo" regge solo per i riordini trasversali delle detrazioni. Tagli singoli di ordine miliardario sono avvenuti (Superbonus). La difficoltà del profilo A sta altrove: chiede circa 0,97 miliardi in più ogni anno (20% di 4,85, crescita lineare) per cinque anni consecutivi, cosa mai avvenuta.

**Gradini della D22 con base 4,85 e profilo A** (variante senza riconoscimento, prudente, miliardi)

| Anno | Scarto | Dopo la Riforma 1 legislativa | a) Sussidi | b) Spending | c) Cedolare | d) Bonus | e) Slittamento della Priorità 2 | Priorità 2 coperta prima / dopo |
|---|---|---|---|---|---|---|---|---|
| 2027 | +0,41 | +0,41 | — | — | — | — | — | 0,31 / 0,31 |
| 2028 | −2,12 | −1,16 | — | — | — | 0,05 | 1,11 | 4,45 / 3,34 |
| 2029 | −4,58 | −2,65 | 0,85 | 0,65 | — | 0,11 | 1,05 | 5,93 / 4,88 |
| 2030 | −6,96 | −4,07 | 0,85 | 0,65 | — | 0,16 | 2,41 | 5,93 / 3,52 |
| 2031 | −8,67 | −4,82 | 0,85 | 0,65 | — | 0,21 | 3,11 | 6,69 / 3,58 |

Nella variante senza riconoscimento la Priorità 2 coperta nel 2031 scende quindi a circa 3,6 miliardi.

**Saldo 2027 nello scenario avverso:** −0,95 miliardi, chiuso con il gradino 4 della salvaguardia (rinvio dei nuovi ingressi della Priorità 1) su una Priorità 1 del 2027 di 5,72 miliardi. Decisione dell'autrice del 14 ottobre 2026.

## 10. Prima casa: decisione D23 (mercoledì 14 ottobre 2026)

**Misura.** La rendita dell'abitazione principale diventa imponibile in modo graduale lungo una curva continua del reddito complessivo: zero fino a 60.000 euro, piena imponibilità a 150.000 euro e oltre.
- Gettito statico: circa 0,37 miliardi.
- Contribuenti interessati: 1,37 milioni.
- La curva è **rivedibile con la riforma del catasto**: con rendite aggiornate ai valori di mercato, la soglia può spostarsi dal reddito al valore dell'immobile.

**Classificazione.** La voce 187 (3,76 miliardi) si divide in due:
- quota dei redditi fino a 60.000 euro: 3,05 miliardi, strutturale, non si tocca;
- quota oltre 60.000 euro: 0,71 miliardi, aggredibile come voce sensibile aperta per decisione dell'autrice. La curva ne recupera 0,37.

| Categoria (2028) | Miliardi |
|---|---|
| Escluse per equità o decisione | 32,4 |
| Strutturali | 8,7 |
| Vincolate | 19,2 |
| Aggredibili | 22,2 |
| Voci minori | 2,2 |
| **Totale** | **84,7** |

**Base del profilo A:** 5,22 miliardi (4,85 più 0,37), con lo stesso aumento lineare del 20% l'anno, a regime nel 2031.

| Grandezza | Valore |
|---|---|
| Priorità 2 coperta per anno, 2027–2031 | 0,33 / 4,57 / 6,16 / 6,16 / 6,97 |
| Priorità 2 rinviata in coda | 10,4 |
| Margine prudente | ≥ 0 ogni anno |
| Saldo 2027 avverso (chiuso con il rinvio dei nuovi ingressi della Priorità 1) | −0,93 |
| Debito 2031: centrale / prudente / avverso con salvaguardia | 131,9 / 133,35 / 133,6 |

**Gradini della D22 con base 5,22** (variante senza riconoscimento, prudente, miliardi)

| Anno | Scarto dopo la Riforma 1 | a) Sussidi | b) Spending | c) Cedolare | d) Bonus | e) Slittamento | Priorità 2 coperta prima / dopo |
|---|---|---|---|---|---|---|---|
| 2027 | +0,44 | — | — | — | — | — | 0,33 / 0,33 |
| 2028 | −1,15 | — | — | — | 0,05 | 1,10 | 4,57 / 3,52 |
| 2029 | −2,69 | 0,85 | 0,65 | — | 0,11 | 1,08 | 6,16 / 5,13 |
| 2030 | −4,05 | 0,85 | 0,65 | — | 0,16 | 2,39 | 6,16 / 3,88 |
| 2031 | −4,80 | 0,85 | 0,65 | — | 0,21 | 3,09 | 6,97 / 4,03 |

## 11. Decisioni D24, D25 e gradino c) (mercoledì 14 ottobre 2026)

**Base del riordino (profilo A).** 3,52 miliardi (4,85 meno la voce 152), con circa 0,70 miliardi in più ogni anno dal 2027 al 2031, crescita lineare. La rampa annua resta sotto il massimo storico dei riordini trasversali, circa 1 miliardo.
- *Voci minori:* dentro i 3,52 ci sono ancora 0,66 miliardi di voci minori (il 30% di 2,19 miliardi, 256 misure), da elencare una per una prima della pubblicazione.
- *Prima casa (D23):* riga separata COP16, 0,37 miliardi dal 2028. È una decisione politica distinta, rivedibile con la riforma del catasto.
- *Totale delle due righe:* 3,89 miliardi.

**Voce 152 (D24).** La maggiorazione per le nuove assunzioni resta come agevolazione del Piano Lavoro Stabile, solo per le assunzioni a tempo indeterminato. Esce dal riordino e dalla copertura della Riforma 19.
- Da verificare se la norma vigente (D.Lgs. 216/2023) la limita già al tempo indeterminato: in quel caso la condizione non cambia il costo.
- Il costo netto della Riforma 19 in coda (Q10) sale da 0,70 a 1,95 miliardi (forbice 1,4–2,5), perché perde il riordino degli incentivi. Se le decontribuzioni annuali, distinte dalla voce 152, restano nel riordino, il costo torna verso 0,70: la composizione del riordino degli incentivi va verificata.
- Con il nuovo costo, nello scenario centrale la Riforma 19 non si attiva entro il 2035.

**Gradino c), cedolare al 21%:** 0,38 miliardi nel prudente (limite inferiore), 0,45 nel centrale (valore medio). Le evidenze sulla risposta comportamentale vengono solo dalla stampa (V26).

**Quadro di Fase 1 (miliardi)**

| Grandezza | Valore |
|---|---|
| Priorità 2 coperta per anno, 2027–2031 | 0,22 / 4,30 / 5,37 / 5,37 / 5,92 |
| Priorità 2 rinviata in coda | 11,44 (di cui 5,45 nuova voce Q15, composizione da decidere) |
| Margine prudente | 0,29 / 0 / 0,49 / 0 / 0 |
| Margine centrale | 1,24 / 3,42 / 5,88 / 5,79 / 6,01 |
| Saldo 2027 avverso | −1,01, chiuso con il rinvio dei nuovi ingressi della Priorità 1 |
| Debito 2031 (centrale / prudente / avverso con salvaguardia) | 131,9 / 133,35 / 133,6 |

**Gradini della D22** (variante senza riconoscimento, prudente, miliardi). Lo scarto è calcolato sulla Priorità 2 già ridotta dal profilo A: la spesa di Fase 1 è quella che il profilo consente, e lo slittamento si aggiunge alla quota già rinviata in coda.

| Anno | Scarto dopo la Riforma 1 | a) Sussidi | b) Spending | c) Cedolare | d) Bonus | e) Slittamento | Priorità 2 coperta prima / dopo |
|---|---|---|---|---|---|---|---|
| 2027 | +0,29 | — | — | — | — | — | 0,22 / 0,22 |
| 2028 | −1,18 | — | — | — | 0,05 | 1,12 | 4,30 / 3,22 |
| 2029 | −2,50 | 0,85 | 0,65 | 0,38 | 0,11 | 0,51 | 5,37 / 4,88 |
| 2030 | −4,12 | 0,85 | 0,65 | 0,38 | 0,16 | 2,08 | 5,37 / 3,39 |
| 2031 | −4,89 | 0,85 | 0,65 | 0,38 | 0,21 | 2,79 | 5,92 / 3,26 |

**Confronto con il passaggio precedente.** Senza riconoscimento la Priorità 2 coperta nel 2031 passa da 3,58 a 3,26 miliardi (−0,32). Prima dello slittamento passa da 6,69 a 5,92 (−0,77). Nello scenario centrale non scatta nessun gradino.

**Salvaguardia.** In ogni slittamento le stabilizzazioni degli insegnanti slittano per ultime. Appartengono alla Priorità 2 (scuola e Piano Lavoro Stabile), quindi la regola opera nei gradini 2 e 3 della salvaguardia e nel gradino e) della riserva. Il rinvio dei nuovi ingressi del 2027 riguarda la Priorità 1 e non le tocca.

## 12. Decisioni sulla voce 152, Riforma 19, stabilizzazioni e Q15 (mercoledì 14 ottobre 2026)

**V32, verificata sul testo.** Il nuovo testo unico delle imposte sui redditi (D.Lgs. 19 giugno 2026, n. 117, art. 104, commi 10-18, in vigore dal 1° gennaio 2027) riprende la maggiorazione dell'art. 4 del D.Lgs. 216/2023 con le stesse condizioni:
- solo assunzioni a tempo indeterminato;
- incremento netto dei dipendenti stabili;
- +20%, fino a +10% in più per le categorie dell'Allegato G.

Il comma 17 la applica ai periodi d'imposta dal 2025 al 2027: dal 2028 non esiste più a legislazione vigente.

**Opzione A nel Piano Lavoro Stabile.** Dal 2028 la maggiorazione sale al 30% per le sole trasformazioni di contratti a termine in contratti stabili.
- È una proroga mirata, quindi un costo nuovo rispetto al tendenziale: circa 0,67 miliardi l'anno se le trasformazioni sono un terzo delle assunzioni stabili (da validare).
- La finanzia la penalità sul turnover, a saldo zero.
- Serve una deroga al comma 13, che esclude l'agevolazione quando il totale dei dipendenti non cresce: nelle trasformazioni non cresce.

**Riforma 19 ridotta (Q10):** 0,5 miliardi, attivazione nel 2031 nello scenario centrale. Contiene:
- conto delle competenze per disoccupati e persone con bassa istruzione, con la formazione a risultato;
- competenze di base per adulti;
- consulenti dei centri per l'impiego.

Credito per il secondo reddito, educazione finanziaria e microcredito sono dichiarati riforma di seconda legislatura.

**Stabilizzazioni degli insegnanti in Priorità 1** (perimetro 0,75): costo 0,11 / 0,25 / 0,41 / 0,63 / 0,75 miliardi dal 2027 al 2031. Nella salvaguardia slittano per ultime anche dentro la Priorità 1. Nello scenario avverso il rinvio dei nuovi ingressi resta molto sotto la capacità della Priorità 1 senza le stabilizzazioni, quindi in nessun anno le raggiunge.

**Q15 (`dati/q15.csv`)**

| Voce | Miliardi |
|---|---|
| Costo di rinvio basso: congedo di paternità, garanzia di lavoro, fondo per la pensione di garanzia, Stato digitale | 1,85 |
| Costo di rinvio medio: lavori gravosi, fondo affitto | 1,00 |
| Scuola: prima metà dell'aumento salariale | 2,25 |
| Scuola: ulteriore rampa (tempo pieno e mense oltre il 2031, interpretazione da confermare) | 0,35 |
| **Totale** | **5,45** |

Q15 è in fondo alla coda e si attiva solo con il gettito certificato del contrasto all'evasione. Nelle proiezioni non si attiva entro il 2035.

**Quadro aggiornato (miliardi)**

| Grandezza | Valore |
|---|---|
| Priorità 2 coperta, 2027–2031 | 0,17 / 4,04 / 4,73 / 4,73 / 5,17 |
| Rinviata in coda | 11,44 |
| Margine prudente | ≥ 0 ogni anno |
| Debito 2031 (centrale / prudente / avverso con salvaguardia) | 131,9 / 133,3 / 133,6 |
| Scenario avverso, rinvio dei nuovi ingressi della Priorità 1 (2027–2031) | 0,89 / 0,71 / 2,37 / 4,67 / 5,58 |

Nel 2031 slitta il 25,5% dei nuovi ingressi della Priorità 1. Il valore era 23% prima dello spostamento delle stabilizzazioni in Priorità 1.

**Gradini della D22** (variante senza riconoscimento, prudente)

| Anno | Scarto | a | b | c | d | e | Priorità 2 coperta prima / dopo |
|---|---|---|---|---|---|---|---|
| 2028 | −1,19 | — | — | — | 0,05 | 1,14 | 4,04 / 2,96 |
| 2029 | −2,32 | 0,85 | 0,65 | 0,38 | 0,11 | 0,33 | 4,73 / 4,42 |
| 2030 | −4,16 | 0,85 | 0,65 | 0,38 | 0,16 | 2,12 | 4,73 / 2,72 |
| 2031 | −4,93 | 0,85 | 0,65 | 0,38 | 0,21 | 2,84 | 5,17 / 2,47 |

## 13. Tranche salariale degli insegnanti finanziata dal dividendo demografico (mercoledì 14 ottobre 2026)

**Rinnovi ordinari.** La L. 207/2024 stanzia per il rinnovo del contratto del personale statale 2028–2030 1.954 milioni nel 2028, 4.027 nel 2029 e 6.112 dal 2030. Il dato viene da Ancrel; il comma va verificato sul testo della legge. I rinnovi ordinari sono quindi nel tendenziale. L'aumento reale degli insegnanti previsto dal programma si aggiunge a quei rinnovi, e il capitolo sulla scuola lo dichiara.

**Dividendo demografico (COP17)**
- *Ipotesi:* 115.000 studenti in meno l'anno; posti comuni in meno a parità di rapporto (614.572 posti per circa 7 milioni di studenti), cioè circa 10.100 posti l'anno.
- *Sovrapposizione con il tendenziale:* i 5.660 posti del comma 828 e i 1.407 del 2026/27 cadono prima del 2027. Dal dividendo sono tolti i 2.510 posti di potenziamento previsti nel 2027/28–2028/29.
- *Costo per posto:* 80% supplenze annuali a 29.500 euro (metà al 31 agosto, metà al 30 giugno, trattamento iniziale del ruolo con oneri) e 20% posti di ruolo a 45.000 euro, per una media di 32.600 euro. Il Conto annuale RGS pubblica solo le retribuzioni del personale di ruolo, quindi il costo della supplenza è una stima della redazione (da validare).

| Anno | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|
| Posti in meno nell'anno | 8.842 | 8.842 | 10.097 | 10.097 | 10.097 |
| Dividendo cumulato (miliardi) | 0,29 | 0,58 | 0,91 | 1,24 | 1,56 |
| Al tasso prudente (70%) | 0,20 | 0,40 | 0,63 | 0,86 | 1,09 |
| Tranche salariale (prezzi dello scenario centrale) | — | — | 0,60 | 0,82 | 1,00 |
| Classi più piccole nelle zone a rischio di dispersione | — | — | — | — | 0,04 |

I risparmi del 2027 e del 2028 non sono contabilizzati: la tranche parte nel 2029. Nel 2029 non arriva a 1,0 miliardi, quindi parte dal valore disponibile (0,60) e cresce con il dividendo. Dal 2032 il residuo crescente va alle classi più piccole.

**Supplenze, stabilizzazioni e mancati rinnovi**

| Anno | Supplenze iniziali (2025/26) | Stabilizzate, cumulate | Non rinnovate per il calo degli studenti, cumulate | Residue |
|---|---|---|---|---|
| 2027 | 182.641 | 15.000 | 7.074 | 160.567 |
| 2028 | 182.641 | 33.600 | 14.147 | 134.894 |
| 2029 | 182.641 | 55.100 | 22.225 | 105.316 |
| 2030 | 182.641 | 84.600 | 30.302 | 67.739 |
| 2031 | 182.641 | 100.000 | 38.380 | 44.261 |

**Nessun doppio conteggio**
- Le 100.000 stabilizzazioni (0,75 miliardi a circa 7.500 euro per posto, secondo il file 07) riguardano soprattutto i posti di sostegno in deroga (76.100), che non calano con gli studenti, e circa 24.000 posti comuni vacanti da due anni.
- I mancati rinnovi riguardano solo posti comuni (106.541 supplenze in tutto).

**Il punto politico da scrivere.** Circa il 28% della riduzione delle supplenze entro il 2031 avviene per mancato rinnovo, perché servono meno posti, e non con assunzioni. Il traguardo del Piano Lavoro Stabile (meno di 30.000 supplenze annuali) richiede il perimetro di 1,40 miliardi, quindi la soluzione del conflitto S1.

**Effetto sul quadro**
- Priorità 2 coperta: 0,17 / 4,04 / 5,56 / 5,56 / 6,21 miliardi.
- Quota rinviata in coda: 10,44.
- Q15 scende a 4,45: la prima metà dell'aumento in coda passa da 2,25 a 1,25.
- Nessuna voce della coda slitta.

## 14. Bacino MIM dei supplenti, dividendo sulle classi e stabilizzazioni (mercoledì 14 ottobre 2026)

Sostituisce la sezione 13 per dividendo, tranche e tabella delle supplenze.

**Bacino dei supplenti (MIM, open data 2024/25)**

| | Al 31 agosto (posto vacante) | Fino al termine (30 giugno) | Totale |
|---|---|---|---|
| Posti comuni | 30.215 | 66.903 | 97.118 |
| Sostegno | 14.202 | 125.462 (deroga) | 139.664 |
| Totale | 44.417 | 192.365 | 236.782 |

**Dividendo demografico sulle classi (COP17)**
- Classi perse dal 2023/24 al 2024/25 (MIM): primaria −1.020, secondaria di I grado −599, secondaria di II grado +347. Docenti per classe: 1,82, 2,02, 2,12. A parità di alunni per classe servono circa 2.326 posti in meno l'anno; infanzia esclusa.
- Al netto dei posti di potenziamento già tagliati nel tendenziale (1.255 l'anno nel 2027 e nel 2028). Costo per posto 32.600 euro (da validare).

| Anno | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---|---|---|---|---|
| Posti in meno nell'anno | 1.071 | 1.071 | 2.326 | 2.326 | 2.326 |
| Dividendo cumulato (miliardi) | 0,03 | 0,07 | 0,15 | 0,22 | 0,30 |
| Al tasso prudente (70%) | 0,02 | 0,05 | 0,10 | 0,16 | 0,21 |
| Indennità M23 (prezzi dello scenario centrale) | — | — | 0,10 | 0,15 | 0,20 |

Il dividendo calcolato sugli studenti (1,56 miliardi) sopravvalutava il calo dei posti: gli studenti in meno si distribuiscono su classi che restano aperte.

**Indennità per gli insegnanti delle scuole a rischio di dispersione (M23).** 5% delle scuole, ordinate per dispersione implicita INVALSI: circa 48.800 docenti sul totale di 976.363 di ruolo e supplenti. A regime 0,20 miliardi, 338 euro lordo Stato al mese, 255 euro lordo dipendente. Dimensionata sul dividendo al tasso prudente al netto del rincaro dei costi del 5%. Fonte dell'indicatore: INVALSI, Rapporto nazionale 2026 (giovedì 16 luglio 2026), dispersione implicita nazionale al 6,3% (8,7% nel 2025); il dato per istituto va richiesto all'INVALSI (V38). La misura si valuta confrontando la mobilità dei docenti e la dispersione implicita delle scuole appena sopra e appena sotto la soglia del 5%.

**Stabilizzazioni con il perimetro 0,75 (circa 7.500 euro per posto, 100.000 posti)**
- Posti comuni: solo posti vacanti, al netto della riduzione cumulata dei posti al 2031 (11.630) e di un margine del 10% per la mobilità: 0,9 × 30.215 − 11.630 = 15.563.
- Sostegno su posto vacante: 14.202.
- Sostegno in deroga: 70.235, al ritmo delle specializzazioni.

| Anno | Stabilizzate, cumulate | Non rinnovate per il calo delle classi, cumulate | Supplenze residue | Comuni su posto vacante | Comuni fino al termine | Sostegno su posto vacante | Sostegno in deroga |
|---|---|---|---|---|---|---|---|
| 2027 | 15.000 | 2.326 | 219.456 | 27.881 | 64.577 | 12.072 | 114.927 |
| 2028 | 33.600 | 4.652 | 198.530 | 24.986 | 62.251 | 9.430 | 101.863 |
| 2029 | 55.100 | 6.978 | 174.704 | 21.640 | 59.925 | 6.377 | 86.763 |
| 2030 | 84.600 | 9.304 | 142.878 | 17.049 | 57.599 | 2.187 | 66.043 |
| 2031 | 100.000 | 11.630 | 125.152 | 14.652 | 55.273 | 0 | 55.227 |

- I mancati rinnovi valgono il 10,4% della riduzione delle supplenze al 2031.
- La riduzione dei posti colpisce soprattutto le supplenze fino al termine; il tetto sui posti vacanti la sconta per intero, quindi è prudente.

**Traguardi al 2031**
- Supplenze su posto vacante (al 31 agosto): da 44.417 a 14.652, sotto 30.000.
- Supplenze in deroga sul sostegno: da 125.462 a 55.227 con il perimetro 0,75; 25.462 con il perimetro massimo.
- Supplenze residue totali: 125.152, di cui 55.273 comuni fino al termine (spezzoni e posti non vacanti, precariato strutturale) e 55.227 in deroga. Il programma elimina il precariato su posto vacante e dichiara il precariato strutturale che resta.

**Perimetro massimo.** Il bacino stabilizzabile è di 129.765 posti (15.563 comuni, 14.202 sostegno vacante, 100.000 in deroga): 0,97 miliardi più 0,09 di corsi. Il perimetro 1,40 del Piano Lavoro Stabile (circa 186.700 posti) supera il bacino. Con il bacino massimo restano 95.387 supplenze.

**Corsi gratuiti di specializzazione (M24, Priorità 1, 0,09 l'anno).** Spostano 0,09 di Priorità 2 in coda. La voce che cede è l'aumento salariale della scuola: la quota in Q15 passa da 2,60 a 2,69 e Q15 da 5,45 a 5,54. Motivo: l'aumento è già scaglionato in coda, resta nel perimetro della scuola e non tocca le voci a costo di rinvio medio (gravosi, fondo affitto).

**Ritmo delle specializzazioni (verifica a)**
- Offerta attuale: TFA X ciclo 35.784 posti (DM MUR 436 del giovedì 26 giugno 2025), XI ciclo 30.241 (nota MUR 4660 del martedì 14 aprile 2026, senza secondaria di II grado); percorsi INDIRE per chi ha tre anni di servizio sul sostegno, 18.137 specializzati nel primo ciclo, prorogati al 31 dicembre 2026. Dati da stampa specializzata (V39).
- Fabbisogno: 70.235 stabilizzazioni in deroga con 0,75, cioè circa 14.000 l'anno; 100.000 con il perimetro massimo, cioè 20.000 l'anno dal 2027.
- Manca il numero dei supplenti in deroga già specializzati (V37). In sua assenza, l'anno in cui si arriva alle stabilizzazioni dipende dal flusso annuo di specializzati tra i supplenti in deroga:

| Specializzati in deroga l'anno | Cumulato al 2031 | 70.235 (perimetro 0,75) | 100.000 (perimetro massimo) |
|---|---|---|---|
| 15.000 | 75.000 | 2031 | 2033 |
| 20.000 | 100.000 | 2030 | 2031 |
| 25.000 | 125.000 | 2029 | 2030 |

- I 0,09 miliardi pagano circa 26.000–30.000 posti di corso l'anno (3.000–3.500 euro per posto, stima della redazione). Il perimetro massimo entro il 2031 richiede che almeno 20.000 posti l'anno vadano ai supplenti in deroga in aggiunta all'offerta attuale, quindi un aumento della capacità degli atenei. Senza questo aumento il perimetro massimo si raggiunge nel 2033 e i 0,22 aggiuntivi restano in parte inutilizzati fino ad allora.

**Opzioni per i 0,22 aggiuntivi dentro i 6,8 miliardi della scuola (verifica b, D27).** Composizione della Riforma 3 (file 01): aumento salariale 4,5; stabilizzazione 0,5–1 (0,75 nel quadro); tempo pieno e mense circa 1,0; diritto allo studio circa 0,5. Le stabilizzazioni sono in Priorità 1: ogni aumento sposta in coda la stessa quota di Priorità 2.

| Opzione | Da dove vengono i 0,22 | A cosa si rinuncia |
|---|---|---|
| A | aumento salariale da 4,5 a 4,28 miliardi | l'aumento reale scende dal 10% a circa il 9,5%; la coda non cresce |
| B | tempo pieno e mense da 1,0 a 0,78 | circa un quinto dell'estensione del tempo pieno e delle mense gratuite, quindi meno classi a tempo pieno nel Mezzogiorno |
| C | voce aggiuntiva in coda, attivata dal gettito certificato | nessuna rinuncia nella scuola; i 30.000 posti in deroga aggiuntivi diventano condizionati al gettito ed escono dalla Priorità 1 |
| D | indennità M23 | la misura sulle scuole a rischio di dispersione sparisce |

Con l'opzione A la scuola torna dentro i 6,8 anche per i corsi se l'aumento scende a 4,19 (0,22 + 0,09). In ogni opzione il perimetro massimo ha effetto entro il 2031 solo se il flusso di specializzati in deroga raggiunge 20.000 l'anno.

**Effetto sul quadro**
- Priorità 2 coperta: 0,13 / 3,95 / 4,79 / 4,79 / 5,28 miliardi.
- Quota rinviata in coda: 11,53, uguale alla somma delle voci di coda.
- Prudente ≥ 0 in ogni anno. Anni di attivazione della coda invariati.

## 15. D27, riserva nei corsi di specializzazione, platea dell'indennità (mercoledì 14 ottobre 2026)

**D27, opzione A.** Stabilizzazioni al perimetro massimo (0,97) e corsi (0,09) rientrano nei 6,8 miliardi della scuola riducendo l'aumento salariale da 4,5 a 4,19 miliardi.

| Voce della Riforma 3 | Prima | Dopo |
|---|---|---|
| Aumento salariale | 4,50 | 4,19 |
| Stabilizzazioni (M21, Priorità 1) | 0,75 | 0,97 |
| Corsi di specializzazione (M24, Priorità 1) | 0,09 | 0,09 |
| Resto della scuola in Priorità 2 (M07) | 6,05 | 5,74 |
| Totale scuola | 6,89 | 6,80 |

- Aumento reale: 10% × 4,19 / 4,5, circa il 9,3% in cinque anni.
- In coda la riduzione di 0,31 assorbe le quote cedute a stabilizzazioni (0,22) e corsi (0,09): Q15 torna a 5,45 e la prima metà dell'aumento in coda resta 2,25.
- Priorità 2 coperta: 0,11 / 3,88 / 4,61 / 4,61 / 5,06 miliardi; quota rinviata 11,44, uguale alla coda. Prudente ≥ 0 in ogni anno; anni di attivazione della coda invariati. Nello scenario avverso del 2031 slitta il 26,0% dei nuovi ingressi della Priorità 1 (Priorità 1 più grande di 0,22).

**Stabilizzazioni con il perimetro 0,97 (129.765 posti)**

| Anno | Stabilizzate, cumulate | di cui in deroga | Specializzati in deroga con 20.000 l'anno | Non rinnovate, cumulate | Supplenze residue | Comuni su posto vacante | Comuni fino al termine | Sostegno su posto vacante | Sostegno in deroga |
|---|---|---|---|---|---|---|---|---|---|
| 2027 | 19.465 | 15.000 | 20.000 | 2.326 | 214.991 | 27.881 | 64.577 | 12.072 | 110.462 |
| 2028 | 43.601 | 33.600 | 40.000 | 4.652 | 188.529 | 24.986 | 62.251 | 9.430 | 91.862 |
| 2029 | 71.501 | 55.100 | 60.000 | 6.978 | 158.303 | 21.640 | 59.925 | 6.377 | 70.362 |
| 2030 | 109.781 | 84.600 | 80.000 | 9.304 | 117.697 | 17.049 | 57.599 | 2.187 | 40.862 |
| 2031 | 129.765 | 100.000 | 100.000 | 11.630 | 95.387 | 14.652 | 55.273 | 0 | 25.462 |

- Nel 2030 la rampa di spesa chiede 84.600 stabilizzazioni in deroga contro 80.000 specializzati: lo scarto di 4.600 si copre con i supplenti in deroga già specializzati (numero da V37) o slitta al 2031.
- Mancati rinnovi: 8,2% della riduzione delle supplenze al 2031.
- Traguardi al 2031: supplenze su posto vacante 14.652 (sotto 30.000); supplenze in deroga 25.462; supplenze residue totali 95.387, di cui 55.273 comuni fino al termine (precariato strutturale).

**Riserva nei corsi di specializzazione (M24)**
- *Situazione vigente.* Il DM MUR 926 del venerdì 26 giugno 2026 autorizza 30.241 posti per l'XI ciclo; i pareri della Funzione pubblica e del MEF coprono 90.000 posti nel triennio 2024/25–2026/27. Il decreto non prevede quote riservate: chi ha i requisiti dell'art. 4, comma 3-bis, del DM 92/2019 accede direttamente alla prova scritta. Il IX ciclo aveva una riserva del 35% (DM 549/2024, da stampa); per il X ciclo la stampa riferisce che la riserva è venuta meno. I percorsi INDIRE (DL 71/2024, art. 6) sono riservati a chi ha tre anni di servizio sul sostegno: 18.137 specializzati nel primo ciclo (da stampa).
- *Misura.* Una norma primaria fissa ogni anno: riserva del 35% dei posti TFA per i supplenti con almeno tre anni di servizio sul sostegno negli ultimi dieci anni (circa 10.600 su 30.000); percorsi INDIRE resi stabili con circa 9.400 posti l'anno. Totale: 20.000 specializzati in deroga l'anno, a capacità degli atenei invariata. I 0,09 miliardi rendono gratuiti i posti riservati (20.000 × 3.000–3.500 euro = 0,06–0,07 miliardi) e coprono il costo dei percorsi INDIRE.
- *Condizione.* La riserva funziona solo se i supplenti in deroga con tre anni di servizio sono almeno 20.000 l'anno fino al 2031: il dato va chiesto al MIM (V37).

**Platea dell'indennità (M23)**
- Il DM 170 del venerdì 24 giugno 2022 ha ripartito 500 milioni PNRR fra 3.198 scuole secondarie di I e II grado con dispersione implicita INVALSI pari o superiore all'8%. Pesi del riparto: 70% sulla dispersione implicita, 30% sugli iscritti; 51,16% al Mezzogiorno. L'elenco per scuola (allegato 2) è in `dati/scuola/dm170_2022_allegato2.csv`; il totale estratto è di 500 milioni.
- Le 3.198 scuole sono circa il 39% delle istituzioni scolastiche: la platea dell'indennità (5%) va scelta dentro l'elenco. Proposta della redazione (I13): ordinare le scuole per quota per iscritto. È un'approssimazione della dispersione implicita valida dentro ciascuna regione. La primaria resta esclusa fino al dato INVALSI per scuola.

**Serie della dispersione implicita (INVALSI, Rapporto nazionale 2026, slide 2)**

| 2019 | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| 7,5 | 9,8 | 9,7 | 8,7 | 6,6 | 8,7 | 6,3 |

Nel 2020 la rilevazione non si è svolta. L'8,7% compare nel 2023 e nel 2025. Il calo del 2026 segue un aumento nel 2025. Rispetto al 2019, ultimo anno pre-pandemico, il 2026 è più basso di 1,2 punti.

## 16. Voci scolastiche del Piano Lavoro Stabile (D28) (mercoledì 14 ottobre 2026)

**Decise**
- *Scuole difficili.* Assorbite nella M23. La M23 aggiunge il punteggio di carriera per chi resta almeno tre anni, senza costo. Le classi meno numerose restano non finanziate (S13). Perimetro: le 3.198 scuole del DM 170/2022; il 5% si sceglie sui valori INVALSI per scuola (richiesta in `incoerenze/richiesta-invalsi-v38.md`); fino ad allora vale l'ordinamento per quota del riparto per iscritto, dichiarato provvisorio.
- *Tutor.* Il tutor dell'anno di prova esiste già: DM 226 del martedì 16 agosto 2022, art. 12, adottato ai sensi della L. 107/2015, art. 1, comma 118. Il dirigente designa un tutor ogni tre docenti in prova al massimo; il compenso è a carico delle risorse per il miglioramento dell'offerta formativa; l'attività entra nel fascicolo personale. In questa legislatura il programma aggiunge solo il punteggio di carriera per il tutor, senza costo. Le ore riconosciute passano alla seconda legislatura.
- *Organico di rete.* Seconda legislatura, dichiarato nel capitolo sulla scuola come prossimo passo contro le supplenze brevi (0,5–0,6 miliardi netti secondo il file 07).

**Contratti al 31 agosto (da decidere)**
- *Platea.* Supplenze fino al termine residue in ciascun anno, dopo stabilizzazioni (perimetro 0,97) e mancati rinnovi. Dai dati MIM 2024/25 sono a orario parziale il 56% delle supplenze comuni fino al termine (37.489 su 66.903) e il 12% di quelle in deroga (15.291 su 125.462). Con lo spezzone medio pari a mezzo posto (ipotesi da validare): 0,72 posti equivalenti per supplenza comune, 0,94 per supplenza in deroga.
- *Costo lordo.* Luglio e agosto, circa 5.360 euro per posto equivalente (costo della supplenza del registro, da validare).
- *NASpI evitata.* Soglia 2026 di 1.456,72 euro, massimo 1.584,70 (INPS, circolare n. 4/2026). Con una retribuzione media di circa 2.000 euro la NASpI vale circa 1.228 euro al mese; decorre dall'ottavo giorno dopo il 30 giugno, quindi copre circa 55 giorni: circa 2.250 euro per supplente. L'INPS non pubblica il numero dei supplenti della scuola che percepiscono la NASpI estiva né la spesa: la stima assume che tutti la chiedano e va validata con l'INPS (V41). Il costo netto è di circa 3.110 euro per posto equivalente.

| Anno di attivazione | Supplenze comuni fino al termine | Supplenze in deroga | Posti equivalenti | Costo lordo (miliardi) | Costo netto della NASpI (miliardi) |
|---|---|---|---|---|---|
| 2027 | 64.577 | 110.462 | 150.329 | 0,81 | 0,47 |
| 2028 | 62.251 | 91.862 | 131.171 | 0,70 | 0,41 |
| 2029 | 59.925 | 70.362 | 109.286 | 0,59 | 0,34 |
| 2030 | 57.599 | 40.862 | 79.881 | 0,43 | 0,25 |
| 2031 | 55.273 | 25.462 | 63.731 | 0,34 | 0,20 |
| 2032 | 52.947 | 25.462 | 62.056 | 0,33 | 0,19 |

- *Prova in coda davanti a Q15, al costo netto.* Lo scorrimento attiva la voce nel 2030 al costo del 2030 (0,25). La Riforma 19 ridotta (Q10) passa dal 2031 al 2032.
- *Dopo Q10.* La posizione dopo Q10 non basta: lo scorrimento attiva comunque per prima la voce più piccola e Q10 slitta al 2032. Per tenere Q10 nel 2031 serve una regola esplicita: la voce si attiva solo dopo Q10, senza scorrimento davanti a Q10. Con questa regola Q10 resta nel 2031 e i contratti al 31 agosto si attivano nel 2032, a 0,19 miliardi netti. Nello scenario prudente nulla cambia.

**Personale ATA (da decidere)**
- *Dati MIM 2024/25.* 179.295 ATA di ruolo; 56.463 supplenti, di cui 17.781 annuali al 31 agosto (posto vacante) e 38.682 fino al termine (53.457 nel 2023/24). Il dataset non distingue i profili (collaboratori, assistenti, tecnici).
- *Comma 828.* Dal 2026/27 la L. 207/2024 taglia 2.174 posti ATA. Con la stessa regola dei docenti (90% dei posti vacanti meno i posti tagliati) i posti ATA stabilizzabili sono 0,9 × 17.781 − 2.174 = 13.829.
- *Costo della stabilizzazione.* I supplenti annuali hanno già lo stipendio estivo: la stabilizzazione costa la progressione di carriera, circa 1.000–2.000 euro l'anno per posto (stima della redazione, da validare sul Conto annuale RGS): 0,01–0,03 miliardi. Il file 07 indica 0,1–0,2 miliardi: la differenza corrisponde ai contratti al 31 agosto per i 38.682 supplenti fino al termine (lordo 0,15–0,19, netto della NASpI 0,07–0,10, a 2.000–2.400 euro lordo Stato al mese, da validare).
- *Opzioni.* A) stabilizzazione dei 13.829 posti vacanti in Priorità 1, dentro i 6,8 della scuola con l'aumento salariale da 4,19 a circa 4,16 miliardi; B) A più contratti al 31 agosto per gli ATA fino al termine, uniti alla voce di coda dei docenti; C) solo la regola di legge (posto vacante da due anni in ruolo d'ufficio) con attuazione dalla seconda legislatura; D) tutto alla seconda legislatura. La condanna della Corte di giustizia UE sulla reiterazione dei contratti ATA (file 07) rende rischiose C e D.

## 17. Contratti al 31 agosto e personale ATA: decisione (mercoledì 14 ottobre 2026)

**Voce unificata Q16 (docenti e ATA con supplenza fino al termine).** Costo netto della NASpI evitata, sulle supplenze residue dell'anno di attivazione: docenti come nella sezione 16; ATA 38.682 supplenti fino al termine a circa 2.300 euro netti (intervallo 1.900–2.700, da validare), cioè circa 0,09 miliardi.

| Opzione | Regola | Q16 | Riforma 19 ridotta (Q10) | Esito |
|---|---|---|---|---|
| A | davanti a Q15, con scorrimento | 2030, 0,34 | 2033 | scartata: Q10 fuori dal 2032 |
| B | davanti a Q15, solo dopo Q10 | 2032, 0,28 | 2031 | scelta |
| C | docenti davanti a Q15; ATA separati solo dopo Q10 | docenti 2030 (0,25); ATA 2033 | 2032 | scartata: ATA fuori dal 2032 |
| D | come A con costo ATA basso | 2030, 0,32 | 2032 | clausola di anticipo se V41 la conferma |

Soglia di A: con la voce fino a 0,33 miliardi Q10 resta nel 2032; a 0,34 passa al 2033. Scenario prudente: nessuna attivazione cambia in nessuna opzione.

**Clausola di anticipo.** Se l'INPS conferma un costo della NASpI che porta Q16 a 0,32 miliardi o meno, Q16 si anticipa al 2030 senza la regola «dopo Q10» e la Riforma 19 ridotta slitta al 2032, dentro la legislatura.

**Stabilizzazione ATA (M25, Priorità 1).** 13.829 posti vacanti, 0,03 miliardi (estremo alto della stima 0,01–0,03). Rientra nei 6,8 della scuola: l'aumento salariale scende da 4,19 a 4,16 miliardi, circa il 9,2% reale in cinque anni.

| Voce della scuola | Miliardi |
|---|---|
| Resto della scuola in Priorità 2 (M07) | 5,71 |
| Stabilizzazioni dei docenti (M21) | 0,97 |
| Corsi di specializzazione (M24) | 0,09 |
| Stabilizzazione ATA (M25) | 0,03 |
| Totale | 6,80 |

**Effetto sul quadro.** Priorità 2 coperta: 0,11 / 3,87 / 4,58 / 4,58 / 5,03 miliardi; Priorità 2 rinviata 11,44, uguale alla coda; prudente ≥ 0 in ogni anno. Coda nello scenario centrale: Q14 2028; Q01, Q05, Q12 2029; Q02, Q03 2030; Q04, Q06, Q10 2031; Q07 e Q16 2032. Nello scenario avverso del 2031 slitta il 26,1% dei nuovi ingressi della Priorità 1.

**Regola nuova del modello.** La colonna `dopo` di `dati/coda.csv` indica un prerequisito: la voce resta fuori dalla coda attiva e dallo scorrimento finché il prerequisito non è attivo.
