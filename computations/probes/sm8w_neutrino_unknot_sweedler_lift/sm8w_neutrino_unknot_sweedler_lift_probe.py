#!/usr/bin/env python3
"""EXPLORATORY shape-probe & 80-dps verification for Non-Zero Unknot 0_1 Neutrino Mass Lift,
Sweedler Weak See-Saw Scaling, Dirac vs Majorana Framing, & S_3 Hierarchy Ratios (bean qou-nu01).

Pre-registered in:
  computations/probes/sm8w_neutrino_unknot_sweedler_lift/PREREGISTRATION.md (commit 1a26e9bbb0d)
Lean companion:
  folio/quantum-observable-universe/lean/QOU/StandardModel/NeutrinoUnknotSweedlerMassLift.lean

Discipline:
  - workdps = 80, zero float64, proton anchor q_0 = q_at(80) (q0Anchor = "proton").
  - Zero fitted parameters (CAL-1 m_e and proton-pinned q_0 only).
  - Honest reporting of both order-of-magnitude hits and multi-order-of-magnitude misses against
    PDG-2024 oscillation splittings and Planck cosmological sum bound.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from mpmath import mp, mpf  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    M_E_MEV_STR,
    Q_MP,
    q_at,
    q_int_at,
    vol_4_1_at,
)
from qou_substrate.witness import WitnessBuilder, check_witness_staleness  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def derived_mp_mev(qv: mpf, me_mev: mpf, dps: int = 80) -> mpf:
    qi = mpf(1) / qv
    hv = qv - qi
    hbar_sq = (mpf(1) - qi) ** 2
    vol = vol_4_1_at(dps)
    tr_m = abs((mpf(4) + hv ** 2 - mpf(3) * (hv ** 4) - hv ** 6) / (hv ** 2 + mpf(4)))
    qf3 = (qv ** 2 + mpf(1) + qi ** 2) * (qv + qi)
    return me_mev * (mpf(2) * vol / hbar_sq * (tr_m * qf3 / (qv ** 3)) - mpf(12))


def solve_ew_nv(qv: mpf, dps: int = 80) -> mpf:
    """Unique root of Bring-Schwinger EW cubic in (0, 2 / T_EW) (ElectroweakVevFixedPointDecomposition)."""
    qi = mpf(1) / qv
    hbar_sq = (mpf(1) - qi) ** 2
    q2 = q_int_at(2, q=qv, dps=dps)
    q4 = q_int_at(4, q=qv, dps=dps)
    q6 = q_int_at(6, q=qv, dps=dps)
    q8 = q_int_at(8, q=qv, dps=dps)
    t_ew = qv * (q2 / mpf(2)) * q4 * q6 * q8 + mpf(1) / mp.pi
    h_norm = q2 / (mpf(8) * mp.pi)
    alpha_v = mp.findroot(
        lambda a: mpf(1) / a - (t_ew - a * h_norm * (mpf(1) - hbar_sq * a)),
        mpf(1) / t_ew,
    )
    return mpf(1) / alpha_v


def solve_alpha_em(qv: mpf, dps: int = 80) -> mpf:
    """Bring-Schwinger EM fixed point (AlphaEmT35Linchpin / BringSchwingerNormalizationDerivation)."""
    qi = mpf(1) / qv
    hbar_sq = (mpf(1) - qi) ** 2
    q2 = q_int_at(2, q=qv, dps=dps)
    q9 = q_int_at(9, q=qv, dps=dps)
    q10 = q_int_at(10, q=qv, dps=dps)
    t_em = qv * q9 * q10 + mpf(2) / (mpf(3) * mp.pi)
    h_norm = q2 / (mpf(8) * mp.pi)
    return mp.findroot(
        lambda a: mpf(1) / a - (t_em + a * h_norm * (mpf(1) - hbar_sq * a)),
        mpf(1) / t_em,
    )


def weak_vertex_t35_trace(qv: mpf) -> mpf:
    """WeakVertexT35.weakVertexTrace: q^2 * (q^12 + q^8 - 1) / (q^2 + 1)^2."""
    return (qv ** 2) * (qv ** 12 + qv ** 8 - mpf(1)) / ((qv ** 2 + mpf(1)) ** 2)


def sin_sq_weinberg_substrates(qv: mpf) -> tuple[mpf, mpf]:
    """Two parameter-free substrate sin^2(theta_W) values from TorusLinkElectroweakSchurRatio.lean:
      1. M4 irrep-weighted Wenzl-Higman Schur on (T(2,4) in H_2, T(3,5) in H_3)
      2. Same-rank (T(2,4), T(2,6)) in H_2
    """
    qi = mpf(1) / qv
    y2_triv = (qv ** 4 + qv ** 2 + mpf(1)) / ((qv ** 2 + mpf(1)) ** 2)
    y2_sign = (qv ** 2) / ((qv ** 2 + mpf(1)) ** 2)
    qi2 = qv + qi
    qi3 = qv ** 2 + mpf(1) + qi ** 2
    c2_triv = qv * qi2
    c2_sign = qi * qi2
    c3_triv = (qv ** 3) * qi2 * qi3
    c3_std = qi3
    y3_triv = (qv ** 4 + mpf(1)) / ((qv ** 2 + mpf(1)) ** 2)
    y3_std = (qv ** 2) / ((qv ** 2 + mpf(1)) ** 2)

    m4_t24 = c2_triv * y2_triv * (qv ** 4) + c2_sign * y2_sign * (qi ** 4)
    m4_t35 = c3_triv * y3_triv * (qv ** 10) - c3_std * y3_std
    sin2_m4 = mpf(1) - (m4_t24 / m4_t35) ** 2

    ratio_24_26 = (qv ** 2) * (qv ** 10 + qv ** 8 + qv ** 6 + mpf(1)) / (
        qv ** 14 + qv ** 12 + qv ** 10 + mpf(1)
    )
    sin2_24_26 = mpf(1) - ratio_24_26 ** 2
    return sin2_m4, sin2_24_26


def classify_scale(m_ev: mpf, sqrt_dm21_ev: mpf, sqrt_dm32_ev: mpf) -> str:
    ratio_atm = m_ev / sqrt_dm32_ev
    ratio_sol = m_ev / sqrt_dm21_ev
    if mpf("0.2") <= ratio_atm <= mpf(5):
        return "ORDER_OF_MAGNITUDE_HIT_ATMOSPHERIC"
    if mpf("0.2") <= ratio_sol <= mpf(5):
        return "ORDER_OF_MAGNITUDE_HIT_SOLAR"
    if m_ev > mpf(5) * sqrt_dm32_ev:
        return "MISS_TOO_HEAVY"
    return "MISS_OVER_SUPPRESSED"


def record_candidate(
    label: str,
    formula: str,
    m_ev: mpf,
    sqrt_dm21_ev: mpf,
    sqrt_dm32_ev: mpf,
) -> dict[str, str]:
    m_mev_milli = m_ev * mpf("1e3")
    return {
        "label": label,
        "formula": formula,
        "m_nu_eV": fmt50(m_ev),
        "m_nu_meV": fmt50(m_mev_milli),
        "ratio_over_sqrt_dm32": fmt50(m_ev / sqrt_dm32_ev),
        "ratio_over_sqrt_dm21": fmt50(m_ev / sqrt_dm21_ev),
        "log10_ratio_atm": fmt50(mp.log10(m_ev / sqrt_dm32_ev)),
        "classification": classify_scale(m_ev, sqrt_dm21_ev, sqrt_dm32_ev),
    }


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        h0 = q0 - qi0
        hbar_q = mpf(1) - qi0
        s0 = q0 ** 2 - mpf(1)

        me_mev = mpf(M_E_MEV_STR)
        me_ev = me_mev * mpf("1e6")
        mp_mev = derived_mp_mev(q0, me_mev, dps=80)
        mp_ev = mp_mev * mpf("1e6")

        nv_q0 = solve_ew_nv(q0, dps=80)
        vew_ev = nv_q0 * mp_ev
        vew_gev = vew_ev * mpf("1e-9")

        alpha_em_q0 = solve_alpha_em(q0, dps=80)
        sin2_m4, sin2_24_26 = sin_sq_weinberg_substrates(q0)
        alpha_w_m4 = alpha_em_q0 / sin2_m4
        alpha_w_24_26 = alpha_em_q0 / sin2_24_26
        w_t35_q0 = weak_vertex_t35_trace(q0)

        # Post-evaluation empirical comparison constants (PDG-2024 & Planck 2018 + BAO)
        dm21_sq_pdg = mpf("7.53e-5")      # eV^2
        dm32_sq_pdg = mpf("2.453e-3")     # eV^2
        sqrt_dm21_pdg = mp.sqrt(dm21_sq_pdg)
        sqrt_dm32_pdg = mp.sqrt(dm32_sq_pdg)
        ratio_dm_pdg = dm21_sq_pdg / dm32_sq_pdg
        planck_sum_bound_ev = mpf("0.12")

        wb = WitnessBuilder(
            "sm8w-neutrino-unknot-sweedler-lift",
            engine="mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps probe of non-zero unknot 0_1 neutrino mass lift via Sweedler "
            "(q_0^2 - 1)^k and 2-loop T(3,5) weak self-energy dressing, dimension-5 Weinberg "
            "v_EW^2 / M_UV(q_0) see-saw scales, 2-loop (alpha_W/pi)^2 m_e (q_0^2 - 1)^k scales, "
            "Sweedler S^2(X) = -X order-4 antipode / Weinberg (LH)^2 singlet invariance, and "
            "3-generation S_3 -> S_2 NH vs IH hierarchy ratios (qou-nu01)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("s0_q0_sq_minus_1_50dps", fmt50(s0))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ── 1. Verify Lean algebraic theorems at 80 dps ──────────────────────────
        # (a) Charged-current self-energy sandwich E * diag(0, m_e) * F = m_e * Pu
        f_mat = mp.matrix([[mpf(0), mpf(0)], [mpf(1), mpf(0)]])
        e_mat = mp.matrix([[mpf(0), mpf(1)], [mpf(0), mpf(0)]])
        d_bare = mp.matrix([[mpf(0), mpf(0)], [mpf(0), me_ev]])
        pu_mat = mp.matrix([[mpf(1), mpf(0)], [mpf(0), mpf(0)]])
        se_mat = e_mat * d_bare * f_mat
        fdf_mat = f_mat * d_bare * f_mat
        ede_mat = e_mat * d_bare * e_mat
        se_err = max(
            abs(se_mat[i, j] - me_ev * pu_mat[i, j])
            + abs(fdf_mat[i, j])
            + abs(ede_mat[i, j])
            for i in range(2)
            for j in range(2)
        )
        wb.add_assertion(
            "lepton_self_energy_projects_purely_onto_neutral_nu_slot",
            computed=se_err,
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="NeutrinoUnknotSweedlerMassLift.lepton_selfEnergy_projects_neutral_slot",
        )

        # (b) Sweedler H_4 antipode S^2(X) = -X, S^4 = I, and G*a*G = S^2(a) on 4D basis {1, G, X, GX}
        # In basis {1, G, X, GX}: S(1)=1, S(G)=G, S(X)=-GX, S(GX)=X
        s_mat4 = mp.matrix([
            [mpf(1), mpf(0), mpf(0), mpf(0)],
            [mpf(0), mpf(1), mpf(0), mpf(0)],
            [mpf(0), mpf(0), mpf(0), mpf(1)],
            [mpf(0), mpf(0), -mpf(1), mpf(0)],
        ])
        s2_mat4 = s_mat4 * s_mat4
        s4_mat4 = s2_mat4 * s2_mat4
        conj_g_mat4 = mp.matrix([
            [mpf(1), mpf(0), mpf(0), mpf(0)],
            [mpf(0), mpf(1), mpf(0), mpf(0)],
            [mpf(0), mpf(0), -mpf(1), mpf(0)],
            [mpf(0), mpf(0), mpf(0), -mpf(1)],
        ])
        nak_mat4 = mp.matrix([
            [mpf(1), mpf(0), mpf(0), mpf(0)],
            [mpf(0), -mpf(1), mpf(0), mpf(0)],
            [mpf(0), mpf(0), -mpf(1), mpf(0)],
            [mpf(0), mpf(0), mpf(0), mpf(1)],
        ])
        id4 = mp.eye(4)
        sweedler_err = max(
            abs(s2_mat4[i, j] - conj_g_mat4[i, j]) + abs(s4_mat4[i, j] - id4[i, j])
            for i in range(4)
            for j in range(4)
        )
        # Also verify S^2(X) != X (gap = 2) and nakayama(G) != S^2(G) (gap = 2)
        s2_x_gap = abs(s2_mat4[2, 2] - mpf(1))
        nak_g_gap = abs(nak_mat4[1, 1] - s2_mat4[1, 1])
        wb.add_assertion(
            "sweedler_antipode_order_four_pivotal_G_and_non_unimodularity",
            computed=sweedler_err + abs(s2_x_gap - mpf(2)) + abs(nak_g_gap - mpf(2)),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="NeutrinoUnknotSweedlerMassLift.sweedler_antipode_sq_eq_conj_G_and_pow_four",
        )

        # (c) Weinberg (LH)^2 4-fold Sweedler coproduct invariance & neutral Higgs vev projection
        l1 = [mpf("1.7"), -mpf("0.9")]
        h1 = [-mpf("0.4"), mpf("2.3")]
        l2 = [-mpf("1.1"), mpf("0.6")]
        h2 = [mpf("0.8"), -mpf("1.5")]

        def ew_eps(u: list[mpf], v: list[mpf]) -> mpf:
            return u[0] * v[1] - u[1] * v[0]

        def wein_op(a: list[mpf], b: list[mpf], c: list[mpf], d: list[mpf]) -> mpf:
            return ew_eps(a, b) * ew_eps(c, d)

        def act_g(u: list[mpf]) -> list[mpf]:
            return [u[0], -u[1]]

        def act_x(u: list[mpf]) -> list[mpf]:
            return [mpf(0), h0 * u[0]]

        lin_g_err = abs(ew_eps(act_g(l1), act_g(h1)) + ew_eps(l1, h1))
        lin_x_err = abs(ew_eps(act_x(l1), h1) + ew_eps(act_g(l1), act_x(h1)))
        wein_g_err = abs(
            wein_op(act_g(l1), act_g(h1), act_g(l2), act_g(h2)) - wein_op(l1, h1, l2, h2)
        )
        wein_x_err = abs(
            wein_op(act_x(l1), h1, l2, h2)
            + wein_op(act_g(l1), act_x(h1), l2, h2)
            + wein_op(act_g(l1), act_g(h1), act_x(l2), h2)
            + wein_op(act_g(l1), act_g(h1), act_g(l2), act_x(h2))
        )
        h_vev = [mpf(0), vew_ev]
        wein_vev_err = abs(
            wein_op(l1, h_vev, l2, h_vev) - (vew_ev ** 2) * l1[0] * l2[0]
        ) + abs(wein_op([mpf(0), l1[1]], h_vev, l2, h_vev))
        wb.add_assertion(
            "weinberg_dim5_sweedler_4fold_coproduct_invariance_and_vev_selectivity",
            computed=lin_g_err + lin_x_err + wein_g_err + wein_x_err + wein_vev_err / (vew_ev ** 2),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="NeutrinoUnknotSweedlerMassLift.weinberg_quadratic_singlet_sweedler_invariant_and_vev",
        )

        # (d) S_3 -> S_2 eigensystem, det factorization, and NH < IH mass-sum theorem
        a_test, b_test, eps_test = mpf("0.003"), mpf("0.017"), mpf("0.0014")
        j3 = mp.ones(3, 3)
        b12 = mp.matrix([
            [mpf(1), mpf(1), -mpf(2)],
            [mpf(1), mpf(1), -mpf(2)],
            [-mpf(2), -mpf(2), mpf(4)],
        ])
        m_s3 = a_test * mp.eye(3) + b_test * j3 + eps_test * b12
        det_exact = a_test * (a_test + mpf(6) * eps_test) * (a_test + mpf(3) * b_test)
        tr_exact = a_test + (a_test + mpf(6) * eps_test) + (a_test + mpf(3) * b_test)
        tr_computed = m_s3[0, 0] + m_s3[1, 1] + m_s3[2, 2]
        wb.add_assertion(
            "s3_neutral_mass_trace_and_det_factorization",
            computed=abs(mp.det(m_s3) - det_exact) + abs(tr_computed - tr_exact),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="NeutrinoUnknotSweedlerMassLift.s3NeutralMass_spectrum_trace_det",
        )

        # ── 2. Pre-registered candidate scale evaluations (Families A, B, C, D) ──
        family_a: list[dict[str, str]] = []
        family_b: list[dict[str, str]] = []
        for k_pow in (8, 10, 12, 14, 16):
            m_a = me_ev * (s0 ** k_pow)
            m_b = me_ev * (w_t35_q0 ** 2) * (s0 ** k_pow)
            family_a.append(
                record_candidate(
                    f"A_k{k_pow}",
                    f"m_e * (q_0^2 - 1)^{k_pow}",
                    m_a,
                    sqrt_dm21_pdg,
                    sqrt_dm32_pdg,
                )
            )
            family_b.append(
                record_candidate(
                    f"B_T35_k{k_pow}",
                    f"m_e * W_T35(q_0)^2 * (q_0^2 - 1)^{k_pow}",
                    m_b,
                    sqrt_dm21_pdg,
                    sqrt_dm32_pdg,
                )
            )

        # Verify strict anti-monotonicity across k = 8, 10, 12, 14, 16 (since 0 < q_0^2 - 1 < 1)
        m_a_vals = [me_ev * (s0 ** k_pow) for k_pow in (8, 10, 12, 14, 16)]
        monotone_ok = all(m_a_vals[idx + 1] < m_a_vals[idx] for idx in range(len(m_a_vals) - 1))
        wb.add_assertion(
            "sweedler_mass_lift_strictly_positive_and_strictly_decreasing_in_k",
            computed=mpf(0) if (monotone_ok and m_a_vals[-1] > mpf(0)) else mpf(1),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="NeutrinoUnknotSweedlerMassLift.sweedlerMassLift_pos & sweedlerMassLift_strictAnti",
        )

        # Family C: Weinberg see-saw v_EW(q_0)^2 / M_UV(q_0)
        family_c: list[dict[str, str]] = []
        for two_m in (16, 18, 20, 22):
            m_uv = mp_ev / (s0 ** two_m)
            m_c = (vew_ev ** 2) / m_uv
            entry = record_candidate(
                f"C_Sw_{two_m}",
                f"v_EW(q_0)^2 / [m_p(q_0) * (q_0^2 - 1)^(-{two_m})]",
                m_c,
                sqrt_dm21_pdg,
                sqrt_dm32_pdg,
            )
            entry["M_UV_GeV"] = fmt50(m_uv * mpf("1e-9"))
            family_c.append(entry)

        for r_pow in (5, 6, 7, 8):
            m_uv = mp_ev * (nv_q0 ** r_pow)
            m_c = (vew_ev ** 2) / m_uv
            entry = record_candidate(
                f"C_Nv_r{r_pow}",
                f"v_EW(q_0)^2 / [m_p(q_0) * N_v(q_0)^{r_pow}] = m_p(q_0) * N_v(q_0)^(2-{r_pow})",
                m_c,
                sqrt_dm21_pdg,
                sqrt_dm32_pdg,
            )
            entry["M_UV_GeV"] = fmt50(m_uv * mpf("1e-9"))
            family_c.append(entry)

        m_uv_exp = me_ev * mp.exp(mpf(1) / (mpf(2) * alpha_em_q0))
        m_c_exp = (vew_ev ** 2) / m_uv_exp
        entry_exp = record_candidate(
            "C_Exp_half_alphaEM_inv",
            "v_EW(q_0)^2 / [m_e * exp(1 / (2 * alpha_EM(q_0)))]",
            m_c_exp,
            sqrt_dm21_pdg,
            sqrt_dm32_pdg,
        )
        entry_exp["M_UV_GeV"] = fmt50(m_uv_exp * mpf("1e-9"))
        family_c.append(entry_exp)

        # Family D: 2-loop (alpha_W / pi)^2 * m_e * (q_0^2 - 1)^k
        family_d_m4: list[dict[str, str]] = []
        family_d_24_26: list[dict[str, str]] = []
        loop_m4 = (alpha_w_m4 / mp.pi) ** 2
        loop_24_26 = (alpha_w_24_26 / mp.pi) ** 2
        for k_pow in (0, 2, 4, 6, 8, 10, 12, 14, 16):
            tag = "control" if k_pow < 8 else "primary"
            m_d1 = loop_m4 * me_ev * (s0 ** k_pow)
            m_d2 = loop_24_26 * me_ev * (s0 ** k_pow)
            row1 = record_candidate(
                f"D_M4_k{k_pow}_{tag}",
                f"(alpha_W^M4 / pi)^2 * m_e * (q_0^2 - 1)^{k_pow}",
                m_d1,
                sqrt_dm21_pdg,
                sqrt_dm32_pdg,
            )
            row2 = record_candidate(
                f"D_24_26_k{k_pow}_{tag}",
                f"(alpha_W^(24/26) / pi)^2 * m_e * (q_0^2 - 1)^{k_pow}",
                m_d2,
                sqrt_dm21_pdg,
                sqrt_dm32_pdg,
            )
            family_d_m4.append(row1)
            family_d_24_26.append(row2)

        # ── 3. Family E: 3-generation S_3 -> S_2 splitting ratios & hierarchy sums ──
        spurion_candidates = [
            ("spurion_s0_pow1", "2*eps/b = (q_0^2 - 1)", s0),
            ("spurion_s0_pow2", "2*eps/b = (q_0^2 - 1)^2", s0 ** 2),
            ("spurion_hbar_pow1", "2*eps/b = hbar_q = 1 - q_0^-1", hbar_q),
            ("spurion_hbar_pow2", "2*eps/b = hbar_q^2 = (1 - q_0^-1)^2", hbar_q ** 2),
        ]
        family_e_ratios: list[dict[str, str]] = []
        for name, formula, rho in spurion_candidates:
            r_21_31 = rho ** 2
            r_21_32 = (rho ** 2) / (mpf(1) - rho ** 2)
            family_e_ratios.append({
                "name": name,
                "formula": formula,
                "dm21_over_dm31": fmt50(r_21_31),
                "dm21_over_dm32": fmt50(r_21_32),
                "ratio_to_PDG_0p03070": fmt50(r_21_32 / ratio_dm_pdg),
                "rel_diff_vs_PDG": fmt50((r_21_32 - ratio_dm_pdg) / ratio_dm_pdg),
            })

        # Minimal NH vs Minimal IH cosmological sum & TBM 0nu2beta benchmark
        # Evaluate at (1) PDG oscillation benchmark, (2) A_k12 = m_e (q_0^2 - 1)^12 + spurion_s0_pow1,
        # and (3) B_T35_k12 = m_e W_T35^2 (q_0^2 - 1)^12 + spurion_s0_pow1
        def hierarchy_observables(
            tag: str, m_atm_ev: mpf, r_sol_over_atm: mpf
        ) -> dict[str, str | bool]:
            # Minimal NH: m1 = 0, m3 = m_atm, m2 = m_atm * sqrt(r / (1 + r)) so dm21^2 / dm32^2 = r
            m2_nh = m_atm_ev * mp.sqrt(r_sol_over_atm / (mpf(1) + r_sol_over_atm))
            m3_nh = mp.sqrt(m_atm_ev ** 2 + m2_nh ** 2)
            sum_nh = m2_nh + m3_nh
            # Minimal IH: m3 = 0, m2 = m3_nh (matched atmospheric |dm31|^2 = m3_nh^2), m1 = sqrt(m2^2 - m2_nh^2)
            n2_ih = m3_nh
            n1_ih = mp.sqrt(n2_ih ** 2 - m2_nh ** 2)
            sum_ih = n1_ih + n2_ih
            # TBM Majorana benchmark |m_bb| (u_e1^2 = 2/3, u_e2^2 = 1/3, u_e3^2 = 0, CP-even/+ vs CP-odd/-)
            mbb_nh = (mpf(1) / mpf(3)) * m2_nh
            mbb_ih_max = (mpf(2) / mpf(3)) * n1_ih + (mpf(1) / mpf(3)) * n2_ih
            mbb_ih_min = abs((mpf(2) / mpf(3)) * n1_ih - (mpf(1) / mpf(3)) * n2_ih)
            return {
                "scenario": tag,
                "m2_NH_meV": fmt50(m2_nh * mpf("1e3")),
                "m3_NH_meV": fmt50(m3_nh * mpf("1e3")),
                "sum_m_nu_NH_eV": fmt50(sum_nh),
                "NH_passes_Planck_0p12eV": bool(sum_nh < planck_sum_bound_ev),
                "n1_IH_meV": fmt50(n1_ih * mpf("1e3")),
                "n2_IH_meV": fmt50(n2_ih * mpf("1e3")),
                "sum_m_nu_IH_eV": fmt50(sum_ih),
                "IH_passes_Planck_0p12eV": bool(sum_ih < planck_sum_bound_ev),
                "NH_sum_strictly_less_than_IH_sum": bool(sum_nh < sum_ih),
                "m_bb_TBM_NH_meV": fmt50(mbb_nh * mpf("1e3")),
                "m_bb_TBM_IH_range_min_meV": fmt50(mbb_ih_min * mpf("1e3")),
                "m_bb_TBM_IH_range_max_meV": fmt50(mbb_ih_max * mpf("1e3")),
            }

        r_s0_sq = (s0 ** 2) / (mpf(1) - s0 ** 2)
        m_a12_ev = me_ev * (s0 ** 12)
        m_b12_ev = me_ev * (w_t35_q0 ** 2) * (s0 ** 12)

        hierarchy_table = [
            hierarchy_observables("PDG2024_empirical_benchmark", sqrt_dm32_pdg, ratio_dm_pdg),
            hierarchy_observables("Substrate_A_k12_with_s0_spurion", m_a12_ev, r_s0_sq),
            hierarchy_observables("Substrate_B_T35_k12_with_s0_spurion", m_b12_ev, r_s0_sq),
        ]

        wb.add_assertion(
            "nh_mass_sum_strictly_less_than_ih_mass_sum_across_all_scenarios",
            computed=mpf(0)
            if all(bool(row["NH_sum_strictly_less_than_IH_sum"]) for row in hierarchy_table)
            else mpf(1),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="NeutrinoUnknotSweedlerMassLift.nh_mass_sum_lt_ih_of_matched_splittings",
        )

        # Collect all order-of-magnitude hits vs misses across Families A-D
        all_candidates = family_a + family_b + family_c + family_d_m4 + family_d_24_26
        hits_atm = [c["label"] for c in all_candidates if c["classification"] == "ORDER_OF_MAGNITUDE_HIT_ATMOSPHERIC"]
        hits_sol = [c["label"] for c in all_candidates if c["classification"] == "ORDER_OF_MAGNITUDE_HIT_SOLAR"]

        wb.add_data(
            "substrate_derived_inputs_80dps",
            {
                "q0_proton": fmt50(q0),
                "hbar_q": fmt50(hbar_q),
                "s0_q0_sq_minus_1": fmt50(s0),
                "m_e_eV_CAL1": fmt50(me_ev),
                "m_p_derived_MeV": fmt50(mp_mev),
                "N_v_derived": fmt50(nv_q0),
                "v_EW_derived_GeV": fmt50(vew_gev),
                "alpha_EM_derived_inv": fmt50(mpf(1) / alpha_em_q0),
                "sin2_thetaW_M4_T24_T35": fmt50(sin2_m4),
                "sin2_thetaW_H2_T24_T26": fmt50(sin2_24_26),
                "alpha_W_M4": fmt50(alpha_w_m4),
                "alpha_W_24_26": fmt50(alpha_w_24_26),
                "W_T35_q0": fmt50(w_t35_q0),
                "W_T35_q0_sq": fmt50(w_t35_q0 ** 2),
            },
        )
        wb.add_data(
            "empirical_comparison_targets_post_eval",
            {
                "PDG2024_dm21_sq_eV2": "7.53e-5",
                "PDG2024_abs_dm32_sq_eV2": "2.453e-3",
                "PDG2024_sqrt_dm21_meV": fmt50(sqrt_dm21_pdg * mpf("1e3")),
                "PDG2024_sqrt_abs_dm32_meV": fmt50(sqrt_dm32_pdg * mpf("1e3")),
                "PDG2024_dm21_over_abs_dm32": fmt50(ratio_dm_pdg),
                "Planck2018_BAO_sum_m_nu_upper_eV": "0.12",
            },
        )
        wb.add_data("family_A_sweedler_pure_ladder", family_a)
        wb.add_data("family_B_t35_two_vertex_sweedler_ladder", family_b)
        wb.add_data("family_C_weinberg_seesaw_scales", family_c)
        wb.add_data("family_D_two_loop_alphaW_M4", family_d_m4)
        wb.add_data("family_D_two_loop_alphaW_24_26", family_d_24_26)
        wb.add_data("family_E_s3_spurion_splitting_ratios", family_e_ratios)
        wb.add_data("family_E_nh_vs_ih_observables", hierarchy_table)
        wb.add_data(
            "honest_summary",
            {
                "atmospheric_order_of_magnitude_hits": hits_atm,
                "solar_order_of_magnitude_hits": hits_sol,
                "total_candidates_evaluated": len(all_candidates),
                "note": (
                    "All pre-registered candidates evaluated at 80 dps with zero fitted parameters. "
                    "Both natural order-of-magnitude hits (e.g. k=12 Sweedler / T(3,5)-dressed "
                    "scales near 12-17 meV vs PDG 8.68-49.5 meV) and multi-order-of-magnitude "
                    "misses (e.g. k=8 too heavy at ~4.3 eV, k=16 over-suppressed at ~36 ueV, and "
                    "compounded (alpha_W/pi)^2 * (q_0^2-1)^k for k>=8 over-suppressed by ~10^-5) "
                    "are reported without post-hoc selection."
                ),
            },
        )

        out_path = wb.save({"q0Anchor": "proton"})
        chk = check_witness_staleness(str(out_path))
        print("=== SM8W Neutrino Unknot Sweedler Lift & Framing Probe (80 dps) ===")
        print(f"q_0 (proton)     = {mp.nstr(q0, 20)}")
        print(f"s_0 = q_0^2 - 1  = {mp.nstr(s0, 15)}")
        print(f"W_T35(q_0)^2     = {mp.nstr(w_t35_q0 ** 2, 15)}")
        print(f"v_EW(q_0)        = {mp.nstr(vew_gev, 12)} GeV (N_v = {mp.nstr(nv_q0, 12)})")
        print(f"PDG targets      : sqrt(dm21^2) = {mp.nstr(sqrt_dm21_pdg * mpf('1e3'), 6)} meV, "
              f"sqrt(|dm32^2|) = {mp.nstr(sqrt_dm32_pdg * mpf('1e3'), 6)} meV, "
              f"ratio = {mp.nstr(ratio_dm_pdg, 6)}")
        print("\n--- Family A & B: m_e * (q_0^2 - 1)^k and T(3,5)^2-dressed ---")
        for ra, rb in zip(family_a, family_b):
            print(f"  {ra['label']:8s}: {mp.nstr(mpf(ra['m_nu_meV']), 6):>12s} meV [{ra['classification']}] | "
                  f"{rb['label']:11s}: {mp.nstr(mpf(rb['m_nu_meV']), 6):>12s} meV [{rb['classification']}]")
        print("\n--- Family C: Weinberg v_EW(q_0)^2 / M_UV(q_0) ---")
        for rc in family_c:
            print(f"  {rc['label']:22s}: {mp.nstr(mpf(rc['m_nu_meV']), 6):>14s} meV "
                  f"(M_UV = {mp.nstr(mpf(rc['M_UV_GeV']), 5):>11s} GeV) [{rc['classification']}]")
        print("\n--- Family D: 2-loop (alpha_W^M4 / pi)^2 * m_e * (q_0^2 - 1)^k ---")
        for rd in family_d_m4:
            print(f"  {rd['label']:20s}: {mp.nstr(mpf(rd['m_nu_meV']), 6):>14s} meV [{rd['classification']}]")
        print("\n--- Family E: S_3 -> S_2 Spurion Ratios dm21^2 / dm32^2 (PDG = 0.030697) ---")
        for re_row in family_e_ratios:
            print(f"  {re_row['name']:18s}: dm21/dm32 = {mp.nstr(mpf(re_row['dm21_over_dm32']), 6):>12s} "
                  f"(ratio/PDG = {mp.nstr(mpf(re_row['ratio_to_PDG_0p03070']), 5)})")
        print("\n--- NH vs IH Sums & TBM |m_bb| ---")
        for hrow in hierarchy_table:
            print(f"  {hrow['scenario']:35s}: sum_NH = {mp.nstr(mpf(str(hrow['sum_m_nu_NH_eV'])), 5)} eV "
                  f"< sum_IH = {mp.nstr(mpf(str(hrow['sum_m_nu_IH_eV'])), 5)} eV | "
                  f"m_bb(NH)={mp.nstr(mpf(str(hrow['m_bb_TBM_NH_meV'])), 4)} meV, "
                  f"m_bb(IH)=[{mp.nstr(mpf(str(hrow['m_bb_TBM_IH_range_min_meV'])), 4)}, "
                  f"{mp.nstr(mpf(str(hrow['m_bb_TBM_IH_range_max_meV'])), 4)}] meV")
        print(f"\nWitness saved to {out_path.name}; staleness check: {chk}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
