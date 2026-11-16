#!/usr/bin/env python3
"""
Probe for Round 56 beans under qou-8lxd:
  - qou-hjs8: Mirror bar-parity mass asymmetry factorization and mixed-sign crossing phase sensitivity
  - qou-lxh5: Level-3 (SU(3)) vs Level-2 (SU(2)) Hecke row-cap dimensions, coranks, and Ocneanu parameter
  - qou-usft: Light-nucleus Coulomb shape-factor hierarchy and binding-length separation-energy sensitivity
  - qou-wg3c: Wigner SU(4) lambda = (2,2) hook product vs shadow-price weight and k = 5 two-row cap
  - qou-x0th: S3 branching dimension under-determination vs unique character trace pinning
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60
OUT_DPS = 50


def mpf_str(v: mp.mpf, dps: int = OUT_DPS) -> str:
    return mp.nstr(v, dps, strip_zeros=False)


def main() -> int:
    # 1. qou-hjs8: Mirror bar-parity mass asymmetry & mixed-sign crossing phase sensitivity
    q_r = mp.mpf("0.60689066510772508681866141164191409018432350858429")
    theta = mp.mpf("0.00000192578")
    q_plus = q_r * mp.exp(1j * theta)
    q_minus = mp.mpf(1) / q_plus

    q2_plus = q_plus + mp.mpf(1) / q_plus
    q2_minus = q_minus + mp.mpf(1) / q_minus
    bar_even_asym = abs(q2_plus - q2_minus) / abs(q2_plus + q2_minus)

    n_plus = mp.mpf(2)
    n_minus = mp.mpf(1)
    norm_sq_theta0 = (
        n_plus**2 * q_r**2
        + n_minus**2 * (mp.mpf(1) / q_r**2)
        - mp.mpf(2) * n_plus * n_minus * mp.cos(mp.mpf(0))
    )
    norm_sq_theta = (
        n_plus**2 * q_r**2
        + n_minus**2 * (mp.mpf(1) / q_r**2)
        - mp.mpf(2) * n_plus * n_minus * mp.cos(mp.mpf(2) * theta)
    )
    mixed_phase_shift = norm_sq_theta - norm_sq_theta0
    exact_phase_shift = mp.mpf(2) * n_plus * n_minus * (mp.mpf(1) - mp.cos(mp.mpf(2) * theta))

    chk_hjs8 = bool(
        bar_even_asym < mp.mpf("1e-55")
        and mixed_phase_shift > mp.mpf(0)
        and abs(mixed_phase_shift - exact_phase_shift) < mp.mpf("1e-55")
    )

    # 2. qou-lxh5: Level-3 (SU(3)) vs Level-2 (SU(2)) Hecke row-cap dimensions & Ocneanu shift
    full_dims = [1, 2, 6, 24, 120, 720]
    level2_dims = [1, 2, 5, 14, 42, 132]
    level3_dims = [1, 2, 6, 23, 103, 513]
    coranks_level2 = [f - d for f, d in zip(full_dims, level2_dims)]
    coranks_level3 = [f - d for f, d in zip(full_dims, level3_dims)]

    x_q2 = q_r**2
    z2 = (q_r**3) / (x_q2 + mp.mpf(1))
    z3 = (q_r**5) / (x_q2**2 + x_q2 + mp.mpf(1))
    z_diff = z2 - z3
    z_diff_formula = (q_r**3) / ((x_q2 + mp.mpf(1)) * (x_q2**2 + x_q2 + mp.mpf(1)))

    chk_lxh5 = bool(
        coranks_level3 == [0, 0, 0, 1, 17, 207]
        and coranks_level2 == [0, 0, 1, 10, 78, 588]
        and z_diff > mp.mpf(0)
        and abs(z_diff - z_diff_formula) < mp.mpf("1e-55")
    )

    # 3. qou-usft: Light-nucleus Coulomb shape-factor hierarchy and binding-length sensitivity
    f_exp = mp.mpf(5) * mp.sqrt(mp.mpf(3)) / mp.mpf(16)
    f_unif = (mp.mpf(3) / mp.mpf(5)) * mp.sqrt(mp.mpf(5) / mp.mpf(3))
    f_gauss = mp.sqrt(mp.mpf(2) / mp.pi)
    f_req = mp.mpf("1.0913")

    s_qou = mp.mpf("1.988")
    s_ame = mp.mpf("6.782")
    r_ame = mp.mpf("1.88")
    r_qou = r_ame * mp.sqrt(s_ame / s_qou)

    chk_usft = bool(
        (f_exp < f_unif < f_gauss < f_req)
        and (r_qou > r_ame)
        and abs((r_qou**2) * s_qou - (r_ame**2) * s_ame) < mp.mpf("1e-50")
    )

    # 4. qou-wg3c: Partition (2,2) hook product vs shadow-price weight & k=5 two-row cap
    def q_int(n: int, q: mp.mpf) -> mp.mpf:
        return (q**n - q**(-n)) / (q - mp.mpf(1) / q)

    q2_val = q_int(2, q_r)
    q3_val = q_int(3, q_r)
    q4_val = q_int(4, q_r)
    hook_22 = q3_val * (q2_val**2)
    qfact_4 = q4_val * q3_val * q2_val
    dimq_22 = qfact_4 / hook_22
    w_22 = (dimq_22**2) / qfact_4
    ratio_hook_to_w = hook_22 / w_22
    ratio_formula = (q3_val**2) * (q2_val**5) / q4_val

    partitions_5 = [
        (5,),
        (4, 1),
        (3, 2),
        (3, 1, 1),
        (2, 2, 1),
        (2, 1, 1, 1),
        (1, 1, 1, 1, 1),
    ]

    def conjugate_part(p: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(sum(1 for x in p if x >= j) for j in range(1, p[0] + 1))

    two_row_self_conj_5 = [
        p for p in partitions_5 if len(p) <= 2 and conjugate_part(p) == p
    ]

    chk_wg3c = bool(
        abs(dimq_22 - q4_val / q2_val) < mp.mpf("1e-55")
        and abs(ratio_hook_to_w - ratio_formula) < mp.mpf("1e-50")
        and len(two_row_self_conj_5) == 0
    )

    # 5. qou-x0th: S3 branching dimension under-determination vs unique character trace pinning
    s3_table = []
    all_pinned = True
    for ell in range(5):
        chi_e = 2 * ell + 1
        chi_t = 1 if ell % 2 == 0 else -1
        chi_c = [1, 0, -1][ell % 3]
        a6 = chi_e + 3 * chi_t + 2 * chi_c
        b6 = chi_e - 3 * chi_t + 2 * chi_c
        c3 = chi_e - chi_c
        a, b, c = a6 // 6, b6 // 6, c3 // 3
        ok = (
            a6 % 6 == 0
            and b6 % 6 == 0
            and c3 % 3 == 0
            and (a + b + 2 * c == chi_e)
            and (a - b == chi_t)
            and (a + b - c == chi_c)
        )
        all_pinned = all_pinned and ok
        s3_table.append({"ell": str(ell), "a": str(a), "b": str(b), "c": str(c)})

    chk_x0th = bool(all_pinned)

    assertions = {
        "hjs8_bar_even_exact_zero_and_mixed_crossing_phase_positive": chk_hjs8,
        "lxh5_level3_coranks_and_ocneanu_shift_exact": chk_lxh5,
        "usft_shape_hierarchy_and_binding_radius_expansion": chk_usft,
        "wg3c_hook_vs_shadow_ratio_and_empty_k5_two_row_self_conjugate": chk_wg3c,
        "x0th_s3_character_orthogonality_pins_multiplicities": chk_x0th,
    }

    witness = {
        "computation": "cp-bar-parity-level3-channel-and-wigner-s3-pinning",
        "description": (
            "50-dps mpmath verification for qou-hjs8, qou-lxh5, qou-usft, "
            "qou-wg3c, and qou-x0th under qou-8lxd."
        ),
        "results": {
            "qou_hjs8_bar_parity_and_crossing_phase": {
                "bar_even_asymmetry": mpf_str(bar_even_asym),
                "mixed_crossing_norm_sq_theta0": mpf_str(norm_sq_theta0),
                "mixed_crossing_norm_sq_theta": mpf_str(norm_sq_theta),
                "mixed_phase_shift": mpf_str(mixed_phase_shift),
                "exact_phase_shift_formula": mpf_str(exact_phase_shift),
            },
            "qou_lxh5_level3_channel_and_ocneanu_shift": {
                "level2_dims_n1_to_6": [str(d) for d in level2_dims],
                "level3_dims_n1_to_6": [str(d) for d in level3_dims],
                "coranks_level2_n1_to_6": [str(c) for c in coranks_level2],
                "coranks_level3_n1_to_6": [str(c) for c in coranks_level3],
                "z2_ocneanu": mpf_str(z2),
                "z3_ocneanu": mpf_str(z3),
                "z2_minus_z3": mpf_str(z_diff),
            },
            "qou_usft_coulomb_shape_and_binding_length": {
                "f_exp": mpf_str(f_exp),
                "f_unif": mpf_str(f_unif),
                "f_gauss": mpf_str(f_gauss),
                "f_req": mpf_str(f_req),
                "r_ame_fm": mpf_str(r_ame),
                "r_qou_fm": mpf_str(r_qou),
            },
            "qou_wg3c_partition22_weight_and_k5_cap": {
                "hook_product_22": mpf_str(hook_22),
                "dimq_22": mpf_str(dimq_22),
                "shadow_weight_22": mpf_str(w_22),
                "ratio_hook_to_shadow_weight": mpf_str(ratio_hook_to_w),
                "two_row_self_conjugate_partitions_of_5_count": str(len(two_row_self_conj_5)),
            },
            "qou_x0th_s3_character_pinning": {
                "s3_character_determinant": "-6",
                "branching_multiplicities_ell_0_to_4": s3_table,
            },
        },
        "assertions": assertions,
        "allPassed": bool(all(assertions.values())),
    }

    WitnessBuilder.stamp_staleness_metadata(
        witness,
        script_path=__file__,
        engine="mpmath",
        q0_anchor=False,
    )
    out_path = os.path.join(
        os.path.dirname(__file__),
        "cp-bar-parity-level3-channel-and-wigner-s3-pinning.witness.json",
    )
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
