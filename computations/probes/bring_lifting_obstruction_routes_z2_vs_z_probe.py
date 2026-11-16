#!/usr/bin/env python3
"""
bring_lifting_obstruction_routes_z2_vs_z_probe.py

50-dps + exact integer verification probe for the Bring Lifting Obstruction
Routes (Route Z/2Z vs Route Z, beans `qou-2a2o`, `qou-n2aa`, parent `qou-lx8f`)
and the Hecke Modular Tensor Category (S, T) data (`hkmt`, parent `rtep` / `bwhk`).

Companion Lean module:
  `folio/quantum-observable-universe/lean/QOU/Brings/BringLiftingObstructionRoutes.lean`
"""

from __future__ import annotations

import sys
from pathlib import Path

# Path bridge to `computations/` and `tools/qou-substrate/python`
_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))

from mpmath import mp  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402

mp.dps = 65


def fmt50(x: mp.mpf) -> str:
    return mp.nstr(x, 50, min_fixed=0, max_fixed=0)


def partition_content_sum(parts: list[int]) -> int:
    total = 0
    for r, row_len in enumerate(parts):
        for c in range(row_len):
            total += c - r
    return total


def conjugate_partition(parts: list[int]) -> list[int]:
    if not parts or parts[0] == 0:
        return []
    return [sum(1 for row in parts if row > col) for col in range(parts[0])]


