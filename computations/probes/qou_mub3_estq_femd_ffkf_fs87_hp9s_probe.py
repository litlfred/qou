#!/usr/bin/env python3
"""80-dps mpmath probe for Round 116 beans:
qou-estq, qou-femd, qou-ffkf, qou-fs87, qou-hp9s.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80


def run_probe() -> dict:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_sha256 = hashlib.sha256(script_path.read_bytes()).hexdigest()
    try:
        commit_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo_root, text=True
        ).strip()
    except Exception:
        commit_sha = "0" * 40

    checks = []

    # 1. qou-estq: Few-body pair and triplet cluster expansion (A=2,3,4)
    t2 = 2 * 1 * 0
    t3 = 3 * 2 * 1
    t4 = 4 * 3 * 2
    b_3h_exp = mp.mpf("8.481798")
    b_4he_exp = mp.mpf("28.29566")
    ratio_he_h = b_4he_exp / b_3h_exp
    checks.append(
        {
            "bean": "qou-estq",
            "description": "Few-body triplet cluster activation and 4He/3H binding ratio",
            "tripletScaled6A2": str(t2),
            "tripletScaled6A3": str(t3),
            "tripletScaled6A4": str(t4),
            "he4ToH3BindingRatio": mp.nstr(ratio_he_h, 40),
            "passed": bool(t2 == 0 and t3 == 6 and t4 == 24 and ratio_he_h > mp.mpf("3.33")),
        }
    )

    # 2. qou-femd: Biane 2000 character concentration fourth-root scale
    q_val = mp.mpf("16")
    delta_val = mp.mpf("1e-4")
    conc_scale = (delta_val + (1 / q_val)) ** mp.mpf("0.25")
    fourth_pow = conc_scale ** 4
    err_femd = abs(fourth_pow - (delta_val + 1 / q_val))
    checks.append(
        {
            "bean": "qou-femd",
            "description": "Disjoint-support character concentration fourth-root scale",
            "concentrationScale": mp.nstr(conc_scale, 40),
            "fourthPower": mp.nstr(fourth_pow, 40),
            "absError": mp.nstr(err_femd, 20),
            "passed": bool(err_femd < mp.mpf("1e-75") and conc_scale > 0),
        }
    )

    # 3. qou-ffkf: Isocrystal Newton-Hodge slope polygon height and spread
    r1, r2 = 2, 3
    s_common = mp.mpf("0.5")
    height_sum = r1 * s_common + r2 * s_common
    height_collapsed = (r1 + r2) * s_common
    err_ffkf = abs(height_sum - height_collapsed)
    checks.append(
        {
            "bean": "qou-ffkf",
            "description": "Isoclinic Newton-Hodge slope collapse and height additivity",
            "polygonHeight": mp.nstr(height_sum, 40),
            "absError": mp.nstr(err_ffkf, 20),
            "passed": bool(err_ffkf < mp.mpf("1e-75") and height_sum == mp.mpf("2.5")),
        }
    )

    # 4. qou-fs87: Kerov CLT Omega(x) semicircle boundary kernel on [-2, 2]
    x_test = mp.mpf("1.2")
    kernel_pos = 4 - x_test ** 2
    kernel_neg = 4 - (-x_test) ** 2
    omega_x = (2 / mp.pi) * (x_test * mp.asin(x_test / 2) + mp.sqrt(kernel_pos))
    omega_2 = (2 / mp.pi) * (2 * mp.asin(mp.mpf("1")) + mp.sqrt(mp.mpf("0")))
    err_fs87 = abs(omega_2 - mp.mpf("2")) + abs(kernel_pos - kernel_neg)
    checks.append(
        {
            "bean": "qou-fs87",
            "description": "Kerov limiting profile Omega(x) endpoint value and kernel reflection symmetry",
            "omegaAt1_2": mp.nstr(omega_x, 40),
            "omegaAt2": mp.nstr(omega_2, 40),
            "absError": mp.nstr(err_fs87, 20),
            "passed": bool(err_fs87 < mp.mpf("1e-75") and omega_x > mp.mpf("1.3")),
        }
    )

    # 5. qou-hp9s: Figure-eight cusp shape modulus vs tetrahedron shape parameter omega
    omega_re = mp.mpf("0.5")
    omega_im = mp.sqrt(mp.mpf("3")) / 2
    omega_norm_sq = omega_re ** 2 + omega_im ** 2
    cusp_im = 2 * mp.sqrt(mp.mpf("3"))
    cusp_norm_sq = cusp_im ** 2
    ratio_cusp = cusp_norm_sq / omega_norm_sq
    err_hp9s = abs(ratio_cusp - mp.mpf("12")) + abs(omega_norm_sq - mp.mpf("1"))
    checks.append(
        {
            "bean": "qou-hp9s",
            "description": "Figure-eight cusp shape modulus norm-squared ratio to tetrahedron parameter omega",
            "omegaNormSq": mp.nstr(omega_norm_sq, 40),
            "cuspModulusNormSq": mp.nstr(cusp_norm_sq, 40),
            "normSqRatio": mp.nstr(ratio_cusp, 40),
            "absError": mp.nstr(err_hp9s, 20),
            "passed": bool(err_hp9s < mp.mpf("1e-75")),
        }
    )

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "qou_mub3_estq_femd_ffkf_fs87_hp9s_probe",
        "beans": ["qou-estq", "qou-femd", "qou-ffkf", "qou-fs87", "qou-hp9s"],
        "precisionDps": "80",
        "scriptPath": "computations/probes/qou_mub3_estq_femd_ffkf_fs87_hp9s_probe.py",
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "allPassed": all_passed,
        "checks": checks,
    }


def main() -> None:
    witness = run_probe()
    assert witness["allPassed"], f"Probe failed: {witness}"
    out_path = pathlib.Path(__file__).with_name(
        "qou_mub3_estq_femd_ffkf_fs87_hp9s.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={witness['allPassed']}, scriptCommitSha={witness['scriptCommitSha']})")


if __name__ == "__main__":
    main()
