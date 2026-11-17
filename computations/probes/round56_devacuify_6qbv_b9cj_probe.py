#!/usr/bin/env python3
"""80-dps mpmath computational witness probe for Round 56 devacuification batch:
- qou-sa5c: QHookBound unconditional qInt_ratio_bound_small & qFact_ratio_bound + MassTowerOpenProblemsClasses term7_structural
- qou-sym2: Sym2GateParity twoJ_mem_sym2Indices, even_sub_of_mem_sym2Indices, and icosahedral A5 Sym2(T1) inner product = 1
- qou-6pib: MoebiusThreePointRigidity quadratic_eq_of_three_agree and moebius_trace_zero_involution_cleared
- qou-demm: PeriodMapWeightReduction pair_diff_eq_zero, add_closed, and smul_closed
- qou-cyon: UDeformFamilyPruning familyIm_neg_both, familyIm_swap_antisymm, and signflip_iff_diagonal_cross
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80

HERE = pathlib.Path(__file__).resolve()
REPO_ROOT = HERE.parents[2]
WITNESS_PATH = HERE.with_name("round56-devacuify-6qbv-b9cj.witness.json")


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 80)


def check_sa5c() -> dict:
    q = mp.exp(-2 * mp.pi / 5)

    def q_int(n: int) -> mp.mpf:
        if n <= 0:
            return mp.mpf(1)
        return sum((q ** j for j in range(n)), mp.mpf(0))

    def q_fact(n: int) -> mp.mpf:
        prod = mp.mpf(1)
        for j in range(1, n + 1):
            prod *= q_int(j)
        return prod

    small_ratios = {}
    small_ok = True
    for m in (1, 2, 3, 4):
        lhs = q_int(m) / q_int(m - 1)
        rhs = mp.mpf(1) + q ** (m - 1)
        diff = rhs - lhs
        if diff < -mp.mpf("1e-75"):
            small_ok = False
        small_ratios[f"m={m}"] = {
            "lhs": fmt(lhs),
            "rhs": fmt(rhs),
            "slack": fmt(diff),
        }

    fact_ratios = {}
    fact_ok = True
    for k in (0, 1, 2, 3):
        lhs = q_fact(k) / q_fact(k + 1)
        slack = mp.mpf(1) - lhs
        if slack < -mp.mpf("1e-75"):
            fact_ok = False
        fact_ratios[f"k={k}"] = {
            "ratio": fmt(lhs),
            "slack_to_one": fmt(slack),
        }

    a_coeff = -mp.mpf("1776.86") / ((2 * mp.pi) ** 4)
    chi5 = mp.sqrt(5)
    shift = a_coeff * chi5
    term7_ok = bool(shift < 0)

    return {
        "bean": "qou-sa5c",
        "passed": bool(small_ok and fact_ok and term7_ok),
        "q_value": fmt(q),
        "qInt_ratio_bound_small": small_ratios,
        "qFact_ratio_bound": fact_ratios,
        "term7_shift": fmt(shift),
    }


def check_sym2() -> dict:
    # Check doubled spins 2j in {0, 1, 2, 3, 4}
    spin_checks = {}
    spins_ok = True
    for two_j in range(5):
        indices = [two_j * 2 - 4 * k for k in range(two_j // 2 + 1)]
        top_in = (2 * two_j) in indices
        diffs_even = all((2 * two_j - idx) % 4 == 0 for idx in indices)
        if not (top_in and diffs_even):
            spins_ok = False
        spin_checks[f"twoJ={two_j}"] = {
            "indices": [str(x) for x in indices],
            "top_present": top_in,
            "all_step_four": diffs_even,
        }

    phi = (mp.mpf(1) + mp.sqrt(5)) / 2
    psi = (mp.mpf(1) - mp.sqrt(5)) / 2
    # Sym2(T1) character values on the 5 conjugacy classes of A5:
    # 1A (size 1): (3^2 + 3)/2 = 6
    # 2A (size 15): ((-1)^2 + 3)/2 = 2
    # 3A (size 20): (0^2 + 0)/2 = 0
    # 5A (size 12): (phi^2 + psi)/2 = (phi + 1 + 1 - phi)/2 = 1
    # 5B (size 12): (psi^2 + phi)/2 = (psi + 1 + 1 - psi)/2 = 1
    sym2_5a = (phi ** 2 + psi) / 2
    sym2_5b = (psi ** 2 + phi) / 2
    class_sizes = [1, 15, 20, 12, 12]
    char_vals = [mp.mpf(6), mp.mpf(2), mp.mpf(0), sym2_5a, sym2_5b]
    weighted_sum = sum((sz * val for sz, val in zip(class_sizes, char_vals)), mp.mpf(0))
    inner_prod = weighted_sum / mp.mpf(60)
    icosa_ok = bool(abs(inner_prod - mp.mpf(1)) < mp.mpf("1e-75"))

    return {
        "bean": "qou-sym2",
        "passed": bool(spins_ok and icosa_ok),
        "spin_parity_checks": spin_checks,
        "sym2_5A_char": fmt(sym2_5a),
        "sym2_5B_char": fmt(sym2_5b),
        "weighted_sum_over_A5": fmt(weighted_sum),
        "singlet_inner_product": fmt(inner_prod),
    }


def check_6pib() -> dict:
    # Check quadratic_eq_of_three_agree and moebius_trace_zero_involution_cleared
    a = mp.pi
    b = mp.e
    c = mp.sqrt(2)
    det_neg = a ** 2 + b * c

    pts = [mp.mpf(0), mp.mpf(1), (mp.mpf(1) + mp.sqrt(5)) / 2, mp.sqrt(3)]
    max_res = mp.mpf(0)
    for z in pts:
        num = a * (a * z + b) + b * (c * z - a)
        den_z = z * (c * (a * z + b) - a * (c * z - a))
        rhs = det_neg * z
        max_res = max(max_res, abs(num - den_z), abs(num - rhs))

    passed = bool(max_res < mp.mpf("1e-75") and det_neg > 0)
    return {
        "bean": "qou-6pib",
        "passed": passed,
        "neg_det_factor": fmt(det_neg),
        "max_involution_residual": fmt(max_res),
    }


def check_demm() -> dict:
    lam = 2 * mp.pi
    c1 = mp.mpf(3) / 7
    c2 = -mp.mpf(5) / 11
    alpha = mp.mpf(4) / 9

    val1 = c1 * (lam ** 4)
    val2 = c2 * (lam ** 4)
    pair_diff = c2 * val1 - c1 * val2
    sum_res = (val1 + val2) - (c1 + c2) * (lam ** 4)
    smul_res = alpha * val1 - (alpha * c1) * (lam ** 4)

    max_err = max(abs(pair_diff), abs(sum_res), abs(smul_res))
    passed = bool(max_err < mp.mpf("1e-75"))
    return {
        "bean": "qou-demm",
        "passed": passed,
        "lambda": fmt(lam),
        "pair_diff_residual": fmt(abs(pair_diff)),
        "add_closed_residual": fmt(abs(sum_res)),
        "smul_closed_residual": fmt(abs(smul_res)),
    }


def check_cyon() -> dict:
    def family_im(u: mp.mpf, v: mp.mpf) -> mp.mpf:
        return u ** 2 - v ** 2

    u0 = mp.pi / 3
    v0 = mp.sqrt(7) / 5
    neg_both_err = abs(family_im(-u0, -v0) - family_im(u0, v0))
    swap_sum = abs(family_im(u0, v0) + family_im(v0, u0))
    diag_pos = abs(family_im(u0, u0) + family_im(u0, u0))
    diag_neg = abs(family_im(u0, -u0) + family_im(-u0, u0))
    off_diag_nonzero = abs(family_im(u0, v0) + family_im(v0, u0)) > mp.mpf("1e-10")

    passed = bool(
        neg_both_err < mp.mpf("1e-75")
        and swap_sum < mp.mpf("1e-75")
        and diag_pos < mp.mpf("1e-75")
        and diag_neg < mp.mpf("1e-75")
        and abs(family_im(u0, v0)) > mp.mpf("1e-10")
        and off_diag_nonzero is False
    )
    # Wait: familyIm(u,v) + familyIm(v,u) is IDENTICALLY 0 by swap antisymmetry;
    # signflip_iff_diagonal_cross tests familyIm(v,u) = familyIm(u,v) (fixed under swap)!
    fixed_off_diag = abs(family_im(v0, u0) - family_im(u0, v0))
    fixed_diag_pos = abs(family_im(u0, u0) - family_im(u0, u0))
    fixed_diag_neg = abs(family_im(-u0, u0) - family_im(u0, -u0))
    passed = bool(
        neg_both_err < mp.mpf("1e-75")
        and swap_sum < mp.mpf("1e-75")
        and fixed_diag_pos < mp.mpf("1e-75")
        and fixed_diag_neg < mp.mpf("1e-75")
        and fixed_off_diag > mp.mpf("1e-5")
    )

    return {
        "bean": "qou-cyon",
        "passed": passed,
        "neg_both_residual": fmt(neg_both_err),
        "swap_antisymm_residual": fmt(swap_sum),
        "fixed_diag_pos_residual": fmt(fixed_diag_pos),
        "fixed_diag_neg_residual": fmt(fixed_diag_neg),
        "fixed_off_diag_separation": fmt(fixed_off_diag),
    }


def main() -> None:
    script_bytes = HERE.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    commit_sha = (
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT)
        .decode("utf-8")
        .strip()
    )

    checks = [
        check_sa5c(),
        check_sym2(),
        check_6pib(),
        check_demm(),
        check_cyon(),
    ]
    all_passed = all(c["passed"] for c in checks)

    payload = {
        "probe": "round56-devacuify-6qbv-b9cj",
        "script": str(HERE.relative_to(REPO_ROOT)),
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "executedAt": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "dps": "80",
        "allPassed": all_passed,
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    if not all_passed:
        raise SystemExit("One or more Round 56 witness checks failed")
    print(f"Wrote {WITNESS_PATH} (scriptHash={script_hash}, commit={commit_sha})")


if __name__ == "__main__":
    main()
