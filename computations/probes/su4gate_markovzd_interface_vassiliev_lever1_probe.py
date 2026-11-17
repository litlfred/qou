#!/usr/bin/env python3
"""80-dps mpmath computational witness probe for Round 72:
- qou-04ub: SU4SupermultipletGate (su4_supermultiplet_at_four_and_five)
- qou-dwf4: QBetaCanonicalMarkovWeightsDerived (canonical_y3_add_two_y21_eq_one)
- qou-foh0: InterfaceOperatorBlockDiagonal (interfaceBlock_zero_and_add)
- qou-tnvz: VassilievMagnitudeA3 (borrDeficit_sub_leadingWeight_mul)
- z2bn: Lever1Depth2Exclusion (lwCl_depth2_residual_at_seed_tau)
"""

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from mpmath import mp

mp.dps = 80


def script_sha256_12(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def run_probe(commit_sha: str) -> dict:
    probe_path = Path(__file__).resolve()
    s_hash = script_sha256_12(probe_path)

    q_val = mp.mpf("3") / mp.mpf("5")

    # 1. qou-04ub: SU4SupermultipletGate
    c44 = math.comb(4, 4)
    c45 = math.comb(4, 5)
    res_04ub = abs(mp.mpf(str(c44)) - mp.mpf("1")) + abs(mp.mpf(str(c45)) - mp.mpf("0"))

    # 2. qou-dwf4: QBetaCanonicalMarkovWeightsDerived
    def markov_zd(q: mp.mpf) -> mp.mpf:
        return (q ** 3) / ((q ** 2) + mp.mpf("1"))

    res_dwf4 = abs(markov_zd(mp.mpf("1")) - (mp.mpf("1") / mp.mpf("2"))) + abs(
        markov_zd(-q_val) - (-markov_zd(q_val))
    )

    # 3. qou-foh0: InterfaceOperatorBlockDiagonal
    # Verify additivity and zero preservation of P_i * I * P_i on 2x2 matrices
    p_mat = [[mp.mpf("1"), mp.mpf("0")], [mp.mpf("0"), mp.mpf("0")]]
    i_mat = [[mp.mpf("7") / mp.mpf("3"), mp.mpf("2")], [mp.mpf("-1"), mp.mpf("5")]]
    j_mat = [[mp.mpf("4") / mp.mpf("3"), mp.mpf("-3")], [mp.mpf("6"), mp.mpf("2")]]
    z_mat = [[mp.mpf("0"), mp.mpf("0")], [mp.mpf("0"), mp.mpf("0")]]

    def mat_mul(a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
        ]

    def mat_add(a, b):
        return [
            [a[0][0] + b[0][0], a[0][1] + b[0][1]],
            [a[1][0] + b[1][0], a[1][1] + b[1][1]],
        ]

    def interface_block(p, op):
        return mat_mul(mat_mul(p, op), p)

    blk_z = interface_block(p_mat, z_mat)
    blk_sum = interface_block(p_mat, mat_add(i_mat, j_mat))
    blk_sep = mat_add(interface_block(p_mat, i_mat), interface_block(p_mat, j_mat))
    res_foh0 = sum(
        abs(blk_z[r][c]) + abs(blk_sum[r][c] - blk_sep[r][c])
        for r in range(2)
        for c in range(2)
    )

    # 4. qou-tnvz: VassilievMagnitudeA3
    # Verify (borrDeficit(h) - leadingWeight(h)) * (h^2 + 4) = (1/4) * h^6
    h_val = q_val - (mp.mpf("1") / q_val)
    borr_def = (h_val ** 4) * (mp.mpf("3") + (h_val ** 2)) / ((h_val ** 2) + mp.mpf("4"))
    lead_wt = (mp.mpf("3") / mp.mpf("4")) * (h_val ** 4)
    lhs_tnvz = (borr_def - lead_wt) * ((h_val ** 2) + mp.mpf("4"))
    rhs_tnvz = (mp.mpf("1") / mp.mpf("4")) * (h_val ** 6)
    res_tnvz = abs(lhs_tnvz - rhs_tnvz)

    # 5. z2bn: Lever1Depth2Exclusion
    # Verify lwCl(4) - ((21/8)*lwCl(3) - lwCl(2)) = -7/240
    lw2 = mp.mpf("4") / mp.mpf("3")
    lw3 = mp.mpf("5") / mp.mpf("2")
    lw4 = mp.mpf("26") / mp.mpf("5")
    tau_seed = mp.mpf("21") / mp.mpf("8")
    lhs_z2bn = lw4 - (tau_seed * lw3 - lw2)
    rhs_z2bn = -mp.mpf("7") / mp.mpf("240")
    res_z2bn = abs(lhs_z2bn - rhs_z2bn)

    tol = mp.mpf("10") ** (-70)
    checks = [
        {
            "id": "qou-04ub-su4-supermultiplet-boundary",
            "bean": "qou-04ub",
            "description": "Wigner SU(4) antisymmetric supermultiplet boundary C(4,4)=1 and C(4,5)=0",
            "choose44": str(c44),
            "choose45": str(c45),
            "residual": mp.nstr(res_04ub, 25),
            "passed": bool(c44 == 1 and c45 == 0 and res_04ub <= tol),
        },
        {
            "id": "qou-dwf4-markovzd-anchor-and-odd-parity",
            "bean": "qou-dwf4",
            "description": "Convention-D Markov parameter z_D(1)=1/2 and odd parity z_D(-q)=-z_D(q) at q=3/5",
            "zDAtOne": mp.nstr(markov_zd(mp.mpf("1")), 40),
            "zDAtQ": mp.nstr(markov_zd(q_val), 40),
            "residual": mp.nstr(res_dwf4, 25),
            "passed": bool(res_dwf4 <= tol),
        },
        {
            "id": "qou-foh0-interface-block-linearity",
            "bean": "qou-foh0",
            "description": "Isotypic compression interfaceBlock P 0 = 0 and interfaceBlock P (I+J) = interfaceBlock P I + interfaceBlock P J",
            "block00Sum": mp.nstr(blk_sum[0][0], 40),
            "residual": mp.nstr(res_foh0, 25),
            "passed": bool(res_foh0 <= tol),
        },
        {
            "id": "qou-tnvz-borromean-deficit-sub-leading-tail",
            "bean": "qou-tnvz",
            "description": "(borrDeficit(h) - leadingWeight(h)) * (h^2 + 4) = (1/4)*h^6 at h = 3/5 - 5/3",
            "lhs": mp.nstr(lhs_tnvz, 40),
            "rhs": mp.nstr(rhs_tnvz, 40),
            "residual": mp.nstr(res_tnvz, 25),
            "passed": bool(res_tnvz <= tol),
        },
        {
            "id": "z2bn-lever1-depth2-seed-residual",
            "bean": "z2bn",
            "description": "Classical lever-1 depth-2 recurrence residual lw(4) - ((21/8)*lw(3) - lw(2)) = -7/240",
            "lhs": mp.nstr(lhs_z2bn, 40),
            "rhs": mp.nstr(rhs_z2bn, 40),
            "residual": mp.nstr(res_z2bn, 25),
            "passed": bool(res_z2bn <= tol),
        },
    ]

    return {
        "schemaVersion": "1.0",
        "probeId": "su4gate-markovzd-interface-vassiliev-lever1",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "scriptPath": "computations/probes/su4gate_markovzd_interface_vassiliev_lever1_probe.py",
        "scriptHash": s_hash,
        "scriptCommitSha": commit_sha,
        "precisionDps": 80,
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit-sha", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    witness = run_probe(args.commit_sha)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
