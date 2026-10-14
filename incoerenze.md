# Incoerenze e punti aperti

Registro aggiornato a mercoledì 14 ottobre 2026. Codici: D = decisione richiesta, I = interpretazione adottata da confermare, V = dato da validare, S = conflitto tra sorgenti.

## Decisioni richieste

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

- **S1.** La parte scolastica del Piano Lavoro Stabile (1,6–2,1 miliardi) dovrebbe stare dentro i 6,8 della scuola, che però prevedono 0,5–1 per la stabilizzazione.
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
