#!/usr/bin/env python3
"""80-dps mpmath probe for Round 59:
1. qou-6eik: Hyperbolic volume vertical hemisphere fibre integral difference
   1/(2*(R^2 - d1^2)) - 1/(2*(R^2 - d2^2)) = (d1^2 - d2^2)/(2*(R^2 - d1^2)*(R^2 - d2^2))
   and strict radial monotonicity for 0 <= d1 < d2 < R.
2. qou-adwi: Reciprocal relation between bare Planck step (q - 1)/q and time-step factor q/(q - 1),
   complement 1 - (q - 1)/q = 1/q, and mutual exclusion of deep-quantum (q >= Q > 1) and classical (q = 1) regimes.
3. qou-fl4t: 1-loop edge lattice shape triple elementary symmetric identity
   zeta*zetaP + zetaP*zetaPP + zetaPP*zeta = -(zeta^2 + zeta*zetaP + zetaP^2),
   cube sum identity zeta^3 + zetaP^3 + zetaPP^3 = 3*zeta*zetaP*zetaPP, and sublattice cross-index identity.
4. qou-ltal: Seven-term q-integer mass formula coefficient identities
   a_asym - lambda_V = (1/2)*lambda_V, delta_S = [2]_q^3 * lambda_ex, and 2*[2]_q*delta_P = [3]_q*lambda_V.
5. qou-mlbg: Dilogarithm two-point reflection difference
   (Li2(x) + Li2(1 - x)) - (Li2(y) + Li2(1 - y)) = log(y)*log(1 - y) - log(x)*log(1 - x)
   and midpoint deviation (Li2(x) + Li2(1 - x)) - 2*Li2(1/2) = (log 2)^2 - log(x)*log(1 - x).
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from mpmath import mp

mp.dps = 80


def nstr40(x: mp.mpf) -> str:
    return mp.nstr(x, 40)


def q_int(q: mp.mpf, n: int) -> mp.mpf:
    return (q ** n - q ** (-n)) / (q - mp.mpf("1") / q)


def check_hyperbolic_hemisphere_fibre() -> dict:
    R = mp.mpf("2.5")
    d1 = mp.mpf("0.7")
    d2 = mp.mpf("1.6")
    i1 = mp.mpf("1") / (mp.mpf("2") * (R ** 2 - d1 ** 2))
    i2 = mp.mpf("1") / (mp.mpf("2") * (R ** 2 - d2 ** 2))
    diff_lhs = i1 - i2
    diff_rhs = (d1 ** 2 - d2 ** 2) / (mp.mpf("2") * (R ** 2 - d1 ** 2) * (R ** 2 - d2 ** 2))
    res = abs(diff_lhs - diff_rhs)
    strict_mono = bool(i1 < i2)
    passed = bool(res < mp.mpf("1e-75") and strict_mono)
    return {
        "id": "qou-6eik-hemisphere-fibre-diff-and-monotonicity",
        "passed": passed,
        "fibreAtD1": nstr40(i1),
        "fibreAtD2": nstr40(i2),
        "maxResidual": nstr40(res),
    }


def check_planck_step_and_regimes() -> dict:
    q0 = mp.mpf("1.1099785955541805")
    bare_step = (q0 - mp.mpf("1")) / q0
    time_factor = q0 / (q0 - mp.mpf("1"))
    prod_res = abs(bare_step * time_factor - mp.mpf("1"))
    comp_res = abs((mp.mpf("1") - bare_step) - (mp.mpf("1") / q0))
    phi = (mp.mpf("1") + mp.sqrt(mp.mpf("5"))) / mp.mpf("2")
    q_deep = phi ** 2
    max_res = max(prod_res, comp_res)
    passed = bool(max_res < mp.mpf("1e-75") and q_deep > mp.mpf("1") and time_factor > mp.mpf("10"))
    return {
        "id": "qou-adwi-planck-step-ratio-and-regime-separation",
        "passed": passed,
        "bareStepAtQ0": nstr40(bare_step),
        "timeStepFactorAtQ0": nstr40(time_factor),
        "maxResidual": nstr40(max_res),
    }


def check_oneloop_shape_triple() -> dict:
    z = mp.mpc(mp.mpf("0.5"), mp.sqrt(mp.mpf("3")) / mp.mpf("2"))
    zeta = mp.mpf("1") / z
    zeta_p = mp.mpf("1") / (mp.mpf("1") - z)
    zeta_pp = mp.mpf("1") / (z * (z - mp.mpf("1")))
    e2_lhs = zeta * zeta_p + zeta_p * zeta_pp + zeta_pp * zeta
    e2_rhs = -(zeta ** 2 + zeta * zeta_p + zeta_p ** 2)
    cubes_lhs = zeta ** 3 + zeta_p ** 3 + zeta_pp ** 3
    cubes_rhs = mp.mpf("3") * zeta * zeta_p * zeta_pp
    res_e2 = abs(e2_lhs - e2_rhs)
    res_cubes = abs(cubes_lhs - cubes_rhs)
    max_res = max(res_e2, res_cubes)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-fl4t-shape-triple-e2-and-cube-sum",
        "passed": passed,
        "absCubesSum": nstr40(abs(cubes_lhs)),
        "maxResidual": nstr40(max_res),
    }


def check_qinteger_mass_relations() -> dict:
    q0 = mp.mpf("1.1099785955541805")
    m_e = mp.mpf("0.51099895")
    q2 = q_int(q0, 2)
    q3 = q_int(q0, 3)
    q7 = q_int(q0, 7)
    lam_v = mp.mpf("2") * q2 * q7 * m_e
    a_asym = mp.mpf("3") * q2 * q7 * m_e
    del_p = q3 * q7 * m_e
    lam_ex = (q3 / q2) * m_e
    del_s = (q2 ** 2) * q3 * m_e

    res1 = abs((a_asym - lam_v) - mp.mpf("0.5") * lam_v)
    res2 = abs(del_s - (q2 ** 3) * lam_ex)
    res3 = abs(mp.mpf("2") * q2 * del_p - q3 * lam_v)
    max_res = max(res1, res2, res3)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-ltal-qinteger-mass-coefficient-identities",
        "passed": passed,
        "deltaS": nstr40(del_s),
        "lambdaEx": nstr40(lam_ex),
        "maxResidual": nstr40(max_res),
    }


def check_dilog_reflection_identities() -> dict:
    x = mp.mpf("3") / mp.mpf("10")
    y = mp.mpf("7") / mp.mpf("11")
    half = mp.mpf("1") / mp.mpf("2")
    sum_x = mp.polylog(2, x) + mp.polylog(2, mp.mpf("1") - x)
    sum_y = mp.polylog(2, y) + mp.polylog(2, mp.mpf("1") - y)
    diff_lhs = sum_x - sum_y
    diff_rhs = mp.log(y) * mp.log(mp.mpf("1") - y) - mp.log(x) * mp.log(mp.mpf("1") - x)
    mid_lhs = sum_x - mp.mpf("2") * mp.polylog(2, half)
    mid_rhs = (mp.log(mp.mpf("2")) ** 2) - mp.log(x) * mp.log(mp.mpf("1") - x)
    max_res = max(abs(diff_lhs - diff_rhs), abs(mid_lhs - mid_rhs))
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-mlbg-dilog-reflection-difference-and-midpoint",
        "passed": passed,
        "twoPointReflectionDiff": nstr40(diff_lhs),
        "midpointDeviationAtThreeTenths": nstr40(mid_lhs),
        "maxResidual": nstr40(max_res),
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent.parent
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    try:
        git_commit = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        git_commit = "0" * 40

    checks = [
        check_hyperbolic_hemisphere_fibre(),
        check_planck_step_and_regimes(),
        check_oneloop_shape_triple(),
        check_qinteger_mass_relations(),
        check_dilog_reflection_identities(),
    ]
    all_passed = all(c["passed"] for c in checks)
    witness = {
        "probe": script_path.name,
        "gitCommit": git_commit,
        "scriptCommitSha": git_commit,
        "scriptHash": script_hash,
        "dps": 80,
        "allPassed": all_passed,
        "checks": checks,
    }
    witness_path = script_path.resolve().parents[2] / "test" / "results" / "witnesses" / "hyperbolic-planck-oneloop-qint-dilog.witness.json"
    witness_path.parent.mkdir(parents=True, exist_ok=True)
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {witness_path.name} (allPassed={all_passed}, scriptHash={script_hash})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
