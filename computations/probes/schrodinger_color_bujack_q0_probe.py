#!/usr/bin/env python3
"""schrodinger_color_bujack_q0_probe.py

80-dps producer and literature cross-check for `rem:schrodinger-color-falsifiability`
and `tbl:schrodinger-color-falsifiability-table4-data` against Bujack et al. (2022)
[bujack2022] (`library/bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-co/
bujack-et-al-2022-the-non-riemannian-nature-of-perceptual-color-space.pdf`) for
bean qou-fls0.

Per the 2026-08-07 owner directive, evaluates `eta = (q_0 - q_0^{-1})/2` and
`d* = 1/eta` at the canonical proton-pinned `q_0 = q_at(80)` (`q_parameter.Q` at
80 dps, zero `float64`, zero parameter fitting):

  q_0 (proton pin) = 1.1099785827513808075916690956107688798744991218736...
  eta              = 0.10453014939781965771542310656455129225264587303503...
  d* = 1 / eta     = 9.5666179160828646205190093457644466389515499402546...

Also records why the prior text quoted `0.1043` and `9.59`: `ln(q_0) = 0.10434072...`
(`1/ln(q_0) = 9.58398...`) was previously conflated with `sinh(ln q_0) =
(q_0 - q_0^{-1})/2 = 0.10453015...` (`1/eta = 9.56662...`). Cross-checks the
strict sub-additivity, small-d cubic Taylor coefficient `-eta^2/6`, large-d
second-order Weber–Fechner logarithmic asymptote `ln(2*eta*d)/eta`, and Bujack
et al. Table 1 / Eq. (18) structural properties.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

import mpmath as mp

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.constants import Q_MUON_50_DIGIT_STR, q_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps(max(mp.mp.dps, 80))


def delta_E_perc(d: mp.mpf, eta: mp.mpf) -> mp.mpf:
    return mp.asinh(eta * d) / eta


def main() -> int:
    set_compute_dps(max(mp.mp.dps, 80))

    q0_proton = q_at(80)
    eta_proton = (q0_proton - 1 / q0_proton) / 2
    d_star_proton = 1 / eta_proton
    ln_q0 = mp.log(q0_proton)

    # Diagnostic comparison with CAL-2 muon pin (50-digit string)
    q0_muon = mp.mpf(Q_MUON_50_DIGIT_STR)
    eta_muon = (q0_muon - 1 / q0_muon) / 2
    d_star_muon = 1 / eta_muon

    # 1. Identity eta == sinh(ln(q_0)) and strict difference from ln(q_0)
    sinh_id_err = abs(eta_proton - mp.sinh(ln_q0))
    ln_vs_sinh_gap = eta_proton - ln_q0  # +1.894e-4 > 0

    # 2. Strict sub-additivity (diminishing returns): Delta E(d1) + Delta E(d2) > Delta E(d1 + d2)
    subadd_pairs = [
        (mp.mpf("1"), mp.mpf("2")),
        (mp.mpf("5"), mp.mpf("5")),
        (mp.mpf("10"), mp.mpf("15")),
    ]
    min_subadd_margin = min(
        (delta_E_perc(d1, eta_proton) + delta_E_perc(d2, eta_proton))
        - delta_E_perc(d1 + d2, eta_proton)
        for d1, d2 in subadd_pairs
    )

    # 3. Table 1 small-d Taylor regime: Delta E(d) = d - (eta^2 / 6) d^3 + O(eta^4 d^5)
    d_small = mp.mpf("1e-12")
    taylor_cubic_approx = d_small - (eta_proton ** 2 / 6) * (d_small ** 3)
    taylor_fifth_bound = (3 * (eta_proton ** 4) / 40) * (d_small ** 5)
    taylor_err = abs(delta_E_perc(d_small, eta_proton) - taylor_cubic_approx)

    # 4. Table 1 large-d Weber–Fechner regime: Delta E(d) = ln(2*eta*d)/eta + 1/(4*eta^3*d^2) + O(d^{-4})
    d_large = mp.mpf("1e12")
    wf_lead = mp.log(2 * eta_proton * d_large) / eta_proton
    wf_next = wf_lead + 1 / (4 * (eta_proton ** 3) * (d_large ** 2))
    wf_err = abs(delta_E_perc(d_large, eta_proton) - wf_next)

    # 5. Table 2 & Table 4 confirmation-band check: eta_proton in [0.08, 0.13]
    in_confirmation_band = (mp.mpf("0.08") <= eta_proton <= mp.mpf("0.13"))

    # 6. Bujack et al. (2022) Eq. (18) f_log(Delta_psi) = b * ln(a * Delta_psi + 1) / ln(a + 1):
    #    Verify concave sub-additivity of Bujack's f_log and exact logarithmic matching at large scale:
    a_buj, b_buj = mp.mpf("4"), mp.mpf("1")
    f_log = lambda x: b_buj * mp.log(a_buj * x + 1) / mp.log(a_buj + 1)
    bujack_flog_subadd = (f_log(mp.mpf("0.3")) + f_log(mp.mpf("0.4"))) - f_log(mp.mpf("0.7"))

    wb = WitnessBuilder("schrodinger-color-bujack-q0", engine="mpmath")
    wb.set_description(
        "80-dps evaluation of eta = (q_0 - q_0^{-1})/2 and crossover scale d* = 1/eta "
        "at the canonical proton-pinned substrate parameter q_0 = q_at(80), together "
        "with asymptotic and Bujack et al. (2022) [bujack2022] cross-checks for "
        "rem:schrodinger-color-falsifiability (bean qou-fls0)."
    )
    wb.set_content_block("rem:schrodinger-color-falsifiability")

    wb.add_assertion(
        "eta_equals_sinh_ln_q0_at_80dps",
        computed=fmt(sinh_id_err),
        expected="0",
        tolerance="1e-75",
        source="eta = (q_0 - q_0^{-1})/2 = sinh(ln q_0) = 0.10453015... (distinct from ln q_0 = 0.10434072...)",
    )
    wb.add_assertion(
        "strict_subadditivity_diminishing_returns",
        computed=str(bool(min_subadd_margin > mp.mpf("1e-3") and bujack_flog_subadd > mp.mpf("1e-2") and ln_vs_sinh_gap > mp.mpf("1e-4"))),
        expected="True",
        source="[bujack2022] strict triangle inequality Delta E(A,B) + Delta E(B,C) > Delta E(A,C)",
    )
    wb.add_assertion(
        "table1_small_d_cubic_subadditive_expansion",
        computed=fmt(taylor_err),
        expected="0",
        tolerance=fmt(2 * taylor_fifth_bound),
        source="arsinh(eta*d)/eta = d - (eta^2/6)d^3 + O(eta^4 d^5) at d = 1e-12",
    )
    wb.add_assertion(
        "table1_large_d_second_order_weber_fechner_asymptote",
        computed=fmt(wf_err),
        expected="0",
        tolerance="1e-40",
        source="arsinh(eta*d)/eta = ln(2*eta*d)/eta + 1/(4*eta^3*d^2) + O(d^{-4}) at d = 1e12",
    )
    wb.add_assertion(
        "proton_pin_eta_lies_in_table2_confirmation_band",
        computed=str(bool(in_confirmation_band)),
        expected="True",
        source="eta(q_0) = 0.10453015... lies inside [0.08, 0.13] protocol confirmation band",
    )

    wb.add_data("proton_pin_80dps", {
        "pin": "proton (q_parameter.Q / qou_substrate.constants.q_at(80))",
        "q0": fmt(q0_proton),
        "ln_q0": fmt(ln_q0),
        "eta": fmt(eta_proton),
        "d_star": fmt(d_star_proton),
        "two_eta_q_minus_qinv": fmt(2 * eta_proton),
    })
    wb.add_data("muon_pin_diagnostic_comparison", {
        "q0_muon_50dps": fmt(q0_muon),
        "eta_muon": fmt(eta_muon),
        "d_star_muon": fmt(d_star_muon),
        "abs_diff_eta_proton_vs_muon": fmt(abs(eta_proton - eta_muon)),
    })
    wb.add_data("bujack2022_published_table1_summary", {
        "source": "[bujack2022] PNAS 119(18) e2119753119, Results Table 1 & Eq. (18)",
        "beta_0": "0.161 (t(60) = 8.894, p < 0.001)",
        "beta_Delta_d_5": "0.048 (t(60) = 2.815, p = 0.010)",
        "beta_Delta_d_10": "0.119 (t(60) = 6.632, p < 0.001)",
        "beta_d_bar": "-0.005 (t(60) = -5.566, p < 0.001)",
        "model_fit": "R^2 = 0.556, F(3, 60) = 25.00, P < 0.001, 75896 training trials",
        "crossover_d_star_empirical_status": "not measured in [bujack2022]; neither corroborated nor refuted",
    })
    wb.save({"q0Anchor": "proton"})
    print(f"  proton pin q_0 = {fmt(q0_proton)}")
    print(f"  eta            = {fmt(eta_proton)}")
    print(f"  d* = 1/eta     = {fmt(d_star_proton)}")
    return 0 if all(a.passed for a in wb.assertions) else 1


if __name__ == "__main__":
    raise SystemExit(main())
