#!/usr/bin/env python3
"""cyclotomic_boundary_power_sum.py — the power-sum test for conj:cyclotomic-boundary-at-keystone.

If P = c * X^j * prod Phi_k has degree d and top coefficients c, a1, a2, then over C its roots
are 0 or roots of unity, so the root power sums s1 = -a1/c and s2 = (a1^2 - 2 c a2)/c^2 are
integers with |s2| <= d (Lean: QOU.Mass.CyclotomicPowerSum.abs_powerSum_two_le and
leadingCoeff_dvd_coeff).  This script computes c, a1, a2, d of the cleared tail P_n for every n
in a range and reports which test fails.

Top coefficients without the full polynomial.  dim_q(lam) = q^{-e} g(q^2) is bar-even with top
exponent e = C(n,2) - N(lam), N(lam) = sum over cells of (row + col).  So the coefficient of
q^{E-k} in S(n), E = C(n,2) - Nmin, is the sum over lam with delta = N(lam) - Nmin <= k,
delta = k mod 2, of the ((k - delta)/2)-th coefficient of g_lam; the first two coefficients of
g_lam are 1 and (#corners - 1).  For n >= 10 the terms S(n-1) and [n-1] S(n-2) of D(n) start at
least 3 below the top, so
    c = #{delta = 0},  a1 = #{delta = 1},  a2 = sum_{delta=0} (corners - 1) + #{delta = 2}.
The script checks this against the exact tails of cyclotomic_boundary_certificates.py for
10 <= n <= N_EXACT before using it.

Exact integer / Fraction arithmetic; no floats, no fitting.
Usage: python3 computations/cyclotomic_boundary_power_sum.py [N] (default 90)
Writes computations/cyclotomic-boundary-power-sum.witness.json.
"""
from __future__ import annotations
import json
import sys
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import cyclotomic_boundary_certificates as exact  # noqa: E402

N_EXACT = 22


def _lower_bound(m, i, width):
    """Least possible sum of (row + col) over m cells in rows >= i, cols < width."""
    tot, v = 0, i
    while m > 0:
        t = min(width, v - i + 1, m)
        tot, m, v = tot + t * v, m - t, v + 1
    return tot


def near_minimal(n, slack):
    nmin = _lower_bound(n, 0, n)
    out = []

    def dfs(rows, m, cur):
        i = len(rows)
        width = rows[-1] if rows else m
        if m == 0:
            out.append((tuple(rows), cur - nmin))
            return
        if cur + _lower_bound(m, i, min(width, m)) > nmin + slack:
            return
        for r in range(min(width, m), 0, -1):
            dfs(rows + [r], m - r, cur + i * r + r * (r - 1) // 2)

    dfs([], n, 0)
    return nmin, out


def corners(lam):
    return sum(1 for i, r in enumerate(lam) if i + 1 == len(lam) or lam[i + 1] < r)


def top_coeffs(n):
    nmin, ps = near_minimal(n, 2)
    c = sum(1 for _, d in ps if d == 0)
    a1 = sum(1 for _, d in ps if d == 1)
    a2 = sum(corners(l) - 1 for l, d in ps if d == 0) + sum(1 for _, d in ps if d == 2)
    return c, a1, a2, 2 * (n * (n - 1) // 2 - nmin)


def verdict(c, a1, a2, d):
    s1 = Fraction(-a1, c)
    s2 = Fraction(a1 * a1 - 2 * c * a2, c * c)
    if s1.denominator != 1:
        return "lead does not divide a1", s1, s2
    if s2.denominator != 1:
        return "s2 not an integer", s1, s2
    if abs(s2) > d:
        return "|s2| > deg", s1, s2
    return None, s1, s2


def main() -> int:
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 90
    for n in range(10, N_EXACT + 1):
        m, P = exact.tail(n)
        P = P[::-1]
        assert (P[0], P[1], P[2], len(P) - 1) == top_coeffs(n), n
    rows, open_n = {}, []
    for n in range(10, N + 1):
        c, a1, a2, d = top_coeffs(n)
        why, s1, s2 = verdict(c, a1, a2, d)
        rows[n] = {"lead": c, "a1": a1, "a2": a2, "deg": d, "s1": str(s1), "s2": str(s2),
                   "fails": why}
        if why is None:
            open_n.append(n)
        print(f"n={n}: lead {c}, s1 {s1}, s2 {s2}, deg {d}: {why}", flush=True)
    out = {"description": "Power-sum test on the cleared tail P_n of D(n); see module docstring.",
           "checked_against_exact_tails": [10, N_EXACT], "range": [10, N],
           "not_settled_by_test": open_n, "rows": rows}
    path = Path(__file__).with_name("cyclotomic-boundary-power-sum.witness.json")
    path.write_text(json.dumps(out, indent=1) + "\n")
    print("not settled by the test:", open_n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
