#!/usr/bin/env python3
"""Does beta_Bor = V^3 factor as gamma(phi)*gamma(psi) with general colour weights, beyond
the collinear corpus factorisation? Groebner basis of the 6 equations in 6 unknowns at a
rational q (exact). Reports: whether the solution set is finite (every variable has a pure
power among the leading terms); vdim, the number of solutions over the algebraic closure
counted with multiplicity (standard monomials); and the solutions sympy's solve returns.
CORRECTED 2026-11-25: sympy's solve returns only the solutions it can express, here the
rational ones, so `solutions` is NOT the full solution set. Compare its length with vdim.
Singular (symbolic h): the ideal is radical, 8 points = the corpus pair + an irreducible
degree-6 component. Never reads q0."""
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
        lead = [m for m in lts]
        bound = max(sum(m) for m in lead) + 2
        std = [m for m in __import__('itertools').product(range(bound + 1), repeat=6)
               if not any(all(m[i] >= l[i] for i in range(6)) for l in lead)]
        r['vdim'] = len(std)
        sols = sp.solve(G.exprs, X, dict=True)
        r['solutions_returned_by_sympy_solve'] = [{str(k): str(v) for k, v in d.items()} for d in sols]
        r['sympy_solve_complete'] = len(sols) == r['vdim']
    return r

out = {'q0Anchor': 'independent', 'q0AnchorReason': 'rational q; never reads q0',
       'runs': [run(sp.Rational(3, 2)), run(sp.Rational(7, 5))]}
Path(__file__).with_name('borromean-general-factorisation.witness.json').write_text(json.dumps(out, indent=1))
print(json.dumps(out, indent=1))
