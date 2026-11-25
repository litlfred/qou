#!/usr/bin/env python3
"""Audit §9 (P11-P13): symmetries of the photon space W and F1 = R1 + W in H3(q), and the
group of linear maps of W preserving the trace data (l, G). Exact sympy over Q(q), convention D.
Never reads q0."""
import json, itertools
from pathlib import Path
import sympy as sp
src = Path(__file__).with_name('photon_jet_probe.py').read_text().split('res = {}')[0]
ns = {}; exec(src, ns)
S0, S1, V, I6, h, q, vec, trM, B, idx = (ns[k] for k in ('S0', 'S1', 'V', 'I6', 'h', 'q', 'vec', 'trM', 'B', 'idx'))
out = {'q0Anchor': 'independent', 'q0AnchorReason': 'symbolic in q; never reads q0'}
S1i, S0i = S1 - h*I6, S0 - h*I6
def word(ws, inv=False):
    M = sp.eye(6)
    for ch in ws:
        M = M * ((S0i if inv else S0) if ch == '0' else (S1i if inv else S1))
    return M
Tw = {b: (I6 if b == 'e' else word(b)) for b in B}
def from_vec(v): return sum((v[idx[b]]*Tw[b] for b in B), sp.zeros(6, 6))
def theta(v):  # automorphism s0<->s1 on basis words
    sw = {'e': 'e', '0': '1', '1': '0', '01': '10', '10': '01', '010': '010'}
    w = sp.zeros(6, 1)
    for b in B: w[idx[sw[b]]] += v[idx[b]]
    return w
def rho(v):  # anti-automorphism T_w -> T_{w^-1}
    sw = {'e': 'e', '0': '0', '1': '1', '01': '10', '10': '01', '010': '010'}
    w = sp.zeros(6, 1)
    for b in B: w[idx[sw[b]]] += v[idx[b]]
    return w
def beta(v):  # bar: T_w -> (T_{w^-1})^{-1} = product of inverse letters in order, q -> 1/q
    acc = sp.zeros(6, 6)
    for b in B:
        if v[idx[b]] == 0: continue
        acc += sp.simplify(v[idx[b]].subs(q, 1/q)) * (I6 if b == 'e' else word(b, inv=True))
    return sp.simplify(vec(acc))
maps = {'id': lambda v: v, 'theta': theta, 'rho': rho, 'beta': beta}
F1 = [vec(I6), vec(S0), vec(S1), vec(V)]
W = [vec(S0), vec(S1), vec(V)]
def inside(vs, space):
    M = sp.Matrix.hstack(*space); r = M.rank(simplify=True)
    return all(sp.Matrix.hstack(M, x).rank(simplify=True) == r for x in vs)
res11 = {}
for k in range(1, 4):
    for combo in itertools.combinations(['theta', 'rho', 'beta'], k):
        def f(v, combo=combo):
            for m in combo: v = maps[m](v)
            return v
        name = '.'.join(combo)
        res11[name] = {'preserves_F1': inside([f(x) for x in F1], F1), 'preserves_W': inside([f(x) for x in W], W)}
out['P11'] = res11
# P12 normaliser of F1 in the Lie algebra H3
xs = sp.symbols('x0:6'); X = from_vec(sp.Matrix(xs))
Lm, Ee = S1*S0, S0*S1*S0
Binv = sp.simplify(sp.Matrix.hstack(*F1, vec(Lm), vec(Ee)).inv())
conds = []
for f in [I6, S0, S1, V]:
    c = sp.simplify(Binv * vec(X*f - f*X))
    conds += [c[4], c[5]]
