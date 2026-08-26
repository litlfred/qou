#!/usr/bin/env python3
"""Find assertions of the form computed=<counter>, expected=<counter> where BOTH
counters are initialised to 0 and only ever incremented -- these pass vacuously
when nothing is processed."""
import ast, subprocess, sys
sys.path.insert(0,"computations/audits")
from _source_normalise import code_only

files=[p for p in subprocess.run(["git","ls-files","computations"],capture_output=True,text=True)
       .stdout.split() if p.endswith(".py") and "_deprecated" not in p]

def zero_init_counters(tree):
    """names assigned literal 0 somewhere, and target of a += somewhere"""
    zero, inc = set(), set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                if isinstance(t, ast.Name) and isinstance(n.value, ast.Constant) \
                   and n.value.value == 0:
                    zero.add(t.id)
        if isinstance(n, ast.AugAssign) and isinstance(n.target, ast.Name) \
           and isinstance(n.op, ast.Add):
            inc.add(n.target.id)
    return zero & inc

hits=[]
for f in files:
    try: tree=ast.parse(code_only(open(f,encoding="utf-8").read()))
    except Exception: continue
    ctr=zero_init_counters(tree)
    if not ctr: continue
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
                and n.func.attr == "add_assertion"): continue
        kw={k.arg:k.value for k in n.keywords if k.arg}
        c,e = kw.get("computed"), kw.get("expected")
        if isinstance(c,ast.Name) and isinstance(e,ast.Name) \
           and c.id in ctr and e.id in ctr:
            name=None
            if n.args and isinstance(n.args[0], ast.Constant): name=n.args[0].value
            hits.append((f, n.lineno, c.id, e.id, str(name)[:52]))

print(f"producers scanned: {len(files)}")
print(f"assertions comparing two zero-initialised counters: {len(hits)}\n")
for f,ln,c,e,nm in sorted(hits):
    print(f"  {f}:{ln}")
    print(f"      computed={c}  expected={e}   \"{nm}\"")
