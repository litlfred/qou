#!/usr/bin/env python3
"""Exact probe: U_q(sl2) on V^{(x)r} and the Schur-Weyl trace split, in the conventions of
QOU/Archimedean/RossoJonesMiddle.lean (bean qou-gd90, parent qou-q425).

Arithmetic: fractions.Fraction at rational sample points q (exact; no floats).

  E = sum_k e_k (x) K^{(x) sites > k},   e: 0 -> 1,   K = diag(q^-1 on 0, q on 1)   (Lean `Em`)
  F = sum_k K^-1^{(x) sites < k} (x) f_k,  f: 1 -> 0                              (Lean `Fm`)
Checked for 1 <= r <= 6 at q in {2, 3/2, -5/7, 1}:
  (a) [E, F] = diag( [2 ones(b) - r]_q )  (signed q-integer; [N] = (q^N - q^-N)/(q - q^-1));
  (b) E : V_m -> V_{m+1} injective for 2m < r, surjective for 2m + 1 >= r;
  (c) gamma E = E gamma (gamma = sigma_0 ... sigma_{r-2});
  (d) the trace split  T_m(gamma^p) = sum_{j <= min(m, r-m)} tr(gamma^p | W_{r,j}),
      W_{r,j} = ker E  intersected with V_{r-j}  (V_m = span of states with m ones), 1 <= p <= r + 1;
  (e) records the scalar by which gamma^r (the full twist) acts on W_{r,j}, if it is one.
      Observed (q = 2, r <= 6): a scalar, q^{r(r-1) - 2j(r-j+1)}.
Exit status 0 iff (a)-(d) pass.
"""
from fractions import Fraction as Fr
from itertools import product
import sys

def states(r):
    return list(product((0, 1), repeat=r))

def zeros_mat(N):
    return [[Fr(0)] * N for _ in range(N)]

def matmul(A, B):
    N, M, P = len(A), len(B), len(B[0])
    C = [[Fr(0)] * P for _ in range(N)]
    for i in range(N):
        Ai = A[i]
        for k in range(M):
            a = Ai[k]
            if a:
                Bk = B[k]
                for j in range(P):
                    if Bk[j]:
                        C[i][j] += a * Bk[j]
    return C

def ki(q, x):
    return 1 / q if x == 0 else q

def build(r, q):
    S = states(r); idx = {s: i for i, s in enumerate(S)}; N = len(S)
    E, F = zeros_mat(N), zeros_mat(N)
    for b in S:
        for k in range(r):
            if b[k] == 0:
                a = list(b); a[k] = 1
                w = Fr(1)
                for l in range(k + 1, r):
                    w *= ki(q, b[l])
                E[idx[tuple(a)]][idx[b]] += w
            else:
                a = list(b); a[k] = 0
                w = Fr(1)
                for l in range(k):
                    w /= ki(q, b[l])
                F[idx[tuple(a)]][idx[b]] += w
    # gamma = sigma_0 ... sigma_{r-2}, rCheck: q on equal pair, q - q^-1 on (0,1) diag, 1 on swap
    G = [[Fr(int(i == j)) for j in range(N)] for i in range(N)]
    for i in range(r - 1):
        Sg = zeros_mat(N)
        for b in S:
            x, y = b[i], b[i + 1]
            if x == y:
                Sg[idx[b]][idx[b]] += q
            else:
                sw = list(b); sw[i], sw[i + 1] = y, x
                Sg[idx[tuple(sw)]][idx[b]] += 1
                if x < y:
                    Sg[idx[b]][idx[b]] += q - 1 / q
        G = matmul(G, Sg)
    return S, idx, E, F, G

def qZ(q, Nn):
    if Nn >= 0:
        return sum((q ** (Nn - 1 - 2 * t) for t in range(Nn)), Fr(0))
    return -qZ(q, -Nn)

