#!/usr/bin/env python3
"""The second component of {(phi, psi) : gamma(phi) gamma(psi) = V^3} in H3(q).

Input: the lex shape basis of component 2 over Q(h), computed by Singular
(`singular/borromean_factorisation_components.sing` -> `singular/component2_shape_basis.txt`).
Each generator is c(h) x + f_x(h, s2) for one colour weight x, except the first, which is the
degree-6 minimal polynomial of s2. We evaluate at the proton pin q0, q = 3/2 and q = 7/5,
find the real roots of the s2 polynomial with mpmath at 60 dps, recover all six weights, and
check gamma(phi) gamma(psi) - V^3 in the regular representation (exact model matrices,
mpmath arithmetic). Reads q0 from qou_substrate (proton pin)."""
import json
from pathlib import Path
import mpmath as mp
import sympy as sp
mp.mp.dps = 60
here = Path(__file__).parent
h = sp.symbols('h'); X = sp.symbols('p0 p1 p2 s0 s1 s2')
gens = [sp.sympify(l.strip().rstrip(',').replace('^', '**')) for l in
        (here/'singular'/'component2_shape_basis.txt').read_text().splitlines() if l.strip()]
s2 = X[5]
minpoly = gens[0]
solve_for = {}
for g in gens[1:]:
    for x in X[:5]:
        if g.has(x):
            c = sp.Poly(g, x).coeff_monomial(x)
            solve_for[x] = sp.simplify(-(g - c*x)/c)
try:
    from qou_substrate.constants import Q_50_DIGIT_STR as Q0S
    q0 = mp.mpf(Q0S); anchor = 'proton'
except Exception:
    raise SystemExit('qou_substrate not importable; refusing to fall back to a typed q0')
def L(hv):
    z = mp.mpf(0)
    L0 = mp.matrix([[0,1,0,0,0,0],[1,hv,0,0,0,0],[0,0,0,1,0,0],[0,0,1,hv,0,0],[0,0,0,0,0,1],[0,0,0,0,1,hv]])
    L1 = mp.matrix([[0,0,1,0,0,0],[0,0,0,0,1,0],[1,0,hv,0,0,0],[0,0,0,0,0,1],[0,1,0,0,hv,0],[0,0,0,1,0,hv]])
    return L0, L1
out = {'q0Anchor': anchor, 'q0Value': mp.nstr(q0, 50), 'precision_dps': 60, 'points': {}}
for name, qv in (('q0_proton', q0), ('3/2', mp.mpf(3)/2), ('7/5', mp.mpf(7)/5)):
    hv = qv - 1/qv
    P = sp.Poly(minpoly.subs(h, sp.Float(mp.nstr(hv, 60), 60)), s2)
    roots = mp.polyroots([mp.mpf(str(c)) for c in P.all_coeffs()], maxsteps=400, extraprec=400)
    L0, L1 = L(hv); I6 = mp.eye(6); V = L0*(L1 - hv*I6); V3 = V*V*V
    pts = []
    for r in roots:
        if abs(mp.im(r)) > mp.mpf(10)**-40: continue
        sv = mp.re(r)
        vals = {str(x): mp.mpf(str(sp.N(e.subs({h: sp.Float(mp.nstr(hv, 60), 60), s2: sp.Float(mp.nstr(sv, 60), 60)}), 60)))
                for x, e in solve_for.items()}
        vals['s2'] = sv
        g1 = I6 + vals['p0']*L0 + vals['p1']*L1 + vals['p2']*V
        g2 = I6 + vals['s0']*L0 + vals['s1']*L1 + vals['s2']*V
        res = mp.mnorm(g1*g2 - V3, 1)
        pts.append({k: mp.nstr(v, 20) for k, v in vals.items()} | {'residual': mp.nstr(res, 5)})
    out['points'][name] = {'h': mp.nstr(hv, 20), 'n_real_extra': len(pts), 'real_extra_factorisations': pts}
(here/'borromean-extra-factorisations.witness.json').write_text(json.dumps(out, indent=1))
for k, v in out['points'].items():
    print(k, 'real extra:', v['n_real_extra'])
    for p in v['real_extra_factorisations']: print('  ', p)
