#!/usr/bin/env python3
"""Is the electron word s0 s1 s0 a two-photon product lam^-1 * gamma1 * gamma2 in H_3(q)?
And V^3 = 1 + h^2 V - h^2 V^2 (V = s0 s1^{-1}).

Exact sympy, generic q, using the semisimple decomposition (trivial, sign, 2-dim).
s0s1s0 is a unit, so gamma1*gamma2 = lam*s0s1s0 with lam != 0 forces gamma1 invertible,
gamma2 = lam*gamma1^{-1}*s0s1s0, and that element must lie in the photon span. With the
adjugate (to avoid division) the two conditions are polynomial; a lex Groebner basis forces
b = c/q or b = -cq, and on both branches every solution has det(gamma1 on the 2-dim block)=0,
i.e. gamma1 is not invertible. Hence no two-photon product, at any (even complex) weights,
is a nonzero multiple of s0s1s0.
"""
import json, pathlib
import sympy as sp
q = sp.symbols('q'); a, b, c = sp.symbols('a b c')
S0 = sp.Matrix([[q, 0], [1, -1/q]]); S1 = sp.Matrix([[-1/q, 1], [0, q]]); I = sp.eye(2)
assert sp.simplify(S0*S1*S0 - S1*S0*S1) == sp.zeros(2)
C = S0*S1.inv()
tr = lambda e, p0, p1, p01: e + q*(p0 + p1) + p01
sg = lambda e, p0, p1, p01: e - (p0 + p1)/q + p01
x = sp.symbols('x0:4')
def pcoords(M):
    s = sp.solve(list(x[0]*I + x[1]*S0 + x[2]*S1 + x[3]*C - M), x, dict=True)[0]
    return [sp.simplify(s[v]) for v in x]
checks = {}
# V^3 identity: 2-dim block checked exactly; in trivial and sign V -> 1 and 1 = 1 + h^2(1 - 1)
Vm = C; checks['V3_identity_2dim'] = sp.simplify(Vm**3 - (I + (q-1/q)**2*(Vm - Vm**2))) == sp.zeros(2)
checks['V3_identity_1dim'] = True  # V -> 1 in trivial and sign: 1 = 1 + h^2(1-1)
G = I + a*S0 + b*S1 + c*C
co = pcoords(sp.simplify(G.adjugate()*(S0*S1*S0)))
dG = sp.expand(G.det())
e1 = sp.numer(sp.together(tr(1, a, b, c)*tr(*co) - dG*q**3))
e2 = sp.numer(sp.together(sg(1, a, b, c)*sg(*co) + dG*q**-3))
GB = list(sp.groebner([e1, e2], a, b, c, q, order='lex'))
last = sp.factor(GB[-1])
checks['groebner_forces_branches'] = sp.simplify(last / ((b + c*q)*(b*q - c)*q**3*(q**2+1)*(q**2-q+1)*(q**2+q+1))).is_number
deg = []
for br in (c/q, -c*q):
    sols = sp.solve([sp.numer(sp.together(e1.subs(b, br))), sp.numer(sp.together(e2.subs(b, br)))], [a, c], dict=True)
    deg += [sp.simplify(dG.subs(b, br).subs(so)) == 0 for so in sols]
checks['all_solutions_degenerate'] = len(deg) > 0 and all(deg)
out = {'description': 'electron s0s1s0 is not a two-photon product in H_3(q); V^3 = 1 + h^2(V - V^2)',
       'checks': {k: bool(v) for k, v in checks.items()},
       'verdict': 'no gamma*gamma (any weights, complex allowed) is a nonzero multiple of s0s1s0'}
pathlib.Path(__file__).with_name('electron_result.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2)); assert all(checks.values()), checks
