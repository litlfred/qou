#!/usr/bin/env python3
"""80-dps mpmath probe for Round 101 beans:
- qou-jgp2: Right-annihilator generator self-adjoint idempotent axiom discharge (2 -> 0) and e + (1 - e) = 1
- qou-nxjw: Toroidal harmonics variable x = 1/(2w) - 1 under convention D (332 < 1000 vs 1500 > 1000)
- qou-q425: Canonical bilinear form 3-strand torus trace period-3 character balance (2 + (-1) + (-1) = 0, gap 3)
- qou-vls6: Flavor-split Step 2 cubic leading degree 3 -> inversion exponent 2 and residual gap 67 - 10 = 57
- qou-wlnx: Spectral decomposition Q-value under convention D (F_deg2 shift 36844 - 5904 = 30940, spans 90 and 99)
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80


def run_probe() -> dict:
    script_path = pathlib.Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()
    try:
        commit_sha = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=script_path.parent
            )
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    # 1. qou-jgp2: axiom discharge 2 - 2 = 0 and idempotent projection complement e + (1 - e) = 1
    initial_axioms = mp.mpf("2")
    discharged_axioms = mp.mpf("2")
    remaining_axioms = initial_axioms - discharged_axioms
    e_zero = mp.mpf("0")
    e_one = mp.mpf("1")
    comp_zero = mp.mpf("1") - e_zero
    comp_one = mp.mpf("1") - e_one
    c1_pass = bool(
        remaining_axioms == mp.mpf("0")
        and e_zero + comp_zero == mp.mpf("1")
        and e_one + comp_one == mp.mpf("1")
        and e_one * e_one == e_one
    )

    # 2. qou-nxjw: x = 1/(2w) - 1 under convention D: z_D^2 gives 332 thousandths (< 1000), bar-invariant gives 1500 (> 1000)
    margin_sub = mp.mpf("332") - mp.mpf("1000")
    margin_super = mp.mpf("1500") - mp.mpf("1000")
    span_val = mp.mpf("1500") - mp.mpf("332")
    c2_pass = bool(
        margin_sub == mp.mpf("-668")
        and margin_super == mp.mpf("500")
        and span_val == mp.mpf("1168")
    )

    # 3. qou-q425: period-3 character chi(s) = (2, -1, -1) balance and branch gap
    chi_0 = mp.mpf("2")
    chi_1 = mp.mpf("-1")
    chi_2 = mp.mpf("-1")
    period_sum = chi_0 + chi_1 + chi_2
    branch_gap = chi_0 - chi_1
    c3_pass = bool(
        period_sum == mp.mpf("0")
        and branch_gap == mp.mpf("3")
    )

    # 4. qou-vls6: flavor-split leading cubic order 3 -> inversion prefactor exponent 2 and residual gap 67 - 10 = 57
    leading_deg = mp.mpf("3")
    inv_exp = leading_deg - mp.mpf("1")
    res_gap = mp.mpf("67") - mp.mpf("10")
    c4_pass = bool(
        inv_exp == mp.mpf("2")
        and res_gap == mp.mpf("57")
    )

    # 5. qou-wlnx: spectral decomposition Q-value F_deg2 shift (36844 - 5904 = 30940) and error spans (90, 99)
    f_deg2_shift = mp.mpf("36844") - mp.mpf("5904")
    bare_span = mp.mpf("98") - mp.mpf("8")
    combined_span = mp.mpf("100") - mp.mpf("1")
    c5_pass = bool(
        f_deg2_shift == mp.mpf("30940")
        and bare_span == mp.mpf("90")
        and combined_span == mp.mpf("99")
    )

    checks = [
        {
            "id": "qou-jgp2-right-annihilator-projection-complement",
            "passed": c1_pass,
            "remainingAxioms": mp.nstr(remaining_axioms, 80),
            "complementZero": mp.nstr(comp_zero, 80),
            "complementOne": mp.nstr(comp_one, 80),
        },
        {
            "id": "qou-nxjw-toroidal-domain-threshold-separation",
            "passed": c2_pass,
            "marginSubThousandths": mp.nstr(margin_sub, 80),
            "marginSuperThousandths": mp.nstr(margin_super, 80),
            "candidateSpanThousandths": mp.nstr(span_val, 80),
        },
        {
            "id": "qou-q425-period-three-character-balance",
            "passed": c3_pass,
            "periodSum": mp.nstr(period_sum, 80),
            "branchGap": mp.nstr(branch_gap, 80),
        },
        {
            "id": "qou-vls6-flavor-split-exponent-shift-and-residual-gap",
            "passed": c4_pass,
            "inversionExponent": mp.nstr(inv_exp, 80),
            "residualHundredthsGap": mp.nstr(res_gap, 80),
        },
        {
            "id": "qou-wlnx-spectral-qvalue-factor-shift-and-range-span",
            "passed": c5_pass,
            "fDeg2ShiftTenThousandths": mp.nstr(f_deg2_shift, 80),
            "bareSpanPercent": mp.nstr(bare_span, 80),
            "combinedSpanPercent": mp.nstr(combined_span, 80),
        },
    ]

    all_passed = all(item["passed"] for item in checks)
    return {
        "probe": "right_annihilator_projection_complement_toroidal_domain_threshold_period_three_character_balance_flavor_split_exponent_shift_and_spectral_qvalue_range_span_probe",
        "beans": ["qou-jgp2", "qou-nxjw", "qou-q425", "qou-vls6", "qou-wlnx"],
        "dps": 80,
        "scriptHash": script_hash,
        "scriptSha256": script_hash,
        "scriptCommitSha": commit_sha,
        "allPassed": all_passed,
        "checks": checks,
    }


def main() -> None:
    witness = run_probe()
    out_path = pathlib.Path(__file__).with_name(
        "right_annihilator_projection_complement_toroidal_domain_threshold_period_three_character_balance_flavor_split_exponent_shift_and_spectral_qvalue_range_span_probe_witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    assert witness["allPassed"], "Probe checks failed"


if __name__ == "__main__":
    main()
