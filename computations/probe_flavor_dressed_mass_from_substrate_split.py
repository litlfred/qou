#!/usr/bin/env python3
# polynomial_q_not_applicable: closed-form substrate evaluation at
# q = q_0 in mpmath; no q-polynomial / symbolic arithmetic.
"""Flavor-dressed mass splitting μ_d − μ_u from the substrate split.

Emits `flavor-dressed-mass-from-substrate-split.witness.json` for both
`prop:flavor-dressed-mass-from-substrate-split` and
`thm:flavor-mass-splitting-bound`.

The down–up dressed-quark splitting is fixed by the substrate formula
(prop:flavor-dressed-mass-from-substrate-split):

    μ_d − μ_u = M_N · (q−1)²(1−q⁻⁴)/3 · (q^½ + q^−½)/(q + q⁻¹)

with M_N = (m_p + m_n)/2 the CODATA nucleon-mass average and q = q_0
the substrate parameter. The leading substrate factor satisfies the
algebraic identity

    (q−1)²(1−q⁻⁴)/3 = (1/3) · ℏ_q² · h_q · [2]_q

where ℏ_q = (q−1)/q, h_q = q − q⁻¹, [2]_q = q + q⁻¹.

The two-sided substrate bound (thm:flavor-mass-splitting-bound) is

    0 < μ_d − μ_u < M_N · ℏ_q² · h_q · [2]_q

and the slack ratio is

    (μ_d − μ_u) / (M_N · ℏ_q² · h_q · [2]_q) = (1/3)·(q^½+q^−½)/(q+q⁻¹).

Cited numerics (rem:dressed-quark-numerology-at-q0):
    μ_d − μ_u ≈ 1.286 MeV
    bound     ≈ 3.88 MeV
    realised/bound ≈ 33 %  (= (1/3)·0.997)

This probe pins the SPLITTING μ_d − μ_u (substrate-pure modulo the
M_N anchor). It does NOT pin the individual μ_u, μ_d (those need the
baryon-content sum rule for μ̄). The CODATA m_n − m_p = 1.29333 MeV
is a cross-check target, not an input.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from codata_constants import (  # noqa: E402
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
)
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    w = WitnessBuilder(
        "flavor-dressed-mass-from-substrate-split",
        engine="mpmath",
    )
    w.set_description(
        "Substrate-derived down–up dressed-quark splitting "
        "μ_d − μ_u = M_N · (q−1)²(1−q⁻⁴)/3 · (q^½+q^−½)/(q+q⁻¹) at "
        "q = q_0. Verifies the substrate identity (q−1)²(1−q⁻⁴)/3 = "
        "(1/3)ℏ²h[2], the two-sided bound 0 < μ_d−μ_u < M_N·ℏ²·h·[2], "
        "and the slack ratio (1/3)(q^½+q^−½)/(q+q⁻¹). Pins μ_d−μ_u ≈ "
        "1.286 MeV (substrate-pure modulo the CODATA M_N anchor); m_n−m_p "
        "is a cross-check target, not an input. Covers "
        "prop:flavor-dressed-mass-from-substrate-split and "
        "thm:flavor-mass-splitting-bound."
    )
    w.set_content_block("prop:flavor-dressed-mass-from-substrate-split")

    set_compute_dps(50)
    with mp.workdps(50):
        q = mp.mpf(Q_50_DIGIT_STR)
        m_p = mp.mpf(M_P_MEV_VALIDATION)
        m_n = mp.mpf(M_N_MEV_VALIDATION)
        M_N = (m_p + m_n) / 2

        # Substrate factor and its identity form.
        sub_factor = (q - 1) ** 2 * (1 - q ** (-4)) / 3
        hbar_q = (q - 1) / q
        h_q = q - 1 / q
        two_q = q + 1 / q
        sub_factor_identity = mp.mpf(1) / 3 * hbar_q ** 2 * h_q * two_q

        # Skein-side adjustment factor.
        skein = (mp.sqrt(q) + 1 / mp.sqrt(q)) / (q + 1 / q)

        # The realised splitting.
        mu_d_minus_u = M_N * sub_factor * skein

        # Two-sided substrate bound.
        bound = M_N * hbar_q ** 2 * h_q * two_q
        slack_ratio = mu_d_minus_u / bound
        slack_closed = mp.mpf(1) / 3 * skein  # = (1/3)(q^½+q^−½)/(q+q⁻¹)

        # m_n − m_p prediction (cross-check, not an input).
        mn_mp_pred = (q + 1 / q) / (mp.sqrt(q) + 1 / mp.sqrt(q)) * mu_d_minus_u
        mn_mp_codata = m_n - m_p
        mn_mp_residual = (mn_mp_pred - mn_mp_codata) / mn_mp_codata

        print(f"  q_0              = {mp.nstr(q, 20)}")
        print(f"  M_N (MeV)        = {mp.nstr(M_N, 12)}")
        print(f"  substrate factor = {mp.nstr(sub_factor, 14)}")
        print(f"  identity (1/3)ℏ²h[2] = {mp.nstr(sub_factor_identity, 14)}")
        print(f"  skein factor     = {mp.nstr(skein, 12)}")
        print(f"  μ_d − μ_u (MeV)  = {mp.nstr(mu_d_minus_u, 12)}  [cited 1.286]")
        print(f"  bound (MeV)      = {mp.nstr(bound, 12)}  [cited 3.88]")
        print(f"  slack ratio      = {mp.nstr(slack_ratio, 12)}  [cited ~0.33]")
        print(f"  m_n−m_p pred     = {mp.nstr(mn_mp_pred, 12)} vs CODATA "
              f"{mp.nstr(mn_mp_codata, 12)}")

        w.add_parameter("q_0", Q_50_DIGIT_STR)
        w.add_parameter("M_N_MeV", str(M_N))
        w.add_parameter("m_p_MeV_codata", M_P_MEV_VALIDATION)
        w.add_parameter("m_n_MeV_codata", M_N_MEV_VALIDATION)
        w.add_parameter("dps", 50)

        w.add_data("substrate_factor", str(sub_factor))
        w.add_data("substrate_factor_identity_form", str(sub_factor_identity))
        w.add_data("skein_factor", str(skein))
        w.add_data("mu_d_minus_mu_u_MeV", str(mu_d_minus_u))
        w.add_data("mu_d_minus_mu_u_MeV_float", float(mu_d_minus_u))
        w.add_data("substrate_bound_MeV", str(bound))
        w.add_data("substrate_bound_MeV_float", float(bound))
        w.add_data("slack_ratio", str(slack_ratio))
        w.add_data("slack_ratio_closed_form", str(slack_closed))
        w.add_data("m_n_minus_m_p_predicted_MeV", str(mn_mp_pred))
        w.add_data("m_n_minus_m_p_codata_MeV", str(mn_mp_codata))
        w.add_data("m_n_minus_m_p_residual_fraction", float(mn_mp_residual))

        # Cross-check assertions.
        w.add_assertion(
            name="mu_d_minus_mu_u_MeV",
            computed=float(mu_d_minus_u),
            expected=1.286,
            tolerance=1e-3,
            unit="MeV",
            source=(
                "rem:dressed-quark-numerology-at-q0 cites μ_d − μ_u ≈ "
                "1.286 MeV from the substrate split at q_0"
            ),
        )
        w.add_assertion(
            name="substrate_identity_holds",
            computed=float(sub_factor),
            expected=float(sub_factor_identity),
            tolerance=1e-40,
            source=(
                "(q−1)²(1−q⁻⁴)/3 = (1/3)·ℏ_q²·h_q·[2]_q "
                "(algebraic identity, prop statement)"
            ),
        )
        w.add_assertion(
            name="substrate_bound_MeV",
            computed=float(bound),
            expected=3.88,
            tolerance=1e-2,
            unit="MeV",
            source=(
                "thm:flavor-mass-splitting-bound upper bound "
                "M_N·ℏ²·h·[2] ≈ 3.88 MeV (rem:dressed-quark-numerology)"
            ),
        )
        w.add_assertion(
            name="slack_ratio_one_third_times_skein",
            computed=float(slack_ratio),
            expected=float(slack_closed),
            tolerance=1e-40,
            source=(
                "slack ratio = (μ_d−μ_u)/(M_N·ℏ²·h·[2]) = "
                "(1/3)·(q^½+q^−½)/(q+q⁻¹) (slack-ratio identity)"
            ),
        )
        w.add_assertion(
            name="splitting_strictly_positive_below_bound",
            computed=1 if (0 < mu_d_minus_u < bound) else 0,
            expected=1,
            tolerance=0,
            source=(
                "thm:flavor-mass-splitting-bound: 0 < μ_d−μ_u < "
                "M_N·ℏ²·h·[2] for q_0 > 1"
            ),
        )

    out = w.save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
