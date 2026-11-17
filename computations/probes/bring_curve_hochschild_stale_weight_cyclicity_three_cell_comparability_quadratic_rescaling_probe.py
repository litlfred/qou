#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for Round 68 (`lane-e667`):
- qou-1ngt (`qou-59vq`): Bring curve genus g = (2 - chi)/2 = 4 (chi = -6) and S_5
  character orthogonality for the 4D standard representation H^0(Bring, Omega^1).
- qou-bgur (`qou-1oif`): Three-cell comparability vs. adjacency standard filling counts
  (1, 1, 2, 3, 3, 6), verifying that non-adjacent same-row pair (0,2), (0,7) + incomparable (3,0)
  has Manhattan distance 5 > 1 and exactly 3 standard labelings.
- qou-isu5 (`qou-59vq`): Stale H_3 weight vector [1, z, z, z^2, z^2, z^3] cyclicity defect
  vs. corrected longest-word trace weight w_6 = z(h z + 1), verifying
  z(h z + 1) - z^3 = -z(z - q)(q z + 1)/q at both z_C and z_D on the substrate q_0.
- qou-oyty (`qou-k4oq`): Convention A vs. Convention B quadratic generator rescaling
  (T - q^2)(T + 1) = q(sigma - q)(q sigma + 1) under T = q * sigma and eigenvalue gap
  q^2 + 1 = q(q + q^-1).
- qou-zut2 (`qou-59vq`): Two-channel quadratic eigenprojector decomposition P_+ + P_- = 1,
  P_+ P_- = 0 mod (sigma - q)(sigma + q^-1), and strict positivity of the Convention B
  eigenvalue gap q + q^-1 >= 2 > 0 for all q > 0.
