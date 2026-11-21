"""Score the forced diagonal sl3 wall K = diag(1,1,0) (u,d kept, s annihilated) on strand 1
against the octet: Cartan-weighted wall trace  K_w * tr(K_1 V3 | weight space). Exact; q0 only for display."""
import itertools, sympy as sp, runpy
g = runpy.run_path('/mnt/project-files/qou-lattice-isospin-review/octet_isospin_probe.py', run_name='lib')
q, s1, s2, ws, restr = g['q'], g['s1'], g['s2'], g['ws'], g['restr']
K1 = sp.kronecker_product(sp.diag(1, 1, 0), sp.eye(9))
V3 = (s1 * s2.inv())**3
Kiso = [q, 1/q, 1]
def Kw(w): return sp.prod([Kiso[k]**c for k, c in enumerate(w)])
pairs = [('N', (2,1,0), (1,2,0)), ('Sigma', (2,0,1), (0,2,1)), ('Xi', (1,0,2), (0,1,2))]
d = {}
for nm, hi, lo in pairs:
    th = sp.simplify(restr(K1*V3, ws(hi)).trace()); tl = sp.simplify(restr(K1*V3, ws(lo)).trace())
    t0 = sp.simplify(restr(V3, ws(hi)).trace())
    d[nm] = sp.factor(Kw(lo)*tl - Kw(hi)*th)
    print(f"{nm:6s} wall trace hi = {sp.factor(th)} | lo = {sp.factor(tl)} | no-wall = {sp.factor(t0)}")
    print(f"       Cartan-weighted (low - high) = {d[nm]}")
q0 = sp.Rational('1.1099785827513808')
r = [sp.simplify(d[n]/d['N']) for n in ('Sigma', 'Xi')]
print("Sigma/N =", sp.factor(r[0]), " Xi/N =", sp.factor(r[1]))
print("at q0 (display): Sigma:N:Xi =", sp.N(r[0].subs(q, q0), 6), ": 1 :", sp.N(r[1].subs(q, q0), 6))
print("lattice QCD parts: 2.584 : 1 : 1.590")
