#!/usr/bin/env python3
"""50-dps Verification Probe for QOU/Archimedean/BringSchwingerNormalizationDerivation.lean.

Evaluates and verifies at >= 50-dps mpmath precision (mp.mp.dps = 80, zero float64):
1. First-principles (2,4,5)-hyperbolic-triangle tiling derivation of the Bring 1-loop
   harmonic-1-form normalization H(q) = [2]_q / (8*pi) = [2]_q / (pi * (2 - chi(Sigma_4)))
   and the Single Transcendental Period Theorem (pi-free ratios):
   - EM sector: H(q) / (2/(3*pi)) = 3 * [2]_q / 16
   - EW sector: H(q) / (1/pi)     = [2]_q / 8 = [2]_q / b_1(Sigma_4)
2. Three-way Habiro/skein parameter hierarchy and Kazhdan-Lusztig bar-involution contraction:
   - hbarQ(q)^2 = (1 - q^-1)^2
   - deltaHabiroSq(q) = [2]_q - 2 = -(1 - q)*(1 - q^-1) = q * hbarQ(q)^2
   - hHecke(q)^2 = (q - q^-1)^2 = (q + 1)^2 * hbarQ(q)^2
   - Bar-Hermitian skein 2-vertex contraction:
     S = sigma - sigma^-1 = hHecke(q), S_bar = sigma^-1 - sigma = -hHecke(q),
     1 + alpha * (S * S_bar) = 1 - hHecke(q)^2 * alpha
   - Contrast with raw same-chirality singlet 2-vertex moment excess:
     m_2(q) - 1 = (q^4 - q^2) / (q^2 + 1) > 0 (order (q-1)^1, opposite sign).
3. Transparent 50-dps comparison of all four parameter-free loop-factor variants
   (c = 0 [quadratic], c = hbarQ^2, c = deltaHabiroSq, c = hHecke^2) on BOTH:
   - Electromagnetic inverse fine-structure constant 1/alpha_EM (scored against
     CODATA 2022 registry 137.035999177(21) and CODATA 2018 Cs-recoil 137.035999084(21)),
   - Electroweak VEV crossing count N_v = v / m_p (scored against PDG/CODATA G_F),
   evaluated at BOTH registered pins (q_proton default and q_muon CAL-2 comparison).

Run:
  python3 -u computations/alpha/bring_schwinger_normalization_derivation_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402
from mpmath import mpf  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate import codata as _codata  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION  # noqa: E402
from witness_base import WitnessBuilder, q0_comparison  # noqa: E402

set_compute_dps()
mp.mp.dps = 80


def qbal(n: int, q: mpf) -> mpf:
    """Balanced quantum integer [n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - mpf(1) / q)


def solve_unified_fixed_point(s: mpf, T_const: mpf, H_norm: mpf, c_loop: mpf) -> mpf:
    """Solve 1/alpha = T_const + s * alpha * H_norm * (1 - c_loop * alpha) for alpha > 0."""
    def cubic(alpha: mpf) -> mpf:
        return (
            -s * c_loop * H_norm * (alpha ** 3)
            + s * H_norm * (alpha ** 2)
            + T_const * alpha
            - mpf(1)
        )
    return mp.findroot(cubic, mpf(1) / T_const)