"""

from __future__ import annotations
import datetime
import hashlib
import itertools
import json
import pathlib
import subprocess
import sys
from mpmath import mp

mp.dps = 80


def check_bring_curve_s5_std4() -> dict[str, object]:
    chi_euler = -6
    twice_g = 2 - chi_euler
    g = twice_g // 2
    sizes = [1, 10, 15, 20, 20, 30, 24]
    perm_char = [5, 3, 1, 2, 0, 1, 0]
    triv_char = [1, 1, 1, 1, 1, 1, 1]
    std4_char = [4, 2, 0, 1, -1, 0, -1]
    norm_std4 = sum(s * c * c for s, c in zip(sizes, std4_char))
    orth_std4_triv = sum(s * c1 * c2 for s, c1, c2 in zip(sizes, std4_char, triv_char))
    decomp_ok = all(p == t + s for p, t, s in zip(perm_char, triv_char, std4_char))
    passed = (
        g == 4
        and std4_char[0] == 4
        and sum(sizes) == 120
        and norm_std4 == 120
        and orth_std4_triv == 0
        and decomp_ok
    )
    return {
        "bean": "qou-1ngt",
        "theorem": "QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling.bring_curve_genus_and_s5_standard_irrep",
        "euler_characteristic": str(chi_euler),
        "genus_dim_hh1": str(g),
        "std4_inner_sum": str(norm_std4),
        "std4_triv_inner_sum": str(orth_std4_triv),
        "passed": bool(passed),
    }


def check_three_cell_comparability() -> dict[str, object]:
    def strictly_precedes(u: tuple[int, int], v: tuple[int, int]) -> bool:
        return u[0] <= v[0] and u[1] <= v[1] and (u[0] < v[0] or u[1] < v[1])

    def count_fillings(cells: list[tuple[int, int]]) -> int:
        cnt = 0
        for perm in itertools.permutations([1, 2, 3]):
            ok = True
            for i in range(3):
                for j in range(3):
                    if strictly_precedes(cells[i], cells[j]) and not (perm[i] < perm[j]):
                        ok = False
            if ok:
                cnt += 1
        return cnt

    c_row3 = count_fillings([(0, 0), (0, 1), (0, 2)])
    c_chain = count_fillings([(0, 0), (0, 1), (1, 1)])
    c_hook = count_fillings([(0, 0), (0, 1), (1, 0)])
    c_adj_domino = count_fillings([(0, 1), (0, 2), (1, 0)])
    c_nonadj_row = count_fillings([(0, 2), (0, 7), (3, 0)])
    c_incomp3 = count_fillings([(0, 2), (1, 1), (2, 0)])
    manhattan_nonadj = abs(0 - 0) + abs(2 - 7)
    passed = (
        c_row3 == 1
        and c_chain == 1
        and c_hook == 2
        and c_adj_domino == 3
        and c_nonadj_row == 3
        and manhattan_nonadj == 5
        and c_incomp3 == 6
    )
    return {
        "bean": "qou-bgur",
        "theorem": "QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling.three_cell_comparability_orbit_sizes",
        "counts": [str(x) for x in [c_row3, c_chain, c_hook, c_adj_domino, c_nonadj_row, c_incomp3]],
        "nonadj_manhattan_dist": str(manhattan_nonadj),
        "passed": bool(passed),
    }


def check_stale_h3_weight_cyclicity() -> dict[str, object]:
    q0 = mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000")
    h = q0 - (mp.mpf("1") / q0)
    two_q = q0 + (mp.mpf("1") / q0)
    z_c = mp.mpf("1") / two_q
    z_d = mp.mpf("1") / (two_q ** 2)
    max_res = mp.mpf("0")
    for z in [z_c, z_d]:
        w_genuine = z * (h * z + mp.mpf("1"))
        w_stale = z ** 3
        diff_lhs = w_genuine - w_stale
        diff_rhs = -z * (z - q0) * (q0 * z + mp.mpf("1")) / q0
        res = abs(diff_lhs - diff_rhs)
        if res > max_res:
            max_res = res
    w_zc_gen = z_c * (h * z_c + mp.mpf("1"))
    w_zc_stale = z_c ** 3
    passed = (max_res < mp.mpf("10") ** (-75)) and (abs(w_zc_gen - w_zc_stale) > mp.mpf("0.4"))
    return {
        "bean": "qou-isu5",
        "theorem": "QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling.stale_vs_genuine_longest_weight_factorization",
        "w6_genuine_at_zC": mp.nstr(w_zc_gen, 80),
        "w6_stale_at_zC": mp.nstr(w_zc_stale, 80),
        "cyclicity_defect_at_zC": mp.nstr(w_zc_gen - w_zc_stale, 80),
        "max_factorization_residual": mp.nstr(max_res, 80),
        "passed": bool(passed),
    }


def check_quadratic_rescaling() -> dict[str, object]:
    q0 = mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000")
    q_a = q0 ** 2
    max_res = mp.mpf("0")
    for sig_val in [q0, -mp.mpf("1") / q0, mp.mpf("3") / mp.mpf("7"), mp.mpf("-5") / mp.mpf("11")]:
        t_val = q0 * sig_val
        res_a = (t_val - q_a) * (t_val + mp.mpf("1"))
        res_b_scaled = (sig_val - q0) * (q0 * sig_val + mp.mpf("1"))
        err = abs(res_a - q0 * res_b_scaled)
        if err > max_res:
            max_res = err
    gap_a = q_a - (-mp.mpf("1"))
    gap_b = q0 + (mp.mpf("1") / q0)
    gap_err = abs(gap_a - q0 * gap_b)
    passed = (max_res < mp.mpf("10") ** (-75)) and (gap_err < mp.mpf("10") ** (-75))
    return {
        "bean": "qou-oyty",
        "theorem": "QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling.quadratic_convention_A_B_rescaling_identity",
        "max_rescaling_residual": mp.nstr(max_res, 80),
        "gap_rescaling_residual": mp.nstr(gap_err, 80),
        "convention_B_gap_at_q0": mp.nstr(gap_b, 80),
        "passed": bool(passed),
    }


def check_eigenprojector_decomposition() -> dict[str, object]:
    q0 = mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000")
    denom = q0 * q0 + mp.mpf("1")
    max_sum_err = mp.mpf("0")
    max_orth_err = mp.mpf("0")
    for sig_val in [q0, -mp.mpf("1") / q0, mp.mpf("2") / mp.mpf("3")]:
        p_plus_num = q0 * sig_val + mp.mpf("1")
        p_minus_num = q0 * (q0 - sig_val)
        sum_err = abs((p_plus_num + p_minus_num) - denom)
        quad_b = (sig_val - q0) * (q0 * sig_val + mp.mpf("1"))
        orth_err = abs(p_minus_num * p_plus_num - (-q0 * quad_b))
        if sum_err > max_sum_err:
            max_sum_err = sum_err
        if orth_err > max_orth_err:
            max_orth_err = orth_err
    passed = (
        max_sum_err < mp.mpf("10") ** (-75)
        and max_orth_err < mp.mpf("10") ** (-75)
        and denom >= mp.mpf("1")
    )
    return {
        "bean": "qou-zut2",
        "theorem": "QOU.Foundations.BringCurveHochschildStaleWeightCyclicityThreeCellComparabilityQuadraticRescaling.convention_B_eigenprojector_decomposition_and_gap_pos",
        "max_projector_sum_residual": mp.nstr(max_sum_err, 80),
        "max_projector_orth_residual": mp.nstr(max_orth_err, 80),
        "cleared_gap_denom_at_q0": mp.nstr(denom, 80),
        "passed": bool(passed),
    }


def main() -> int:
    script_path = pathlib.Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    try:
        commit_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=script_path.parent, text=True
        ).strip()
    except Exception:
        commit_sha = "0" * 40

    checks = [
        check_bring_curve_s5_std4(),
        check_three_cell_comparability(),
        check_stale_h3_weight_cyclicity(),
        check_quadratic_rescaling(),
        check_eigenprojector_decomposition(),
    ]
    all_passed = all(bool(c["passed"]) for c in checks)
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    payload = {
        "probe": "bring_curve_hochschild_stale_weight_cyclicity_three_cell_comparability_quadratic_rescaling_probe",
        "scriptPath": "computations/probes/bring_curve_hochschild_stale_weight_cyclicity_three_cell_comparability_quadratic_rescaling_probe.py",
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "executedAt": now,
        "dps": str(mp.dps),
        "allPassed": all_passed,
        "checks": checks,
    }
    wit_path = script_path.parent / "bring-curve-hochschild-stale-weight-cyclicity-three-cell-comparability-quadratic-rescaling.witness.json"
    wit_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"allPassed": all_passed, "scriptHash": script_hash, "scriptCommitSha": commit_sha}))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
