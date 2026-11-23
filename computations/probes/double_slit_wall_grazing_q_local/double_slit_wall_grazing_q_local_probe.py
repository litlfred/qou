#!/usr/bin/env python3
"""80-dps evaluation of the parameter-free wall-grazing `q_local(y)` aperture
integral across the Bach et al. (2013) gold-coated silicon double-slit (`a = 50 nm`
and `a = 62 nm`), retiring the un-derived `q = 1.020` slider claim.

Bean `qou-x9tm`. Pre-registered in `PREREGISTRATION.md` (commit `3004225fb9c`)
BEFORE running any numerical evaluation.

References:
  - Roger Bach, Damian Pope, Sy-Hwang Liou & Herman Batelaan,
    "Controlled double-slit electron diffraction", New J. Phys. 15, 033018 (2013)
  - `folio/quantum-observable-universe/observations/proton-gravity-tests-intro.md`
  - `folio/quantum-observable-universe/observations/w-boson-mass-discrepancy.md`
  - `folio/quantum-observable-universe/observations/double-slit-analytical.md`

Precision & anti-fit discipline:
  - `mpmath` at `workdps = 80` (`OUT_DPS = 50` serialized),
  - `q0Anchor = "proton"` (`qou_substrate.constants.q_at(80)`),
  - Form-B Bring-Schwinger `alpha_q` (`1/alpha_q = 137.035999127...`, ZERO CODATA alpha_EM),
  - CAL-1 `m_e` (`lambda_bar_{C,e} = hbar*c / m_e`), CAL-3 `m_{pi+-} = 139.57039 MeV`
    (`r_pi = hbar*c / m_{pi+-}`),
  - zero `float64` imports, literals, or casts, zero fitted parameters.
"""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT / "tools" / "qou-substrate" / "python") not in sys.path:
    sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
if str(_ROOT / "computations") not in sys.path:
    sys.path.insert(0, str(_ROOT / "computations"))

import mpmath as mp  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import q_at  # noqa: E402
from qou_substrate.precision import fmt, set_compute_dps  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

WORK_DPS = 80
OUT_DPS = 50
set_compute_dps(WORK_DPS)

M_PI_CHARGED_MEV = mp.mpf("139.57039")
RETIRED_SLIDER_DELTA_Q = mp.mpf("0.020")  # retired un-derived q = 1.020 slider offset


def solve_form_b_alpha_inv(q_val: mp.mpf) -> mp.mpf:
    """Solve QOU Form-B Bring-Schwinger cubic for `alpha_EM^{-1}(q)` at 85 dps."""
    with mp.workdps(85):
        q = mp.mpf(q_val)
        one = mp.mpf(1)
        h = q - one / q
        h2 = h * h
        two_q = q + one / q
        q9 = (q ** 9 - q ** (-9)) / h
        q10 = (q ** 10 - q ** (-10)) / h
        t_term = q * q9 * q10 + mp.mpf(2) / (mp.mpf(3) * mp.pi)
        h_term = two_q / (mp.mpf(8) * mp.pi)
        a = (-t_term + mp.sqrt(t_term * t_term + mp.mpf(4) * h_term)) / (
            mp.mpf(2) * h_term
        )
        for _ in range(35):
            fa = -h_term * h2 * (a ** 3) + h_term * (a ** 2) + t_term * a - one
            dfa = (
                -mp.mpf(3) * h_term * h2 * (a ** 2)
                + mp.mpf(2) * h_term * a
                + t_term
            )
            da = fa / dfa
            a -= da
            if abs(da) < mp.mpf(10) ** (-80):
                break
        return one / a


