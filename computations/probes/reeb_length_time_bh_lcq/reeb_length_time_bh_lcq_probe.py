#!/usr/bin/env python3
"""Pre-registered 80-dps evaluation of Reeb length/time reconciliation, causal cone c_q(q_0),
categorical energy E = m c_q^2, L_cal boundary scale invariance, Temperley-Lieb / Hecke /
SU_q(2) horizon crossing channel entropy rates, Kaul-Majumdar -3/2 ln A logarithmic
correction, and candidate Sasakian/CR/LCQ area quanta vs 4 ln 2 and 4 ln [2]_{q_0}.

Bean `qou-slfm` (with upstream threads `qou-mumr`, `qou-5uj7`, `qou-jfx8`, `qou-apma`,
and `QOU/GravitySpacetime/ReebLengthTimeAndLightConeEntropy.lean`).
Pre-registered in `PREREGISTRATION.md` (commit `3008f273ec9`) BEFORE evaluating any
candidate horizon area quantum against the Bekenstein-Hawking 1/4 coefficient.

Precision & anti-fit discipline (STRICT):
  - `mpmath` at `workdps = 80` (`OUT_DPS = 70` serialized into witness),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - ZERO `float64` imports, literals, or casts anywhere in the script or witness,
  - ZERO parameter tuning: all candidate area quanta are evaluated side-by-side and
    reported honestly, isolating the unproved Lorentzian CR null-focusing bridge as
    the Rule-13a zero-instance class `LCQHorizonPunctureAreaConjecture`.

Reproduce:
    python3 -u computations/probes/reeb_length_time_bh_lcq/reeb_length_time_bh_lcq_probe.py
"""

from __future__ import annotations

import os as _os
import sys as _sys
from pathlib import Path as _Path

_os.environ.setdefault("QOU_COMPUTE_DPS", "80")
_os.environ.setdefault("QOU_OUTPUT_DPS", "70")

_ROOT = _Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in _sys.path:
    _sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in _sys.path:
    _sys.path.insert(0, str(_ROOT / "computations"))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp  # noqa: E402

from qou_substrate.codata import value_str  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 70


def q_bracket_half(q: mp.mpf, two_m: int) -> mp.mpf:
    """Balanced quantum number [two_m / 2]_q = (q^(two_m/2) - q^(-two_m/2)) / (q - q^-1)."""
    half_pow = mp.power(q, mp.mpf(two_m) / mp.mpf(2))
    return (half_pow - mp.mpf(1) / half_pow) / (q - mp.mpf(1) / q)


def q_int(q: mp.mpf, n: int) -> mp.mpf:
    """Balanced quantum integer [n]_q = (q^n - q^-n) / (q - q^-1)."""
    if n == 0:
        return mp.mpf(0)
    qn = q ** n
    return (qn - mp.mpf(1) / qn) / (q - mp.mpf(1) / q)


