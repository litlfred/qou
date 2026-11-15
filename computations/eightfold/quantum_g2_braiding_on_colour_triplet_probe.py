"""Check D (bean qou-cb3r, option C): which U_q(g2)-intertwiners of V7 (x) V7 preserve W = 3 (x) 3 ?

Exact over the field Q(q) (sympy DomainMatrix over QQ.frac_field(q)); q is a symbol, not a sample.
Same module and Jantzen coproduct as quantum_g2_colour_stabilizer_probe.py.

Why W is the only candidate: each weight of the triplet 3 = span{v1, v6, v5} has multiplicity 1
in V7, so any K-stable 3-dim subspace with the triplet's weights IS this span. This closes the
"other q-deformed embeddings" gap of check B for K-stable embeddings.

Every braiding R-check_{V7,V7} lies in End_{U_q(g2)}(V7 (x) V7). If some element of that algebra
preserved W and restricted to a Hecke operator with two distinct eigenvalues (as Jimbo's R-check does
on Q^3 (x) Q^3), it would show up below as a W-preserving element that is not scalar on W.
Scope (b) for the statements printed (generic q, i.e. over Q(q)); specialisation to a particular q0 is
not claimed.
"""
import sys, json, sympy as sp
q = sp.symbols('q', positive=True)
LAB = [(1, 0), (-1, 1), (2, -1), (0, 0), (-2, 1), (1, -1), (-1, 0)]
TRIP = [0, 5, 4]
def qint(n, x): return sum(x**(n-1-2*k) for k in range(n))
def module():
    q1, q2 = q, q**3
    Z = lambda: sp.zeros(7)
    E = {1: Z(), 2: Z()}; F = {1: Z(), 2: Z()}; K = {1: Z(), 2: Z()}; Ki = {1: Z(), 2: Z()}
    for v, (a, b) in enumerate(LAB):
        K[1][v, v] = q1**a; K[2][v, v] = q2**b; Ki[1][v, v] = q1**-a; Ki[2][v, v] = q2**-b
    strings = {1: [[0, 1], [2, 3, 4], [5, 6]], 2: [[1, 2], [4, 5]]}
    for i, sts in strings.items():
        qi = q1 if i == 1 else q2
        for st in sts:
            n = len(st)
            for k in range(1, n):
                a, b = st[k-1], st[k]; F[i][b, a] = 1; E[i][a, b] = qint(k, qi)*qint(n-k, qi)
    return E, F, K, Ki
E, F, K, Ki = module(); I = sp.eye(7)
from sympy.physics.quantum import TensorProduct as TP
G = []
for i in (1, 2):
    G.append(TP(E[i], I) + TP(K[i], E[i])); G.append(TP(F[i], Ki[i]) + TP(I, F[i]))
basis = [(a, b) for a in range(7) for b in range(7)]
tw = lambda i: (LAB[basis[i][0]][0]+LAB[basis[i][1]][0], LAB[basis[i][0]][1]+LAB[basis[i][1]][1])
var = [(r, c) for r in range(49) for c in range(49) if tw(r) == tw(c)]
idx = {rc: k for k, rc in enumerate(var)}
rows = []
for X in G:
    for r in range(49):
        for c in range(49):
            row = {}
            for t in range(49):
                if X[t, c] != 0 and (r, t) in idx: row[idx[(r, t)]] = row.get(idx[(r, t)], 0) + X[t, c]
                if X[r, t] != 0 and (t, c) in idx: row[idx[(t, c)]] = row.get(idx[(t, c)], 0) - X[r, t]
            row = {k: sp.cancel(v) for k, v in row.items() if sp.cancel(v) != 0}
            if row: rows.append(row)
A = sp.zeros(len(rows), len(var))
for i, row in enumerate(rows):
    for k, v in row.items(): A[i, k] = v
from sympy.polys.matrices import DomainMatrix
dom = sp.QQ.frac_field(q)
dm = DomainMatrix.from_Matrix(A).convert_to(dom)
N = dm.nullspace().to_Matrix()   # rows = basis vectors
print("commutant dim over Q(q):", N.shape[0])
W = [i for i, (a, b) in enumerate(basis) if a in TRIP and b in TRIP]; Ws = set(W)
leak = [k for k, (r, c) in enumerate(var) if c in Ws and r not in Ws]
L = N[:, leak].T
sub = DomainMatrix.from_Matrix(L).convert_to(dom).nullspace().to_Matrix()
print("W-preserving dim over Q(q):", sub.shape[0])
allscalar = True
for s in range(sub.shape[0]):
    m = (sub[s, :] * N)
    M = sp.zeros(9)
    for k, (r, c) in enumerate(var):
        if r in Ws and c in Ws: M[W.index(r), W.index(c)] = sp.cancel(m[k])
    ok = all(sp.cancel(M[i, j] - (M[0, 0] if i == j else 0)) == 0 for i in range(9) for j in range(9))
    print(" element", s, "scalar on 3(x)3:", ok, " value:", sp.factor(M[0, 0]))
    allscalar &= ok
print("ALL W-preserving intertwiners scalar on 3(x)3 over Q(q):", allscalar)
import os
json.dump({"producer": "computations/eightfold/quantum_g2_braiding_on_colour_triplet_probe.py",
           "bean": "qou-cb3r", "arithmetic": "sympy DomainMatrix over QQ(q) (exact, generic q)",
           "commutant_dim": int(N.shape[0]), "W_preserving_dim": int(sub.shape[0]),
           "all_W_preserving_scalar_on_W": bool(allscalar)},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
               "quantum-g2-braiding-on-colour-triplet.witness.json"), "w"), indent=1)
