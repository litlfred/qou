#!/usr/bin/env python3
"""Electroweak Analog of the Bring Genus (1/π) + 1-Loop Schwinger Fixed-Point Probe.

Verifies at 50-dps mpmath precision (zero float64 in computations or witness) all
identities and predictions formalized in
`QOU/StandardModel/ElectroweakBringSchwingerBridge.lean`:

1. **Torus-Link Plancherel Trace Polynomials `P_m(h)` (`m = 1, 2, 3, 4`)**:
   - Exact Chebyshev/Laurent identity:
     `2 · P_m(q - q⁻¹) = (q^{2m+1} + q^{-(2m+1)}) / (q + q⁻¹)`
     for `W = T(2,4)` (`m=2`), `Z = T(2,6)` (`m=3`), `H = T(2,8)` (`m=4`).
   - Quantum-dimension dressing identity:
     `([2]_q / 2)² = 1 + h²/4`.

2. **Electroweak VEV `v = (√2 G_F)^{-1/2}` & Fermi Constant `G_F` Fixed-Point Cubic**:
   - Tree crossing complexity (Table 1 of `electroweak-higgs-torus-link-triplet`):
     `N_v^bare(q₀) = q₀ · [4]_{q₀} · [6]_{q₀} · [8]_{q₀} = 260.679866939...`
   - 2-strand quantum-dimension dressed tree complexity:
     `N_v^tree(q₀) = q₀ · ([2]_{q₀}/2) · [4]_{q₀} · [6]_{q₀} · [8]_{q₀} = 262.100163821...`
   - Bring Seifert-Hodge zero-mode for `{T(2,4), T(2,6), T(2,8)}` (`g_W+g_Z+g_H = 1+2+3 = 6`):
     `2(g_W + g_Z + g_H) / Area(Σ₄) = 12 / (12π) = 1 / π = (3/2) · (2/(3π)) = 0.318309886...`
   - 1-loop Schwinger/Habiro self-consistency fixed-point equation (`α_v = 1/N_v = m_p/v`):
     `1 / α_v = T_EW(q₀) - α_v · H · (1 - ℏ_q² · α_v)`, `H = [2]_{q₀}/(8π)`.
   - Solution at proton-pinned `q₀`:
     `N_v = 262.418168819...` (vs `v_exp / m_p = 262.418176527...`, `-29.37 ppb`, `-0.114 σ`),
     `v   = 246.219643562... GeV` (vs `246.219650794(63) GeV`, `-29.37 ppb`, `-0.114 σ`),
     `G_F = 1.1663787685... × 10^{-5} GeV^{-2}` (vs `1.1663787(6) × 10^{-5} GeV^{-2}`, `+58.74 ppb`, `+0.114 σ`).

3. **Reconciliation of `W`-Anchor and `Z`-Anchor Higgs Mass Predictions & `m_Z / m_W` Ratio**:
   - Dressing the `W → Z` genus step by `([2]_{q₀}/2)² = 1 + h₀²/4` gives
     `m_Z / m_W = (P₃(h₀)/P₂(h₀)) · ([2]_{q₀}/2)² = 1.134806999` (vs PDG `1.134608780`, `+174.7 ppm = +1.06 σ_W`).
   - Resolves the 1.07% discrepancy between the `W`-anchored and `Z`-anchored Higgs mass
     predictions in `higgs_categorical_mass_formula_attempt.py`, collapsing their gap from
     `1.34 GeV` (`10726 ppm`) down to `21.9 MeV` (`174.7 ppm`), with both landing inside the
     PDG `125.20 ± 0.11 GeV` window under the parameter-free 1-loop / Bring zero-mode factors.
"""
from __future__ import annotations

import os
import sys
from math import comb
from pathlib import Path

THIS = Path(__file__).resolve()
COMPUTE_DIR = THIS.parent.parent
sys.path.insert(0, str(COMPUTE_DIR))
sys.path.insert(0, str(COMPUTE_DIR / "substrate"))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_E_MEV, M_P_MEV_VALIDATION  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()


def qbal(k: int, q: mpf) -> mpf:
    """Balanced quantum integer [k]_q = (q^k - q^{-k}) / (q - q^{-1})."""
    return (q ** k - q ** (-k)) / (q - mpf(1) / q)


def trace_poly_P(m: int, h: mpf) -> mpf:
    """Binomial trace polynomial P_m(h) = Σ_{j=0}^m (1/2) C(m+j, 2j) h^{2j}."""
    return sum(mpf(comb(m + j, 2 * j)) / mpf(2) * h ** (2 * j) for j in range(m + 1))


