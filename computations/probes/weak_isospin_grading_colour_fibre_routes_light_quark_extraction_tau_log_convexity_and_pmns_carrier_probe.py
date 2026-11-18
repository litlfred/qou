#!/usr/bin/env python3
"""
Exact 80-dps mpmath + exact rational probe for Round 66 qou-8lxd beans:
  - qou-20sx: Weak-isospin (up/down-type) grading orthogonal to generation winding,
              Gell-Mann-Nishijima Y = 2(Q - T_3), anomaly cancellation, and sin^2(theta_W^0) = 3/8
  - qou-8p1x: Colour SU(3) 3D fibre routes scoreboard (Weyl alt^3 singlet at N=3,
              Bruhat GL(3,F_2) flags = 21, |PG(2,F_2)| = 7, |GL(3,F_2)| = 168,
              tetraplectic codimension 4m - 4 = 0 at m=1 vs 4 at m=2)
  - qou-ha6c: Light quark m_d - m_u stage-1 extraction delta_QCD = Delta_pn + E_EM,
              hyperbolic Coulomb-to-strong bond h/[2]_q = tanh(ln q) = (q^2 - 1)/(q^2 + 1),
              and common-mode shift invariance
  - qou-pvu4: Tau lepton mass gap (m_tau) two-mode additive exponential tower Cauchy-Schwarz
              log-convexity M(0)*M(2) - M(1)^2 = A*B*(r1 - r2)^2 >= 0 vs empirical log-concave bend
  - qou-y0mq: PMNS sector unknot chirality obstruction w(T(2,1)) = 0, zero hyperbolic volume
              Vol(T(2,2k-1)) = 0, and ribbon-framing twist lift w_framed(q, r) = (q - 1) + r
"""

from fractions import Fraction
from pathlib import Path
import sys

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import _path_bridge  # noqa: F401
from witness_base import WitnessBuilder

mp.mp.dps = 80


