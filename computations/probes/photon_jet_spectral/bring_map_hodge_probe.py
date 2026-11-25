#!/usr/bin/env python3
"""Bring's surface as the regular map {5,4} with rotation group S5 (audit §14, item 5).
Darts = the 120 elements g of S5 (right regular action). Vertex rotation sigma(g) = g*S (order 4),
edge involution alpha(g) = g*A (fixed-point free, order 2), face rotation phi = sigma*alpha with
S*A of order 5. Vertices, edges, faces = orbits of <S>, <A>, <S*A>. Boundary maps are built with
orientations; d1 o d2 = 0 is checked. The combinatorial Hodge Laplacian on 1-cochains,
Delta_1 = d1^T d1 + d2 d2^T, has kernel of dimension b1 = 2g. Exact integer/rational ranks
(Fraction Gaussian elimination), no floats. Never reads q0."""
import itertools, json
from pathlib import Path
from fractions import Fraction as Fr
n = 5
G = list(itertools.permutations(range(n)))
def mul(a, b): return tuple(a[b[i]] for i in range(n))      # (a*b)(i) = a(b(i))
def order(a):
    e = tuple(range(n)); x = a; k = 1
    while x != e: x = mul(x, a); k += 1
    return k
def closure(gens):
    e = tuple(range(n)); S = {e}; fr = [e]
    while fr:
        nf = []
        for x in fr:
            for g in gens:
                y = mul(x, g)
                if y not in S: S.add(y); nf.append(y)
        fr = nf
    return S
found = None
for S in G:
    if order(S) != 4: continue
    for A in G:
        if order(A) != 2: continue
        if order(mul(S, A)) == 5 and len(closure([S, A])) == 120:
            # prefer A a transposition (for the Lean generation lemma)
            if sum(1 for i in range(n) if A[i] != i) == 2: found = (S, A); break
    if found: break
S, A = found
def orbits(gen):
    seen = {}; reps = []
    for g in G:
        if g in seen: continue
        k = len(reps); x = g
        while x not in seen: seen[x] = k; x = mul(x, gen)
        reps.append(g)
    return seen, len(reps)
vtx, nV = orbits(S); edg, nE = orbits(A); fac, nF = orbits(mul(S, A))
# orient each edge by a chosen representative dart d0: d0 goes from vtx[d0] to vtx[alpha d0]
rep = {}
for g in G:
    e = edg[g]
    if e not in rep: rep[e] = g
def sign(d): return 1 if rep[edg[d]] == d else -1
def zeros(r, c): return [[0]*c for _ in range(r)]
def matmul(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)) if X[i][k]) for j in range(len(Y[0]))] for i in range(len(X))]
def T(X): return [list(r) for r in zip(*X)]
def is_zero(X): return all(v == 0 for r in X for v in r)
def rank(X):
    M = [[Fr(v) for v in r] for r in X]; rk = 0; cols = len(M[0]) if M else 0
    for c in range(cols):
        pv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if pv is None: continue
        M[rk], M[pv] = M[pv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]/M[rk][c]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk
def nullspace(X):
    M = [[Fr(v) for v in r] for r in X]; n_ = len(M[0]); piv = []; rk = 0
    for c in range(n_):
        pv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if pv is None: continue
        M[rk], M[pv] = M[pv], M[rk]; inv = 1/M[rk][c]; M[rk] = [a*inv for a in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        piv.append(c); rk += 1
    free = [c for c in range(n_) if c not in piv]; basis = []
    for fc in free:
        v = [Fr(0)]*n_; v[fc] = Fr(1)
        for r, pc in enumerate(piv): v[pc] = -M[r][fc]
        basis.append(v)
    return basis
d1 = zeros(nV, nE)
for e, d in rep.items():
    d1[vtx[mul(d, A)]][e] += 1; d1[vtx[d]][e] -= 1
def d2_build(conv):
    M = zeros(nE, nF)
    for g in G:
        dart = g if conv == 0 else mul(g, A)
        M[edg[g]][fac[g]] += sign(dart) if conv == 0 else -sign(g)
    return M
d2 = None
for conv in (0, 1):
    for s in (1, -1):
        cand = [[s*v for v in r] for r in d2_build(conv)]
        if is_zero(matmul(d1, cand)): d2 = cand; break
    if d2 is not None: break
out = {'q0Anchor': 'independent', 'q0AnchorReason': 'finite combinatorics; never reads q0',
       'S': list(S), 'A': list(A), 'V': nV, 'E': nE, 'F': nF, 'chi': nV - nE + nF,
       'd1_d2_zero': d2 is not None}
if d2 is not None:
    a = matmul(T(d1), d1); b = matmul(d2, T(d2))
    L1 = [[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(a, b)]
    out['rank_d1'] = rank(d1); out['rank_d2'] = rank(d2)
    out['dim_ker_Delta1'] = nE - rank(L1)
    out['b1_from_ranks'] = nE - out['rank_d1'] - out['rank_d2']
    K = nullspace(L1)
    col = lambda k: [[v] for v in k]
    out['harmonic_have_zero_vorticity'] = all(is_zero(matmul(T(d2), col(k))) for k in K)
    out['harmonic_are_coclosed'] = all(is_zero(matmul(d1, col(k))) for k in K)
    out['nonzero_eigen_gap_note'] = 'kernel = harmonic 1-cochains; every other eigenvalue of Delta_1 is > 0' 
Path(__file__).with_name('bring-map-hodge.witness.json').write_text(json.dumps(out, indent=1))
print(out)
