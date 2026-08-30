"""Union-resolve a rebase conflict on the vacuity ledger.

Losing an entry here is silent and expensive: main's a0c901f2a landed
BECAUSE a writer deleted other tools' entries and '116 verdicts were one run
away'. So never take a side -- union the keys, and on a key both sides
adjudicated take the LATER `reviewed_at` (ties go to main's, whose file_sha is
fresher). Every subsequent commit in the rebase re-applies on top, so a verdict
I genuinely re-adjudicated today still wins on its own turn.
"""
import json, subprocess, sys, datetime
P='docs/audits/lean-vacuity-review-ledger.json'
def stage(s):
    o=subprocess.run(['git','show',f':{s}:{P}'],capture_output=True,text=True)
    return json.loads(o.stdout) if o.returncode==0 else None
main_doc, mine_doc = stage(2), stage(3)
M, T = main_doc['entries'], mine_doc['entries']
def when(e):
    v=e.get('reviewed_at')
    return v if isinstance(v,str) else ''
out=dict(M)
took_mine=took_main=added=0
for k,v in T.items():
    if k not in out: out[k]=v; added+=1
    elif out[k]!=v:
        if when(v) > when(out[k]): out[k]=v; took_mine+=1
        else: took_main+=1
merged=dict(main_doc)
merged['entries']=out
merged['updated_at']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump(merged,open(P,'w'),indent=2,ensure_ascii=False); open(P,'a').write('\n')
print(f'  union: main {len(M)} + mine {len(T)} -> {len(out)} '
      f'(added {added}, mine-wins {took_mine}, main-wins {took_main})')
