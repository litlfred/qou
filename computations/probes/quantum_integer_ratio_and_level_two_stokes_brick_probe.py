#!/usr/bin/env python3
"""80-dps mpmath probe for QuantumIntegerRatioAndLevelTwoStokesBrick (qou-l2t2, qou-l39s, qou-l525, qou-li27, qou-lzzi)."""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
import mpmath as mp

mp.mp.dps = 80

SCRIPT_PATH = pathlib.Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
WITNESS_PATH = SCRIPT_PATH.with_name(
    "quantum-integer-ratio-and-level-two-stokes-brick.witness.json"
)


def q_integer_two_three_pair(q: int) -> tuple[int, int]:
    return (1 + q, 1 + q + q * q)


def parity_signed_dim_pair(d_even: int, d_odd: int) -> tuple[int, int]:
    return (d_even + d_odd, d_even - d_odd)


def depth_comm_cost(bandwidth: int, depth: int, comm: int) -> int:
    return bandwidth * depth + comm


def symmetry_folded_block(mult: int, weight: int, trace_val: int) -> int:
    return mult * (weight * trace_val)


def unipotent_three_compose(
    a12: int, a23: int, a13: int, b12: int, b23: int, b13: int
) -> tuple[int, int, int]:
    return (a12 + b12, a23 + b23, a13 + b13 + a12 * b23)


