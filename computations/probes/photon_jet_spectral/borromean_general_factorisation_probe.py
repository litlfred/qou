#!/usr/bin/env python3
"""Does beta_Bor = V^3 factor as gamma(phi)*gamma(psi) with general colour weights, beyond
the collinear corpus factorisation? Groebner basis of the 6 equations in 6 unknowns at a
rational q (exact). Reports the solution-set dimension via the Hilbert-dimension test:
the set is finite iff for every variable some leading term is a pure power of it.
Never reads q0."""
import json
from pathlib import Path
import sympy as sp
src = Path(__file__).with_name('photon_jet_probe.py').read_text().split('res = {}')[0]
ns = {}; exec(src, ns)
S0, S1, V, I6, q, vec = ns['S0'], ns['S1'], ns['V'], ns['I6'], ns['q'], ns['vec']
X = sp.symbols('p0 p1 p01 s0 s1 s01')
g = lambda w: I6 + w[0]*S0 + w[1]*S1 + w[2]*V
def run(qv):
    eqs = [sp.expand(sp.nsimplify(e.subs(q, qv))) for e in vec(g(X[:3])*g(X[3:]) - V**3)]
    eqs = [sp.numer(sp.together(e)) for e in eqs if e != 0]
    G = sp.groebner(eqs, *X, order='grevlex')
    lts = [sp.Poly(p, *X).monoms(order='grevlex')[0] for p in G.exprs]
    pure = {i for m in lts for i in range(6) if m[i] > 0 and sum(m) == m[i]}
    r = {'q': str(qv), 'groebner_size': len(G.exprs), 'finite_solution_set': len(pure) == 6,
         'variables_with_pure_leading_power': sorted(X[i].name for i in pure)}
    if r['finite_solution_set']:
        sols = sp.solve(G.exprs, X, dict=True)
        r['solutions'] = [{str(k): str(v) for k, v in d.items()} for d in sols]
    return r

out = {'q0Anchor': 'independent', 'q0AnchorReason': 'rational q; never reads q0',
       'runs': [run(sp.Rational(3, 2)), run(sp.Rational(7, 5))]}
Path(__file__).with_name('borromean-general-factorisation.witness.json').write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
