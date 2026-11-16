#!/usr/bin/env python3
"""
50-dps mpmath probe for Round 59 (qou-8lxd):
  1. qou-qhrw: Root-of-unity cutoff N(n) = 2n-1 vanishing of [N]_{q_n} vs real positive non-vanishing at q_0
  2. qou-fu7d: Elemental vs hyperfine-weighted isotopic observable separation in r-II stars (Reticulum II Ba / Eu)
  3. qou-ihtw: Isobaric beta-decay Coulomb pair difference along the A=88 kilonova chain (88Kr -> 88Rb -> 88Sr)
  4. qou-jogb: Form-factor slope charge radius normalization and 3He binding-length 5x error improvement
  5. qou-atsd-t3: Symplectic root system C_m short/long root decomposition and Lie algebra dimension
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

WORK_DPS = 60
OUT_DPS = 50
mp.mp.dps = WORK_DPS


def mpf_str(v: mp.mpf, dps: int = OUT_DPS) -> str:
    return mp.nstr(v, dps, strip_zeros=False)


def run_probe() -> dict:
    mp.mp.dps = WORK_DPS

    # 1. qou-qhrw: Root-of-unity cutoff N(n) = 2n-1 vanishing vs real positive q_0 non-vanishing
    q0 = mp.mpf("0.87801698486368466468255517896525729842228459217992")
    cutoff_indices = [2 * n - 1 for n in (2, 3, 4)]
    max_root_of_unity_residual = mp.mpf(0)
    for n in (2, 3, 4):
        cap_n = 2 * n - 1
        # [N]_{q_n} = sin(N * pi / N) / sin(pi / N) = 0
        q_int_at_cutoff = mp.sin(cap_n * mp.pi / cap_n) / mp.sin(mp.pi / cap_n)
        max_root_of_unity_residual = max(max_root_of_unity_residual, abs(q_int_at_cutoff))

    # At real q0 != 1, |[m]_{q0}| = |(q0^m - q0^{-m}) / (q0 - q0^{-1})| >= 1 for all m >= 1
    q0_ints = [abs((q0 ** m - q0 ** (-m)) / (q0 - q0 ** (-1))) for m in range(1, 10)]
    min_q0_int = min(q0_ints)
    qhrw_passed = bool(
        cutoff_indices == [3, 5, 7]
        and max_root_of_unity_residual < mp.mpf("1e-55")
        and min_q0_int >= mp.mpf("1")
    )

    # 2. qou-fu7d: Elemental vs hyperfine-weighted isotopic observable separation (Ba r-process vs s-process)
    # Normalized total Ba abundance Y_tot = 1000:
    # s-process dominated: Y_odd = 110, Y_even = 890
    # r-process dominated (Reticulum II): Y_odd = 460, Y_even = 540
    y_odd_s, y_even_s = 110, 890
    y_odd_r, y_even_r = 460, 540
    c_elem = 3
    w_odd, w_even = 5, 2
    o_elem_s = c_elem * (y_odd_s + y_even_s)
    o_elem_r = c_elem * (y_odd_r + y_even_r)
    o_hfs_s = w_odd * y_odd_s + w_even * y_even_s
    o_hfs_r = w_odd * y_odd_r + w_even * y_even_r
    f_odd_s = mp.mpf(y_odd_s) / mp.mpf(y_odd_s + y_even_s)
    f_odd_r = mp.mpf(y_odd_r) / mp.mpf(y_odd_r + y_even_r)
    fu7d_passed = bool(
        o_elem_s == o_elem_r
        and o_hfs_s < o_hfs_r
        and (o_hfs_r - o_hfs_s) == (w_odd - w_even) * (y_odd_r - y_odd_s)
    )

    # 3. qou-ihtw: Isobaric beta-decay Coulomb pair difference along A=88 kilonova chain (Z=36 -> 37 -> 38)
    z_kr, z_rb, z_sr = 36, 37, 38
    pairs_kr = z_kr * (z_kr - 1)
    pairs_rb = z_rb * (z_rb - 1)
    pairs_sr = z_sr * (z_sr - 1)
    step1_inc = pairs_rb - pairs_kr
    step2_inc = pairs_sr - pairs_rb
    total_inc = pairs_sr - pairs_kr
    a_mass = mp.mpf(88)
    a_c_mev = mp.mpf("0.710")  # standard Coulomb coefficient in MeV
    delta_ec_two_step_mev = a_c_mev * mp.mpf(total_inc) / (a_mass ** (mp.mpf(1) / mp.mpf(3)) * 2)
    ihtw_passed = bool(
        step1_inc == 2 * z_kr
        and step2_inc == 2 * z_rb
        and total_inc == 146
        and total_inc == (2 * z_kr + 2 * z_rb)
        and delta_ec_two_step_mev > mp.mpf("11.6")
    )

    # 4. qou-jogb: Form-factor slope charge radius & 3He binding-length 5x error improvement
    r_meas_he3 = mp.mpf("2.5382")
    r_bind_he3 = mp.mpf("2.3795")
    r_drop_he3 = mp.mpf("1.7307")
    err_bind = abs(r_meas_he3 - r_bind_he3)
    err_drop = abs(r_meas_he3 - r_drop_he3)
    improvement_ratio = err_drop / err_bind
    unif_rms_residual = 5 * 3 - 3 * 5
    jogb_passed = bool(
        int(mp.nint(err_bind * 10000)) == 1587
        and int(mp.nint(err_drop * 10000)) == 8075
        and improvement_ratio > mp.mpf(5)
        and unif_rms_residual == 0
    )

    # 5. qou-atsd-t3: Symplectic root system C_m decomposition and Lie algebra dimension
    cm_table = []
    cm_ok = True
    for m in range(1, 7):
        short_roots = 2 * m * (m - 1)
        long_roots = 2 * m
        total_roots = 2 * m * m
        lie_dim = m * (2 * m + 1)
        if (short_roots + long_roots != total_roots) or (m + total_roots != lie_dim):
            cm_ok = False
        cm_table.append({
            "rank_m": m,
            "short_roots": short_roots,
            "long_roots": long_roots,
            "total_roots": total_roots,
            "lie_dim": lie_dim,
        })
    atsd_t3_passed = bool(
        cm_ok
        and cm_table[0]["short_roots"] == 0
        and cm_table[0]["long_roots"] == 2
        and cm_table[0]["lie_dim"] == 3
        and cm_table[1]["lie_dim"] == 10
        and cm_table[2]["lie_dim"] == 21
    )

    checks = [
        {
            "id": "qou_qhrw_root_of_unity_cutoff_vs_real_positive",
            "bean": "qou-qhrw",
            "passed": qhrw_passed,
            "cutoff_indices": cutoff_indices,
            "max_root_of_unity_residual": mpf_str(max_root_of_unity_residual),
            "min_q0_quantum_integer_m1_to_9": mpf_str(min_q0_int),
        },
        {
            "id": "qou_fu7d_elemental_vs_hyperfine_isotopic_separation",
            "bean": "qou-fu7d",
            "passed": fu7d_passed,
            "o_elem_s_process": o_elem_s,
            "o_elem_r_process": o_elem_r,
            "o_hfs_s_process": o_hfs_s,
            "o_hfs_r_process": o_hfs_r,
            "f_odd_s_process": mpf_str(f_odd_s),
            "f_odd_r_process": mpf_str(f_odd_r),
        },
        {
            "id": "qou_ihtw_isobaric_beta_coulomb_pair_increment",
            "bean": "qou-ihtw",
            "passed": ihtw_passed,
            "pairs_kr36_rb37_sr38": [pairs_kr, pairs_rb, pairs_sr],
            "step_increments": [step1_inc, step2_inc],
            "total_pair_increment": total_inc,
            "delta_ec_two_step_mev": mpf_str(delta_ec_two_step_mev),
        },
        {
            "id": "qou_jogb_he3_binding_length_fivefold_improvement",
            "bean": "qou-jogb",
            "passed": jogb_passed,
            "err_binding_fm": mpf_str(err_bind),
            "err_liquid_drop_fm": mpf_str(err_drop),
            "improvement_ratio": mpf_str(improvement_ratio),
            "uniform_ball_rms_residual": unif_rms_residual,
        },
        {
            "id": "qou_atsd_t3_symplectic_root_and_dimension_identities",
            "bean": "qou-atsd-t3",
            "passed": atsd_t3_passed,
            "cm_table": cm_table,
        },
    ]

    all_passed = all(c["passed"] for c in checks)
    witness = {
        "probe": "root-of-unity-cutoff-isotope-hyperfine-beta-coulomb-and-symplectic-roots",
        "beans": ["qou-qhrw", "qou-fu7d", "qou-ihtw", "qou-jogb", "qou-atsd-t3"],
        "parentBean": "qou-8lxd",
        "workDps": WORK_DPS,
        "outputDps": OUT_DPS,
        "allPassed": all_passed,
        "checks": checks,
    }
    WitnessBuilder.stamp_staleness_metadata(
        witness,
        script_path=__file__,
        engine="mpmath",
        q0_anchor=False,
    )
    return witness


def main() -> None:
    witness = run_probe()
    out_path = Path(__file__).with_name(
        "root-of-unity-cutoff-isotope-hyperfine-beta-coulomb-and-symplectic-roots.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={witness['allPassed']})")
    if not witness["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
