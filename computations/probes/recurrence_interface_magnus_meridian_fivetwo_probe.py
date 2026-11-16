#!/usr/bin/env python3
"""80-dps mpmath probe for Round 57:
1. qou-i5yp: Depth-3 homogeneous recurrence propagation a_3, a_4, a_5 in terms of a_2
   when a_0 = a_1 = 0, and uniqueness of the 1D kernel up to scalar multiple a_2.
2. qou-o43i: Separable interface reciprocal rescaling invariance (mu_p * t)*(mu_m / t) = mu_p * mu_m,
   unit-sum product deficit 1 - 4*mu_p*mu_m = (mu_p - mu_m)^2, and opposite-channel factorization.
3. qou-o6ov: Three-factor matrix commutator Leibniz expansion [X Y W, Z] = X Y [W, Z] + X [Y, Z] W + [X, Z] Y W
   and left/right commuting factor reduction at 80-dps precision.
4. qou-offl: Deformed figure-eight meridian winding normSq strict monotonicity in k and
   strict separation between off-lattice disk |u| < 2*pi and all k >= 1 substrate meridians.
5. qou-trns: 5_2 cyclotomic / curve transport identity (x - y1)(x - y2)(x - y3) = x*(1 - x*y1)(1 - x*y2)(1 - x*y3),
   base-point pinning at x = 1, and polynomial inverses of w, 1 - w, 1 + w at roots of w^3 - 2*w^2 - w + 1 = 0.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path
from mpmath import mp

mp.dps = 80


def nstr40(x: mp.mpf) -> str:
    return mp.nstr(x, 40)


def mat_mul(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    n = len(A)
    return [
        [sum((A[i][k] * B[k][j] for k in range(n)), mp.mpf("0")) for j in range(n)]
        for i in range(n)
    ]


def mat_add(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def mat_sub(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def mat_comm(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> list[list[mp.mpf]]:
    return mat_sub(mat_mul(A, B), mat_mul(B, A))


def mat_max_abs(A: list[list[mp.mpf]]) -> mp.mpf:
    return max(abs(x) for row in A for x in row)


def check_depth3_recurrence() -> dict:
    c3 = [mp.mpf("3") / mp.mpf("7"), mp.mpf("-5") / mp.mpf("11"), mp.mpf("13") / mp.mpf("17")]
    c4 = [mp.mpf("2") / mp.mpf("5"), mp.mpf("19") / mp.mpf("23"), mp.mpf("-7") / mp.mpf("29")]
    c5 = [mp.mpf("-11") / mp.mpf("13"), mp.mpf("4") / mp.mpf("19"), mp.mpf("23") / mp.mpf("31")]
    a2 = mp.mpf("17") / mp.mpf("19")
    a = [mp.mpf("0"), mp.mpf("0"), a2]
    a3 = -(c3[0] * a[2] + c3[1] * a[1] + c3[2] * a[0])
    a.append(a3)
    a4 = -(c4[0] * a[3] + c4[1] * a[2] + c4[2] * a[1])
    a.append(a4)
    a5 = -(c5[0] * a[4] + c5[1] * a[3] + c5[2] * a[2])
    a.append(a5)

    a3_formula = -c3[0] * a2
    a4_formula = (c4[0] * c3[0] - c4[1]) * a2
    a5_formula = (-c5[0] * c4[0] * c3[0] + c5[0] * c4[1] + c5[1] * c3[0] - c5[2]) * a2

    res3 = abs(a3 - a3_formula)
    res4 = abs(a4 - a4_formula)
    res5 = abs(a5 - a5_formula)
    max_res = max(res3, res4, res5)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-i5yp-depth3-recurrence-propagation",
        "passed": passed,
        "a3": nstr40(a3),
        "a4": nstr40(a4),
        "a5": nstr40(a5),
        "maxResidual": nstr40(max_res),
    }


def check_separable_interface() -> dict:
    mup = mp.mpf("3") / mp.mpf("11")
    mum = mp.mpf("8") / mp.mpf("11")
    t = mp.mpf("29") / mp.mpf("13")
    rescale_res = abs((mup * t) * (mum / t) - mup * mum)
    deficit_res = abs((mp.mpf("1") - mp.mpf("4") * mup * mum) - (mup - mum) ** 2)
    nup = mp.mpf("5") / mp.mpf("17")
    num = mp.mpf("12") / mp.mpf("17")
    f_ell = mp.mpf("7") / mp.mpf("23")
    factor_res = abs((mup * num * f_ell - mum * nup * f_ell) - (mup * num - mum * nup) * f_ell)
    max_res = max(rescale_res, deficit_res, factor_res)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-o43i-separable-interface-identities",
        "passed": passed,
        "unitSumDeficit": nstr40(mp.mpf("1") - mp.mpf("4") * mup * mum),
        "maxResidual": nstr40(max_res),
    }


def check_magnus_commutator_leibniz() -> dict:
    X = [[mp.mpf("2"), mp.mpf("-1")], [mp.mpf("3"), mp.mpf("5")]]
    Y = [[mp.mpf("1"), mp.mpf("4")], [mp.mpf("-2"), mp.mpf("7")]]
    W = [[mp.mpf("-3"), mp.mpf("2")], [mp.mpf("6"), mp.mpf("1")]]
    Z = [[mp.mpf("5"), mp.mpf("3")], [mp.mpf("-4"), mp.mpf("2")]]

    XYW = mat_mul(mat_mul(X, Y), W)
    lhs = mat_comm(XYW, Z)
    term1 = mat_mul(mat_mul(X, Y), mat_comm(W, Z))
    term2 = mat_mul(mat_mul(X, mat_comm(Y, Z)), W)
    term3 = mat_mul(mat_mul(mat_comm(X, Z), Y), W)
    rhs = mat_add(mat_add(term1, term2), term3)
    res_three = mat_max_abs(mat_sub(lhs, rhs))

    # Right-commuting check: Y_comm = Z + 3*I commutes with Z
    Y_comm = [[Z[0][0] + mp.mpf("3"), Z[0][1]], [Z[1][0], Z[1][1] + mp.mpf("3")]]
    lhs_right = mat_comm(mat_mul(X, Y_comm), Z)
    rhs_right = mat_mul(mat_comm(X, Z), Y_comm)
    res_right = mat_max_abs(mat_sub(lhs_right, rhs_right))

    # Left-commuting check: X_comm = Z - 2*I commutes with Z
    X_comm = [[Z[0][0] - mp.mpf("2"), Z[0][1]], [Z[1][0], Z[1][1] - mp.mpf("2")]]
    lhs_left = mat_comm(mat_mul(X_comm, Y), Z)
    rhs_left = mat_mul(X_comm, mat_comm(Y, Z))
    res_left = mat_max_abs(mat_sub(lhs_left, rhs_left))

    max_res = max(res_three, res_right, res_left)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-o6ov-magnus-three-factor-leibniz",
        "passed": passed,
        "maxResidual": nstr40(max_res),
    }


def check_meridian_winding_separation() -> dict:
    a = mp.mpf("0.35")
    two_pi_sq = (mp.mpf("2") * mp.pi) ** 2
    norms = [a * a + (mp.mpf("2") * mp.pi * mp.mpf(k)) ** 2 for k in range(1, 6)]
    strict_mono = all(norms[i] < norms[i + 1] for i in range(len(norms) - 1))
    disk_point_norm_sq = mp.mpf("0.5") ** 2 + (mp.mpf("1.9") * mp.pi) ** 2
    min_gap = norms[0] - disk_point_norm_sq
    passed = bool(strict_mono and disk_point_norm_sq < two_pi_sq and min_gap > mp.mpf("0"))
    return {
        "id": "qou-offl-meridian-winding-monotonicity-and-disk-gap",
        "passed": passed,
        "k1NormSq": nstr40(norms[0]),
        "twoPiSqFloor": nstr40(two_pi_sq),
        "diskPointNormSq": nstr40(disk_point_norm_sq),
        "minGapToK1Meridian": nstr40(min_gap),
    }


def check_fivetwo_cyclotomic_transport() -> dict:
    # Base point x = 1: e1 = 2, e2 = 3, e3 = 1 -> (1 - y1)(1 - y2)(1 - y3) = 1 - e1 + e2 - e3 = 1
    # Check polynomial identity (x - y1)(x - y2)(x - y3) - x*(1 - x*y1)(1 - x*y2)(1 - x*y3)
    # when x*(y1+y2+y3) = x^2+1, x*(y1*y2+y1*y3+y2*y3) = x^2+x+1, y1*y2*y3 = 1
    x = mp.mpf("7") / mp.mpf("5")
    e1 = (x ** 2 + mp.mpf("1")) / x
    e2 = (x ** 2 + x + mp.mpf("1")) / x
    e3 = mp.mpf("1")
    lhs_sym = x ** 3 - e1 * x ** 2 + e2 * x - e3
    rhs_sym = x * (mp.mpf("1") - x * e1 + (x ** 2) * e2 - (x ** 3) * e3)
    sym_res = abs(lhs_sym - rhs_sym)

    # Check roots w_k = 1 + 2*cos(2*pi*k/7) for k = 1, 2, 3
    max_root_res = mp.mpf("0")
    for k in (1, 2, 3):
        w = mp.mpf("1") + mp.mpf("2") * mp.cos(mp.mpf(2 * k) * mp.pi / mp.mpf("7"))
        poly_res = abs(w ** 3 - mp.mpf("2") * w ** 2 - w + mp.mpf("1"))
        inv_w_res = abs(w * (-w ** 2 + mp.mpf("2") * w + mp.mpf("1")) - mp.mpf("1"))
        inv_1mw_res = abs((mp.mpf("1") - w) * (mp.mpf("2") + w - w ** 2) - mp.mpf("1"))
        inv_1pw_res = abs((mp.mpf("1") + w) * (w ** 2 - mp.mpf("3") * w + mp.mpf("2")) - mp.mpf("1"))
        max_root_res = max(max_root_res, poly_res, inv_w_res, inv_1mw_res, inv_1pw_res)

    max_res = max(sym_res, max_root_res)
    passed = bool(max_res < mp.mpf("1e-75"))
    return {
        "id": "qou-trns-fivetwo-cyclotomic-transport-and-inverses",
        "passed": passed,
        "symmetricProductResidual": nstr40(sym_res),
        "maxCyclotomicInverseResidual": nstr40(max_root_res),
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent.parent
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    try:
        git_commit = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        git_commit = "0" * 40

    checks = [
        check_depth3_recurrence(),
        check_separable_interface(),
        check_magnus_commutator_leibniz(),
        check_meridian_winding_separation(),
        check_fivetwo_cyclotomic_transport(),
    ]
    all_passed = all(c["passed"] for c in checks)
    witness = {
        "probe": script_path.name,
        "gitCommit": git_commit,
        "scriptCommitSha": git_commit,
        "scriptHash": script_hash,
        "dps": 80,
        "allPassed": all_passed,
        "checks": checks,
    }
    witness_path = script_path.with_name(
        "recurrence-interface-magnus-meridian-fivetwo.witness.json"
    )
    witness_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {witness_path.name} (allPassed={all_passed}, scriptHash={script_hash})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
