"""For each shape-A candidate, count what READS the Prop field and its proof.

The discriminator between vacuous-and-harmless and vacuous-and-load-bearing is
consumption: a write-only pair misleads a reader but corrupts nothing, while a
consumed one propagates the unencoded claim into whatever reads it.
"""
import re, subprocess, sys
out=subprocess.run(['python3','scripts/lean-prop-field-carrier-audit.py'],capture_output=True,text=True).stdout
cands=[]
for ln in out.split('\n'):
    m=re.match(r'\s+([A-Za-z_][\w.]*)\.(\w+) : (\w+)\s+(\S+):(\d+)',ln)
    if m: cands.append(dict(carrier=m.group(1),proof=m.group(2),prop=m.group(3),file=m.group(4),line=int(m.group(5))))
def n(pat):
    r=subprocess.run(['grep','-rn','--include=*.lean',pat,'content/'],capture_output=True,text=True)
    return [l for l in r.stdout.split('\n') if l.strip()]
rows=[]
for c in cands:
    reads_prop  = n(r'\.'+c['prop']+r'\b')
    reads_proof = n(r'\.'+c['proof']+r'\b')
    rows.append((c, len(reads_prop), len(reads_proof)))
rows.sort(key=lambda r: -(r[1]+r[2]))
wo=[r for r in rows if r[1]+r[2]==0]
print(f"{len(rows)} candidates | WRITE-ONLY (0 readers of either): {len(wo)} | consumed: {len(rows)-len(wo)}\n")
print("CONSUMED — the ones that propagate:")
for c,a,b in rows:
    if a+b: print(f"  prop={a:3d} proof={b:3d}  {c['carrier']}.{c['prop']}   {c['file']}")
