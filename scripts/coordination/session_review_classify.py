import json,sys,re,collections
S=sys.argv[1]
sess=json.load(open(S+'/sess.json')); beans=json.load(open(S+'/beans.json'))
full={p['number']:p for p in json.load(open(S+'/prs.json'))}
pc={int(k):v for k,v in json.load(open(S+'/pr_commits.json')).items()}
RX=r'claude\.ai/code/(session_[A-Za-z0-9]+)'
BATCH=re.compile(r'^(feat/qou-|feat/round|qou-10v9-|claude/round|qou-8lxd-|cat/round|claude/qou-rtxm-|qou-mub3-)')
OPEN={'todo','in-progress','open','draft'}
W1={8523,8522,8365}; W2={8521,8082,8098,8100,7610,7440,7443,7590,7205,6307,6025,6178,7229,7477}
W3={8367,8517,8502,8126,7876,8064,8374}; COORD={8526}
def pr_ws(p):
    n=p['number']
    if n in COORD: return 'COORD'
    if n in W1: return 'W1'
    if n in W2: return 'W2'
    if n in W3: return 'W3'
    if BATCH.match(p['head']) or re.match(r'^(feat|fix)/',p['head']): return 'W4'
    return 'W5'
def topic_ws(t):
    if re.search(r'photon|γγ|\bgg\b|QED|alpha.?em|α_?EM|collider|Feynman|electron observ',t,re.I): return 'W3'
    if re.search(r'mass.endomorph|mass.identity|def:mass|fibre quantum trace|multiplicative integral',t,re.I): return 'W1'
    if re.search(r'float64|precision|dps|witness|producer|dashboard|Q_?β|qbeta|c_k|ladder|binding|AME|CODATA|q0|q₀|convention.?[CD]\b|mass',t,re.I): return 'W2'
    if re.search(r'lean|formaliz|sorry|vacu|axiom|mathlib|devacuif|\bTrue\b',t,re.I): return 'W4'
    if re.search(r'agent|skill|AGENTS|memory|hook|bean|tracker|library|ingest|platform|render|latex|pdf|docs?\b',t,re.I): return 'W8'
    return 'W5'
def kind(t):
    if re.search(r'GAP|derive|deriv|open|conjectur|prove|proof|route|whether|\?|is the|why|identify|closure|mechanism|research|probe',t,re.I): return 'research-open'
    return 'mechanical'
ids=set(beans)
def brefs(t): return set(m for m in re.findall(r'\bqou-[a-z0-9]{4}\b',t) if m in ids)
# PR sessions
s2pr=collections.defaultdict(set)
for n,p in full.items():
    i=set(re.findall(RX,p['body'] or ''))
    if pc.get(n): i|=set(pc[n]['sessions'])
    p['sessions']=sorted(i)
    for x in i: s2pr[x].add(n)
s2b=collections.defaultdict(set); pr2b=collections.defaultdict(set); br2b=collections.defaultdict(set)
for b,v in beans.items():
    for x in v['sessions']: s2b[x].add(b)
    pr=(v['pr'] or '').strip("'\"")
    if pr.isdigit(): pr2b[int(pr)].add(b)
    for br in v['branches']: br2b[br].add(b)
mention=collections.defaultdict(set)
for n,p in full.items():
    for m in set(int(x) for x in re.findall(r'#(\d{3,5})\b',(p['body'] or '')+' '+p['title'])):
        if m>0 and m!=n: mention[m].add(n)
PARENT='session_01AgoHcE'
rows=[]
for s in set(sess)|set(s2pr):
    v=sess.get(s,{'n':0,'first':None,'last':None,'subjects':[]})
    mine=[full[n] for n in sorted(s2pr[s])]
    o=[p for p in mine if p['state']=='open']; m=[p for p in mine if p['merged_at']]; c=[p for p in mine if p['state']=='closed' and not p['merged_at']]
    bs=set(s2b[s])
    for p in mine: bs|=pr2b[p['number']]|br2b.get(p['head'],set())|brefs(p['title']+' '+p['head'])
    ob=sorted(b for b in bs if beans[b]['status'] in OPEN)
    dts=[d for d in [v['first'],v['last']] if d]+[p['created_at'][:10] for p in mine]
    if pc:
        for p in o:
            lc=(pc.get(p['number']) or {}).get('last_commit')
            if lc: dts.append(lc[:10])
    succ={}
    for p in c:
        later=sorted(x for x in mention[p['number']] if x>p['number'] and (full[x]['merged_at'] or full[x]['state']=='open'))
        succ[p['number']]=later
    items=[]
    for p in o:
        items.append({'kind':'pr','id':p['number'],'title':p['title'],'ws':pr_ws(p),'class':'mechanical' if pr_ws(p)=='W4' else kind(p['title']),'batch':bool(BATCH.match(p['head']))})
    for b in ob:
        B=beans[b]
        bprs=[full[n] for n in B['prs'] if n in full]
        allm=bool(bprs) and all(x['merged_at'] for x in bprs if x['number'] in s2pr[s] or True)
        bopen=[x for x in bprs if x['state']=='open']
        ws=pr_ws(bopen[0]) if bopen else topic_ws(B['title'])
        if not bopen and ws in ('W4','W5','W8'): ws='NEW-R' if ws!='W8' else 'NEW-P'
        stale = (not bopen) and allm and B['status']=='in-progress'
        items.append({'kind':'bean','id':b,'title':B['title'],'status':B['status'],'type':B['type'],'ws':'NEW-H' if stale else ws,
          'class':'mechanical' if stale else kind(B['title']),'stale_close_candidate':stale,'updated':B['updated']})
    real=[i for i in items if not i.get('stale_close_candidate')]
    if real: cls='HAS-OUTSTANDING-WORK'
    elif c and not m and all(succ[x] for x in succ): cls='SUPERSEDED-BY '+','.join('#%d'%min(succ[x]) for x in succ)
    else: cls='COMPLETE'
    short=s[8:20]
    rows.append({'session':s,'url':'https://claude.ai/code/'+s,'short':short,'parent':PARENT if re.match(r'session_(01Qmmkt|0151ZZJ)',s) else None,
      'main_commits':v['n'],'first':min(dts) if dts else None,'last':max(dts) if dts else None,
      'subjects':(v['subjects'][:2]+v['subjects'][-1:]) if v['subjects'] else [p['title'] for p in mine[:2]],
      'prs_merged':len(m),'prs_open':[p['number'] for p in o],'prs_closed_unmerged':[p['number'] for p in c],'closed_successors':succ,
      'class':cls,'items':items,'real_session_id': not s.startswith('session_01E66739')})
rows.sort(key=lambda r:(r['last'] or '',r['session']),reverse=True)
json.dump(rows,open(S+'/rows2.json','w'),indent=1,ensure_ascii=False)
print(len(rows),collections.Counter(r['class'].split()[0] for r in rows))
it=[i for r in rows for i in r['items']]
print(collections.Counter((i['kind'],i['ws'],i['class']) for i in {(i['kind'],i['id']):i for i in it}.values()))