def evaluate_aperture_grazing_case(
    a_nm_str: str,
    d_nm_str: str,
    l_screen_m_str: str,
    lam_db_pm: mp.mpf,
    ell_fm: mp.mpf,
    dq_wall: mp.mpf,
) -> dict[str, object]:
    """Analytical + 80-dps Gauss-Legendre quadrature aperture average of q_local(y) - 1."""
    one = mp.mpf(1)
    two = mp.mpf(2)
    a_fm = mp.mpf(a_nm_str) * mp.mpf("1e6")  # 1 nm = 1e6 fm
    d_m = mp.mpf(d_nm_str) * mp.mpf("1e-9")
    a_m = mp.mpf(a_nm_str) * mp.mpf("1e-9")
    l_m = mp.mpf(l_screen_m_str)
    lam_m = lam_db_pm * mp.mpf("1e-12")

    u_max = a_fm / ell_fm
    exp_neg_u = mp.exp(-u_max)
    exp_neg_2u = mp.exp(-two * u_max)

    # Exact analytical integral over y in [-a/2, +a/2]:
    #   q_local(y) - 1 = dq_wall * (exp(-(a/2 - y)/ell) + exp(-(a/2 + y)/ell))
    avg_dq = dq_wall * (two * ell_fm / a_fm) * (one - exp_neg_u)
    avg_dq2_minus_1 = two * avg_dq + (dq_wall * dq_wall) * (
        (ell_fm / a_fm) * (one - exp_neg_2u) + two * exp_neg_u
    )

    # Midpoint value at slit centre y = 0: 2 * dq_wall * exp(-a / (2 * ell))
    center_dq = two * dq_wall * mp.exp(-u_max / two)

    # Independent 80-dps Gauss-Legendre quadrature cross-check via u = (a/2 - y)/ell in [0, u_max]:
    #   (1/a) int_{-a/2}^{a/2} dq_wall (e^{-(a/2-y)/ell} + e^{-(a/2+y)/ell}) dy
    #   = (2 * dq_wall * ell / a) * int_0^{u_max} e^{-u} du
    # Split [0, min(u_max, 250)] + [min(u_max, 250), u_max] so e^{-u} boundary layer is resolved to 1e-80:
    u_split = min(u_max, mp.mpf(250))
    quad_i1 = mp.quad(lambda u: mp.exp(-u), [mp.mpf(0), u_split])
    quad_i2 = (
        mp.quad(lambda u: mp.exp(-u), [u_split, u_max])
        if u_max > u_split
        else mp.mpf(0)
    )
    avg_dq_quad = (two * dq_wall * ell_fm / a_fm) * (quad_i1 + quad_i2)
    quad_rel_err = abs(avg_dq - avg_dq_quad) / avg_dq

    # Standard vs wall-grazing fringe spacing and single-slit envelope half-width
    fringe_std_um = (lam_m * l_m / d_m) * mp.mpf("1e6")
    envelope_std_mm = (lam_m * l_m / a_m) * mp.mpf("1e3")
    delta_fringe_fm = fringe_std_um * mp.mpf("1e9") * avg_dq  # 1 um = 1e9 fm
    delta_envelope_pm = envelope_std_mm * mp.mpf("1e9") * avg_dq2_minus_1  # 1 mm = 1e9 pm

    suppression_vs_retired_1p020 = RETIRED_SLIDER_DELTA_Q / avg_dq

    return {
        "raw": {
            "avg_dq": avg_dq,
            "avg_dq2_minus_1": avg_dq2_minus_1,
            "quad_rel_err": quad_rel_err,
            "suppression_vs_retired": suppression_vs_retired_1p020,
        },
        "serialized": {
            "slit_width_nm": a_nm_str,
            "slit_separation_nm": d_nm_str,
            "decay_length_fm": fmt(ell_fm, dps=30),
            "wall_delta_q": fmt(dq_wall, dps=30),
            "aspect_ratio_a_over_ell": fmt(u_max, dps=20),
            "center_q_minus_1_at_y0": fmt(center_dq, dps=15),
            "aperture_avg_q_local_minus_1": fmt(avg_dq, dps=OUT_DPS),
            "q_eff_aperture": fmt(one + avg_dq, dps=OUT_DPS),
            "fractional_fringe_shift": fmt(avg_dq, dps=30),
            "fractional_hodge_envelope_shift_q2_minus_1": fmt(avg_dq2_minus_1, dps=30),
            "fringe_spacing_std_um": fmt(fringe_std_um, dps=20),
            "predicted_fringe_shift_fm": fmt(delta_fringe_fm, dps=20),
            "envelope_halfwidth_std_mm": fmt(envelope_std_mm, dps=20),
            "predicted_envelope_shift_pm": fmt(delta_envelope_pm, dps=20),
            "quadrature_rel_residual": fmt(quad_rel_err, dps=15),
            "retired_1p020_over_predicted_ratio": fmt(suppression_vs_retired_1p020, dps=15),
            "log10_retired_over_predicted_dex": fmt(
                mp.log10(suppression_vs_retired_1p020), dps=12
            ),
        },
    }


