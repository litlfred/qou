#!/usr/bin/env python3
"""80-dps mpmath probe for Round 100 Mass theorems (qou-ahsy, qou-ahxm, qou-aj91, qou-akdup, qou-augu)."""

import argparse
import hashlib
import json
from pathlib import Path
from mpmath import mp

mp.dps = 80


def verify_saddle_offset_add() -> dict:
    q_val = mp.mpf("11") / mp.mpf("10")
    w_val = mp.mpf("7") / mp.mpf("5")
    hbar_q = mp.mpf("1") - mp.mpf("1") / q_val
    offset = w_val / q_val - w_val
    residual = offset + hbar_q * w_val
    return {
        "offset": mp.nstr(offset, 80),
        "hbarQMulW": mp.nstr(hbar_q * w_val, 80),
        "residual": mp.nstr(residual, 80),
        "passed": abs(residual) < mp.mpf("10") ** (-75),
    }


def verify_complete_b3_add_b4() -> dict:
    f2, f3, f4 = mp.mpf("1"), mp.mpf("3"), mp.mpf("6")
    b3_c = f3 - mp.mpf("3") * f2
    b4_c = f4 - mp.mpf("4") * f3 + mp.mpf("6") * f2
    total = b3_c + b4_c
    return {
        "b3Contrib": mp.nstr(b3_c, 80),
        "b4Contrib": mp.nstr(b4_c, 80),
        "sum": mp.nstr(total, 80),
        "passed": abs(total) < mp.mpf("10") ** (-75),
    }


def verify_sub_per_nucleon_pos() -> dict:
    av = mp.mpf("16")
    as_val = mp.mpf("18")
    ac = mp.mpf("7") / mp.mpf("10")
    u_val = mp.mpf("4")
    per_nuc = av - as_val / u_val - ac * (u_val ** 2)
    gap = av - per_nuc
    return {
        "perNucleon": mp.nstr(per_nuc, 80),
        "gap": mp.nstr(gap, 80),
        "passed": gap > mp.mpf("0"),
    }


def verify_tau_anchors_sub() -> dict:
    b_val = mp.mpf("21") / mp.mpf("10")
    lhs = (mp.mpf("1") + (mp.mpf("3") * (b_val ** 2) - mp.mpf("2")) / mp.mpf("4")) / ((b_val + mp.mpf("2")) / mp.mpf("3"))
    rhs = mp.mpf("3") * (mp.mpf("3") * (b_val ** 2) + mp.mpf("2")) / (mp.mpf("4") * (b_val + mp.mpf("2")))
    diff = lhs - rhs
    return {
        "lhs": mp.nstr(lhs, 80),
        "rhs": mp.nstr(rhs, 80),
        "residual": mp.nstr(diff, 80),
        "passed": abs(diff) < mp.mpf("10") ** (-75),
    }


def verify_binding_add_mutual() -> dict:
    self_e = mp.mpf("19") / mp.mpf("3")
    mutual_e = -mp.mpf("5") / mp.mpf("7")
    assembly_e = self_e + mutual_e
    binding_e = self_e - assembly_e
    total = binding_e + mutual_e
    return {
        "binding": mp.nstr(binding_e, 80),
        "mutualEnergy": mp.nstr(mutual_e, 80),
        "residual": mp.nstr(total, 80),
        "passed": abs(total) < mp.mpf("10") ** (-75),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", default="HEAD")
    parser.add_argument("--out", default="")
    args = parser.parse_args()

    script_bytes = Path(__file__).read_bytes()
    script_sha256 = hashlib.sha256(script_bytes).hexdigest()

    c1 = verify_saddle_offset_add()
    c2 = verify_complete_b3_add_b4()
    c3 = verify_sub_per_nucleon_pos()
    c4 = verify_tau_anchors_sub()
    c5 = verify_binding_add_mutual()

    all_passed = all(x["passed"] for x in (c1, c2, c3, c4, c5))
    payload = {
        "probe": "saddle_satinvis_satpeak_selrule_selfmutual_probe",
        "scriptPath": "folio/quantum-observable-universe/computations/probes/saddle_satinvis_satpeak_selrule_selfmutual_probe.py",
        "scriptCommitSha": args.commit_sha,
        "scriptHash": script_sha256,
        "scriptSha256": script_sha256,
        "dps": int(mp.dps),
        "allPassed": all_passed,
        "checks": {
            "saddleOffsetAddEqZero": c1,
            "completeB3AddB4EqZero": c2,
            "subPerNucleonPos": c3,
            "tauFromQuantumIntegerAnchorsSubEqZero": c4,
            "bindingAddMutualEnergyEqZero": c5,
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
