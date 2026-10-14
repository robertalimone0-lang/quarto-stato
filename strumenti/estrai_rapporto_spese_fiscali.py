import re, sys, csv
L=open(sys.argv[1],encoding='utf-8').read().splitlines()
start=re.compile(r'^\s{1,8}(\d{1,3})\s{2,}\S')
VAL=r'(-?\d{1,3}(?:\.\d{3})*,\d+|Non quantificabile|Trascurabile|trascurabile|n\.d\.|-)'
EFF=re.compile(VAL+r'\s{2,}'+VAL+r'\s{2,}'+VAL)
TRIB=re.compile(r'\b(IRPEF/IRES/IRAP|IRPEF/IRES|IRES/IRAP|IRPEF|IRES|IRAP|IVA|ACCISE|ACCISA|ALTRO|IMPOSTA DI REGISTRO|REGISTRO|IPOTECARIA|BOLLO|IMU|SUCCESSIONI)\b')
miss=None; blocks=[]; cur=None
for i,l in enumerate(L):
    m=re.search(r'MISSIONE\s+(\d+):\s*(.+?)\s*$',l)
    if m: miss=m.group(1)+' '+m.group(2).strip()
    s=start.match(l)
    if s and (cur is None or int(s.group(1))==cur['n']+1 or (cur and int(s.group(1))>cur['n'])):
        if cur: blocks.append(cur)
        cur={'n':int(s.group(1)),'lines':[l],'missione':miss}
    elif cur: cur['lines'].append(l)
if cur: blocks.append(cur)
def num(x):
    if x in ('Non quantificabile','n.d.','-'): return None
    if x.lower()=='trascurabile': return 0.0
    return float(x.replace('.','').replace(',','.'))
out=[]
for b in blocks:
    txt='\n'.join(b['lines'])
    effline=next((l for l in b['lines'] if EFF.search(l) and re.search(r'(A REGIME|\b20\d\d\b|TEMPORANE|PERMANENTE)',l[:EFF.search(l).start()]) and 'otale' not in l),None) or next((l for l in b['lines'] if EFF.search(l) and 'otale' not in l and 'di cui' not in l),None)
    e=EFF.search(effline) if effline else None
    trib=TRIB.search(effline or txt)
    desc=' '.join(re.sub(r'\s+',' ',l[80:225]).strip() for l in b['lines'] if l[80:225].strip())
    tail=effline[e.end():] if e else ''
    nums=re.findall(r'-?\d{1,3}(?:\.\d{3})*(?:,\d+)?',tail)
    cat=' '.join(re.findall(r'(PERSONE FISICHE|IMPRESE|SOGGETTI E|CATEGORIE|PARTICOLARI|ENTI|LAVORATORI|FAMIGLIE|NON RESIDENTI|PENSIONATI|CONTRIBUENTI)',txt))
    out.append(dict(n=b['n'],missione=b['missione'],tributo=trib.group(1) if trib else '',
        e2026=num(e.group(1)) if e else None,e2027=num(e.group(2)) if e else None,e2028=num(e.group(3)) if e else None,
        frequenze=nums[0] if nums else '',pro_capite=nums[1] if len(nums)>1 else '',categoria=cat,descrizione=desc[:400]))
w=csv.DictWriter(open(sys.argv[2],'w',encoding='utf-8',newline=''),fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
q=[o for o in out if o['e2026'] is not None]
print('misure',len(out),'max n',max(o['n'] for o in out),'quantificate',len(q),'totale 2026',round(sum(o['e2026'] for o in q),1))
