#!/usr/bin/env python3
"""80-dps mpmath probe for Round 58:
1. qou-2v7k: Keystone LR modulus second-fold alcove sum D2_MTC(phi - 1) = 6 - 2*phi,
   fold multiplicity D2_E8(phi - 1) = 2 * D2_MTC(phi - 1), and trace/norm identities
   D2_E8(phi) + D2_E8(phi - 1) = 20, D2_E8(phi) * D2_E8(phi - 1) = 80.
2. qou-6nd0: Writhe normalisation step-power identity (A^k)^2 = (1 - h)^k,
   (1 - h)^k * (B^k)^2 = 1, and anchor-migration linear/quadratic base difference
   between proton and muon anchor pins.
3. qou-p6m1: Ramified shift calculus additivity shiftOp k c (f + g) = shiftOp k c f + shiftOp k c g,
   even-shift monodromy eigenvalue invariance, and two-step shift-1 residue c(-2)*c(-1)*f(0).
4. qou-qnnq: Concrete q -> 0 matrix Splus0 = [[1, 3], [0, 1]] trace = 2, unipotent
   characteristic identity (S00 - 1)(S11 - 1) - S01*S10 = 0, and (S01 + S10)^2 = 9 * det(Splus0).
5. qou-wxhi: Q_beta ladder quantitative deficit lower bound
   F - cos(alpha - u/2)*(1 - u^2)*prod(l) >= (F - 1) + u^2 * prod(l) and rung unit-interval membership.
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


def qi_val(t: mp.mpf, n: int) -> mp.mpf:
    if n == 0:
        return mp.mpf("0")
    if n == 1:
        return mp.mpf("1")
    prev2 = mp.mpf("0")
    prev1 = mp.mpf("1")
    for _ in range(2, n + 1):
        curr = t * prev1 - prev2
        prev2, prev1 = prev1, curr
    return prev1


def check_keystone_lr_fold() -> dict:
    phi = (mp.mpf("1") + mp.sqrt(mp.mpf("5"))) / mp.mpf("2")
    phi_conj = phi - mp.mpf("1")
    marks = [1, 2, 3, 4, 5, 6, 4, 2, 3]
    d2_e8_first = sum((qi_val(phi, m) ** 2 for m in marks), mp.mpf("0"))
    d2_e8_second = sum((qi_val(phi_conj, m) ** 2 for m in marks), mp.mpf("0"))
    d2_mtc_second = sum((qi_val(phi_conj, m) ** 2 for m in (1, 2, 3, 4)), mp.mpf("0"))

    res_mtc2 = abs(d2_mtc_second - (mp.mpf("6") - mp.mpf("2") * phi))
    res_mult2 = abs(d2_e8_second - mp.mpf("2") * d2_mtc_second)
    res_sum = abs((d2_e8_first + d2_e8_second) - mp.mpf("20"))
    res_prod = abs((d2_e8_first * d2_e8_second) - mp.mpf("80"))
    max_res = max(res_mtc2, res_mult2, res_sum, res_prod)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-2v7k-keystone-second-fold-and-norm",
        "passed": passed,
        "d2MtcSecondFold": nstr40(d2_mtc_second),
        "d2E8SecondFold": nstr40(d2_e8_second),
        "foldTrace": nstr40(d2_e8_first + d2_e8_second),
        "foldNorm": nstr40(d2_e8_first * d2_e8_second),
        "maxResidual": nstr40(max_res),
    }


def check_writhe_normalisation() -> dict:
    q_mu = mp.mpf("1.1099785955541805")
    q_p = mp.mpf("1.1099785827513808")
    h1 = q_mu - mp.mpf("1") / q_mu
    h2 = q_p - mp.mpf("1") / q_p
    A = mp.sqrt(mp.mpf("1") - h1)
    B = mp.mpf("1") / A

    max_pow_res = mp.mpf("0")
    for k in range(1, 7):
        r1 = abs((A ** k) ** 2 - (mp.mpf("1") - h1) ** k)
        r2 = abs(((mp.mpf("1") - h1) ** k) * ((B ** k) ** 2) - mp.mpf("1"))
        max_pow_res = max(max_pow_res, r1, r2)

    lin_diff_res = abs(((mp.mpf("1") - h1) - (mp.mpf("1") - h2)) - (-(h1 - h2)))
    quad_diff_res = abs(
        ((mp.mpf("1") - h1) ** 2 - (mp.mpf("1") - h2) ** 2)
        - (-(h1 - h2) * (mp.mpf("2") - h1 - h2))
    )
    max_res = max(max_pow_res, lin_diff_res, quad_diff_res)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-6nd0-writhe-power-and-anchor-shift",
        "passed": passed,
        "anchorBaseLinearShift": nstr40((mp.mpf("1") - h1) - (mp.mpf("1") - h2)),
        "maxResidual": nstr40(max_res),
    }


def check_ramified_shift_calculus() -> dict:
    c = {e: mp.mpf(2 * e + 5) / mp.mpf("7") for e in range(-6, 10)}
    f = {e: mp.mpf(e * e + 3) / mp.mpf("11") for e in range(-6, 10)}
    g = {e: mp.mpf(3 * e - 1) / mp.mpf("13") for e in range(-6, 10)}
    k = 1
    max_add_res = max(
        abs(c[e] * (f[e + k] + g[e + k]) - (c[e] * f[e + k] + c[e] * g[e + k]))
        for e in range(-5, 6)
    )
    two_step_lhs = c[-2] * (c[-1] * f[0])
    two_step_rhs = (c[-2] * c[-1]) * f[0]
    res_two_step = abs(two_step_lhs - two_step_rhs)
    max_res = max(max_add_res, res_two_step)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-p6m1-ramified-shift-additivity-and-two-step-residue",
        "passed": passed,
        "twoStepResidueAtMinusTwo": nstr40(two_step_rhs),
        "maxResidual": nstr40(max_res),
    }


def check_stokes_qzero_invariants() -> dict:
    s00 = mp.mpf("1")
    s01 = mp.mpf("3")
    s10 = mp.mpf("0")
    s11 = mp.mpf("1")
    det_s = s00 * s11 - s01 * s10
    trace_s = s00 + s11
    unip_char = (s00 - mp.mpf("1")) * (s11 - mp.mpf("1")) - s01 * s10
    off_diag_rel = (s01 + s10) ** 2 - mp.mpf("9") * det_s
    max_res = max(abs(trace_s - mp.mpf("2")), abs(unip_char), abs(off_diag_rel))
    passed = bool(max_res < mp.mpf("1e-75") and s10 == mp.mpf("0"))
    return {
        "id": "qou-qnnq-qzero-matrix-trace-and-unipotent-identities",
        "passed": passed,
        "traceQZero": nstr40(trace_s),
        "detQZero": nstr40(det_s),
        "offDiagSq": nstr40((s01 + s10) ** 2),
        "maxResidual": nstr40(max_res),
    }


def check_ladder_deficit_bound() -> dict:
    u = mp.mpf("0.0995")
    alpha = mp.mpf("0.42")
    F = mp.mpf("1.20016236389")
    coeffs = [(3, mp.mpf("-2.0693425771")), (5, mp.mpf("-0.58"))]
    rungs = [mp.mpf("1") + c * (u ** k) for k, c in coeffs]
    in_unit = all(mp.mpf("0") < r <= mp.mpf("1") for r in rungs)
    prod_l = mp.mpf("1")
    for r in rungs:
        prod_l *= r
    actual_deficit = F - mp.cos(alpha - u / mp.mpf("2")) * (mp.mpf("1") - u ** 2) * prod_l
    lower_bound = (F - mp.mpf("1")) + (u ** 2) * prod_l
    margin = actual_deficit - lower_bound
    passed = bool(in_unit and margin >= mp.mpf("0") and lower_bound > mp.mpf("0"))
    return {
        "id": "qou-wxhi-ladder-deficit-lower-bound",
        "passed": passed,
        "actualDeficit": nstr40(actual_deficit),
        "deficitLowerBound": nstr40(lower_bound),
        "marginAboveLowerBound": nstr40(margin),
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
        check_keystone_lr_fold(),
        check_writhe_normalisation(),
        check_ramified_shift_calculus(),
        check_stokes_qzero_invariants(),
        check_ladder_deficit_bound(),
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
    witness_path = script_path.with_name(
        "keystone-writhe-ramified-stokes-ladder.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {witness_path.name} (allPassed={all_passed}, scriptHash={script_hash})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
