#!/usr/bin/env python3
"""Reeb-holonomy Laplacian on the regular representation of H_n(q), exact (issue #8091).

Checks, in exact arithmetic (sympy over Q(q), or exact rationals at q = 3), with the skein
convention T^2 = (q - q^-1) T + 1 and the Murphy elements L_0 = 1, L_k = T_k L_{k-1} T_k:

  1. L_k = (Delta^2_{k-1})^{-1} Delta^2_k  (relative full twist), Delta^2_k = (T_1...T_k)^{k+1};
  2. C_n = sum_k (q L_k + q^-1 L_k^-1 - (q + q^-1)) is central;
  3. the spectrum of C_n on the regular representation is (q - q^-1)^2 sum_cells [c][c+1]
     (symmetric q-integers) with multiplicity d_lambda^2 -- no seminormal form is used;
  4. (n <= 3, symbolic q) C_n / (q - q^-1)^2 -> sum_k X_k (X_k + 1) as q -> 1, X_k classical JM.

No floating point anywhere. Audit: docs/audits/2026-11-16-binding-reeb-holonomy-laplacian.md.
Lean: QOU/BraidKnot/HeckeReebHolonomyLaplacian.lean.
"""
import itertools
import sys

import sympy as sp
from sympy.utilities.iterables import partitions

FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def length(w):
    return sum(1 for i in range(len(w)) for j in range(i + 1, len(w)) if w[i] > w[j])


def regular_rep(n, q):
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    N = len(perms)
    Ts = []
    for i in range(n - 1):
        M = sp.zeros(N, N)
        for w in perms:
            sw = tuple(i + 1 if x == i else i if x == i + 1 else x for x in w)
            if length(sw) > length(w):
                M[idx[sw], idx[w]] += 1
            else:
                M[idx[w], idx[w]] += q - 1 / q
                M[idx[sw], idx[w]] += 1
        Ts.append(M)
    return Ts, N


def predicted_spectrum(n, q):
    def br(m):
        return (q ** m - q ** (-m)) / (q - 1 / q)
    pred = {}
    for p in partitions(n):
        lam = sorted([k for k, v in p.items() for _ in range(v)], reverse=True)
        cells = [(i, j) for i, r in enumerate(lam) for j in range(r)]
        conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
        hooks = 1
        for i, j in cells:
            hooks *= (lam[i] - j - 1) + (conj[j] - i - 1) + 1
        val = sp.nsimplify((q - 1 / q) ** 2 * sum(br(j - i) * br(j - i + 1) for i, j in cells))
        pred[val] = pred.get(val, 0) + (sp.factorial(n) / hooks) ** 2
    return pred


def run(n, q, symbolic):
    Ts, N = regular_rep(n, q)
    I = sp.eye(N)
    simp = sp.simplify if symbolic else (lambda M: M)
    L = [I]
    for k in range(1, n):
        L.append(Ts[k - 1] * L[-1] * Ts[k - 1])
    FT = [I]
    for k in range(1, n):
        d = I
        for j in range(k):
            d = d * Ts[j]
        FT.append(d ** (k + 1))
    check(f"n={n}: L_k is the relative full twist",
          all(simp(FT[k] - FT[k - 1] * L[k]) == sp.zeros(N, N) for k in range(1, n)))
    C = sum((q * Lk + Lk.inv() / q - (q + 1 / q) * I for Lk in L), sp.zeros(N, N))
    check(f"n={n}: C_n central", all(simp(T * C - C * T) == sp.zeros(N, N) for T in Ts))
    qv = sp.Rational(3)
    Cv = C.subs(q, qv) if symbolic else C
    ev = {sp.nsimplify(k): v for k, v in Cv.eigenvals().items()}
    check(f"n={n}: spectrum at q=3 = (q-q^-1)^2 sum[c][c+1], mult d^2",
          ev == predicted_spectrum(n, qv))
    if symbolic:
        D = (C / (q - 1 / q) ** 2).applyfunc(lambda e: sp.limit(sp.cancel(e), q, 1))
        P = [T.subs(q, 1) for T in Ts]

        def transp(i, j):
            M = I
            for s in list(range(j - 1, i, -1)) + [i] + list(range(i + 1, j)):
                M = M * P[s]
            return M
        X = [sum((transp(i, k) for i in range(k)), sp.zeros(N, N)) for k in range(n)]
        S = sum((Xk * (Xk + I) for Xk in X), sp.zeros(N, N))
        check(f"n={n}: q->1 limit is sum X_k(X_k+1)", sp.simplify(D - S) == sp.zeros(N, N))


def main():
    q = sp.symbols("q")
    for n in (2, 3):
        run(n, q, symbolic=True)
    run(4, sp.Rational(3), symbolic=False)
    print(f"{len(FAILS)} failures")
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