def rank(M):
    M = [row[:] for row in M]
    if not M or not M[0]:
        return 0
    rows, cols = len(M), len(M[0]); rk = 0
    for c in range(cols):
        piv = next((i for i in range(rk, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(rows):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / M[rk][c]
                M[i] = [M[i][t] - f * M[rk][t] for t in range(cols)]
        rk += 1
    return rk

def nullspace(M):
    """basis (list of column vectors) of the kernel of M (rows x cols)."""
    rows, cols = len(M), len(M[0]) if M else 0
    A = [row[:] for row in M]; pivcols = []; rk = 0
    for c in range(cols):
        piv = next((i for i in range(rk, rows) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[rk], A[piv] = A[piv], A[rk]
        pv = A[rk][c]; A[rk] = [x / pv for x in A[rk]]
        for i in range(rows):
            if i != rk and A[i][c] != 0:
                f = A[i][c]; A[i] = [A[i][t] - f * A[rk][t] for t in range(cols)]
        pivcols.append(c); rk += 1
    free = [c for c in range(cols) if c not in pivcols]
    basis = []
    for fc in free:
        v = [Fr(0)] * cols; v[fc] = Fr(1)
        for i, pc in enumerate(pivcols):
            v[pc] = -A[i][fc]
        basis.append(v)
    return basis

def trace_on(X, B):
    """trace of X restricted to the invariant subspace spanned by columns B (list of vectors)."""
    if not B:
        return Fr(0), None
    n = len(B[0]); k = len(B)
    # solve B C = X B for C (k x k) by least-squares-free elimination on [B | XB]
    XB = [[sum(X[i][t] * b[t] for t in range(n)) for i in range(n)] for b in B]
    # augmented: rows = coordinates, columns = basis vectors
    aug = [[B[c][i] for c in range(k)] + [XB[c][i] for c in range(k)] for i in range(n)]
    rk = 0; piv = []
    for c in range(k):
        p = next((i for i in range(rk, n) if aug[i][c] != 0), None)
        aug[rk], aug[p] = aug[p], aug[rk]
        pv = aug[rk][c]; aug[rk] = [x / pv for x in aug[rk]]
        for i in range(n):
            if i != rk and aug[i][c] != 0:
                f = aug[i][c]; aug[i] = [aug[i][t] - f * aug[rk][t] for t in range(2 * k)]
        rk += 1
    for i in range(k, n):  # invariance check
        assert all(aug[i][t] == 0 for t in range(k, 2 * k)), "not invariant"
    C = [[aug[i][k + j] for j in range(k)] for i in range(k)]
    tr = sum(C[i][i] for i in range(k))
    scalar = C[0][0] if all(C[i][j] == (C[0][0] if i == j else 0) for i in range(k) for j in range(k)) else None
    return tr, scalar

def main():
    fails = checks = 0
    for q in (Fr(2), Fr(3, 2), Fr(-5, 7), Fr(1)):
        for r in range(1, 7):
            S, idx, E, F, G = build(r, q); N = len(S)
            EF, FE = matmul(E, F), matmul(F, E)
            for i in range(N):
                for j in range(N):
                    want = qZ(q, 2 * sum(S[i]) - r) if i == j else 0
                    checks += 1
                    if EF[i][j] - FE[i][j] != want:
                        fails += 1; print("[E,F] FAIL", q, r, S[i], S[j])
            GE, EG = matmul(G, E), matmul(E, G)
            checks += 1
            if GE != EG:
                fails += 1; print("gamma E != E gamma", q, r)
            Vm = {m: [i for i in range(N) if sum(S[i]) == m] for m in range(r + 1)}
            for m in range(r):
                sub = [[E[i][j] for j in Vm[m]] for i in Vm[m + 1]]
                rk = rank(sub); checks += 1
                if 2 * m < r and rk != len(Vm[m]):
                    fails += 1; print("E not injective", q, r, m)
                if 2 * m + 1 >= r and rk != len(Vm[m + 1]):
                    fails += 1; print("E not surjective", q, r, m)
            # W_{r,j} = ker E  on V_{r-j}, embedded in V^{(x)r}
            W = {}
            for j in range(r // 2 + 1):
                cols = Vm[r - j]
                sub = [[E[i][c] for c in cols] for i in range(N)]
                W[j] = []
                for v in nullspace(sub):
                    full = [Fr(0)] * N
                    for t, c in enumerate(cols):
                        full[c] = v[t]
                    W[j].append(full)
            Gp = [[Fr(int(i == j)) for j in range(N)] for i in range(N)]
            for p in range(1, r + 2):
                Gp = matmul(G, Gp)
                trW = {j: trace_on(Gp, W[j]) for j in W}
                for m in range(r + 1):
                    Tm = sum(Gp[i][i] for i in Vm[m])
                    split = sum(trW[j][0] for j in W if j <= min(m, r - m))
                    checks += 1
                    if Tm != split:
                        fails += 1; print("split FAIL", q, r, p, m)
                if p == r and q == Fr(2):
                    print(f"r={r}: full twist gamma^r on W_(r,j):",
                          {j: (len(W[j]), trW[j][1]) for j in W})
    print(f"checks={checks} fails={fails}")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
