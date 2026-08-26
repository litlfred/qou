#!/usr/bin/env python3
"""Assertions whose computed and expected are the SAME expression -- vacuous for
all data, not merely at zero. The compute-side `theorem X : X = X := rfl`."""
import ast, subprocess, sys
sys.path.insert(0,"computations/audits")
from _source_normalise import code_only
files=[p for p in subprocess.run(["git","ls-files","computations"],capture_output=True,
       text=True).stdout.split() if p.endswith(".py") and "_deprecated" not in p]
hits=[]
for f in files:
    try: tree=ast.parse(code_only(open(f,encoding="utf-8").read()))
    except Exception: continue
    for n in ast.walk(tree):
        if not (isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute)
                and n.func.attr=="add_assertion"): continue
        kw={k.arg:k.value for k in n.keywords if k.arg}
        c,e=kw.get("computed"),kw.get("expected")
        if c is None or e is None: continue
        try:
            if ast.dump(c)==ast.dump(e):
                nm=kw.get("name")
                nm=nm.value if isinstance(nm,ast.Constant) else (
                    n.args[0].value if n.args and isinstance(n.args[0],ast.Constant) else "?")
                hits.append((f,n.lineno,ast.unparse(c),str(nm)))
        except Exception: pass
print(f"producers scanned: {len(files)}")
print(f"assertions with IDENTICAL computed and expected: {len(hits)}\n")
for f,ln,expr,nm in sorted(hits):
    print(f"  {f}:{ln}")
    print(f"      computed == expected == {expr}")
    print(f"      named: \"{nm}\"")
