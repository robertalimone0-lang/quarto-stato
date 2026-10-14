# Quarto Stato — Regole del progetto

## Cos'è
Programma politico del partito Quarto Stato, redatto come un business plan pubblico: riforme, coperture certificate, modello del debito, tre fasi di attuazione. Le sorgenti originali sono in `sorgenti/` e non si modificano.

## Registro
- Italiano tecnico-istituzionale, come redatto da un gruppo di esperti di macro e microeconomia, finanza pubblica, politica interna e welfare.
- Frasi dirette, affermative e concise. Niente retorica, slogan, immagini a effetto, formule o ridondanze.
- Mai costruzioni antitetiche negazione-affermazione ("non è X: è Y", "non... ma...", "X, non Y").
- Linguaggio schietto, senza cautele diplomatiche, anche quando si criticano attori politici o economici.
- Date sempre complete (es. "giovedì 2 ottobre 2026").

## Metodo
- Ogni numero viene da una fonte primaria verificata e aggiornata: ISTAT, MEF, Banca d'Italia, UPB, RGS, Eurostat, Gazzetta Ufficiale, norme vigenti. Mai inventare dati, norme o studi.
- Un numero non verificato resta nel testo marcato "da validare" e nel registro `dati/fonti.yaml` con stato `da_validare`.
- Le tendenze si misurano rispetto al periodo pre-pandemico, mai sugli anni della pandemia.
- Le misure si fondano sul diritto e sui dati italiani. I confronti esteri sono ammessi solo se la misura è stata attuata, ha risultati misurati ed è trasferibile all'Italia.
- Le innovazioni mai sperimentate sono ammesse se analiticamente solide: problema misurato, meccanismo esplicito, aggiramenti previsti, sperimentazione con gruppo di confronto prima dell'estensione.
- Ogni misura deve funzionare anche per chi non ha conto corrente, computer o smartphone.

