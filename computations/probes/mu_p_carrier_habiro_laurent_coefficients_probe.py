#!/usr/bin/env python3
"""mu_p_carrier_habiro_laurent_coefficients_probe.py — exact Laurent-polynomial
Habiro-basis coefficients a_n(q) in Z[q^{+/-1}] and figure-eight cyclotomic
rungs c_n(q0) vs q=1 Taylor expansion in h^2 (bean `qou-6gf9`).

Bean `qou-6gf9` (parent `qou-2002`) noted in its closing scope statement that
prior probes evaluated either:
  * the bare bar-even basis omega_n(q0) = (q0; q0)_n (q0^-1; q0^-1)_n
    (`computations/mu_p_habiro_basis_order_probe.py`), or
  * the q = 1 Taylor / Ohtsuki expansion in x = q - 1
    (`computations/mu_p_sigma235_ohtsuki_resolution_probe.py`),
leaving open the exact Laurent-polynomial Habiro-basis coefficients
a_n(q) in Z[q^{+/-1}] and the comparison between the Laurent-kept cyclotomic
rungs c_n(q0) = a_n(q0) (q0; q0)_n^2 and the q = 1 Taylor expansion in
h^2 = (q0 - 1/q0)^2.

What this probe computes (exact Laurent arithmetic over Z[q, q^-1] + 50-dps
mpmath at the proton pin q0, with zero fitting):

  1. Exact Laurent identity in Z[q, q^-1] for n = 0..8:
     In the (q; q)_n^2 Habiro cyclotomic basis for the figure-eight knot 4_1,
         J_{4_1}(q) = sum_{n>=0} (q; q)_n (q^-1; q^-1)_n
                    = sum_{n>=0} a_n(q) (q; q)_n^2,
     where (1 - q^-k) = -q^-k (1 - q^k) gives the exact Laurent monomial
         a_n(q) = (-1)^n q^{-n(n+1)/2} in Z[q, q^-1].
     Multiplying a_n(q) by (q; q)_n^2 in Z[q, q^-1] reproduces the bar-even
     tower c_n(q) = (-1)^n prod_{k=1}^n (q^k + q^-k - 2) = omega_n(q) with
     zero coefficient discrepancy for every n = 0..8, and satisfies
     c_n(q^-1) = c_n(q) identically, whereas freezing a_n(q) -> a_n(1) = (-1)^n
     breaks bar-evenness by the factor q^{n(n+1)/2}.

  2. Exact comparison of c_n(q0) against the q = 1 Taylor expansion in
     h^2 = (q0 - 1/q0)^2 and against the q = 1 frozen-coefficient rung
     a_n(1) (q0; q0)_n^2 at n = 1 and n = 2:
     * At n = 1:
         c_1(q) = -q^-1 (1 - q)^2 = -w(q),   w(q) = q + q^-1 - 2,
         h(q)^2 = (q - q^-1)^2 = w(q)^2 + 4 w(q),
       so the leading q = 1 Taylor approximation in h^2 is
         c_1^{Taylor-h^2}(q) = -h(q)^2 / 4,
       and keeping the exact Laurent coefficient a_1(q0) = -q0^-1 shifts c_1(q0)
       relative to -h(q0)^2 / 4 by the exact positive bar-even remainder
         Delta_h2 c_1(q0) = c_1(q0) - (-h(q0)^2 / 4) = +w(q0)^2 / 4
                          = +2.96854260081976e-5  (+2724.2 ppm of |c_1(q0)|),
       while shifting a_1(1)(1 - q0)^2 = -(1 - q0)^2 by the factor
       q0^-1 = 1 - hbar_{q0} (-9.90817%).
     * At n = 2:
         c_2(q) = +q^-3 (q; q)_2^2 = w(q) (w(q) + 4) w(q) = w(q) h(q)^2,
       whose leading q = 1 Taylor approximation in h^2 is
         c_2^{Taylor-h^2}(q) = +h(q)^4 / 4,
       with exact Laurent-vs-Taylor shift
         Delta_h2 c_2(q0) = c_2(q0) - h(q0)^4 / 4 = -w(q0)^2 h(q0)^2 / 4
                          = -1.297437419491036e-6  (-2724.2 ppm of |c_2(q0)|).

  3. Position relative to the Class I mu-p carrier gap t (without fitting):
     Tested against both the historical CODATA-2018 datum quoted in `qou-6gf9`
     (t_2018 = +209.754920524 ppb) and the live CODATA-2022 tension witness
     `mu-substrate-tension-audit-100dps.witness.json`
     (t_live = +211.164914360 ppb):
       * |c_1(q0)| / t_2018 = 51950.5,  |Delta_h2 c_1(q0)| / t_2018 = 141.524
       * |c_2(q0)| / t_2018 = 2270.56,  |Delta_h2 c_2(q0)| / t_2018 = 6.18549
     Neither the n = 1 nor the n = 2 Laurent-kept Habiro rung, nor their
     Laurent-vs-Taylor shifts, lies inside the [1.8e-7, 2.4e-7] residual window.

Output: `computations/probes/mu-p-carrier-habiro-laurent-coefficients.witness.json`
"""
from __future__ import annotations

