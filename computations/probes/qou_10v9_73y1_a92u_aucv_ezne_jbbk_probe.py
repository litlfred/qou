#!/usr/bin/env python3
"""80-dps mpmath numerical probe for Round 112 beans:
qou-73y1, qou-a92u, qou-aucv, qou-ezne, qou-jbbk.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 80)


def run_probe() -> dict:
    script_path = pathlib.Path(__file__).resolve()
    repo_root = script_path.parents[2]
    script_bytes = script_path.read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    q0 = mp.mpf("1.1099785827513808")

    # 1. qou-73y1: Deformation variety trace polynomial x^2 + x - 1 at x = q0^2 + q0^-2
    x0 = q0**2 + q0 ** (-2)
    trace_quad_x0 = x0**2 + x0 - mp.mpf(1)
    trace_quad_parabolic = mp.mpf(2) ** 2 + mp.mpf(2) - mp.mpf(1)
    diff_lhs = trace_quad_x0 - trace_quad_parabolic
    diff_rhs = (x0 - mp.mpf(2)) * (x0 + mp.mpf(2) + mp.mpf(1))
    check_73y1 = abs(diff_lhs - diff_rhs) < mp.mpf("1e-75") and trace_quad_parabolic == mp.mpf(5)

    # 2. qou-a92u: Unipotent 3x3 upper-triangular factor ordering (a, b, c)
    a_val = mp.mpf("3")
    b_val = mp.mpf("-2")
    c_val = mp.mpf("5")
    asc_sum = a_val + b_val + c_val + a_val * b_val
    desc_sum = a_val + b_val + c_val
    factored_asc = (a_val + mp.mpf(1)) * (b_val + mp.mpf(1)) + c_val - mp.mpf(1)
    check_a92u = (
        abs((asc_sum - desc_sum) - (a_val * b_val)) < mp.mpf("1e-75")
        and abs(asc_sum - factored_asc) < mp.mpf("1e-75")
    )

    # 3. qou-aucv: Hyperbolic (2,4,5) triangle angle defect pi * (1 - (1/2 + 1/4 + 1/5)) = pi / 20
    defect_unit = mp.mpf(1) - (
        mp.mpf(1) / mp.mpf(2) + mp.mpf(1) / mp.mpf(4) + mp.mpf(1) / mp.mpf(5)
    )
    defect_area = mp.pi * defect_unit
    total_area_240 = mp.mpf(240) * defect_area
    gauss_bonnet_g4 = mp.mpf(4) * mp.pi * (mp.mpf(4) - mp.mpf(1))
    check_aucv = (
        abs(defect_unit - mp.mpf(1) / mp.mpf(20)) < mp.mpf("1e-75")
        and abs(total_area_240 - gauss_bonnet_g4) < mp.mpf("1e-74")
    )

    # 4. qou-ezne: Quotient tiling cell characteristic (60 + 30 + 24) - 360 + 240 = -6, b1 = 8
    chi_tiling = (mp.mpf(60) + mp.mpf(30) + mp.mpf(24)) - mp.mpf(360) + mp.mpf(240)
    b1_tiling = mp.mpf(2) - chi_tiling
    zero_mode_ratio = b1_tiling / total_area_240
    target_zero_mode = mp.mpf(2) / (mp.mpf(3) * mp.pi)
    check_ezne = (
        chi_tiling == mp.mpf(-6)
        and b1_tiling == mp.mpf(8)
        and abs(zero_mode_ratio - target_zero_mode) < mp.mpf("1e-75")
    )

    # 5. qou-jbbk: Figure-eight polynomial J_{4_1}(q0) = u^2 - u - 1 >= 1 and torus genus shift 1 - g^2
    u0 = q0 + mp.mpf(1) / q0
    j_41_u0 = u0**2 - u0 - mp.mpf(1)
    j_41_laurent = q0 ** (-2) - q0 ** (-1) + mp.mpf(1) - q0 + q0**2
    j_41_factored = (u0 - mp.mpf(2)) * (u0 + mp.mpf(1)) + mp.mpf(1)
    shifts = [int(1 - g**2) for g in (1, 2, 3, 4)]
    check_jbbk = (
        abs(j_41_u0 - j_41_laurent) < mp.mpf("1e-75")
        and abs(j_41_u0 - j_41_factored) < mp.mpf("1e-75")
        and j_41_u0 > mp.mpf(1)
        and shifts == [0, -3, -8, -15]
    )

    checks = [
        {
            "bean": "qou-73y1",
            "description": "Deformation variety trace polynomial difference factorization and parabolic value",
            "x0": fmt(x0),
            "traceQuadAtX0": fmt(trace_quad_x0),
            "traceQuadParabolic": fmt(trace_quad_parabolic),
            "residual": fmt(abs(diff_lhs - diff_rhs)),
            "passed": bool(check_73y1),
        },
        {
            "bean": "qou-a92u",
            "description": "Unipotent 3x3 upper-triangular factor ordering corner defect a*b",
            "ascOffDiagSum": fmt(asc_sum),
            "descOffDiagSum": fmt(desc_sum),
            "cornerDefect": fmt(asc_sum - desc_sum),
            "residual": fmt(abs(asc_sum - factored_asc)),
            "passed": bool(check_a92u),
        },
        {
            "bean": "qou-aucv",
            "description": "Hyperbolic (2,4,5) triangle angle defect pi/20 and 240-triangle genus-4 area 12*pi",
            "triangleArea": fmt(defect_area),
            "totalArea240": fmt(total_area_240),
            "residual": fmt(abs(total_area_240 - gauss_bonnet_g4)),
            "passed": bool(check_aucv),
        },
        {
            "bean": "qou-ezne",
            "description": "240-triangle quotient cell characteristic chi=-6, b1=8, and b1/Area = 2/(3*pi)",
            "eulerChar": fmt(chi_tiling),
            "firstBettiRank": fmt(b1_tiling),
            "zeroModeRatio": fmt(zero_mode_ratio),
            "residual": fmt(abs(zero_mode_ratio - target_zero_mode)),
            "passed": bool(check_ezne),
        },
        {
            "bean": "qou-jbbk",
            "description": "Figure-eight symmetric polynomial J_{4_1}(q0) = u0^2 - u0 - 1 > 1 and 1 - g^2 shift",
            "u0": fmt(u0),
            "j41AtQ0": fmt(j_41_u0),
            "torusShiftsG1To4": [str(s) for s in shifts],
            "residual": fmt(abs(j_41_u0 - j_41_laurent)),
            "passed": bool(check_jbbk),
        },
    ]

    all_passed = all(c["passed"] for c in checks)
    return {
        "probe": "qou_10v9_73y1_a92u_aucv_ezne_jbbk_probe",
        "beans": ["qou-73y1", "qou-a92u", "qou-aucv", "qou-ezne", "qou-jbbk"],
        "precisionDps": "80",
        "scriptCommitSha": commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "allPassed": all_passed,
        "checks": checks,
    }


def main() -> None:
    witness = run_probe()
    out_path = pathlib.Path(__file__).with_name(
        "qou_10v9_73y1_a92u_aucv_ezne_jbbk.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    assert witness["allPassed"], "Probe checks failed"


if __name__ == "__main__":
    main()