A = sp.Matrix([[sp.diff(cnd, x) for x in xs] for cnd in conds])
N = A.nullspace(simplify=True)
out['P12_dim_normaliser_F1'] = len(N)
Z = [vec(I6), vec(S0*S1*S0*S0*S1*S0)]  # 1 and Delta^2 are central
# centre dimension of H3 = number of partitions of 3 = 3; check N is commutative-with-all
def central(M): return all(sp.simplify(M*g - g*M) == sp.zeros(6, 6) for g in (S0, S1))
out['P12_normaliser_is_central'] = all(central(from_vec(n)) for n in N)
# P13: trace data on W under convention D
zD = q**3/(q**2 + 1)
Wm = [S0, S1, V]
l = sp.Matrix([trM(w) for w in Wm])
G = sp.Matrix(3, 3, lambda i, j: sp.factor(trM(Wm[i]*Wm[j])))
out['P13_det_G'] = str(sp.factor(G.det()))
v = sp.simplify(G.inv() * l)                      # G v = l  (v is the l-dual vector)
out['P13_G(v,v)'] = str(sp.factor((v.T*G*v)[0]))
# complement basis: kernel of l^T (vectors x with l.x = 0 = G(v,x))
K = sp.Matrix(l.T).nullspace(simplify=True)
Gc = sp.Matrix(2, 2, lambda i, j: sp.factor((K[i].T*G*K[j])[0]))
out['P13_det_G_on_complement'] = str(sp.factor(Gc.det()))
for qv in (sp.Rational(111, 100), sp.Rational(3, 2)):
    d = Gc.det().subs(q, qv); out[f'P13_sign_det_complement_q={qv}'] = int(sp.sign(d))
Path(__file__).with_name('photon-symmetry.witness.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
for k, val in out.items(): print(k, ':', val)

# P13b (exploratory): the infinitesimal generator J of O(G) cap Stab(l) on W, and whether it
# also preserves the 3-photon form C(x,y,z) = tr_M(xyz). Also: theta rho on colour weights,
# and theta maps W to its mirror W' = span{s0, s1, s1 s0^{-1}}.
js = sp.symbols('j0:9'); J = sp.Matrix(3, 3, js)
eqs = list(J.T*G + G*J) + list(l.T*J)
Jsol = sp.solve(eqs, js, dict=True)
Jg = sp.simplify(J.subs(Jsol[0]))
free = sorted(Jg.free_symbols - {q}, key=str)
out['P13b_dim_lie_O(G)_stab(l)'] = len(free)
Jg1 = sp.simplify(Jg.subs({free[0]: 1})) if free else Jg
C = {}
for i, j, k in itertools.product(range(3), repeat=3):
    C[(i, j, k)] = trM(Wm[i]*Wm[j]*Wm[k])
def Cform(a, b, c):
    return sum(a[i]*b[j]*c[k]*C[(i, j, k)] for i in range(3) for j in range(3) for k in range(3))
E3 = [sp.Matrix([int(i == t) for t in range(3)]) for i in range(3)]
viol = []
for a, b, c in itertools.product(E3, repeat=3):
    d = sp.simplify(Cform(Jg1*a, b, c) + Cform(a, Jg1*b, c) + Cform(a, b, Jg1*c))
    viol.append(d)
out['P13b_J_preserves_cubic_trace'] = all(v == 0 for v in viol)
# theta rho on colour weights: image of gamma(phi) coordinates in basis {1,s0,s1,V}
f0, f1, f01 = sp.symbols('phi0 phi1 phi01')
g = vec(I6 + f0*S0 + f1*S1 + f01*V)
tg = theta(rho(g))
co = sp.simplify(sp.Matrix.hstack(*F1).solve_least_squares(tg)) if False else None
BF = sp.Matrix.hstack(*F1, vec(Lm), vec(Ee))
cc = sp.simplify(BF.inv()*tg)
out['P13b_theta_rho_on_colour_weights'] = [str(sp.factor(cc[i])) for i in range(4)]
Wp = [vec(S0), vec(S1), vec(S1*S0i)]
out['P13b_theta_W_equals_mirror'] = inside([theta(x) for x in W], Wp) and inside(Wp, [theta(x) for x in W])
out['P13b_W_equals_mirror'] = inside(Wp, W)
Path(__file__).with_name('photon-symmetry.witness.json').write_text(json.dumps(out, indent=1, ensure_ascii=False))
for k in [k for k in out if k.startswith('P13b')]: print(k, ':', out[k])