def run_probe() -> dict:
    mp.mp.dps = 80
    checks = []

    # 1. qou-l2t2: quantum-integer polynomial numerators & normalization shift
    l2t2_ok = True
    for q in [-4, -2, 1, 2, 3, 5, 8]:
        n2, n3 = q_integer_two_three_pair(q)
        u2, u3 = q_integer_two_three_pair(1)
        if not (
            n3 - n2 == q * q
            and n3 * (q - 1) == q * (q * q) - 1
            and n2 * n2 - n3 == q
            and u2 + u3 + q == 5 + q
        ):
            l2t2_ok = False
    q0_mp = (mp.mpf(3) + mp.sqrt(mp.mpf(5))) / mp.mpf(2)
    sym_ratio = mp.log(q0_mp + mp.mpf(1) + mp.mpf(1) / q0_mp) / mp.log(
        mp.sqrt(q0_mp) + mp.mpf(1) / mp.sqrt(q0_mp)
    )
    unsym_ratio = mp.log(mp.mpf(1) + q0_mp + q0_mp**2) / mp.log(mp.mpf(1) + q0_mp)
    norm_gap_mp = abs(unsym_ratio - sym_ratio)
    checks.append(
        {
            "bean": "qou-l2t2",
            "name": "qIntegerTwoThreePair_gap_cubic_and_normalization_shift",
            "passed": bool(l2t2_ok and norm_gap_mp > mp.mpf("0.01")),
            "conventionLogRatioShift80dps": mp.nstr(norm_gap_mp, 80),
        }
    )

    # 2. qou-l39s: parity-signed partition dimension decomposition
    l39s_ok = True
    for e1, o1, e2, o2 in [(7, 5, 11, 3), (14, 9, 6, 12), (21, 18, 4, 7)]:
        tot, sgn = parity_signed_dim_pair(e1, o1)
        _, sgn_sum = parity_signed_dim_pair(e1 + e2, o1 + o2)
        _, sgn2 = parity_signed_dim_pair(e2, o2)
        _, sgn_flip = parity_signed_dim_pair(o1, e1)
        if not (
            tot + sgn == 2 * e1
            and tot - sgn + e1 == 2 * o1 + e1
            and sgn_sum == sgn + sgn2
            and sgn_flip + sgn + e2 + o2 == e2 + o2
        ):
            l39s_ok = False
    s3_signed_sum_mp = mp.mpf(parity_signed_dim_pair(2, 2)[1])
    checks.append(
        {
            "bean": "qou-l39s",
            "name": "paritySignedDimPair_channel_projection_and_conjugate_flip",
            "passed": bool(l39s_ok and s3_signed_sum_mp == mp.mpf(0)),
            "s3SignedDimensionSum80dps": mp.nstr(s3_signed_sum_mp, 80),
        }
    )

    # 3. qou-l525: restricted-model depth & communication cost
    l525_ok = True
    for b1, b2, d1, d2, c1, c2 in [
        (4, 3, 7, 5, 11, 6),
        (9, 2, 12, 8, 4, 15),
        (6, 5, 10, 3, 0, 9),
    ]:
        c_comp = depth_comm_cost(b1, d1 + d2, c1 + c2)
        c_parts = depth_comm_cost(b1, d1, c1) + depth_comm_cost(b1, d2, c2)
        c_pure = depth_comm_cost(b1, d1, 0)
        c_bw_diff = depth_comm_cost(b1 + b2, d1, c1) - depth_comm_cost(b1, d1, c1)
        c_step = depth_comm_cost(b1, d1 + 1, c1) - depth_comm_cost(b1, d1, c1)
        if not (
            c_comp == c_parts
            and c_pure + d2 + c1 + c2 == b1 * d1 + d2 + c1 + c2
            and c_bw_diff == b2 * d1
            and c_step + b2 == b1 + b2
        ):
            l525_ok = False
    cost_sample_mp = mp.mpf(depth_comm_cost(8, 12, 19))
    checks.append(
        {
            "bean": "qou-l525",
            "name": "depthCommCost_stage_composition_and_bandwidth_split",
            "passed": bool(l525_ok and cost_sample_mp == mp.mpf(115)),
            "sampleDepthCommCost80dps": mp.nstr(cost_sample_mp, 80),
        }
    )

    # 4. qou-li27: symmetry-folded branching contraction
    li27_ok = True
    for m1, m2, w, t1, t2 in [
        (3, 3, 7, 11, -4),
        (6, 2, -5, 9, 13),
        (4, 4, 12, -8, 15),
    ]:
        b_tsum = symmetry_folded_block(m1, w, t1 + t2)
        b_tparts = symmetry_folded_block(m1, w, t1) + symmetry_folded_block(m1, w, t2)
        b_msum = symmetry_folded_block(m1 + m2, w, t1)
        b_mparts = symmetry_folded_block(m1, w, t1) + symmetry_folded_block(m2, w, t1)
        b_assoc = symmetry_folded_block(m1, w, t1)
        b_unit = symmetry_folded_block(1, w, t1)
        if not (
            b_tsum == b_tparts
            and b_msum + t2 == b_mparts + t2
            and b_assoc == (m1 * w) * t1
            and b_unit + m1 == w * t1 + m1
        ):
            li27_ok = False
    folded_mp = mp.mpf(symmetry_folded_block(6, 5, 11))
    checks.append(
        {
            "bean": "qou-li27",
            "name": "symmetryFoldedBlock_linearity_and_associativity",
            "passed": bool(li27_ok and folded_mp == mp.mpf(330)),
            "foldedOrbitContraction80dps": mp.nstr(folded_mp, 80),
        }
    )

    # 5. qou-lzzi: level-2 upper-triangular 3x3 unipotent multiplication & commutator
    lzzi_ok = True
    for a12, a23, a13, b12, b23, b13 in [
        (3, -5, 7, 4, 6, -2),
        (-8, 9, 4, 5, -3, 11),
        (6, 2, -9, -6, -2, 21),
    ]:
        ab12, ab23, ab13 = unipotent_three_compose(a12, a23, a13, b12, b23, b13)
        _, _, ba13 = unipotent_three_compose(b12, b23, b13, a12, a23, a13)
        inv12, inv23, inv13 = unipotent_three_compose(
            a12, a23, a13, -a12, -a23, a12 * a23 - a13
        )
        if not (
            ab13 - ba13 == a12 * b23 - b12 * a23
            and ab12 + ab23 + a13 + b13 == a12 + b12 + a23 + b23 + a13 + b13
            and inv13 + a12 + a23 + a13 == a12 + a23 + a13
            and inv12 + inv23 + a12 + a23 + a13 == a12 + a23 + a13
        ):
            lzzi_ok = False
    comm_val_mp = mp.mpf(3 * 6 - 4 * (-5))
    checks.append(
        {
            "bean": "qou-lzzi",
            "name": "unipotentThreeCompose_corner_commutator_and_inverse",
            "passed": bool(lzzi_ok and comm_val_mp == mp.mpf(38)),
            "levelTwoCornerCommutator80dps": mp.nstr(comm_val_mp, 80),
        }
    )

    script_bytes = SCRIPT_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    commit_sha = (
        subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(REPO_ROOT), text=True
        ).strip()
    )
    status_out = subprocess.check_output(
        [
            "git",
            "status",
            "--porcelain",
            "--",
            str(SCRIPT_PATH.relative_to(REPO_ROOT)),
        ],
        cwd=str(REPO_ROOT),
        text=True,
    ).strip()

    witness = {
        "probe": "quantum_integer_ratio_and_level_two_stokes_brick_probe",
        "beans": ["qou-l2t2", "qou-l39s", "qou-l525", "qou-li27", "qou-lzzi"],
        "leanModule": "folio/quantum-observable-universe/lean/QOU/QBeta/QuantumIntegerRatioAndLevelTwoStokesBrick.lean",
        "precisionDps": "80",
        "scriptCommitSha": commit_sha,
        "scriptHash": script_hash,
        "dirty": bool(status_out),
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }
    WITNESS_PATH.write_text(json.dumps(witness, indent=2) + "\n")
    return witness


if __name__ == "__main__":
    result = run_probe()
    print(
        f"Witness written to {WITNESS_PATH.name}: allPassed={result['allPassed']}, "
        f"scriptCommitSha={result['scriptCommitSha']}, scriptHash={result['scriptHash']}"
    )
