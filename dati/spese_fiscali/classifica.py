import csv, sys
# E = esclusa per decisione o vincolo; L = rate di bonus edilizi gia avviati (affidamento); R = voce della riserva;
# S = regime sostitutivo (serve decisione); X = gia nei sussidi ambientalmente dannosi (doppio conteggio);
# C = candidata alla base; K = candidata sensibile (casa, istruzione, terzo settore, premi di produttivita)
CL = {
213:("L","Recupero edilizio, rate in corso"),456:("E","Cuneo fiscale lavoratori dipendenti"),304:("E","Assegno unico non imponibile"),
233:("K","Spese sanitarie al 19% (solo sopra la soglia ISEE)"),398:("E","Pensioni di guerra, invalidita e rendite esenti"),
187:("K","Deduzione della rendita dell'abitazione principale"),550:("S","Regime forfettario"),208:("S","Cedolare secca"),
391:("E","Previdenza complementare"),219:("L","Bonus facciate, rate in corso"),205:("L","Ecobonus, rate in corso"),
211:("L","Superbonus, rate in corso"),185:("K","Registro al 2% sulla prima casa"),169:("C","Crediti d'imposta per investimenti delle imprese"),
181:("C","Esenzioni dall'imposta sulle assicurazioni"),188:("K","Interessi sui mutui per la prima casa"),152:("C","Maggiorazione del costo del lavoro per nuove assunzioni (IRES)"),
64:("X","Agevolazioni sulle accise (sussidi dannosi)"),110:("E","Regime impatriati (CLAUDE.md)"),198:("K","Catastale fissa sulla prima casa"),
400:("E","Vitto e mense dei lavoratori"),232:("C","Deduzione dei contributi ai fondi sanitari integrativi"),434:("K","Premi di produttivita al 5%"),
139:("C","Riallineamento fiscale dell'avviamento"),277:("K","Spese di istruzione al 19%"),215:("R","Bonus mobili (riserva sulle spese nuove)"),
425:("C","Compensi sportivi dilettantistici esenti"),388:("C","Sostitutiva sulle prestazioni svizzere di prepensionamento"),214:("L","Sismabonus acquisti, rate in corso"),
87:("K","IRES delle cooperative sulla riserva obbligatoria"),71:("C","Tonnage tax"),283:("E","Rientro di docenti e ricercatori (art. 44)"),
57:("C","Agevolazioni di registro sui trasferimenti di terreni"),231:("E","Spese mediche per disabili"),197:("K","Ipotecaria fissa sulla prima casa"),
153:("C","Credito d'imposta investimenti Mezzogiorno"),195:("C","Riduzione forfettaria del reddito dei fabbricati locati"),
455:("E","Ulteriore detrazione per lavoratori dipendenti"),441:("E","Trattamento integrativo"),136:("S","PIR-PMI (redditi finanziari)"),
146:("E","IVA: note di variazione nelle procedure concorsuali"),129:("C","Superammortamento"),192:("E","Affitti dei giovani a basso reddito"),
428:("E","Rivalutazione del TFR"),302:("E","Assegni periodici al coniuge separato"),317:("C","Premi assicurativi vita e infortuni al 19%"),
224:("E","Barriere architettoniche"),431:("E","Indennita di fine rapporto minime"),170:("C","Patent box"),78:("C","Registro internazionale navale"),
305:("E","Assegni per i figli dei genitori separati"),438:("E","Indennita di fine servizio"),499:("C","IVA monofase editoria"),
301:("E","IRES ridotta per enti di beneficenza e istruzione"),412:("C","Fringe benefit sulle auto aziendali"),72:("C","Rivalutazione dei beni d'impresa"),
303:("E","Nuclei senza figli"),422:("C","Intramoenia: reddito al 75%"),386:("E","Contributi colf e badanti"),315:("K","Spese funebri al 19%"),
242:("E","Prestazioni aggiuntive in sanita (Riforma 4)"),264:("C","Credito d'imposta cinema"),461:("X","Accise nelle zone franche (sussidi dannosi)"),
131:("C","Iperammortamento"),279:("E","Spese per asili nido"),121:("S","PIR delle casse previdenziali"),147:("S","Proventi da OICR"),
288:("E","Anticipazioni della previdenza complementare"),63:("K","IRES delle cooperative"),423:("C","Voce 423"),
}
r=[x for x in csv.DictReader(open(sys.argv[1])) if x['e2028']]
agg={}; rest=0; restn=0
out=[]
for x in r:
    n=int(x['n']); v=-float(x['e2028'])
    if n in CL:
        c,l=CL[n]; agg[c]=agg.get(c,0)+v; out.append((n,c,l,v,x['e2026'],x['tributo'],x['missione']))
    else:
        rest+=v; restn+=1
tot=sum(agg.values())+rest
for c in "CKSRXLE": print(c, round(agg.get(c,0)/1000,2))
print("non classificate (voci minori)", restn, round(rest/1000,2), "totale 2028", round(tot/1000,2))
w=csv.writer(open(sys.argv[2],'w',newline='',encoding='utf-8')); w.writerow(["n","classe","voce","effetto_2028_mln","effetto_2026_mln","tributo","missione"])
for o in sorted(out,key=lambda o:-o[3]): w.writerow([o[0],o[1],o[2],round(o[3],1),o[4],o[5],o[6]])
