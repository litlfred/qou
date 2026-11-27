#!/usr/bin/env python3
"""Which existing rule selects the corpus photon pair among the factorisations of V^3?
(owner 2026-11-25: "Test whether an existing rule already forces it.")

Factorisations: the 2 corpus points and the real points of the degree-6 component
(`borromean-extra-factorisations.witness.json`), at the proton q0.
Rules tested:
 N-term: linking neutrality (PhotonU1NeutralCut.Neutral, ported) applied to every braid-group
         element of the FORMAL expansion of gamma(phi)gamma(psi) in Z[B3] (no Hecke relation):
         every non-neutral group element must have total coefficient 0. Group elements are
         identified by their reduced Burau matrices (faithful on B3), exactly in Q(t).
 P3:     reading-3 Frobenius positivity of each factor: chi_(3) >= 0 and chi_(2,1) >= 0
         (y_(1^3) = 0 under convention D).
 R7c:    weights lie in Z[q, q^-1] (the section 7c generic-ring convention).
Reads q0 from qou_substrate (proton). mpmath 60 dps."""
import json, itertools
from pathlib import Path
import mpmath as mp, sympy as sp
mp.mp.dps = 60
here = Path(__file__).parent
from qou_substrate.constants import Q_50_DIGIT_STR as Q0S
q0 = mp.mpf(Q0S); h0 = q0 - 1/q0
# --- port of PhotonU1NeutralCut.Neutral
def swapAt(p, i):
    p = list(p); p[i], p[i+1] = p[i+1], p[i]; return p
def finalPos(w):
    p = [0, 1, 2]
    for i, _ in w: p = swapAt(p, i)
    return p
def step(w, x): return finalPos(w).index(x)
def comp(w, x): return min(x, step(w, x), step(w, step(w, x))) % 3
def cnt(w, C, D):
    p = [0, 1, 2]; tot = 0
    for i, e in w:
        x, y = comp(w, p[i]), comp(w, p[i+1])
        if (x == C and y == D) or (x == D and y == C): tot += e
        p = swapAt(p, i)
    return tot
def neutral(w): return all(cnt(w, C, D) == 0 for C in range(3) for D in range(3))
# --- Burau (reduced) for group identification
t = sp.symbols('t')
B = {(0, 1): sp.Matrix([[-t, 1], [0, 1]]), (1, 1): sp.Matrix([[1, 0], [t, -t]])}
B[(0, -1)] = B[(0, 1)].inv(); B[(1, -1)] = B[(1, 1)].inv()
def bur(w):
    M = sp.eye(2)
    for l in w: M = M*B[l]
    return tuple(sp.simplify(x) for x in M)
terms = [[], [(0, 1)], [(1, 1)], [(0, 1), (1, -1)]]   # 1, s0, s1, V
def expansion(p, s):
    cs = [1, p[0], p[1], p[2]]; ds = [1, s[0], s[1], s[2]]
    groups = {}
    for i, j in itertools.product(range(4), range(4)):
        w = terms[i] + terms[j]
        key = bur(w)
        g = groups.setdefault(key, {'word': w, 'coef': 0})
        g['coef'] += cs[i]*ds[j]
    return groups
pts = []
qs = mp.nstr(q0, 60)
corp_a, corp_b = q0*h0, -h0/q0
pts.append(('corpus (qh, -h/q)', (0, 0, corp_a), (0, 0, corp_b)))
pts.append(('corpus swapped', (0, 0, corp_b), (0, 0, corp_a)))
W = json.loads((here/'borromean-extra-factorisations.witness.json').read_text())
for k, P in enumerate(W['points']['q0_proton']['real_extra_factorisations']):
    f = lambda n: mp.mpf(P[n])
    pts.append((f'extra {k+1}', (f('p0'), f('p1'), f('p2')), (f('s0'), f('s1'), f('s2'))))
out = {'q0Anchor': 'proton', 'q0Value': mp.nstr(q0, 50), 'precision_dps': 60, 'rules': {}}
for name, p, s in pts:
    G = expansion(p, s)
    worst = max((abs(g['coef']) for g in G.values() if not neutral(g['word'])), default=mp.mpf(0))
    nonneutral = {str(g['word']): mp.nstr(g['coef'], 8) for g in G.values() if not neutral(g['word']) and abs(g['coef']) > mp.mpf(10)**-40}
    chi3 = lambda x: 1 + q0*(x[0] + x[1]) + x[2]
    chi21 = lambda x: 2 + h0*(x[0] + x[1]) - (1 + h0**2)*x[2]
    P3 = all(v >= 0 for v in (chi3(p), chi21(p), chi3(s), chi21(s)))
    R7c = name.startswith('corpus')
    out['rules'][name] = {'N_term_passes': worst < mp.mpf(10)**-40, 'max_nonneutral_coef': mp.nstr(worst, 8),
                          'nonneutral_terms': nonneutral, 'P3_passes': bool(P3),
                          'chi': [mp.nstr(v, 8) for v in (chi3(p), chi21(p), chi3(s), chi21(s))],
                          'R7c_weights_in_Zq': R7c}
(here/'borromean-factorisation-selection.witness.json').write_text(json.dumps(out, indent=1))
for k, v in out['rules'].items():
    print(k, '| N-term:', v['N_term_passes'], v['max_nonneutral_coef'], '| P3:', v['P3_passes'], v['chi'], '| R7c:', v['R7c_weights_in_Zq'])