def main() -> int:
    q_proton = mpf(Q_50_DIGIT_STR)
    q_muon = q_muon_at(50)
    pi = mp.pi

    # Physical references (read from CODATA/PDG substrate)
    alpha_entry = _codata.codata("inverse fine-structure constant")
    alpha_inv_c22 = mpf(alpha_entry.value_str)
    alpha_inv_c22_sig = mpf(alpha_entry.uncertainty_str)
    alpha_inv_c22_sig_ppb = alpha_inv_c22_sig / alpha_inv_c22 * mpf("1e9")

    alpha_inv_c18 = mpf("137.035999084")
    alpha_inv_c18_sig = mpf("0.000000021")

    m_p_gev = M_P_MEV_VALIDATION / mpf(1000)
    G_F_exp = mpf("1.1663787e-5")
    G_F_sig = mpf("0.0000006e-5")
    v_exp = mpf(1) / mp.sqrt(mp.sqrt(mpf(2)) * G_F_exp)
    v_sig = v_exp * G_F_sig / (mpf(2) * G_F_exp)
    N_v_exp = v_exp / m_p_gev
    N_v_sig = v_sig / m_p_gev

    wb = WitnessBuilder("bring_schwinger_normalization_derivation_probe", engine="mpmath")
    wb.set_content_block("prop:em-coupling-bring-zero-mode")
    wb.set_description(
        "50-dps verification of QOU/Archimedean/BringSchwingerNormalizationDerivation.lean: "
        "(1) tiling derivation of H(q) = [2]_q/(8*pi) = [2]_q/(pi*(2 - chi(Sigma_4))) from the "
        "(2,4,5) hyperbolic triangle tiling of Bring's curve (F=240, E=360, V=114, chi=-6, b_1=8, "
        "Area=12*pi) and the Single Transcendental Period Theorem (pi-free ratios "
        "H/T0_EM = 3*[2]_q/16 and H/T0_EW = [2]_q/8); "
        "(2) three-way Habiro/skein parameter hierarchy (0 < hbarQ^2 < deltaHabiroSq < 4*hbarQ^2 < hHecke^2) "
        "and Kazhdan-Lusztig bar-Hermitian skein 2-vertex contraction "
        "1 + alpha*(sigma - sigma^-1)*(sigma^-1 - sigma) = 1 - hHecke^2*alpha vs raw same-chirality "
        "singlet moment excess (q^4 - q^2)/(q^2 + 1) > 0; "
        "(3) complete zero-fit comparison of all 4 parameter-free loop variants (c = 0, hbarQ^2, "
        "deltaHabiroSq, hHecke^2) on BOTH 1/alpha_EM and N_v = v/m_p at BOTH q_proton and q_muon."
    )

    # Section 1: Tiling combinatorics & single-period (pi-free) ratios at q_proton
    F_faces = 240
    E_edges = 3 * F_faces // 2
    V_verts = F_faces // 4 + F_faces // 8 + F_faces // 10
    chi_bring = V_verts - E_edges + F_faces
    b1_bring = 2 - chi_bring
    tri_area = pi - (pi / mpf(2) + pi / mpf(4) + pi / mpf(5))
    area_bring = mpf(F_faces) * tri_area

    q2_p = qbal(2, q_proton)
    H_p = (q_proton + mpf(1) / q_proton) / (mpf(8) * pi)
    H_p_tiling = q2_p / (pi * mpf(b1_bring))
    T0_em = mpf(b1_bring) / area_bring
    G_ew = 1 + 2 + 3  # g_W + g_Z + g_H = 6
    T0_ew = mpf(2 * G_ew) / area_bring

    wb.add_assertion(
        name="habiroNorm_tiling_derived",
        computed=fmt(H_p),
        expected=fmt(H_p_tiling),
        tolerance="1e-45",
        source="BringSchwingerNormalizationDerivation.habiroNorm_tiling_derived",
    )
    wb.add_assertion(
        name="habiroNorm_div_bringZeroModeValue_pi_free",
        computed=fmt(H_p / T0_em),
        expected=fmt(mpf(3) * (q_proton + mpf(1) / q_proton) / mpf(16)),
        tolerance="1e-45",
        source="BringSchwingerNormalizationDerivation.habiroNorm_div_bringZeroModeValue",
    )
    wb.add_assertion(
        name="habiroNorm_div_ewBringZeroMode_pi_free",
        computed=fmt(H_p / T0_ew),
        expected=fmt((q_proton + mpf(1) / q_proton) / mpf(b1_bring)),
        tolerance="1e-45",
        source="BringSchwingerNormalizationDerivation.habiroNorm_div_ewBringZeroMode",
    )

    wb.add_data("tiling_and_single_period_identities", {
        "bring_tiling_F_E_V": [F_faces, E_edges, V_verts],
        "bring_tiling_euler_chi": chi_bring,
        "bring_tiling_b1": b1_bring,
        "bring_surface_area_over_pi": fmt(area_bring / pi),
        "T0_EM_2_div_3pi": fmt(T0_em),
        "T0_EW_1_div_pi": fmt(T0_ew),
        "H_habiro_norm_proton": fmt(H_p),
        "ratio_H_over_T0_EM_pi_free": fmt(H_p / T0_em),
        "ratio_H_over_T0_EW_pi_free": fmt(H_p / T0_ew),
    })

    # Section 2: Three-way Habiro/skein parameter hierarchy & bar-involution identities
    hbar_p = mpf(1) - mpf(1) / q_proton
    hbar_p_bar = mpf(1) - q_proton
    h_hecke_p = q_proton - mpf(1) / q_proton
    h_hecke_p_bar = mpf(1) / q_proton - q_proton
    delta_hab_sq_p = (q_proton + mpf(1) / q_proton) - mpf(2)
    singlet_same_chirality_p = (q_proton ** 4 - q_proton ** 2) / (q_proton ** 2 + mpf(1))

    wb.add_assertion(
        name="hHecke_sq_eq_q_add_one_sq_mul_hbarQ_sq",
        computed=fmt(h_hecke_p ** 2),
        expected=fmt(((q_proton + mpf(1)) ** 2) * (hbar_p ** 2)),
        tolerance="1e-45",
        source="BringSchwingerNormalizationDerivation.hHecke_sq_eq_q_add_one_sq_mul_hbarQ_sq",
    )
    wb.add_assertion(
        name="deltaHabiroSq_eq_q_mul_hbarQ_sq",
        computed=fmt(delta_hab_sq_p),
        expected=fmt(q_proton * (hbar_p ** 2)),
        tolerance="1e-45",
        source="BringSchwingerNormalizationDerivation.deltaHabiroSq_eq_q_mul_hbarQ_sq",
    )
    wb.add_assertion(
        name="hHecke_bar_hermitian_product",
        computed=fmt(h_hecke_p * h_hecke_p_bar),
        expected=fmt(-(h_hecke_p ** 2)),
        tolerance="1e-45",
        source="BringSchwingerNormalizationDerivation.hHecke_bar_hermitian_product",
    )
    wb.add_assertion(
        name="hbarQ_bar_product_eq_neg_deltaHabiroSq",
        computed=fmt(hbar_p * hbar_p_bar),
        expected=fmt(-delta_hab_sq_p),
        tolerance="1e-45",
        source="BringSchwingerNormalizationDerivation.hbarQ_bar_product_eq_neg_deltaHabiroSq",
    )

    hierarchy_ok = (
        mpf(0) < (hbar_p ** 2) < delta_hab_sq_p < mpf(4) * (hbar_p ** 2) < (h_hecke_p ** 2)
        and (h_hecke_p * h_hecke_p_bar) < mpf(0)
        and singlet_same_chirality_p > mpf(0)
    )
    wb.add_assertion(
        name="habiro_skein_parameter_hierarchy_of_one_lt",
        computed="1" if hierarchy_ok else "0",
        expected="1",
        tolerance="0.5",
        source="BringSchwingerNormalizationDerivation.habiro_skein_parameter_hierarchy_of_one_lt",
    )

    wb.add_data("habiro_skein_parameters_at_proton_pin", {
        "hbarQ": fmt(hbar_p),
        "hbarQ_sq": fmt(hbar_p ** 2),
        "deltaHabiroSq_qInt2_sub_2": fmt(delta_hab_sq_p),
        "four_mul_hbarQ_sq": fmt(mpf(4) * (hbar_p ** 2)),
        "hHecke": fmt(h_hecke_p),
        "hHecke_sq": fmt(h_hecke_p ** 2),
        "ratio_hHecke_sq_over_hbarQ_sq_eq_q_add_1_sq": fmt((h_hecke_p ** 2) / (hbar_p ** 2)),
        "ratio_deltaHabiroSq_over_hbarQ_sq_eq_q": fmt(delta_hab_sq_p / (hbar_p ** 2)),
        "bar_hermitian_skein_product_h_mul_hbar": fmt(h_hecke_p * h_hecke_p_bar),
        "bar_hermitian_asymmetric_product": fmt(hbar_p * hbar_p_bar),
        "raw_singlet_same_chirality_excess_m2_sub_1": fmt(singlet_same_chirality_p),
    })

    # Section 3: Transparent 4-variant x 2-sector x 2-pin evaluation
    pins = [("proton", q_proton), ("muon", q_muon)]
    comparison_table = {}

    print("=" * 96)
    print("BRING-SCHWINGER 1-LOOP NORMALIZATION & PARAMETER-FREE HABIRO/SKEIN AUDIT (50 dps)")
    print("=" * 96)
    print(f"  Tiling forced invariants : F={F_faces}, E={E_edges}, V={V_verts} => chi={chi_bring}, b_1={b1_bring}, Area=12*pi")
    print(f"  Single-period pi-free EM : H(q_p) / T0_EM = 3*[2]_q/16 = {mp.nstr(H_p / T0_em, 18)}")
    print(f"  Single-period pi-free EW : H(q_p) / T0_EW = [2]_q/8    = {mp.nstr(H_p / T0_ew, 18)}")
    print(f"  Parameter hierarchy (q_p): hbarQ^2        = {mp.nstr(hbar_p ** 2, 16)}")
    print(f"                             deltaHabiroSq  = {mp.nstr(delta_hab_sq_p, 16)}")
    print(f"                             hHecke^2       = {mp.nstr(h_hecke_p ** 2, 16)}")
    print(f"                             raw m2-1 (e_-) = {mp.nstr(singlet_same_chirality_p, 16)} (wrong order/sign)")
    print()

    for pin_name, q_val in pins:
        q2 = qbal(2, q_val)
        q4 = qbal(4, q_val)
        q6 = qbal(6, q_val)
        q8 = qbal(8, q_val)
        q9 = qbal(9, q_val)
        q10 = qbal(10, q_val)

        hbar_v = mpf(1) - mpf(1) / q_val
        delta_v = q2 - mpf(2)
        h_hecke_v = q_val - mpf(1) / q_val

        T_em_tree = q_val * q9 * q10
        T_em_const = T_em_tree + T0_em
        T_ew_tree = q_val * (q2 / mpf(2)) * q4 * q6 * q8
        T_ew_const = T_ew_tree + T0_ew
        H_norm = q2 / (mpf(8) * pi)

        variants = [
            ("c0_quadratic", "Quadratic truncation (c = 0)", mpf(0)),
            ("c_hbarQ_sq", "Asymmetric Iwahori-Hecke hbarQ^2 = (1 - q^-1)^2", hbar_v ** 2),
            ("c_deltaHabiroSq", "Habiro cyclotomic norm delta^2 = [2]_q - 2", delta_v),
            ("c_hHecke_sq", "Balanced Hecke skein h^2 = (q - q^-1)^2", h_hecke_v ** 2),
        ]

        pin_data = {
            "q0": fmt(q_val, 50),
            "T_EM_tree": fmt(T_em_tree),
            "T_EM_const": fmt(T_em_const),
            "T_EW_dressed_tree": fmt(T_ew_tree),
            "T_EW_const": fmt(T_ew_const),
            "H_habiro_norm": fmt(H_norm),
            "em_variants": {},
            "ew_variants": {},
        }

        print(f"--- PIN: {pin_name.upper()} (q = {mp.nstr(q_val, 22)}) ---")
        print("  [A] Electromagnetic Fixed Point: 1/alpha = T_EM + alpha * H * (1 - c * alpha)")
        for key, label, c_val in variants:
            a_root = solve_unified_fixed_point(mpf(1), T_em_const, H_norm, c_val)
            a_inv = mpf(1) / a_root
            err_c22_ppb = (a_inv - alpha_inv_c22) / alpha_inv_c22 * mpf("1e9")
            err_c22_sig = (a_inv - alpha_inv_c22) / alpha_inv_c22_sig
            err_c18_ppb = (a_inv - alpha_inv_c18) / alpha_inv_c18 * mpf("1e9")
            err_c18_sig = (a_inv - alpha_inv_c18) / alpha_inv_c18_sig

            pin_data["em_variants"][key] = {
                "label": label,
                "c_loop": fmt(c_val),
                "alpha_inv_pred": fmt(a_inv),
                "err_vs_codata2022_ppb": fmt(err_c22_ppb),
                "err_vs_codata2022_sigma": fmt(err_c22_sig),
                "err_vs_codata2018_ppb": fmt(err_c18_ppb),
                "err_vs_codata2018_sigma": fmt(err_c18_sig),
            }
            print(
                f"    {key:16s}: 1/alpha = {mp.nstr(a_inv, 16)} | "
                f"vs C22: {mp.nstr(err_c22_ppb, 6):>9s} ppb ({mp.nstr(err_c22_sig, 4):>6s} sig) | "
                f"vs C18: {mp.nstr(err_c18_ppb, 6):>9s} ppb ({mp.nstr(err_c18_sig, 4):>6s} sig)"
            )

        print("  [B] Electroweak VEV Fixed Point: 1/alpha_v = T_EW - alpha_v * H * (1 - c * alpha_v)")
        for key, label, c_val in variants:
            av_root = solve_unified_fixed_point(mpf(-1), T_ew_const, H_norm, c_val)
            N_v_pred = mpf(1) / av_root
            v_pred = N_v_pred * m_p_gev
            err_nv_ppb = (N_v_pred - N_v_exp) / N_v_exp * mpf("1e9")
            err_nv_sig = (N_v_pred - N_v_exp) / N_v_sig

            pin_data["ew_variants"][key] = {
                "label": label,
                "c_loop": fmt(c_val),
                "N_v_pred": fmt(N_v_pred),
                "v_pred_GeV": fmt(v_pred),
                "err_vs_exp_ppb": fmt(err_nv_ppb),
                "err_vs_exp_sigma": fmt(err_nv_sig),
            }
            print(
                f"    {key:16s}: N_v     = {mp.nstr(N_v_pred, 16)} | "
                f"v = {mp.nstr(v_pred, 13)} GeV | "
                f"vs exp: {mp.nstr(err_nv_ppb, 6):>9s} ppb ({mp.nstr(err_nv_sig, 4):>6s} sig)"
            )
        print()
        comparison_table[pin_name] = pin_data

    wb.add_data("four_variant_two_sector_comparison", comparison_table)
    wb.add_data("references", {
        "codata_2022_alpha_inv": alpha_entry.value_str,
        "codata_2022_uncertainty": alpha_entry.uncertainty_str,
        "codata_2022_sigma_ppb": fmt(alpha_inv_c22_sig_ppb),
        "codata_2018_alpha_inv": fmt(alpha_inv_c18),
        "pdg_2024_G_F_GeV_inv2": fmt(G_F_exp),
        "pdg_2024_G_F_uncertainty": fmt(G_F_sig),
        "v_exp_GeV": fmt(v_exp),
        "N_v_exp_v_over_mp": fmt(N_v_exp),
    })

    out_path = wb.save(
        q0_comparison(
            muon=fmt(q_muon, 50),
            proton=fmt(q_proton, 50),
            reason=(
                "audits all four parameter-free Habiro/skein loop-factor variants "
                "(c = 0, hbarQ^2, deltaHabiroSq, hHecke^2) on both 1/alpha_EM and "
                "N_v = v/m_p at both registered pins (q_proton default and q_muon CAL-2)"
            ),
        )
    )
    print(f"  Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
