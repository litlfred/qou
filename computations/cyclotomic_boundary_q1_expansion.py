#!/usr/bin/env python3
"""cyclotomic_boundary_q1_expansion.py — the q = 1 expansion of D(n), for the cumulant test of
conj:cyclotomic-boundary-at-keystone.

Put q = e^t.  S(n) and [n-1]_q are even in t, so D(n) = d2 t^2 + d4 t^4 + O(t^6), and for the
cleared tail P = q^m D(n)/(q-1)^2 one gets P(1) = d2 and 12 kappa_2(P) = 24 d4/d2 - 2.  So the
cumulant-integrality test (cyclotomic_boundary_cumulant_integrality.py) holds iff d2 | 24 d4.

Derivation (each step re-checked below in exact arithmetic):
  1. log [k] = log k + (k^2-1) t^2/6 - (k^4-1) t^4/180 + O(t^6).
  2. Hook power sums in contents c(u) = col - row:
       sum h^2 = sum c^2 + n^2                       (classical),
       sum h^4 = sum c^4 + 12 n sum c^2 + n^2 - 12 (sum c)^2   (all lam; see the proof checks).
  3. A content power sum is the central character of a Jucys-Murphy power sum, and
     sum_lam f^lam omega_lam(z) = sum_g z_g r(g), r(g) = #{x : x^2 = g}.  The class expansions of
     sum J_i^2, sum J_i^4, (sum J_i)^2, (sum J_i^2)^2 used are in CLASS_SUMS (checked against
     partition sums for n <= 13 here; derived for all n from Jucys-Murphy products in
     cyclotomic_boundary_q1_proof_checks.py).
  4. This gives d2 and d4 as polynomial combinations of x = I_{n-8}, y = I_{n-9} (involution
     numbers):
       6 d2    = c (n-6)(n^2-13) x + 2 c (n-8)(n-5)(2n-5) y,          c = (n-1)(n-2)(n-3),
       1080 d4 = c (n-6) Q5(n) x + 2 c (n-8)(n-5) Q4(n) y,
     Q5 = 10n^5 - 51n^4 - 86n^3 + 774n^2 - 536n - 1695,  Q4 = 20n^4 - 157n^3 + 419n^2 - 333n - 219.
  5. If d2 | 24 d4 then d2 | Delta(n) x and d2 | Delta(n) y with
       Delta = a*e - b*cc = -2 (n-8)(n-7)(n-6)(n-5)(n-4) c^2 (5n^3 - 21n^2 - 101n + 201), and
     gcd(I_m, I_{m-1}) is a power of 2 (I_{m+p} = I_m mod p for odd p, and (I_0, I_1) = (1, 1)),
     so odd(d2) | Delta(n).

  6. 2-adic step.  v(m) = v_2(I_m) = floor(m/4) + (0, 0, 1, 2)[m mod 4] for all m
     (Lean: QOU.Mass.InvolutionTwoAdic, sorry-free; re-checked here for m <= 3009),
     so in 6 d2 = c (A x + B y) the two terms never
     have equal 2-adic valuation (case split on n mod 4), so v_2(d2) <= v_2(c) + (n+1)/4.  Then
     odd(d2) grows like I_{n-8} / 2^{n/4} and exceeds |Delta| for large n, and the test excludes
     every n >= 9.

Status: steps 2 and 3 hold for all n as polynomial identities
(cyclotomic_boundary_q1_proof_checks.py); 1 is classical; 5 and 6 are proved.  The ranges
checked here are a cross-check.

Exact integer / Fraction arithmetic; no floats, no fitting.
Usage: python3 computations/cyclotomic_boundary_q1_expansion.py [N]   (default N = 3000)
Writes computations/cyclotomic-boundary-q1-expansion.witness.json.
"""
from __future__ import annotations
import json
import math
import sys
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cyclotomic_boundary_certificates as exact  # noqa: E402
import cyclotomic_boundary_cumulant_integrality as cum  # noqa: E402


def ff(n, s):
    r = 1
    for i in range(s):
        r *= n - i
    return r


# total weight of each class, as a function of n: {cycle type: f(n)}; r-count = (factor, support)
CLASS_SUMS = {
    "p2": {(): lambda n: F(n * (n - 1), 2), (3,): lambda n: F(ff(n, 3), 3)},
    "p1sq": {(): lambda n: F(n * (n - 1), 2), (3,): lambda n: F(ff(n, 3)),
             (2, 2): lambda n: F(ff(n, 4), 4)},
    "p4": {(): lambda n: F(n * (n - 1) * (4 * n - 5), 6), (3,): lambda n: F(ff(n, 3) * (3 * n - 4), 3),
           (2, 2): lambda n: F(ff(n, 4), 2), (5,): lambda n: F(ff(n, 5), 5)},
    "p2sq": {(): lambda n: F(n * (n - 1) * (3 * n * n + n - 8), 12),
             (3,): lambda n: F(ff(n, 3) * (n - 2) * (n + 4), 3), (2, 2): lambda n: F(ff(n, 4)),
             (5,): lambda n: F(ff(n, 5)), (3, 3): lambda n: F(ff(n, 6), 9)},
}
ROOTS = {(): (1, 0), (3,): (1, 3), (2, 2): (2, 4), (5,): (1, 5), (3, 3): (4, 6)}

_I = [1, 1]


def I(m):
    if m < 0:
        return 0
    while len(_I) <= m:
        k = len(_I)
        _I.append(_I[-1] + (k - 1) * _I[-2])
    return _I[m]


def M(key, n):
    if n < 0:
        return 0
    if key == "1":
        return F(I(n))
    return sum(w(n) * ROOTS[t][0] * I(n - ROOTS[t][1]) for t, w in CLASS_SUMS[key].items())