## Regole finanziarie
- Mai spendere oggi entrate incerte di domani. Coperture classificate per affidabilità (classi A, B, C).
- Una sola tabella delle coperture (`dati/coperture.csv`): nessuna risorsa può finanziare due misure.
- Regola di fondo: lo scenario prudente chiude ogni anno con margine maggiore o uguale a zero. Ogni voce che lo porta sotto zero passa alla coda di attivazione (Fase 2 o 3), condizionata a gettito certificato.
- Il margine si ricalcola anno per anno dal profilo dello scenario centrale (metodo del piano 02). Nessun valore fisso. La parte delle coperture che a consuntivo supera lo scenario prudente, certificata dall'UPB, va per il 50% alla riduzione del debito e per il 50% alla coda di attivazione. Il resto del margine va alla riduzione del debito (Sezione 1).
- Clausola di salvaguardia: se il consuntivo segue lo scenario avverso, i congelamenti scattano in quest'ordine automatico: 1) sospensione di tutte le attivazioni della coda; 2) rinvio delle voci di Priorità 2 non ancora avviate; 3) rallentamento dei profili di avvio della Priorità 2 già avviata; 4) per la Priorità 1, solo il rinvio dei nuovi ingressi, mai la riduzione delle prestazioni già riconosciute.
- Gettito dall'evasione oltre lo scenario prudente: 50% riduzione dell'IRPEF sui redditi bassi e medi, 30% debito, 20% riserva.
- Evasione: scenari 8 / 14,5 / 18,5 miliardi (revisione del Giorno 1). Il traguardo del 12% di propensione è un obiettivo di legislatura e resta fuori dalle coperture.
- Scenari finanziari: metodo per voce, con tassi di realizzazione e rampe d'avvio; costi +5% nel prudente e +10% nell'avverso.
- Gioco d'azzardo e patrimonio pubblico stanno in tabella in classe C e non coprono mai la Priorità 1.
- Coperture aggiunte: immobili non accatastati (classe B); affitti passivi dello Stato al netto del risparmio già previsto dal Demanio (classe B); incentivi alle imprese senza effetti (classe C finché una valutazione con gruppo di confronto non quantifica il risparmio).
- Imposte sulle bevande zuccherate e sulla plastica: già legge (L. 160/2019), decorrenza 1° gennaio 2027 (L. 199/2025), gettito già nel tendenziale. Non sono coperture nuove. Il programma vincola il gettito dell'imposta sulle bevande zuccherate alla prevenzione sanitaria e si impegna a non rinviarle più.
- Minore costo del debito e recupero delle imposte dichiarate e non versate: solo alla riduzione del debito, mai in somma alle stime della Riforma 1.
- Entrate regionali (canoni delle acque minerali, grandi derivazioni idroelettriche): meccanismo di cofinanziamento regionale. Una legge statale fissa un canone minimo nazionale con curva continua (art. 117, secondo comma, lettere e ed s); la Regione destina il maggior gettito a trasporto locale, alloggi e prevenzione; lo Stato riduce di pari importo il proprio finanziamento delle stesse voci; la Regione trattiene una quota come incentivo. Classe C fino all'intesa in Conferenza Stato-Regioni, classe B dopo. Nessuna riduzione diretta dei trasferimenti (art. 119).
- Tutte le coperture di classe A e B si approvano nella prima legge di bilancio, con calendario pubblico di soppressione delle agevolazioni. La Priorità 2 del 2027 parte dal 1° luglio 2027; il cofinanziamento degli investimenti di Fase 1 parte nel 2028. La regola è fissa e non dipende dai dati del primo trimestre.
- Contributi previdenziali di regolarizzati e lavoratori emersi: solo alla riduzione del debito o al saldo INPS, mai a nuova spesa permanente. Parte fiscale e parte contributiva si calcolano separatamente.
- Nessun condono: ravvedimento al posto delle sanatorie fiscali. Tutte le soglie che determinano importi, aliquote o sanzioni sono curve continue, senza scalini; restano solo le soglie amministrative che non producono salti d'imposta, elencate una per una. Le piccole imprese, gli artigiani e i commercianti sono tutelati dalle misure contro la grande evasione.

