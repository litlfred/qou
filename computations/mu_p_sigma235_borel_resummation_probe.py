#!/usr/bin/env python3
"""mu_p_sigma235_borel_resummation_probe.py — Borel resummation of the
Sigma(2,3,5) Ohtsuki series at the substrate pin, and what scales it produces.

BEAN `qou-6gf9`, option 2 of the mu-p residual front (resummation). Follows
`mu_p_sigma235_ohtsuki_resolution_probe.py`, whose SCOPE section left exactly
this open: "a resummation (Borel, median, Ecalle-Borel) of the same series".
Lean scaffold: `QOU/BraidsAndKnots/PoincareSphereBorelSectors.lean`.

## Mathematics (no measured input until the COMPARISON block)

Source: `library/arxiv-2605.15740v1` (lovejoy2026), eq. (LZ0)/(LZ):

    1 + q(1-q) I(Sigma(2,3,5); q) = H(q)   at roots of unity,
    H = -(1/2) q^{-1/120} Phi~ ,  Phi~ = sum chi(n) q^{n^2/120}.

With the sign convention of this file, A(q) = sum_{n>=1} chi+(n) q^{(n^2-1)/120},
chi+ = +1 on n = 1,11,19,29 and -1 on n = 31,41,49,59 (mod 60), H = A/2.

RESULT 1 (exact). The q -> 1 expansion of (A/2 - 1)/(q(1-q)) reproduces the
Ohtsuki integers 1, -6, 45, -464, ... exactly (checked through order N_CHECK)
from Bernoulli-polynomial L-values L(-2k, chi+), independently of the
Pochhammer expansion in the sibling probe.

RESULT 2 (closed form, exact up to the j-sum). With q = e^{-t},
f(t) = sum chi+(n) e^{-n^2 t/120} ~ sum a_k t^k, and

    a_k = (1/pi) sum_{j>=1} (s(j)/j) (2k)!/k! (30/(4 pi^2 j^2))^k,
    s(j) = sum_{a=1}^{60} chi+(a) sin(2 pi j a/60),

so the Borel transform is B(xi) = (1/pi) sum_j (s(j)/j)(1 - 30 xi/(pi^2 j^2))^{-1/2}.
Singularities: xi_j = pi^2 j^2/30 on the POSITIVE axis, j in the dual support
(j^2 = 1 or 49 mod 120). Hence:

* q0 > 1  (t0 < 0): the series is alternating and BOREL SUMMABLE; the sum is
  unique, there is no Stokes ambiguity and median = lateral = Borel sum:
      S(t0) = (1/pi) sum_j (s(j)/j) sqrt(pi c_j) e^{c_j} erfc(sqrt c_j),
      c_j = pi^2 j^2 / (30 |t0|).
* bar image 1/q0 < 1 (t > 0): the positive axis is a Stokes line; lateral sums
  differ by i * sum_j (s(j)/j) (...) and the MEDIAN reproduces the convergent
  false theta f(t) (checked to the working precision).
* trans-series sector sizes at the pin are exp(-c_1 j^2): j = 1 then j = 7
  (Lean: `dualSupport_action_gap`, no j^2 strictly between 1 and 49).

Cross-check: Borel-Pade from the exact a_k reproduces S(t0).

COMPARISON (the only place the measured residual enters). The residual
t_res = 211 ppb (live tension witness) is set beside the a-priori scales the
resummation produces. Nothing is selected or tuned: every row is fixed before
t_res is read. Scope-(a): this says which numbers THIS resummation of THIS
series produces at q0; it does not exclude other uses of Sigma(2,3,5).
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()

PERIOD = 60
N_CHECK = 12      # Ohtsuki coefficients checked exactly
K_SUB = 4         # asymptotic terms subtracted in the j-sum (tail ~ j^-(2K+1))
J_MAX = 20000     # j-sum cutoff
PADE_ORDER = 22   # [m/m] Pade of the Borel transform
OHTSUKI = [1, -6, 45, -464, 6224, -102816, 2015237, -45679349, 1175123730,
           -33819053477, 1076447743008, -37544249290614]

_TENSION = (
    Path(__file__).resolve().parent / "mu-substrate-tension-audit-100dps.witness.json"
)


def chi(n: int) -> int:
    r = n % PERIOD
    if r in (1, 11, 19, 29):
        return 1
    if r in (31, 41, 49, 59):
        return -1
    return 0


# ---------- exact Bernoulli machinery (Fractions) ----------
def bernoulli_numbers(m: int) -> list[F]:
    B = [F(0)] * (m + 1)
    B[0] = F(1)
    for n in range(1, m + 1):
        B[n] = -sum(comb(n + 1, k) * B[k] for k in range(n)) / F(n + 1)
    return B


def L_neg(m: int, B: list[F]) -> F:
    """L(-m, chi) = -(N^m/(m+1)) sum_a chi(a) B_{m+1}(a/N), exact."""
    tot = F(0)
    for a in range(1, PERIOD + 1):
        c = chi(a)
        if not c:
            continue
        x = F(a, PERIOD)
        poly = sum(comb(m + 1, i) * B[i] * x ** (m + 1 - i) for i in range(m + 2))
        tot += c * poly
    return -F(PERIOD ** m, m + 1) * tot


def a_exact(kmax: int) -> list[F]:
    B = bernoulli_numbers(2 * kmax + 2)
    return [L_neg(2 * k, B) * F(-1, 120) ** k / factorial(k) for k in range(kmax)]


def series_mul(a, b, n):
    out = [F(0)] * n
    for i, ai in enumerate(a[:n]):
        if ai:
            for j, bj in enumerate(b[: n - i]):
                out[i + j] += ai * bj
    return out


def ohtsuki_from_false_theta(n: int) -> list[F]:
    """Coefficients in x = q-1 of (A/2 - 1)/(q(1-q)), A = e^{t/120} f(t), t = -log(1+x)."""
    m = n + 2
    a = a_exact(m)
    # t = -log(1+x) = sum_{i>=1} (-1)^i x^i / i
    tx = [F(0)] + [F((-1) ** i, i) for i in range(1, m)]
    # powers of t
    pw = [[F(1)] + [F(0)] * (m - 1)]
    for _ in range(1, m):
        pw.append(series_mul(pw[-1], tx, m))
    # e^{t/120}
    e = [F(0)] * m
    for k in range(m):
        ck = F(1, 120 ** k * factorial(k))
        e = [e[i] + ck * pw[k][i] for i in range(m)]
    f = [F(0)] * m
    for k in range(m):
        f = [f[i] + a[k] * pw[k][i] for i in range(m)]
    A = series_mul(e, f, m)
    num = [A[i] / 2 for i in range(m)]
    num[0] -= 1
    assert num[0] == 0
    # divide by q(1-q) = -x(1+x): shift by one, negate, divide by (1+x)
    g = [-num[i + 1] for i in range(m - 1)]
    inv = [F((-1) ** i) for i in range(m - 1)]
    return series_mul(g, inv, n)


# ---------- Borel sums ----------
def s_hat() -> dict[int, mp.mpf]:
    return {j: mp.fsum(chi(a) * mp.sin(2 * mp.pi * j * a / PERIOD)
                       for a in range(1, PERIOD + 1))
            for j in range(1, PERIOD + 1)}


def _asym(c, sign):
    return mp.fsum((sign ** k) * mp.fac2(2 * k - 1) / (2 * c) ** k for k in range(K_SUB))


def borel_sum_negative_t(t, a, s):
    """Unique Borel sum of sum a_k t^k for t < 0."""
    T = -t
    tail = mp.fsum(
        s[(j - 1) % PERIOD + 1] / j * (
            mp.sqrt(mp.pi * c) * mp.exp(c) * mp.erfc(mp.sqrt(c)) - _asym(c, -1))
        for j in range(1, J_MAX + 1) if s[(j - 1) % PERIOD + 1]
        for c in [mp.pi ** 2 * j * j / (30 * T)])
    return mp.fsum(a[k] * t ** k for k in range(K_SUB)) + tail / mp.pi


def median_sum_positive_t(t, a, s):
    """Median (real part of lateral) Borel sum for t > 0."""
    tail = mp.fsum(
        s[(j - 1) % PERIOD + 1] / j * (
            mp.sqrt(mp.pi * c) * mp.exp(-c) * mp.erfi(mp.sqrt(c)) - _asym(c, 1))
        for j in range(1, J_MAX + 1) if s[(j - 1) % PERIOD + 1]
        for c in [mp.pi ** 2 * j * j / (30 * t)])
    return mp.fsum(a[k] * t ** k for k in range(K_SUB)) + tail / mp.pi


def stokes_jump(t, s, j):
    """|Im| of a lateral sum from sector j at t > 0: (s(j)/(pi j)) sqrt(pi c) e^{-c}."""
    c = mp.pi ** 2 * j * j / (30 * t)
    return abs(s[(j - 1) % PERIOD + 1]) / (mp.pi * j) * mp.sqrt(mp.pi * c) * mp.exp(-c)


def live_residual() -> mp.mpf:
    with _TENSION.open() as fh:
        w = json.load(fh)
    return mp.mpf(str(w["data"]["residual_ppb_at_canonical_q0"])) / mp.mpf(10) ** 9


def main() -> int:
    q0 = q_at()
    x0 = q0 - 1
    t0 = -mp.log(q0)

    # RESULT 1
    lam = ohtsuki_from_false_theta(N_CHECK)
    match = all(lam[i] == OHTSUKI[i] for i in range(N_CHECK))

    # RESULT 2
    a = [mp.mpf(v.numerator) / v.denominator for v in a_exact(2 * PADE_ORDER + 1)]
    s = s_hat()
    support = sorted(j for j in s if abs(s[j]) > mp.mpf(10) ** (-mp.mp.dps // 2))
    S0 = borel_sum_negative_t(t0, a, s)
    A0 = mp.exp(t0 / 120) * S0
    I_B = (A0 / 2 - 1) / (q0 * (1 - q0))

    b = [a[k] / mp.factorial(k) for k in range(2 * PADE_ORDER + 1)]
    P, Q = mp.pade(b, PADE_ORDER, PADE_ORDER)
    Bf = lambda xi: mp.polyval(P[::-1], xi) / mp.polyval(Q[::-1], xi)  # noqa: E731
    S_pade = mp.quad(lambda u: mp.exp(-u) * Bf(t0 * u), [0, 5, 20, 60, mp.inf])

    tb = -t0
    f_conv = mp.fsum(chi(n) * mp.exp(-n * n * tb / 120) for n in range(1, 6000))
    f_med = median_sum_positive_t(tb, a, s)

    partial = [mp.fsum(OHTSUKI[i] * x0 ** i for i in range(n + 1)) for n in range(6)]
    least = min(abs(OHTSUKI[i] * x0 ** i) for i in range(8))
    c1 = mp.pi ** 2 / (30 * abs(t0))
    sectors = {j: mp.exp(-c1 * j * j) for j in (1, 7, 11, 13)}
    jump1 = stokes_jump(tb, s, 1)

    # ---------------- COMPARISON (measured residual enters only here) ----------
    t_res = live_residual()
    rows = [
        ("Borel sum I_B(q0)", abs(I_B)),
        ("|I_B - optimal truncation (n=2)|", abs(I_B - partial[2])),
        ("least term (sibling probe floor)", least),
        ("sector j=1: exp(-c1)", sectors[1]),
        ("Stokes jump at 1/q0, j=1", jump1),
        ("sector j=7: exp(-49 c1)", sectors[7]),
    ]
    gap_lo, gap_hi = sectors[7], sectors[1]

    print("=" * 78)
    print(" Sigma(2,3,5): Borel resummation of the Ohtsuki series at the substrate pin")
    print("=" * 78)
    print(f"  q0 = {mp.nstr(q0, 18)}  t0 = -log q0 = {mp.nstr(t0, 15)}")
    print(f"  RESULT 1  Ohtsuki from false theta, orders 0..{N_CHECK-1}: "
          f"{'EXACT MATCH' if match else 'MISMATCH'}")
    print(f"  dual support j mod 60: {support}")
    print(f"  RESULT 2  Borel sum S(t0) = {mp.nstr(S0, 30)}")
    print(f"            Borel-Pade [{PADE_ORDER}/{PADE_ORDER}] diff = {mp.nstr(S_pade - S0, 5)}")
    print(f"            I_B(q0) = {mp.nstr(I_B, 30)}")
    print(f"            partial sums: {[mp.nstr(p, 8) for p in partial]}")
    print(f"            bar side: f_conv - median = {mp.nstr(f_conv - f_med, 5)}")
    print(f"            c1 = {mp.nstr(c1, 15)}; sectors: "
          + ", ".join(f"j={j}: {mp.nstr(v, 6)}" for j, v in sectors.items()))
    print(f"  COMPARISON  t_res = {mp.nstr(t_res, 10)}")
    for name, v in rows:
        print(f"    {name:38s} {mp.nstr(v, 8):>14s}   / t_res = {mp.nstr(v / t_res, 6)}")
    print(f"    no sector lies in ({mp.nstr(gap_lo, 3)}, {mp.nstr(gap_hi, 3)}), "
          f"which contains t_res: {gap_lo < t_res < gap_hi}")

    wb = WitnessBuilder("mu-p-sigma235-borel-resummation", engine="python")
    wb.add_data("pin", {"q0": fmt(q0), "x0": fmt(x0), "t0": fmt(t0)})
    wb.add_data("ohtsuki_from_false_theta", [str(v) for v in lam])
    wb.add_data("dual_support_mod_60", support)
    wb.add_data("borel", {
        "S_t0": fmt(S0), "S_pade_minus_closed": fmt(S_pade - S0),
        "I_borel_q0": fmt(I_B), "partial_sums": [fmt(p) for p in partial],
        "c1": fmt(c1), "sectors": {str(j): fmt(v) for j, v in sectors.items()},
        "bar_side_fconv_minus_median": fmt(f_conv - f_med),
        "stokes_jump_j1_at_inverse_q0": fmt(jump1),
        "j_max": J_MAX, "k_subtracted": K_SUB,
    })
    wb.add_data("comparison", {
        "t_res": fmt(t_res),
        "rows": [{"quantity": n, "value": fmt(v), "over_t_res": fmt(v / t_res)}
                 for n, v in rows],
        "scope": "(a): this resummation of this series at q0; selection-free",
    })
    wb.add_data("source", {
        "series": "I(Sigma(2,3,5);q) = (1-q)^-1 sum q^n (q^{n+1})_{n+1}",
        "relation": "1 + q(1-q) I = H = A/2, A = sum chi+(n) q^{(n^2-1)/120} (lovejoy2026 LZ0)",
        "lean": "QOU/BraidsAndKnots/PoincareSphereBorelSectors.lean",
    })
    tiny = mp.mpf(10) ** (-20)
    wb.add_assertion("ohtsuki_series_equals_false_theta_expansion",
                     computed=str(int(match)), expected="1", tolerance=0,
                     source=f"exact Fraction match of orders 0..{N_CHECK-1}")
    wb.add_assertion("borel_pade_agrees_with_closed_form",
                     computed=str(int(abs(S_pade - S0) < tiny)), expected="1", tolerance=0,
                     source="independent Pade-Laplace of exact a_k")
    wb.add_assertion("median_reproduces_false_theta_on_bar_side",
                     computed=str(int(abs(f_conv - f_med) < tiny)), expected="1", tolerance=0,
                     source="t = +|t0|; convergent q-series vs median Borel sum")
    wb.add_assertion("borel_sum_within_least_term_of_optimal_truncation",
                     computed=str(int(abs(I_B - partial[2]) < least)), expected="1",
                     tolerance=0, source="consistency of the resummation with the asymptotics")
    wb.add_assertion("residual_falls_in_sector_gap",
                     computed=str(int(gap_lo < t_res < gap_hi)), expected="1", tolerance=0,
                     source="COMPARISON ONLY: sectors j=1, j=7 bracket t_res; Lean action gap")
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