import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

import mpmath as mp

from _precision import fmt, set_compute_dps
from q_parameter import Q_50_DIGIT_STR
from witness_base import WitnessBuilder

set_compute_dps()

HERE = Path(__file__).resolve().parent
COMPUTATIONS_ROOT = HERE.parent
TENSION_WITNESS = COMPUTATIONS_ROOT / "mu-substrate-tension-audit-100dps.witness.json"

# Historical CODATA-2018 residual quoted in bean qou-6gf9 header (+209.755 ppb)
T_CODATA_2018 = mp.mpf("2.09754920524e-7")
WINDOW_LO = mp.mpf("1.8e-7")
WINDOW_HI = mp.mpf("2.4e-7")
SMALL_HEIGHT_LO = mp.mpf(1) / 5
SMALL_HEIGHT_HI = mp.mpf(5)

LaurentPoly = dict[int, int]


def laurent_clean(p: LaurentPoly) -> LaurentPoly:
    return {k: v for k, v in sorted(p.items()) if v != 0}


def laurent_mul(a: LaurentPoly, b: LaurentPoly) -> LaurentPoly:
    out: LaurentPoly = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            out[ka + kb] = out.get(ka + kb, 0) + va * vb
    return laurent_clean(out)


def laurent_sub(a: LaurentPoly, b: LaurentPoly) -> LaurentPoly:
    out = dict(a)
    for kb, vb in b.items():
        out[kb] = out.get(kb, 0) - vb
    return laurent_clean(out)


def laurent_bar(p: LaurentPoly) -> LaurentPoly:
    """Bar involution q -> q^-1 on Z[q, q^-1]."""
    return laurent_clean({-k: v for k, v in p.items()})


def laurent_eval_mpf(p: LaurentPoly, q: mp.mpf) -> mp.mpf:
    total = mp.mpf(0)
    for k, v in p.items():
        total += mp.mpf(v) * (q ** k)
    return total


def q_pochhammer_laurent(n: int) -> LaurentPoly:
    """Exact (q; q)_n = prod_{k=1}^n (1 - q^k) in Z[q, q^-1]."""
    res: LaurentPoly = {0: 1}
    for k in range(1, n + 1):
        res = laurent_mul(res, {0: 1, k: -1})
    return res


def qinv_pochhammer_laurent(n: int) -> LaurentPoly:
    """Exact (q^-1; q^-1)_n = prod_{k=1}^n (1 - q^-k) in Z[q, q^-1]."""
    res: LaurentPoly = {0: 1}
    for k in range(1, n + 1):
        res = laurent_mul(res, {0: 1, -k: -1})
    return res


def habiro_a_n_laurent(n: int) -> LaurentPoly:
    """Exact Habiro coefficient a_n(q) = (-1)^n q^{-n(n+1)/2} in the (q; q)_n^2 basis."""
    exp = -(n * (n + 1)) // 2
    sign = -1 if (n % 2 == 1) else 1
    return {exp: sign}


