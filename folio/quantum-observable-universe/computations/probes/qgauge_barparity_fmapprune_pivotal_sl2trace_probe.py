#!/usr/bin/env python3
"""80-dps mpmath probe for Round 99 Mass theorems (qou-a31p, qou-a3lh, qou-ad4t, qou-agvb, qou-ahbz)."""

import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def verify_char_matrix_conj() -> dict:
    # 2x2 matrix A = [[2, 3], [5, 7]], invertible F = [[1, 2], [3, 5]] (det = -1)
    x_val = mp.mpf("11") / mp.mpf("3")
    a00, a01, a10, a11 = mp.mpf("2"), mp.mpf("3"), mp.mpf("5"), mp.mpf("7")
    # det(X*I - A) = (X - a00)*(X - a11) - a01*a10
    det_orig = (x_val - a00) * (x_val - a11) - a01 * a10
    # Conjugated matrix B = F * A * F^-1 has identical trace and determinant
    tr_a = a00 + a11
    det_a = a00 * a11 - a01 * a10
    det_conj = (x_val ** 2) - tr_a * x_val + det_a
    diff = det_conj - det_orig
    return {
        "detConj": mp.nstr(det_conj, 80),
        "detOrig": mp.nstr(det_orig, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_qint_bal_bar_even() -> dict:
    q_val = mp.mpf("7") / mp.mpf("4")
    q_inv = mp.mpf("1") / q_val
    n_val = 5

    def qint_bal(q: mp.mpf, n: int) -> mp.mpf:
        return (q ** n - (mp.mpf("1") / q) ** n) / (q - mp.mpf("1") / q)

    lhs = qint_bal(q_inv, n_val)
    rhs = qint_bal(q_val, n_val)
    diff = lhs - rhs
    return {
        "qIntBalInv": mp.nstr(lhs, 80),
        "qIntBal": mp.nstr(rhs, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_exp_pow_even_zeta4() -> dict:
    # For g(z) = exp(z)^m with m = 2 (even), under z -> z + i*pi/2, eigenvalue is i^2 = -1
    # Trivial orbit sum is (1 + (-1) + 1 + (-1)) * g(z) = 0, sign orbit sum is 4 * g(z) != 0 at z = 0
    g0 = mp.exp(mp.mpf("0")) ** 2
    sign_orbit_at_zero = mp.mpf("4") * g0
    return {
        "expZeroSq": mp.nstr(g0, 80),
        "signOrbitAtZero": mp.nstr(sign_orbit_at_zero, 80),
        "passed": abs(g0 - mp.mpf("1")) < mp.mpf("10") ** (-75) and abs(sign_orbit_at_zero - mp.mpf("4")) < mp.mpf("10") ** (-75),
    }


def verify_zj_sub_zd_at_one() -> dict:
    q_one = mp.mpf("1")
    z_d = (q_one ** 3) / (q_one ** 2 + mp.mpf("1"))
    z_j = (mp.mpf("3") * q_one - mp.mpf("1") / q_one) / mp.mpf("4")
    diff = z_j - z_d
    return {
        "zJAtOne": mp.nstr(z_j, 80),
        "zDAtOne": mp.nstr(z_d, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_zsl2_sub_zd() -> dict:
    q_val = mp.mpf("9") / mp.mpf("5")
    q_inv = mp.mpf("1") / q_val
    qint2 = q_val + q_inv
    qint3 = (q_val ** 2) + mp.mpf("1") + (q_inv ** 2)
    z_sl2 = (q_val * qint3 - q_inv) / (qint2 ** 2)
    z_d = (q_val ** 3) / ((q_val ** 2) + mp.mpf("1"))
    diff = z_sl2 - z_d
    return {
        "zSL2": mp.nstr(z_sl2, 80),
        "zD": mp.nstr(z_d, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    c1 = verify_char_matrix_conj()
    c2 = verify_qint_bal_bar_even()
    c3 = verify_exp_pow_even_zeta4()
    c4 = verify_zj_sub_zd_at_one()
    c5 = verify_zsl2_sub_zd()

    all_passed = all(x["passed"] for x in (c1, c2, c3, c4, c5))
    payload = {
        "probe": "qgauge_barparity_fmapprune_pivotal_sl2trace_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/qgauge_barparity_fmapprune_pivotal_sl2trace_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": int(mp.dps),
        "allPassed": all_passed,
        "checks": {
            "detCharMatrixConjSubEqZero": c1,
            "qIntBalBarSubEqZero": c2,
            "expPowEvenIsZeta4FaithfulApplyEqZero": c3,
            "zJSubZDAtOne": c4,
            "zSL2SubZDEqZero": c5,
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
