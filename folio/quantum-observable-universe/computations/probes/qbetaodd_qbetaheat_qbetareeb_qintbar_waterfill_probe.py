#!/usr/bin/env python3
"""80-dps mpmath numerical witness probe for Round 116 BraidKnot theorems:
- qou-sof3: qbeta_odd_parity_c3_content_sub_g_eq_zero (QBetaOddParityAvatarReduction.lean)
- qou-srvu: heat_two_mode_composition_sub_eq_zero (QBetaPreArchHeatDepthOneKernel.lean)
- qou-ss52: qbeta_phase_leading_sq_sub_two_eq_zero (QBetaReebSinhParity.lean)
- qou-supr: denominator_bar_add_self_eq_zero (QuantumIntBarSymmetric.lean)
- qou-sxyr: extra_rows_tradeoff_sub_nonneg (RoundedWaterfillExchange.lean)
"""

import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def run_checks():
    results = []

    # 1. qou-sof3: qbeta_odd_parity_c3_content_sub_g_eq_zero
    a2 = -mp.mpf(1)
    g_val = -mp.mpf(23) / mp.mpf(9)
    u_val = mp.mpf(7) / mp.mpf(13)
    lhs1 = (mp.mpf(1) + a2 * (u_val ** 2)) * (mp.mpf(1) + g_val * (u_val ** 3)) - (mp.mpf(1) + a2 * (u_val ** 2)) - a2 * g_val * (u_val ** 5)
    rhs1 = g_val * (u_val ** 3)
    diff1 = lhs1 - rhs1
    results.append({
        "bean": "qou-sof3",
        "theorem": "QOU.BraidKnot.qbeta_odd_parity_c3_content_sub_g_eq_zero",
        "lhs": mp.nstr(lhs1, 80),
        "rhs": mp.nstr(rhs1, 80),
        "residual": mp.nstr(abs(diff1), 80),
        "passed": abs(diff1) < mp.mpf(10) ** (-75),
    })

    # 2. qou-srvu: heat_two_mode_composition_sub_eq_zero
    q_val = mp.mpf(17) / mp.mpf(11)
    mu1 = mp.mpf(3)
    mu2 = mp.mpf(7)
    t_val = mp.mpf(2) / mp.mpf(9)
    f0 = mp.mpf(5)
    g0 = mp.mpf(11)
    a_t = mp.mpf(1) - (q_val - mp.mpf(1)) * (mu1 * t_val)
    b_t = mp.mpf(1) - (q_val - mp.mpf(1)) * (mu2 * t_val)
    a_qt = mp.mpf(1) - (q_val - mp.mpf(1)) * (mu1 * (q_val * t_val))
    b_qt = mp.mpf(1) - (q_val - mp.mpf(1)) * (mu2 * (q_val * t_val))
    f_qt = a_t * f0
    g_qt = b_t * g0
    f_q2t = a_qt * f_qt
    g_q2t = b_qt * g_qt
    lhs2 = (b_t - a_t) * ((f_q2t + g_q2t) - a_qt * (f_qt + g_qt))
    rhs2 = (b_qt - a_qt) * b_t * ((f_qt + g_qt) - a_t * (f0 + g0))
    diff2 = lhs2 - rhs2
    results.append({
        "bean": "qou-srvu",
        "theorem": "QOU.BraidKnot.heat_two_mode_composition_sub_eq_zero",
        "lhs": mp.nstr(lhs2, 80),
        "rhs": mp.nstr(rhs2, 80),
        "residual": mp.nstr(abs(diff2), 80),
        "passed": abs(diff2) < mp.mpf(10) ** (-75),
    })

    # 3. qou-ss52: qbeta_phase_leading_sq_sub_two_eq_zero
    phi1 = mp.sqrt(mp.mpf(2))
    c2_val = -(phi1 ** 2) / mp.mpf(2)
    diff3 = (phi1 ** 2) - mp.mpf(2)
    results.append({
        "bean": "qou-ss52",
        "theorem": "QOU.BraidKnot.qbeta_phase_leading_sq_sub_two_eq_zero",
        "phi1": mp.nstr(phi1, 80),
        "c2Val": mp.nstr(c2_val, 80),
        "residual": mp.nstr(abs(diff3), 80),
        "passed": abs(c2_val + mp.mpf(1)) < mp.mpf(10) ** (-75) and abs(diff3) < mp.mpf(10) ** (-75),
    })

    # 4. qou-supr: denominator_bar_add_self_eq_zero
    q4 = mp.mpf(23) / mp.mpf(17)
    q4_bar = mp.mpf(1) / q4
    denom = q4 - (mp.mpf(1) / q4)
    denom_bar = q4_bar - (mp.mpf(1) / q4_bar)
    sum4 = denom_bar + denom
    results.append({
        "bean": "qou-supr",
        "theorem": "QOU.BraidKnot.QuantumIntBarSymmetric.denominator_bar_add_self_eq_zero",
        "denom": mp.nstr(denom, 80),
        "denomBar": mp.nstr(denom_bar, 80),
        "residual": mp.nstr(abs(sum4), 80),
        "passed": abs(sum4) < mp.mpf(10) ** (-75),
    })

    # 5. qou-sxyr: extra_rows_tradeoff_sub_nonneg
    a_val = mp.mpf(11) / mp.mpf(3)
    l_val = mp.mpf(4) / mp.mpf(5)
    j_val = mp.mpf(3)
    ceiling = ((a_val + l_val / mp.mpf(2)) ** 2) / (mp.mpf(2) * l_val)
    net_gain = j_val * a_val - (l_val / mp.mpf(2)) * (j_val * (j_val - mp.mpf(1)))
    margin5 = ceiling - net_gain
    results.append({
        "bean": "qou-sxyr",
        "theorem": "QOU.BraidKnot.RoundedWaterfillExchange.extra_rows_tradeoff_sub_nonneg",
        "ceiling": mp.nstr(ceiling, 80),
        "netGain": mp.nstr(net_gain, 80),
        "margin": mp.nstr(margin5, 80),
        "passed": margin5 > mp.mpf(0),
    })

    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()
    results = run_checks()
    all_passed = all(r["passed"] for r in results)
    if not all_passed:
        raise SystemExit("One or more probe checks failed")

    payload = {
        "probe": "qbetaodd_qbetaheat_qbetareeb_qintbar_waterfill_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/qbetaodd_qbetaheat_qbetareeb_qintbar_waterfill_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": "80",
        "allPassed": all_passed,
        "results": results,
    }
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
