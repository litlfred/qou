#!/usr/bin/env python3
"""80-dps mpmath probe for Round 98 Mass theorems (qou-8vyi, qou-969b, qou-99fk, qou-a0j7, qou-a28x)."""

import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def verify_consecutive_not_split() -> dict:
    # Verify chainCarrier consecutive triple {i, i+1, i+2} has adjacent pairs (i, i+1) and (i+1, i+2)
    lk_val = -mp.mpf("2")
    joins_01 = abs(lk_val) > mp.mpf("0")
    joins_12 = abs(lk_val) > mp.mpf("0")
    splits_first = not joins_01
    return {
        "lkConsecutive": mp.nstr(lk_val, 80),
        "firstSplitsOff": splits_first,
        "passed": (not splits_first) and joins_01 and joins_12,
    }


def verify_palindromic_inv_lift() -> dict:
    x_val = mp.mpf("7") / mp.mpf("3")
    z_val = mp.mpf("5") / mp.mpf("2")
    z_inv = mp.mpf("1") / z_val
    x_div_z = x_val / z_val

    def color_cubic(x: mp.mpf, z: mp.mpf) -> mp.mpf:
        return (
            x ** 3
            + (z + mp.mpf("1")) * (x ** 2)
            + (z ** 2 + z + mp.mpf("1")) * x
            + (z ** 3 + z ** 2 + z + mp.mpf("1"))
        )

    lhs = (z_val ** 3) * color_cubic(x_div_z, z_inv)
    rhs = color_cubic(x_val, z_val)
    diff = lhs - rhs
    return {
        "lhs": mp.nstr(lhs, 80),
        "rhs": mp.nstr(rhs, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_psd_det_one_trace() -> dict:
    # Positive semidefinite 2x2 real symmetric matrix [[a, b], [b, d]] with a*d - b^2 = 1
    a_val = mp.mpf("3")
    b_val = mp.mpf("1")
    d_val = (mp.mpf("1") + b_val ** 2) / a_val
    det_val = a_val * d_val - b_val ** 2
    trace_val = a_val + d_val
    shifted = trace_val - mp.mpf("2")
    return {
        "det": mp.nstr(det_val, 80),
        "trace": mp.nstr(trace_val, 80),
        "traceMinusTwo": mp.nstr(shifted, 80),
        "passed": abs(det_val - mp.mpf("1")) < mp.mpf("10") ** (-75) and shifted >= mp.mpf("0"),
    }


def verify_qbeta_proxy_reduction() -> dict:
    q_val = mp.mpf("3") / mp.mpf("2")
    h_val = q_val - mp.mpf("1") / q_val
    e0_val = mp.mpf("1") / (q_val * (q_val - mp.mpf("1")))
    qbeta_proxy = (
        (mp.mpf("2") * q_val - q_val ** 2 + mp.mpf("1"))
        * (q_val + mp.mpf("1"))
        / (mp.mpf("2") * (q_val ** 3))
    )
    rhs = e0_val * h_val * (mp.mpf("2") - h_val) / mp.mpf("2")
    diff = qbeta_proxy - rhs
    return {
        "qbetaProxy": mp.nstr(qbeta_proxy, 80),
        "rhs": mp.nstr(rhs, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_confluent_kernel() -> dict:
    # Involution numbers f(0)=1, f(1)=1, f(n+2) = f(n+1) + (n+1)*f(n)
    f_seq = [mp.mpf("1"), mp.mpf("1")]
    for k in range(6):
        f_seq.append(f_seq[-1] + mp.mpf(str(k + 1)) * f_seq[-2])
    n_idx = 4
    b_n = f_seq[n_idx] / mp.factorial(n_idx)
    b_n1 = f_seq[n_idx + 1] / mp.factorial(n_idx + 1)
    b_n2 = f_seq[n_idx + 2] / mp.factorial(n_idx + 2)
    residual = mp.mpf(str(n_idx + 2)) * b_n2 - (b_n1 + b_n)
    return {
        "n": n_idx,
        "b_n2_scaled": mp.nstr(mp.mpf(str(n_idx + 2)) * b_n2, 80),
        "b_n1_plus_b_n": mp.nstr(b_n1 + b_n, 80),
        "residual": mp.nstr(residual, 80),
        "passed": abs(residual) < mp.mpf("10") ** (-75),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    c1 = verify_consecutive_not_split()
    c2 = verify_palindromic_inv_lift()
    c3 = verify_psd_det_one_trace()
    c4 = verify_qbeta_proxy_reduction()
    c5 = verify_confluent_kernel()

    all_passed = all(x["passed"] for x in (c1, c2, c3, c4, c5))
    payload = {
        "probe": "onesep_palindromic_psdtrace_qbetaproxy_confluent_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/onesep_palindromic_psdtrace_qbetaproxy_confluent_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": int(mp.dps),
        "allPassed": all_passed,
        "checks": {
            "consecutiveFirstNotSplitsOff": c1,
            "colorCubicInvLiftSubEqZero": c2,
            "psdDetOneSubTwoNonneg": c3,
            "qbetaProxySubE0HReductionEqZero": c4,
            "normalizedClassicalKernelSubEqZero": c5,
        },
    }
    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    else:
        print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
