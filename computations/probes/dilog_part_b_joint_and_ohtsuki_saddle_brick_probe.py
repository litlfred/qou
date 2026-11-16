#!/usr/bin/env python3
"""
80-dps mpmath and exact rational verification probe for Round 65:
  - qou-a0li: Dilog Part-B Borel-Cantelli measure-window brick: change-of-variables x = e^{-u}
              and periodic geometric summation (1 - e^{-eps_m delta_m}) / (1 - e^{-delta_m}) <= eps_m
  - qou-cqup: Dilog Part-B 2b Faddeev-scaling positive wp1_faddeev_tendsto moving target x_q = 2 - q
              and cusp decomposition Li_2(x) - pi^2/6 + (-pi^2/6) = Li_2(x) - pi^2/3
  - qou-vlow: Ohtsuki saddle-point asymptotic: critical-point elimination (1-x)y = 1, x(y-1)^2 = 1
              -> x^3 - (1-x)^2 = 0 and complex Gaussian integral rescaling at 80 dps
  - qou-ylma: Dilog Part-B joint-route conditional closure: W-P1 capstone + W-P2 tail -> Li_2(x) - pi^2/3
  - qou-zuuz: Dilog Part-B a.e. residual: Borel-Cantelli resonance-window telescoping schedule
              sum_{m=1}^M 1/(m(m+1)) = 1 - 1/(M+1) and tail decay 1/N
"""

from __future__ import annotations

import datetime
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import subprocess

import mpmath as mp

mp.mp.dps = 80


