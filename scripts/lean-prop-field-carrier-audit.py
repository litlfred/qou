#!/usr/bin/env python3
"""Shape A: a class/structure field of BARE type `Prop`, plus a sibling field
whose type IS that field.  An instance may then take the Prop field to be `True`
and discharge its partner with `trivial`, so the docstring's equation is never
encoded.  Verified instance: HeckeAlgebra.WedderburnDecomposition (qou-qcy6)."""
import re, sys, pathlib
sys.path.insert(0,'scripts/lib')
from lean_decl_scan import blank_comments

CARRIER = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*'
                     r'(class|structure)\s+([A-Za-z_][A-Za-z0-9_\'.]*)')
FIELD   = re.compile(r'^\s{1,}([A-Za-z_][A-Za-z0-9_\']*)\s*:\s*(.+?)\s*$')

hits=[]
for p in pathlib.Path('folio').rglob('*.lean'):
    src=blank_comments(p.read_text(encoding='utf-8',errors='replace'))
    lines=src.split('\n')
    cur=None; fields={}; start=0
    def flush():
        global cur,fields
        if not cur: return
        props={n for n,t in fields.items() if t.strip()=='Prop'}
        for n,t in fields.items():
            if t.strip() in props and n not in props:
                hits.append((str(p), start, cur, t.strip(), n))
        cur=None; fields={}
    for i,ln in enumerate(lines):
        m=CARRIER.match(ln)
        if m: flush(); cur=m.group(2); start=i+1; fields={}; continue
        if cur is None: continue
        if ln.strip() and not ln[0].isspace(): flush(); continue
        f=FIELD.match(ln)
        if f: fields[f.group(1)] = f.group(2)
    flush()
seen=set(); out=[]
for h in hits:
    k=(h[0],h[2],h[3],h[4])
    if k in seen: continue
    seen.add(k); out.append(h)
print(f"SHAPE A candidates: {len(out)}  across {len({h[0] for h in out})} files\n")
for f,l,c,pf,proof in out:
    print(f"  {c}.{proof} : {pf}   {f.split('/')[-1]}:{l}")
