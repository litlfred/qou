"""FKR 1307.6697 section 6.1 elimination, SATURATED — the non-zero condition is preserved.

WHY v3 WAS WRONG. snappy appends one equation t*prod(coords) - 1 = 0 whose whole job is to
force every Ptolemy coordinate invertible. v3 fed that equation into the elimination pool,
where it was immediately used at STEP 0 to solve for t itself (t = 1/prod). The constraint
then vanished from the system, and since the reduction clears denominators via
numer(q.subs(x, -B/A)) -- which adds the locus {A = 0} -- nothing was left to cut those
spurious components out. All 18 points of the resulting variety sat on them.

THE FIX. Hold the non-zero-condition equation aside, never eliminate using it and never
eliminate t. Run the elimination on the remaining equations, then substitute every
elimination into the held equation and append it. Because A is always a monomial in
coordinates, A = 0 forces some coordinate to 0, which the restored equation forbids -- so
the spurious components are cut out by construction rather than by a separate saturation.

Exact throughout (sympy over Q). Writes the substitution log so solutions lift back.
"""
import sympy as sp, snappy, re, sys, time, json

name = sys.argv[1] if len(sys.argv) > 1 else '4_1'
kcls = int(sys.argv[2]) if len(sys.argv) > 2 else 0
CAP  = int(sys.argv[3]) if len(sys.argv) > 3 else 25

M = snappy.Manifold(name)
V = M.ptolemy_variety(3, obstruction_class=kcls, eliminate_fixed_ptolemys=True)
vs      = [str(v) for v in V.variables_with_non_zero_condition]
plain   = {str(v) for v in V.variables}
alleq   = [str(e) for e in V.equations_with_non_zero_condition]
maineq  = {str(e) for e in V.equations}
sym = {v: sp.Symbol('x%d' % i) for i, v in enumerate(vs)}
protected = {sym[v] for v in vs if v not in plain}      # the non-zero-condition variable t
def conv(s):
    for v in sorted(vs, key=len, reverse=True):
        s = re.sub(r'\b%s\b' % re.escape(v), str(sym[v]), s)
    return s

polys, held = [], []
for e in alleq:
    p = sp.expand(sp.sympify(conv(e).replace('^', '**')))
    (polys if e in maineq else held).append(p)
print(f"{name} c{kcls}: {len(polys)} main eqs + {len(held)} held (non-zero condition), "
      f"{len(vs)} vars, protected {[str(p) for p in protected]}", flush=True)

units = set()
for p in held:
    for t_ in sp.Add.make_args(p):
        if not t_.is_number:
            units |= t_.free_symbols
def unit_coeff(A):
    if A == 0: return False
    if not A.free_symbols: return True
    return A.free_symbols <= units and len(sp.Add.make_args(sp.expand(A))) == 1

t0, elim, subs_log = time.time(), 0, []
while time.time() - t0 < 1200:
    best = None
    for i, p in enumerate(polys):
        for x in sorted(p.free_symbols, key=str):
            if x in protected: continue                  # never eliminate t
            if sp.Poly(p, x).degree() != 1: continue
            A = sp.expand(p.coeff(x, 1))
            if not unit_coeff(A): continue
            val = sp.cancel(-sp.expand(p.coeff(x, 0)) / A)
            cand, ok = [], True
            for j, q in enumerate(polys):
                if j == i: continue
                r = sp.expand(sp.numer(sp.cancel(sp.together(q.subs(x, val)))))
                if r != 0 and sp.total_degree(r) > CAP: ok = False; break
                if r != 0: cand.append(r)
            if ok:
                score = (0 if not A.free_symbols else 1,
                         max([sp.total_degree(c) for c in cand] or [0]))
                if best is None or score < best[0]: best = (score, i, x, cand, val)
        if best and best[0][0] == 0: break
    if not best: break
    _, i, x, polys, val = best
    held = [sp.expand(sp.numer(sp.cancel(sp.together(h.subs(x, val))))) for h in held]
    subs_log.append((str(x), str(val)))
    elim += 1

polys = polys + held                                     # RESTORE the constraint
rem = sorted(set().union(*[p.free_symbols for p in polys]) if polys else set(), key=str)
print(f"AFTER: {len(rem)} vars, {len(polys)} eqs (eliminated {elim}, non-zero condition "
      f"RESTORED), maxdeg {max([sp.total_degree(p) for p in polys] or [0])}, "
      f"{time.time()-t0:.1f}s", flush=True)
json.dump({'vars_original': [str(sym[v]) for v in vs], 'ptolemy_names': vs,
           'subs_order': subs_log, 'remaining': [str(v) for v in rem]},
          open(f'{name}_c{kcls}_sat_subs.json', 'w'), indent=1)
with open(f'{name}_c{kcls}_sat.sing', 'w') as f:
    f.write("ring r = 0, (%s), dp;\n" % ",".join(str(v) for v in rem))
    f.write("ideal I = %s;\n" % (",\n ".join(str(p).replace('**', '^') for p in polys)))
    f.write('int t0=timer; ideal G=std(I);\n')
    f.write('printf("std %s sec | GB %s | dim %s", timer-t0, size(G), dim(G));\n')
    f.write('if (size(G)==1 && G[1]==1) { printf("EMPTY"); } else { printf("NON-EMPTY"); }\n')
    f.write('quit;\n')
print(f"wrote {name}_c{kcls}_sat.sing + _sat_subs.json", flush=True)
