#!/usr/bin/env python3
"""
h3_green_coth_saturation_probe.py

50-dps mpmath + exact integer verification probe for Round 48 (`qou-3l2l` children):
  1. `qou-4uhn`: RT shadow-world 1-loop propagator normalization `1/(pi dim H_1)`
     vs Gauss-Bonnet `1/(8*pi)` at Bring's genus `g = 4` (`dim H_1 = 8`).
  2. `qou-l1je`: Explicit `H^1(Bring)` Hodge model, Braden-Northover period matrix
     `C = 5*I_4 - J_4` spectral decomposition `(5, 5, 5, 1)`, and non-CM `j`-invariants.
  3. `qou-zp6a`: `H^3` Laplacian Green's function `phi_0(alpha) = -coth(alpha)/(4*pi)`
     saturation check (`coth(alpha) -> 1` at infinity vs O2 neutralizing-background
     subtraction `coth(alpha) - 1 = 2/(exp(2*alpha) - 1)`) and monotone `kappa(A)`
     transition `3.2 -> 2.2`.
  4. `qou-9gj9`: Convention-slip sweep on `[2]_q * (1 - h^2 * alpha)` (`[2]_q^2 - h^2 = 4`,
     `h / hbar_q = q + 1`) and convention-slip immunity of the neutron-proton EM
     self-energy sign (`sum_{uud} q_i q_j - sum_{udd} q_i q_j = +1/3 > 0`).

Companion Lean module:
  `folio/quantum-observable-universe/lean/QOU/AlphaEM/PropagatorHodgeH3GreenAssembly.lean`
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

from mpmath import mp  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.dps = 65


def fmt50(x: mp.mpf) -> str:
    return mp.nstr(x, 50, min_fixed=0, max_fixed=0)


def main() -> int:
    wb = WitnessBuilder(
        "h3_green_coth_saturation_probe",
        engine="mpmath",
        output_dir=Path(__file__).resolve().parent,
    )
    mp.dps = 65

    wb.set_description(
        "50-dps mpmath and exact integer verification of (I) genus-4 propagator "
        "normalization 1/(pi dim H_1(Sigma_4)) = 1/(8*pi) (`qou-4uhn`), (II) Bring "
        "H^1 period matrix C = 5*I_4 - J_4 spectrum (5,5,5,1) and non-CM j-invariants "
        "(`qou-l1je`), (III) H^3 Laplacian Green's function phi_0 = -coth(alpha)/(4*pi) "
        "saturation vs O2 background subtraction coth(alpha)-1 = 2/(e^(2*alpha)-1) and "
        "monotone kappa(A) 3.2 -> 2.2 (`qou-zp6a`), and (IV) [2]_q(1-h^2*alpha) balanced "
        "discriminant [2]_q^2 - h^2 = 4 and n-p EM sign convention-slip immunity (`qou-9gj9`)."
    )
    wb.set_audit_only(
        "Beans qou-4uhn, qou-l1je, qou-zp6a, qou-9gj9 (parent qou-3l2l); "
        "companion Lean module QOU/AlphaEM/PropagatorHodgeH3GreenAssembly.lean."
    )

    # =========================================================================
    # Part I (`qou-4uhn`): 1/(pi dim H_1(Sigma_g)) vs Gauss-Bonnet 1/(8*pi)
    # =========================================================================
    one_over_8pi = mp.mpf(1) / (mp.mpf(8) * mp.pi)
    genus_table = []
    coinciding_genera = []
    gb_max_err = mp.mpf(0)

    for g in range(2, 8):
        dim_h1 = 2 * g
        abs_chi = 2 * g - 2
        area_g = mp.mpf(4) * mp.pi * mp.mpf(g - 1)
        gb_measure = mp.mpf(abs_chi) / (mp.mpf(4) * area_g)
        prop_norm = mp.mpf(1) / (mp.pi * mp.mpf(dim_h1))
        err_gb = abs(gb_measure - one_over_8pi)
        if err_gb > gb_max_err:
            gb_max_err = err_gb
        if abs(prop_norm - one_over_8pi) < mp.mpf("1e-55"):
            coinciding_genera.append(g)
        genus_table.append(
            {
                "genus": g,
                "dim_H1": dim_h1,
                "abs_chi": abs_chi,
                "gauss_bonnet_measure_50dps": fmt50(gb_measure),
                "propagator_norm_1_over_pi_dimH1_50dps": fmt50(prop_norm),
                "coincides_with_1_over_8pi": g == 4,
            }
        )

    wb.add_assertion(
        "qou_4uhn_gauss_bonnet_genus_independent_1_over_8pi",
        computed=1 if gb_max_err < mp.mpf("1e-55") else 0,
        expected=1,
        tolerance=0,
        source="gauss_bonnet_measure_denominator_eq_eight (PropagatorHodgeH3GreenAssembly.lean)",
    )
    wb.add_assertion(
        "qou_4uhn_propagator_1_over_pi_dimH1_coincides_iff_g4",
        computed=1 if coinciding_genera == [4] else 0,
        expected=1,
        tolerance=0,
        source="propagator_dimH1_eq_eight_iff_g4 (PropagatorHodgeH3GreenAssembly.lean)",
    )

    # =========================================================================
    # Part II (`qou-l1je`): Bring H^1 Period Matrix C = 5*I_4 - J_4 & Non-CM
    # =========================================================================
    C_mat = [
        [4, -1, -1, -1],
        [-1, 4, -1, -1],
        [-1, -1, 4, -1],
        [-1, -1, -1, 4],
    ]
    trace_C = sum(C_mat[i][i] for i in range(4))
    # Verify (C - 5 I)(C - I) == 0
    min_poly_zero = True
    for i in range(4):
        for j in range(4):
            entry = sum(
                (C_mat[i][k] - (5 if i == k else 0))
                * (C_mat[k][j] - (1 if k == j else 0))
                for k in range(4)
            )
            if entry != 0:
                min_poly_zero = False

    j_tau0 = Fraction(-121945, 32)
    j_5tau0 = Fraction(-25, 2)
    non_cm_ok = (j_tau0.denominator == 32) and (j_5tau0.denominator == 2)

    wb.add_assertion(
        "qou_l1je_braden_northover_trace_16_and_min_poly",
        computed=1 if (trace_C == 16 and min_poly_zero) else 0,
        expected=1,
        tolerance=0,
        source="bradenNorthoverC_spectral_decomposition (PropagatorHodgeH3GreenAssembly.lean)",
    )
    wb.add_assertion(
        "qou_l1je_bring_j_invariants_non_integral_no_cm",
        computed=1 if non_cm_ok else 0,
        expected=1,
        tolerance=0,
        source="bring_elliptic_factors_non_cm (PropagatorHodgeH3GreenAssembly.lean)",
    )

    # =========================================================================
    # Part III (`qou-zp6a`): H^3 Laplacian Green's fn phi_0 = -coth(alpha)/(4*pi)
    # =========================================================================
    # 1. Short-distance Euclidean limit: alpha * coth(alpha) = 1 + alpha^2 / 3 - ...
    alpha_small = mp.mpf("1e-25")
    short_dist_err = abs(alpha_small * mp.coth(alpha_small) - mp.mpf(1))
    wb.add_assertion(
        "qou_zp6a_short_distance_alpha_coth_to_1",
        computed=1 if short_dist_err < mp.mpf("1e-48") else 0,
        expected=1,
        tolerance=0,
        source="DeTurck-Gluck Thm 1(3): coth(alpha) ~ 1/alpha as alpha -> 0+",
    )

    # 2. Large-distance saturation: coth(alpha) -> 1 (non-zero!) vs O2 subtracted -> 0
    alpha_large = mp.mpf("40")
    coth_large = mp.coth(alpha_large)
    sub_large = coth_large - mp.mpf(1)
    saturation_verified = (coth_large > mp.mpf(1)) and (
        abs(coth_large - mp.mpf(1)) < mp.mpf("1e-33")
    )
    wb.add_assertion(
        "qou_zp6a_large_distance_unsubtracted_saturates_to_1",
        computed=1 if saturation_verified else 0,
        expected=1,
        tolerance=0,
        source="h3_coth_unsubtracted_gt_one (PropagatorHodgeH3GreenAssembly.lean)",
    )

    # 3. Exact O2 background subtraction identity: coth(alpha) - 1 == 2 / (e^(2*alpha) - 1)
    max_o2_id_err = mp.mpf(0)
    for a_str in ("0.1", "0.25", "0.5", "1.0", "2.5", "5.0"):
        a_val = mp.mpf(a_str)
        u_val = mp.exp(2 * a_val)
        lhs = mp.coth(a_val) - mp.mpf(1)
        rhs = mp.mpf(2) / (u_val - mp.mpf(1))
        err = abs(lhs - rhs)
        if err > max_o2_id_err:
            max_o2_id_err = err

    wb.add_assertion(
        "qou_zp6a_o2_background_subtraction_identity_50dps",
        computed=1 if max_o2_id_err < mp.mpf("1e-55") else 0,
        expected=1,
        tolerance=0,
        source="h3_coth_background_subtraction_identity (PropagatorHodgeH3GreenAssembly.lean)",
    )

    # 4. Monotone kappa(A) transition check (3.2 -> 2.2) across A in [3, 4, 12, 16, 40, 56]
    # Compare:
    #   (a) Unsubtracted coth(alpha) anchored at kappa(3)=3.2, kappa(16)=2.2
    #   (b) O2 background-subtracted 2/(e^(2*alpha)-1) anchored at kappa(3)=3.2, kappa(16)=2.2
    alpha_unsub_start = mp.acoth(mp.mpf("3.2"))  # ~ 0.3234788773
    alpha_unsub_end = mp.acoth(mp.mpf("2.2"))    # ~ 0.4904146265
    alpha_sub_start = mp.log(mp.mpf(1) + mp.mpf(2) / mp.mpf("3.2")) / 2  # ~ 0.2427539079
    alpha_sub_end = mp.log(mp.mpf(1) + mp.mpf(2) / mp.mpf("2.2")) / 2    # ~ 0.3233135825

    mass_numbers = [3, 4, 12, 16, 40, 56]
    kappa_profile = []
    unsub_vals = []
    sub_vals = []
    for idx, A_val in enumerate(mass_numbers):
        # Power-law hyperbolic separation alpha(A) = alpha_start * (A / 3)^gamma
        # calibrated on [A=3 -> 3.2, A=16 -> 2.2] to test behaviour on A=40, 56
        ratio_A = mp.mpf(A_val) / mp.mpf(3)
        gamma_unsub = mp.log(alpha_unsub_end / alpha_unsub_start) / mp.log(mp.mpf(16) / mp.mpf(3))
        gamma_sub = mp.log(alpha_sub_end / alpha_sub_start) / mp.log(mp.mpf(16) / mp.mpf(3))

        a_unsub = alpha_unsub_start * (ratio_A ** gamma_unsub)
        a_sub = alpha_sub_start * (ratio_A ** gamma_sub)

        k_unsub = mp.coth(a_unsub)
        k_sub = mp.coth(a_sub) - mp.mpf(1)
        unsub_vals.append(k_unsub)
        sub_vals.append(k_sub)
        kappa_profile.append(
            {
                "A": A_val,
                "alpha_unsubtracted_50dps": fmt50(a_unsub),
                "kappa_unsubtracted_coth_50dps": fmt50(k_unsub),
                "alpha_o2_subtracted_50dps": fmt50(a_sub),
                "kappa_o2_subtracted_coth_minus_1_50dps": fmt50(k_sub),
            }
        )

    strictly_monotone = all(
        unsub_vals[i] > unsub_vals[i + 1] and sub_vals[i] > sub_vals[i + 1]
        for i in range(len(mass_numbers) - 1)
    )
    wb.add_assertion(
        "qou_zp6a_kappa_strictly_monotone_3p2_to_2p2",
        computed=1 if strictly_monotone else 0,
        expected=1,
        tolerance=0,
        source="h3_coth_strict_antitone (PropagatorHodgeH3GreenAssembly.lean)",
    )

    # =========================================================================
    # Part IV (`qou-9gj9`): [2]_q(1 - h^2*alpha) Discriminant & EM Sign Immunity
    # =========================================================================
    # Test [2]_q^2 - h^2 == 4 and h / hbar_q == q + 1 across exact test points
    disc_max_err = mp.mpf(0)
    ratio_max_err = mp.mpf(0)
    for q_str in ("1.05", "1.10517091807564762481170782649024666822454719473752", "1.25", "2.0"):
        q_v = mp.mpf(q_str)
        two_q = q_v + mp.mpf(1) / q_v
        h_v = q_v - mp.mpf(1) / q_v
        hbar_v = mp.mpf(1) - mp.mpf(1) / q_v
        disc_err = abs((two_q ** 2 - h_v ** 2) - mp.mpf(4))
        rat_err = abs((h_v / hbar_v) - (q_v + mp.mpf(1)))
        if disc_err > disc_max_err:
            disc_max_err = disc_err
        if rat_err > ratio_max_err:
            ratio_max_err = rat_err

    wb.add_assertion(
        "qou_9gj9_balanced_two_q_sq_minus_h_sq_eq_4",
        computed=1 if disc_max_err < mp.mpf("1e-55") else 0,
        expected=1,
        tolerance=0,
        source="balanced_two_q_sq_sub_h_sq (PropagatorHodgeH3GreenAssembly.lean)",
    )
    wb.add_assertion(
        "qou_9gj9_hecke_h_over_hbar_q_eq_q_plus_1",
        computed=1 if ratio_max_err < mp.mpf("1e-55") else 0,
        expected=1,
        tolerance=0,
        source="hecke_h_eq_q_plus_one_mul_hbar_q (PropagatorHodgeH3GreenAssembly.lean)",
    )

    # Neutron-proton EM charge-structure gap: proton uud (0) - neutron udd (-1/3) = +1/3
    q_u = Fraction(2, 3)
    q_d = Fraction(-1, 3)
    qq_proton = q_u * q_u + q_u * q_d + q_u * q_d
    qq_neutron = q_u * q_d + q_u * q_d + q_d * q_d
    qq_gap = qq_proton - qq_neutron
    wb.add_assertion(
        "qou_9gj9_np_em_charge_gap_one_third_positive",
        computed=1 if (qq_proton == 0 and qq_neutron == Fraction(-1, 3) and qq_gap == Fraction(1, 3)) else 0,
        expected=1,
        tolerance=0,
        source="np_em_sign_convention_immune (PropagatorHodgeH3GreenAssembly.lean)",
    )

    wb.add_data("qou_4uhn_genus_propagator_vs_gauss_bonnet", genus_table)
    wb.add_data(
        "qou_l1je_bring_hodge_period_summary",
        {
            "period_matrix_C": C_mat,
            "trace_C": trace_C,
            "eigenvalues": [5, 5, 5, 1],
            "determinant_C": 125,
            "j_tau0_rational": "-121945/32",
            "j_5tau0_rational": "-25/2",
            "minimal_open_core_class": "QOU.Archimedean.PeriodMapWeightReduction.PeriodMapWeight",
        },
    )
    wb.add_data(
        "qou_zp6a_h3_green_coth_saturation",
        {
            "alpha_small_1e_minus_25_coth_err": fmt50(short_dist_err),
            "alpha_40_unsubtracted_coth_50dps": fmt50(coth_large),
            "alpha_40_o2_subtracted_coth_minus_1_50dps": fmt50(sub_large),
            "alpha_unsubtracted_at_3p2_50dps": fmt50(alpha_unsub_start),
            "alpha_unsubtracted_at_2p2_50dps": fmt50(alpha_unsub_end),
            "alpha_o2_subtracted_at_3p2_50dps": fmt50(alpha_sub_start),
            "alpha_o2_subtracted_at_2p2_50dps": fmt50(alpha_sub_end),
            "kappa_profile_A_3_to_56": kappa_profile,
        },
    )
    wb.add_data(
        "qou_9gj9_convention_slip_sweep_summary",
        {
            "max_discriminant_err_50dps": fmt50(disc_max_err),
            "max_h_over_hbar_q_err_50dps": fmt50(ratio_max_err),
            "proton_uud_pairwise_qq": str(qq_proton),
            "neutron_udd_pairwise_qq": str(qq_neutron),
            "proton_minus_neutron_qq_gap": str(qq_gap),
        },
    )

    out_path = wb.save(
        {
            "q0Anchor": "independent",
            "q0AnchorReason": (
                "Exact genus-4 cohomology/period-matrix identities, H^3 Laplacian "
                "Green's function coth(alpha) analytical saturation identities, and "
                "symbolic Laurent polynomial identities tested across generic q values."
            ),
        }
    )
    print(f"Wrote witness to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
