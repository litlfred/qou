"""FKR 1307.6697 section 6.1 pre-processing, FULL version: unit leading coefficients.

FKR substitute z = -B/A whenever A is a UNIT on the constructible set (for them, a
product of z or 1-z, all non-zero by the restrictions).  v1 allowed only constant A and
took 4_1 from 7 vars to 4; FKR reach 2 in their own coordinates, so the gap is the unit
case.  Here the units are read off the non-zero condition: snappy appends one equation
(monomial)*t - 1, and every variable in that monomial is invertible on the variety.

Substituting a rational function requires clearing denominators, which can RAISE degrees
-- FKR warn about exactly this.  No solutions are lost because A is a unit.  Exact
throughout (sympy over Q); degrees are reported before and after so the trade is visible.
"""
import sympy as sp, snappy, re, sys, time

name = sys.argv[1] if len(sys.argv) > 1 else '4_1'
kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 0
CAP  = int(sys.argv[3]) if len(sys.argv) > 3 else 40    # abandon a substitution past this degree

M = snappy.Manifold(name)
V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
vs  = [str(v) for v in V.variables_with_non_zero_condition]
eqs = [str(e) for e in V.equations_with_non_zero_condition]
sym = {v: sp.Symbol('x%d' % i) for i, v in enumerate(vs)}
def conv(s):
    for v in sorted(vs, key=len, reverse=True):
        s = re.sub(r'\b%s\b' % re.escape(v), str(sym[v]), s)
    return s
polys = [sp.expand(sp.sympify(conv(e).replace('^','**'))) for e in eqs]

# units: variables in the non-zero-condition monomial, i.e. the equation <monomial> - 1
units = set()
for p in polys:
    t = sp.Add.make_args(p)
    if len(t) == 2 and any(x.is_number for x in t):
        mono = [x for x in t if not x.is_number][0]
        if mono.is_Mul or mono.is_Pow or mono.is_Symbol:
            units |= mono.free_symbols
print(f"{name} c{kcls}: START {len(set().union(*[p.free_symbols for p in polys]))} vars, "
      f"{len(polys)} eqs, maxdeg {max(sp.total_degree(p) for p in polys)}; "
      f"{len(units)} unit vars", flush=True)

def unit_coeff(A):
    """A is a unit if it is a nonzero constant times a monomial in unit variables."""
    if A == 0: return False
    if not A.free_symbols: return True
    n, d = sp.fraction(sp.cancel(A))
    if not (n.is_Mul or n.is_Pow or n.is_Symbol or n.is_number): return False
    return A.free_symbols <= units and len(sp.Add.make_args(sp.expand(A))) == 1

_val_of = {}
t0, elim = time.time(), 0
subs_log = []   # (var, value) in elimination order, for lifting solutions back
while time.time() - t0 < 900:
    best = None
    for i, p in enumerate(polys):
        for x in sorted(p.free_symbols, key=lambda s: str(s)):
            if sp.Poly(p, x).degree() != 1: continue
            A = sp.expand(p.coeff(x, 1))
            if not unit_coeff(A): continue
            val = sp.cancel(-sp.expand(p.coeff(x, 0)) / A)
            _val_of[x] = val
            cand = []
            ok = True
            for j, q in enumerate(polys):
                if j == i: continue
                r = sp.numer(sp.cancel(sp.together(q.subs(x, val))))
                r = sp.expand(r)
                if r != 0 and sp.total_degree(r) > CAP: ok = False; break
                if r != 0: cand.append(r)
            if ok:
                score = (0 if not A.free_symbols else 1, max([sp.total_degree(c) for c in cand] or [0]))
                if best is None or score < best[0]: best = (score, i, x, cand)
        if best and best[0][0] == 0: break
    if not best: break
    _, i, x, polys = best
    subs_log.append((str(x), str(_val_of[x])))
    elim += 1

rem = sorted(set().union(*[p.free_symbols for p in polys]) if polys else set(), key=str)
print(f"AFTER: {len(rem)} vars, {len(polys)} eqs (eliminated {elim}), "
      f"maxdeg {max([sp.total_degree(p) for p in polys] or [0])}, {time.time()-t0:.1f}s", flush=True)
with open(f'{name}_c{kcls}_fkr2.sing','w') as f:
    f.write("ring r = 0, (%s), dp;\n" % ",".join(str(v) for v in rem))
    f.write("ideal I = %s;\n" % (",\n ".join(str(p).replace('**','^') for p in polys)))
    f.write('int t0=timer; ideal G=std(I);\n')
    f.write('printf("std %s sec | GB %s | dim %s", timer-t0, size(G), dim(G));\n')
    f.write('if (size(G)==1 && G[1]==1) { printf("EMPTY"); } else { printf("NON-EMPTY -> complex type EXISTS"); }\n')
    f.write('quit;\n')
import json
json.dump({'vars_original': [str(sym[v]) for v in vs],
           'ptolemy_names': vs,
           'subs_order': subs_log,
           'remaining': [str(v) for v in rem]},
          open(f'{name}_c{kcls}_subs.json','w'), indent=1)
print(f"wrote {name}_c{kcls}_fkr2.sing and {name}_c{kcls}_subs.json ({len(subs_log)} substitutions)", flush=True)
