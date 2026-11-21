#!/usr/bin/env python3
"""expo_xcheck_exact_identities_probe.py — three exact cross-checks from the
expo-cite-xcheck bean drain (issue #8802). Cross-checks only: no external number
is adopted, nothing is wired, and a match corroborates a transcription; it proves
no identity beyond the orders checked.

PRE-REGISTRATION (written before the first run, 2026-11-21)

Check A — bean qou-07m1. Source [arxiv-2302.08363v2] §3 (Complex Chern–Simons
  theory), display after eq. (I2):
      M_1(q) = 1 - 8q - 9q^2 + 18q^3 + 46q^4 + O(q^5)
      M_2(q) = -9q - 3q^2 + 39q^3 + 69q^4 + O(q^5).
  Corpus: computations/probes/fourone_stokes_series_selfcheck.py printed blocks
      g_0  = 1 - q - 2q^2 - 2q^3 - 2q^4 + ...
      2G_0 = 1 - 7q - 14q^2 - 8q^3 - 2q^4 + ...
  Hypothesis H_A: M_1 = g_0 * (2G_0) through q^4.
  PASS iff all five coefficients q^0..q^4 of the product equal (1,-8,-9,18,46)
  in exact integer arithmetic. FAIL otherwise. Also REPORT (no pass/fail)
  M_2/g_0 and M_2/(g_0*2G_0) through q^4.

Check B — bean qou-mmq7. Source [arxiv-hep-ph-0103325v4] §2: with the
  BALANCED q-integer [n]_q = (q^n - q^-n)/(q - q^-1),
      [n]_q - [n-1]_q = Delta_q{T(2,2n-1)}   ([1]_q := 1, [0]_q := 0),
  Delta the symmetrised Alexander polynomial of the (2,2n-1) torus knot,
  Delta_{T(2,m)}(t) = t^{-(m-1)/2} (t^m + 1)/(t + 1).
  Hypothesis H_B: the identity holds as Laurent polynomials for n = 2..16.
  PASS iff equal for every n in 2..16. Also REPORT (no pass/fail) whether it
  holds with the UNBALANCED [n]_q = 1 + q + ... + q^(n-1); expected not (that
  difference is q^(n-1)), which would make the identity convention-dependent.

Check C — bean qou-e1me. Source [takata2004] §2 (Hoste–Shanahan initial data):
      A_{K_-1}(l,m) = -l + l m^2 + m^4 + 2 l m^4 + l^2 m^4 + l m^6 - l m^8.
  Corpus: computations/probes/qbeta_nz_even_series_fourone_probe.py `A_poly`:
      M^4 L^2 - (M^8 - M^6 - 2M^4 - M^2 + 1) L + M^4.
  Hypothesis H_C: identical as integer polynomials under (l,m) = (L,M).
  PASS iff every coefficient agrees. FAIL otherwise.

Check D — bean qou-5rou. Source [lin-wang1999] §5 Example (1) and Remark: for
  M = Sigma(2,3,5) as +1-surgery on the right-handed trefoil, lambda_2(M) = 39;
  under orientation reversal lambda_2(Mbar) = lambda_2(M) + lambda_1(M); and
  lambda_1 = 6 x Casson, so |lambda_1| = 6 here. Corpus: the affine Ohtsuki form
  in computations/probes/keystone_colored_sigma235_wrt.py,
      q(q-1) Z_inf(q) = 1 - (1/2) S_JL(q),  S_JL = sum chi(n) q^((n^2-1)/120),
  chi odd mod 60, +1 on {1,11,19,29}. Expand S_JL at q -> 1 by the standard
  asymptotic sum_n C(n) e^{-n^2 s} ~ sum_k L(-2k,C) (-s)^k / k!, with
  L(-m,C) = -(60^m/(m+1)) sum_a C(a) B_{m+1}(a/60) (exact rationals), q = e^{-t},
  then re-expand in h = q - 1 and read Z_inf = sum lambda_n h^n.
  Hypothesis H_D: (lambda_1, lambda_2) is Lin–Wang's pair for one orientation.
  PASS iff lambda_0 = 1, |lambda_1| = 6, lambda_2 in 3Z, and either lambda_2 = 39
  or lambda_2 + lambda_1 = 39 (the reversed orientation). FAIL otherwise. REPORT
  which orientation the corpus series carries, and lambda_3..lambda_5.
  (Criterion fixed before the first evaluation; Check D was added to this file
  after Checks A–C had run.)

All arithmetic is exact (Python int / Fraction / sympy Rational); no float.
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction


# ---------- truncated power series over Z (lists of int, index = degree) ----------
def ps_mul(a, b, n):
    out = [0] * n
    for i, x in enumerate(a[:n]):
        for j, y in enumerate(b[: n - i]):
            out[i + j] += x * y
    return out


def ps_div(a, b, n):
    """a/b as a power series to order n; b[0] must be +-1 (exact over Z)."""
    assert b[0] in (1, -1)
    out = [Fraction(0)] * n
    for k in range(n):
        s = Fraction(a[k] if k < len(a) else 0)
        for j in range(1, k + 1):
            if j < len(b):
                s -= b[j] * out[k - j]
        out[k] = s / b[0]
    assert all(x.denominator == 1 for x in out)
    return [int(x) for x in out]


def check_a():
    g0 = [1, -1, -2, -2, -2]
    twoG0 = [1, -7, -14, -8, -2]
    M1 = [1, -8, -9, 18, 46]
    M2 = [0, -9, -3, 39, 69]
    prod = ps_mul(g0, twoG0, 5)
    return {
        "product_g0_2G0": prod,
        "M1_source": M1,
        "pass": prod == M1,
        "report_M2_over_g0": ps_div(M2, g0, 5),
        "report_M2_over_g0_2G0": ps_div(M2, prod, 5),
    }


# ---------- Laurent polynomials as {exponent: int} ----------
def lp_add(a, b, s=1):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + s * v
    return {k: v for k, v in out.items() if v}


def qint_balanced(n):
    if n <= 0:
        return {}
    return {e: 1 for e in range(-(n - 1), n, 2)}


def qint_unbalanced(n):
    return {e: 1 for e in range(0, n)}


def alexander_t2(m):
    # t^{-(m-1)/2} (t^m + 1)/(t + 1) = sum_{k=0}^{m-1} (-1)^k t^{k - (m-1)/2}
    h = (m - 1) // 2
    return {k - h: (-1) ** k for k in range(m)}


def check_b():
    rows, ok, unb = [], True, []
    for n in range(2, 17):
        lhs = lp_add(qint_balanced(n), qint_balanced(n - 1), -1)
        rhs = alexander_t2(2 * n - 1)
        good = lhs == rhs
        ok &= good
        lhs_u = lp_add(qint_unbalanced(n), qint_unbalanced(n - 1), -1)
        unb.append({"n": n, "unbalanced_difference": {str(k): v for k, v in sorted(lhs_u.items())},
                    "equals_alexander": lhs_u == rhs})
        rows.append({"n": n, "pass": good})
    return {"pass": ok, "rows": rows, "report_unbalanced": unb}


def check_c():
    # keys (deg_l, deg_m)
    takata = {(1, 0): -1, (1, 2): 1, (0, 4): 1, (1, 4): 2, (2, 4): 1, (1, 6): 1, (1, 8): -1}
    corpus = {(2, 4): 1, (0, 4): 1}
    for (dm, c) in [(8, 1), (6, -1), (4, -2), (2, -1), (0, 1)]:
        corpus[(1, dm)] = corpus.get((1, dm), 0) - c
    corpus = {k: v for k, v in corpus.items() if v}
    return {"takata": {str(k): v for k, v in sorted(takata.items())},
            "corpus": {str(k): v for k, v in sorted(corpus.items())},
            "pass": takata == corpus}


def check_d(order=6):
    import sympy as sp
    N, pos = 60, {1, 11, 19, 29}

    def chi(n):
        n %= N
        return 1 if n in pos else (-1 if (N - n) % N in pos else 0)

    def l_neg(m):
        return -sp.Rational(N ** m, m + 1) * sum(
            chi(a) * sp.bernoulli(m + 1, sp.Rational(a, N)) for a in range(1, N + 1))

    t, h = sp.symbols("t h")
    K = order + 2
    inner = sum(l_neg(2 * k) * (-t / 120) ** k / sp.factorial(k) for k in range(K))
    S = sp.series(sp.exp(t / 120) * inner, t, 0, K).removeO()
    aff = sp.series((1 - S / 2).subs(t, -sp.log(1 + h)), h, 0, K).removeO()
    Z = sp.series(aff / (h * (1 + h)), h, 0, order).removeO()
    lam = [sp.Rational(c) for c in sp.Poly(sp.expand(Z), h).all_coeffs()[::-1]]
    l0, l1, l2 = lam[0], lam[1], lam[2]
    ok = (l0 == 1 and abs(l1) == 6 and l2 % 3 == 0 and (l2 == 39 or l2 + l1 == 39))
    orient = ("Lin-Wang M (+1 surgery on right-handed trefoil)" if l2 == 39
              else "orientation-reversed Mbar (lambda_2 + lambda_1 = 39)" if l2 + l1 == 39
              else "neither")
    return {"lambda": [str(x) for x in lam], "pass": bool(ok), "report_orientation": orient,
            "report_all_integer": all(x.q == 1 for x in lam)}


def main() -> int:
    res = {"A_qou-07m1": check_a(), "B_qou-mmq7": check_b(), "C_qou-e1me": check_c(),
           "D_qou-5rou": check_d()}
    print(json.dumps(res, indent=1))
    ok = all(v["pass"] for v in res.values())
    print("ALL PRE-REGISTERED CHECKS PASS" if ok else "A PRE-REGISTERED CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