## Attivazione condizionata
- Le misure fuori totale entrano in una coda di attivazione (`dati/coda.csv`). Ciascuna parte quando le leve di entrata hanno prodotto gettito certificato sufficiente a coprirla in modo permanente.
- Leve di entrata nel registro `dati/leve.csv`: fonte del dato, metodo di misura, ritardo della misura, organo che certifica, stima prudente, centrale e alta.
- Conta solo il gettito a consuntivo. Certifica l'Ufficio parlamentare di bilancio con una Relazione annuale sul gettito delle riforme, prima della legge di bilancio. Il gettito è netto dei costi della leva ed è strutturale, corretto per il ciclo. La certificazione è trimestrale, sui dati di cassa, con media mobile delle ultime quattro trimestralità; l'UPB la conferma ogni anno sul consuntivo, e se la conferma annuale smentisce il dato trimestrale scatta la reversibilità.
- Una misura si attiva con la legge di bilancio successiva quando il gettito certificato disponibile copre il suo costo a regime più un margine di sicurezza del 10%. Ordine della coda: Q01–Q14, deciso dall'autrice.
- Scorrimento: se la voce successiva non è coperta, si attiva la prima voce minore coperta. La voce bloccata accumula una prenotazione pari al 50% delle risorse libere di ogni anno successivo.
- Leve: evasione oltre la quota di Fase 1, regolarizzazione (IRPEF e IVA), rientro dei cervelli al netto delle esenzioni, titoli esteri se misurabili, cannabis dal 2030, risparmi certificati dell'audit sanitario e della Riforma 18, aliquota minima sui redditi altissimi. Il dividendo dell'occupazione compare solo come scenario di confronto. I risparmi della cannabis su polizia e tribunali restano fuori.
- Il fondo CDP per le imprese dei rientrati è una sezione di CDP Venture Capital finanziata con risorse proprie: nessun costo per lo Stato, fuori dalla coda.
- Reversibilità: se per due anni consecutivi il gettito certificato scende sotto il costo delle misure attivate, si sospendono le attivazioni successive e si usa la riserva. Le prestazioni già riconosciute non si riducono.
- Ripartizione: il gettito certificato delle leve copre prima la coda; la regola 50-30-20 si applica al resto.
- Condizione europea (D19): una misura in coda si attiva solo se, oltre al gettito certificato, è compatibile con il percorso di spesa netta del Piano rivisto. Coprono spesa ai fini UE solo le misure discrezionali di entrata e le riduzioni di spesa.
- Riforma 1 per le regole UE: ogni misura contro l'evasione è una misura legislativa distinta con stima di gettito ex ante validata dall'UPB, con l'indicazione se si qualifica come misura discrezionale di entrata. Il gettito non attribuibile a una misura specifica va solo al debito. Riferimento: Commissione europea, Report on Public Finances in EMU 2024 (Institutional Paper 325), parte II, cap. 3: le iniziative contro l'evasione sono misure solo se cambiano l'orientamento delle politiche; la stima ex ante va tenuta molto prudente e rivista sul consuntivo e sul tax gap.
- Finché la classificazione non è concordata con la Commissione, il quadro presenta due varianti: evasione riconosciuta e non riconosciuta.
- Riconoscimento prudente della Riforma 1 (D20): IVA e imposte dichiarate e non versate al 75% (versamento automatico dell'IVA e riscossione automatica); IRPEF di autonomi e imprese al 50% (ritenute sugli incassi, tracciabilità, incarico digitale); controlli amministrativi solo al debito.
- Riserva condizionata (D20): il riordino delle spese fiscali resta al 10% come base. La quota aggiuntiva fino al 13,1%, l'ampliamento del taglio dei sussidi ambientalmente dannosi (+1 miliardo netto) e la spending review aggiuntiva (+1 miliardo) sono approvati per legge nella prima legge di bilancio. Scattano solo se nel negoziato sul Piano rivisto la Commissione non riconosce le misure contro l'evasione, e solo per l'importo necessario a chiudere lo scarto di spesa netta di quell'anno.
- Equità del riordino aggiuntivo: solo spese fiscali con beneficio concentrato sui decili di reddito più alti. Escluse le detrazioni per lavoro dipendente e pensione, le spese sanitarie dei redditi sotto la soglia ISEE del programma e gli strumenti contro la povertà. Analisi distributiva sul Rapporto annuale sulle spese fiscali del MEF.
- Sussidi ambientalmente dannosi: compensazioni per le famiglie a basso reddito, già incluse nel calcolo al netto.

## Decisioni già prese (non modificare senza istruzione esplicita)
- Programma in tre fasi: 1) diritti, legalità, lavoro stabile, burocrazia; 2) trasporti, strade, assicurazioni, energia; 3) meno tasse, meno debito, inflazione. Debito e protezione dai rincari attivi dal primo giorno.
- Nessun incentivo alla natalità; Assegno Unico Universale invariato. Le risorse nuove vanno al capitale umano e al rientro dei cervelli.
- Art. 44 DL 78/2010 invariato nella misura; regime impatriati al 70% poi 50%, con tetto di 150.000 euro di reddito agevolabile.
- Regolarizzazione degli stranieri presenti, con esclusione dei condannati per delitti non colposi, sospensione per indagati e imputati, rigetto in presenza di misure cautelari, revoca ed espulsione per condanne successive.
- Conversione dei titoli di studio esteri nel titolo italiano analogo, con procedura unica nazionale.
- Difesa: priorità all'esercito europeo, nessun aumento gonfiato della spesa militare nazionale. Spiagge ad accesso libero. Cannabis in Fase 2, gettito dal 2030.
- Per ogni tema vale la versione più recente delle sorgenti (02, 03, 04, 07, 09, Excel). I testi che si aggiungono senza sostituirsi si uniscono.
- Numerazione per fase con codici stabili (es. F1-R01); tabella di corrispondenza con la vecchia numerazione in appendice.
- Riforma 16 (sex work): Fase 2, fuori totale, testo da recuperare. Riforma 17 (assicurazioni): Fase 2, parte sanitaria del 04 più misure RC auto del 01, testo completo da recuperare.
- Sanità: 11 miliardi a regime in Fase 1. Obiettivo di questa legislatura: la quota raggiunta nello scenario centrale, circa 6,8% del PIL nel 2031. Il 7,0% è obiettivo della legislatura successiva. La quota eccedente sta in coda, in euro, in due tranche da 2,47 miliardi, con la quota di PIL raggiunta in ogni scenario.
- Capitale umano: nessun aumento del riordino delle spese fiscali; costi ridotti e scaglionati.
- Riforma 14: dotazione originale (0,4 miliardi). Le voci assegnate da 04, 05, 08 e 09 sono righe proprie nella tabella unica, con costo e copertura.
- Congedo di paternità solo nella riforma del lavoro. Nessuna dote alla nascita né dote sostitutiva.
- Contratti a termine: regole del Piano Lavoro Stabile (07), con le tutele "Porte aperte a chi cerca lavoro". Il modello spagnolo è citato solo come rischio da evitare.
- Emersione dei rapporti di lavoro: il datore versa integralmente i contributi dovuti, con sanzioni ridotte secondo il ravvedimento; la non punibilità riguarda solo il reato di impiego irregolare, mai lo sfruttamento.
- Ravvedimento per i redditi bassi: sanzioni ridotte con curva continua crescente dal reddito zero.
- Tenure track: testo unico nel capitolo capitale umano (09), con la conversione degli assegni prevista dal 07.
- Versamento automatico dell'IVA nei pagamenti elettronici al consumo per tutti; split payment solo per i grandi fornitori della PA.
- Occupazione: impegno al 74,5% nel 2031 per la fascia 20-64 anni, circa 1 punto sopra la tendenza Eurostat 2015-2019 prolungata, raggiungibile senza la Riforma 19. Il 75% è un risultato possibile se la Riforma 19 si attiva prima; la sua posizione in coda non cambia. Il capitolo sul lavoro dichiara che pensioni, scuola e casa precedono la Riforma 19 per scelta politica. Le stime vanno sostituite da una microsimulazione prima della pubblicazione.
- Priorità 2 rinviata: 6,0 miliardi in coda; 0,5 miliardi di diritto allo studio e tempo pieno restano in Fase 1.
- Ordine di scrittura: 1) Principi e metodo; 2) Quadro macroeconomico e di finanza pubblica; 3) riforme di Priorità 1, una per sessione, con la scheda obbligatoria. Prima di ogni capitolo la scaletta; dopo, il riepilogo delle modifiche e dei dati da validare.
- Modello del debito: base tendenziale del DPFP del 2 ottobre 2026; il programmatico con la clausola per la difesa è uno scenario di confronto. Avanzo aggiuntivo anno per anno dal modello del programma.
- Grafici rigenerati nella build dai dati aggiornati; le versioni del 9 ottobre 2026 non entrano nel documento.

## Come lavorare
- Prima di scrivere o modificare file, mostra il piano e attendi l'approvazione.
- Una sezione alla volta.
- Mai perdere progressi già concordati né tornare a versioni precedenti.
- Quando due sorgenti sono in conflitto, segnala il conflitto in `incoerenze.md` e lascia la decisione all'autrice. Non scegliere da solo.
- Pubblicazione: GitHub → Cloudflare Pages. Comandi sempre pronti da incollare; verifica i percorsi dei file prima di copiarli o spostarli.
