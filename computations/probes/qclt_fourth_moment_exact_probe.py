#!/usr/bin/env python3
"""
qclt_fourth_moment_exact_probe.py -- the fourth moment of the centred Hecke generator
sum under the convention-D Markov trace, in exact rational arithmetic.

Bean qou-e1uf (q-CLT), bean qou-o8lo.  Tests the pinned limit of
QOU.Observations.QCltCut: m4/m2^2 -> 2 + q (q-Gaussian).

Model (exact, no floats): the convention-D Markov trace on H_n(q) is the U_q(sl2)
quantum trace on V^{(x)n}: omega(x) = Tr(mu^{(x)n} x) / Tr(mu)^n with mu = diag(1, q^-2),
sigma_i = R-matrix on tensor factors (i, i+1), eigenvalues q, -q^-1.  The probe checks
tr(sigma_0) = q^3/(q^2+1) (= z_D) exactly.  S = sum_{i<n-1} (sigma_i - z), k = n - 1,
m2 = omega(S^2)/k, m4 = omega(S^4)/k^2.

Finding: for n >= 5 the ratio r(k) = m4/m2^2 is exactly a + b/k + c/k^2 in k... checked
by solving with three exact points and confirming on further points; the solved a is 3
at every q tested.  So the limit is the CLASSICAL Gaussian (3), not the q-Gaussian
(2 + q).  Reason: omega is a product state and sigma_i, sigma_j with |i - j| >= 2 act on
disjoint factors, so crossing pairings factorise with weight 1.
"""
from __future__ import annotations
import sys
from fractions import Fraction as F


def moments(n: int, q: F):
    qi = 1 / q
    h = q - qi
    mu = (F(1), qi * qi)

    def R(vec, i):
        out = {}
        for b, c in vec.items():
            x, y = (b >> i) & 1, (b >> (i + 1)) & 1
            sw = b ^ (1 << i) ^ (1 << (i + 1))
            if x == y:
                out[b] = out.get(b, 0) + c * q
            elif x == 0:
                out[sw] = out.get(sw, 0) + c
            else:
                out[sw] = out.get(sw, 0) + c
                out[b] = out.get(b, 0) + c * h
        return out

    def wt(b):
        w = F(1)
        for j in range(n):
            w *= mu[(b >> j) & 1]
        return w

    Z = (mu[0] + mu[1]) ** n
    z = sum(wt(b) * R({b: F(1)}, 0).get(b, 0) for b in range(2 ** n)) / Z

    def S(vec):
        out = {}
        for i in range(n - 1):
            for bb, cc in R(vec, i).items():
                out[bb] = out.get(bb, 0) + cc
            for bb, cc in vec.items():
                out[bb] = out.get(bb, 0) - z * cc
        return out

    m2 = m4 = F(0)
    for b in range(2 ** n):
        v2 = S(S({b: F(1)}))
        v4 = S(S(v2))
        w = wt(b)
        m2 += w * v2.get(b, 0)
        m4 += w * v4.get(b, 0)
    k = n - 1
    return z, m2 / (Z * k), m4 / (Z * k * k)


def solve3(pts):
    """Exact a, b, c with r = a + b/k + c/k^2 through three (k, r) points."""
    import itertools
    (k1, r1), (k2, r2), (k3, r3) = pts
    M = [[F(1), F(1, k), F(1, k * k)] for k in (k1, k2, k3)]
    rhs = [r1, r2, r3]
    # Gaussian elimination over Q
    for col in range(3):
        piv = next(r for r in range(col, 3) if M[r][col] != 0)
        M[col], M[piv] = M[piv], M[col]
        rhs[col], rhs[piv] = rhs[piv], rhs[col]
        for r in range(3):
            if r != col and M[r][col] != 0:
                f = M[r][col] / M[col][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[col])]
                rhs[r] -= f * rhs[col]
    return [rhs[i] / M[i][i] for i in range(3)]


def main() -> int:
    ok = True
    for q in (F(11, 10), F(3, 2), F(2)):
        pts = []
        for n in (6, 7, 8, 9):
            z, m2, m4 = moments(n, q)
            assert z == q ** 3 / (q ** 2 + 1), "trace is not convention D"
            pts.append((n - 1, m4 / (m2 * m2)))
        a, b, c = solve3(pts[:3])
        k4, r4 = pts[3]
        fits = (a + b / k4 + c / (k4 * k4)) == r4
        print(f"q = {q}: limit m4/m2^2 = {a}  (q-Gaussian pin 2+q = {2 + q});"
              f" exact fit confirmed on 4th point: {fits}")
        ok &= (a == 3) and fits
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