def bar_even_tower_laurent(n: int) -> LaurentPoly:
    """Exact (-1)^n prod_{k=1}^n (q^k + q^-k - 2) in Z[q, q^-1]."""
    res: LaurentPoly = {0: -1 if (n % 2 == 1) else 1}
    for k in range(1, n + 1):
        res = laurent_mul(res, {-k: 1, 0: -2, k: 1})
    return res


def load_live_residual() -> mp.mpf:
    data = json.loads(TENSION_WITNESS.read_text(encoding="utf-8"))
    ppb = mp.mpf(data["data"]["residual_ppb_at_canonical_q0"])
    return ppb * mp.mpf("1e-9")


def main() -> int:
    q0 = mp.mpf(Q_50_DIGIT_STR)
    hbar_q0 = mp.mpf(1) - mp.mpf(1) / q0
    h_q0 = q0 - mp.mpf(1) / q0
    h2_q0 = h_q0 ** 2
    w_q0 = q0 + mp.mpf(1) / q0 - mp.mpf(2)
    t_live = load_live_residual()

    # 1. Exact Laurent polynomial verification for n = 0..8
    max_laurent_identity_diff = 0
    max_bar_parity_diff = 0
    max_eval_diff = mp.mpf(0)
    laurent_table = []

    for n in range(0, 9):
        poch_q = q_pochhammer_laurent(n)
        poch_q_sq = laurent_mul(poch_q, poch_q)
        poch_qinv = qinv_pochhammer_laurent(n)
        a_n = habiro_a_n_laurent(n)

        c_n_from_an = laurent_mul(a_n, poch_q_sq)
        c_n_from_poch = laurent_mul(poch_q, poch_qinv)
        c_n_from_tower = bar_even_tower_laurent(n)

        diff1 = laurent_sub(c_n_from_an, c_n_from_poch)
        diff2 = laurent_sub(c_n_from_an, c_n_from_tower)
        diff_bar = laurent_sub(c_n_from_an, laurent_bar(c_n_from_an))

        if diff1 or diff2:
            max_laurent_identity_diff = max(
                max_laurent_identity_diff,
                max((abs(v) for v in diff1.values()), default=0),
                max((abs(v) for v in diff2.values()), default=0),
            )
        if diff_bar:
            max_bar_parity_diff = max(
                max_bar_parity_diff,
                max((abs(v) for v in diff_bar.values()), default=0),
            )

        c_n_val = laurent_eval_mpf(c_n_from_an, q0)
        an_val = laurent_eval_mpf(a_n, q0)
        poch_sq_val = laurent_eval_mpf(poch_q_sq, q0)
        c_n_q1_frozen = (mp.mpf(-1) ** n) * poch_sq_val
        max_eval_diff = max(max_eval_diff, abs(c_n_val - an_val * poch_sq_val))

        laurent_table.append({
            "n": n,
            "a_n_exponent": -(n * (n + 1)) // 2,
            "a_n_sign": -1 if (n % 2 == 1) else 1,
            "a_n_at_q0": fmt(an_val),
            "c_n_laurent_num_terms": len(c_n_from_an),
            "c_n_min_degree": min(c_n_from_an.keys()),
            "c_n_max_degree": max(c_n_from_an.keys()),
            "c_n_l1_norm": int(sum(abs(v) for v in c_n_from_an.values())),
            "c_n_at_q0": fmt(c_n_val),
            "c_n_q1_frozen_at_q0": fmt(c_n_q1_frozen),
            "laurent_over_q1_frozen_ratio": fmt(c_n_val / c_n_q1_frozen) if n > 0 else "1",
        })

    # 2. Detailed n = 1 and n = 2 comparison: Laurent-kept c_n(q0) vs q=1 Taylor in h^2
    c1_laurent = laurent_eval_mpf(bar_even_tower_laurent(1), q0)
    c1_q1_frozen = -((mp.mpf(1) - q0) ** 2)
    c1_taylor_h2_leading = -h2_q0 / mp.mpf(4)
    c1_taylor_h2_two_term = -h2_q0 / mp.mpf(4) + (h2_q0 ** 2) / mp.mpf(64)
    c1_shift_vs_taylor_h2 = c1_laurent - c1_taylor_h2_leading
    c1_shift_exact_w2_over_4 = (w_q0 ** 2) / mp.mpf(4)
    c1_shift_vs_q1_frozen = c1_laurent - c1_q1_frozen

    c2_laurent = laurent_eval_mpf(bar_even_tower_laurent(2), q0)
    c2_q1_frozen = ((mp.mpf(1) - q0) * (mp.mpf(1) - q0 ** 2)) ** 2
    c2_taylor_h2_leading = (h2_q0 ** 2) / mp.mpf(4)
    c2_taylor_h2_two_term = (h2_q0 ** 2) / mp.mpf(4) - (h2_q0 ** 3) / mp.mpf(64)
    c2_shift_vs_taylor_h2 = c2_laurent - c2_taylor_h2_leading
    c2_shift_exact_neg_w2_h2_over_4 = -(w_q0 ** 2) * h2_q0 / mp.mpf(4)
    c2_shift_vs_q1_frozen = c2_laurent - c2_q1_frozen

    # Identity checks at 50 dps
    err_h2_w_identity = abs(h2_q0 - (w_q0 ** 2 + mp.mpf(4) * w_q0))
    err_c1_shift_identity = abs(c1_shift_vs_taylor_h2 - c1_shift_exact_w2_over_4)
    err_c2_shift_identity = abs(c2_shift_vs_taylor_h2 - c2_shift_exact_neg_w2_h2_over_4)

    # 3. Comparison against the mu-p residual (both CODATA-2018 209.755 ppb and live CODATA-2022 211.165 ppb)
    n1_n2_gap_comparison = {
        "t_codata2018": fmt(T_CODATA_2018),
        "t_codata2022_live": fmt(t_live),
        "abs_c1_over_t_2018": fmt(abs(c1_laurent) / T_CODATA_2018),
        "abs_c1_over_t_live": fmt(abs(c1_laurent) / t_live),
        "abs_delta_h2_c1_over_t_2018": fmt(abs(c1_shift_vs_taylor_h2) / T_CODATA_2018),
        "abs_delta_h2_c1_over_t_live": fmt(abs(c1_shift_vs_taylor_h2) / t_live),
        "abs_c2_over_t_2018": fmt(abs(c2_laurent) / T_CODATA_2018),
        "abs_c2_over_t_live": fmt(abs(c2_laurent) / t_live),
        "abs_delta_h2_c2_over_t_2018": fmt(abs(c2_shift_vs_taylor_h2) / T_CODATA_2018),
        "abs_delta_h2_c2_over_t_live": fmt(abs(c2_shift_vs_taylor_h2) / t_live),
        "n1_or_n2_in_residual_window": bool(
            (WINDOW_LO <= abs(c1_laurent) <= WINDOW_HI)
            or (WINDOW_LO <= abs(c1_shift_vs_taylor_h2) <= WINDOW_HI)
            or (WINDOW_LO <= abs(c2_laurent) <= WINDOW_HI)
            or (WINDOW_LO <= abs(c2_shift_vs_taylor_h2) <= WINDOW_HI)
        ),
    }

    # 4. Full sweep n = 1..12 of Laurent-kept c_n(q0) vs leading h^2 Taylor (n!)^2 (h^2/4)^n
    rung_comparison_rows = []
    small_height_orders_live = []
    for n in range(1, 13):
        cn = mp.mpf(-1) ** n
        for k in range(1, n + 1):
            cn *= (q0 ** k + q0 ** (-k) - mp.mpf(2))
        cn_taylor_h2 = (mp.mpf(-1) ** n) * (mp.factorial(n) ** 2) * ((h2_q0 / mp.mpf(4)) ** n)
        req_coeff_live = t_live / abs(cn)
        req_coeff_2018 = T_CODATA_2018 / abs(cn)
        in_small_height = bool(SMALL_HEIGHT_LO <= req_coeff_live <= SMALL_HEIGHT_HI)
        if in_small_height:
            small_height_orders_live.append(n)
        rung_comparison_rows.append({
            "n": n,
            "c_n_laurent_at_q0": fmt(cn),
            "c_n_leading_h2_taylor": fmt(cn_taylor_h2),
            "laurent_minus_h2_taylor": fmt(cn - cn_taylor_h2),
            "laurent_over_h2_taylor_ratio": fmt(cn / cn_taylor_h2),
            "t_live_over_abs_c_n": fmt(req_coeff_live),
            "t_2018_over_abs_c_n": fmt(req_coeff_2018),
            "in_small_height_band": in_small_height,
        })

    print("=" * 78)
    print(" Exact Habiro Laurent Coefficients a_n(q) & Rungs c_n(q0) vs h^2 Taylor")
    print("=" * 78)
    print(f"  q0          = {mp.nstr(q0, 20)}")
    print(f"  hbar_q0     = {mp.nstr(hbar_q0, 16)}   h(q0)^2 = {mp.nstr(h2_q0, 16)}")
    print(f"  w(q0)       = {mp.nstr(w_q0, 16)}")
    print(f"  t_2018      = {mp.nstr(T_CODATA_2018, 12)}   t_live  = {mp.nstr(t_live, 12)}")
    print(f"  n=1 Laurent c_1(q0)        = {mp.nstr(c1_laurent, 16)}")
    print(f"  n=1 leading h^2 Taylor     = {mp.nstr(c1_taylor_h2_leading, 16)}")
    print(f"  n=1 shift (+w^2/4)         = {mp.nstr(c1_shift_vs_taylor_h2, 16)}  ({mp.nstr(abs(c1_shift_vs_taylor_h2)/T_CODATA_2018, 7)} x t_2018)")
    print(f"  n=2 Laurent c_2(q0)        = {mp.nstr(c2_laurent, 16)}")
    print(f"  n=2 leading h^2 Taylor     = {mp.nstr(c2_taylor_h2_leading, 16)}")
    print(f"  n=2 shift (-w^2 h^2 / 4)   = {mp.nstr(c2_shift_vs_taylor_h2, 16)}  ({mp.nstr(abs(c2_shift_vs_taylor_h2)/T_CODATA_2018, 7)} x t_2018)")
    print(f"  small-height orders (n=1..12): {small_height_orders_live}")

    wb = WitnessBuilder("mu-p-carrier-habiro-laurent-coefficients", engine="mpmath")
    wb.set_description(
        "Exact Laurent-polynomial Habiro cyclotomic coefficients "
        "a_n(q) = (-1)^n q^{-n(n+1)/2} in Z[q, q^-1] for the figure-eight "
        "expansion J_{4_1}(q) = sum_{n>=0} a_n(q) (q; q)_n^2, evaluated "
        "term-by-term at the proton pin q0 and compared against the q = 1 "
        "Taylor expansion in h^2 = (q0 - 1/q0)^2 and the Class I mu-p "
        "carrier residual (+209.755 ppb CODATA-2018; +211.165 ppb live "
        "CODATA-2022) without fitting (bean qou-6gf9)."
    )
    wb.add_parameter("q0", fmt(q0))
    wb.add_parameter("hbar_q0", fmt(hbar_q0))
    wb.add_parameter("h_q0", fmt(h_q0))
    wb.add_parameter("h2_q0", fmt(h2_q0))
    wb.add_parameter("w_q0", fmt(w_q0))
    wb.add_parameter("t_codata2018", fmt(T_CODATA_2018))
    wb.add_parameter("t_codata2022_live", fmt(t_live))

    wb.add_data("exact_laurent_basis_table_n0_to_8", laurent_table)
    wb.add_data("n1_comparison", {
        "a_1_laurent": "-q^-1",
        "a_1_at_q0": fmt(-mp.mpf(1) / q0),
        "c_1_laurent_at_q0": fmt(c1_laurent),
        "c_1_q1_frozen_at_q0": fmt(c1_q1_frozen),
        "c_1_leading_h2_taylor": fmt(c1_taylor_h2_leading),
        "c_1_two_term_h2_taylor": fmt(c1_taylor_h2_two_term),
        "shift_laurent_minus_leading_h2_taylor": fmt(c1_shift_vs_taylor_h2),
        "shift_closed_form_w2_over_4": fmt(c1_shift_exact_w2_over_4),
        "shift_laurent_minus_q1_frozen": fmt(c1_shift_vs_q1_frozen),
        "relative_shift_vs_leading_h2_taylor": fmt(c1_shift_vs_taylor_h2 / abs(c1_taylor_h2_leading)),
        "relative_shift_vs_q1_frozen": fmt(c1_shift_vs_q1_frozen / abs(c1_q1_frozen)),
    })
    wb.add_data("n2_comparison", {
        "a_2_laurent": "+q^-3",
        "a_2_at_q0": fmt(mp.mpf(1) / (q0 ** 3)),
        "c_2_laurent_at_q0": fmt(c2_laurent),
        "c_2_q1_frozen_at_q0": fmt(c2_q1_frozen),
        "c_2_leading_h2_taylor": fmt(c2_taylor_h2_leading),
        "c_2_two_term_h2_taylor": fmt(c2_taylor_h2_two_term),
        "shift_laurent_minus_leading_h2_taylor": fmt(c2_shift_vs_taylor_h2),
        "shift_closed_form_neg_w2_h2_over_4": fmt(c2_shift_exact_neg_w2_h2_over_4),
        "shift_laurent_minus_q1_frozen": fmt(c2_shift_vs_q1_frozen),
        "relative_shift_vs_leading_h2_taylor": fmt(c2_shift_vs_taylor_h2 / c2_taylor_h2_leading),
        "relative_shift_vs_q1_frozen": fmt(c2_shift_vs_q1_frozen / c2_q1_frozen),
    })
    wb.add_data("gap_comparison", n1_n2_gap_comparison)
    wb.add_data("rung_comparison_n1_to_12", rung_comparison_rows)
    wb.add_data("small_height_orders_live", small_height_orders_live)

    wb.add_assertion(
        name="laurent_habiro_basis_matches_bar_even_tower_identically",
        computed=str(max_laurent_identity_diff + max_bar_parity_diff),
        expected="0",
        tolerance="0",
        source="Exact Z[q, q^-1] identity (-1)^n q^{-n(n+1)/2} (q; q)_n^2 = (q; q)_n (q^-1; q^-1)_n = omega_n(q)",
    )
    wb.add_assertion(
        name="n1_laurent_vs_h2_taylor_shift_equals_w2_over_4",
        computed=fmt(err_c1_shift_identity + err_h2_w_identity),
        expected="0",
        tolerance="1e-45",
        source="Exact algebraic identity c_1(q) - (-h^2/4) = -w + (w^2 + 4w)/4 = w^2/4",
    )
    wb.add_assertion(
        name="n2_laurent_vs_h2_taylor_shift_equals_neg_w2_h2_over_4",
        computed=fmt(err_c2_shift_identity),
        expected="0",
        tolerance="1e-45",
        source="Exact algebraic identity c_2(q) - h^4/4 = w h^2 - (w + w^2/4) h^2 = -w^2 h^2 / 4",
    )
    wb.add_assertion(
        name="n1_and_n2_laurent_rungs_and_shifts_outside_mup_residual_window",
        computed="0" if n1_n2_gap_comparison["n1_or_n2_in_residual_window"] else "1",
        expected="1",
        tolerance="0",
        source="Bean qou-6gf9: n=1 shift is 141.5x t and n=2 shift is 6.19x t; neither lands in [1.8e-7, 2.4e-7]",
    )
    wb.add_assertion(
        name="small_height_band_remains_six_consecutive_orders_6_to_11",
        computed=str(small_height_orders_live == [6, 7, 8, 9, 10, 11]),
        expected="True",
        tolerance="0",
        source="Corroborates mu_p_habiro_basis_order_probe.py: orders 6..11 bracket t in [1/5, 5]",
    )

    out_path = wb.save()
    print(f"\n  witness: {out_path}")

    ok = (
        max_laurent_identity_diff == 0
        and max_bar_parity_diff == 0
        and max_eval_diff < mp.mpf("1e-45")
        and err_c1_shift_identity < mp.mpf("1e-45")
        and err_c2_shift_identity < mp.mpf("1e-45")
        and not n1_n2_gap_comparison["n1_or_n2_in_residual_window"]
        and small_height_orders_live == [6, 7, 8, 9, 10, 11]
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