def T(k, n):
    return sum(i ** k for i in range(1, n + 1))


def s2(n):
    return F(T(2, n) - n * n, 6) * M("1", n) - M("p2", n) / 6 if n >= 0 else 0


def s4(n):
    if n < 0:
        return 0
    A = F(T(2, n) - n * n)
    return (-(F(T(4, n) - n * n) * M("1", n) - M("p4", n) - 12 * n * M("p2", n) + 12 * M("p1sq", n)) / 180
            + (A * A * M("1", n) - 2 * A * M("p2", n) + M("p2sq", n)) / 72)


def D_series(n):
    k = n - 1
    k2, k4 = F(k * (k * k - 1), 6), F(k * (k * k - 1) * (3 * k * k - 7), 360)
    d2 = s2(n) - s2(n - 1) - (k * s2(n - 2) + k2 * M("1", n - 2))
    d4 = s4(n) - s4(n - 1) - (k * s4(n - 2) + k2 * s2(n - 2) + k4 * M("1", n - 2))
    return d2, d4


def closed(n):
    x, y, c = I(n - 8), I(n - 9), (n - 1) * (n - 2) * (n - 3)
    a, b = c * (n - 6) * (n * n - 13), 2 * c * (n - 8) * (n - 5) * (2 * n - 5)
    cc = c * (n - 6) * (10 * n**5 - 51 * n**4 - 86 * n**3 + 774 * n**2 - 536 * n - 1695)
    e = 2 * c * (n - 8) * (n - 5) * (20 * n**4 - 157 * n**3 + 419 * n**2 - 333 * n - 219)
    return F(a * x + b * y, 6), F(cc * x + e * y, 1080), a * e - b * cc


def delta_poly(n):
    return -2 * (n - 8) * (n - 7) * (n - 6) * (n - 5) * (n - 4) * ((n - 3) * (n - 2) * (n - 1)) ** 2 * (
        5 * n**3 - 21 * n**2 - 101 * n + 201)


def odd(a):
    a = abs(a)
    while a and a % 2 == 0:
        a //= 2
    return a


def v2(a):
    a, k = abs(a), 0
    while a % 2 == 0:
        a, k = a // 2, k + 1
    return k


def checks():
    for m in range(0, 3010):
        assert v2(I(m)) == m // 4 + (0, 0, 1, 2)[m % 4], m
    # hook identities
    for n in range(1, 17):
        for lam in exact.partitions(n):
            h = exact.hooks(lam)
            c = [j - i for i, r in enumerate(lam) for j in range(r)]
            p1, p2, p4 = sum(c), sum(v * v for v in c), sum(v**4 for v in c)
            assert sum(v * v for v in h) == p2 + n * n
            assert sum(v**4 for v in h) == p4 + 12 * n * p2 + n * n - 12 * p1 * p1
    # class sums vs partition sums
    for n in range(1, 14):
        tot = defaultdict(int)
        for lam in exact.partitions(n):
            h = exact.hooks(lam)
            f = math.factorial(n) // math.prod(h)
            c = [j - i for i, r in enumerate(lam) for j in range(r)]
            p1, p2, p4 = sum(c), sum(v * v for v in c), sum(v**4 for v in c)
            tot["p2"] += f * p2; tot["p1sq"] += f * p1 * p1
            tot["p4"] += f * p4; tot["p2sq"] += f * p2 * p2
        for key in CLASS_SUMS:
            assert M(key, n) == tot[key], (key, n)
    # series vs exact D(n), and closed form vs series
    for n in range(4, 25):
        _, P = exact.tail(n)
        P, k = cum.strip_q_minus_one(P)
        assert k == 2
        kap = cum.cumulants(P, 2)
        d2, d4 = D_series(n)
        assert d2 == sum(P) and 24 * d4 / d2 - 2 == 12 * kap[2], n
        if n >= 9:
            c2, c4, dl = closed(n)
            assert (c2, c4) == (d2, d4) and dl == delta_poly(n), n


def main() -> int:
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    checks()
    passes, odd_divides, last_small = [], [], 8
    for n in range(9, N + 1):
        d2, d4, dl = closed(n)
        assert d2.denominator == 1
        if (24 * d4 / d2).denominator == 1:
            passes.append(n)
        o = odd(d2.numerator)
        if dl % o == 0:
            odd_divides.append(n)
        if o <= abs(dl):
            last_small = n
        x, y, c = I(n - 8), I(n - 9), (n - 1) * (n - 2) * (n - 3)
        A, B = (n - 6) * (n * n - 13), 2 * (n - 8) * (n - 5) * (2 * n - 5)
        assert v2(A) + v2(x) != v2(B) + v2(y), n
        assert v2(d2.numerator) <= v2(c) + (n + 1) // 4, n
    print(f"9 <= n <= {N}: cumulant test passes at {passes}")
    print(f"odd(d2) | Delta at {odd_divides}; odd(d2) > |Delta| for all {last_small + 1} <= n <= {N}")
    path = Path(__file__).with_name("cyclotomic-boundary-q1-expansion.witness.json")
    path.write_text(json.dumps({
        "producer": Path(__file__).name,
        "block": "conj:cyclotomic-boundary-at-keystone",
        "range": [9, N],
        "cumulant_test_passes": passes,
        "odd_d2_divides_delta": odd_divides,
        "odd_d2_exceeds_delta_from": last_small + 1,
        "status": "closed forms checked against exact D(n) for n <= 24; proved for all n in cyclotomic_boundary_q1_proof_checks.py"},
        indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
