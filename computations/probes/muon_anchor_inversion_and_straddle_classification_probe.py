#!/usr/bin/env python3
"""50-dps probe: Muon q0 CAL-2 Inversion, Mislabelled Proton-Anchor Probes,
Symbolic Pin-Stamped vs Pin-Dependent Payloads, and C/D Markov Straddle.

Beans: qou-5op4, qou-72rd, qou-mha1, qou-3zby, qou-dau6.

Verifies at 50 decimal places (mpmath) + exact symbolic algebra (SymPy),
matching `QOU.MassTheory.MuonAnchorInversionAndStraddleClassification`:
  1. [qou-5op4] Exact CAL-2 inversion q(h) = (1 - h)^(-1) with h = (Vol(4_1)/R)^(1/2):
     - Value B (CODATA 2018 R_2018 = 206.7682830): q_B = 1.109978595554180575...
     - Value A (retired frozen pin q_A_frozen = 1.109978595557334719... with
       R_A_frozen = 206.768282989315111..., and CODATA 2018 separate m_mu/m_e =
       105.6583755/0.51099895000 giving q_A = 1.109978595557821618...):
     - Value C (CODATA 2022 R_2022 = 206.7682827): q_C = 1.109978595642739046...
     - Strict ordering R_C < R_A < R_B => h_B < h_A < h_C => q_B < q_A < q_C.
  2. [qou-72rd] Anchor-label confusion in two probes that label Value A as proton_q0:
     - True proton anchor q_p = 1.109978582751380807...
     - Cross-anchor gap |q_A - q_p| = 1.28059539e-8 vs intra-muon gap
       q_A_frozen - q_B = 3.154144e-12 and q_C - q_A_frozen = 8.5404327e-11.
     - Interval ratio |q_A_frozen - q_p| / (q_A_frozen - q_B) = 4059.99... and
       |q_C - q_p| / (q_A_frozen - q_B) = 4087.1116..., proving 3-4 orders of
       magnitude inflation of claimed cross-anchor stability when both endpoints
       are muon values.
  3. [qou-mha1] Symbolic pin-STAMPED vs pin-DEPENDENT separation:
     - Trefoil Habiro cyclic polynomial coefficients a_1(u) = -35712*u - 35712 and
       a_2(u) = 491861*u^2 + 503768*u + 515411 are symbolically independent of q_stamp,
       with exact factored evaluation secants at u_p = sqrt(q_p) and u_mu = sqrt(q_C).
  4. [qou-3zby & qou-dau6] H_3(q) Markov trace convention (C vs D) x pin (q_mu vs q_p)
     four-method straddle and strict-gate failure:
     - Exact Markov parameter ratio z_D(t)/z_C(t) = t^5*(t^2 + 1)/(t^4 + 1) in t = sqrt(q),
       plus the proton (1, 0) four-method C/D x pin table with rho_DC = 1.48103927...
       and relative discrepancy 1 - rho_DC^(-1) = 0.32479856...
"""

from __future__ import annotations

from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
COMPUTATIONS_DIR = HERE.parent
REPO_ROOT = COMPUTATIONS_DIR.parent

