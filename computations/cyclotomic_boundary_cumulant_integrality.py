#!/usr/bin/env python3
"""cyclotomic_boundary_cumulant_integrality.py — cumulant integrality test for
conj:cyclotomic-boundary-at-keystone.

Test.  Read a polynomial P with P(1) != 0 as a signed weight on exponents i -> coeff_i / P(1)
and take its formal cumulants kappa_d (raw moments m_d = sum_i coeff_i i^d / P(1), then the
moment-cumulant recursion).  Cumulants add under multiplication of polynomials, a monomial
c X^j shifts only kappa_1, and for a cyclotomic polynomial Phi_m (m >= 2)
    kappa_{2d}(Phi_m) = (B_{2d} / 2d) J_{2d}(m)          (J = Jordan totient)
(Billey-Swanson, "Cyclotomic Generating Functions", arXiv:2305.07620v3,
Cor. 43).  With B_2 = 1/6, B_4 = -1/30, B_6 = 1/42, B_8 = -1/30, any
P = c X^j prod Phi_{m_k} (all m_k >= 2) therefore has
    12 kappa_2 = sum J_2(m_k),    120 kappa_4 = -sum J_4,
    252 kappa_6 = sum J_6,        240 kappa_8 = -sum J_8,
all integers.  A non-integral value proves P is not of that form.

Applied to D(n) = S(n) - S(n-1) - [n-1]_q S(n-2) after clearing q^m and stripping every factor
(q - 1).  Exact integer / Fraction arithmetic; no floats, no fitting.  The test is a necessary
condition only; it does not decide n beyond the range scanned.

Usage: python3 computations/cyclotomic_boundary_cumulant_integrality.py [N]   (default N = 24)
Writes computations/cyclotomic-boundary-cumulant-integrality.witness.json.
"""
from __future__ import annotations
import json
import sys
from fractions import Fraction
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cyclotomic_boundary_certificates as exact  # noqa: E402

SCALE = {2: 12, 4: 120, 6: 252, 8: 240}


def strip_q_minus_one(P):
    """Divide by (q - 1) while P(1) = 0; return quotient and multiplicity."""
    k = 0
    while sum(P) == 0:
        Q, acc = [0] * (len(P) - 1), 0
        for i in range(len(P) - 1, 0, -1):
            acc += P[i]
            Q[i - 1] = acc
        assert acc + P[0] == 0
        P, k = Q, k + 1
    return P, k


def cumulants(P, D):
    tot = sum(P)
    m = [Fraction(sum(c * i ** d for i, c in enumerate(P)), tot) for d in range(D + 1)]
    k = [Fraction(0)] * (D + 1)
    for n in range(1, D + 1):
        k[n] = m[n] - sum(comb(n - 1, j - 1) * k[j] * m[n - j] for j in range(1, n))
    return k


def jordan(d, m):
    r = Fraction(m ** d)
    x, f = m, 2
    while f * f <= x:
        if x % f == 0:
            while x % f == 0:
                x //= f
            r *= 1 - Fraction(1, f ** d)
        f += 1
    if x > 1:
        r *= 1 - Fraction(1, x ** d)
    return int(r)


def self_check():
    """The test must accept products of cyclotomics with the predicted values."""
    def phi(m):  # cyclotomic polynomial by exact division of X^m - 1
        P = [-1] + [0] * (m - 1) + [1]
        for d in range(1, m):
            if m % d == 0:
                P = exact.pdiv_exact(P, phi(d))
        return P
    for ms in ([2, 3], [4, 6, 6], [5, 7, 12]):
        P = [3]
        for m in ms:
            P = exact.pmul(P, phi(m))
        k = cumulants(P, 8)
        for d, s in SCALE.items():
            sign = 1 if d % 4 == 2 else -1
            assert s * k[d] == sign * sum(jordan(d, m) for m in ms), (ms, d)


def main() -> int:
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
    self_check()
    out = {}
    for n in range(4, N + 1):
        t = exact.tail(n)
        if t is None:
            out[n] = {"D": 0}
            continue
        _, P = t
        P, k1 = strip_q_minus_one(P)
        k = cumulants(P, 8)
        vals = {f"{s}k{d}": s * k[d] for d, s in SCALE.items()}
        bad = [x for x, v in vals.items() if v.denominator != 1]
        out[n] = {
            "q_minus_1_multiplicity": k1,
            "P1_after_strip": sum(P),
            "scaled_cumulants": {x: str(v) for x, v in vals.items()},
            "non_integral": bad,
            "excluded_by_test": bool(bad),
        }
        print(f"n={n}: (q-1)^{k1}, " + ("passes" if not bad else "FAILS " + ",".join(bad))
              + f"  12k2={vals['12k2']}")
    path = Path(__file__).with_name("cyclotomic-boundary-cumulant-integrality.witness.json")
    path.write_text(json.dumps({
        "producer": Path(__file__).name,
        "block": "conj:cyclotomic-boundary-at-keystone",
        "source": "Billey-Swanson arXiv:2305.07620 Cor. 43",
        "results": out}, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