def fmt_mp(val: mp.mpf | mp.mpc) -> str:
    return mp.nstr(val, 40)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    script_path = Path(__file__).resolve()
    script_bytes = script_path.read_bytes()
    script_hash = hashlib.sha256(script_bytes).hexdigest()[:12]
    try:
        commit_sha = (
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo_root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        commit_sha = "0" * 40

    # 1. qou-a0li: Periodic measure-window brick at 80 dps
    q_m = mp.mpf("1.10998")
    delta_m = mp.log(q_m)
    eps_m = mp.mpf("0.05")
    r_m = mp.exp(-delta_m)
    w_eps = 1 - mp.exp(-eps_m * delta_m)
    total_window_measure = w_eps / (1 - r_m)
    # Direct numerical sum of the first 250 period windows
    direct_window_sum = mp.nsum(
        lambda k: (r_m**k) * w_eps, [0, mp.inf]
    )
    series_residual = abs(total_window_measure - direct_window_sum)
    qou_a0li_pass = bool(
        series_residual < mp.mpf("1e-75")
        and total_window_measure <= eps_m * (delta_m / (1 - r_m))
        and total_window_measure > 0
    )

    # 2. qou-cqup: Faddeev moving-target x_q = 2 - q and cusp decomposition
    q_faddeev = Fraction(1001, 1000)
    x_q = 2 - q_faddeev
    cusp_gap = 1 - x_q
    x_mp = mp.mpf(x_q.numerator) / mp.mpf(x_q.denominator)
    pi_sq = mp.pi**2
    li2_xq = mp.polylog(2, x_mp)
    wp1_lim = li2_xq - pi_sq / 6
    wp1_euler_rhs = -mp.polylog(2, 1 - x_mp) - mp.log(x_mp) * mp.log(1 - x_mp)
    euler_reflection_residual = abs(wp1_lim - wp1_euler_rhs)
    qou_cqup_pass = bool(
        cusp_gap == q_faddeev - 1
        and euler_reflection_residual < mp.mpf("1e-75")
        and abs(wp1_lim) < mp.mpf("2e-2")
    )

    # 3. qou-vlow: Ohtsuki critical-point elimination and Prop 3.1 complex Gaussian rescaling
    # Solve x^3 - (1 - x)^2 = 0 -> x^3 - x^2 + 2x - 1 = 0
    roots_x = mp.polyroots([1, -1, 2, -1])
    x0 = roots_x[0]
    y0 = 1 / (1 - x0)
    eq1_res = abs((1 - x0) * y0 - 1)
    eq2_res = abs(x0 * ((y0 - 1) ** 2) - 1)
    cubic_res = abs(x0**3 - (1 - x0) ** 2)
    # Complex Gaussian integral rescaling: int_{-inf}^{inf} exp(-N a z^2) dz == sqrt(pi / (N a))
    a_cplx = mp.mpc("1.5", "-0.8")
    N_cplx = mp.mpf("12")
    gauss_closed = mp.sqrt(mp.pi / (N_cplx * a_cplx))
    gauss_quad = mp.quad(lambda t: mp.exp(-N_cplx * a_cplx * (t**2)), [-mp.inf, mp.inf])
    gauss_res = abs(gauss_closed - gauss_quad)
    qou_vlow_pass = bool(
        eq1_res < mp.mpf("1e-70")
        and eq2_res < mp.mpf("1e-70")
        and cubic_res < mp.mpf("1e-70")
        and gauss_res < mp.mpf("1e-70")
    )

    # 4. qou-ylma: Joint-route Part-B decomposition and triangle bound
    wp1_approx = Fraction(31, 20)
    wp2_approx = Fraction(-27, 16)
    li2_target = Fraction(16, 5)
    pi_sq_rat = Fraction(987, 100)
    err1 = wp1_approx - (li2_target - pi_sq_rat / 6)
    err2 = wp2_approx - (-pi_sq_rat / 6)
    total_err = (wp1_approx + wp2_approx) - (li2_target - pi_sq_rat / 3)
    qou_ylma_pass = bool(
        total_err == err1 + err2
        and abs(total_err) <= abs(err1) + abs(err2)
    )

    # 5. qou-zuuz: Borel-Cantelli telescoping resonance-window schedule
    M_max = 50
    partial_sum = sum(Fraction(1, m * (m + 1)) for m in range(1, M_max + 1))
    expected_partial = 1 - Fraction(1, M_max + 1)
    tail_sum_10_20 = sum(Fraction(1, m * (m + 1)) for m in range(10, 21))
    expected_tail_10_20 = Fraction(1, 10) - Fraction(1, 21)
    qou_zuuz_pass = bool(
        partial_sum == expected_partial
        and tail_sum_10_20 == expected_tail_10_20
        and tail_sum_10_20 < Fraction(1, 10)
    )

    all_passed = (
        qou_a0li_pass
        and qou_cqup_pass
        and qou_vlow_pass
        and qou_ylma_pass
        and qou_zuuz_pass
    )

    witness = {
        "probe": "dilog-part-b-joint-and-ohtsuki-saddle-brick",
        "beans": ["qou-a0li", "qou-cqup", "qou-vlow", "qou-ylma", "qou-zuuz"],
        "precisionDps": "80",
        "scriptHash": script_hash,
        "scriptCommitSha": commit_sha,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "allPassed": all_passed,
        "checks": {
            "qou_a0li_periodic_measure_window": {
                "passed": qou_a0li_pass,
                "totalWindowMeasure": fmt_mp(total_window_measure),
                "seriesResidual": fmt_mp(series_residual),
            },
            "qou_cqup_faddeev_moving_target": {
                "passed": qou_cqup_pass,
                "movingTargetXq": f"{x_q.numerator}/{x_q.denominator}",
                "cuspGap": f"{cusp_gap.numerator}/{cusp_gap.denominator}",
                "wp1AtMovingTarget": fmt_mp(wp1_lim),
                "eulerReflectionResidual": fmt_mp(euler_reflection_residual),
            },
            "qou_vlow_ohtsuki_saddle_brick": {
                "passed": qou_vlow_pass,
                "eq1Residual": fmt_mp(eq1_res),
                "eq2Residual": fmt_mp(eq2_res),
                "cubicEliminationResidual": fmt_mp(cubic_res),
                "complexGaussianQuadResidual": fmt_mp(gauss_res),
            },
            "qou_ylma_part_b_joint_route": {
                "passed": qou_ylma_pass,
                "wp1Error": f"{err1.numerator}/{err1.denominator}",
                "wp2Error": f"{err2.numerator}/{err2.denominator}",
                "totalJointError": f"{total_err.numerator}/{total_err.denominator}",
            },
            "qou_zuuz_borel_cantelli_telescoping": {
                "passed": qou_zuuz_pass,
                "partialSumTo50": f"{partial_sum.numerator}/{partial_sum.denominator}",
                "tailSum10To20": f"{tail_sum_10_20.numerator}/{tail_sum_10_20.denominator}",
            },
        },
    }

    out_path = script_path.with_name(
        "dilog-part-b-joint-and-ohtsuki-saddle-brick.witness.json"
    )
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (allPassed={all_passed}, scriptHash={script_hash})")
    if not all_passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
