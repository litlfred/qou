#!/usr/bin/env python3
"""80-dps pre-registered probe for the W6 Inhomogeneous Lepton Loop Resolvent,
the R = tau_e / hbar_q^2 = 70.4037 carrier split, and zero-parameter mechanisms
for the +211.206 ppb proton-pinned m_mu / m_e offset & m_tau / m_e check.

Beans: qou-91w7, qou-6gf9, qou-mk7u (Q-Gap-2 / W6).
Lean companion: folio/quantum-observable-universe/lean/QOU/Observations/InhomogeneousLeptonLoopResolvent.lean.
Pre-registration: computations/probes/w6_inhomogeneous_lepton_resolvent/PREREGISTRATION.md.
Zero fitting, zero float64; proton pin q_0 = q_at(80).
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

from mpmath import mp, mpc, mpf  # noqa: E402
from q_parameter import q_muon_at  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import Q_MP, q_at, vol_4_1_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def q_int(qv: mpf, n: int) -> mpf:
    """Quantum integer [n]_q = (q^n - q^-n) / (q - q^-1)."""
    qn = qv ** n
    qni = mpf(1) / qn
    return (qn - qni) / (qv - mpf(1) / qv)


def form_b_alpha_q(qv: mpf) -> mpf:
    """Derived Bring-surface Form-B fine-structure coupling (zero CODATA alpha):
    alpha_q(q) = (q [9]_q [10]_q + 2 / (3 pi))^-1.
    """
    inv_alpha = qv * q_int(qv, 9) * q_int(qv, 10) + mpf(2) / (mpf(3) * mp.pi)
    return mpf(1) / inv_alpha


def y3_weight(qv: mpf) -> mpf:
    return mpf(1) - mpf(2) / ((qv + mpf(1) / qv) ** 2)


def y21_weight(qv: mpf) -> mpf:
    return mpf(1) / ((qv + mpf(1) / qv) ** 2)


def tau_electron(qv: mpf) -> mpf:
    """Convention-D trace of beta_e = sigma_0 sigma_1 sigma_0 in H_3(q)."""
    return (qv ** 3) * y3_weight(qv)


def fig8_mat21_trace_direct(qv: mpf) -> mpf:
    """Direct 2x2 matrix trace of (r21a(q) * inv21(r21b(q)))^2 in H_3(q)."""
    qi = mpf(1) / qv
    r21a = mp.matrix([[qv, mpf(1)], [mpf(0), -qi]])
    inv_r21b = mp.matrix([[-qv, mpf(0)], [mpf(1), qi]])
    step = r21a * inv_r21b
    mat = step * step
    return mat[0, 0] + mat[1, 1]


def tau_figure_eight(qv: mpf) -> mpf:
    """Closed-form Convention-D trace of beta_mu = (sigma_0 sigma_1^-1)^2 in H_3(q)."""
    hv = qv - mpf(1) / qv
    return ((hv ** 4) + mpf(3) * (hv ** 2) + mpf(1)) / ((qv + mpf(1) / qv) ** 2)


def tau_t27_h2(qv: mpf) -> mpf:
    """Convention-D trace of torus knot T(2,7) = sigma_0^7 in H_2(q)
    (y_{(2)}^D = 1 - q^2/(q^2+1)^2, y_{(1,1)}^D = q^2/(q^2+1)^2).
    """
    qi = mpf(1) / qv
    y11 = (qv ** 2) / ((qv ** 2 + mpf(1)) ** 2)
    y2 = mpf(1) - y11
    return y2 * (qv ** 7) + y11 * (-(qi ** 7))


def q_volume_rearranged(zv: mpc, qv: mpf) -> mpc:
    """Convergent Lambert rearrangement of G(z; q) = sum_{n>=1} z^n / (1 - q^-n)^2:
    G(z; q) = sum_{m>=0} (m + 1) z q^-m / (1 - z q^-m).
    """
    return mp.nsum(
        lambda m: (m + mpf(1)) * zv * (qv ** (-m)) / (mpf(1) - zv * (qv ** (-m))),
        [0, mp.inf],
    )


def bloch_wigner(zv: mpc) -> mpf:
    """Bloch-Wigner dilogarithm D(z) = Im(Li_2(z)) + arg(1 - z) * ln|z|."""
    return mp.im(mp.polylog(2, zv)) + mp.arg(mpf(1) - zv) * mp.log(abs(zv))


def solve_z_5_2() -> mpc:
    """Unique root with Im(z) > 0 of z^3 - z^2 + 1 = 0 (ideal triangulation of 5_2)."""
    z = mpc(mpf(7) / mpf(8), mpf(3) / mpf(4))
    for _ in range(30):
        f = (z ** 3) - (z ** 2) + mpf(1)
        df = mpf(3) * (z ** 2) - mpf(2) * z
        z = z - f / df
    return z


def murakami_deformed_action_4_1(u_val: mpf) -> dict[str, mpf]:
    """Murakami 2011 ([murakami-h2011] Thm. 1.3) real off-root-of-unity deformation
    of the 4_1 colored Jones asymptotic at xi = 2*pi*i + u for 0 < u < ln((3+sqrt(5))/2).

    With cosh(u) - 1/2 in (1/2, 1), phi(u) = -i * theta(u) where theta(u) = arccos(cosh(u) - 1/2)
    selects the hyperbolic branch S(0) = +i Vol(4_1):
      S(u) = Li_2(e^{u - phi(u)}) - Li_2(e^{u + phi(u)}) - u * phi(u) = i * Sigma(u),
      Re(S(u) / (2*pi*i + u)) = 2 * pi * Sigma(u) / (4 * pi^2 + u^2).
    """
    mv = mp.exp(u_val)
    mvi = mpf(1) / mv
    wv = mv + mvi - mpf(2)
    theta = mp.acos(mp.cosh(u_val) - mpf(1) / mpf(2))
    phi = mpc(mpf(0), -theta)
    s_complex = (
        mp.polylog(2, mp.exp(u_val - phi))
        - mp.polylog(2, mp.exp(u_val + phi))
        - u_val * phi
    )
    xi = mpc(u_val, mpf(2) * mp.pi)
    eff_vol_equiv = mpf(2) * mp.pi * mp.re(s_complex / xi)
    disc = (mv + mvi + mpf(1)) * (mv + mvi - mpf(3))
    tors_abs_sq = mpf(4) / (-disc)
    tors_excess = tors_abs_sq / (mpf(4) / mpf(3)) - mpf(1)
    # Riley longitude norm check: ((m^2 - m - 2 - m^-1 + m^-2)^2 - (m - m^-1)^2 * disc) / 4 == 1
    riley_a = (mv ** 2) - mv - mpf(2) - mvi + (mvi ** 2)
    riley_norm_sq = ((riley_a ** 2) - ((mv - mvi) ** 2) * disc) / mpf(4)
    # Subtracted Kirk-Klassen cone-manifold CS_u(4_1) = S(u) - i*pi*u - u*v/4 ([murakami-h2011] Sec. 4.3),
    # where ell(e^u) = e^{v/2} on the unit circle (v = 2*i*arg(ell) purely imaginary):
    ell_complex = mpc(riley_a / mpf(2), ((mv - mvi) / mpf(2)) * mp.sqrt(-disc))
    v_imag = mpf(2) * mp.arg(ell_complex)
    im_cs_kirk_klassen = mp.im(s_complex) - mp.pi * u_val - (u_val * v_imag) / mpf(4)
    return {
        "u": u_val,
        "theta_rad": theta,
        "re_S_u": mp.re(s_complex),
        "im_S_u": mp.im(s_complex),
        "eff_vol_2pi_Re_S_over_xi": eff_vol_equiv,
        "kirk_klassen_im_CS_u": im_cs_kirk_klassen,
        "reidemeister_disc": disc,
        "w_coord": wv,
        "torsion_abs_sq_excess": tors_excess,
        "riley_norm_sq_minus_1": riley_norm_sq - mpf(1),
    }


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        q_mu = q_muon_at(80)
        hbar_q = mpf(1) - qi0
        hbar_sq = hbar_q ** 2
        hbar_cu = hbar_q ** 3
        h0 = q0 - qi0
        w0 = q0 + qi0 - mpf(2)

        alpha_q = form_b_alpha_q(q0)
        vol_41 = vol_4_1_at(80)
        z_52 = solve_z_5_2()
        vol_52 = mpf(3) * bloch_wigner(z_52)

        # Comparison-only NIST CODATA-2022 constants (parsed from value_str at 80 dps)
        mu_e_entry = codata("muon-electron mass ratio")
        tau_e_entry = codata("tau-electron mass ratio")
        mu_e_codata = mpf(mu_e_entry.value_str)
        tau_e_codata = mpf(tau_e_entry.value_str)
        mu_e_sigma = mpf(mu_e_entry.uncertainty_str)

        wb = WitnessBuilder(
            "w6-inhomogeneous-lepton-resolvent",
            engine="mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps verification of QOU/Observations/InhomogeneousLeptonLoopResolvent.lean "
            "(W6 / Q-Gap-2, beans qou-91w7, qou-6gf9, qou-mk7u): exact H_3(q) figure-eight closed form, "
            "R = tau_e/hbar_q^2 = 70.4037 homogeneous obstruction, inhomogeneous loop resolvent "
            "decomposition, Murakami 2011 real-q Reidemeister torsion & deformed Chern-Simons test (H1), "
            "Form-B alpha_q(q_0) two-term radiative self-energy differentials (H2), and T(2,7)x4_1 / 5_2 "
            "m_tau/m_e resolvent check (H3). Zero fitted parameters."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("alpha_q_formB_inv_50dps", fmt50(mpf(1) / alpha_q))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ------------------------------------------------------------------
        # Section 1 & 2: Lean algebraic identity checks at 80 dps
        # ------------------------------------------------------------------
        tr21_direct = fig8_mat21_trace_direct(q0)
        tr21_closed = (h0 ** 4) + mpf(2) * (h0 ** 2) - mpf(1)
        tau_41_q0 = tau_figure_eight(q0)
        tau_41_from_blocks = y3_weight(q0) * mpf(1) + y21_weight(q0) * tr21_direct
        tau_41_bar_err = abs(tau_figure_eight(qi0) - tau_41_q0)

        tau_e_q0 = tau_electron(q0)
        unit_ratio_R = tau_e_q0 / hbar_sq
        unit_ratio_split_rhs = (q0 ** 3) / (mpf(2) * hbar_sq) + (
            (q0 ** 5) * ((q0 + mpf(1)) ** 2) / (mpf(2) * ((q0 ** 2 + mpf(1)) ** 2))
        )
        half_over_tau_e = (mpf(1) / mpf(2)) / tau_e_q0

        wb.add_assertion(
            "lean_fig8_21_trace_and_closed_form_exact",
            computed=abs(tr21_direct - tr21_closed)
            + abs(tau_41_q0 - tau_41_from_blocks)
            + tau_41_bar_err,
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="InhomogeneousLeptonLoopResolvent.fig8_21_trace, tauFigureEight_closed_form, tauFigureEight_bar",
        )
        wb.add_assertion(
            "lean_unit_ratio_gt_six_and_split_exact",
            computed=abs(unit_ratio_R - unit_ratio_split_rhs)
            + (mpf(0) if (unit_ratio_R > mpf(6) and half_over_tau_e < mpf(1)) else mpf(1)),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="InhomogeneousLeptonLoopResolvent.unit_ratio_gt_six & half_div_tauElectron_lt_one",
        )

        # Bare leading carrier & inhomogeneous resolvent normalization comparison
        bare_carrier = vol_41 / hbar_sq
        bare_diff_abs = bare_carrier - mu_e_codata
        bare_rel_ppb = (bare_diff_abs / mu_e_codata) * mpf("1e9")
        req_rel_shift = (mu_e_codata - bare_carrier) / bare_carrier
        req_rel_ppb = req_rel_shift * mpf("1e9")

        z_41 = mp.exp(mpc(mpf(0), mp.pi / mpf(3)))
        w_mu_qvol = mpf(2) * mp.im(q_volume_rearranged(z_41, q0))
        qvol_c_half_ratio = (tau_41_q0 + w_mu_qvol / mpf(2)) / tau_e_q0
        w_alg_norm_41 = tau_41_q0 / tau_e_q0
        resolvent_with_unsubtracted_contact = w_alg_norm_41 + bare_carrier

        # Verify carrier_ratio_of_electron_unit_alg exactly at test c_tors, c_2
        test_ctors = -mp.log(mpf(3)) / mpf(4)
        test_c2 = (mpf(2) * (mp.pi ** 2)) / mpf(27)
        res_eval_mu = w_alg_norm_41 + (vol_41 / hbar_sq) * (
            mpf(1) + test_ctors * hbar_q + test_c2 * hbar_sq
        )
        res_decomp_rhs = (
            bare_carrier
            + w_alg_norm_41
            + (vol_41 / hbar_q) * test_ctors
            + vol_41 * test_c2
        )
        wb.add_assertion(
            "lean_inhomogeneous_resolvent_electron_unit_decomp_exact",
            computed=abs(res_eval_mu - res_decomp_rhs),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="InhomogeneousLoopResolvent.carrier_ratio_of_electron_unit_alg",
        )

        # ------------------------------------------------------------------
        # (H1) Kashaev-Andersen-Hansen / Ohtsuki / Murakami real-q tests
        # ------------------------------------------------------------------
        n_eff = (mpf(2) * mp.pi) / hbar_sq
        s1_torsion = -mp.log(mpf(3)) / mpf(4)
        kappa1 = mpf(11) * mp.sqrt(mpf(3)) * mp.pi / mpf(108)
        kappa2 = mpf(2) * (mp.pi ** 2) / mpf(27)
        kappa3 = mpf(1081) * mp.sqrt(mpf(3)) * (mp.pi ** 3) / mpf(21870)

        h1a_one_loop_abs = (mpf(3) / mpf(2)) * mp.log(n_eff) + s1_torsion
        h1a_rungs_abs = (kappa1 / n_eff) + (kappa2 / (n_eff ** 2)) + (kappa3 / (n_eff ** 3))
        h1a_total_rel_ppb = ((h1a_one_loop_abs + h1a_rungs_abs) / bare_carrier) * mpf("1e9")

        # Multiplicative real-hbar_q subleading tests
        h1b_s1_hbar_ppb = s1_torsion * hbar_q * mpf("1e9")
        h1b_s1_hbar2_ppb = s1_torsion * hbar_sq * mpf("1e9")
        h1b_kappa1_hbar_ppb = kappa1 * hbar_q * mpf("1e9")
        h1b_kappa1_hbar2_ppb = kappa1 * hbar_sq * mpf("1e9")

        # H1.c: Murakami 2011 Thm. 1.3 real deformation at u_0 = ln(q_0), u = hbar_q, u = hbar_q^2
        u_max = mp.log((mpf(3) + mp.sqrt(mpf(5))) / mpf(2))
        u0 = mp.log(q0)
        mur_u0 = murakami_deformed_action_4_1(u0)
        mur_hbar = murakami_deformed_action_4_1(hbar_q)
        mur_hbar_sq = murakami_deformed_action_4_1(hbar_sq)

        mur_u0_vol_rel_ppb = ((mur_u0["eff_vol_2pi_Re_S_over_xi"] / vol_41) - mpf(1)) * mpf("1e9")
        mur_hbar_vol_rel_ppb = ((mur_hbar["eff_vol_2pi_Re_S_over_xi"] / vol_41) - mpf(1)) * mpf("1e9")
        mur_hbar_sq_vol_rel_ppb = (
            (mur_hbar_sq["eff_vol_2pi_Re_S_over_xi"] / vol_41) - mpf(1)
        ) * mpf("1e9")
        mur_u0_tors_ppb = mur_u0["torsion_abs_sq_excess"] * mpf("1e9")

        disc_w_identity_err = abs(
            mur_u0["reidemeister_disc"] - ((w0 + mpf(3)) * (w0 - mpf(1)))
        )
        wb.add_assertion(
            "lean_murakami_cone_window_and_riley_unit_norm_exact",
            computed=disc_w_identity_err
            + abs(mur_u0["re_S_u"])
            + abs(mur_u0["riley_norm_sq_minus_1"])
            + (
                mpf(0)
                if (
                    mpf(0) < u0 < u_max
                    and mpf(0) < w0 < mpf(1)
                    and mur_u0["torsion_abs_sq_excess"] > mpf(0)
                )
                else mpf(1)
            ),
            expected=mpf(0),
            tolerance=mpf("1e-72"),
            source="InhomogeneousLeptonLoopResolvent.reidemeisterDisc41_eq_wCoord, riley_longitude_unit_norm_identity, reidemeisterTorsionAbsSq_excess_pos",
        )

        # ------------------------------------------------------------------
        # (H2) Two-term QED radiative self-energy differences at Form-B alpha_q(q_0)
        # ------------------------------------------------------------------
        schwinger_1loop = alpha_q / (mpf(2) * mp.pi)
        # Universal multiplicative 1-loop cancels identically in m_mu / m_e:
        univ_cancel_err = abs(
            ((bare_carrier * (mpf(1) + schwinger_1loop)) / (mpf(1) + schwinger_1loop))
            - bare_carrier
        )
        wb.add_assertion(
            "lean_universal_qed_self_energy_cancels_exact",
            computed=univ_cancel_err
            + (mpf(0) if tr21_direct < mpf(0) else mpf(1)),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="InhomogeneousLeptonLoopResolvent.universal_qed_self_energy_cancels & fig8_21_trace_neg_of_le_five_fourths",
        )

        h2_candidates = {
            "universal_1loop_schwinger_ratio_shift": mpf(0),
            "shared_cutoff_pole_mass_log_neg_3alpha_2pi_ln_R0": -(
                mpf(3) * alpha_q / (mpf(2) * mp.pi)
            )
            * mp.log(bare_carrier),
            "pure_qed_neg_alpha_over_pi_sq": -((alpha_q / mp.pi) ** 2),
            "pure_qed_neg_alpha_over_pi_cu": -((alpha_q / mp.pi) ** 3),
            "mixed_neg_alpha_sq_h0_sq": -(alpha_q ** 2) * (h0 ** 2),
            "mixed_neg_alpha_h0_pow4_over_4pi": -(alpha_q * (h0 ** 4)) / (mpf(4) * mp.pi),
            "mixed_neg_y21_alpha_h0_pow4_over_4pi": -(
                y21_weight(q0) * alpha_q * (h0 ** 4)
            )
            / (mpf(4) * mp.pi),
            "mixed_neg_alpha_hbar_pow4_over_4pi": -(alpha_q * (hbar_q ** 4))
            / (mpf(4) * mp.pi),
            "mixed_neg_alpha_w0_sq_over_2pi": -(alpha_q * (w0 ** 2)) / (mpf(2) * mp.pi),
            "channel_21_1loop_schwinger_y21_chi21": schwinger_1loop
            * y21_weight(q0)
            * tr21_direct,
            "channel_21_2loop_schwinger_sq_chi21_over_tau41": (schwinger_1loop ** 2)
            * (tr21_direct / tau_41_q0),
        }

        h2_report = {}
        for key, rel_shift in h2_candidates.items():
            shifted_ratio = bare_carrier * (mpf(1) + rel_shift)
            res_vs_codata_ppb = ((shifted_ratio - mu_e_codata) / mu_e_codata) * mpf("1e9")
            h2_report[key] = {
                "fractional_shift": fmt50(rel_shift),
                "fractional_shift_ppb": fmt50(rel_shift * mpf("1e9")),
                "shifted_mu_over_e": fmt50(shifted_ratio),
                "post_shift_residual_vs_codata_ppb": fmt50(res_vs_codata_ppb),
                "post_shift_sigma": fmt50((shifted_ratio - mu_e_codata) / mu_e_sigma),
            }

        # ------------------------------------------------------------------
        # (H3) Satellite T(2,7) x 4_1 & hyperbolic 5_2 check for m_tau / m_e
        # ------------------------------------------------------------------
        z_52_poly_err = abs((z_52 ** 3) - (z_52 ** 2) + mpf(1))
        wb.add_assertion(
            "knot_5_2_shape_cubic_and_volume_verified",
            computed=z_52_poly_err
            + (mpf(0) if abs(vol_52 - mpf("2.828122")) < mpf("1e-5") else mpf(1)),
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="5_2 ideal triangulation z^3 - z^2 + 1 = 0, Vol(5_2) = 3 D(z) = 2.828122088...",
        )

        tau_t27_q0 = tau_t27_h2(q0)
        w_52_qvol = mpf(3) * mp.im(q_volume_rearranged(z_52, q0))
        h3_candidates = {
            "H3a_satellite_T27_41_additive_hbar2": bare_carrier,
            "H3a_satellite_T27_41_with_contact_trace": (tau_t27_q0 / tau_e_q0) + bare_carrier,
            "H3b_satellite_cable_p2_sq_4x_Vol41_hbar2": mpf(4) * bare_carrier,
            "H3b_generation_step_Vol41_hbar3": vol_41 / hbar_cu,
            "H3c_five_two_Vol52_hbar2": vol_52 / hbar_sq,
            "H3c_five_two_Vol52_hbar3": vol_52 / hbar_cu,
            "H3c_five_two_qvolume_3ImG_hbar0": w_52_qvol,
            "H3c_five_two_qvolume_div_hbar": w_52_qvol / hbar_q,
        }
        h3_report = {}
        for key, pred_val in h3_candidates.items():
            rel_pct = ((pred_val - tau_e_codata) / tau_e_codata) * mpf(100)
            h3_report[key] = {
                "predicted_tau_over_e": fmt50(pred_val),
                "relative_error_percent": fmt50(rel_pct),
            }

        wb.add_data(
            "section1_2_resolvent_baseline",
            {
                "q0_proton": fmt50(q0),
                "q_muon_comparison": fmt50(q_mu),
                "hbar_q": fmt50(hbar_q),
                "hbar_q_sq": fmt50(hbar_sq),
                "h0": fmt50(h0),
                "w0": fmt50(w0),
                "alpha_q_formB": fmt50(alpha_q),
                "alpha_q_formB_inv": fmt50(mpf(1) / alpha_q),
                "tau_electron_hopf_q0": fmt50(tau_e_q0),
                "tau_figure_eight_q0": fmt50(tau_41_q0),
                "fig8_21_trace_q0": fmt50(tr21_direct),
                "homogeneous_trace_ratio_q0": fmt50(w_alg_norm_41),
                "unit_split_R_tau_e_over_hbar_sq": fmt50(unit_ratio_R),
                "half_over_tau_e_scale_drift": fmt50(half_over_tau_e),
                "qvolume_c_half_unnormalized_ratio": fmt50(qvol_c_half_ratio),
                "resolvent_with_unsubtracted_O1_contact": fmt50(
                    resolvent_with_unsubtracted_contact
                ),
                "bare_singular_carrier_Vol41_over_hbar_sq": fmt50(bare_carrier),
                "codata_2022_mu_over_e_comparison": mu_e_entry.value_str,
                "codata_2022_mu_over_e_sigma": mu_e_entry.uncertainty_str,
                "bare_carrier_residual_ppb": fmt50(bare_rel_ppb),
                "required_fractional_shift_ppb": fmt50(req_rel_ppb),
            },
        )
        wb.add_data(
            "H1_kashaev_ohtsuki_murakami_real_q",
            {
                "N_eff_2pi_over_hbar_sq": fmt50(n_eff),
                "S1_torsion_neg_quarter_ln3": fmt50(s1_torsion),
                "H1a_root_of_unity_1loop_plus_rungs_ppb": fmt50(h1a_total_rel_ppb),
                "H1b_multiplicative_S1_hbar_ppb": fmt50(h1b_s1_hbar_ppb),
                "H1b_multiplicative_S1_hbar_sq_ppb": fmt50(h1b_s1_hbar2_ppb),
                "H1b_multiplicative_kappa1_hbar_ppb": fmt50(h1b_kappa1_hbar_ppb),
                "H1b_multiplicative_kappa1_hbar_sq_ppb": fmt50(h1b_kappa1_hbar2_ppb),
                "murakami_cone_upper_bound_u_max": fmt50(u_max),
                "H1c_murakami_at_u0_ln_q0": {
                    "u0": fmt50(u0),
                    "theta_rad": fmt50(mur_u0["theta_rad"]),
                    "im_S_u0": fmt50(mur_u0["im_S_u"]),
                    "eff_vol_2pi_Re_S_over_xi": fmt50(
                        mur_u0["eff_vol_2pi_Re_S_over_xi"]
                    ),
                    "eff_vol_shift_ppb": fmt50(mur_u0_vol_rel_ppb),
                    "kirk_klassen_im_CS_u0": fmt50(mur_u0["kirk_klassen_im_CS_u"]),
                    "kirk_klassen_im_CS_shift_ppb": fmt50(
                        ((mur_u0["kirk_klassen_im_CS_u"] / vol_41) - mpf(1)) * mpf("1e9")
                    ),
                    "reidemeister_disc_q0": fmt50(mur_u0["reidemeister_disc"]),
                    "torsion_abs_sq_shift_ppb": fmt50(mur_u0_tors_ppb),
                    "amphichiral_cusp_slope_d_eff_vol_du_at_0": "+pi (strictly positive for all 0 < |u| < u_max by [murakami-h2011] Thm 1.3 & Rem 1.4)",
                },
                "H1c_murakami_at_u_eq_hbar_q_vol_shift_ppb": fmt50(mur_hbar_vol_rel_ppb),
                "H1c_murakami_at_u_eq_hbar_q_sq_vol_shift_ppb": fmt50(
                    mur_hbar_sq_vol_rel_ppb
                ),
            },
        )
        wb.add_data("H2_two_term_radiative_self_energy_at_alpha_q", h2_report)
        wb.add_data(
            "H3_tau_resolvent_candidates",
            {
                "vol_5_2_exact": fmt50(vol_52),
                "codata_2022_tau_over_e_comparison": tau_e_entry.value_str,
                "candidates": h3_report,
            },
        )

        wb.save(
            {
                "q0Anchor": "proton",
                "q0AnchorReason": (
                    "Canonical proton pin q_0 = q_at(80) held fixed per owner gate qou-eic1; "
                    "muon pin q_muon_at(80) recorded strictly as a labelled comparison datum."
                ),
            }
        )

        print(f"R = tau_e/hbar^2 = {mp.nstr(unit_ratio_R, 14)}")
        print(
            f"Bare Vol(4_1)/hbar^2 = {mp.nstr(bare_carrier, 14)} "
            f"(+{mp.nstr(bare_rel_ppb, 7)} ppb vs CODATA; needed {mp.nstr(req_rel_ppb, 7)} ppb)"
        )
        print(
            f"H1c Murakami u0=ln(q0): vol shift = {mp.nstr(mur_u0_vol_rel_ppb, 7)} ppb, "
            f"torsion |T|^2 shift = +{mp.nstr(mur_u0_tors_ppb, 7)} ppb"
        )
        print(
            f"H1c Murakami u=hbar_q^2: vol shift = {mp.nstr(mur_hbar_sq_vol_rel_ppb, 7)} ppb"
        )
        for k, v in h2_report.items():
            print(
                f"H2 {k}: shift={mp.nstr(mpf(v['fractional_shift_ppb']), 6)} ppb -> "
                f"res={mp.nstr(mpf(v['post_shift_residual_vs_codata_ppb']), 6)} ppb "
                f"({mp.nstr(mpf(v['post_shift_sigma']), 4)} sigma)"
            )
        for k, v in h3_report.items():
            print(
                f"H3 {k}: {mp.nstr(mpf(v['predicted_tau_over_e']), 8)} "
                f"({mp.nstr(mpf(v['relative_error_percent']), 5)}%)"
            )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
