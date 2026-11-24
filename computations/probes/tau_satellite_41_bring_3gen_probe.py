#!/usr/bin/env python3
"""80-dps SymPy + mpmath Adjudication Probe for N_gen = 3 Bring Fission & Satellite Tau Mass (`qou-gen3` + `qou-htk4`).

Evaluates symbolically in SymPy and numerically at 80 decimal places (`mp.mp.dps = 80`,
zero `float64`, NO FITTING, `q0_comparison` at proton default `q_p` and muon comparison `q_mu`):

1. Unified `N_gen = 3` Bring Complete-Intersection & Composite `T(2,9) -> 3 T(2,3)` Fission Identity:
   - Bring's curve Sigma_4 = V(p_1, p_2, p_3) in P^4 has intersection degree 1*2*3 = 6,
     canonical degree 6, Euler characteristic chi = -6, and genus g = 4 = dim H^{1,0}(Sigma_4).
   - Under Z_3 < S_3 < S_4 < S_5, V_{(4,1)} branches as (2 + 1) + 1 = 3 + 1, matching the
     exact partition of Bring's 4 admissible odd torus windings {3, 5, 7, 9} into 3 three-body-
     indecomposable generation windings {3, 5, 7} + 1 composite fissioning harmonic {9}.

2. Pre-Committed Zero-Parameter 3rd-Generation Tau Mass Catalog (`m_tau / m_e`, zero tuning):
   - Family A (Soma-Agol Satellite JSJ Volumes `P(4_1)`): proves & verifies the topological
     forbidden gap `(Vol(4_1), Vol(4_1) + 4*G_Catalan) = (2.02988, 5.69375)` excluding ALL
     pure JSJ-volume satellites (Seifert cables `C_{2,n}(4_1)`, Whitehead `5^2_1`, Mazur `L7n2`,
     twisted Whitehead, Borromean `6^3_2`, magic-parent `6^3_1`) from `Vol_req^{(k=3)} = 3.38231`,
     while requiring >= 9 Whitehead pieces at `k = 2` (`Vol_req^{(k=2)} = 34.1387`).
   - Family B (Mednykh-Vesnin Cyclic Branched Covers `M_n(4_1)` via Exact A-Polynomial Schlafli
     Integral): verifies `int_0^{2pi/3} acosh(2 + cos t - 2 cos^2 t) dt == 2 Cl_2(pi/3)` to 75+ dps,
     `Vol(M_4(4_1)) == Vol(4_1)`, `Vol(M_6(4_1)) == 8 G_Catalan`, and proves integer-straddle
     exclusion at both `k = 3` (`n=4: 2086.85` vs `n=5: 4817.54`) and `k = 2` (`n=17: 3314.71` vs
     `n=18: 3532.17`), plus Silver-Williams Mahler growth `ln((3+sqrt(5))/2) = 2 ln(phi)`.
   - Family C (Bring `4 x 4* = 1 + 15` Quantum-Dimension Dressings of `Vol(4_1)/hbar_q^2`):
     tests `[4]_q^2` (`3492.21`, `+0.431%`), `[3]_q[5]_q` (`3285.44`, `-5.52%`), `[2]_q^4`
     (`3380.98`, `-2.77%`), and `([4]_q^2 + h^2)` (`3501.25`, `+0.691%`).
   - Family D (Classical-Protected vs Finite-q_0 Koide Resolvent on `Vol(4_1)/hbar_q^2` & 1-Digit
     PDG Entropy Bound): evaluates `R_Koide_protected` (`3477.442306`) vs finite-q_0 TL_3-deformed
     Koide (`Q_TL3(q_0) = 0.659538 -> 3199.13`, `-8.00%`), audits the `10x` parenthetical
     uncertainty transcription slip in `gap2b` (`3477.228 +/- 0.2348` from `1776.86 +/- 0.12 MeV`
     mis-typed as `+/- 0.023`, turning `+0.911 sigma` into a spurious `+9.32 sigma`), scores
     against CODATA-2022 (`3477.23 +/- 0.23`, `+0.923 sigma`), PDG pre-Belle-II (`1776.86(12) MeV`,
     `+0.911 sigma`), and PDG-2024 post-Belle-II (`1776.93(9) MeV -> 3477.365 +/- 0.176`,
     `+22.15 ppm = +0.437 sigma`), and proves the Shannon precision/entropy bound showing `< 1 sigma`
     (`0` statistically significant digits) remains beyond protected `Q = 2/3`.

Formalized companion:
  `folio/quantum-observable-universe/lean/QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean`
Audit ledger:
  `docs/audits/2026-11-24-tau-satellite-41-bring-3gen-adjudication.md`

Run:
  python3 -u computations/probes/tau_satellite_41_bring_3gen_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp
import sympy as sp
from mpmath import mpf

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, q_muon_at  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.witness import WitnessBuilder, q0_comparison  # noqa: E402

set_compute_dps()
mp.mp.dps = 80


def fmt80(val: mpf) -> str:
    """Serialize an mpmath mpf to an 80-significant-digit decimal string (zero float64)."""
    return mp.nstr(val, 80)


def log_q(val: mpf, ln_q: mpf) -> mpf:
    """Base-q logarithm log_q(x) = ln(x) / ln(q) per scientific-accuracy skill."""
    return mp.log(val) / ln_q


def q_bal(k: int, q: mpf) -> mpf:
    """Balanced quantum integer [k]_q = (q^k - q^-k) / (q - q^-1)."""
    return (q ** k - q ** (-k)) / (q - mpf(1) / q)


def schlafli_integrand_4_1(t: mpf) -> mpf:
    """Exact A-polynomial longitudinal half-length ell(t)/2 = acosh(2 + cos t - 2 cos^2 t)."""
    arg = mpf(2) + mp.cos(t) - mpf(2) * (mp.cos(t) ** 2)
    if arg <= mpf(1):
        return mpf(0)
    return mp.acosh(arg)


def vol_branched_cover_4_1(n: int) -> mpf:
    """Exact 80-dps hyperbolic volume of the n-fold cyclic branched cover M_n(4_1) (Mednykh 1990)."""
    if n <= 3:
        return mpf(0)
    alpha_n = mpf(2) * mp.pi / mpf(n)
    upper = mpf(2) * mp.pi / mpf(3)
    integral_val = mp.re(mp.quad(schlafli_integrand_4_1, [alpha_n, upper]))
    return mpf(n) * integral_val


def solve_general_koide_tau_ratio(mu_over_e: mpf, q_koide: mpf) -> mpf:
    """Solve (1 + mu_over_e + x^2) / (1 + sqrt(mu_over_e) + x)^2 = q_koide for the heavy root x^2."""
    u = mpf(1)
    v = mp.sqrt(mu_over_e)
    # (1 - q_koide) x^2 - 2 q_koide (u + v) x + ((1 - q_koide)(u^2 + v^2) - 2 q_koide u v) = 0
    a_c = mpf(1) - q_koide
    b_c = -mpf(2) * q_koide * (u + v)
    c_c = (mpf(1) - q_koide) * (u ** 2 + v ** 2) - mpf(2) * q_koide * u * v
    disc = b_c ** 2 - mpf(4) * a_c * c_c
    x_plus = (-b_c + mp.sqrt(disc)) / (mpf(2) * a_c)
    return x_plus ** 2


def main() -> int:
    mp.mp.dps = 80

    # ------------------------------------------------------------------
    # Part 1: Symbolic Verification in SymPy (Matching Lean 4 Module)
    # ------------------------------------------------------------------
    c_sym, q_sym = sp.symbols("c q", nonzero=True)

    # Bring complete-intersection adjunction
    d_int = 1 * 2 * 3
    deg_k = d_int * ((1 + 2 + 3) - 5)
    chi_sigma4 = -deg_k
    g_sigma4 = 1 - chi_sigma4 // 2

    # A-polynomial longitudinal trace identities
    long_tr = 2 + c_sym - 2 * c_sym ** 2
    diff_factor = sp.expand((long_tr - 1) - (1 - c_sym) * (1 + 2 * c_sym))
    diff_comp_sq = sp.expand((sp.Rational(17, 8) - long_tr) - 2 * (c_sym - sp.Rational(1, 4)) ** 2)

    # su_q(4) / Bring 4 x 4* = 1 + 15 quantum-dimension identity: [4]_q^2 = 1 + [3]_q * [5]_q
    def sym_qbal(k: int):
        return (q_sym ** k - q_sym ** (-k)) / (q_sym - 1 / q_sym)

    diff_su4_qdim = sp.simplify(sym_qbal(4) ** 2 - (1 + sym_qbal(3) * sym_qbal(5)))

    # Monic Koide resolvent identity
    u_s, v_s, x_s = sp.symbols("u v x")
    diff_koide_res = sp.expand(
        (3 * (u_s ** 2 + v_s ** 2 + x_s ** 2) - 2 * (u_s + v_s + x_s) ** 2)
        - (x_s ** 2 - 4 * (u_s + v_s) * x_s + (u_s ** 2 + v_s ** 2 - 4 * u_s * v_s))
    )

    assert d_int == 6 and deg_k == 6 and chi_sigma4 == -6 and g_sigma4 == 4
    assert diff_factor == 0 and diff_comp_sq == 0
    assert diff_su4_qdim == 0 and diff_koide_res == 0

    # ------------------------------------------------------------------
    # Part 2: 80-dps Geometric Invariants of 4_1 Satellites & Covers
    # ------------------------------------------------------------------
    vol_4_1 = mpf(2) * mp.clsin(2, mp.pi / mpf(3))
    catalan_g = mp.clsin(2, mp.pi / mpf(2))
    vol_whitehead = mpf(4) * catalan_g
    vol_borromean = mpf(8) * catalan_g
    vol_magic_6_3_1 = mpf(5) * mp.clsin(2, mp.pi / mpf(3))  # 3-cusped magic parent of Mazur L7n2

    # Verify exact Schlafli A-polynomial integral at cusp alpha = 0 (must equal Vol(4_1))
    vol_4_1_schlafli = mp.re(mp.quad(schlafli_integrand_4_1, [mpf(0), mpf(2) * mp.pi / mpf(3)]))
    vol_m4 = vol_branched_cover_4_1(4)
    vol_m5 = vol_branched_cover_4_1(5)
    vol_m6 = vol_branched_cover_4_1(6)
    vol_m7 = vol_branched_cover_4_1(7)
    vol_m9 = vol_branched_cover_4_1(9)
    vol_m17 = vol_branched_cover_4_1(17)
    vol_m18 = vol_branched_cover_4_1(18)

    # Silver-Williams Mahler growth rate of |H_1(M_n(4_1); Z)_tors| = |L_n - 2| -> (3 + sqrt(5))/2 = phi^2
    phi_golden = (mpf(1) + mp.sqrt(mpf(5))) / mpf(2)
    mahler_exp_4_1 = phi_golden ** 2  # (3 + sqrt(5)) / 2 = 2.6180339887...

    # ------------------------------------------------------------------
    # Part 3: Experimental Benchmarks & Uncertainty Audit (Read-Only)
    # ------------------------------------------------------------------
    me_entry = codata("electron mass energy equivalent in MeV")
    mu_ratio_entry = codata("muon-electron mass ratio")
    tau_ratio_entry = codata("tau-electron mass ratio")

    m_e_mev = mpf(me_entry.value_str)
    LN_Q_PROTON = mp.log(mpf(Q_50_DIGIT_STR))

    # Benchmark 1: CODATA-2022 / NIST registry (3477.23 +/- 0.23, rel 66.14 ppm)
    r_tau_codata = mpf(tau_ratio_entry.value_str)
    r_tau_codata_sig = mpf(tau_ratio_entry.uncertainty_str)

    # Benchmark 2: PDG pre-Belle-II (1776.86 +/- 0.12 MeV -> 3477.228275 +/- 0.234834, rel 67.54 ppm)
    # Audits gap2b's 10x parenthetical slip where (23) in 3477.23(23) was read as +/- 0.023 on 3477.228!
    m_tau_pdg22_mev = mpf("1776.86")
    m_tau_pdg22_sig_mev = mpf("0.12")
    r_tau_pdg22 = m_tau_pdg22_mev / m_e_mev
    r_tau_pdg22_sig_true = m_tau_pdg22_sig_mev / m_e_mev
    r_tau_pdg22_sig_legacy_bug = mpf("0.023")

    # Benchmark 3: PDG-2024 post-Belle-II world average (Phys. Rev. D 110, 030001: 1776.93 +/- 0.09 MeV)
    m_tau_pdg24_mev = mpf("1776.93")
    m_tau_pdg24_sig_mev = mpf("0.09")
    r_tau_pdg24 = m_tau_pdg24_mev / m_e_mev
    r_tau_pdg24_sig = m_tau_pdg24_sig_mev / m_e_mev

    # Shannon / precision-digit entropy bound from experimental uncertainty (PR #1805 formula):
    # D_avail = -log10(2 * sigma_rel) = log_q(...) * log10(q)
    rel_sig_pdg22 = r_tau_pdg22_sig_true / r_tau_pdg22
    rel_sig_pdg24 = r_tau_pdg24_sig / r_tau_pdg24
    digits_avail_pdg22 = -(log_q(mpf(2) * rel_sig_pdg22, LN_Q_PROTON) * LN_Q_PROTON / mp.log(mpf(10)))
    digits_avail_pdg24 = -(log_q(mpf(2) * rel_sig_pdg24, LN_Q_PROTON) * LN_Q_PROTON / mp.log(mpf(10)))

    wb = WitnessBuilder("tau-satellite-41-bring-3gen-probe", engine="sympy")
    wb.set_description(
        "80-dps SymPy + mpmath adjudication of `qou-gen3` + `qou-htk4` (companion Lean 4 module "
        "`QOU/StandardModel/BringThreeGenerationsAndTauSatellite.lean`): "
        "(1) unifies Bring's genus-4 complete intersection (d=6, chi=-6, dim H^{1,0}=4) and Z_3 < S_5 "
        "branching 4 = (2 + 1) + 1 = 3 + 1 with the 3-body fission threshold T(2,9) -> 3 T(2,3) "
        "({3,5,7} indecomposable vs {9} composite); "
        "(2) proves & verifies the Soma-Agol JSJ forbidden gap (2.02988, 5.69375) excluding ALL "
        "pure JSJ-volume satellites P(4_1) at k=3, and Mednykh's A-polynomial Schlafli integral "
        "excluding all cyclic branched covers M_n(4_1) by integer straddle; "
        "(3) scores zero-parameter Bring [4]_q^2 / [3]_q[5]_q quantum-dimension dressings and "
        "Koide resolvent candidates against CODATA-2022 3477.23(23), PDG 1776.86(12) MeV, and "
        "PDG-2024 1776.93(9) MeV, correcting gap2b's 10x uncertainty slip (+/-0.023 -> +/-0.2348, "
        "pull +9.32 sigma -> +0.911 sigma / +0.437 sigma PDG-2024) and establishing the 3.87-digit "
        "experimental entropy bound."
    )

    # Assertions on exact geometric & symbolic theorems
    wb.add_assertion(
        name="bring_adjunction_and_su4_qdim_symbolic_zero",
        computed=str(int(diff_factor) + abs(int(diff_comp_sq)) + abs(int(diff_su4_qdim)) + abs(int(diff_koide_res))),
        expected="0",
        tolerance="0",
        source="Bring adjunction, A-poly factorization, [4]_q^2 = 1 + [3]_q[5]_q, and Koide resolvent",
    )
    wb.add_assertion(
        name="schlafli_apoly_integral_matches_vol_4_1_75dps",
        computed=fmt80(vol_4_1_schlafli),
        expected=fmt80(vol_4_1),
        tolerance="1e-75",
        source="int_0^{2pi/3} acosh(2 + cos t - 2 cos^2 t) dt == 2 Cl_2(pi/3)",
    )
    wb.add_assertion(
        name="mednykh_m4_equals_vol_4_1_75dps",
        computed=fmt80(vol_m4),
        expected=fmt80(vol_4_1),
        tolerance="1e-75",
        source="Vol(M_4(4_1)) == Vol(4_1) (Mednykh-Vesnin 4-fold cover identity)",
    )
    wb.add_assertion(
        name="mednykh_m6_equals_borromean_8G_75dps",
        computed=fmt80(vol_m6),
        expected=fmt80(vol_borromean),
        tolerance="1e-75",
        source="Vol(M_6(4_1)) == 8 * G_Catalan == Vol(6^3_2)",
    )

    wb.add_data("hyperbolic_manifold_invariants_80dps", {
        "Vol_4_1_Clausen": fmt80(vol_4_1),
        "Vol_4_1_Schlafli_Apoly": fmt80(vol_4_1_schlafli),
        "Catalan_G": fmt80(catalan_g),
        "Vol_Whitehead_5_2_1_eq_4G": fmt80(vol_whitehead),
        "Vol_Borromean_6_3_2_eq_8G": fmt80(vol_borromean),
        "Vol_Magic_6_3_1_eq_5_Cl2_pi_3": fmt80(vol_magic_6_3_1),
        "Agol_min_hyperbolic_satellite_Vol_4_1_plus_4G": fmt80(vol_4_1 + vol_whitehead),
        "Mazur_satellite_upper_bound_Vol_4_1_plus_Vol_6_3_1": fmt80(vol_4_1 + vol_magic_6_3_1),
        "Vol_M3_4_1_Euclidean": "0",
        "Vol_M4_4_1": fmt80(vol_m4),
        "Vol_M5_4_1_Fibonacci": fmt80(vol_m5),
        "Vol_M6_4_1_Borromean": fmt80(vol_m6),
        "Vol_M7_4_1": fmt80(vol_m7),
        "Vol_M9_4_1": fmt80(vol_m9),
        "Vol_M17_4_1": fmt80(vol_m17),
        "Vol_M18_4_1": fmt80(vol_m18),
        "Silver_Williams_Mahler_base_phi_sq": fmt80(mahler_exp_4_1),
    })

    wb.add_data("experimental_benchmarks_and_entropy_audit", {
        "codata_2022_tau_over_e": tau_ratio_entry.value_str,
        "codata_2022_tau_over_e_sigma": tau_ratio_entry.uncertainty_str,
        "codata_2022_rel_sigma_ppm": fmt80(r_tau_codata_sig / r_tau_codata * mpf("1e6")),
        "pdg_pre_belle2_1776_86_MeV_tau_over_e": fmt80(r_tau_pdg22),
        "pdg_pre_belle2_true_sigma_from_0_12_MeV": fmt80(r_tau_pdg22_sig_true),
        "pdg_pre_belle2_rel_sigma_ppm": fmt80(rel_sig_pdg22 * mpf("1e6")),
        "gap2b_legacy_mistyped_sigma": fmt80(r_tau_pdg22_sig_legacy_bug),
        "pdg_2024_post_belle2_1776_93_MeV_tau_over_e": fmt80(r_tau_pdg24),
        "pdg_2024_post_belle2_sigma_from_0_09_MeV": fmt80(r_tau_pdg24_sig),
        "pdg_2024_rel_sigma_ppm": fmt80(rel_sig_pdg24 * mpf("1e6")),
        "shannon_available_decimal_digits_pdg22": fmt80(digits_avail_pdg22),
        "shannon_available_decimal_digits_pdg24": fmt80(digits_avail_pdg24),
    })

    q_proton = mpf(Q_50_DIGIT_STR)
    q_muon = q_muon_at(80)
    pins_data: dict[str, object] = {}

    print("=" * 94)
    print("80-DPS BRING N_gen = 3 FISSION & SATELLITE T(2,n)-4_1 TAU MASS ADJUDICATION (`qou-gen3`/`htk4`)")
    print("=" * 94)
    print(f"  Schlafli A-poly integral vs 2 Cl_2(pi/3) diff : {mp.nstr(abs(vol_4_1_schlafli - vol_4_1), 6)}")
    print(f"  Mednykh Vol(M_4(4_1)) - Vol(4_1) diff         : {mp.nstr(abs(vol_m4 - vol_4_1), 6)}")
    print(f"  Mednykh Vol(M_6(4_1)) - 8*G_Catalan diff      : {mp.nstr(abs(vol_m6 - vol_borromean), 6)}")
    print(
        f"  Benchmarks: CODATA-2022 = {tau_ratio_entry.value_str} +/- {tau_ratio_entry.uncertainty_str} | "
        f"PDG(1776.86+-0.12) = {mp.nstr(r_tau_pdg22, 8)} +/- {mp.nstr(r_tau_pdg22_sig_true, 4)} | "
        f"PDG-2024(1776.93+-0.09) = {mp.nstr(r_tau_pdg24, 8)} +/- {mp.nstr(r_tau_pdg24_sig, 4)}"
    )
    print(
        f"  Entropy precision ceiling: {mp.nstr(digits_avail_pdg22, 4)} digits (67.54 ppm) / "
        f"{mp.nstr(digits_avail_pdg24, 4)} digits (50.65 ppm)"
    )
    print()

    for pin_name, q_val in [("proton", q_proton), ("muon", q_muon)]:
        hbar_q = mpf(1) - mpf(1) / q_val
        h_skein = q_val - mpf(1) / q_val
        mu_qou = vol_4_1 / (hbar_q ** 2)

        vol_req_k3 = r_tau_codata * (hbar_q ** 3)
        vol_req_k2 = r_tau_codata * (hbar_q ** 2)

        # Verify Soma-Agol forbidden gap at k = 3
        in_forbidden_gap_k3 = vol_4_1 < vol_req_k3 < (vol_4_1 + vol_whitehead)
        # Verify Mednykh integer straddles
        m_straddle_k3 = vol_m4 < vol_req_k3 < vol_m5
        m_straddle_k2 = vol_m17 < vol_req_k2 < vol_m18

        wb.add_assertion(
            name=f"soma_agol_and_mednykh_exclusions_hold_{pin_name}",
            computed="1" if (in_forbidden_gap_k3 and m_straddle_k3 and m_straddle_k2) else "0",
            expected="1",
            tolerance="0",
            source=f"Vol_req^(k=3) in (Vol(4_1), Vol(4_1)+4G) and M_4<req<M_5, M_17<req<M_18 at {pin_name}",
        )

        # Quantum integers & TL_3 Koide ratio
        qb2 = q_bal(2, q_val)
        qb3 = q_bal(3, q_val)
        qb4 = q_bal(4, q_val)
        qb5 = q_bal(5, q_val)
        q_tl3 = mpf(2) / mpf(3) - (h_skein ** 2) / (mpf(3) * (q_val ** 2 + q_val ** (-2)))

        candidates = [
            ("A1_cable_C27_4_1_jsj_k2", "Vol(4_1) / hbar_q^2 [Seifert cable k=2]", vol_4_1 / (hbar_q ** 2)),
            ("A2_cable_C27_4_1_jsj_k3", "Vol(4_1) / hbar_q^3 [Seifert cable k=3]", vol_4_1 / (hbar_q ** 3)),
            ("A3_whitehead_sat_min_hyp_k2", "(Vol(4_1) + 4G) / hbar_q^2 [Agol min hyp sat k=2]", (vol_4_1 + vol_whitehead) / (hbar_q ** 2)),
            ("A4_whitehead_sat_min_hyp_k3", "(Vol(4_1) + 4G) / hbar_q^3 [Agol min hyp sat k=3]", (vol_4_1 + vol_whitehead) / (hbar_q ** 3)),
            ("A5_mazur_magic_cusp_bound_k3", "(Vol(4_1) + 5 Cl_2(pi/3)) / hbar_q^3 [Mazur parent k=3]", (vol_4_1 + vol_magic_6_3_1) / (hbar_q ** 3)),
            ("A6_borromean_sat_k2", "(Vol(4_1) + 8G) / hbar_q^2 [Borromean sat k=2]", (vol_4_1 + vol_borromean) / (hbar_q ** 2)),
            ("B1_branched_M5_4_1_k3", "Vol(M_5(4_1)) / hbar_q^3 [Fibonacci 5-cover k=3]", vol_m5 / (hbar_q ** 3)),
            ("B2_branched_M7_4_1_k3", "Vol(M_7(4_1)) / hbar_q^3 [7-cover k=3]", vol_m7 / (hbar_q ** 3)),
            ("B3_branched_M17_4_1_k2", "Vol(M_17(4_1)) / hbar_q^2 [linking-17 cover k=2]", vol_m17 / (hbar_q ** 2)),
            ("B4_branched_M18_4_1_k2", "Vol(M_18(4_1)) / hbar_q^2 [18-cover straddle k=2]", vol_m18 / (hbar_q ** 2)),
            ("C1_bring_qdim_4_sq", "[4]_q^2 * Vol(4_1) / hbar_q^2 [Bring dim_q(4)^2]", (qb4 ** 2) * mu_qou),
            ("C2_bring_adjoint_3_mul_5", "[3]_q * [5]_q * Vol(4_1) / hbar_q^2 [su_q(4) adjoint 15]", (qb3 * qb5) * mu_qou),
            ("C3_spin_tower_2_pow_4", "[2]_q^4 * Vol(4_1) / hbar_q^2 [4-fold doublet]", (qb2 ** 4) * mu_qou),
            ("D1_koide_tl3_deformed_q0", "Koide resolvent at Q_TL3(q_0) on Vol(4_1)/hbar_q^2", solve_general_koide_tau_ratio(mu_qou, q_tl3)),
            ("D2_koide_protected_q1_on_vol41", "Protected Q=2/3 Koide resolvent on Vol(4_1)/hbar_q^2 (§3b-cond)", solve_general_koide_tau_ratio(mu_qou, mpf(2) / mpf(3))),
        ]

        scored_rows: dict[str, object] = {}
        print(f"--- PIN: {pin_name.upper()} (q0 = {mp.nstr(q_val, 22)}) ---")
        print(
            f"  Vol_req^(k=3) = {mp.nstr(vol_req_k3, 8)} in forbidden (2.0299, 5.6937): {in_forbidden_gap_k3} | "
            f"Vol_req^(k=2) = {mp.nstr(vol_req_k2, 8)}"
        )
        for key, formula_str, pred_val in candidates:
            rel_codata_ppm = (pred_val - r_tau_codata) / r_tau_codata * mpf("1e6")
            pull_codata = (pred_val - r_tau_codata) / r_tau_codata_sig
            rel_pdg22_ppm = (pred_val - r_tau_pdg22) / r_tau_pdg22 * mpf("1e6")
            pull_pdg22_true = (pred_val - r_tau_pdg22) / r_tau_pdg22_sig_true
            pull_pdg22_legacy = (pred_val - r_tau_pdg22) / r_tau_pdg22_sig_legacy_bug
            rel_pdg24_ppm = (pred_val - r_tau_pdg24) / r_tau_pdg24 * mpf("1e6")
            pull_pdg24 = (pred_val - r_tau_pdg24) / r_tau_pdg24_sig

            scored_rows[key] = {
                "formula": formula_str,
                "predicted_m_tau_over_m_e": fmt80(pred_val),
                "predicted_m_tau_MeV": fmt80(pred_val * m_e_mev),
                "rel_err_vs_codata2022_ppm": fmt80(rel_codata_ppm),
                "pull_vs_codata2022_sigma": fmt80(pull_codata),
                "rel_err_vs_pdg_1776_86_ppm": fmt80(rel_pdg22_ppm),
                "pull_vs_pdg_1776_86_true_sigma": fmt80(pull_pdg22_true),
                "pull_vs_gap2b_mistyped_0_023_sigma": fmt80(pull_pdg22_legacy),
                "rel_err_vs_pdg2024_1776_93_ppm": fmt80(rel_pdg24_ppm),
                "pull_vs_pdg2024_1776_93_sigma": fmt80(pull_pdg24),
                "within_1sigma_pdg2024": abs(pull_pdg24) <= mpf(1),
                "within_1sigma_codata2022": abs(pull_codata) <= mpf(1),
            }
            print(
                f"  {key:34s}: {mp.nstr(pred_val, 10):>12s} | "
                f"vs C22: {mp.nstr(rel_codata_ppm, 6):>10s} ppm ({mp.nstr(pull_codata, 4):>7s}s) | "
                f"vs PDG24: {mp.nstr(rel_pdg24_ppm, 6):>10s} ppm ({mp.nstr(pull_pdg24, 4):>7s}s)"
            )
        print()

        d2_pull_ok = (
            abs(mpf(scored_rows["D2_koide_protected_q1_on_vol41"]["pull_vs_codata2022_sigma"])) < mpf(1)
            and abs(mpf(scored_rows["D2_koide_protected_q1_on_vol41"]["pull_vs_pdg_1776_86_true_sigma"])) < mpf(1)
            and abs(mpf(scored_rows["D2_koide_protected_q1_on_vol41"]["pull_vs_pdg2024_1776_93_sigma"])) < mpf(1)
        )
        wb.add_assertion(
            name=f"koide_protected_vol41_within_1sigma_all_true_benchmarks_{pin_name}",
            computed="1" if d2_pull_ok else "0",
            expected="1",
            tolerance="0",
            source=f"Protected Q=2/3 + Vol(4_1)/hbar_q^2 is < 1 sigma vs CODATA-2022, PDG-2022, and PDG-2024 at {pin_name}",
        )

        pins_data[pin_name] = {
            "q0": fmt80(q_val),
            "hbar_q": fmt80(hbar_q),
            "mu_over_e_qou_vol41": fmt80(mu_qou),
            "vol_req_k3": fmt80(vol_req_k3),
            "vol_req_k2": fmt80(vol_req_k2),
            "soma_agol_k3_excluded": in_forbidden_gap_k3,
            "mednykh_k3_straddle_excluded": m_straddle_k3,
            "mednykh_k2_straddle_excluded": m_straddle_k2,
            "candidates": scored_rows,
        }

    wb.add_data("pins", pins_data)
    wb.add_caveat(
        "Metrological & structural adjudication (`qou-gen3` + `qou-htk4`): "
        "(1) Pure JSJ simplicial volumes of ALL satellites P(4_1) are excluded at k=3 by the "
        "Soma-Agol forbidden gap (2.02988, 5.69375) and all cyclic branched covers M_n(4_1) "
        "straddle the target without integer hit; "
        "(2) Bring's [4]_q^2 * Vol(4_1)/hbar_q^2 reaches +0.431% (3492.21) parameter-free, "
        "confirming the 16x scale of dim_q(H^{1,0}(Sigma_4))^2 = 1 + [3]_q[5]_q, but misses "
        "metrological 1-sigma by +65 sigma; "
        "(3) Protected Q=2/3 Koide resolvent welded to QOU's zero-CAL-2 muon Vol(4_1)/hbar_q^2 "
        "gives 3477.442306 (+0.923 sigma vs CODATA-2022 3477.23(23), +0.911 sigma vs PDG "
        "1776.86(12) MeV after correcting gap2b's 10x parenthetical slip +/-0.023 -> +/-0.2348, "
        "and +0.437 sigma / +22.15 ppm vs PDG-2024 1776.93(9) MeV), saturating the 3.87-digit "
        "experimental entropy ceiling; deriving topological protection of Q=2/3 from q_0 drift "
        "remains gated in `KoideTopologicalProtectionHypothesis` (Rule 13a)."
    )

    out_path = wb.save(
        q0_comparison(
            muon=mp.nstr(q_muon, 50),
            proton=Q_50_DIGIT_STR,
            reason=(
                "adjudicates zero-parameter satellite P(4_1), cyclic branched cover M_n(4_1), "
                "Bring [4]_q^2 quantum-dimension, and Koide resolvent m_tau/m_e candidates at "
                "both registered pins (proton default q_p and muon CAL-2 comparison q_mu)"
            ),
        )
    )
    print(f"Witness written to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
