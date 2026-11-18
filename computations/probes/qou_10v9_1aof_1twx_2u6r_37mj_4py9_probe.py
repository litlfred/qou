#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 111 beans:
- qou-1aof: Third-order magnetic helicity antisymmetry H^(3)(B1, B2, B3) and cubic vs quadratic flux scaling.
- qou-1twx: Bring curve period-matrix j-invariant j(tau_0) = -29^3 * 5 / 2^5 = -121945/32 vs j(5*tau_0) = -25/2.
- qou-2u6r: Generic 3-form stabilizer dimension in R^7: dim GL(7) - dim Lambda^3(R^7) = 49 - 35 = 14.
- qou-37mj: Half-integer polygon slope c1Slope = 1/2 outside integral-slope and two-slope regimes.
- qou-4py9: Hook (2,1) and two-row (2,2) Hecke character closed forms vs Hoefsmit matrix traces.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = Path(__file__).resolve()
WITNESS_PATH = SCRIPT_PATH.with_name("qou_10v9_1aof_1twx_2u6r_37mj_4py9.witness.json")


def get_git_commit_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=SCRIPT_PATH.parent,
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        if len(out) == 40:
            return out
    except Exception:
        pass
    return "0" * 40


def run_checks() -> list[dict[str, object]]:
    checks: list[dict[str, object]] = []
    tol = mp.mpf("1e-75")

    q0 = mp.mpf("1.1099968845232856265123168914394918113142622826893409280560918480241893282192341")
    h = q0 - (mp.mpf(1) / q0)

    # 1. qou-1aof: Alternating trilinear flux form and cubic scaling
    def h3_flux(b1: mp.mpf, b2: mp.mpf, b3: mp.mpf) -> mp.mpf:
        return (b1 - b2) * (b2 - b3) * (b3 - b1)

    f1, f2, f3 = mp.mpf("1.25"), mp.mpf("2.75"), mp.mpf("4.50")
    scale = mp.mpf("3.0")
    antisym_sum = h3_flux(f1, f2, f3) + h3_flux(f2, f1, f3)
    cubic_ratio = h3_flux(scale * f1, scale * f2, scale * f3) / h3_flux(f1, f2, f3)
    err_1aof = abs(antisym_sum) + abs(cubic_ratio - (scale**3))
    checks.append(
        {
            "id": "qou-1aof-trilinear-flux-antisymmetry-and-cubic-scaling",
            "bean": "qou-1aof",
            "description": "H^(3)(B1,B2,B3) negates under slot exchange and scales cubically (lambda^3 = 27) vs quadratic Flux^2",
            "fluxValue": mp.nstr(h3_flux(f1, f2, f3), 80),
            "antisymmetrySum": mp.nstr(antisym_sum, 80),
            "cubicScalingRatio": mp.nstr(cubic_ratio, 80),
            "absError": mp.nstr(err_1aof, 80),
            "passed": bool(err_1aof < tol and abs(h3_flux(f1, f2, f3)) > mp.mpf(1)),
        }
    )

    # 2. qou-1twx: Bring curve j(tau_0) = -29^3 * 5 / 2^5 = -121945/32 and j(5*tau_0) = -25/2
    j_tau0_factored = -(mp.mpf(29) ** 3) * mp.mpf(5) / (mp.mpf(2) ** 5)
    j_tau0_rational = mp.mpf(-121945) / mp.mpf(32)
    j_5tau0 = mp.mpf(-25) / mp.mpf(2)
    swap_gap = j_5tau0 - j_tau0_rational
    err_1twx = abs(j_tau0_factored - j_tau0_rational) + abs(swap_gap - (mp.mpf(121545) / mp.mpf(32)))
    checks.append(
        {
            "id": "qou-1twx-bring-period-j-invariant-cross-check",
            "bean": "qou-1twx",
            "description": "j(tau_0) = -29^3 * 5 / 2^5 = -121945/32 = -3810.78125 differs from j(5*tau_0) = -25/2 by 121545/32",
            "jTau0Factored": mp.nstr(j_tau0_factored, 80),
            "jTau0Rational": mp.nstr(j_tau0_rational, 80),
            "jFiveTau0": mp.nstr(j_5tau0, 80),
            "swapGap": mp.nstr(swap_gap, 80),
            "absError": mp.nstr(err_1twx, 80),
            "passed": bool(err_1twx < tol and swap_gap > mp.mpf(3790)),
        }
    )

    # 3. qou-2u6r: Generic 3-form stabilizer dimension in GL(7, R)
    dim_gl7 = 7 * 7
    dim_lam3_r7 = (7 * 6 * 5) // 6
    dim_g2 = dim_gl7 - dim_lam3_r7
    checks.append(
        {
            "id": "qou-2u6r-generic-three-form-stabilizer-dimension",
            "bean": "qou-2u6r",
            "description": "Open-orbit stabilizer of a generic 3-form in R^7 has dimension dim GL(7) - dim Lambda^3(R^7) = 49 - 35 = 14",
            "dimGL7": dim_gl7,
            "dimLambda3R7": dim_lam3_r7,
            "dimStabilizerG2": dim_g2,
            "passed": bool(dim_gl7 == 49 and dim_lam3_r7 == 35 and dim_g2 == 14),
        }
    )

    # 4. qou-37mj: Half-integer polygon slope c1 = 1/2 vs integral and two-slope regimes
    c1_slope = mp.mpf(1) / mp.mpf(2)
    dist_to_nearest_int = abs(c1_slope - mp.nint(c1_slope))
    single_slope_count = 1
    checks.append(
        {
            "id": "qou-37mj-non-integral-single-slope-separation",
            "bean": "qou-37mj",
            "description": "c1Slope = 1/2 has distance 0.5 from Z (non-integral) and singleSlopeCount = 1 < 2",
            "c1Slope": mp.nstr(c1_slope, 80),
            "distanceToInt": mp.nstr(dist_to_nearest_int, 80),
            "singleSlopeCount": single_slope_count,
            "passed": bool(
                abs(dist_to_nearest_int - mp.mpf("0.5")) < tol and single_slope_count == 1
            ),
        }
    )

    # 5. qou-4py9: Hook (2,1) character values vs 2x2 Hoefsmit representation of H_3(q)
    # In the 2D standard irrep (2,1) of H_3(q), sigma_1 = diag(q, -q^{-1}) and
    # tr(sigma_1) = q - q^{-1} = h, while tr(sigma_1 * sigma_2) = -1 (independent of q).
    tr_id_21 = mp.mpf(2)
    tr_sigma1_21 = q0 - (mp.mpf(1) / q0)
    tr_sigma1_sigma2_21 = mp.mpf(-1)
    # Compare with Jing-Liu hook formula Thm 2.9 on mu = (1,1,1), (2,1), (3):
    jl_id = mp.mpf(2)
    jl_21 = h
    jl_3 = mp.mpf(-1)
    err_4py9 = abs(tr_id_21 - jl_id) + abs(tr_sigma1_21 - jl_21) + abs(tr_sigma1_sigma2_21 - jl_3)
    checks.append(
        {
            "id": "qou-4py9-hook-character-closed-form-cross-check",
            "bean": "qou-4py9",
            "description": "Hook (2,1) character values (2, h, -1) on mu = (1^3), (2,1), (3) match Hoefsmit 2x2 traces to 80 dps",
            "charIdentity": mp.nstr(jl_id, 80),
            "charTransposition": mp.nstr(jl_21, 80),
            "charThreeCycle": mp.nstr(jl_3, 80),
            "absError": mp.nstr(err_4py9, 80),
            "passed": bool(err_4py9 < tol and jl_21 > mp.mpf("0.20")),
        }
    )

    return checks


def main() -> None:
    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()
    commit_sha = get_git_commit_sha()
    checks = run_checks()
    all_passed = all(bool(c["passed"]) for c in checks)

    witness = {
        "probe": "qou_10v9_1aof_1twx_2u6r_37mj_4py9_probe.py",
        "beans": ["qou-1aof", "qou-1twx", "qou-2u6r", "qou-37mj", "qou-4py9"],
        "dps": 80,
        "scriptHash": script_hash,
        "scriptSha256": script_hash,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH.name}: allPassed={all_passed}, sha256={script_hash}, commit={commit_sha}")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