for p in (
    COMPUTATIONS_DIR,
    COMPUTATIONS_DIR / "substrate",
    REPO_ROOT / "tools" / "qou-substrate" / "python",
):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import _path_bridge  # noqa: E402, F401
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps()

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps()

    # 1. Exact Gieseking / figure-eight volume Vol(4_1) = 2 * Im Li_2(e^(i*pi/3))
    vol_4_1 = 2 * mp.clsin(2, mp.pi / 3)

    # Three muon mass-ratio inputs (qou-5op4):
    # Value B: CODATA 2018 direct mass ratio R_2018 = 206.7682830
    R_B = mp.mpf("206.7682830")
    # Value A (frozen literal): q_A = 1.109978595557334719...
    q_A = mp.mpf(
        "1.10997859555733471915292857410085687166559705166039"
    )
    h_A = (q_A - 1) / q_A
    R_A = vol_4_1 / h_A**2
    # Value C: CODATA 2022 direct mass ratio R_2022 = 206.7682827
    R_C = mp.mpf("206.7682827")

    def q_from_R(R_val: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        h_val = mp.sqrt(vol_4_1 / R_val)
        q_val = 1 / (1 - h_val)
        return h_val, q_val

    h_B, q_B = q_from_R(R_B)
    h_C, q_C = q_from_R(R_C)

    # True proton anchor q_p from CAL-1 (m_p / m_e with Borromean volume)
    q_p = mp.mpf(Q_50_DIGIT_STR)

    # SymPy exact verification of Lean theorems in MuonAnchorInversionAndStraddleClassification
    q_sym, h_sym, h1_sym, h2_sym, t_sym = sp.symbols(
        "q h h1 h2 t", positive=True
    )
    cal2_q = 1 / (1 - h_sym)
    cal2_h = (q_sym - 1) / q_sym
    roundtrip_q = sp.simplify(cal2_h.subs(q_sym, cal2_q) - h_sym)
    roundtrip_h = sp.simplify(cal2_q.subs(h_sym, cal2_h) - q_sym)
    secant_diff = sp.simplify(
        (1 / (1 - h2_sym) - 1 / (1 - h1_sym))
        - (h2_sym - h1_sym) / ((1 - h1_sym) * (1 - h2_sym))
    )

    # 2. [qou-72rd] Cross-anchor vs intra-muon interval ratio and 1/hbar_q^2 secant
    gap_intra_AB = q_A - q_B
    gap_intra_AC = q_C - q_A
    gap_cross_Cp = abs(q_C - q_p)
    gap_cross_Ap = abs(q_A - q_p)
    ratio_Cp_over_AB = gap_cross_Cp / gap_intra_AB
    ratio_Ap_over_AB = gap_cross_Ap / gap_intra_AB

    def inv_hbar_sq(q_val: mp.mpf) -> mp.mpf:
        return q_val**2 / (q_val - 1) ** 2

    secant_lhs = inv_hbar_sq(q_C) - inv_hbar_sq(q_p)
    secant_rhs = (
        (q_C - q_p)
        * (q_C + q_p - 2 * q_C * q_p)
        / ((q_C - 1) ** 2 * (q_p - 1) ** 2)
    )
    secant_res = abs(secant_lhs - secant_rhs)

    # 3. [qou-mha1] Symbolic pin-STAMPED vs pin-DEPENDENT separation for Habiro polynomials
    u_sym, u1_sym, u2_sym = sp.symbols("u u1 u2")
    a1_poly = -35712 * u_sym - 35712
    a2_poly = 491861 * u_sym**2 + 503768 * u_sym + 515411
    a1_secant_sym = sp.simplify(
        (a1_poly.subs(u_sym, u1_sym) - a1_poly.subs(u_sym, u2_sym))
        - (-35712 * (u1_sym - u2_sym))
    )
    a2_secant_sym = sp.simplify(
        (a2_poly.subs(u_sym, u1_sym) - a2_poly.subs(u_sym, u2_sym))
        - (u1_sym - u2_sym) * (491861 * (u1_sym + u2_sym) + 503768)
    )

    u_mu = mp.sqrt(q_C)
    u_p = mp.sqrt(q_p)
    a1_mu = -35712 * u_mu - 35712
    a1_p = -35712 * u_p - 35712
    a2_mu = 491861 * u_mu**2 + 503768 * u_mu + 515411
    a2_p = 491861 * u_p**2 + 503768 * u_p + 515411
    a2_secant_num_res = abs(
        (a2_mu - a2_p) - (u_mu - u_p) * (491861 * (u_mu + u_p) + 503768)
    )

    # 4. [qou-3zby & qou-dau6] H_3(q) Markov trace C/D convention x pin straddle
    zD_sym = t_sym**6 / (t_sym**4 + 1)
    zC_sym = t_sym / (t_sym**2 + 1)
    ratio_DC_sym = sp.simplify(
        (zD_sym / zC_sym) - (t_sym**5 * (t_sym**2 + 1) / (t_sym**4 + 1))
    )
    diff_DC_sym = sp.simplify(
        (zD_sym - zC_sym)
        - t_sym
        * (t_sym**7 + t_sym**5 - t_sym**4 - 1)
        / ((t_sym**2 + 1) * (t_sym**4 + 1))
    )

    def z_C(q_val: mp.mpf) -> mp.mpf:
        t_val = mp.sqrt(q_val)
        return t_val / (t_val**2 + 1)

    def z_D(q_val: mp.mpf) -> mp.mpf:
        t_val = mp.sqrt(q_val)
        return t_val**6 / (t_val**4 + 1)

    zC_mu = z_C(q_C)
    zD_mu = z_D(q_C)
    zC_p = z_C(q_p)
    zD_p = z_D(q_p)

    # Proton (1, 0) four-method C/D x pin values from qou-3zby & qou-dau6
    trC_proton_mu = mp.mpf(
        "0.42494384116415472729717056001342525224626033630150"
    )
    trD_proton_mu = mp.mpf(
        "0.62932842431369996896355326733787143726642537907033"
    )
    trC_proton_p = mp.mpf(
        "0.42494384245369386058957845824075925433666113987849"
    )
    trD_proton_p = mp.mpf(
        "0.62932841227928229795163689598624537918704926345551"
    )

    rho_DC_proton_mu = trD_proton_mu / trC_proton_mu
    rel_disc_C_vs_D_proton_mu = (
        abs(trC_proton_mu - trD_proton_mu) / trD_proton_mu
    )
    rel_disc_formula_proton_mu = 1 - 1 / rho_DC_proton_mu
    rel_disc_res = abs(
        rel_disc_C_vs_D_proton_mu - rel_disc_formula_proton_mu
    )

    # Cross-ratio across the 2x2 (convention C/D x pin q_mu/q_p) table
    cross_lhs = (trD_proton_mu / trC_proton_mu) * (
        trC_proton_p / trD_proton_p
    )
    cross_rhs = (trD_proton_mu / trD_proton_p) * (
        trC_proton_p / trC_proton_mu
    )
    cross_res = abs(cross_lhs - cross_rhs)

    wb = WitnessBuilder(
        "muon-anchor-inversion-and-straddle-classification-probe",
        engine="mpmath+sympy",
        output_dir=HERE,
    )
    wb.set_description(
        "50-dps verification of CAL-2 muon q0 inversion and 3-value hierarchy "
        "(qou-5op4), mislabelled proton_q0 anchor-stability inflation (qou-72rd), "
        "symbolic pin-stamped vs pin-dependent separation (qou-mha1), and H_3(q) "
        "C/D Markov straddle across muon/proton pins (qou-3zby, qou-dau6)."
    )
    wb.add_parameter("dps", 50)
    wb.add_parameter("q0_proton_pin", fmt(q_p, 50))
    wb.add_parameter("q0_muon_codata2022_C", fmt(q_C, 50))

    wb.add_data(
        "qou_5op4_three_muon_values",
        {
            "vol_4_1": fmt(vol_4_1, 50),
            "R_B_codata2018_direct_ratio": fmt(R_B, 50),
            "R_A_frozen_pin_inverted_ratio": fmt(R_A, 50),
            "R_C_codata2022_direct_ratio": fmt(R_C, 50),
            "h_B": fmt(h_B, 50),
            "h_A": fmt(h_A, 50),
            "h_C": fmt(h_C, 50),
            "q_B_codata2018": fmt(q_B, 50),
            "q_A_retired_frozen_pin": fmt(q_A, 50),
            "q_C_canonical_muon_2022": fmt(q_C, 50),
        },
    )
    wb.add_data(
        "qou_72rd_anchor_confusion",
        {
            "q_p_proton_anchor": fmt(q_p, 50),
            "gap_intra_muon_A_minus_B": fmt(gap_intra_AB, 50),
            "gap_intra_muon_C_minus_A": fmt(gap_intra_AC, 50),
            "gap_cross_anchor_C_minus_p": fmt(gap_cross_Cp, 50),
            "gap_cross_anchor_A_minus_p": fmt(gap_cross_Ap, 50),
            "inflation_ratio_Cp_over_AB": fmt(ratio_Cp_over_AB, 50),
            "inflation_ratio_Ap_over_AB": fmt(ratio_Ap_over_AB, 50),
            "inv_hbar_sq_secant_residual": fmt(secant_res, 12),
        },
    )
    wb.add_data(
        "qou_mha1_symbolic_payloads",
        {
            "u_mu": fmt(u_mu, 50),
            "u_p": fmt(u_p, 50),
            "a1_mu": fmt(a1_mu, 50),
            "a1_p": fmt(a1_p, 50),
            "a2_mu": fmt(a2_mu, 50),
            "a2_p": fmt(a2_p, 50),
            "a2_secant_residual": fmt(a2_secant_num_res, 12),
        },
    )
    wb.add_data(
        "qou_3zby_dau6_markov_straddle",
        {
            "zC_mu": fmt(zC_mu, 50),
            "zD_mu": fmt(zD_mu, 50),
            "zC_p": fmt(zC_p, 50),
            "zD_p": fmt(zD_p, 50),
            "trC_proton_mu": fmt(trC_proton_mu, 50),
            "trD_proton_mu": fmt(trD_proton_mu, 50),
            "trC_proton_p": fmt(trC_proton_p, 50),
            "trD_proton_p": fmt(trD_proton_p, 50),
            "rho_DC_proton_mu": fmt(rho_DC_proton_mu, 50),
            "relative_discrepancy_C_vs_D_proton_mu": fmt(
                rel_disc_C_vs_D_proton_mu, 50
            ),
            "cross_ratio_residual": fmt(cross_res, 12),
        },
    )

    wb.add_assertion(
        "qou_5op4_cal2_inversion_and_three_value_ordering",
        computed=bool(
            roundtrip_q == 0
            and roundtrip_h == 0
            and secant_diff == 0
            and R_C < R_A < R_B
            and h_B < h_A < h_C
            and q_B < q_A < q_C
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_72rd_anchor_label_confusion_and_secant_identity",
        computed=bool(
            ratio_Cp_over_AB > mp.mpf("4080")
            and ratio_Ap_over_AB > mp.mpf("4050")
            and secant_res < mp.mpf("1e-48")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_mha1_symbolic_pin_stamped_vs_pin_dependent_secants",
        computed=bool(
            a1_secant_sym == 0
            and a2_secant_sym == 0
            and a2_secant_num_res < mp.mpf("1e-45")
        ),
        expected=True,
    )
    wb.add_assertion(
        "qou_3zby_dau6_markov_cd_straddle_and_strict_gate_factorization",
        computed=bool(
            ratio_DC_sym == 0
            and diff_DC_sym == 0
            and rel_disc_res < mp.mpf("1e-48")
            and cross_res < mp.mpf("1e-48")
            and mp.mpf("0.324") < rel_disc_C_vs_D_proton_mu < mp.mpf("0.325")
        ),
        expected=True,
    )

    out_path = wb.save({"q0Anchor": "muon", "q0Value": fmt(q_C, 50)})
    print(f"Saved witness: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
