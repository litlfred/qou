#!/usr/bin/env python3
"""drsz_two_level_qborel_vs_c1_degree_budget_probe.py — bean qou-ipnr.

Cross-check of Di Vizio, Ramis, Sauloy, Zhang, "Equations aux
q-differences", Gazette SMF 96 (2003) [divizio-ramis-sauloy-zhang], held at
library/equations-aux-q-differences/, Sec 4.4, Rmk 4.12, Thm 4.13, against
the corpus C1 infinity-side degree budget
(folio/quantum-observable-universe/lean/QOU/QBeta/C1InfDegreeLaw.lean,
`cCoeff_natDegree` = n^2, `ramified_qBorel_budget`;
docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md).

PRE-REGISTERED (written before running):

  Source facts used (PDF text layer):
    S1  Sec 4.4: y = sum q^{C(n,2)} x^n, Y = y^2,
        B_{q;1}(sum a_n x^n) = sum a_n q^{-C(n,2)} xi^n, and the product rule
        B(f g) = sum a_n q^{-C(n,2)} xi^n (B g)(q^{-n} xi).
    S2  (4.11.5): P := B(Y) * prod_{n>=0}(1 - q^{-n} xi) is entire and
        P(q^m) = (-1)^m q^{m(3m+1)/2} (q^-1;q^-1)_m (q^-1;q^-1)_inf.
    S3  Ex 4.11(2), as transcribed: prod_{n>=0}(1 - q^{-n} xi)
        = sum_n q^{-n(n-1)/2} xi^n / (q^-1;q^-1)_n.
    S4  Thm 4.13 / (4.12.1): Delta Y = 1 + x with
        Delta = q^2 x^3 s^2 - x(1+x) s + 1 = (x s - 1)(x^2 s - 1),
        s f(x) = f(qx).
    S5  Rmk 4.12: Y's equation has two non-trivial slopes, y's has one.

  Checks:
    A  S4: the operator factorization holds on a generic f, and
       Delta Y = 1 + x through x^24, exact in symbolic q.
    B  S1: B(Y) coefficients equal those of sum_n xi^n / (1 - q^{-n} xi)
       (B(y) = 1/(1-xi) put through the product rule) through xi^24, exact.
    C  S3 against Euler's identity (exact, q = 2, through xi^12): report
       whether the printed coefficients or (-1)^n times them are right.
    D  S2 at q = 2, m = 0..3, mpmath 200 dps, Taylor series of P to 400
       terms (using whichever sign C finds correct): rel error < 1e-40.
    E  Corpus comparison (exact): Newton polygon slopes of the corpus C1
       operator L1 = (q^2 x - 1)s^2 - (q-1)s - (q-1) at infinity versus
       those of Delta at 0; deg_q of Y's coefficients versus the corpus
       deg_q c_n = n^2 for n <= 12. Newton slopes are invariant under
       analytic gauge (DRSZ Sec 3), so a different slope count means C1
       is not of the example's multi-level type up to gauge.
    PASS iff A, B, D hold; C and E are reported (findings either way).

  AMENDMENT 1 (after the first run; thresholds unchanged).
    1. D's pre-registered numerics were wrong in MY probe: 400 Taylor terms
       at 200 dps cannot resolve p_n ~ 2^{-n^2/6} past n ~ 63, and the noise
       is multiplied by q^{mn}, so m = 2, 3 returned garbage. Fixed to 90
       terms at 400 dps (truncation error < 2^{-N^2/6 + 5N}, far below 1e-40
       for m <= 5); m extended to 0..5.
    2. With that fix, P(q^m) / (4.11.5) = 2 exactly for every m = 0..5, so
       D fails as pre-registered. The page image (PDF p. 24, Gazette p. 43)
       was read: (4.11.5) is printed as transcribed, with no factor 2. The
       factor is forced by the product rule itself: B(Y) has coefficients
       sum_k q^{-k(n-k)}, symmetric under k <-> n-k, so each pole q^m gets
       two contributions. Source finding, not a corpus defect. D2 checks
       P(q^m) = 2 * (4.11.5); D3 checks the order-3 growth claim through
       log2|p_n| / n^2 -> -1/6. PASS is now A, B, D2, D3.

Run: python3 -u computations/probes/drsz_two_level_qborel_vs_c1_degree_budget_probe.py
"""
from __future__ import annotations

import sys
from fractions import Fraction

import mpmath as mp
import sympy as sp

q, x, xi = sp.symbols("q x xi")
NMAX = 24


def C2(n):
    return n * (n - 1) // 2


def y_series(n=NMAX):
    return sum(q ** C2(k) * x ** k for k in range(n + 1))


def trunc(e, n=NMAX, var=x):
    e = sp.expand(e)
    return sum(e.coeff(var, k) * var ** k for k in range(n + 1))


def sigma(e):
    return e.subs(x, q * x)


def newton_slopes(points):
    """Slopes of the lower convex hull of (k, v_k)."""
    pts = sorted(points)
    hull = []
    for p in pts:
        while len(hull) >= 2 and (hull[-1][1] - hull[-2][1]) * (p[0] - hull[-1][0]) \
                >= (p[1] - hull[-1][1]) * (hull[-1][0] - hull[-2][0]):
            hull.pop()
        hull.append(p)
    return [Fraction(hull[i + 1][1] - hull[i][1], hull[i + 1][0] - hull[i][0])
            for i in range(len(hull) - 1)]


