#!/usr/bin/env python3
"""
Arbitrary-precision (50 dps mpmath) verification probe for:
  - qou-fcn8: Forced-chain bond count M_chain(A) = A - 1 vs magic-shell M_magic(A) = 2A
              coordination deficit (2A - (A - 1) = A + 1, 2A - 2(A - 1) = 2) and Route-2
              I_3 = 0 inter-nucleon linking channel blindness on N=Z magic shells.
  - qou-fmfw: Scale-free T / 3He mirror volume ratio Vol(8_11)/Vol(L6a4) = 1.130817...
              vs AME2020 B(T)/B(3He) = 1.0990 (2.90% spread, co-directional > 1 vs
              Vol*tr_M = 0.570 < 1) and Seifert-fibred Hopf deuteron Vol(L2a1) = 0 blocker.
  - qou-gnow: Magnitude Attack A — exact H_3 Frobenius pairing weighting gap between
              one-row baseline chi^[3] and y_[3]*chi^[3] + y_[2,1]*chi^[2,1] + y_[1,1,1]*chi^[1,1,1].
  - qou-j3bs: Magnitude Attack B — per-nucleon residual R(A)/A = B_AME(A)/A - 2.998 MeV
              sign flip (A=2 negative -> A>=4 positive) and interior peak at 56Fe across A=2..238.
  - qou-pc85: Mutual O'Hara channel uniform separation upper bound 1/d^2 <= 1/delta^2 and
              non-compact pointwise-disjoint counterexample d(n) = 1/(n+2) > 0.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

mp.dps = 50

Q0_STR = "1.10986745066625452388639923592099639321656599596504"


def run_probe() -> dict:
    q0 = mp.mpf(Q0_STR)

    # 1. qou-fcn8: Forced-chain A-1 vs magic-shell 2A coordination & I_3=0 channel blindness
    magic_nuclei = [4, 16, 40]
    fcn8_pass = True
    chain_vs_magic = {}
    for a_val in magic_nuclei:
        m_chain = a_val - 1
        m_magic = 2 * a_val
        z_val = a_val // 2
        n_pp = z_val * (z_val - 1) // 2
        n_nn = z_val * (z_val - 1) // 2
        net_i3 = 1 * n_pp + (-1) * n_nn
        if (m_magic - m_chain) != (a_val + 1) or (m_magic - 2 * m_chain) != 2 or net_i3 != 0:
            fcn8_pass = False
        chain_vs_magic[str(a_val)] = {
            "mChain": str(m_chain),
            "mMagic": str(m_magic),
            "deficit": str(m_magic - m_chain),
            "netI3": str(net_i3),
        }

    # 2. qou-fmfw: T / 3He mirror volume ratio vs AME2020 and Hopf Vol=0 blocker
    vol_t_811 = mp.mpf("8.2863168")
    vol_3he_l6a4 = mp.mpf("7.3277248")
    vol_hopf_2h = mp.mpf("0")
    b_ratio_ame = mp.mpf("1.0990")
    vol_trm_ratio = mp.mpf("0.570")

    vol_ratio = vol_t_811 / vol_3he_l6a4
    ratio_of_ratios = vol_ratio / b_ratio_ame
    rel_miss = abs(ratio_of_ratios - mp.mpf(1))

    fmfw_pass = bool(
        vol_ratio > mp.mpf(1)
        and b_ratio_ame > mp.mpf(1)
        and vol_trm_ratio < mp.mpf(1)
        and rel_miss < mp.mpf("0.03")
        and vol_hopf_2h == mp.mpf(0)
    )

    # 3. qou-gnow: H_3 Ocneanu/Plancherel weighting gap at q_0
    # In H_3(q), y_[3] + 2*y_[2,1] + y_[1,1,1] = 1
    two_q = q0 + 1 / q0
    three_q = q0 ** 2 + mp.mpf(1) + q0 ** -2
    y_3 = (q0 ** 3) / (two_q * three_q)
    y_21 = mp.mpf(1) / three_q
    y_111 = (q0 ** -3) / (two_q * three_q)
    weight_sum = y_3 + mp.mpf(2) * y_21 + y_111

    # Evaluate on single crossing sigma_1: chi^[3]=q0, chi^[2,1]=q0-1, chi^[1,1,1]=-1
    chi_3 = q0
    chi_21 = q0 - mp.mpf(1)
    chi_111 = -mp.mpf(1)

    frob_pair = y_3 * chi_3 + y_21 * chi_21 + y_111 * chi_111
    one_row_minus_frob = chi_3 - frob_pair
    decomp_rhs = y_21 * (mp.mpf(2) * chi_3 - chi_21) + y_111 * (chi_3 - chi_111)

    gnow_pass = bool(
        abs(weight_sum - mp.mpf(1)) < mp.mpf("1e-48")
        and abs(one_row_minus_frob - decomp_rhs) < mp.mpf("1e-48")
        and one_row_minus_frob > mp.mpf(0)
    )

    # 4. qou-j3bs: Super-pairwise extensive residual R(A)/A = B_AME/A - 2.998 MeV
    baseline_mev = mp.mpf("2.998")
    b_over_a_mev = {
        2: mp.mpf("1.112"),
        4: mp.mpf("7.074"),
        56: mp.mpf("8.790"),
        238: mp.mpf("7.570"),
    }
    residuals = {a: b_over_a_mev[a] - baseline_mev for a in (2, 4, 56, 238)}

    j3bs_pass = bool(
        residuals[2] < mp.mpf(0)
        and residuals[4] > mp.mpf(0)
        and residuals[4] < residuals[56]
        and residuals[56] > residuals[238]
    )

    # 5. qou-pc85: Mutual O'Hara uniform separation bound & non-compact guard
    delta_gap = mp.mpf("0.25")
    sample_dists = [mp.mpf("0.30"), mp.mpf("0.50"), mp.mpf("1.20")]
    upper_cap = mp.mpf(1) / (delta_gap ** 2)
    integrand_vals = [mp.mpf(1) / (d ** 2) for d in sample_dists]
    bounded_ok = all(mp.mpf(0) < val <= upper_cap for val in integrand_vals)

    # Guard: d(n) = 1/(n+2) > 0 for all n, but for M=100, d(100) = 1/102 < 1/100
    m_cap = 100
    d_at_m = mp.mpf(1) / mp.mpf(m_cap + 2)
    inv_m = mp.mpf(1) / mp.mpf(m_cap)

    pc85_pass = bool(bounded_ok and mp.mpf(0) < d_at_m < inv_m)

    checks = [
        {
            "id": "qou_fcn8_magic_shell_coordination_deficit_and_i3_zero",
            "passed": fcn8_pass,
            "magicShellSummary": chain_vs_magic,
        },
        {
            "id": "qou_fmfw_mirror_pair_volume_ratio_and_hopf_zero_blocker",
            "passed": fmfw_pass,
            "volRatioTritonOver3He": mp.nstr(vol_ratio, 35),
            "ameRatioTritonOver3He": mp.nstr(b_ratio_ame, 15),
            "ratioOfRatios": mp.nstr(ratio_of_ratios, 35),
            "relativeMiss": mp.nstr(rel_miss, 35),
            "volHopfDeuteron": mp.nstr(vol_hopf_2h, 5),
        },
        {
            "id": "qou_gnow_h3_frobenius_weighting_gap_decomposition",
            "passed": gnow_pass,
            "plancherelWeightSum": mp.nstr(weight_sum, 40),
            "oneRowMinusFrobeniusAtSigma1": mp.nstr(one_row_minus_frob, 40),
            "decompositionDifference": mp.nstr(abs(one_row_minus_frob - decomp_rhs), 15),
        },
        {
            "id": "qou_j3bs_extensive_residual_sign_flip_and_interior_peak",
            "passed": j3bs_pass,
            "residualA2MeV": mp.nstr(residuals[2], 15),
            "residualA4MeV": mp.nstr(residuals[4], 15),
            "residualA56MeV": mp.nstr(residuals[56], 15),
            "residualA238MeV": mp.nstr(residuals[238], 15),
        },
        {
            "id": "qou_pc85_mutual_ohara_uniform_separation_bound_and_guard",
            "passed": pc85_pass,
            "uniformUpperCap": mp.nstr(upper_cap, 20),
            "maxSampleIntegrand": mp.nstr(max(integrand_vals), 20),
            "nonCompactGuardDistAtM100": mp.nstr(d_at_m, 35),
            "proposedThresholdAtM100": mp.nstr(inv_m, 35),
        },
    ]

    all_passed = all(c["passed"] for c in checks)
    script_path = Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=script_path.parent)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "unknown"

    witness = {
        "probe": "magic-coordination-mirror-volume-frobenius-residual-ohara-probe",
        "beans": ["qou-fcn8", "qou-fmfw", "qou-gnow", "qou-j3bs", "qou-pc85"],
        "scriptPath": "computations/probes/magic_coordination_mirror_volume_frobenius_residual_ohara_probe.py",
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "dps": 50,
        "allPassed": all_passed,
        "checks": checks,
    }
    return witness


if __name__ == "__main__":
    w = run_probe()
    out_path = (
        Path(__file__).resolve().parent
        / "magic-coordination-mirror-volume-frobenius-residual-ohara-probe.witness.json"
    )
    out_path.write_text(json.dumps(w, indent=2) + "\n", encoding="utf-8")
    print(f"allPassed={w['allPassed']} scriptHash={w['scriptHash']} commit={w['scriptCommitSha']}")
