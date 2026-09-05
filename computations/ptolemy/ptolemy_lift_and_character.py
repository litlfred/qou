"""Lift a solution of the FKR-reduced + sliced system back to Ptolemy coordinates,
build the PGL(3,C) holonomy, and test self-duality DIRECTLY.

This is the check that does not use the obstruction argument at all: if chi(g) differs
from chi(g^-1) for some g, the representation is complex type as a matter of computation,
independent of whether duality negates the obstruction class.

Numerically at high precision first (mpmath, 60 dps) to locate a solution; exactness is a
separate step. Calibrated on 4_1, whose answer is already known exactly.
"""
import json, sys, re, mpmath as mp, snappy, sympy as sp
mp.mp.dps = 60

name = sys.argv[1] if len(sys.argv) > 1 else '4_1'
kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 0
sub  = json.load(open(f'{name}_c{kcls}_subs.json'))

M = snappy.Manifold(name); G = M.fundamental_group()
V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
vs  = sub['ptolemy_names']
eqs = [str(e) for e in V.equations_with_non_zero_condition]
sym = {v: sp.Symbol(s) for v, s in zip(vs, sub['vars_original'])}
def conv(s):
    for v in sorted(vs, key=len, reverse=True):
        s = re.sub(r'\b%s\b' % re.escape(v), str(sym[v]), s)
    return s
polys = [sp.expand(sp.sympify(conv(e).replace('^','**'))) for e in eqs]
rem = [sp.Symbol(v) for v in sub['remaining']]
print(f"{name} c{kcls}: {len(vs)} ptolemy vars, {len(sub['subs_order'])} eliminated, "
      f"{len(rem)} free", flush=True)

# solve the reduced system numerically with sympy nsolve from many starts
red = [p for p in polys]
for v, val in sub['subs_order']:
    red = [sp.expand(sp.numer(sp.cancel(sp.together(q.subs(sp.Symbol(v), sp.sympify(val))))))
           for q in red]
    red = [q for q in red if q != 0]
print(f"  reduced to {len(red)} eqs in {len(rem)} unknowns", flush=True)
print(f"  (lifting map recorded; character evaluation is the next step)", flush=True)

# --- solve the reduced system exactly (feasible for 4_1) and lift ---
from snappy.ptolemy.coordinates import PtolemyCoordinates
sols = sp.solve(red, rem, dict=True)
print(f"  {len(sols)} solution(s) of the reduced system", flush=True)
exp = eval(V.py_eval_variable_dict())
inv = {v: k for k, v in sym.items()}
seen = []
for si, s in enumerate(sols):
    full = {}
    for r in rem:
        full[r] = sp.nsimplify(sp.radsimp(sp.simplify(s.get(r, r))))
    for v, val in reversed(sub['subs_order']):
        e = sp.sympify(val)
        e = e.subs({k: full[k] for k in full if k in e.free_symbols})
        full[sp.Symbol(v)] = sp.nsimplify(sp.radsimp(sp.simplify(e)))
    if any(x.free_symbols for x in full.values()):
        continue                        # not a point
    pt = {inv[k]: v for k, v in full.items() if k in inv}
    pt['1'] = sp.Integer(1)
    try:
        P = PtolemyCoordinates(exp(pt), is_numerical=False, manifold_thunk=lambda: M)
        A = sp.Matrix(P.evaluate_word('a', G))
        d = sp.simplify(sp.radsimp(sp.expand(A.trace() - A.inv().trace())))
        tag = "SELF-DUAL" if d == 0 else "COMPLEX TYPE"
        print(f"   sol {si}: chi(a)-chi(a^-1) = {d}   -> {tag}", flush=True)
        seen.append(d)
    except Exception as ex:
        print(f"   sol {si}: {type(ex).__name__}: {str(ex)[:70]}", flush=True)
print(f"  summary: {sum(1 for d in seen if d==0)} self-dual, "
      f"{sum(1 for d in seen if d!=0)} complex type", flush=True)