def main() -> int:
    with mp.workdps(WORK_DPS):
        q0 = q_at(dps=WORK_DPS)
        one = mp.mpf(1)
        two = mp.mpf(2)

        h_j_s = codata("Planck constant").value
        hbar_j_s = h_j_s / (two * mp.pi)
        c_m_s = codata("speed of light in vacuum").value
        e_c = codata("elementary charge").value
        hbar_c_mev_fm = (hbar_j_s * c_m_s / (e_c * mp.mpf("1e6"))) * mp.mpf("1e15")
        m_e_mev = codata("electron mass energy equivalent in mev").value

        alpha_q_inv = solve_form_b_alpha_inv(q0)
        alpha_q = one / alpha_q_inv

        # Relativistic 600 eV electron de Broglie wavelength (Bach et al. 2013)
        k_600_mev = mp.mpf("600e-6")
        p_600_c_mev = mp.sqrt(k_600_mev * (k_600_mev + two * m_e_mev))
        lam_db_600_pm = (two * mp.pi * hbar_c_mev_fm * mp.mpf("1e-3")) / p_600_c_mev

        # CAL-3 pion reduced Compton length & CAL-1 electron Compton lengths
        r_pi_fm = hbar_c_mev_fm / M_PI_CHARGED_MEV
        lambda_bar_ce_fm = hbar_c_mev_fm / m_e_mev
        lambda_full_ce_fm = two * mp.pi * lambda_bar_ce_fm

        # Pre-registered wall boundary amplitudes (zero fitted parameters)
        dq_w1_saturating = q0 - one
        dq_w2_em_vertex = (q0 - one) * (alpha_q / (two * mp.pi)) / mp.mpf(6)

        geometries = (
            ("a50nm_sim_default", "50", "280", "0.24"),
            ("a62nm_bach2013_physical", "62", "272", "0.24"),
        )
        lengths = (
            ("L1_pion_Compton_r_pi", r_pi_fm),
            ("L2_electron_reduced_Compton", lambda_bar_ce_fm),
            ("L2b_electron_full_Compton_2pi", lambda_full_ce_fm),
        )
        walls = (
            ("W1_saturating_core_q0_minus_1", dq_w1_saturating),
            ("W2_EM_vertex_projected", dq_w2_em_vertex),
        )

        cases: dict[str, dict[str, object]] = {}
        max_quad_rel_err = mp.mpf(0)
        for g_name, a_nm, d_nm, l_m in geometries:
            for l_name, ell_val in lengths:
                for w_name, dq_val in walls:
                    key = f"{g_name}__{l_name}__{w_name}"
                    res = evaluate_aperture_grazing_case(
                        a_nm_str=a_nm,
                        d_nm_str=d_nm,
                        l_screen_m_str=l_m,
                        lam_db_pm=lam_db_600_pm,
                        ell_fm=ell_val,
                        dq_wall=dq_val,
                    )
                    cases[key] = res
                    max_quad_rel_err = max(max_quad_rel_err, res["raw"]["quad_rel_err"])

        # Key headline numbers at a = 50 nm
        yukawa_50_w1 = cases[
            "a50nm_sim_default__L1_pion_Compton_r_pi__W1_saturating_core_q0_minus_1"
        ]["raw"]["avg_dq"]
        compton_50_w1 = cases[
            "a50nm_sim_default__L2_electron_reduced_Compton__W1_saturating_core_q0_minus_1"
        ]["raw"]["avg_dq"]
        compton_50_w2 = cases[
            "a50nm_sim_default__L2_electron_reduced_Compton__W2_EM_vertex_projected"
        ]["raw"]["avg_dq"]

        yukawa_62_w1 = cases[
            "a62nm_bach2013_physical__L1_pion_Compton_r_pi__W1_saturating_core_q0_minus_1"
        ]["raw"]["avg_dq"]
        compton_62_w1 = cases[
            "a62nm_bach2013_physical__L2_electron_reduced_Compton__W1_saturating_core_q0_minus_1"
        ]["raw"]["avg_dq"]

        codata_rce_fm = codata("reduced Compton wavelength").value * mp.mpf("1e15")
        assert max_quad_rel_err < mp.mpf("1e-75")
        assert abs(r_pi_fm - mp.mpf("1.4138169311")) < mp.mpf("1e-9")
        assert abs(lambda_bar_ce_fm - codata_rce_fm) < mp.mpf("1e-8")
        assert yukawa_50_w1 < mp.mpf("1e-8")
        assert compton_50_w1 < mp.mpf("2e-6")

        print("=== qou-x9tm: Bach (2013) Double-Slit Wall-Grazing q_local(y) Evaluation (80 dps) ===")
        print(f"  q0 (proton pin)               = {fmt(q0, dps=30)}")
        print(f"  1/alpha_q (Form B)            = {fmt(alpha_q_inv, dps=20)}")
        print(f"  600 eV lambda_dB (rel) [pm]   = {fmt(lam_db_600_pm, dps=20)}")
        print(f"  r_pi = hbar*c/m_pi [fm]       = {fmt(r_pi_fm, dps=20)}")
        print(f"  lambda_bar_C,e [fm]           = {fmt(lambda_bar_ce_fm, dps=20)}")
        print(f"  W1 saturating dq = q0 - 1     = {fmt(dq_w1_saturating, dps=20)}")
        print(f"  W2 EM vertex dq               = {fmt(dq_w2_em_vertex, dps=20)}")
        print(f"  max quadrature rel residual   = {fmt(max_quad_rel_err, dps=12)}")
        print()
        print("  -- Aperture-averaged <q_local - 1>_a (fractional fringe shift) --")
        for key, res in cases.items():
            s = res["serialized"]
            print(
                f"    {key:<78} <q-1> = {s['aperture_avg_q_local_minus_1'][:18]:<18} "
                f"(retired/pred = 10^{s['log10_retired_over_predicted_dex'][:6]})"
            )

        wb = WitnessBuilder(Path(__file__).stem, engine="mpmath")
        wb.set_description(
            "80-dps (50-dps serialized) aperture-averaged Yukawa/Compton wall-grazing "
            "q_local(y) evaluation across the a = 50 nm simulator default and a = 62 nm "
            "Bach et al. (2013) 600 eV electron double-slit apertures, proving that "
            "parameter-free <q_local - 1>_a lies between 1.2e-13 and 1.70e-6 (4 to 11 "
            "orders of magnitude below the retired un-derived q = 1.020 slider offset; "
            "Bean qou-x9tm)."
        )
        wb.set_content_block("sim:double-slit-analytical")
        wb.add_parameter("q0", fmt(q0, dps=OUT_DPS))
        wb.add_parameter("q0_pin", "proton (qou_substrate.constants.q_at)")
        wb.add_parameter("work_dps", WORK_DPS)
        wb.add_parameter("output_dps", OUT_DPS)
        wb.add_parameter("alpha_EM_inv_FormB", fmt(alpha_q_inv, dps=OUT_DPS))
        wb.add_parameter("r_pi_CAL3_fm", fmt(r_pi_fm, dps=OUT_DPS))
        wb.add_parameter("lambda_bar_Ce_CAL1_fm", fmt(lambda_bar_ce_fm, dps=OUT_DPS))
        wb.add_parameter("lambda_dB_600eV_rel_pm", fmt(lam_db_600_pm, dps=OUT_DPS))

        wb.add_data(
            "headline_a50nm",
            {
                "yukawa_r_pi_saturating_avg_q_minus_1": fmt(yukawa_50_w1, dps=OUT_DPS),
                "electron_compton_saturating_avg_q_minus_1": fmt(compton_50_w1, dps=OUT_DPS),
                "electron_compton_em_vertex_avg_q_minus_1": fmt(compton_50_w2, dps=OUT_DPS),
                "retired_slider_q_minus_1": fmt(RETIRED_SLIDER_DELTA_Q, dps=10),
            },
        )
        wb.add_data(
            "headline_a62nm_bach2013",
            {
                "yukawa_r_pi_saturating_avg_q_minus_1": fmt(yukawa_62_w1, dps=OUT_DPS),
                "electron_compton_saturating_avg_q_minus_1": fmt(compton_62_w1, dps=OUT_DPS),
            },
        )
        wb.add_data(
            "all_cases",
            {key: res["serialized"] for key, res in cases.items()},
        )

        wb.add_assertion(
            "quadrature_matches_analytical_aperture_integral",
            fmt(max_quad_rel_err, dps=15),
            "0",
            "1e-70",
            source="80-dps Gauss-Legendre quadrature vs closed-form (2*ell/a)*(1 - exp(-a/ell))",
        )
        wb.add_assertion(
            "yukawa_r_pi_a50nm_saturating_avg_q_minus_1",
            fmt(yukawa_50_w1, dps=12),
            "6.2195843e-9",
            "1e-14",
            source="(q0 - 1) * (2 * r_pi / 50 nm) * (1 - exp(-50 nm / r_pi))",
        )
        wb.add_assertion(
            "electron_compton_a50nm_saturating_avg_q_minus_1",
            fmt(compton_50_w1, dps=12),
            "1.6987704e-6",
            "1e-11",
            source="(q0 - 1) * (2 * lambda_bar_{C,e} / 50 nm) * (1 - exp(-50 nm / lambda_bar_{C,e}))",
        )

        wb.add_caveat(
            "Even at the saturating core upper bound Delta q_wall = q0 - 1, the "
            "aperture-averaged shift across a = 50 nm is 6.22e-9 (pion Yukawa r_pi) to "
            "1.70e-6 (electron reduced Compton lambda_bar_{C,e}), 4 to 6 orders of "
            "magnitude smaller than the retired un-derived q = 1.020 slider setting."
        )

        out = wb.save({"q0Anchor": "proton", "q0Value": fmt(q0, dps=OUT_DPS)})
        print(f"\nwitness -> {out}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