def solve_lqg_pole(
    q: mp.mpf,
    *,
    sqrt_area: bool = False,
    two_state_dl: bool = False,
    n_terms: int = 450,
) -> mp.mpf:
    """Solve sum_{n>=0} w_n(q) * exp(-s * E_n(q)) = 1 at 80 dps.

    - Default (`sqrt_area=False, two_state_dl=False`): `lqg-entropy-qdim-partition-pole`
      convention w_n = [n+2]_q, E_n = [(n+1)/2]_q * [(n+3)/2]_q.
    - `sqrt_area=True, two_state_dl=True`: Domagala-Lewandowski (2004) m = +-j horizon
      projection w_n = 2, E_n = sqrt([(n+1)/2]_q * [(n+3)/2]_q).
    - `sqrt_area=True, two_state_dl=False`: Agullo-Barbero-Diaz-Fernandez-Villasenor
      full [2j+1]_q multiplicity with sqrt-Casimir area spectrum.
    """
    is_classical = abs(q - mp.mpf(1)) < mp.mpf("1e-70")
    weights: list[mp.mpf] = []
    energies: list[mp.mpf] = []
    for n in range(n_terms):
        if is_classical:
            qd = mp.mpf(2) if two_state_dl else mp.mpf(n + 2)
            cas = mp.mpf(n + 1) * mp.mpf(n + 3) / mp.mpf(4)
        else:
            qd = mp.mpf(2) if two_state_dl else q_int(q, n + 2)
            cas = q_bracket_half(q, n + 1) * q_bracket_half(q, n + 3)
        en = mp.sqrt(cas) if sqrt_area else cas
        weights.append(qd)
        energies.append(en)

    def z1_and_deriv(s: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        val = mp.mpf(0)
        dval = mp.mpf(0)
        for qd, en in zip(weights, energies):
            term = qd * mp.exp(-s * en)
            val += term
            dval -= en * term
            if term < mp.mpf("1e-95"):
                break
        return val, dval

    s = mp.mpf("1.5")
    for _ in range(40):
        f_val, df_val = z1_and_deriv(s)
        step = (f_val - mp.mpf(1)) / df_val
        s -= step
        if abs(step) < mp.mpf("1e-78"):
            break
    return s


def catalan_and_central_binom_table(max_m: int) -> tuple[list[int], list[int]]:
    """Exact pure-integer Catalan C_m and central binomial (2m choose m) for 0 <= m <= max_m."""
    cat = [1]
    cbin = [1]
    for m in range(max_m):
        next_cbin = (cbin[-1] * 2 * (2 * m + 1)) // (m + 1)
        next_cat = next_cbin // (m + 2)
        cbin.append(next_cbin)
        cat.append(next_cat)
    return cat, cbin


def main() -> int:
    set_compute_dps(WORK_DPS)
    with mp.workdps(WORK_DPS):
        q0 = q_at(WORK_DPS)
        one = mp.mpf(1)
        two = mp.mpf(2)
        three = mp.mpf(3)
        four = mp.mpf(4)
        eight = mp.mpf(8)
        quarter = one / four
        pi_mp = mp.pi

        # =====================================================================
        # Battery A: Reeb Length/Time, c_q(q_0), E = m c_q^2, KMS, L_cal
        # =====================================================================
        q0_inv = one / q0
        hbar_q0 = one - q0_inv
        t_p_q0 = one / hbar_q0
        ell_p_circuit = hbar_q0 * t_p_q0
        c_q0 = one / (q0 - one)
        c_q0_ratio = q0_inv / hbar_q0
        c_q0_sq = c_q0 ** 2

        convex_split_res = abs((q0_inv + hbar_q0) - one)
        circuit_unit_res = abs(ell_p_circuit - one)
        cq_ratio_res = abs(c_q0 - c_q0_ratio)
        cq_tick_res = abs((c_q0 + one) - t_p_q0)
        hbar_mul_cq_res = abs((hbar_q0 * c_q0) - q0_inv)

        step_samples = [1, 3, 10, 18, 137]
        max_cone_res = mp.mpf(0)
        max_dirac_cost_res = mp.mpf(0)
        for n_steps in step_samples:
            n_mp = mp.mpf(n_steps)
            dt_comp = n_mp * hbar_q0
            dx_cone = n_mp * q0_inv
            max_cone_res = max(max_cone_res, abs(dx_cone - c_q0 * dt_comp))
            max_dirac_cost_res = max(max_dirac_cost_res, abs((dx_cone + dt_comp) - n_mp))

        # KMS modular clock on O_{q_0}(SU(2)) vs traciality obstruction
        modular_step_q2 = q0 ** 2
        beta_mod_oqsu2 = two * mp.log(q0)
        # Explicit 2x2 non-tracial density check: tau = Tr, D = diag(q_0, q_0^-1)
        # phi_D(x) = Tr(D x), sigma_mod(y) = D y D^-1
        d0, d1 = q0, q0_inv
        # Test off-diagonal matrices X = [[2, 3], [5, 7]], Y = [[11, 13], [17, 19]]
        # phi_D(X * sigma_mod(Y)) vs phi_D(Y * X)
        x00, x01, x10, x11 = mp.mpf(2), mp.mpf(3), mp.mpf(5), mp.mpf(7)
        y00, y01, y10, y11 = mp.mpf(11), mp.mpf(13), mp.mpf(17), mp.mpf(19)
        sy00, sy01 = y00, (d0 / d1) * y01
        sy10, sy11 = (d1 / d0) * y10, y11
        phi_x_sy = d0 * (x00 * sy00 + x01 * sy10) + d1 * (x10 * sy01 + x11 * sy11)
        phi_yx = d0 * (y00 * x00 + y01 * x10) + d1 * (y10 * x01 + y11 * x11)
        kms_swap_res = abs(phi_x_sy - phi_yx)

        # Categorical energy & internal gravitational identities
        eta_q0 = (two * q0 - one) / (q0 ** 3)
        s_cell_series = eta_q0 * (hbar_q0 ** 2) / (one - hbar_q0 ** 2)
        s_cell_closed = ((q0 - one) ** 2) / (q0 ** 3)
        s_cell_res = abs(s_cell_series - s_cell_closed)

        g_q0 = (c_q0 ** 3) * hbar_q0 / s_cell_series
        g_q0_closed = (q0 ** 2) / ((q0 - one) ** 4)
        g_q0_res = abs(g_q0 - g_q0_closed)

        g_planck_mc = g_q0 * ((hbar_q0 / c_q0) ** 2)
        newton_planck_area_sub = hbar_q0 * g_q0 / (c_q0 ** 3)
        cell_area_ratio_sub = (hbar_q0 ** 2) / s_cell_series
        g_planck_res = max(
            abs(g_planck_mc - one),
            abs(newton_planck_area_sub - q0),
            abs(cell_area_ratio_sub - q0),
        )

        # Layer-III boundary L_cal invariance (CAL-1 reduced Compton wavelength vs SI Planck length)
        lambda_bar_ce_m = mp.mpf(value_str("reduced Compton wavelength"))
        ell_planck_si_m = mp.mpf(value_str("Planck length"))
        compton_to_planck_ratio = lambda_bar_ce_m / ell_planck_si_m

        # Test calibration invariance across both L_cal choices
        max_cal_inv_res = mp.mpf(0)
        a_sub_test = mp.mpf(37)
        ell_sub_test = q0
        n_test = mp.mpf(18)
        for l_cal in (lambda_bar_ce_m, ell_planck_si_m):
            cq_cal = (l_cal * (n_test * q0_inv)) / (l_cal * (n_test * hbar_q0))
            bh_cal = ((l_cal ** 2) * a_sub_test) / (four * ((l_cal * ell_sub_test) ** 2))
            bh_sub = a_sub_test / (four * (ell_sub_test ** 2))
            max_cal_inv_res = max(
                max_cal_inv_res,
                abs(cq_cal - c_q0),
                abs(bh_cal - bh_sub),
            )

        # =====================================================================
        # Battery B: Horizon Crossing Channel Entropy Rates & Subleading Law
        # =====================================================================
        ln2 = mp.log(two)
        q2_q0 = q0 + q0_inv
        q3_q0 = (q0 ** 2) + one + (q0_inv ** 2)
        q5_q0 = (q0 ** 4) + (q0 ** 2) + one + (q0_inv ** 2) + (q0_inv ** 4)
        jones_index_q0 = q2_q0 ** 2

        # Exact Clebsch-Gordan checks: [2]_q^2 = 1 + [3]_q and [2]_q^4 = 2 + 3 [3]_q + [5]_q
        cg2_res = abs(jones_index_q0 - (one + q3_q0))
        cg4_res = abs((q2_q0 ** 4) - (two + three * q3_q0 + q5_q0))

        s_cat = ln2
        s_tl_q2 = mp.log(q2_q0)
        q2_half_q0 = mp.sqrt(q0) + one / mp.sqrt(q0)
        s_tl_q2_half = mp.log(q2_half_q0)
        s_q3 = mp.log(q3_q0)
        s_q3_per_strand = s_q3 / three
        s_tl3_dim5_per_strand = mp.log(mp.mpf(5)) / three

        # Woronowicz Haar modular qubit weights & von Neumann entropy
        p_plus = (q0 ** 2) / (one + q0 ** 2)
        p_minus = one / (one + q0 ** 2)
        haar_weight_res = max(
            abs((p_plus + p_minus) - one),
            abs((p_plus - p_minus) - ((q0 - q0_inv) / q2_q0)),
            abs((p_plus / p_minus) - (q0 ** 2)),
        )
        s_haar = -(p_plus * mp.log(p_plus) + p_minus * mp.log(p_minus))
        s_haar_formula = s_tl_q2 - ((q0 - q0_inv) / q2_q0) * mp.log(q0)
        haar_entropy_res = abs(s_haar - s_haar_formula)
        haar_tl_midpoint_minus_ln2 = (s_haar + s_tl_q2) / two - ln2

        # Exact Catalan & Kaul-Majumdar -3/2 ln N_Sigma verification up to N_Sigma = 10000 (m = 5000)
        cat_list, cbin_list = catalan_and_central_binom_table(5000)
        bounds_ok = True
        pow4 = 1
        for m in range(5001):
            cm = cat_list[m]
            if not (pow4 <= ((m + 1) ** 2) * cm and cm <= pow4):
                bounds_ok = False
                break
            pow4 *= 4

        km_const = mp.log(eight / pi_mp) / two
        meissner_const = mp.log(two / pi_mp) / two
        catalan_scaling_rows: dict[str, dict[str, str]] = {}
        for n_sigma in (20, 100, 500, 2000, 10000):
            m = n_sigma // 2
            n_mp = mp.mpf(n_sigma)
            ln_cm = mp.log(mp.mpf(cat_list[m]))
            ln_cbin = mp.log(mp.mpf(cbin_list[m]))
            km_asymp_1 = (
                n_mp * ln2
                - (three / two) * mp.log(n_mp)
                + km_const
                - (mp.mpf(9) / four) / n_mp
            )
            meissner_asymp_0 = n_mp * ln2 - (one / two) * mp.log(n_mp) + meissner_const
            eff_alpha_km = (n_mp * ln2 + km_const - ln_cm) / mp.log(n_mp)
            eff_alpha_u1 = (n_mp * ln2 + meissner_const - ln_cbin) / mp.log(n_mp)
            catalan_scaling_rows[f"N_{n_sigma}"] = {
                "m_pairs": str(m),
                "ln_dim_singlet": fmt(ln_cm, dps=OUT_DPS),
                "rate_per_puncture_ln_dim_over_N": fmt(ln_cm / n_mp, dps=OUT_DPS),
                "effective_subleading_log_coeff_singlet": fmt(eff_alpha_km, dps=25),
                "kaul_majumdar_order1_abs_err": fmt(abs(ln_cm - km_asymp_1), dps=25),
                "effective_subleading_log_coeff_u1_binom": fmt(eff_alpha_u1, dps=25),
                "meissner_u1_order0_abs_err": fmt(abs(ln_cbin - meissner_asymp_0), dps=25),
            }

        km_err_10000 = abs(
            mp.log(mp.mpf(cat_list[5000]))
            - (
                mp.mpf(10000) * ln2
                - (three / two) * mp.log(mp.mpf(10000))
                + km_const
                - (mp.mpf(9) / four) / mp.mpf(10000)
            )
        )

        # Full SU_{q_0}(2) vs classical SU(2) spin-tower poles Z_1(s_star) = 1
        s_star_q0 = solve_lqg_pole(q0, sqrt_area=False, two_state_dl=False)
        gamma_star_q0 = s_star_q0 / (two * pi_mp)
        s_star_classical = solve_lqg_pole(one, sqrt_area=False, two_state_dl=False)
        gamma_casimir_classical = s_star_classical / (two * pi_mp)

        s_dl_q0 = solve_lqg_pole(q0, sqrt_area=True, two_state_dl=True)
        gamma_dl_q0 = s_dl_q0 / (two * pi_mp)
        s_dl_classical = solve_lqg_pole(one, sqrt_area=True, two_state_dl=True)
        gamma_dl_classical = s_dl_classical / (two * pi_mp)

        s_abdfv_q0 = solve_lqg_pole(q0, sqrt_area=True, two_state_dl=False)
        gamma_abdfv_q0 = s_abdfv_q0 / (two * pi_mp)

        # =====================================================================
        # Battery C: Candidate Area Quanta a_0 vs Required Lock a_0* = 4 s_punct
        # =====================================================================
        a0_star_cat = four * s_cat
        a0_star_tl = four * s_tl_q2
        a0_star_haar = four * s_haar
        a0_star_q3 = four * s_q3

        casimir_half_q0 = q_bracket_half(q0, 1) * q_bracket_half(q0, 3)
        sqrt_casimir_half_q0 = mp.sqrt(casimir_half_q0)

        candidate_areas: list[tuple[str, mp.mpf, str]] = [
            ("Q1_unit_circuit_cell", one, "a_0 = 1 (unit normalised Reeb circuit cell)"),
            ("Q2a_horiz_step_sq", q0_inv ** 2, "a_0 = q_0^-2 (elementary horizontal step squared)"),
            ("Q2b_newton_cell_ratio", q0, "a_0 = hbar_{q_0}^2 / S_cell(q_0) = q_0"),
            (
                "Q3_dirac_share_ashtekar_spin12",
                eight * pi_mp * hbar_q0 * sqrt_casimir_half_q0,
                "a_0 = 8*pi * hbar_{q_0} * sqrt([1/2]_{q_0}[3/2]_{q_0}) (gamma = hbar_{q_0})",
            ),
            (
                "Q4_contact_anisotropy_spin12",
                eight * pi_mp * (q0 - one) * sqrt_casimir_half_q0,
                "a_0 = 8*pi * (q_0 - 1) * sqrt([1/2]_{q_0}[3/2]_{q_0}) (gamma = c_{q_0}^-1)",
            ),
            ("Q5a_meridian_disk_pi", pi_mp, "a_0 = pi (unit meridian disk)"),
            ("Q5b_hemisphere_2pi", two * pi_mp, "a_0 = 2*pi (hemisphere / modular period)"),
            ("Q5c_two_sphere_4pi", four * pi_mp, "a_0 = 4*pi (unit 2-sphere solid angle)"),
        ]

        candidate_evaluation: dict[str, dict[str, str]] = {}
        min_abs_rel_miss = mp.mpf("1e9")
        for key, a0_val, desc in candidate_areas:
            coeff_cat = s_cat / a0_val
            coeff_tl = s_tl_q2 / a0_val
            rel_miss_cat = (coeff_cat - quarter) / quarter
            rel_miss_tl = (coeff_tl - quarter) / quarter
            min_abs_rel_miss = min(min_abs_rel_miss, abs(rel_miss_cat), abs(rel_miss_tl))
            candidate_evaluation[key] = {
                "formula": desc,
                "a0_value": fmt(a0_val, dps=OUT_DPS),
                "S_over_A_catalan_ln2": fmt(coeff_cat, dps=OUT_DPS),
                "rel_diff_vs_quarter_catalan": fmt(rel_miss_cat, dps=20),
                "S_over_A_tl_ln_q2": fmt(coeff_tl, dps=OUT_DPS),
                "rel_diff_vs_quarter_tl_q2": fmt(rel_miss_tl, dps=20),
            }

        # Q6: Exact LCQ Clausius-Raychaudhuri cancellation check
        # Modular boost: dS / dK = 2*pi / hbar_{q_0}; Raychaudhuri focusing: dA / dK = 8*pi*G_{q_0} / c_{q_0}^3
        lcq_ds_over_dk = (two * pi_mp) / hbar_q0
        lcq_da_over_dk = (eight * pi_mp * g_q0) / (c_q0 ** 3)
        lcq_ds_over_da = lcq_ds_over_dk / lcq_da_over_dk
        lcq_target_quarter_over_ellp_sq = one / (four * newton_planck_area_sub)
        lcq_cancellation_res = abs(lcq_ds_over_da - lcq_target_quarter_over_ellp_sq)

        # Ratio mismatch between D_nabla Reeb share hbar_{q_0} and LQG critical pole gamma_star(q_0)
        gamma_star_over_hbar_q0 = gamma_star_q0 / hbar_q0
        gamma_star_over_q0_minus_1 = gamma_star_q0 / (q0 - one)

        # =====================================================================
        # Build 80-dps Witness JSON
        # =====================================================================
        wb = WitnessBuilder(
            "reeb-length-time-bh-lcq",
            engine="mpmath",
            output_dir=_Path(__file__).resolve().parent,
        )
        wb.set_description(
            "Pre-registered 80-dps (70-dps serialized) evaluation of Reeb length/time "
            "reconciliation, Lieb-Robinson causal cone speed c_q(q_0), categorical energy "
            "E = m c_q^2, KMS modular clock vs traciality obstruction, Layer-III L_cal "
            "boundary invariance, Temperley-Lieb / Catalan / SU_{q_0}(2) horizon crossing "
            "channel entropy rates (ln 2 vs ln[2]_{q_0} vs Haar vs ln[3]_{q_0} and -3/2 ln A "
            "Kaul-Majumdar subleading law), and zero-parameter candidate area quanta vs "
            "4 ln 2 and 4 ln[2]_{q_0} (Bean qou-slfm)."
        )
        wb.set_content_block("rem:spacetime-length-distance-layers")
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("preregistration_commit", "3008f273ec92545960757eb158f6afd6951aff6a")

        wb.add_data(
            "battery_a_reeb_length_time_causal_cone",
            {
                "q0_inv_horiz_weight": fmt(q0_inv, dps=OUT_DPS),
                "hbar_q0_reeb_share": fmt(hbar_q0, dps=OUT_DPS),
                "t_P_q0_full_circuit_tick": fmt(t_p_q0, dps=OUT_DPS),
                "ell_P_normalised_circuit": fmt(ell_p_circuit, dps=OUT_DPS),
                "c_q0_lieb_robinson_speed": fmt(c_q0, dps=OUT_DPS),
                "c_q0_squared_energy_factor": fmt(c_q0_sq, dps=OUT_DPS),
                "hbar_q0_mul_c_q0": fmt(hbar_q0 * c_q0, dps=OUT_DPS),
                "oqsu2_modular_step_q0_sq": fmt(modular_step_q2, dps=OUT_DPS),
                "oqsu2_modular_beta_2ln_q0": fmt(beta_mod_oqsu2, dps=OUT_DPS),
                "eta_q0_operational_entropy": fmt(eta_q0, dps=OUT_DPS),
                "S_cell_q0_jet_entropy": fmt(s_cell_closed, dps=OUT_DPS),
                "G_q0_substrate": fmt(g_q0_closed, dps=OUT_DPS),
                "G_Planck_mc_norm": fmt(g_planck_mc, dps=OUT_DPS),
                "newton_planck_area_hbar_G_over_c3": fmt(newton_planck_area_sub, dps=OUT_DPS),
                "compton_to_si_planck_ratio": fmt(compton_to_planck_ratio, dps=30),
                "max_calibration_invariance_residual": fmt(max_cal_inv_res, dps=OUT_DPS),
            },
        )

        wb.add_data(
            "battery_b_horizon_channel_entropy_rates",
            {
                "q_two_q0_loop_fugacity": fmt(q2_q0, dps=OUT_DPS),
                "jones_subfactor_index_q2_sq": fmt(jones_index_q0, dps=OUT_DPS),
                "q_three_q0_spin1": fmt(q3_q0, dps=OUT_DPS),
                "s_catalan_singlet_ln2": fmt(s_cat, dps=OUT_DPS),
                "s_tl_loop_fugacity_ln_q2": fmt(s_tl_q2, dps=OUT_DPS),
                "s_tl_half_power_ln_q2_sqrt_q0": fmt(s_tl_q2_half, dps=OUT_DPS),
                "s_woronowicz_haar_qubit": fmt(s_haar, dps=OUT_DPS),
                "haar_tl_midpoint_minus_ln2": fmt(haar_tl_midpoint_minus_ln2, dps=OUT_DPS),
                "s_spin1_ln_q3": fmt(s_q3, dps=OUT_DPS),
                "s_spin1_per_strand_one_third_ln_q3": fmt(s_q3_per_strand, dps=OUT_DPS),
                "s_tl3_dim5_per_strand_one_third_ln5": fmt(s_tl3_dim5_per_strand, dps=OUT_DPS),
                "lqg_casimir_pole_s_star_q0": fmt(s_star_q0, dps=OUT_DPS),
                "lqg_casimir_immirzi_gamma_star_q0": fmt(gamma_star_q0, dps=OUT_DPS),
                "lqg_casimir_immirzi_gamma_star_1": fmt(gamma_casimir_classical, dps=OUT_DPS),
                "lqg_sqrt_casimir_DL_gamma_q0": fmt(gamma_dl_q0, dps=OUT_DPS),
                "lqg_sqrt_casimir_DL_gamma_1": fmt(gamma_dl_classical, dps=OUT_DPS),
                "lqg_sqrt_casimir_full_qdim_gamma_q0": fmt(gamma_abdfv_q0, dps=OUT_DPS),
                "kaul_majumdar_catalan_scaling": catalan_scaling_rows,
            },
        )

        wb.add_data(
            "battery_c_area_quantum_lock_diagnosis",
            {
                "required_a0_star_catalan_4ln2": fmt(a0_star_cat, dps=OUT_DPS),
                "required_a0_star_tl_4ln_q2": fmt(a0_star_tl, dps=OUT_DPS),
                "required_a0_star_haar_4s_haar": fmt(a0_star_haar, dps=OUT_DPS),
                "required_a0_star_spin1_4ln_q3": fmt(a0_star_q3, dps=OUT_DPS),
                "gamma_star_q0_over_hbar_q0": fmt(gamma_star_over_hbar_q0, dps=30),
                "gamma_star_q0_over_q0_minus_1": fmt(gamma_star_over_q0_minus_1, dps=30),
                "untuned_candidates": candidate_evaluation,
                "min_abs_relative_miss_among_untuned_candidates": fmt(min_abs_rel_miss, dps=20),
                "lcq_clausius_raychaudhuri_cancellation_residual": fmt(
                    lcq_cancellation_res, dps=OUT_DPS
                ),
            },
        )

        wb.add_assertion(
            "battery_a_reeb_cone_kms_grav_and_lcal_identities_exact",
            computed=fmt(
                max(
                    convex_split_res,
                    circuit_unit_res,
                    cq_ratio_res,
                    cq_tick_res,
                    hbar_mul_cq_res,
                    max_cone_res,
                    max_dirac_cost_res,
                    kms_swap_res,
                    s_cell_res,
                    g_q0_res,
                    g_planck_res,
                    max_cal_inv_res,
                ),
                dps=OUT_DPS,
            ),
            expected="0",
            tolerance="1e-74",
            source="ReebLengthTimeAndLightConeEntropy §§1-3: exact Layer-I/II/III Reeb, c_q, "
                   "KMS swap, G_Planck=1, hbar_q*G_q/c_q^3=q, and L_cal cancellation at 80 dps.",
        )
        wb.add_assertion(
            "battery_b_catalan_bounds_and_clebsch_gordan_exact",
            computed="1"
            if (
                bounds_ok
                and max(cg2_res, cg4_res, haar_weight_res, haar_entropy_res) < mp.mpf("1e-74")
                and s_haar < s_cat < s_tl_q2
            )
            else "0",
            expected="1",
            source="ReebLengthTimeAndLightConeEntropy §4: 4^m/(m+1)^2 <= C_m <= 4^m for m<=5000, "
                   "[2]_q^4 = C_2 + 3[3]_q + [5]_q, and s_Haar(q_0) < ln 2 < ln[2]_{q_0}.",
        )
        wb.add_assertion(
            "kaul_majumdar_minus_three_halves_log_correction_verified",
            computed=fmt(km_err_10000, dps=25),
            expected="0",
            tolerance="1e-6",
            source="Catalan singlet asymptotic expansion ln C_{N/2} = N ln 2 - (3/2) ln N + "
                   "(1/2) ln(8/pi) - 9/(4N) + O(N^-2) at N_Sigma = 10000.",
        )
        wb.add_assertion(
            "untuned_algebraic_and_sasakian_area_quanta_miss_quarter_law",
            computed="1" if min_abs_rel_miss > mp.mpf("0.11") else "0",
            expected="1",
            source="Honest refutation check: every pre-registered un-tuned rational/Sasakian "
                   "area candidate Q1-Q5 misses S = A/(4 ell_P^2) by > 11% (closest: pi at -11.1% / -11.7%, "
                   "gamma = q_0 - 1 at +15.3%, gamma = hbar_{q_0} at +28.0%).",
        )
        wb.add_assertion(
            "lcq_clausius_raychaudhuri_null_focusing_cancels_to_quarter",
            computed=fmt(lcq_cancellation_res, dps=OUT_DPS),
            expected="0",
            tolerance="1e-74",
            source="bekenstein_hawking_and_puncture_lock_of_lcq: (2*pi/hbar_q) / (8*pi*G_q/c_q^3) "
                   "= 1 / (4 * (hbar_q*G_q/c_q^3)) conditional on LCQHorizonPunctureAreaConjecture.",
        )

        wb.add_caveat(
            "Minimal Temperley-Lieb / SU_{q_0}(2) puncture channel counting fixes the dimensionless "
            "entropy per puncture (ln 2 = 0.6931472... for Catalan singlets with -3/2 ln N_Sigma "
            "Kaul-Majumdar correction; ln[2]_{q_0} = 0.6985808... for loop fugacity; 0.6877332... "
            "for Woronowicz Haar qubits) but CANNOT yield S = A/(4 ell_P^2) without an independent "
            "geometric theorem locking the elementary puncture area to a_0 = 4 s_punct (2.7725887... "
            "or 2.7943233...). All un-tuned algebraic/Sasakian candidates miss by >= 11.1%, and "
            "hbar_{q_0} = 0.0990817... differs from the LQG critical Immirzi poles (0.2086194... "
            "Casimir, 0.2371449... DL sqrt-Casimir, 0.2740182... full-qdim sqrt-Casimir) by 2.11x-2.77x. "
            "The required Lorentzian CR Bisognano-Wichmann + Raychaudhuri null-focusing bridge "
            "remains an open Rule-13a conjecture (LCQHorizonPunctureAreaConjecture, zero instances)."
        )

        out_path = wb.save({"q0Anchor": "proton", "workdps": WORK_DPS})

        print("=== 80-dps Reeb Length/Time & Light-Cone (LCQ) Bekenstein-Hawking Probe ===")
        print(f"q_0 (proton, 80 dps)         = {fmt(q0, dps=50)}")
        print(f"hbar_q0 = 1 - q_0^-1         = {fmt(hbar_q0, dps=50)}")
        print(f"t_P(q_0) = hbar_q0^-1        = {fmt(t_p_q0, dps=50)}")
        print(f"c_q(q_0) = 1 / (q_0 - 1)     = {fmt(c_q0, dps=50)}")
        print(f"c_q(q_0)^2                   = {fmt(c_q0_sq, dps=50)}")
        print(f"G_q(q_0)                     = {fmt(g_q0_closed, dps=50)}")
        print(f"hbar_q0 * G_q0 / c_q0^3      = {fmt(newton_planck_area_sub, dps=50)} (= q_0)")
        print(f"lambda_bar_Ce / ell_P^SI     = {fmt(compton_to_planck_ratio, dps=25)}")
        print("\n--- Horizon Channel Entropy Rates (80 dps) ---")
        print(f"s_Cat  = ln 2                = {fmt(s_cat, dps=50)}")
        print(f"s_TL   = ln [2]_q0           = {fmt(s_tl_q2, dps=50)}")
        print(f"s_Haar = H_vN(diag(p+, p-))  = {fmt(s_haar, dps=50)}")
        print(f"s_[3]  = ln [3]_q0           = {fmt(s_q3, dps=50)}")
        print(f"s_star(q_0) [full tower]     = {fmt(s_star_q0, dps=50)}")
        print(f"gamma_star(q_0) = s*/(2*pi)  = {fmt(gamma_star_q0, dps=50)} (vs classical {fmt(gamma_dl_classical, dps=30)})")
        print(f"gamma_star(q_0) / hbar_q0    = {fmt(gamma_star_over_hbar_q0, dps=25)}")
        print("\n--- Required Lock Targets a_0* = 4 * s_punct ---")
        print(f"4 * ln 2                     = {fmt(a0_star_cat, dps=50)}")
        print(f"4 * ln [2]_q0                = {fmt(a0_star_tl, dps=50)}")
        print(f"4 * s_Haar(q_0)              = {fmt(a0_star_haar, dps=50)}")
        print(f"4 * ln [3]_q0                = {fmt(a0_star_q3, dps=50)}")
        print("\n--- Un-tuned Candidate Area Quanta vs 1/4 = 0.25 ---")
        for k, row in candidate_evaluation.items():
            print(
                f"  {k:<32} a0={row['a0_value'][:14]}  "
                f"S/A(Cat)={row['S_over_A_catalan_ln2'][:12]} ({row['rel_diff_vs_quarter_catalan'][:9]})  "
                f"S/A(TL)={row['S_over_A_tl_ln_q2'][:12]} ({row['rel_diff_vs_quarter_tl_q2'][:9]})"
            )
        print(f"\nWitness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
