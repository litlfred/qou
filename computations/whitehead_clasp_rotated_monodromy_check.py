#!/usr/bin/env python3
"""Exact symbolic check: van der Veen's clasp C(n,t) is the 90-degree-rotated monodromy.

Context: issue #7912 (deriving van der Veen 2008, Lemma 1). The clasp tangle has
antiparallel strands, so it is the full twist M = Ř'Ř turned through 90 degrees.
Bending M with the U_q(sl2)-invariant cup/cap of V_N (V_N* identified with V_N) gives

    X = (cap ⊗ 1 ⊗ 1)(1 ⊗ M ⊗ 1)(1 ⊗ 1 ⊗ cup)   on V_N ⊗ V_N.

This script checks, in exact rational functions of s (q = s^2, t = q^2), that X acts
on the highest-weight vector of each summand V_{2n+1} by

    (-1)^(N-1) * t^{N(N-1)/2} * sum_{k=0}^{N-1-n} t^{-N(n+k)}
        * prod_{j=1}^{n} (1 - t^{N-j-k})(1 - t^{j+k}) / (1 - t^j),

which is van der Veen's C(n,t) without the same-component framing factor
t^{(N^2-1)/2}. The sign (-1)^(N-1) is the Frobenius-Schur indicator of V_N, which
enters through the identification V_N* = V_N.

Conventions match QOU/Mass/QuantumSl2RMatrix.lean (Kassel): R = Theta * sum_n c_n E^n (x) F^n,
c_n = s^{n(n-1)} (q - q^-1)^n / [n]!.

No floating point: everything is exact sympy rational functions in s.
Usage: python3 whitehead_clasp_rotated_monodromy_check.py [N ...]   (default 2 3 4)
"""
import sys
import sympy as sp

s = sp.symbols("s", positive=True)
q = s**2


def qi(n):
    return sp.cancel((q**n - q**-n) / (q - 1 / q))


def qfact(n):
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= qi(k)
    return r


def irrep(m):
    d = m + 1
    E, F, K = sp.zeros(d), sp.zeros(d), sp.zeros(d)
    for p in range(d):
        K[p, p] = q**(m - 2 * p)
        if p >= 1:
            E[p - 1, p] = qi(m - p + 1)
        if p + 1 < d:
            F[p + 1, p] = qi(p + 1)
    return E, F, K


def kron(A, B):
    return sp.kronecker_product(A, B)


def rmat(m):
    E, F, _ = irrep(m)
    S = sp.zeros((m + 1) ** 2)
    for n in range(m + 1):
        S += s**(n * (n - 1)) * (q - 1 / q)**n / qfact(n) * kron(E**n, F**n)
    theta = sp.diag(*[s**((m - 2 * p) * (m - 2 * r)) for p in range(m + 1) for r in range(m + 1)])
    return theta * S


def swap(d):
    P = sp.zeros(d * d)
    for p in range(d):
        for r in range(d):
            P[r * d + p, p * d + r] = 1
    return P


def clasp_vdv(N, n, t):
    tot = 0
    for k in range(N - n):
        pr = 1
        for j in range(1, n + 1):
            pr *= (1 - t**(N - j - k)) * (1 - t**(j + k)) / (1 - t**j)
        tot += t**(-N * (n + k)) * pr
    return t**sp.Rational(N * (N - 1), 2) * tot


def check(N):
    m, d = N - 1, N
    E, F, K = irrep(m)
    I = sp.eye(d)
    Rc = swap(d) * rmat(m)
    M = sp.simplify(Rc * Rc)
    dE = kron(E, K) + kron(I, E)
    dF = kron(F, I) + kron(K.inv(), F)
    dK = kron(K, K)
    one = sp.eye(d * d)
    cup = sp.Matrix.vstack(dE, dF, dK - one).nullspace()
    cap = sp.Matrix.vstack(dE.T, dF.T, (dK - one).T).nullspace()
    assert len(cup) == 1 and len(cap) == 1
    cup, cap = cup[0], cap[0].T
    cup = cup / cup[m]  # normalise a_0 = 1 at v_0 (x) v_m
    lam = sp.simplify((kron(cap, I) * kron(I, cup))[0, 0])
    cap = cap / lam
    # Closed forms (Lean targets for Stage 3b):
    #   cup a_p = (-1)^p q^{p(m-p-1)} / qbinom(m,p)   (= hwCoef q m m m p)
    #   cap b_p = (-1)^m q^{m-2p} / a_p               (quantum-trace weight, FS sign)
    for pp in range(d):
        qb = qfact(m) / (qfact(pp) * qfact(m - pp))
        a_pp = (-1)**pp * q**(pp * (m - pp - 1)) / qb
        assert sp.simplify(cup[pp * d + m - pp] - a_pp) == 0, ("cup", N, pp)
        assert sp.simplify(cap[pp * d + m - pp] - (-1)**m * q**(m - 2 * pp) / a_pp) == 0, ("cap", N, pp)
    print(f"N={N}: cup/cap closed forms OK")
    assert sp.simplify(kron(cap, I) * kron(I, cup) - I) == sp.zeros(d)
    assert sp.simplify(kron(I, cap) * kron(cup, I) - I) == sp.zeros(d)
    X = sp.simplify(kron(cap, kron(I, I)) * kron(I, kron(M, I)) * kron(I, kron(I, cup)))
    t = s**4
    ok = True
    for n in range(N):
        w = sp.Matrix.vstack(dE, dK - q**(2 * n) * one).nullspace()[0]
        i0 = next(i for i in range(d * d) if w[i] != 0)
        c = sp.simplify((X * w)[i0] / w[i0])
        assert sp.simplify(X * w - c * w) == sp.zeros(d * d, 1)
        # Term-by-term: read the eigenvalue at output v_j (x) v_0 (j = m - n). The sum over the
        # support v_k (x) v_{j-k} of w_j reproduces van der Veen's sum over k with NO summation
        # identity: each entry X[(j,0),(k,j-k)] is a single product of R-matrix entries.
        j = m - n
        o = j * d
        terms = [sp.factor(X[o, i] * w[i] / w[o]) for i in range(d * d) if w[i] != 0]
        vdv_terms = []
        for kk in range(N - n):
            pr = 1
            for jj in range(1, n + 1):
                pr *= (1 - t**(N - jj - kk)) * (1 - t**(jj + kk)) / (1 - t**jj)
            vdv_terms.append(sp.factor((-1)**(N - 1) * t**sp.Rational(N * (N - 1), 2)
                                       * t**(-N * (n + kk)) * pr))
        assert sorted(map(str, terms)) == sorted(map(str, vdv_terms)), ("termwise", N, n)
        ratio = sp.simplify(c / clasp_vdv(N, n, t))
        good = sp.simplify(ratio - (-1)**(N - 1)) == 0
        ok &= good
        print(f"N={N} n={n}: X/C_vdv = {ratio}, termwise match  {'OK' if good else 'MISMATCH'}")
    return ok


if __name__ == "__main__":
    Ns = [int(a) for a in sys.argv[1:]] or [2, 3, 4]
    results = [check(N) for N in Ns]
    print("ALL OK" if all(results) else "FAILED")
    sys.exit(0 if all(results) else 1)