def main() -> None:
    q0 = mpf(Q_50_DIGIT_STR)
    h0 = q0 - mpf(1) / q0
    hbar_q = (q0 - mpf(1)) / q0
    pi = mp.pi
    G_cat = mp.catalan

    # Physical constants (CODATA 2022 / PDG 2024)
    m_p_gev = M_P_MEV_VALIDATION / mpf(1000)
    m_e_gev = M_E_MEV / mpf(1000)
    G_F_exp = mpf("1.1663787e-5")       # GeV^-2 (PDG 2024)
    G_F_sig = mpf("0.0000006e-5")       # GeV^-2 (0.514 ppm)
    v_exp = mpf(1) / mp.sqrt(mp.sqrt(mpf(2)) * G_F_exp)
    v_sig = v_exp * G_F_sig / (mpf(2) * G_F_exp)

    m_Z_exp = mpf("91.1876")            # GeV (PDG 2024)
    m_Z_sig = mpf("0.0021")             # GeV (23.0 ppm)
    m_W_exp = mpf("80.3692")            # GeV (PDG 2024 world average)
    m_W_sig = mpf("0.0133")             # GeV (165.5 ppm)
    m_H_exp = mpf("125.20")             # GeV (PDG 2024)
    m_H_sig = mpf("0.11")               # GeV (878.6 ppm)

    alpha_inv_codata = mpf("137.035999177")
    alpha_codata = mpf(1) / alpha_inv_codata

    wb = (
        WitnessBuilder("electroweak-bring-schwinger-bridge", engine="mpmath")
        .set_description(
            "50-dps verification of QOU/StandardModel/ElectroweakBringSchwingerBridge.lean: "
            "2-strand torus-link Plancherel trace polynomials P_m(h), quantum-dimension "
            "dressing ([2]_q/2)^2 = 1 + h^2/4, electroweak Bring Seifert-Hodge zero-mode "
            "1/pi = 2(g_W+g_Z+g_H)/(4*pi*(g_Bring-1)), 1-loop Schwinger fixed-point cubic "
            "for N_v = v/m_p and G_F, and W/Z-anchor reconciliation for m_H."
        )
    )

    # 1. Verify Laurent identities for P_m(h) (m = 1, 2, 3, 4) and ([2]_q/2)^2 = 1 + h^2/4
    P_vals = {}
    for m in (1, 2, 3, 4):
        pm = trace_poly_P(m, h0)
        P_vals[m] = pm
        lhs = (q0 + mpf(1) / q0) * (mpf(2) * pm)
        rhs = q0 ** (2 * m + 1) + q0 ** (-(2 * m + 1))
        wb.add_assertion(
            name=f"twoMulP{m}_laurent_identity",
            computed=fmt(lhs),
            expected=fmt(rhs),
            tolerance="1e-45",
            source=f"ElectroweakBringSchwingerBridge.twoMulP{m}_laurent",
        )

    q2 = qbal(2, q0)
    q4 = qbal(4, q0)
    q6 = qbal(6, q0)
    q8 = qbal(8, q0)
    q9 = qbal(9, q0)
    q10 = qbal(10, q0)

    wb.add_assertion(
        name="qInt2_sq_eq_h_sq_add_four",
        computed=fmt(q2 ** 2),
        expected=fmt(h0 ** 2 + mpf(4)),
        tolerance="1e-45",
        source="ElectroweakBringSchwingerBridge.qInt2_sq_eq_h_sq_add_four",
    )

    # 2. Verify Bring Seifert-Hodge zero-mode 1/pi = (3/2) * (2/(3*pi))
    bring_zero_em = mpf(2) / (mpf(3) * pi)
    gauss_bonnet_g4 = mpf(4) * pi * (mpf(4) - mpf(1))
    ew_seifert_genus_sum = mpf(1 + 2 + 3)  # g_W + g_Z + g_H = 6
    ew_bring_zero = (mpf(2) * ew_seifert_genus_sum) / gauss_bonnet_g4

    wb.add_assertion(
        name="ewBringZeroMode_eq_one_div_pi",
        computed=fmt(ew_bring_zero),
        expected=fmt(mpf(1) / pi),
        tolerance="1e-45",
        source="ElectroweakBringSchwingerBridge.ewBringZeroMode_eq_one_div_pi",
    )
    wb.add_assertion(
        name="ewBringZeroMode_eq_three_halves_bringZeroMode",
        computed=fmt(ew_bring_zero),
        expected=fmt((mpf(3) / mpf(2)) * bring_zero_em),
        tolerance="1e-45",
        source="ElectroweakBringSchwingerBridge.ewBringZeroMode_eq_three_halves_bringZeroMode",
    )

    # 3. Electroweak VEV fixed-point cubic: 1/alpha_v = T_EW - alpha_v * H * (1 - hbar_q^2 * alpha_v)
    N_v_exp = v_exp / m_p_gev
    N_v_bare = q0 * q4 * q6 * q8
    N_v_dressed_tree = N_v_bare * (q2 / mpf(2))
    T_EW = N_v_dressed_tree + ew_bring_zero
    H_hab = q2 / (mpf(8) * pi)

    def ew_cubic(alpha_v: mpf) -> mpf:
        return (
            (hbar_q ** 2) * H_hab * (alpha_v ** 3)
            - H_hab * (alpha_v ** 2)
            + T_EW * alpha_v
            - mpf(1)
        )

    alpha_v_root = mp.findroot(ew_cubic, mpf(1) / T_EW)
    N_v_pred = mpf(1) / alpha_v_root
    v_pred_gev = N_v_pred * m_p_gev
    G_F_pred = mpf(1) / (mp.sqrt(mpf(2)) * (v_pred_gev ** 2))

    # Fixed-point equivalence check
    fp_lhs = mpf(1) / alpha_v_root
    fp_rhs = T_EW - alpha_v_root * H_hab * (mpf(1) - (hbar_q ** 2) * alpha_v_root)
    wb.add_assertion(
        name="ewFixedPoint_iff_cubic_residual",
        computed=fmt(fp_lhs),
        expected=fmt(fp_rhs),
        tolerance="1e-45",
        source="ElectroweakBringSchwingerBridge.ewFixedPoint_iff_cubic",
    )
    wb.add_assertion(
        name="ew_vev_within_1sigma_codata",
        computed=fmt(v_pred_gev),
        expected=fmt(v_exp),
        tolerance=fmt(v_sig),
        source="Electroweak VEV fixed-point prediction vs CODATA/PDG G_F (+/- 0.514 ppm)",
    )

    v_err_ppb = (v_pred_gev - v_exp) / v_exp * mpf("1e9")
    v_err_sigma = (v_pred_gev - v_exp) / v_sig
    GF_err_ppb = (G_F_pred - G_F_exp) / G_F_exp * mpf("1e9")
    GF_err_sigma = (G_F_pred - G_F_exp) / G_F_sig

    # 4. Z/W Mass Ratio and Higgs Mass W/Z-Anchor Reconciliation
    P2, P3, P4 = P_vals[2], P_vals[3], P_vals[4]
    r_ZW_exp = m_Z_exp / m_W_exp
    r_ZW_bare = P3 / P2
    r_ZW_dressed = (P3 / P2) * ((q2 / mpf(2)) ** 2)
    m_W_pred_from_Z = m_Z_exp / r_ZW_dressed
    m_Z_pred_from_W = m_W_exp * r_ZW_dressed

    six_fifths = mpf(6) / mpf(5)
    # Exact algebraic reconciliation when m_Z = m_W_pred_from_Z:
    mH_from_W_exact_Z = m_W_pred_from_Z * (P4 / P2) * six_fifths * (q2 / mpf(2))
    mH_from_Z_exact_Z = m_Z_exp * (P4 / P3) * six_fifths * (mpf(2) / q2)
    wb.add_assertion(
        name="higgs_W_Z_anchor_reconciliation_exact",
        computed=fmt(mH_from_W_exact_Z),
        expected=fmt(mH_from_Z_exact_Z),
        tolerance="1e-45",
        source="ElectroweakBringSchwingerBridge.higgs_W_Z_anchor_reconciliation",
    )

    # Evaluate Higgs mass candidates from experimental m_W and m_Z
    higgs_variants = {}
    for key, label, loop_factor in [
        ("tree_dressed", "Tree dressed: (6/5)*([2]_q/2)^{±1}", mpf(1)),
        ("bring_zero_hbar2", "Bring zero-mode: 1 - (2/(3*pi))*hbar_q^2", mpf(1) - bring_zero_em * (hbar_q ** 2)),
        ("schwinger_1loop_alpha_pi", "1-loop Schwinger: 1 - alpha_EM/pi", mpf(1) - alpha_codata / pi),
        ("habiro_half_h2", "Half-Habiro: 1 - ([2]_q/(16*pi))*h_0^2", mpf(1) - (H_hab / mpf(2)) * (h0 ** 2)),
        ("catalan_G_h4", "Octahedral volume: 1 - G*h_0^4", mpf(1) - G_cat * (h0 ** 4)),
        ("catalan_2G_h4", "Borromean volume: 1 - 2*G*h_0^4", mpf(1) - mpf(2) * G_cat * (h0 ** 4)),
        ("habiro_full_h2", "Full-Habiro: 1 - ([2]_q/(8*pi))*h_0^2", mpf(1) - H_hab * (h0 ** 2)),
    ]:
        mH_W = m_W_exp * (P4 / P2) * six_fifths * (q2 / mpf(2)) * loop_factor
        mH_Z = m_Z_exp * (P4 / P3) * six_fifths * (mpf(2) / q2) * loop_factor
        higgs_variants[key] = {
            "label": label,
            "loop_factor": fmt(loop_factor),
            "m_H_from_W_GeV": fmt(mH_W),
            "m_H_from_Z_GeV": fmt(mH_Z),
            "anchor_spread_MeV": fmt(abs(mH_W - mH_Z) * mpf(1000)),
            "err_W_ppm": fmt((mH_W - m_H_exp) / m_H_exp * mpf("1e6")),
            "err_Z_ppm": fmt((mH_Z - m_H_exp) / m_H_exp * mpf("1e6")),
            "err_W_sigma": fmt((mH_W - m_H_exp) / m_H_sig),
            "err_Z_sigma": fmt((mH_Z - m_H_exp) / m_H_sig),
        }

    wb.add_data("electroweak_vev_fixed_point", {
        "N_v_bare_q4_q6_q8": fmt(N_v_bare),
        "N_v_dressed_tree": fmt(N_v_dressed_tree),
        "ew_bring_zero_mode_1_div_pi": fmt(ew_bring_zero),
        "T_EW_const": fmt(T_EW),
        "H_habiro_norm": fmt(H_hab),
        "N_v_fixed_point_pred": fmt(N_v_pred),
        "N_v_exp_v_over_mp": fmt(N_v_exp),
        "v_pred_GeV": fmt(v_pred_gev),
        "v_exp_GeV": fmt(v_exp),
        "v_sigma_exp_GeV": fmt(v_sig),
        "v_err_ppb": fmt(v_err_ppb),
        "v_err_sigma": fmt(v_err_sigma),
        "G_F_pred_GeV_inv2": fmt(G_F_pred),
        "G_F_exp_GeV_inv2": fmt(G_F_exp),
        "G_F_err_ppb": fmt(GF_err_ppb),
        "G_F_err_sigma": fmt(GF_err_sigma),
    })
    wb.add_data("zw_mass_ratio", {
        "P2_at_h0": fmt(P2),
        "P3_at_h0": fmt(P3),
        "P4_at_h0": fmt(P4),
        "qInt2_over_2_sq": fmt((q2 / mpf(2)) ** 2),
        "r_ZW_bare_P3_div_P2": fmt(r_ZW_bare),
        "r_ZW_dressed": fmt(r_ZW_dressed),
        "r_ZW_exp": fmt(r_ZW_exp),
        "r_ZW_err_ppm": fmt((r_ZW_dressed - r_ZW_exp) / r_ZW_exp * mpf("1e6")),
        "m_W_pred_from_Z_GeV": fmt(m_W_pred_from_Z),
        "m_W_exp_GeV": fmt(m_W_exp),
        "m_W_pred_err_sigma": fmt((m_W_pred_from_Z - m_W_exp) / m_W_sig),
        "m_Z_pred_from_W_GeV": fmt(m_Z_pred_from_W),
        "m_Z_exp_GeV": fmt(m_Z_exp),
    })
    wb.add_data("higgs_mass_variants", higgs_variants)

    out_path = wb.save()

    print("=" * 92)
    print("ELECTROWEAK ANALOG OF BRING GENUS (1/pi) + 1-LOOP SCHWINGER FIXED POINT (50 dps)")
    print("=" * 92)
    print(f"  N_v^bare  = q0*[4][6][8]                  = {mp.nstr(N_v_bare, 16)}")
    print(f"  N_v^tree  = q0*([2]/2)*[4][6][8]          = {mp.nstr(N_v_dressed_tree, 16)}")
    print(f"  Bring EW zero-mode = 12/(12*pi) = 1/pi    = {mp.nstr(ew_bring_zero, 16)}")
    print(f"  T_EW = N_v^tree + 1/pi                    = {mp.nstr(T_EW, 16)}")
    print(f"  1-loop fixed-point root N_v               = {mp.nstr(N_v_pred, 16)}")
    print(f"  Experimental N_v = v_exp / m_p            = {mp.nstr(N_v_exp, 16)}")
    print(f"  Predicted VEV v = N_v * m_p               = {mp.nstr(v_pred_gev, 14)} GeV  (err: {float(v_err_ppb):+.2f} ppb = {float(v_err_sigma):+.3f} sigma)")
    print(f"  Predicted G_F = 1/(sqrt(2)*v^2)           = {mp.nstr(G_F_pred, 14)} GeV^-2 (err: {float(GF_err_ppb):+.2f} ppb = {float(GF_err_sigma):+.3f} sigma)")
    print(f"  Predicted m_W from m_Z                    = {mp.nstr(m_W_pred_from_Z, 10)} GeV  (exp: 80.3692 +/- 0.0133 GeV, {float((m_W_pred_from_Z-m_W_exp)/m_W_sig):+.2f} sigma_W)")
    print(f"  Witness written to: {out_path}")


if __name__ == "__main__":
    main()
