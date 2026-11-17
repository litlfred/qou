#!/usr/bin/env python3
"""80-dps mpmath numerical witness probe for Round 65 (qou-68e1, qou-mhx0, qou-pha4, qou-xyxc, qou-zwzd).

Verifies at 80 decimal places (mpmath.mp.dps = 80):
1. qou-pha4: Cumulative swap operators L_2(q), L_3(q) and elementary symmetric centrality
   e_1(L_2, L_3) = (q^2 - q) I_2, e_2(L_2, L_3) = -q^3 I_2 commuting with G_1(q), G_2(q).
2. qou-mhx0: Base-tabloid to diagonal-eigenbasis transition matrix P(q) = [v_0 | v_1(q)]
   diagonalizing L_2(q) and L_3(q) with determinant q + 1.
3. qou-68e1: Consolidated cell-length and content-shift polynomial product identities
   (1 - Q^3)(1 - Q)^2 = (1 - Q)^3 H_{(2,1)}(Q) and [2]_Q H_{(2,1)}(Q) = H_{(3)}(Q).
4. qou-zwzd: Additive multiplicity-weighted sum 1 + 2 Q [2]_Q + Q^3 = [3]_Q! and multiplicative
   shape product [2]_Q H_{(3)}(Q) H_{(2,1)}(Q) H_{(1,1,1)}(Q) = ([3]_Q!)^3.
5. qou-xyxc: Curl-difference trace factorization (q - q^-1) dim_q(V) = q^2 - q^-2 and cleared
   polynomial identity (q^2 - 1)(q^2 + 1) = q^4 - 1 uniquely forcing dim_q(V) = q + q^-1.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
import subprocess
from mpmath import mp

mp.dps = 80

PROBE_PATH = pathlib.Path(__file__).resolve()
REPO_ROOT = PROBE_PATH.parents[2]
WITNESS_DIR = REPO_ROOT / "computations" / "probes"
WITNESS_PATH = (
    WITNESS_DIR
    / "cumulative-swap-centrality-tabloid-transition-cell-product-factorial-curl-trace.witness.json"
)


def fmt(x: mp.mpf) -> str:
    return mp.nstr(x, 80, strip_zeros=False)


def mat2_mul(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [
        [
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
        ],
        [
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ],
    ]


def mat2_add(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return [
        [A[0][0] + B[0][0], A[0][1] + B[0][1]],
        [A[1][0] + B[1][0], A[1][1] + B[1][1]],
    ]


def mat2_sub_norm(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> mp.mpf:
    return max(
        abs(A[0][0] - B[0][0]),
        abs(A[0][1] - B[0][1]),
        abs(A[1][0] - B[1][0]),
        abs(A[1][1] - B[1][1]),
    )


def mat2_act(A: list[list[mp.mpf]], v: list[mp.mpf]) -> list[mp.mpf]:
    return [
        A[0][0] * v[0] + A[0][1] * v[1],
        A[1][0] * v[0] + A[1][1] * v[1],
    ]


def vec2_sub_norm(u: list[mp.mpf], v: list[mp.mpf]) -> mp.mpf:
    return max(abs(u[0] - v[0]), abs(u[1] - v[1]))


def run_probe() -> dict[str, object]:
    tol = mp.mpf("1e-75")
    q_trans = mp.exp(mp.mpf(1) / mp.mpf(7))
    q_samples = [q_trans, mp.mpf(2), mp.mpf(3), mp.mpf(5)]

    # 1. qou-pha4: Cumulative swap centrality
    pha4_records = []
    pha4_pass = True
    for q in q_samples:
        G1 = [[q, mp.mpf(1)], [mp.mpf(0), mp.mpf(-1)]]
        G2 = [[mp.mpf(-1), mp.mpf(0)], [q, q]]
        L2 = [[q * q, q], [mp.mpf(0), -q]]
        L3 = [[-q, -q], [mp.mpf(0), q * q]]
        E1 = mat2_add(L2, L3)
        E2 = mat2_mul(L2, L3)
        S1 = [[q * q - q, mp.mpf(0)], [mp.mpf(0), q * q - q]]
        S2 = [[-(q * q * q), mp.mpf(0)], [mp.mpf(0), -(q * q * q)]]

        braid_lhs = mat2_mul(mat2_mul(G1, G2), G1)
        braid_rhs = mat2_mul(mat2_mul(G2, G1), G2)
        res_braid = mat2_sub_norm(braid_lhs, braid_rhs)
        res_comm_L = mat2_sub_norm(mat2_mul(L2, L3), mat2_mul(L3, L2))
        res_E1 = mat2_sub_norm(E1, S1)
        res_E2 = mat2_sub_norm(E2, S2)
        res_E1_G1 = mat2_sub_norm(mat2_mul(E1, G1), mat2_mul(G1, E1))
        res_E1_G2 = mat2_sub_norm(mat2_mul(E1, G2), mat2_mul(G2, E1))
        res_E2_G1 = mat2_sub_norm(mat2_mul(E2, G1), mat2_mul(G1, E2))
        res_E2_G2 = mat2_sub_norm(mat2_mul(E2, G2), mat2_mul(G2, E2))

        max_res = max(
            res_braid,
            res_comm_L,
            res_E1,
            res_E2,
            res_E1_G1,
            res_E1_G2,
            res_E2_G1,
            res_E2_G2,
        )
        ok = bool(max_res < tol)
        pha4_pass = pha4_pass and ok
        pha4_records.append(
            {
                "q": fmt(q),
                "e1Scalar": fmt(q * q - q),
                "e2Scalar": fmt(-(q * q * q)),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    # 2. qou-mhx0: Base-tabloid to diagonal-eigenbasis transition
    mhx0_records = []
    mhx0_pass = True
    for q in q_samples:
        L2 = [[q * q, q], [mp.mpf(0), -q]]
        L3 = [[-q, -q], [mp.mpf(0), q * q]]
        v0 = [mp.mpf(1), mp.mpf(0)]
        v1 = [mp.mpf(-1), q + mp.mpf(1)]

        res_L2_v0 = vec2_sub_norm(mat2_act(L2, v0), [q * q * v0[0], q * q * v0[1]])
        res_L3_v0 = vec2_sub_norm(mat2_act(L3, v0), [-q * v0[0], -q * v0[1]])
        res_L2_v1 = vec2_sub_norm(mat2_act(L2, v1), [-q * v1[0], -q * v1[1]])
        res_L3_v1 = vec2_sub_norm(mat2_act(L3, v1), [q * q * v1[0], q * q * v1[1]])
        det_val = v0[0] * v1[1] - v0[1] * v1[0]
        res_det = abs(det_val - (q + mp.mpf(1)))
        max_res = max(res_L2_v0, res_L3_v0, res_L2_v1, res_L3_v1, res_det)
        ok = bool(max_res < tol and abs(det_val) > tol)
        mhx0_pass = mhx0_pass and ok
        mhx0_records.append(
            {
                "q": fmt(q),
                "transitionDeterminant": fmt(det_val),
                "maxEigenResidual": fmt(max_res),
                "passed": ok,
            }
        )

    # 3. qou-68e1: Consolidated cell-length and content-shift polynomial products
    q68e1_records = []
    q68e1_pass = True
    for q in q_samples:
        Q = q * q
        b1 = mp.mpf(1)
        b2 = mp.mpf(1) + Q
        b3 = mp.mpf(1) + Q + Q * Q
        cell_row3 = b3 * b2 * b1
        cell_21 = b3 * b1 * b1
        unnorm_21 = (mp.mpf(1) - Q * Q * Q) * (mp.mpf(1) - Q) * (mp.mpf(1) - Q)
        factored_21 = ((mp.mpf(1) - Q) ** 3) * cell_21
        poly_row3 = mp.mpf(1) + mp.mpf(2) * Q + mp.mpf(2) * Q * Q + Q * Q * Q
        res1 = abs(unnorm_21 - factored_21)
        res2 = abs(b2 * cell_21 - cell_row3)
        res3 = abs(cell_row3 - poly_row3)
        max_res = max(res1, res2, res3)
        ok = bool(max_res < tol)
        q68e1_pass = q68e1_pass and ok
        q68e1_records.append(
            {
                "Q": fmt(Q),
                "cellProductTwoRow21": fmt(cell_21),
                "cellProductRow3": fmt(cell_row3),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    # 4. qou-zwzd: Additive sum and multiplicative shape product to [3]_Q!
    zwzd_records = []
    zwzd_pass = True
    for q in q_samples:
        Q = q * q
        b1 = mp.mpf(1)
        b2 = mp.mpf(1) + Q
        b3 = mp.mpf(1) + Q + Q * Q
        qfact3 = b1 * b2 * b3
        sum_weighted = mp.mpf(1) + mp.mpf(2) * Q * b2 + Q * Q * Q
        cell_row3 = b3 * b2 * b1
        cell_21 = b3 * b1 * b1
        cell_111 = b3 * b2 * b1
        prod_lhs = b2 * cell_row3 * cell_21 * cell_111
        prod_rhs = qfact3 * qfact3 * qfact3
        res_sum = abs(sum_weighted - qfact3)
        res_prod = abs(prod_lhs - prod_rhs)
        max_res = max(res_sum, res_prod)
        ok = bool(max_res < tol and qfact3 > mp.mpf(0))
        zwzd_pass = zwzd_pass and ok
        zwzd_records.append(
            {
                "Q": fmt(Q),
                "qPolyFactorial3": fmt(qfact3),
                "shapeProductCube": fmt(prod_rhs),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    # 5. qou-xyxc: Curl-difference trace factorization and dim_q(V) = [2]_q
    xyxc_records = []
    xyxc_pass = True
    for q in q_samples:
        a = q * q
        skein_diff = q - (mp.mpf(1) / q)
        curl_diff = a - (mp.mpf(1) / a)
        qdim_two = curl_diff / skein_diff
        expected_qdim_two = q + (mp.mpf(1) / q)
        scaled_lhs = (q * q - mp.mpf(1)) * (q * q + mp.mpf(1))
        scaled_rhs = (q ** 4) - mp.mpf(1)
        res_laurent = abs(qdim_two - expected_qdim_two)
        res_scaled = abs(scaled_lhs - scaled_rhs)
        max_res = max(res_laurent, res_scaled)
        ok = bool(max_res < tol)
        xyxc_pass = xyxc_pass and ok
        xyxc_records.append(
            {
                "q": fmt(q),
                "qDimTwo": fmt(qdim_two),
                "scaledCurlDiff": fmt(scaled_rhs),
                "maxResidual": fmt(max_res),
                "passed": ok,
            }
        )

    all_passed = bool(
        pha4_pass and mhx0_pass and q68e1_pass and zwzd_pass and xyxc_pass
    )

    script_bytes = PROBE_PATH.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    try:
        commit_sha = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
            ).strip()
        )
    except Exception:
        commit_sha = "0" * 40

    payload: dict[str, object] = {
        "probe": "cumulative_swap_centrality_tabloid_transition_cell_product_factorial_curl_trace_probe",
        "beans": ["qou-68e1", "qou-mhx0", "qou-pha4", "qou-xyxc", "qou-zwzd"],
        "precisionDps": 80,
        "scriptPath": str(PROBE_PATH.relative_to(REPO_ROOT))
        if PROBE_PATH.is_relative_to(REPO_ROOT)
        else str(PROBE_PATH.name),
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "timestampUtc": datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ"
        ),
        "allPassed": all_passed,
        "results": {
            "qou_pha4_cumulative_swap_centrality": {
                "passed": pha4_pass,
                "samples": pha4_records,
            },
            "qou_mhx0_base_tabloid_transition": {
                "passed": mhx0_pass,
                "samples": mhx0_records,
            },
            "qou_68e1_consolidated_cell_products": {
                "passed": q68e1_pass,
                "samples": q68e1_records,
            },
            "qou_zwzd_shape_factorial_connection": {
                "passed": zwzd_pass,
                "samples": zwzd_records,
            },
            "qou_xyxc_curl_trace_qdim_two": {
                "passed": xyxc_pass,
                "samples": xyxc_records,
            },
        },
    }
    return payload


def main() -> None:
    payload = run_probe()
    if WITNESS_DIR.parent.exists():
        WITNESS_DIR.mkdir(parents=True, exist_ok=True)
        WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "allPassed": payload["allPassed"],
                "scriptHash": payload["scriptHash"],
                "scriptCommitSha": payload["scriptCommitSha"],
            }
        )
    )
    if not payload["allPassed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
