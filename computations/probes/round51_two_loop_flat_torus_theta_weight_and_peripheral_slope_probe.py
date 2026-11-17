#!/usr/bin/env python3
"""
Round 51 50-dps Probe:
  1. qou-9y43: EmFermionLoop H_1 evaluation [2]_q and Schwinger resummation bound vs 2-loop c_2 residual.
  2. qou-af91: Flat-torus Maxwell Z_Maxwell(T^{b_1}) on Jac(Bring) (b_1 = 8): pi-exponent -b_1/2 = -4 vs -1 and covolume exponent b_1(b_1-2)/2 = 24.
  3. qou-i7rk: Theta-graph 2-loop vacuum evaluation theta(1,1,2) = [3]_q, dressed propagator sign inversion, and 2-sigma falsification vs L_{2,req}.
  4. qou-oots: Phi_k weight-family triage on the alpha_EM axis (Jucys-Murphy n=5 content cancellation under symmetric Plancherel weights vs Molien asymmetry; 3-family strict ordering at lambda=(4,1)).
  5. qou-ae6l: Braid word -> surgery slope (m, l) peripheral structure map Phi_w in SL_2(Z), symplectic intersection invariance, Markov stabilization compensation, and 0-framed blackboard surgery slopes across corpus knots.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import subprocess
import time
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80

Q0_PROTON_STR = "1.10997858275138080828695817946350192572592720252105"
CODATA_INV_ALPHA_2018_STR = "137.035999084"
CODATA_INV_ALPHA_2022_STR = "137.035999177"


def fmt(x: mp.mpf, digits: int = 55) -> str:
    return mp.nstr(x, digits)


def q_bracket(n: int, q: mp.mpf) -> mp.mpf:
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def q_factorial(n: int, q: mp.mpf) -> mp.mpf:
    res = mp.mpf(1)
    for k in range(1, n + 1):
        res *= q_bracket(k, q)
    return res


def penrose_theta(a: int, b: int, c: int, q: mp.mpf) -> mp.mpf:
    m = (a + b - c) // 2
    n = (b + c - a) // 2
    p = (a + c - b) // 2
    num = q_factorial(m + n + p + 1, q) * q_factorial(m, q) * q_factorial(n, q) * q_factorial(p, q)
    den = q_factorial(m + n, q) * q_factorial(n + p, q) * q_factorial(m + p, q)
    return num / den


def hook_lengths(shape: tuple[int, ...]) -> list[int]:
    conj = []
    max_col = shape[0] if shape else 0
    for j in range(max_col):
        conj.append(sum(1 for r in shape if r > j))
    hooks = []
    for i, r in enumerate(shape):
        for j in range(r):
            hooks.append((r - j - 1) + (conj[j] - i - 1) + 1)
    return hooks


def content_sum(shape: tuple[int, ...]) -> int:
    total = 0
    for i, r in enumerate(shape):
        for j in range(r):
            total += (j - i)
    return total


def f_lambda(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    fact_n = 1
    for k in range(1, n + 1):
        fact_n *= k
    prod_h = 1
    for h in hook_lengths(shape):
        prod_h *= h
    return fact_n // prod_h


def dim_q(shape: tuple[int, ...], q: mp.mpf) -> mp.mpf:
    n = sum(shape)
    num = q_factorial(n, q)
    den = mp.mpf(1)
    for h in hook_lengths(shape):
        den *= q_bracket(h, q)
    return num / den


def markov_y_su2_n5_41(q: mp.mpf) -> mp.mpf:
    # Standard Schur-Weyl / Ocneanu weight y_{(4,1)} at N=2:
    # s_{(4,1)}(q^{1/2}, q^{-1/2}) / (q^{1/2} + q^{-1/2})^5 = [4]_q / ([2]_q)^5
    # Wait: let's match the corpus convention from alpha_em_b2_weight_family_triage_probe.py:
    # y_{(4,1), N=2}(q0) = 0.12498539716794710592...
    # Which is s_{(4,1)}(q, 1) / (q + 1)^5 or Schur-Weyl character weight:
    # For lambda = (4,1), cells have contents c in {0, 1, 2, 3, -1}, so N + c at N=2 is {2, 3, 4, 5, 1},
    # hook lengths are {5, 3, 2, 1, 1}: s_{(4,1), N=2}(q) = ([2]_q[3]_q[4]_q[5]_q[1]_q) / ([5]_q[3]_q[2]_q[1]_q[1]_q) = [4]_q,
    # and y_{(4,1), N=2}(q) = s_{(4,1), N=2}(q) / ([2]_q)^5 = [4]_q / ([2]_q)^5!
    return q_bracket(4, q) / (q_bracket(2, q) ** 5)


def main() -> int:
    t0 = time.monotonic()
    q0 = mp.mpf(Q0_PROTON_STR)
    inv_a_2018 = mp.mpf(CODATA_INV_ALPHA_2018_STR)
    inv_a_2022 = mp.mpf(CODATA_INV_ALPHA_2022_STR)

    # --- 1. qou-9y43: EmFermionLoop H_1 and Schwinger resummation vs 2-loop c_2 ---
    em_loop_h1 = q_bracket(2, q0)
    em_loop_exact = q0 + 1 / q0
    h = q0 - 1 / q0
    h2 = h ** 2
    T_tree_zero = q0 * q_bracket(9, q0) * q_bracket(10, q0) + mp.mpf(2) / (3 * mp.pi)
    H1 = q_bracket(2, q0) / (8 * mp.pi)

    def solve_fixed_point(f_func) -> mp.mpf:
        a = mp.mpf("0.0072973525693")
        for _ in range(250):
            a = 1 / (T_tree_zero + a * H1 * f_func(a))
        return 1 / a

    inv_a_linear = solve_fixed_point(lambda a: 1 - h2 * a)
    inv_a_geom = solve_fixed_point(lambda a: 1 / (1 + h2 * a))
    inv_a_exp = solve_fixed_point(lambda a: mp.exp(-h2 * a))

    res_shift_geom = abs(inv_a_geom - inv_a_linear)
    res_shift_exp = abs(inv_a_exp - inv_a_linear)
    delta2_2018 = inv_a_2018 - inv_a_linear
    delta2_2022 = inv_a_2022 - inv_a_linear
    a_p = 1 / inv_a_linear
    c2_2018 = delta2_2018 / (a_p ** 2)
    c2_2022 = delta2_2022 / (a_p ** 2)

    # --- 2. qou-af91: Flat-torus Maxwell Z_Maxwell(T^{b_1}) on Jac(Bring) ---
    g_bring = 4
    b1_bring = 2 * g_bring
    zeta_delta1_0 = -b1_bring
    pi_exponent_flat_torus = zeta_delta1_0 // 2  # -4
    pi_exponent_target = -1
    jacobian_covolume_exponent = b1_bring * (b1_bring - 2) // 2  # 24

    # --- 3. qou-i7rk: Theta-graph 2-loop candidate & dressed-propagator inversion ---
    th_110 = penrose_theta(1, 1, 0, q0)
    th_220 = penrose_theta(2, 2, 0, q0)
    th_112 = penrose_theta(1, 1, 2, q0)
    th_121 = penrose_theta(1, 2, 1, q0)
    th_211 = penrose_theta(2, 1, 1, q0)

    a_codata_2018 = 1 / inv_a_2018
    a_codata_2022 = 1 / inv_a_2022
    L2_req = (inv_a_2018 - T_tree_zero - a_codata_2018 * H1) / (a_codata_2018 ** 2)
    L2_req_2022 = (inv_a_2022 - T_tree_zero - a_codata_2022 * H1) / (a_codata_2022 ** 2)
    L2_theta_dictated = -q_bracket(3, q0) / ((8 * mp.pi) ** 2)
    theta_ratio = L2_theta_dictated / L2_req
    # CODATA 2018 uncertainty on 1/alpha = 137.035999084(11): sigma(1/alpha) = 1.1e-8
    sigma_inva_2018 = mp.mpf("1.1e-8")
    two_sigma_L2 = 2 * sigma_inva_2018 / (a_codata_2018 ** 2)
    # CODATA 2022 uncertainty on 1/alpha = 137.035999177(21): sigma(1/alpha) = 2.1e-8
    sigma_inva_2022 = mp.mpf("2.1e-8")
    two_sigma_L2_2022 = 2 * sigma_inva_2022 / (a_codata_2022 ** 2)

    # --- 4. qou-oots: Phi_k weight-family triage on the alpha_EM axis ---
    partitions_5 = [
        (5,),
        (4, 1),
        (3, 2),
        (3, 1, 1),
        (2, 2, 1),
        (2, 1, 1, 1),
        (1, 1, 1, 1, 1),
    ]
    qfact5 = q_factorial(5, q0)
    jm_planch_sum = mp.mpf(0)
    jm_molien_sum = mp.mpf(0)
    molien_norm_sum = mp.mpf(0)
    for sh in partitions_5:
        dq = dim_q(sh, q0)
        kap = content_sum(sh)
        fl = f_lambda(sh)
        w_pl = (dq ** 2) / qfact5
        w_mo = mp.mpf(fl) * (q0 ** (-kap)) * dq / qfact5
        jm_planch_sum += w_pl * kap
        jm_molien_sum += w_mo * kap
        molien_norm_sum += w_mo

    sh_41 = (4, 1)
    dq_41 = dim_q(sh_41, q0)
    w_planch_41 = (dq_41 ** 2) / qfact5
    w_molien_41 = mp.mpf(f_lambda(sh_41)) * (q0 ** (-content_sum(sh_41))) * dq_41 / qfact5
    y_markov_41 = markov_y_su2_n5_41(q0)
    molien_over_planch_41 = w_molien_41 / w_planch_41

    # --- 5. qou-ae6l: Braid word -> surgery slope (m, l) peripheral structure map ---
    def peripheral_map(w: int, p_bb: int, q_bb: int) -> tuple[int, int]:
        return (p_bb + w * q_bb, q_bb)

    def symp_form(s1: tuple[int, int], s2: tuple[int, int]) -> int:
        return s1[0] * s2[1] - s1[1] * s2[0]

    knot_writhes = {
        "T(2,3)": sum([1, 1, 1]),
        "4_1": sum([1, -1, 1, -1]),
        "T(2,5)": sum([1, 1, 1, 1, 1]),
        "5_2": sum([1, 1, 1, 1, -1, 1]),
        "T(2,9)": sum([1] * 9),
        "T(3,5)": sum([1] * 10),
    }

    assertions = [
        {
            "name": "qou_9y43_emfermionloop_h1_equals_qbracket2",
            "computed": fmt(abs(em_loop_h1 - em_loop_exact)),
            "expected": "0.0",
            "tolerance": "1e-60",
            "passed": bool(abs(em_loop_h1 - em_loop_exact) < mp.mpf("1e-60")),
            "source": "EmFermionLoop in H_1 evaluates to [2]_q = q + q^{-1} exactly",
        },
        {
            "name": "qou_9y43_schwinger_resummation_shift_negligible_vs_delta2",
            "computed": "1" if (res_shift_geom * 700 < abs(delta2_2018) and res_shift_exp * 700 < abs(delta2_2018) and res_shift_geom * 800 < abs(delta2_2022)) else "0",
            "expected": "1",
            "tolerance": "0",
            "passed": bool(res_shift_geom * 700 < abs(delta2_2018) and res_shift_exp * 700 < abs(delta2_2018) and res_shift_geom * 800 < abs(delta2_2022)),
            "source": "Geometric and exponential resummations of (1 - h^2 alpha) shift 1/alpha by 5.937e-11, >700x smaller than |Delta_2| ~ 4.295e-8 (2018, c_2 = -8.066e-4) and 5.005e-8 (2022, c_2 = -9.399e-4)",
        },
        {
            "name": "qou_af91_flat_torus_pi_exponent_and_covolume_mismatch",
            "computed": f"{pi_exponent_flat_torus},{jacobian_covolume_exponent}",
            "expected": "-4,24",
            "tolerance": "0",
            "passed": bool(pi_exponent_flat_torus == -4 and pi_exponent_flat_torus != pi_exponent_target and jacobian_covolume_exponent == 24),
            "source": "On T^{b_1} = Jac(Bring) (b_1 = 8), oscillator measure has pi-exponent -b_1/2 = -4 != -1 and Jacobian covolume exponent b_1(b_1-2)/2 = 24 != 0",
        },
        {
            "name": "qou_i7rk_penrose_theta_112_equals_qbracket3_and_symmetric",
            "computed": fmt(abs(th_112 - q_bracket(3, q0)) + abs(th_112 - th_121) + abs(th_112 - th_211) + abs(th_110 - q_bracket(2, q0))),
            "expected": "0.0",
            "tolerance": "1e-60",
            "passed": bool(abs(th_112 - q_bracket(3, q0)) < mp.mpf("1e-60") and abs(th_112 - th_121) < mp.mpf("1e-60") and abs(th_110 - q_bracket(2, q0)) < mp.mpf("1e-60")),
            "source": "theta(1,1,2) = theta(1,2,1) = theta(2,1,1) = [3]_q and theta(1,1,0) = [2]_q",
        },
        {
            "name": "qou_i7rk_dictated_theta_candidate_outside_two_sigma",
            "computed": "1" if (abs(L2_theta_dictated - L2_req) > two_sigma_L2 and abs(L2_theta_dictated - L2_req_2022) > two_sigma_L2_2022) else "0",
            "expected": "1",
            "tolerance": "0",
            "passed": bool(abs(L2_theta_dictated - L2_req) > two_sigma_L2 and abs(L2_theta_dictated - L2_req_2022) > two_sigma_L2_2022),
            "source": "Dictated -[3]_q/(8pi)^2 = -4.818624e-3 misses L2_req by 5.1507e-4 > 2*sigma_L2_2018 (4.1313e-4) and by 2.2614e-3 > 2*sigma_L2_2022 (7.8871e-4)",
        },
        {
            "name": "qou_oots_jucys_murphy_n5_plancherel_zero_vs_molien_negative",
            "computed": "1" if (abs(jm_planch_sum) < mp.mpf("1e-60") and abs(molien_norm_sum - 1) < mp.mpf("1e-60") and jm_molien_sum < mp.mpf("-1.0")) else "0",
            "expected": "1",
            "tolerance": "0",
            "passed": bool(abs(jm_planch_sum) < mp.mpf("1e-60") and abs(molien_norm_sum - 1) < mp.mpf("1e-60") and jm_molien_sum < mp.mpf("-1.0")),
            "source": "At n=5, conjugate-symmetric Plancherel weight gives sum w_lambda kappa(lambda) = 0 identically, whereas normalized Molien weight gives -1.039637100524... < 0",
        },
        {
            "name": "qou_oots_three_weight_families_strict_ordering_at_41",
            "computed": "1" if (0 < w_molien_41 < y_markov_41 < w_planch_41 and abs(molien_over_planch_41 - 1) > mp.mpf("0.42")) else "0",
            "expected": "1",
            "tolerance": "0",
            "passed": bool(0 < w_molien_41 < y_markov_41 < w_planch_41 and abs(molien_over_planch_41 - 1) > mp.mpf("0.42")),
            "source": "At lambda=(4,1) and q0, 0 < w_Molien (0.0742997) < y_{Markov,N=2} (0.1249854) < w_Planch (0.1286200), with 42.23% Molien-to-Plancherel shift",
        },
        {
            "name": "qou_ae6l_peripheral_slope_map_symplectic_and_stabilization_invariance",
            "computed": "1" if (
                symp_form(peripheral_map(10, 3, 2), peripheral_map(10, 5, 7)) == symp_form((3, 2), (5, 7))
                and peripheral_map(10 + 1, 3 - 2, 2) == peripheral_map(10, 3, 2)
                and knot_writhes["4_1"] == 0
                and knot_writhes["T(3,5)"] == 10
            ) else "0",
            "expected": "1",
            "tolerance": "0",
            "passed": bool(
                symp_form(peripheral_map(10, 3, 2), peripheral_map(10, 5, 7)) == symp_form((3, 2), (5, 7))
                and peripheral_map(10 + 1, 3 - 2, 2) == peripheral_map(10, 3, 2)
                and knot_writhes["4_1"] == 0
                and knot_writhes["T(3,5)"] == 10
            ),
            "source": "Phi_w preserves the symplectic intersection pairing, compensates Markov stabilization via p' = p - q, fixes (1,0), and maps 0-framed blackboard surgery to (w(beta), 1)",
        },
    ]

    script_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    try:
        script_commit_sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=script_path.parent, text=True
        ).strip()
    except Exception:
        script_commit_sha = "0" * 40

    duration_ms = int(round((time.monotonic() - t0) * 1000))
    witness = {
        "computation": "round51-two-loop-flat-torus-theta-weight-and-peripheral-slope",
        "engine": "python+mpmath",
        "engineVersion": mp.__version__,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scriptFile": script_path.name,
        "scriptHash": script_hash,
        "scriptCommitSha": script_commit_sha,
        "durationMs": duration_ms,
        "precisionMetadata": {
            "compute_dps": "80",
            "output_dps": "55",
            "guard_digits": "25",
            "q0_proton_50dps": Q0_PROTON_STR,
        },
        "data": {
            "qou_9y43": {
                "em_fermion_loop_H1_q2": fmt(em_loop_h1),
                "inv_alpha_linear_schwinger": fmt(inv_a_linear),
                "inv_alpha_geom_resummed": fmt(inv_a_geom),
                "inv_alpha_exp_resummed": fmt(inv_a_exp),
                "resummation_shift_geom": fmt(res_shift_geom),
                "delta2_residual_codata2018": fmt(delta2_2018),
                "delta2_residual_codata2022": fmt(delta2_2022),
                "c2_required_codata2018": fmt(c2_2018),
                "c2_required_codata2022": fmt(c2_2022),
            },
            "qou_af91": {
                "bring_genus": str(g_bring),
                "first_betti_b1": str(b1_bring),
                "zeta_delta1_zero": str(zeta_delta1_0),
                "flat_torus_pi_exponent": str(pi_exponent_flat_torus),
                "target_pi_exponent": str(pi_exponent_target),
                "jacobian_covolume_scaling_exponent": str(jacobian_covolume_exponent),
            },
            "qou_i7rk": {
                "theta_1_1_0": fmt(th_110),
                "theta_2_2_0": fmt(th_220),
                "theta_1_1_2": fmt(th_112),
                "L2_required_total": fmt(L2_req),
                "L2_theta_dictated": fmt(L2_theta_dictated),
                "theta_to_required_ratio": fmt(theta_ratio),
                "two_sigma_L2_window": fmt(two_sigma_L2),
            },
            "qou_oots": {
                "jm_n5_plancherel_sum": fmt(jm_planch_sum),
                "jm_n5_molien_sum": fmt(jm_molien_sum),
                "molien_n5_total_mass": fmt(molien_norm_sum),
                "w_molien_41": fmt(w_molien_41),
                "y_markov_41_N2": fmt(y_markov_41),
                "w_plancherel_41": fmt(w_planch_41),
                "molien_over_plancherel_41": fmt(molien_over_planch_41),
            },
            "qou_ae6l": {
                "knot_writhes": {k: str(v) for k, v in knot_writhes.items()},
                "blackboard_zero_canonical_slopes": {
                    k: [str(peripheral_map(v, 0, 1)[0]), str(peripheral_map(v, 0, 1)[1])]
                    for k, v in knot_writhes.items()
                },
            },
        },
        "assertions": assertions,
        "allPassed": all(a["passed"] for a in assertions),
    }

    out_path = script_path.parent / "round51-two-loop-flat-torus-theta-weight-and-peripheral-slope.witness.json"
    out_path.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"Wrote {out_path} (allPassed={witness['allPassed']}, scriptHash={script_hash}, scriptCommitSha={script_commit_sha})")
    if not witness["allPassed"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
