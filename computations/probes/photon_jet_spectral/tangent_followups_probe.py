#!/usr/bin/env python3
"""Follow-up probe (audit §8): P8 tangent-line factorisation of V^3, P10 quadratic algebra on W.
Exact sympy over Q(q). Never reads q0."""
import json, itertools
from pathlib import Path
import sympy as sp
src = Path(__file__).with_name('photon_jet_probe.py').read_text().split('res = {}')[0]
ns = {}; exec(src, ns)
S0, S1, V, I6, h, q, vec = ns['S0'], ns['S1'], ns['V'], ns['I6'], ns['h'], ns['q'], ns['vec']
out = {'q0Anchor': 'independent', 'q0AnchorReason': 'symbolic in q over Q(q); never reads the substrate q0'}
# P8
M = sp.Matrix.hstack(vec(I6), vec(V), vec(V*V))
out['P8_rank_1_V_V2'] = int(M.rank(simplify=True))
c = sp.symbols('c0 c1 c2')
sol = sp.solve(list(vec(V**3) - (c[0]*vec(I6) + c[1]*vec(V) + c[2]*vec(V*V))), c, dict=True)[0]
out['P8_V3_coeffs'] = {str(k): str(sp.factor(v)) for k, v in sol.items()}
a, b = sp.symbols('a b')
fac = sp.solve([sp.Eq(a + b, sol[c[1]]), sp.Eq(a*b, sol[c[2]])], [a, b], dict=True)
out['P8_factorisations'] = [{str(k): str(sp.factor(v)) for k, v in s.items()} for s in fac]
out['P8_V3_eq_gamma_qh_gamma_mqinvh'] = bool(sp.simplify((I6 + q*h*V)*(I6 - h/q*V) - V**3) == sp.zeros(6, 6))
# generic: which k-th powers V^k split into k collinear photons? char poly of V on the line
x = sp.symbols('x')
out['P8_V_min_poly'] = str(sp.factor(x**3 - sol[c[2]]*x**2 - sol[c[1]]*x - sol[c[0]]))
# P10: quadratic algebra T(W)/(R)
W = [S0, S1, V]
F1 = [I6] + W
def rk(L): return sp.Matrix.hstack(*[vec(m) for m in L]).rank(simplify=True)
# map W(x)W -> H3/F1 : coordinates; compute kernel R in Q(q)^9
# basis of H3/F1 complement: use L- and e-
Lm, Ee = S1*S0, S0*S1*S0
Bmat = sp.Matrix.hstack(*[vec(m) for m in F1 + [Lm, Ee]])  # invertible 6x6
Binv = sp.simplify(Bmat.inv())
cols = []
for x1, x2 in itertools.product(W, W):
    co = sp.simplify(Binv*vec(x1*x2))
    cols.append(co[4:6, 0])
A = sp.Matrix.hstack(*cols)  # 2 x 9
out['P10_rank_WW_to_gr2'] = int(A.rank(simplify=True))
R = A.nullspace(simplify=True)
out['P10_dim_R'] = len(R)
# degree 3: (W(x)R + R(x)W) in W^{(x)3}, 27-dim
def kron(u, v): return sp.Matrix([ui*vj for ui in u for vj in v])
E3 = [sp.Matrix([int(i == j) for j in range(3)]) for i in range(3)]
gens = [kron(e, r) for e in E3 for r in R] + [kron(r, e) for r in R for e in E3]
r3 = sp.Matrix.hstack(*gens).rank(simplify=True)
out['P10_rank_I3'] = int(r3); out['P10_dim_degree3_of_quadratic_algebra'] = 27 - int(r3)
Path(__file__).with_name('tangent-followups.witness.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
for k, v in out.items(): print(k, ':', v)
