"""FKR arXiv:1307.6697 section 6.1 pre-processing, ported to Ptolemy coordinates.

Their step 2: when an equation is affine in some variable, A*z + B, with A a unit on
the constructible set, substitute z = -B/A everywhere and drop the equation.  For 4_1
in their flag coordinates this took 8 variables to 2.  Coordinates differ; the move
does not depend on them.  Exact throughout (sympy over Q) -- no floating point.
"""
import sympy as sp, snappy, re, sys, time

name = sys.argv[1] if len(sys.argv) > 1 else 'L6a4'
kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 1

M = snappy.Manifold(name)
V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
vs  = [str(v) for v in V.variables_with_non_zero_condition]
eqs = [str(e) for e in V.equations_with_non_zero_condition]
sym = {v: sp.Symbol('x%d' % i) for i, v in enumerate(vs)}

def conv(s):
    for v in sorted(vs, key=len, reverse=True):
        s = re.sub(r'\b%s\b' % re.escape(v), str(sym[v]), s)
    return s

polys = [sp.expand(sp.sympify(conv(e).replace('^', '**'))) for e in eqs]
allv  = sorted(set().union(*[p.free_symbols for p in polys]), key=lambda s: str(s))
print(f"{name} class {kcls}: START {len(allv)} vars, {len(polys)} eqs", flush=True)

subs_made, t0 = {}, time.time()
while True:
    hit = None
    for i, p in enumerate(polys):
        if p == 0:
            continue
        for x in sorted(p.free_symbols, key=lambda s: str(s)):
            d = sp.Poly(p, x).degree()
            if d != 1:
                continue
            A = sp.expand(p.coeff(x, 1))
            if A.free_symbols:          # unit test: constant coefficient only (safe)
                continue
            if A == 0:
                continue
            B = sp.expand(p.coeff(x, 0))
            hit = (i, x, sp.cancel(-B / A))
            break
        if hit:
            break
    if not hit:
        break
    i, x, val = hit
    polys = [sp.expand(q.subs(x, val)) for j, q in enumerate(polys) if j != i]
    polys = [q for q in polys if q != 0]
    subs_made[x] = val

rem = sorted(set().union(*[p.free_symbols for p in polys]) if polys else set(), key=lambda s: str(s))
degs = [sp.total_degree(p) for p in polys]
print(f"AFTER FKR 6.1 pre-pass: {len(rem)} vars, {len(polys)} eqs  "
      f"(eliminated {len(subs_made)}) in {time.time()-t0:.1f}s", flush=True)
print(f"  max total degree: {max(degs) if degs else 0}", flush=True)
print(f"  remaining vars: {[str(v) for v in rem]}", flush=True)

with open(f'{name}_c{kcls}_fkr.sing', 'w') as f:
    f.write("ring r = 0, (%s), dp;\n" % ",".join(str(v) for v in rem))
    f.write("ideal I = %s;\n" % (",\n ".join(str(p).replace('**', '^') for p in polys)))
    f.write('int t0=timer; ideal G=std(I);\n')
    f.write('printf("std %s sec | GB %s | dim %s", timer-t0, size(G), dim(G));\n')
    f.write('if (size(G)==1 && G[1]==1) { printf("IDEAL=(1) -> variety EMPTY"); }'
            ' else { printf("ideal PROPER -> NON-EMPTY -> complex type EXISTS"); }\n')
    f.write('quit;\n')
print(f"wrote {name}_c{kcls}_fkr.sing", flush=True)
