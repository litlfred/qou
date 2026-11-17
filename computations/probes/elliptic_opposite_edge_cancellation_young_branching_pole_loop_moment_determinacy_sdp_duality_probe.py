#!/usr/bin/env python3
"""80-dps mpmath numerical verification probe for QOU Round 62:
- qou-nuxb: Opposite-edge cancellation of contour integrals on the period parallelogram
- qou-vvk7: Hook-length branching ratio and box-removal sum identity for partitions
- qou-wdgz: Logarithmic derivative contour integral count of interior poles minus zeros
- qou-x1rm: Three-node Vandermonde moment determinacy and symmetric-cone moment positivity
- qou-yc05: Semidefinite trace inner product duality gap and rank-one complementarity
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from mpmath import mp, mpc, mpf

mp.dps = 80


def fmt(x: mpf) -> str:
    return mp.nstr(x, 30)


def check_nuxb_elliptic_opposite_edge_cancellation() -> dict:
    """Verify doubly periodic opposite-edge contour integral cancellation using a
    trigonometric doubly periodic surrogate f(z) = cos(2*pi*z/omega1) * sin(2*pi*z/omega2)
    on a rectangular period parallelogram [z0, z0+omega1] x [z0, z0+omega2].
    """
    omega1 = mpf("1.7")
    omega2 = mpc("0.3", "1.3")
    z0 = mpc("0.2", "0.15")

    def f(z: mpc) -> mpc:
        # Doubly periodic in omega1 and omega2 via lattice coordinates (s, t):
        # z = s * omega1 + t * omega2
        det = omega1.real * omega2.imag - omega1.imag * omega2.real
        s = (z.real * omega2.imag - z.imag * omega2.real) / det
        t = (omega1.real * z.imag - omega1.imag * z.real) / det
        return mp.cos(2 * mp.pi * s) + mpc(0, 1) * mp.sin(2 * mp.pi * t) + mp.cos(
            2 * mp.pi * (s + t)
        )

    bottom = mp.quad(lambda u: f(z0 + u * omega1) * omega1, [0, 1])
    right = mp.quad(lambda u: f(z0 + omega1 + u * omega2) * omega2, [0, 1])
    top = mp.quad(lambda u: -f(z0 + omega2 + (1 - u) * omega1) * omega1, [0, 1])
    left = mp.quad(lambda u: -f(z0 + (1 - u) * omega2) * omega2, [0, 1])

    loop_sum = bottom + right + top + left
    opp_horiz = abs(bottom + top)
    opp_vert = abs(right + left)
    loop_err = abs(loop_sum)

    passed = bool(
        opp_horiz < mpf("1e-65")
        and opp_vert < mpf("1e-65")
        and loop_err < mpf("1e-65")
    )
    return {
        "beanId": "qou-nuxb",
        "oppositeHorizontalCancellationError": fmt(opp_horiz),
        "oppositeVerticalCancellationError": fmt(opp_vert),
        "closedParallelogramLoopResidual": fmt(loop_err),
        "passed": passed,
    }


def check_vvk7_young_diagram_hook_branching() -> dict:
    """Verify hook-length dimension formula f^lambda = n! / prod h(i,j) and
    branching recurrence f^lambda = sum_{mu <- lambda} f^mu for lambda = (4, 2, 1)
    of size n = 7, where corners remove to (3, 2, 1), (4, 1, 1), and (4, 2).
    """
    # Partition lambda = (4, 2, 1), size 7
    # Hook lengths of (4, 2, 1):
    # row 1: 6, 4, 2, 1
    # row 2: 3, 1
    # row 3: 1
    hooks_421 = [6, 4, 2, 1, 3, 1, 1]
    prod_421 = mpf(1)
    for h in hooks_421:
        prod_421 *= h
    f_421 = mp.factorial(7) / prod_421  # 5040 / 144 = 35

    # Corner 1 removed: (3, 2, 1), size 6; hooks: (5,3,1; 2,1; 1) -> prod = 30 -> 720/30 = 24?
    # Wait: conjugate of (3,2,1) is (3,2,1):
    # (1,1): 3+3-1=5; (1,2): 3+2-2=3; (1,3): 3+1-3=1
    # (2,1): 2+3-2=3; (2,2): 2+2-3=1
    # (3,1): 1+3-3=1
    # Product = 5*3*1*3*1*1 = 45 -> 720 / 45 = 16
    f_321 = mp.factorial(6) / mpf(45)

    # Corner 2 removed: (4, 1, 1), size 6; conjugate is (3, 1, 1, 1)
    # hooks row 1: 6, 3, 2, 1; row 2: 2; row 3: 1 -> prod = 72 -> 720 / 72 = 10
    f_411 = mp.factorial(6) / mpf(72)

    # Corner 3 removed: (4, 2), size 6; conjugate is (2, 2, 1, 1)
    # hooks row 1: 5, 4, 2, 1; row 2: 2, 1 -> prod = 80 -> 720 / 80 = 9
    f_42 = mp.factorial(6) / mpf(80)

    branch_sum = f_321 + f_411 + f_42
    residual = abs(f_421 - branch_sum)

    # Normalized hook ratio sum: sum (prod_421 / (7 * prod_mu)) = (144/315 + 144/504 + 144/560) = 1
    ratio_sum = (prod_421 / (mpf(7) * mpf(45))) + (prod_421 / (mpf(7) * mpf(72))) + (
        prod_421 / (mpf(7) * mpf(80))
    )
    ratio_err = abs(ratio_sum - mpf(1))

    passed = bool(
        f_421 == mpf(35)
        and residual == mpf(0)
        and ratio_err < mpf("1e-75")
    )
    return {
        "beanId": "qou-vvk7",
        "fLambda_4_2_1": fmt(f_421),
        "branchingChildren_321_411_42": [fmt(f_321), fmt(f_411), fmt(f_42)],
        "branchingRecurrenceResidual": fmt(residual),
        "normalizedHookRatioSumResidual": fmt(ratio_err),
        "passed": passed,
    }


def check_wdgz_pole_zero_loop_winding() -> dict:
    """Verify argument principle contour integral (1/(2*pi*i)) oint (f'(z)/f(z)) dz = Z - P
    for meromorphic f(z) = (z - z1)^2 / ((z - p1)*(z - p2)^3) inside |z| = R = 2.
    Interior zeros: z1 = 0.25 + 0.15i (mult 2) -> Z = 2.
    Interior poles: p1 = -0.3 + 0.2i (mult 1), p2 = 0.1 - 0.35i (mult 3) -> P = 4.
    Exterior zero: z_ext = 3.5 + 1.0i (mult 1, outside |z|=2).
    Net winding count = Z - P = 2 - 4 = -2.
    """
    z1 = mpc("0.25", "0.15")
    p1 = mpc("-0.3", "0.2")
    p2 = mpc("0.1", "-0.35")
    z_ext = mpc("3.5", "1.0")
    radius = mpf("2.0")

    def log_deriv(z: mpc) -> mpc:
        return (
            mpf(2) / (z - z1)
            + mpf(1) / (z - z_ext)
            - mpf(1) / (z - p1)
            - mpf(3) / (z - p2)
        )

    def integrand(theta: mpf) -> mpc:
        z = radius * mp.exp(mpc(0, 1) * theta)
        dz_dtheta = mpc(0, 1) * z
        return log_deriv(z) * dz_dtheta / (2 * mp.pi * mpc(0, 1))

    winding = mp.quad(integrand, [0, 2 * mp.pi])
    expected = mpf(-2)
    err = abs(winding - expected)

    passed = bool(err < mpf("1e-60"))
    return {
        "beanId": "qou-wdgz",
        "interiorZeroMultiplicitySum": "2",
        "interiorPoleMultiplicitySum": "4",
        "expectedWindingCount": fmt(expected),
        "computedWindingReal": fmt(winding.real),
        "computedWindingImag": fmt(winding.imag),
        "windingResidual": fmt(err),
        "passed": passed,
    }


def check_x1rm_moment_determinacy_vandermonde() -> dict:
    """Verify 3-node Vandermonde moment determinacy and Hankel quadratic form
    for distinct nodes (-2, 1, 3) and positive weights w = (3, 5, 2).
    """
    x0, x1, x2 = mpf(-2), mpf(1), mpf(3)
    w0, w1, w2 = mpf(3), mpf(5), mpf(2)

    m0 = w0 + w1 + w2
    m1 = w0 * x0 + w1 * x1 + w2 * x2
    m2 = w0 * x0**2 + w1 * x1**2 + w2 * x2**2

    # Recover w from (m0, m1, m2) via Lagrange fundamental polynomials:
    rec_w0 = (m2 - (x1 + x2) * m1 + x1 * x2 * m0) / ((x0 - x1) * (x0 - x2))
    rec_w1 = (m2 - (x0 + x2) * m1 + x0 * x2 * m0) / ((x1 - x0) * (x1 - x2))
    rec_w2 = (m2 - (x0 + x1) * m1 + x0 * x1 * m0) / ((x2 - x0) * (x2 - x1))

    rec_err = max(abs(rec_w0 - w0), abs(rec_w1 - w1), abs(rec_w2 - w2))

    # Hankel quadratic form c^T H c = sum_k w_k (c0 + c1 x_k)^2 for c = (4, -3):
    c0, c1 = mpf(4), mpf(-3)
    hankel_quad = c0**2 * m0 + 2 * c0 * c1 * m1 + c1**2 * m2
    sum_of_squares = (
        w0 * (c0 + c1 * x0) ** 2
        + w1 * (c0 + c1 * x1) ** 2
        + w2 * (c0 + c1 * x2) ** 2
    )
    quad_err = abs(hankel_quad - sum_of_squares)

    passed = bool(rec_err < mpf("1e-75") and quad_err < mpf("1e-75") and hankel_quad > 0)
    return {
        "beanId": "qou-x1rm",
        "moments_m0_m1_m2": [fmt(m0), fmt(m1), fmt(m2)],
        "weightRecoveryMaxError": fmt(rec_err),
        "hankelQuadraticFormValue": fmt(hankel_quad),
        "hankelSumOfSquaresResidual": fmt(quad_err),
        "passed": passed,
    }


def check_yc05_sdp_trace_duality_complementarity() -> dict:
    """Verify weak SDP duality gap decomposition and rank-one symmetric cone
    trace inner product identity tr((u u^T)(v v^T)) = (u^T v)^2 >= 0.
    """
    u1, u2 = mpf(5), mpf(-3)
    v1, v2 = mpf(3), mpf(5)  # Orthogonal to u: u^T v = 15 - 15 = 0

    # Rank-one PSD matrices X = u u^T, S = v v^T
    x11, x12, x22 = u1 * u1, u1 * u2, u2 * u2
    s11, s12, s22 = v1 * v1, v1 * v2, v2 * v2

    trace_xs = x11 * s11 + 2 * x12 * s12 + x22 * s22
    dot_uv = u1 * v1 + u2 * v2
    comp_err = abs(trace_xs - dot_uv**2)

    # Non-orthogonal pair v_pos = (2, -1) -> dot = 13 -> trace = 169
    vp1, vp2 = mpf(2), mpf(-1)
    sp11, sp12, sp22 = vp1 * vp1, vp1 * vp2, vp2 * vp2
    trace_x_sp = x11 * sp11 + 2 * x12 * sp12 + x22 * sp22
    dot_u_vp = u1 * vp1 + u2 * vp2
    pos_err = abs(trace_x_sp - dot_u_vp**2)

    # Primal-dual weak duality identity with primal Objective <C, X>, dual b^T y:
    # Let A1 = [[1, 0], [0, 2]], A2 = [[0, 1], [1, 1]], y = (4, -3), S = v_pos v_pos^T
    # C = y1 A1 + y2 A2 + S
    y1, y2 = mpf(4), mpf(-3)
    b1 = x11 * 1 + 2 * x12 * 0 + x22 * 2
    b2 = x11 * 0 + 2 * x12 * 1 + x22 * 1
    c11 = y1 * 1 + y2 * 0 + sp11
    c12 = y1 * 0 + y2 * 1 + sp12
    c22 = y1 * 2 + y2 * 1 + sp22

    primal_obj = c11 * x11 + 2 * c12 * x12 + c22 * x22
    dual_obj = b1 * y1 + b2 * y2
    duality_gap = primal_obj - dual_obj
    gap_err = abs(duality_gap - trace_x_sp)

    passed = bool(
        comp_err == mpf(0)
        and trace_xs == mpf(0)
        and pos_err == mpf(0)
        and trace_x_sp == mpf(169)
        and gap_err == mpf(0)
    )
    return {
        "beanId": "qou-yc05",
        "orthogonalTraceInnerProduct": fmt(trace_xs),
        "orthogonalComplementarityResidual": fmt(comp_err),
        "positiveRankOneTraceInnerProduct": fmt(trace_x_sp),
        "weakDualityGap": fmt(duality_gap),
        "weakDualityIdentityResidual": fmt(gap_err),
        "passed": passed,
    }


def main() -> None:
    script_path = Path(__file__).resolve()
    script_bytes = script_path.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]

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

    checks = [
        check_nuxb_elliptic_opposite_edge_cancellation(),
        check_vvk7_young_diagram_hook_branching(),
        check_wdgz_pole_zero_loop_winding(),
        check_x1rm_moment_determinacy_vandermonde(),
        check_yc05_sdp_trace_duality_complementarity(),
    ]
    all_passed = all(c["passed"] for c in checks)

    witness = {
        "probe": "elliptic-opposite-edge-cancellation-young-branching-pole-loop-moment-determinacy-sdp-duality",
        "beans": ["qou-nuxb", "qou-vvk7", "qou-wdgz", "qou-x1rm", "qou-yc05"],
        "precisionDps": "80",
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": checks,
    }

    out_path = script_path.with_name(
        "elliptic-opposite-edge-cancellation-young-branching-pole-loop-moment-determinacy-sdp-duality.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.name}: allPassed={all_passed}, scriptHash={script_hash}")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
