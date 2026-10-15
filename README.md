# Quarto Stato

**Programma politico 2028–2032 · Modello finanziario in Python · Documentazione con Quarto**

Quarto Stato è un progetto per elaborare e verificare un programma politico per la legislatura 2028–2032. Integra un modello di finanza pubblica sviluppato in Python, dati strutturati, fonti documentali, simulazioni pluriennali e documenti generati con Quarto.

## Funzionalità

- Modello parametrico di finanza pubblica in Python.
- Simulazione pluriennale di costi, coperture, saldi e debito.
- Scenari centrale, prudente e avverso.
- Registro unitario delle coperture e controlli contro i doppi conteggi.
- Coda di attivazione per le misure subordinate a entrate certificate.
- Regole di salvaguardia e reversibilità.
- Generazione di tabelle e grafici a partire dai dati del modello.
- Tracciabilità di fonti, ipotesi e decisioni metodologiche.
- Test di non regressione per individuare variazioni inattese nei risultati.
- Produzione coordinata del programma politico e del volume tecnico tramite Quarto.

## Tecnologie

- **Python** — modello finanziario e simulazioni.
- **Quarto** — generazione della documentazione.
- **CSV** — registri strutturati di dati e coperture.
- **YAML** — fonti, configurazioni e decisioni metodologiche.
- **JSON** — istantanee di riferimento per i test.
- **Git** — controllo delle versioni.

## Struttura del progetto

Il repository separa il codice di calcolo, i dati, le fonti e la documentazione.

| Percorso | Contenuto |
|---|---|
| `dati/modello.py` | Modello finanziario in Python |
| `dati/grafici.py` | Generazione dei grafici |
| `dati/coperture.csv` | Registro unitario delle coperture |
| `dati/coda.csv` | Misure in attesa di attivazione |
| `dati/leve.csv` | Fonti di entrata e criteri di certificazione |
| `dati/riserva.csv` | Regole della riserva condizionata |
| `dati/perimetro.csv` | Perimetro del modello |
| `dati/fonti.yaml` | Fonti e stato di validazione |
| `dati/decisioni.yaml` | Registro delle decisioni metodologiche |
| `dati/spese_fiscali/base_proposta.csv` | Base delle spese fiscali oggetto di riordino |
| `strumenti/istantanea.py` | Strumento per le verifiche di non regressione |
| `strumenti/istantanea_riferimento.json` | Risultati di riferimento |
| `sorgenti/` | Fonti documentali originali |

I percorsi descrivono l'organizzazione prevista del progetto; la presenza effettiva dei singoli file dipende dalla versione del repository.

## Modello finanziario

Il modello collega ciascuna misura al costo annuale, alla copertura, al profilo di attuazione e agli scenari di rischio.

Le regole fondamentali sono:

1. Una risorsa può finanziare una sola misura.
2. Lo scenario prudente deve mantenere un margine annuale non negativo.
3. Le coperture sono classificate secondo il grado di affidabilità.
4. Le misure condizionate si attivano soltanto quando le entrate strutturali sono certificate e sufficienti.
5. Gli scenari avversi attivano una sequenza prestabilita di salvaguardie.
6. Le prestazioni già riconosciute non vengono ridotte.
7. Le ipotesi non verificate sono identificate come `da validare`.
8. I risultati numerici pubblicati devono provenire dal modello e dai registri, evitando trascrizioni manuali.

## Scenari e coperture

Le simulazioni distinguono gli scenari centrale, prudente e avverso. I profili annuali considerano i costi delle misure, i tassi di realizzazione delle entrate e i tempi di avvio.

Il modello prevede una maggiorazione dei costi del 5% nello scenario prudente e del 10% nello scenario avverso.

Le coperture incerte non sono trattate automaticamente come risorse disponibili. Le misure inserite nella coda di attivazione richiedono entrate strutturali certificate sufficienti a coprire il costo a regime, con un margine aggiuntivo del 10%.

Il sistema contempla verifiche periodiche, conferma annuale dei risultati e sospensione delle nuove attivazioni quando le entrate non sono sufficienti a sostenere le misure già attivate.

## Fonti e metodo

Le fonti statistiche, normative e finanziarie devono essere identificabili e verificabili. Le elaborazioni del progetto restano distinguibili dai dati ufficiali e dalle valutazioni politiche.

Le fonti originali conservate in `sorgenti/` non devono essere modificate. Le eventuali ipotesi non verificate devono essere dichiarate esplicitamente.

Il registro delle decisioni documenta le scelte metodologiche, le alternative considerate e le ragioni delle modifiche al modello.

## Riproducibilità e test

Il progetto prevede test di non regressione basati su `strumenti/istantanea_riferimento.json`.

Ogni modifica che altera i risultati deve essere verificata e motivata. L'aggiornamento dell'istantanea di riferimento deve essere associato alla decisione metodologica pertinente e registrato nel controllo delle versioni.

I comandi di installazione, test e build devono essere definiti sulla base dei file di configurazione effettivamente presenti nel repository.

## Documentazione

Il programma politico e il volume tecnico condividono lo stesso sistema di build basato su Quarto.

Il volume tecnico documenta:

- metodo e regole del modello;
- scenari e analisi di sensibilità;
- coperture e profili di attuazione;
- decisioni metodologiche;
- fonti e dati da validare;
- procedure di riproducibilità.

Tabelle e grafici devono essere generati a partire dai dati e dal modello, mantenendo coerenti i risultati riportati nei diversi documenti.

## Stato del progetto

Il progetto è in sviluppo. Le ipotesi non ancora validate e le decisioni metodologiche aperte devono essere dichiarate nella documentazione.

I risultati delle simulazioni non costituiscono, da soli, una certificazione indipendente delle coperture o della sostenibilità finanziaria.

## Principi di sviluppo

- Tracciabilità delle fonti e delle ipotesi.
- Separazione tra dati, codice e documentazione.
- Assenza di doppi conteggi delle coperture.
- Prudenza nelle stime delle entrate.
- Salvaguardie esplicite per gli scenari avversi.
- Risultati riproducibili e modifiche versionate.
- Accessibilità delle misure pubbliche anche per chi non dispone di conto bancario, computer o smartphone.

---

**Quarto Stato · Orizzonte programmatico 2028–2032**
