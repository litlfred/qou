#!/usr/bin/env python3
"""80-dps mpmath probe for QOU.QBeta.NucleonOrderingAndBringAdjointTorsionBrick.

Covers beans:
  - qou-q6h7: three-representation nucleon ordering trace factorization
              `wSym * sPi + wStd * (z * aPi + bPi) + wAlt * aAlt`
  - qou-qd27: Bring curve Sigma_4 (genus 4) adjoint H^1 rank `(2 * g - 2) * d = 6 * d`
  - qou-qint: balanced q-integer bar-even symmetry `[k]_q = (q^k - q^{-k}) / (q - q^{-1})`
              and difference-of-squares doubling
  - qou-r91v: hook-length log-dimension reduction `ln f = ln k! - sum ln h_box`,
              covariance sign flip, and conjugate-odd mode cancellation
  - qou-tvok: Poissonized (`v_A = 8 / pi^2`) vs de-Poissonized (`V_A = 8 / (9 * pi^2)`)
              content-variance ninefold ratio `v_A - 9 * V_A = 0`

All numerical outputs are serialized as 80-dps strings or integer/boolean fields (zero raw float64).
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
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "nucleon-ordering-and-bring-adjoint-torsion-brick.witness.json"
)


def fmt_mp(val: mp.mpf) -> str:
    return mp.nstr(val, 80, min_fixed=0, max_fixed=0)


def git_commit_sha() -> str:
    out = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    )
    return out.strip()


def git_is_dirty() -> bool:
    out = subprocess.check_output(
        ["git", "status", "--porcelain", "--untracked-files=no"],
        cwd=REPO_ROOT,
        text=True,
    )
    for line in out.splitlines():
        if not line.endswith(WITNESS_PATH.name):
            return True
    return False


def script_sha256_prefix() -> str:
    digest = hashlib.sha256(SCRIPT_PATH.read_bytes()).hexdigest()
    return digest[:12]


def run_probe() -> dict:
    tol = mp.mpf("1e-75")

    # 1. Bean qou-q6h7: Nucleon ordering factorization
    w_sym = mp.mpf("0.1875")
    s_pi = mp.mpf("1.5")
    w_std = mp.mpf("0.625")
    z_val = mp.mpf("0.3125")
    dz_val = mp.mpf("0.125")
    a_pi = mp.mpf("2.25")
    b_pi = mp.mpf("-0.75")
    w_alt = mp.mpf("0.1875")
    a_alt = mp.mpf("-1.0")
    tr_base = w_sym * s_pi + w_std * (z_val * a_pi + b_pi) + w_alt * a_alt
    tr_exp = (
        w_sym * s_pi + w_std * (z_val * a_pi) + w_std * b_pi + w_alt * a_alt
    )
    tr_shift = (
        w_sym * s_pi
        + w_std * ((z_val + dz_val) * a_pi + b_pi)
        + w_alt * a_alt
    )
    exp_res = tr_base - tr_exp
    z_step_res = (tr_shift - tr_base) - w_std * (dz_val * a_pi)
    pass_q6h7 = bool(abs(exp_res) < tol and abs(z_step_res) < tol)

    # 2. Bean qou-qd27: Bring curve Sigma_4 (genus 4) adjoint H^1 rank (2g - 2) * d
    # For PSL(2, C) / sl_2 adjoint bundle (d = 3) on Bring's curve (g = 4): H^1 dim = 6 * 3 = 18
    g_bring = mp.mpf(4)
    d_sl2 = mp.mpf(3)
    d_sl3 = mp.mpf(8)
    h1_bring_sl2 = (2 * g_bring - 2) * d_sl2
    h1_g5_sl2 = (2 * (g_bring + 1) - 2) * d_sl2
    h1_torus_sl2 = (2 * mp.mpf(1) - 2) * d_sl2
    step_g_res = (h1_g5_sl2 - h1_bring_sl2) - 2 * d_sl2
    bring_four_res = h1_bring_sl2 - 6 * d_sl2
    fibre_add_res = (2 * g_bring - 2) * (d_sl2 + d_sl3) - (
        (2 * g_bring - 2) * d_sl2 + (2 * g_bring - 2) * d_sl3
    )
    pass_qd27 = bool(
        abs(step_g_res) < tol
        and abs(bring_four_res) < tol
        and abs(h1_torus_sl2) < tol
        and abs(fibre_add_res) < tol
        and h1_bring_sl2 == 18
    )

    # 3. Bean qou-qint: Balanced q-integer bar-even symmetry and doubling
    q_val = mp.exp(mp.mpf("0.175"))
    q_inv = 1 / q_val
    k_int = 5
    qk = q_val ** k_int
    q_inv_k = q_inv ** k_int
    num_pos = qk - q_inv_k
    num_bar = q_inv_k - qk
    sym_pos = qk + q_inv_k
    sym_bar = q_inv_k + qk
    q_int_pos = num_pos / (q_val - q_inv)
    q_int_bar = num_bar / (q_inv - q_val)
    bar_num_res = num_bar - (-num_pos)
    bar_sym_res = sym_bar - sym_pos
    bar_qint_res = q_int_bar - q_int_pos
    doubling_res = (num_pos * sym_pos) - (qk * qk - q_inv_k * q_inv_k)
    pass_qint = bool(
        abs(bar_num_res) < tol
        and abs(bar_sym_res) < tol
        and abs(bar_qint_res) < tol
        and abs(doubling_res) < tol
    )

    # 4. Bean qou-r91v: Hook-length log-dimension reduction ln f = ln k! - sum ln h
    # Check on S_5 partitions (4,1) [hooks 5,3,2,1,1; f=4] and (3,2) [hooks 4,3,1,2,1; f=5]
    log_fact_5 = mp.log(mp.mpf(120))
    sum_log_h_41 = mp.log(mp.mpf(5 * 3 * 2 * 1 * 1))  # ln 30
    sum_log_h_32 = mp.log(mp.mpf(4 * 3 * 1 * 2 * 1))  # ln 24
    log_f_41 = log_fact_5 - sum_log_h_41  # ln 4
    log_f_32 = log_fact_5 - sum_log_h_32  # ln 5
    diff_neg_res = (log_f_41 - log_f_32) - (-(sum_log_h_41 - sum_log_h_32))
    inv_res = (log_fact_5 - log_f_41) - sum_log_h_41
    c_odd = mp.mpf("1.375")
    odd_cancel_res = c_odd * log_f_41 + (-c_odd) * log_f_41
    pass_r91v = bool(
        abs(diff_neg_res) < tol
        and abs(inv_res) < tol
        and abs(odd_cancel_res) < tol
        and abs(log_f_41 - mp.log(mp.mpf(4))) < tol
        and abs(log_f_32 - mp.log(mp.mpf(5))) < tol
    )

    # 5. Bean qou-tvok: Poissonized (8/pi^2) vs de-Poissonized (8/(9*pi^2)) content variance
    v_poisson = 8 / (mp.pi ** 2)
    v_depoisson = 8 / (9 * (mp.pi ** 2))
    ninefold_res = v_poisson - 9 * v_depoisson
    r_p = mp.mpf("-0.0678")
    r_d = mp.mpf("-0.0075")
    rem_res = ((9 * v_depoisson + r_p) - 9 * (v_depoisson + r_d)) - (
        r_p - 9 * r_d
    )

    # Also verify exact partial-fraction identity for 1 / (n * (n^2 - 4)^2) for n = 3, 5, 7, 9:
    # 1 / (n * (n^2 - 4)^2) = 1/(16*n) - 1/(32*(n-2)) - 1/(32*(n+2))
    #                         + 1/(32*(n-2)^2) - 1/(32*(n+2)^2)
    max_pf_err = mp.mpf(0)
    for n_odd in (3, 5, 7, 9):
        nm = mp.mpf(n_odd)
        lhs_pf = 1 / (nm * ((nm ** 2 - 4) ** 2))
        rhs_pf = (
            1 / (16 * nm)
            - 1 / (32 * (nm - 2))
            - 1 / (32 * (nm + 2))
            + 1 / (32 * ((nm - 2) ** 2))
            - 1 / (32 * ((nm + 2) ** 2))
        )
        err_pf = abs(lhs_pf - rhs_pf)
        if err_pf > max_pf_err:
            max_pf_err = err_pf

    pass_tvok = bool(
        abs(ninefold_res) < tol and abs(rem_res) < tol and max_pf_err < tol
    )

    all_passed = bool(
        pass_q6h7 and pass_qd27 and pass_qint and pass_r91v and pass_tvok
    )

    return {
        "schemaVersion": "1.0",
        "brick": "QOU.QBeta.NucleonOrderingAndBringAdjointTorsionBrick",
        "beans": [
            "qou-q6h7",
            "qou-qd27",
            "qou-qint",
            "qou-r91v",
            "qou-tvok",
        ],
        "scriptPath": str(SCRIPT_PATH.relative_to(REPO_ROOT)),
        "scriptHash": script_sha256_prefix(),
        "scriptCommitSha": git_commit_sha(),
        "dirty": git_is_dirty(),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "precisionDps": 80,
        "allPassed": all_passed,
        "checks": {
            "qou_q6h7_nucleon_ordering_factorization": {
                "theorem": "nucleonOrderingTrace_expanded_and_z_shift",
                "baseNucleonOrderingTrace": fmt_mp(tr_base),
                "expansionResidual": fmt_mp(exp_res),
                "zShiftResidual": fmt_mp(z_step_res),
                "passed": pass_q6h7,
            },
            "qou_qd27_bring_sigma4_adjoint_h1_rank": {
                "theorem": "adjointSurfaceH1Rank_genus_step_and_bring_four",
                "bringSigma4Sl2H1Rank": fmt_mp(h1_bring_sl2),
                "genusStepResidual": fmt_mp(step_g_res),
                "bringGenusFourResidual": fmt_mp(bring_four_res),
                "torusGenusOneRank": fmt_mp(h1_torus_sl2),
                "fibreAdditivityResidual": fmt_mp(fibre_add_res),
                "passed": pass_qd27,
            },
            "qou_qint_balanced_q_integer_bar_parity": {
                "theorem": "balancedQPair_bar_parity",
                "balancedQ5AtExp0175": fmt_mp(q_int_pos),
                "barNumeratorResidual": fmt_mp(bar_num_res),
                "barSymmetricResidual": fmt_mp(bar_sym_res),
                "barBalancedQIntResidual": fmt_mp(bar_qint_res),
                "doublingProductResidual": fmt_mp(doubling_res),
                "passed": pass_qint,
            },
            "qou_r91v_hook_log_dimension_reduction": {
                "theorem": "logDimFromHooks_diff_negation_and_involution",
                "logDimPartition41": fmt_mp(log_f_41),
                "logDimPartition32": fmt_mp(log_f_32),
                "differenceNegationResidual": fmt_mp(diff_neg_res),
                "involutionResidual": fmt_mp(inv_res),
                "conjugateOddModeCancellationResidual": fmt_mp(odd_cancel_res),
                "passed": pass_r91v,
            },
            "qou_tvok_poisson_depoisson_variance_ratio": {
                "theorem": "poissonDePoissonGap_ninefold_locus_and_remainder",
                "poissonizedLeadingVariance": fmt_mp(v_poisson),
                "dePoissonizedLeadingVariance": fmt_mp(v_depoisson),
                "ninefoldRatioResidual": fmt_mp(ninefold_res),
                "remainderPropagationResidual": fmt_mp(rem_res),
                "maxPartialFractionResidual": fmt_mp(max_pf_err),
                "passed": pass_tvok,
            },
        },
    }


def main() -> None:
    payload = run_probe()
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH} (allPassed={payload['allPassed']})")
    if not payload["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