def main() -> None:
    wb = WitnessBuilder(
        name="weak-isospin-grading-colour-fibre-routes-light-quark-extraction-tau-log-convexity-and-pmns-carrier",
        engine="mpmath",
    )
    wb.description = (
        "Exact 80-dps mpmath and Fraction verification for qou-20sx, qou-8p1x, "
        "qou-ha6c, qou-pvu4, and qou-y0mq under epic qou-8lxd."
    )

    # 1. qou-20sx: Weak-isospin grading, hypercharge Y = 2*(Q - T3), anomalies, and sin^2(theta_W^0) = 3/8
    fermion_states = [
        ("u_L", Fraction(2, 3), Fraction(1, 2), 3),
        ("d_L", Fraction(-1, 3), Fraction(-1, 2), 3),
        ("u_R", Fraction(2, 3), Fraction(0, 1), 3),
        ("d_R", Fraction(-1, 3), Fraction(0, 1), 3),
        ("nu_L", Fraction(0, 1), Fraction(1, 2), 1),
        ("e_L", Fraction(-1, 1), Fraction(-1, 2), 1),
        ("e_R", Fraction(-1, 1), Fraction(0, 1), 1),
    ]
    hypercharges = {name: 2 * (q_el - t3) for name, q_el, t3, _ in fermion_states}
    gmn_residual = sum(
        abs(q_el - (t3 + hypercharges[name] / 2))
        for name, q_el, t3, _ in fermion_states
    )
    n_c = 3
    linear_anomaly = (
        n_c * (2 * hypercharges["u_L"] - hypercharges["u_R"] - hypercharges["d_R"])
        + (2 * hypercharges["nu_L"] - hypercharges["e_R"])
    )
    cubic_anomaly = (
        n_c * (2 * hypercharges["u_L"] ** 3 - hypercharges["u_R"] ** 3 - hypercharges["d_R"] ** 3)
        + (2 * hypercharges["nu_L"] ** 3 - hypercharges["e_R"] ** 3)
    )
    tr_t3_sq = sum(mult * (t3 ** 2) for _, _, t3, mult in fermion_states)
    tr_q_sq = sum(mult * (q_el ** 2) for _, q_el, _, mult in fermion_states)
    sin2_theta_w0 = tr_t3_sq / tr_q_sq

    wb.add_assertion(
        "qou_20sx_gell_mann_nishijima_and_anomaly_cancellation",
        str(int(gmn_residual == 0 and linear_anomaly == 0 and cubic_anomaly == 0)),
        "1",
        tolerance="0",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.standard_generation_hypercharge_anomalies_cancel",
    )
    wb.add_assertion(
        "qou_20sx_unnormalized_weinberg_trace_ratio_three_eighths",
        f"{sin2_theta_w0.numerator}/{sin2_theta_w0.denominator}",
        "3/8",
        tolerance="0",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.weinberg_unnormalized_trace_ratio_three_eighths",
    )

    # 2. qou-8p1x: Colour SU(3) 3D fibre routes scoreboard
    weyl_alt3 = [n * (n - 1) * (n - 2) // 6 for n in (1, 2, 3)]
    q_f2 = 2
    bruhat_flags_s3 = 1 + q_f2 + q_f2 + q_f2 ** 2 + q_f2 ** 2 + q_f2 ** 3
    fano_points = q_f2 ** 2 + q_f2 + 1
    order_gl3_f2 = (q_f2 ** 3 - 1) * (q_f2 ** 3 - q_f2) * (q_f2 ** 3 - q_f2 ** 2)
    tetraplectic_codim_m1 = 4 * 1 - 4
    tetraplectic_codim_m2 = 4 * 2 - 4

    wb.add_assertion(
        "qou_8p1x_colour_su3_scoreboard_exact_counts",
        f"{weyl_alt3}:{bruhat_flags_s3}:{fano_points}:{order_gl3_f2}:{tetraplectic_codim_m1}:{tetraplectic_codim_m2}",
        "[0, 0, 1]:21:7:168:0:4",
        tolerance="0",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.colour_su3_route_scoreboard_identities",
    )

    # 3. qou-ha6c: Light quark m_d - m_u extraction & hyperbolic Coulomb-to-strong bond h/[2]_q = tanh(ln q)
    q0 = mp.mpf("1.1097601919822567262135982475")
    ln_q0 = mp.log(q0)
    h_val = 2 * mp.sinh(ln_q0)
    two_q = 2 * mp.cosh(ln_q0)
    ratio_hyperbolic = h_val / two_q
    ratio_rational = (q0 ** 2 - 1) / (q0 ** 2 + 1)
    bond_identity_diff = abs(ratio_hyperbolic - ratio_rational)

    m_u_ref = Fraction(216, 100)
    m_d_ref = Fraction(467, 100)
    c_shift = Fraction(73, 100)
    diff_before = m_d_ref - m_u_ref
    diff_after = (m_d_ref + c_shift) - (m_u_ref + c_shift)

    wb.add_assertion(
        "qou_ha6c_coulomb_to_strong_bond_hyperbolic_identity",
        mp.nstr(bond_identity_diff, 30),
        "0.0",
        tolerance="1e-70",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.coulomb_to_strong_bond_strict_bounds",
    )
    wb.add_assertion(
        "qou_ha6c_common_mode_shift_invariance_of_md_minus_mu",
        str(int(diff_before == diff_after and (m_u_ref + c_shift) + (m_d_ref + c_shift) == (m_u_ref + m_d_ref) + 2 * c_shift)),
        "1",
        tolerance="0",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.light_quark_difference_common_mode_shift_invariance",
    )

    # 4. qou-pvu4: Tau lepton mass gap two-mode additive tower log-convexity vs empirical log-concave bend
    a_w, b_w, r1, r2 = mp.mpf("1.7"), mp.mpf("2.3"), mp.mpf("2.0"), mp.mpf("5.0")
    m0 = a_w + b_w
    m1 = a_w * r1 + b_w * r2
    m2 = a_w * (r1 ** 2) + b_w * (r2 ** 2)
    cs_det = m0 * m2 - (m1 ** 2)
    lagrange_rhs = a_w * b_w * ((r1 - r2) ** 2)

    m_e_mev = mp.mpf("0.51099895000")
    m_mu_mev = mp.mpf("105.6583755")
    m_tau_mev = mp.mpf("1776.86")
    empirical_bend_ratio = (m_mu_mev / m_e_mev) / (m_tau_mev / m_mu_mev)
    empirical_cs_sign = -1 if (m_e_mev * m_tau_mev - m_mu_mev ** 2) < 0 else 1

    wb.add_assertion(
        "qou_pvu4_two_mode_cauchy_schwarz_lagrange_identity",
        mp.nstr(abs(cs_det - lagrange_rhs), 30),
        "0.0",
        tolerance="1e-70",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.two_mode_tower_log_convexity_and_lepton_bend_exclusion",
    )
    wb.add_assertion(
        "qou_pvu4_empirical_lepton_log_concavity_sign_and_bend",
        f"{empirical_cs_sign}:{int(empirical_bend_ratio > 12)}",
        "-1:1",
        tolerance="0",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.two_mode_tower_log_convexity_and_lepton_bend_exclusion",
    )

    # 5. qou-y0mq: PMNS unknot chirality obstruction w(T(2,1)) = 0 and ribbon-framed lift w_framed(q, r) = (q - 1) + r
    q_ladder = [1, 3, 5]
    unframed_writhes = [q - 1 for q in q_ladder]
    r_twist = 1
    framed_writhes = [(q - 1) + r_twist for q in q_ladder]
    spacings = [framed_writhes[i + 1] - framed_writhes[i] for i in range(len(framed_writhes) - 1)]

    wb.add_assertion(
        "qou_y0mq_pmns_unknot_chirality_and_framed_twist_lift",
        f"{unframed_writhes}:{framed_writhes}:{spacings}",
        "[0, 2, 4]:[1, 3, 5]:[2, 2]",
        tolerance="0",
        source="QOU.Eightfold.WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.pmns_unknot_chirality_obstruction_and_framed_lift",
    )

    wb.data["sin2_theta_w0_exact"] = "3/8"
    wb.data["coulomb_to_strong_bond_at_q0"] = mp.nstr(ratio_hyperbolic, 40)
    wb.data["empirical_lepton_bend_ratio"] = mp.nstr(empirical_bend_ratio, 40)
    wb.save()


if __name__ == "__main__":
    main()