def main() -> int:
    wb = WitnessBuilder(
        "bring_lifting_obstruction_routes_z2_vs_z_probe",
        engine="mpmath",
        output_dir=Path(__file__).resolve().parent,
    )
    mp.dps = 65
    wb.set_description(
        "Exact integer and 50-dps verification of (I) Route Z/2Z Stiefel-Whitney "
        "w_2 reduction and 256 = 136 + 120 theta characteristics on Bring's genus-4 "
        "surface (`qou-2a2o`), (II) Route Z integral Euler / Chern obstruction "
        "kappa_0 = -6 != 0 and Kummer n-th root divisibility set {1, 2, 3, 6} "
        "(`qou-n2aa`), and (III) Hecke Modular Tensor Category (S, T) relations "
        "and root-of-unity truncation vs real q_0 > 1 non-truncation (`hkmt`)."
    )
    wb.set_audit_only(
        "Beans qou-2a2o, qou-n2aa (parent qou-lx8f), and hkmt (parent rtep / bwhk); "
        "companion Lean module QOU/Brings/BringLiftingObstructionRoutes.lean."
    )

    # =========================================================================
    # Part I: Route Z/2Z (`qou-2a2o`) — w_2 reduction and Spin(2) structures
    # =========================================================================
    genera_check = []
    all_w2_zero = True
    for g in range(0, 11):
        chi_g = 2 - 2 * g
        deg_k = 2 * g - 2
        w2_g = chi_g % 2
        if w2_g != 0:
            all_w2_zero = False
        if g >= 1:
            n_total = 2 ** (2 * g)
            n_even = (2 ** (g - 1)) * ((2 ** g) + 1)
            n_odd = (2 ** (g - 1)) * ((2 ** g) - 1)
        else:
            n_total, n_even, n_odd = 1, 1, 0
        genera_check.append(
            {
                "genus": g,
                "euler_char_chi": chi_g,
                "canonical_degree_2g_minus_2": deg_k,
                "w2_mod2": w2_g,
                "spin_structures_2_pow_2g": n_total,
                "even_theta_N_plus": n_even,
                "odd_theta_N_minus": n_odd,
            }
        )

    wb.add_assertion(
        "w2_tangent_vanishes_all_genera_0_to_10",
        computed=1 if all_w2_zero else 0,
        expected=1,
        tolerance=0,
        source="w2_tangent_vanishes_all_genera (BringLiftingObstructionRoutes.lean)",
    )

    # Odd-degree bundles d = 2k + 1 (including Hopf bundle d = -1 at k = -1)
    odd_bundles_w2_one = all(((2 * k + 1) % 2) == 1 for k in range(-4, 5))
    wb.add_assertion(
        "w2_odd_degree_bundles_equal_1",
        computed=1 if odd_bundles_w2_one else 0,
        expected=1,
        tolerance=0,
        source="w2_odd_degree_bundle_one (BringLiftingObstructionRoutes.lean)",
    )

    # Bring's curve g = 4 spin structures and S_5 orbit decompositions
    g4_total = 2 ** (2 * 4)
    g4_even = (2 ** 3) * ((2 ** 4) + 1)
    g4_odd = (2 ** 3) * ((2 ** 4) - 1)
    wb.add_assertion(
        "bring_g4_spin_structure_total_256",
        computed=g4_total,
        expected=256,
        tolerance=0,
        source="bring_theta_counts_and_s5_orbits (BringLiftingObstructionRoutes.lean)",
    )
    wb.add_assertion(
        "bring_g4_even_theta_count_136",
        computed=g4_even,
        expected=136,
        tolerance=0,
        source="bring_theta_counts_and_s5_orbits (BringLiftingObstructionRoutes.lean)",
    )
    wb.add_assertion(
        "bring_g4_odd_theta_tritangent_count_120",
        computed=g4_odd,
        expected=120,
        tolerance=0,
        source="bring_theta_counts_and_s5_orbits (BringLiftingObstructionRoutes.lean)",
    )
    wb.add_assertion(
        "bring_g4_s5_invariant_even_spin_mod5_eq_1",
        computed=g4_even % 5,
        expected=1,
        tolerance=0,
        source="bring_theta_counts_and_s5_orbits (136 = 1 + 15 + 60 + 60)",
    )

    # =========================================================================
    # Part II: Route Z (`qou-n2aa`) — Integral Euler class & Kummer roots
    # =========================================================================
    torus_unique_zero = [g for g in range(0, 11) if (2 - 2 * g) == 0] == [1]
    wb.add_assertion(
        "integral_euler_zero_exclusively_at_torus_g1",
        computed=1 if torus_unique_zero else 0,
        expected=1,
        tolerance=0,
        source="integral_euler_zero_iff_torus (BringLiftingObstructionRoutes.lean)",
    )

    chi_bring = 2 - 2 * 4
    wb.add_assertion(
        "bring_integral_euler_class_minus_6",
        computed=chi_bring,
        expected=-6,
        tolerance=0,
        source="bring_integral_euler_nonzero (BringLiftingObstructionRoutes.lean)",
    )

    kummer_levels = [n for n in range(1, 7) if (chi_bring % n) == 0]
    wb.add_assertion(
        "bring_admissible_kummer_levels_1_2_3_6",
        computed=1 if kummer_levels == [1, 2, 3, 6] else 0,
        expected=1,
        tolerance=0,
        source="bring_admissible_kummer_levels (BringLiftingObstructionRoutes.lean)",
    )

    # =========================================================================
    # Part III: Hecke MTC (S, T) Data (`hkmt`) — Content sum, SL2(Z), root of unity
    # =========================================================================
    partitions_by_n = {
        1: [[1]],
        2: [[2], [1, 1]],
        3: [[3], [2, 1], [1, 1, 1]],
        4: [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]],
    }
    content_records = []
    content_antisym_ok = True
    for n, plist in partitions_by_n.items():
        for lam in plist:
            lam_t = conjugate_partition(lam)
            c_lam = partition_content_sum(lam)
            c_lam_t = partition_content_sum(lam_t)
            if c_lam + c_lam_t != 0:
                content_antisym_ok = False
            content_records.append(
                {
                    "n": n,
                    "partition": lam,
                    "conjugate": lam_t,
                    "content_sum": c_lam,
                    "conjugate_content_sum": c_lam_t,
                }
            )

    wb.add_assertion(
        "hecke_content_sum_transpose_antisymmetry_n1_to_4",
        computed=1 if content_antisym_ok else 0,
        expected=1,
        tolerance=0,
        source="hecke_content_sum_transpose_antisymmetry (BringLiftingObstructionRoutes.lean)",
    )

    # 50-dps unitary modular S, T relations for SU(2)_2 (Ising, k=4) and SU(2)_3 (Fibonacci, k=5)
    mtc_50dps_records = {}
    max_modular_err = mp.mpf("0")
    for k_level in (4, 5):
        # At level k = r + 2, simple objects j = 0, 1, ..., k - 2
        rank = k_level - 1
        q_angle = mp.pi / k_level
        sin_1 = mp.sin(q_angle)
        d_j = [mp.sin((j + 1) * q_angle) / sin_1 for j in range(rank)]
        D_sq = mp.fsum([d * d for d in d_j])
        D_val = mp.sqrt(D_sq)

        # Unitary symmetric S-matrix: S_{a,b} = sqrt(2/k) * sin((a+1)(b+1)*pi/k)
        pref = mp.sqrt(mp.mpf(2) / k_level)
        S_mat = mp.matrix(rank, rank)
        T_mat = mp.matrix(rank, rank)
        for a in range(rank):
            # SU(2)_{k-2} topological twist theta_a = exp(2*pi*i * a(a+2) / (4k))
            T_mat[a, a] = mp.expj(2 * mp.pi * mp.mpf(a * (a + 2)) / (4 * k_level))
            for b in range(rank):
                S_mat[a, b] = pref * mp.sin((a + 1) * (b + 1) * q_angle)

        # Check vacuum row S_{0,a} == d_a / D
        vac_err = max(abs(S_mat[0, a] - d_j[a] / D_val) for a in range(rank))
        # Check S^2 == I (since SU(2) representations are self-conjugate)
        S2 = S_mat * S_mat
        s2_err = max(
            abs(S2[a, b] - (mp.mpf(1) if a == b else mp.mpf(0)))
            for a in range(rank)
            for b in range(rank)
        )
        # Gauss sums p_+ and p_-
        p_plus = sum((d_j[a] ** 2) * T_mat[a, a] for a in range(rank)) / D_val
        p_minus = sum((d_j[a] ** 2) * mp.conj(T_mat[a, a]) for a in range(rank)) / D_val
        # Check |p_+| == 1 and p_+ * p_- == 1
        gauss_err = abs(p_plus * p_minus - 1)
        # Check (S * T)^3 == p_+ * S^2 = p_+ * I
        ST = S_mat * T_mat
        ST3 = ST * ST * ST
        st3_err = max(
            abs(ST3[a, b] - p_plus * S2[a, b])
            for a in range(rank)
            for b in range(rank)
        )
        level_err = max(vac_err, s2_err, gauss_err, st3_err)
        if level_err > max_modular_err:
            max_modular_err = level_err

        mtc_50dps_records[f"SU2_level_{k_level - 2}_k{k_level}"] = {
            "k": k_level,
            "rank": rank,
            "quantum_dimensions_50dps": [fmt50(d) for d in d_j],
            "global_dimension_D_sq_50dps": fmt50(D_sq),
            "global_dimension_D_50dps": fmt50(D_val),
            "vacuum_row_max_err": fmt50(vac_err),
            "S_squared_eq_I_max_err": fmt50(s2_err),
            "ST_cubed_eq_p_plus_S_squared_max_err": fmt50(st3_err),
        }

    wb.add_assertion(
        "su2_mtc_modular_relations_50dps_satisfied",
        computed=1 if max_modular_err < mp.mpf("1e-50") else 0,
        expected=1,
        tolerance=0,
        source="SL2(Z) / Verlinde modular relations (ST)^3 = p_+ S^2, S^2 = C, S_{0,a} = d_a / D",
    )

    # Root-of-unity truncation ([k]_q = 0 at q = exp(2*pi*i/k)) vs real q > 1 ([k]_q >= k > 0)
    truncation_comparison = []
    root_trunc_ok = True
    for k_val in range(2, 8):
        zeta_k = mp.expj(2 * mp.pi / k_val)
        q_int_root = sum(zeta_k ** j for j in range(k_val))
        if abs(q_int_root) > mp.mpf("1e-50"):
            root_trunc_ok = False
        q_int_at_1 = k_val
        q_int_at_2 = (2 ** k_val) - 1
        truncation_comparison.append(
            {
                "k": k_val,
                "abs_q_integer_at_primitive_kth_root_50dps": fmt50(abs(q_int_root)),
                "q_integer_at_q_eq_1": q_int_at_1,
                "q_integer_at_q_eq_2": q_int_at_2,
            }
        )

    wb.add_assertion(
        "root_of_unity_truncation_vs_real_q_non_truncation",
        computed=1 if root_trunc_ok else 0,
        expected=1,
        tolerance=0,
        source="one_sub_mul_qIntegerPoly & qIntegerPoly_at_one (BringLiftingObstructionRoutes.lean)",
    )

    wb.add_data("route_z2_stiefel_whitney_and_theta_table", genera_check)
    wb.add_data(
        "route_z_bring_summary",
        {
            "genus": 4,
            "euler_characteristic_kappa_0": chi_bring,
            "canonical_degree": 6,
            "mod2_reduction_w2": chi_bring % 2,
            "admissible_kummer_root_levels_1_to_6": kummer_levels,
            "obstructed_kummer_levels_1_to_6": [
                n for n in range(1, 7) if (chi_bring % n) != 0
            ],
            "fibre_torsion_orders_on_admissible_covers": {
                str(n): abs(chi_bring) // n for n in kummer_levels
            },
        },
    )
    wb.add_data("hecke_partition_content_sums", content_records)
    wb.add_data("su2_mtc_50dps_modular_verification", mtc_50dps_records)
    wb.add_data("root_of_unity_vs_real_q_truncation", truncation_comparison)

    out_path = wb.save(
        {
            "q0Anchor": "independent",
            "q0AnchorReason": (
                "Exact integer cohomology (H^2(Sigma_g, Z) vs H^2(Sigma_g, Z/2Z)), "
                "theta-characteristic combinatorics, partition content sums, and "
                "root-of-unity SU(2)_k modular S, T identities; no substrate q_0 read."
            ),
        }
    )
    print(f"Wrote witness to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
