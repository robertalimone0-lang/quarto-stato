# Incoerenze e punti aperti

Registro aggiornato a mercoledì 14 ottobre 2026. Codici: D = decisione richiesta, I = interpretazione adottata da confermare, V = dato da validare, S = conflitto tra sorgenti.

## Decisioni richieste

- **D28. Voci scolastiche del Piano Lavoro Stabile fuori dal quadro.** Organico di rete, contratti al 31 agosto, tutor, scuole difficili e personale ATA valgono circa 0,9–1,2 miliardi al netto dei corsi e oggi non hanno copertura né posto in coda. Da decidere: voce di coda, riduzione o rinvio alla seconda legislatura.
- **D18. Strumenti di build.** Quarto e matplotlib non sono installati: i comandi sono stati proposti il 14 ottobre 2026.

## Decisioni prese il 14 ottobre 2026, seconda tornata (chiuse)

D14 cofinanziamento regionale (classe C fino all'intesa, poi B); D15 cofinanziamento degli investimenti di Fase 1 dal 2028, con saldo avverso 2027 a +0,08 miliardi; D16 quota rinviata di 6,0 miliardi; D17 coda invariata, impegno al 74,5%.

## Decisioni prese il 14 ottobre 2026 (chiuse)

D1 opzione A; D2–D3 ordine e composizione confermati; D4 capitale umano confermato; D5–D6 leve; D7 margine centrale diviso 50% debito e 50% coda; D8 scorrimento con prenotazione; D9 fondo CDP fuori dalla coda; I1–I3 confermate; D10 prenotazione al 50%; D11 proposte A, B, C (in parte), D ed E approvate; D12 sanità circa 6,8% in questa legislatura e 7,0% nella successiva; D13 Priorità 2 del 2027 dal 1° luglio 2027.

## Interpretazioni adottate da confermare

- **I4.** La sanità al 7,0% del PIL vale 0,6 punti di PIL del 2031 (circa 15,9 miliardi). In coda la quota oltre gli 11 miliardi è espressa in due tranche da 2,47 miliardi.
- **I5.** Certificazione: l'attivazione dell'anno Y usa la media degli anni Y-2 e Y-3, sia per le leve sia per l'eccedenza delle coperture rispetto al prudente.
- **I6.** Il debito conta come riduzione tutto ciò che non viene speso: margine, quote del 30% e del 20%, prenotazioni non ancora attivate, contributi.
- **I7.** La cella B13 dell'Excel non viene modificata, perché le sorgenti non si toccano. Il modello si ricostruisce in `dati/debito.py`.
- **I8.** La coda attinge prima alla metà dell'eccedenza delle coperture, poi al gettito delle leve; la regola 50-30-20 si applica al gettito delle leve rimasto libero.
- **I9.** Stime di lavoro, da validare, per due leve nuove: audit sanitario 0 / 0,5 / 1,0 miliardi dal 2029 (prudente, centrale, alta); Riforma 18 tra 0,06 e 0,12 miliardi l'anno. L'aliquota minima sui redditi altissimi resta a zero finché il Dipartimento delle Finanze non la quantifica.

## Dati da validare

- **V6. Precari della scuola.** 182.641 contratti a termine al 24 settembre 2025: dati del Ministero comunicati ai sindacati, riportati da stampa specializzata. Non ho trovato la pubblicazione del MIM né il Conto annuale RGS. Resta da validare.
- **V9.** Stime delle leve (regolarizzazione, rientro, titoli, emersione) costruite su ipotesi dichiarate. Servono microsimulazioni INPS e MEF.
- **V10.** Costo del nuovo regime impatriati (70% poi 50%, tetto 150.000 euro): non stimato.
- **V11.** Popolazione 20–64 anni per convertire i punti di occupazione in persone (circa 345.000 per punto): da leggere su Eurostat.
- **V12.** Contributo delle singole riforme all'obiettivo di occupazione: stime d'ordine di grandezza da sostituire con una microsimulazione.
- **V13. Imposte sulle bevande zuccherate e sulla plastica.** La L. 199/2025 (comma 125) ha spostato la decorrenza al 1° gennaio 2027. Il rinvio è stato contabilizzato come minori entrate nel 2026 (bevande zuccherate 372 milioni secondo l'Osservatorio CPI, 312 secondo un'altra fonte; plastica 73 milioni), quindi il gettito dal 2027 è nel tendenziale. Da verificare: il testo vigente su Normattiva (commi 652 e 676 della L. 160/2019, non leggibili con gli strumenti di questa sessione) e la relazione tecnica originale (A.S. 1586, XVIII legislatura). Rischio: se la legge di bilancio 2027 le rinvia ancora, il tendenziale perde il gettito. Il programma ne vincola l'uso senza contarle come copertura.
- **V14. Immobili non accatastati e affitti passivi.** Valori di lavoro: 0,45 miliardi (rendita presunta di circa 305 milioni secondo il piano dell'Agenzia delle Entrate 2025–2027; stima del 2013 di 589 milioni) e 0,30 miliardi (oltre i 144 milioni di risparmio previsti dal Demanio). Da validare con Agenzia delle Entrate, Dipartimento delle Finanze e Demanio.
- **V15. Incentivi alle imprese senza effetti.** Nessun totale nazionale verificato: la riga resta a zero in classe C.

Chiusi il 14 ottobre 2026:
- **V1. Infermieri:** 7,0 per mille residenti nel 2024 e 6,9 nel 2023 (Istat, audizione del 7 luglio 2026).
- **V3. Spesa delle famiglie:** 42,4 miliardi nel 2025, 22,3% del totale (Istat, Sistema dei conti della sanità, maggio 2026).
- **V8. DPFP:** tutte le cifre confermate dal dossier della Camera del 7 ottobre 2026.
- V2, V4, V5 e V7 erano già chiusi.

## Conflitti tra sorgenti ancora aperti

- **S2.** Il riordino degli incentivi all'assunzione (1,0–1,5 miliardi) copre la Riforma 19, mentre il Piano Lavoro Stabile usa gli stessi bonus per lo sgravio sulle stabilizzazioni.
- **S3.** La sintesi del file 04 dice "circa 11 miliardi", i costi dello stesso file valgono 13. Va scelto quali voci entrano negli 11.
- **S4.** Il file 04 rimanda al registro "F15", che nel file 01 è il costo di cassa delle pensioni.
- **S5.** Il file 08 dichiara che nessuna delle otto misure è applicata altrove; esistono istituti analoghi in Estonia e in Germania. Da verificare.
- **S6.** CLAUDE.md cita come esempio di data "giovedì 2 ottobre 2026": il 2 ottobre 2026 è un venerdì.
- **S7.** Elenco delle soglie solo amministrative da presentare prima della redazione.
- **S8.** Mancano i testi delle Riforme 16 e 17.
- **S9.** L'emersione non cambia il tasso di occupazione Istat, che conta già i lavoratori irregolari. Le sorgenti la presentano come leva dell'occupazione.

## Capitolo 1 (mercoledì 14 ottobre 2026)

- **D19. Condizione europea nella coda.** Il capitolo 1 aggiunge alla coda una seconda condizione di attivazione: la compatibilità con il percorso di spesa netta del Piano rivisto. Le leve fondate su un maggiore adempimento riducono il deficit ma non aprono spazio di spesa nelle regole UE. Va confermata.
- **V16. Trattamento UE di ogni copertura** (colonna `riconoscimento_ue` di `dati/coperture.csv`): classificazione proposta dalla redazione, da concordare con MEF e Commissione nel Piano rivisto.
- **V17. Definizione di spesa netta** (art. 2 del regolamento 2024/1263): letta da fonti secondarie (Consiglio UE, dossier parlamentari) perché EUR-Lex blocca le richieste automatiche. L'articolo 15 è verificato sul testo fornito dall'autrice.
- **V18. Legge n. 243 del 2012.** Il capitolo cita l'istituzione dell'UPB e la disciplina degli scostamenti senza numeri di articolo. Gli articoli (Capo VII per l'UPB, art. 6 per gli scostamenti) vanno verificati su Normattiva prima di citarli.
- **V19.** Quota di popolazione che non ha usato internet (16,9%): riportata dal file 08 con rimando a Istat, non verificata sul comunicato.
- **V20.** Crescita cumulata della spesa netta (6,2% raccomandata, 5,9% tendenziale) e spesa per interessi 2027: lette dalla copia del DPFP di QualEnergia. Il dossier della Camera non le riporta.
- **S10. Pubblicazione.** Il workflow pubblica solo se esiste la variabile `CF_PAGES_PROJECT`; servono i secret `CLOUDFLARE_API_TOKEN` e `CLOUDFLARE_ACCOUNT_ID`.

## Verifica V16 e variante senza riconoscimento (mercoledì 14 ottobre 2026)

- **V16, testo primario trovato.** Il codice di condotta dell'EFC del 1° dicembre 2025 ("Specifications on the Implementation of the Stability and Growth Pact", sez. 1, nota 3) rimanda per la registrazione delle misure discrezionali al Report on Public Finances in EMU 2024 della Commissione (Institutional Paper 325, parte II, cap. 3, "The definition and quantification of fiscal policy measures"). A p. 68: le iniziative contro l'evasione "do not always represent fiscal measures but, if they do, it is appropriate to take a very prudent approach to their quantification"; le azioni che proseguono senza cambiare l'orientamento delle politiche "do not constitute a fiscal policy measure"; le stime ex ante "should therefore remain very prudent" e vanno riviste sul consuntivo e sulla variazione del tax gap. Resta da concordare con la Commissione la classificazione di ogni singola misura della Riforma 1.
- **D20. Scarto di spesa netta nella variante senza riconoscimento.** Non riconosciuti: evasione di Fase 1 (7,0 miliardi), multinazionali e offshore (1,38 al tasso prudente), patrimonio pubblico (0,55), immobili non accatastati (0,32). Scarto prudente: −3,25 miliardi nel 2029, −6,47 nel 2030, −8,28 nel 2031. Decisa il 14 ottobre 2026: Riforma 1 come misure legislative distinte, riconosciute in via prudente per circa 3,85 miliardi, più riserva condizionata (spese fiscali fino al 13,1%, sussidi dannosi +1 miliardo, spending review +1 miliardo), che scatta solo senza riconoscimento e per l'importo necessario.
- **I10.** Il cofinanziamento nazionale degli investimenti è trattato come cofinanziamento di programmi UE ed escluso dalla spesa netta. Va verificato voce per voce: i prestiti BEI restano nella spesa netta.
- **I11.** Le riduzioni di spesa (spending review, affitti passivi, incentivi, risparmi dell'audit sanitario e della Riforma 18) abbassano direttamente la spesa netta.

- **V21. Elenco delle spese fiscali per la riserva condizionata.** Il Rapporto annuale sulle spese fiscali 2025 del MEF (giugno 2026, 573 misure) dà costo, frequenza e beneficio pro capite, ma non la distribuzione per reddito. La distribuzione per decili è stata calcolata sulle statistiche delle dichiarazioni 2025 (anno d'imposta 2024) del Dipartimento delle Finanze, per ventili di reddito complessivo. Limiti:
  - i dati precedono le regole in vigore dal 2025 (tetto alle detrazioni per i redditi oltre 75.000 euro e aliquote ridotte dei bonus edilizi, L. 207/2024), già incluse nel tendenziale: il gettito va ricalcolato sulle regole vigenti;
  - le detrazioni edilizie ed energetiche si fruiscono in rate decennali; applicare la riduzione solo alle spese future rende il gettito graduale, applicarla anche alle rate in corso solleva un problema di affidamento;
  - il gettito delle deduzioni è stimato con l'aliquota marginale per ventile.
- **D21. Rapporto tra riserva e base del riordino.** La base di 11 miliardi non ha ancora l'elenco nominativo (Giorno 2 del calendario di revisione mai svolto). Le voci della riserva vanno tenute fuori dalla base, oppure base e riserva vanno costruite insieme.
- **V22. Riconoscimento della Riforma 1.** Le quote del 75% e del 50% sono una proposta prudente della redazione, da negoziare con la Commissione nel Piano rivisto e da validare con l'UPB.

## Spese fiscali e riserva (mercoledì 14 ottobre 2026)

- **D22 (decisa: ordine dei gradini). Scarto della riserva.** La curva continua sui bonus edilizi, applicata solo alle spese nuove e al netto del tetto della L. 207/2024, rende circa 54 milioni per ogni annualità di spese: 0,21 miliardi nel 2031, 0,43 nel 2035. Nella variante senza riconoscimento la riserva (sussidi dannosi 0,85, spending review 0,65 e curva, valori prudenti) copre 1,61 miliardi nel 2029, 1,66 nel 2030 e 1,71 nel 2031, contro un fabbisogno di 1,32, 3,58 e 4,43. Scarto: +0,29 nel 2029, −1,92 nel 2030, −2,72 nel 2031.
- **V23. Gettito del tetto L. 207/2024.** La relazione tecnica non lo espone separatamente. Il valore di 79 milioni per annualità è dedotto dalla crescita annua della riga IRPEF nella tabella degli effetti dei commi 9 e 10.
- **V24. Flusso delle spese nuove.** Il gettito a regime della curva usa un fattore del 55% (forbice 40–70%) tra il flusso annuo di detrazioni con le regole vigenti (aliquote ridotte dalla L. 207/2024) e lo stock 2024. Da validare con il Dipartimento delle Finanze.
- **V25. Totale delle spese fiscali.** Il Rapporto 2025 indica 122,6 miliardi nel 2026 per 573 misure; le sorgenti usavano 119 miliardi (2025). La base del riordino resta fissata a 11 miliardi nominali.
- **S11. Regime forfettario.** Il reddito forfettario non entra nel reddito complessivo, quindi le tavole per ventile non ne descrivono la distribuzione. Servono le tavole sul quadro LM o l'Osservatorio sulle partite IVA.
- **S12. Redditi finanziari.** Tassati quasi solo alla fonte: non compaiono nelle dichiarazioni e il Rapporto non li censisce come spesa fiscale, salvo i PIR (103 milioni). Per la distribuzione serve l'Indagine sui bilanci delle famiglie della Banca d'Italia.

## Verifica della base (mercoledì 14 ottobre 2026)

- **D23. Base del riordino non ricostruibile.** Con le esclusioni decise, la base realistica vale circa 5,1 miliardi contro 11. Conseguenze: Priorità 2 coperta nel 2031 da 11,4 a 6,9 miliardi; quota in coda da 6,0 a 10,5; saldo avverso 2027 di nuovo negativo (−0,59). Dettaglio in `incoerenze/report-riserva.md`.
- **D24.** La voce 152 (maggiorazione per nuove assunzioni, 1,33 miliardi) è usata due volte: riordino degli incentivi della Riforma 19 e Piano Lavoro Stabile. Va assegnata a una sola misura.
- **V26. Risposta comportamentale alla cedolare.** Evidenze sul 2011 solo da stampa; sconto del 30–50% ipotizzato. Manca uno studio primario.
- **V27. Estrazione del Rapporto 2025.** Il parser ricostruisce 126,7 miliardi di effetti 2026 contro 129,7 ufficiali; 326 misure quantificate lette contro 406. Le voci minori (256 misure, 2,2 miliardi) vanno elencate una per una.
- **D25. Profilo realistico del riordino.** Il massimo mai ottenuto da un riordino è circa 1 miliardo l'anno; gli 11 miliardi lo superano di circa dieci volte. Profili proposti: A) base 4,85 a regime nel 2031; B) base 3,0 a regime nel 2029. In entrambi il buco del 2027 nello scenario avverso riguarda la Priorità 1 (−0,95). Dettaglio in `incoerenze/report-riserva.md`, sezioni 7 e 8.
- **V28.** Esito del riordino della delega 2023 (circa 1 miliardo) da fonti di stampa; gettito del D.Lgs. 216/2023 non trovato nella relazione tecnica.
- **D23 (decisa il 14 ottobre 2026).** Prima casa: rendita dell'abitazione principale imponibile con curva continua da 60.000 a 150.000 euro di reddito complessivo, gettito statico 0,37 miliardi, nella base del riordino come voce sensibile aperta per decisione dell'autrice. Base del profilo A: 5,22 miliardi. Rivedibile con la riforma del catasto. Resta da validare la stima con il Dipartimento delle Finanze (aliquota marginale applicata alla rendita per classe).
- **V29.** I sussidi ambientalmente dannosi (base 6 miliardi e gradino a) da 1 miliardo) non hanno un elenco nominativo: va costruito per escludere che la stessa voce finanzi due misure.
- **V30.** Importi delle relazioni tecniche su Superbonus (DL 176/2022, DL 11/2023, DL 39/2024) e abrogazione dell'ACE (D.Lgs. 216/2023) non reperiti.
- **Decisione del 14 ottobre 2026.** Saldo 2027 nello scenario avverso: si chiude con il rinvio dei nuovi ingressi della Priorità 1 (gradino 4).
- **Decisioni del 14 ottobre 2026.** D25 profilo A (riordino 3,52 + prima casa 0,37); D24 voce 152 al Piano Lavoro Stabile; gradino c) approvato (0,38 prudente, 0,45 centrale); stabilizzazioni degli insegnanti per ultime negli slittamenti.
- **D26 (decisa).** Q15 composta (`dati/q15.csv`), in fondo alla coda, sbloccata dal gettito certificato del contrasto all'evasione. **I12:** la quota di 0,35 attribuita a una rampa più lenta del tempo pieno e delle mense oltre il 2031 è un'interpretazione della redazione da confermare.
- **V31. Riordino degli incentivi della Riforma 19.** Senza la voce 152 il costo netto passa da 0,70 a 1,95 miliardi. Da verificare quali decontribuzioni annuali restano disponibili.
- **V32 (verificata).** Il nuovo TUIR (D.Lgs. 117/2026, art. 104, commi 10-18) riprende la maggiorazione solo per il tempo indeterminato e solo fino al periodo d'imposta 2027. **V34:** l'opzione A richiede una proroga dal 2028 (costo stimato circa 0,67 miliardi, se le trasformazioni sono un terzo delle assunzioni stabili, a saldo zero con la penalità sul turnover) e una deroga al comma 13, che esclude l'agevolazione quando il totale dei dipendenti non cresce, come accade nelle trasformazioni.
- **V33. Voci minori nella base.** 0,66 miliardi (30% di 256 misure) ancora da elencare una per una.
- **Decisioni del 14 ottobre 2026 (seconda tornata).** Riforma 19 ridotta (0,5 miliardi, attivabile nel 2031); stabilizzazioni degli insegnanti in Priorità 1 (0,75); salvaguardia corretta: tutta la Priorità 2 non avviata slitta prima di qualsiasi rinvio della Priorità 1.
- **Q15 non si attiva entro il 2035** in nessuno scenario: richiede che il solo gettito certificato dall'evasione copra 6 miliardi e viene dopo le altre voci della coda.
- **Decisione del 14 ottobre 2026 (superata).** Tranche salariale degli insegnanti dal dividendo demografico calcolato sugli studenti; sostituita dalle decisioni della terza tornata (report, sezione 14).
- **V35. Dividendo demografico.** Calo degli studenti, posti di organico e numero di supplenze vengono da stampa specializzata che riporta dati MIM: servono le pubblicazioni del MIM. Il costo della supplenza annuale (29.500 euro) è una stima della redazione: il Conto annuale RGS non pubblica il costo del personale non di ruolo.
- **V36. Rinnovi 2028–2030.** Gli importi della L. 207/2024 (1.954 / 4.027 / 6.112 milioni) vengono da Ancrel: comma da verificare sul testo della legge.
- **S13. Promessa del file 01 sulle classi.** La Riforma 3 (punto 6) prometteva di usare le risorse del calo degli studenti per classi più piccole nelle zone a rischio di dispersione. Le risorse restano nella scuola e finanziano l'indennità per gli insegnanti delle scuole a rischio di dispersione (M23); le classi più piccole non sono finanziate in questa legislatura.

## Scuola: bacino MIM, dividendo sulle classi, stabilizzazioni (mercoledì 14 ottobre 2026, terza tornata)

- **Decisioni.** Dividendo demografico sulle classi (COP17, 0,30 miliardi nel 2031); indennità M23 sul 5% delle scuole per dispersione implicita INVALSI (0,20 miliardi, circa 48.800 docenti, 338 euro lordo Stato al mese); corsi gratuiti di specializzazione sul sostegno in Priorità 1 (M24, 0,09); i 0,09 di Priorità 2 spostati in coda sono una quota dell'aumento salariale della scuola (Q15 a 5,54); perimetro delle stabilizzazioni 0,75 fino alla decisione D27; traguardi al 2031: meno di 30.000 supplenze su posto vacante (14.652) e 55.227 supplenze in deroga sul sostegno. Dettaglio in `incoerenze/report-riserva.md`, sezione 14.
- **Bacino.** I valori 182.641 e 76.100 sono sostituiti dal dato MIM 2024/25 (236.782 supplenti, di cui 139.664 sul sostegno). La voce `supplenze_annuali_2025_26` resta nel registro come dato di stampa, senza uso nel quadro.
- **V37. Dati MIM per fascia di graduatoria.** Servono, per provincia e ordine di scuola: supplenti per fascia di graduatoria (GPS prima e seconda fascia, MAD), titolo di specializzazione sul sostegno, anni di servizio, posti in deroga ripetuti da almeno due anni. Richiesta al MIM e, in mancanza di risposta entro 30 giorni, istanza di accesso civico generalizzato (D.Lgs. 33/2013, art. 5, comma 2).
- **V38 (superato, vedi quarta tornata).**  Il Rapporto INVALSI 2026 (giovedì 16 luglio 2026) pubblica il dato nazionale (6,3%) e regionale; il dato per istituto va richiesto all'INVALSI, anche con accesso civico generalizzato. Il 6,3% va riscontrato sul rapporto.
- **V39 (aggiornato, vedi quarta tornata).**  Posti TFA (X ciclo 35.784, XI ciclo 30.241) e percorsi INDIRE (18.137 specializzati) da stampa specializzata: vanno riscontrati sui decreti MUR. Manca la quota dei supplenti in deroga già specializzati (V37) e il costo per posto di corso (0,09 miliardi l'anno corrispondono a circa 26.000–30.000 posti a 3.000–3.500 euro, stima della redazione).
- **V40. Dividendo.** Posti di potenziamento tagliati nel tendenziale (1.255 l'anno nel 2027 e 2028) e costo per posto (32.600 euro) da validare. V35 resta aperto per il costo della supplenza.

## Scuola: D27, riserva nei corsi, platea dell'indennità (mercoledì 14 ottobre 2026, quarta tornata)

- **D27 (decisa): opzione A.** L'aumento salariale scende da 4,5 a 4,19 miliardi, circa il 9,3% reale in cinque anni; stabilizzazioni al perimetro massimo (0,97) e corsi (0,09) rientrano nei 6,8 miliardi della scuola (6,8 = 5,74 + 0,97 + 0,09). Q15 torna a 5,45. Dettaglio nel report, sezione 15.
- **S1 (chiuso per stabilizzazioni e corsi).** Stabilizzazioni (0,97) e corsi (0,09) stanno dentro i 6,8 della scuola. Le altre voci scolastiche del Piano Lavoro Stabile non sono nel quadro: organico di rete per le supplenze brevi (0,5–0,6 miliardi netti), contratti al 31 agosto, tutor e scuole difficili (0,4–0,5, di cui i corsi sono una parte), personale ATA in ruolo (0,1–0,2). Il residuo in coda (Q01, 0,55) copre solo la parte fuori dalla scuola. Vedi D28.
- **Riserva nei corsi di specializzazione.** Il DM MUR 926/2026 (XI ciclo, 30.241 posti) non prevede quote riservate: ammette direttamente alla prova scritta chi rientra nell'art. 4, comma 3-bis, del DM 92/2019. Il IX ciclo aveva una riserva del 35% (DM 549/2024, da stampa); per il X ciclo la stampa riferisce che la riserva non c'è più. I percorsi INDIRE (DL 71/2024, art. 6) sono riservati per costruzione a chi ha tre anni di servizio sul sostegno. Il programma fissa per legge: riserva del 35% dei posti TFA (circa 10.600 su 30.000) più percorsi INDIRE annuali per circa 9.400 posti, per 20.000 specializzati in deroga l'anno.
- **V39.** Da riscontrare sui testi: il numero del decreto del X ciclo (436 o 636), la riserva del 35% del IX ciclo (DM 549/2024), il contenuto dell'art. 4, comma 3-bis, del DM 92/2019, gli specializzati INDIRE (18.137) e la proroga dei percorsi al 31 dicembre 2026. Manca il numero dei supplenti in deroga con tre anni di servizio sul sostegno (V37): se è inferiore al fabbisogno, la riserva non arriva a 20.000 l'anno.
- **V38 (in parte chiuso).** Il DM 170/2022 ha ripartito 500 milioni del PNRR fra 3.198 scuole secondarie di I e II grado con dispersione implicita INVALSI pari o superiore all'8% (70% del peso sulla dispersione implicita, 30% sugli iscritti). L'elenco per scuola è pubblicato nell'allegato 2, ora in `dati/scuola/dm170_2022_allegato2.csv` (totale 500 milioni, controllato). Resta da richiedere all'INVALSI il tasso per scuola.
- **I13. Platea iniziale dell'indennità.** Le 3.198 scuole del DM 170 sono circa il 39% delle istituzioni scolastiche statali; l'indennità copre il 5%. La redazione propone di scegliere il 5% dentro l'elenco, ordinando le scuole per quota per iscritto (quota del DM 170 divisa per gli iscritti MIM dello stesso anno). La quota per iscritto riflette la dispersione implicita solo dentro ciascuna regione, perché il riparto regionale pesa l'ELET e riserva il 51,16% al Mezzogiorno. Il DM 170 esclude la primaria. Da confermare.
- **Serie INVALSI (verificata).** Dispersione implicita: 7,5% nel 2019, 9,8% nel 2021, 9,7% nel 2022, 8,7% nel 2023, 6,6% nel 2024, 8,7% nel 2025, 6,3% nel 2026 (Rapporto nazionale 2026, slide 2). L'8,7% compare sia nel 2023 sia nel 2025: il 2025 è un aumento sul 2024. Rispetto al 2019, ultimo anno pre-pandemico, il 2026 è più basso di 1,2 punti.

