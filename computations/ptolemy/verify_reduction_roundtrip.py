"""GUARD: a reduction is trustworthy only if a solution ROUND-TRIPS to the original system.

This is the check whose absence cost a retraction. The FKR elimination clears denominators
via numer(q.subs(x, -B/A)), which ADDS the locus {A = 0}; a reduced system can therefore be
non-empty while the original is not. Matching solution counts on a small calibration case
does NOT detect this -- 4_1 passed at every stage while the L6a4 reduction was unsound,
because 4_1's solutions happened to avoid the spurious locus.

The only sufficient test is the round trip: solve the reduced system, lift through the
recorded substitutions, and evaluate the ORIGINAL equations. A lift that blows up, or that
leaves a residual, means the reduced solution is spurious.

Usage: verify_reduction.py <manifold> <class> <subs.json>
Exit 0 iff at least one reduced solution lifts with residual < 1e-20 AND every Ptolemy
coordinate is non-zero at that point.
"""
import json, re, sys, sympy as sp, snappy, mpmath as mp
mp.mp.dps = 50

name, kcls, subfile = sys.argv[1], int(sys.argv[2]), sys.argv[3]
sub = json.load(open(subfile))
M = snappy.Manifold(name)
V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
vs = sub['ptolemy_names']
sym = {v: sp.Symbol(s) for v, s in zip(vs, sub['vars_original'])}
def conv(s):
    for v in sorted(vs, key=len, reverse=True):
        s = re.sub(r'\b%s\b' % re.escape(v), str(sym[v]), s)
    return s
orig = [sp.sympify(conv(str(e)).replace('^','**')) for e in V.equations_with_non_zero_condition]
red = list(orig)
for v, val in sub['subs_order']:
    red = [sp.expand(sp.numer(sp.cancel(sp.together(q.subs(sp.Symbol(v), sp.sympify(val))))))
           for q in red]
    red = [q for q in red if q != 0]
rem = [sp.Symbol(v) for v in sub['remaining']]
print(f"round-trip guard: {len(red)} reduced eqs in {len(rem)} unknowns", flush=True)
sols = sp.solve(red, rem, dict=True)
print(f"  {len(sols)} reduced solution(s)", flush=True)
good = 0
for si, s in enumerate(sols):
    full = {r: sp.simplify(s.get(r, r)) for r in rem}
    if any(x.free_symbols for x in full.values()): continue
    ok = True
    for v, val in reversed(sub['subs_order']):
        e = sp.sympify(val)
        d = sp.denom(sp.together(e)).subs(full)
        if sp.simplify(d) == 0:
            print(f"  sol {si}: SPURIOUS -- denominator of {v} vanishes", flush=True); ok = False; break
        full[sp.Symbol(v)] = sp.simplify(e.subs(full))
    if not ok: continue
    res = max(abs(complex(sp.simplify(p.subs(full)))) for p in orig)
    zero = [str(k) for k, x in full.items() if sp.simplify(x) == 0]
    tag = "OK" if res < 1e-20 and not zero else f"residual {res:.2e}" + (f" zero coords {zero}" if zero else "")
    print(f"  sol {si}: round-trip {tag}", flush=True)
    if res < 1e-20 and not zero: good += 1
print(f"\n{good} of {len(sols)} reduced solutions round-trip to genuine points", flush=True)
sys.exit(0 if good else 1)