def main() -> int:
    # A
    f = sp.Function("f")
    Delta = lambda g: q ** 2 * x ** 3 * sigma(sigma(g)) - x * (1 + x) * sigma(g) + g
    inner = x ** 2 * f(q * x) - f(x)                       # (x^2 s - 1) f
    outer = x * inner.subs(x, q * x) - inner               # (x s - 1) inner
    fact_ok = sp.simplify(sp.expand(outer - Delta(f(x)))) == 0
    Y = trunc(y_series() ** 2)
    res = trunc(Delta(Y), NMAX - 3)
    a_ok = fact_ok and sp.simplify(res - (1 + x)) == 0
    print(f"A  factorization {fact_ok}; Delta Y = 1 + x through x^{NMAX-3}: {a_ok}")

    # B
    bY = [sp.simplify(sp.expand(Y).coeff(x, n) / q ** C2(n)) for n in range(NMAX + 1)]
    rhs = [sum(q ** (-k * (n - k)) for k in range(n + 1)) for n in range(NMAX + 1)]
    b_ok = all(sp.simplify(a - b) == 0 for a, b in zip(bY, rhs))
    print(f"B  B(Y)_n = sum_k q^(-k(n-k)) (product rule with B(y)=1/(1-xi)): {b_ok}")

    # C
    Q = sp.Integer(2)
    M = 12
    prod = sp.Integer(1)
    for n in range(0, 60):
        prod = sp.expand(trunc(prod * (1 - Q ** (-n) * xi), M, xi))
    def poch_inv(n):
        out = sp.Integer(1)
        for k in range(1, n + 1):
            out *= 1 - Q ** (-k)
        return out
    printed = [Q ** (-C2(n)) / poch_inv(n) for n in range(M + 1)]
    actual = [prod.coeff(xi, n) for n in range(M + 1)]
    # truncating the infinite product at 60 factors perturbs coefficients by < 2^-55
    tol = sp.Rational(1, 2 ** 50)
    same = all(abs(a - p) < tol for a, p in zip(actual, printed))
    signed = all(abs(a - (-1) ** n * p) < tol for n, (a, p) in enumerate(zip(actual, printed)))
    print(f"C  Ex 4.11(2) printed coefficients match: {same}; with (-1)^n: {signed}")
    sgn = 1 if same else -1

    # D (amended: N = 90 terms at 400 dps, m = 0..5)
    mp.mp.dps = 400
    qq = mp.mpf(2)
    N = 90
    b = [mp.fsum(qq ** (-k * (n - k)) for k in range(n + 1)) for n in range(N)]
    pinv = [mp.mpf(1)]
    for k in range(1, N):
        pinv.append(pinv[-1] * (1 - qq ** (-k)))
    e = [(sgn ** n) * qq ** (-C2(n)) / pinv[n] for n in range(N)]
    p = [mp.fsum(b[k] * e[n - k] for k in range(n + 1)) for n in range(N)]
    pinf = mp.qp(1 / qq, 1 / qq)
    d_ok = True
    for m in range(6):
        lhs = mp.fsum(p[n] * qq ** (m * n) for n in range(N))
        rhs_v = (-1) ** m * qq ** (mp.mpf(m * (3 * m + 1)) / 2) * pinv[m] * pinf
        ratio = lhs / rhs_v
        good = abs(ratio / 2 - 1) < mp.mpf("1e-40")
        print(f"D  m={m}: P(q^m) / (4.11.5) = {mp.nstr(ratio, 25)}"
              f"  (D as printed: {abs(ratio - 1) < mp.mpf('1e-40')}; D2 factor 2: {good})")
        d_ok &= good
    slopes = [mp.log(abs(p[n]), 2) / n ** 2 for n in (40, 60, 80)]
    d3 = abs(slopes[-1] + mp.mpf(1) / 6) < mp.mpf("0.02")
    print(f"D3 log2|p_n|/n^2 at n=40,60,80: {[mp.nstr(v, 6) for v in slopes]} (-> -1/6, order 3): {d3}")
    d_ok &= d3

    # E
    c1_inf = newton_slopes([(0, 0), (1, 0), (2, -1)])     # v = -deg_x at infinity
    delta0 = newton_slopes([(0, 0), (1, 1), (2, 3)])      # v = ord_x at 0
    Yx = sp.expand(y_series(14) ** 2)
    degY = [sp.degree(Yx.coeff(x, n), q) for n in range(13)]
    X = sp.Symbol("X")
    c = sp.Integer(1)
    degc = [0]
    for m in range(12):
        c = sp.expand(c * (1 + (X - 1) * X ** m + (X - 1) * X ** (2 * m)))
        degc.append(sp.degree(c, X))
    print(f"E  Newton slopes: C1 at infinity {[str(s) for s in c1_inf]} (one slope); "
          f"DRSZ Delta at 0 {[str(s) for s in delta0]} (two slopes)")
    print(f"E  deg_q Y_n = C(n,2): {degY == [C2(n) for n in range(13)]};"
          f" corpus deg_q c_n = n^2: {degc == [n * n for n in range(13)]}")
    ok = a_ok and b_ok and d_ok
    print("ALL PASS (A, B, D2, D3; D fails by the factor 2, amendment 1)" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
