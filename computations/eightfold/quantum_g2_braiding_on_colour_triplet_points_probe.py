"""Check D (this thread): which U_q(g2)-endomorphisms of V7 (x) V7 preserve W = 3 (x) 3 ?
The triplet 3 = span{v1,v6,v5} is forced as a subspace by its weights (each weight has
multiplicity 1 in V7), so any K-stable copy of the colour triplet is this one.
Exact rational arithmetic at q in {1,2,3,5/2}. At q=1, classical U(g2) (E,F,H primitive)."""
import sys, json
from fractions import Fraction as Fr
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import quantum_g2_colour_stabilizer_probe as P

def gens(q):
    E, F, K, Ki = P.module(q)
    I = P.eye(7); G = []
    for i in (1, 2):
        if q == 1:
            H = P.zeros(7)
            for v, lab in enumerate(P.LAB): H[v][v] = Fr(lab[i-1])
            for X in (E[i], F[i], H): G.append(P.add(P.kron(X, I), P.kron(I, X)))
        else:
            G.append(P.add(P.kron(E[i], I), P.kron(K[i], E[i])))
            G.append(P.add(P.kron(F[i], Ki[i]), P.kron(I, F[i])))
    return G

def wt(v): return P.LAB[v]
basis = [(a, b) for a in range(7) for b in range(7)]
W = [i for i, (a, b) in enumerate(basis) if a in P.TRIP and b in P.TRIP]
def tw(i):
    a, b = basis[i]; return (wt(a)[0]+wt(b)[0], wt(a)[1]+wt(b)[1])
# weight-preserving unknown entries m[r][c]
var = [(r, c) for r in range(49) for c in range(49) if tw(r) == tw(c)]
idx = {rc: k for k, rc in enumerate(var)}

def commutant(q):
    G = gens(q); eqs = []
    for X in G:
        # (mX - Xm)[r][c] = sum_t m[r][t]X[t][c] - X[r][t]m[t][c]
        for r in range(49):
            for c in range(49):
                row = {}
                for t in range(49):
                    if X[t][c] and (r, t) in idx: row[idx[(r, t)]] = row.get(idx[(r, t)], 0) + X[t][c]
                    if X[r][t] and (t, c) in idx: row[idx[(t, c)]] = row.get(idx[(t, c)], 0) - X[r][t]
                row = {k: v for k, v in row.items() if v}
                if row: eqs.append(row)
    return eqs

def solve(eqs, nvar):
    # sparse RREF -> nullspace basis
    piv = {}  # col -> row dict
    for row in eqs:
        row = dict(row)
        for c, prow in piv.items():
            if c in row:
                f = row[c]
                for k, v in prow.items(): row[k] = row.get(k, 0) - f*v
                row = {k: v for k, v in row.items() if v}
        if not row: continue
        c = min(row); inv = 1/row[c]; row = {k: v*inv for k, v in row.items()}
        for c2 in list(piv):
            p = piv[c2]
            if c in p:
                f = p[c]
                for k, v in row.items(): p[k] = p.get(k, 0) - f*v
                piv[c2] = {k: v for k, v in p.items() if v}
        piv[c] = row
    free = [c for c in range(nvar) if c not in piv]
    out = []
    for f in free:
        v = [Fr(0)]*nvar; v[f] = Fr(1)
        for c, p in piv.items(): v[c] = -p.get(f, 0)
        out.append(v)
    return out

def run(q):
    C = solve(commutant(q), len(var))
    # within span(C), elements preserving W: block (r not in W, c in W) = 0
    Wset = set(W)
    leak = [k for k, (r, c) in enumerate(var) if c in Wset and r not in Wset]
    eqs = []
    for k in leak:
        row = {j: C[j][k] for j in range(len(C)) if C[j][k]}
        if row: eqs.append(row)
    sub = solve(eqs, len(C))
    res = {"q": str(q), "commutant_dim": len(C), "W_preserving_dim": len(sub)}
    # restrict each W-preserving element to W and record min poly degree info
    mats = []
    for s in sub:
        m = [Fr(0)]*len(var)
        for j, cj in enumerate(s):
            if cj:
                for k in range(len(var)): m[k] += cj*C[j][k]
        M = [[Fr(0)]*9 for _ in range(9)]
        for k, (r, c) in enumerate(var):
            if r in Wset and c in Wset: M[W.index(r)][W.index(c)] = m[k]
        mats.append(M)
    scal = all(all(M[i][j] == (M[0][0] if i == j else 0) for i in range(9) for j in range(9)) for M in mats)
    res["W_preserving_all_scalar_on_W"] = scal
    return res

if __name__ == "__main__":
    out = [run(Fr(x)) for x in ("1", "2", "3", "5/2")]
    print(json.dumps(out, indent=1))
