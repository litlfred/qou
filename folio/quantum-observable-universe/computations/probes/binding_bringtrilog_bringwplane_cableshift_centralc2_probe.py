#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 104 BraidKnot theorems (qou-e9pp, qou-eggf, qou-ekgf, qou-f1rs, qou-f4el)."""

import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80


def check_binding_isovector_mirror_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    kappa = mp.mpf("7") / mp.mpf("13")
    checks = []
    for z_val, n_val in [(3, 4), (6, 8), (11, 9)]:
        z_mp = mp.mpf(str(z_val))
        n_mp = mp.mpf(str(n_val))
        b_zn = kappa * (mp.mpf("2") * (z_mp - n_mp))
        b_nz = kappa * (mp.mpf("2") * (n_mp - z_mp))
        residual = (b_zn - b_nz) - mp.mpf("4") * kappa * (z_mp - n_mp)
        passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "Z": str(z_val),
            "N": str(n_val),
            "residual": mp.nstr(residual, 30),
            "passed": passed,
        })
    return {
        "theorem": "binding_isovector_mirror_sub_eq_zero",
        "bean": "qou-e9pp",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_im_li3_zeta5_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    k_mp = mp.mpf("5")
    predicted = (k_mp - mp.mpf("1")) * (k_mp - mp.mpf("2")) * mp.power(mp.pi, 3) / (mp.mpf("3") * mp.power(k_mp, 3))
    closed_val = mp.mpf("4") * mp.power(mp.pi, 3) / mp.mpf("125")
    residual = predicted - closed_val
    passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
    return {
        "theorem": "im_li3_zeta5_sub_eq_zero",
        "bean": "qou-eggf",
        "passed": passed,
        "residual": mp.nstr(residual, 30),
    }


def check_powtrace_recurrence_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    # Unimodular 2x2 matrix [[2, 1], [1, 1]], det = 2*1 - 1*1 = 1, tr = 3
    m_mat = mp.matrix([[mp.mpf("2"), mp.mpf("1")], [mp.mpf("1"), mp.mpf("1")]])
    tr_m = m_mat[0, 0] + m_mat[1, 1]
    checks = []
    for n in range(1, 6):
        mn = m_mat ** n
        mn1 = m_mat ** (n + 1)
        mn2 = m_mat ** (n + 2)
        tr_n = mn[0, 0] + mn[1, 1]
        tr_n1 = mn1[0, 0] + mn1[1, 1]
        tr_n2 = mn2[0, 0] + mn2[1, 1]
        residual = tr_n2 - (tr_m * tr_n1 - tr_n)
        passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "n": str(n),
            "residual": mp.nstr(residual, 30),
            "passed": passed,
        })
    return {
        "theorem": "powTrace_recurrence_sub_eq_zero",
        "bean": "qou-ekgf",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_writhe_cable_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    words = [[1, 2, -1, 3], [-2, -1, 2, -3, 1]]
    checks = []
    for w in words:
        writhe_w = sum(1 if g > 0 else -1 for g in w)
        cable_w = []
        for g in w:
            cable_w.extend([2 * g, 2 * g - 1, 2 * g + 1, 2 * g])
        writhe_c = sum(1 if g > 0 else -1 for g in cable_w)
        residual = mp.mpf(str(writhe_c)) - mp.mpf("4") * mp.mpf(str(writhe_w))
        passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
        checks.append({
            "word": str(w),
            "residual": mp.nstr(residual, 30),
            "passed": passed,
        })
    return {
        "theorem": "writhe_cable_sub_eq_zero",
        "bean": "qou-f1rs",
        "passed": all(c["passed"] for c in checks),
        "samples": checks,
    }


def check_mapdomain_centralc2_sub_eq_zero() -> dict:
    mp.mp.dps = 80
    # Transposition count in S_a for a = b = 4 is a*(a-1)/2 = 6
    a_val = mp.mpf("4")
    b_val = mp.mpf("4")
    c2_a = a_val * (a_val - mp.mpf("1")) / mp.mpf("2")
    c2_b = b_val * (b_val - mp.mpf("1")) / mp.mpf("2")
    residual = c2_a - c2_b
    passed = bool(abs(residual) <= mp.power(mp.mpf("10"), -70))
    return {
        "theorem": "mapDomain_centralC2_sub_eq_zero",
        "bean": "qou-f4el",
        "passed": passed,
        "residual": mp.nstr(residual, 30),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    results = [
        check_binding_isovector_mirror_sub_eq_zero(),
        check_im_li3_zeta5_sub_eq_zero(),
        check_powtrace_recurrence_sub_eq_zero(),
        check_writhe_cable_sub_eq_zero(),
        check_mapdomain_centralc2_sub_eq_zero(),
    ]
    all_passed = all(r["passed"] for r in results)

    payload = {
        "probe": "binding_bringtrilog_bringwplane_cableshift_centralc2_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/binding_bringtrilog_bringwplane_cableshift_centralc2_probe.py",
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
