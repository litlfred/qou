#!/usr/bin/env python3
"""qbeta_ck_q_difference_kernel_on_corrected_probe.py — probe 6.c
from the c_k generating-function scoping doc.

PR #1824 follow-on. Probe 6.a (commit 4e9d27f31d) confirmed the
generating-function hypothesis at c_2, c_3: the leading-order
bias correction Δc_k = c_{k+1}·u recovers c_2 = -1 (canonical)
and c_3 = -2 (J_Hopf at q=1) to ppm precision.

This probe extends: apply the bias correction to the FULL c_k
ladder, then test whether the corrected c_k satisfy a depth-2
LINEAR RECURRENCE:

    c_{k+1}_corr = α · c_k_corr + β · c_{k-1}_corr

PR #1786's depth-d sweep REFUTED the constant-kernel recurrence
on the RAW SDP-extracted c_k. But the raw c_k were biased by
the truncation cross-talk — they don't represent the algebraic
ladder coefficients. The CORRECTED c_k_corr might satisfy a
clean recurrence that the raw values do not.

**Why this matters**: if the corrected c_k_corr satisfy a depth-2
recurrence with constant (or q-dependent) kernel, the generating
function F(u) is a rational function

    F(u) = (something) / (1 - α u - β u²)

and the kernel (α, β) IS the generating function's structural
data — exactly the "kernel R / element F(q) open keystone" of
the ck-dk registry §3.

Methodology:
  1. Read raw c_k from witness.
  2. Apply leading bias correction c_k_corr = c_k - c_{k+1} · u.
  3. For each sliding window k ∈ [k_min, k_max-2], solve
     2x2 system:
       (c_k     c_{k-1}) (α)   (c_{k+1})
       (c_{k+1} c_k    ) (β) = (c_{k+2})
     for (α, β) at that window.
  4. Report spread of (α, β) across windows.
  5. Verdict: CONSTANT kernel passes if spread < 1%, FAILS otherwise.
  6. If passes, report the inferred generating function form.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402


def u_subst_from_canonical_q0() -> mp.mpf:
    """u = b·ℏ_q² rebuilt from the canonical q₀ PINNING, closed form only.

    The second route to the `U_SUBST` literal below. Nothing here reads that
    literal and nothing there reads the pinning: b = √((h²+3)/(h²+4)) with
    h = q − q⁻¹, and ℏ_q² = (1 − q⁻¹)², both at
    `q_parameter.Q_50_DIGIT_STR`. U_SUBST IS the bias correction
    (c_k_corr = c_k − c_{k+1}·u), so a drift in it moves every kernel fit.
    """
    from q_parameter import Q_50_DIGIT_STR  # noqa: E402 — local: 2nd route only
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    return mp.sqrt((h ** 2 + 3) / (h ** 2 + 4)) * (1 - 1 / q) ** 2


def main() -> int:
    U_SUBST = mp.mpf("0.00852")
    # Half a unit in the last place of the 3-significant-figure literal above:
    # the coarsest tolerance at which "0.00852 is the correct rounding of
    # b·ℏ_q²" is still a claim that can fail. Fixed by the literal's own
    # precision, not fitted to the current gap.
    U_SUBST_LITERAL_HALF_ULP = "5e-6"
    u_closed = u_subst_from_canonical_q0()
    u_literal_dev = abs(U_SUBST - u_closed)

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-ck-q-difference-kernel-on-corrected-probe",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Probe 6.c: test depth-2 recurrence on the bias-corrected "
        "c_k_corr (from probe 6.a). PR #1786 refuted the constant-"
        "kernel recurrence on the RAW c_k, but the raw values are "
        "biased. If c_k_corr satisfies a depth-2 recurrence with "
        "constant kernel, the generating function F(u) is rational "
        "with denominator (1 - α u - β u²)."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Probe 6.c — depth-2 recurrence on bias-corrected c_k")
    print("=" * 78)
    print()

    print(f"  U_SUBST literal            = {mp.nstr(U_SUBST, 12)}")
    print(f"  b·ℏ_q² at the canonical q₀ = {mp.nstr(u_closed, 20)}"
          f"   |Δ| = {mp.nstr(u_literal_dev, 6)}")
    print()

    witness_path = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    with open(witness_path, encoding="utf-8") as f:
        w = json.load(f)
    ck_raw_str = w["data"]["c_k_extracted_50dps"]

    # Every rung may be `null`. The SDP extractor nulls a rung it could not
    # resolve; its `why_unresolved_rungs_are_null` note says that once
    # R_k − 1 stops dropping it IS the model's accuracy floor, and
    # c_k := (R_k−1)/u^k then manufactures a geometric blow-up of ratio
    # exactly 1/u. Fail with that in hand rather than `cannot create mpf
    # from None` — a recurrence fitted to manufactured numbers would not
    # look broken, it would look refuted.
    missing = sorted((k for k, v in ck_raw_str.items() if v is None),
                     key=lambda k: int(k.replace("c_", "")))
    if missing:
        raise SystemExit(
            f"BLOCKED: {witness_path.name} has no extracted value for "
            f"{', '.join(missing)} — those rungs are recorded unresolved. "
            f"Probe 6.c's bias correction and depth-2 fit both need them; "
            f"re-derive the c_k before re-running."
        )

    ck = {}
    for k_str, v in ck_raw_str.items():
        k = int(k_str.replace("c_", "")) if k_str.startswith("c_") else int(k_str)
        ck[k] = mp.mpf(v)

    # Apply leading bias correction
    ck_corr = {}
    for k in sorted(ck.keys()):
        if (k + 1) in ck:
            ck_corr[k] = ck[k] - ck[k + 1] * U_SUBST
        else:
            ck_corr[k] = ck[k]
    k_max = max(ck_corr.keys())
    k_min = min(ck_corr.keys())

    print(f"  Bias-corrected c_k_corr (from probe 6.a):")
    for k in sorted(ck_corr.keys()):
        print(f"    c_{k}_corr = {mp.nstr(ck_corr[k], 12)}")
    print()

    print(f"  Sliding-window depth-2 recurrence fit:")
    print(f"  c_{{k+1}}_corr = α · c_k_corr + β · c_{{k-1}}_corr")
    print()
    print(f"  {'window k':>8} {'α':>14} {'β':>14} {'residual':>12}")
    print(f"  {'-'*8} {'-'*14} {'-'*14} {'-'*12}")

    alphas = []
    betas = []
    windows = []
    for k in range(k_min + 1, k_max - 1):
        # Solve [[c_k, c_{k-1}], [c_{k+1}, c_k]] · [α, β]ᵀ = [c_{k+1}, c_{k+2}]
        A = mp.matrix([[ck_corr[k], ck_corr[k - 1]],
                       [ck_corr[k + 1], ck_corr[k]]])
        b_vec = mp.matrix([[ck_corr[k + 1]], [ck_corr[k + 2]]])
        try:
            sol = mp.lu_solve(A, b_vec)
            alpha, beta = sol[0, 0], sol[1, 0]
        except (ValueError, ZeroDivisionError):
            continue
        # Residual: how well does the recurrence FORWARD-predict the
        # next coefficient beyond the fit window?
        # At the boundary (no c_{k+3} available) the residual is NOT
        # computable — use a None sentinel (NOT 0, which would read as
        # a perfect fit; per Copilot review on PR #1824).
        if (k + 3) in ck_corr:
            c_k_plus_3_pred = alpha * ck_corr[k + 2] + beta * ck_corr[k + 1]
            residual = mp.fabs((c_k_plus_3_pred - ck_corr[k + 3])
                               / ck_corr[k + 3]) if ck_corr[k + 3] != 0 else mp.mpf("inf")
        else:
            residual = None  # boundary: forward prediction not computable
        alphas.append(alpha)
        betas.append(beta)
        windows.append(k)
        residual_str = (f"{float(residual):>12.4e}" if residual is not None
                        else f"{'(boundary)':>12}")
        print(f"  {k:>8} {mp.nstr(alpha, 10):>14} {mp.nstr(beta, 10):>14} "
              f"{residual_str}")

    print()

    if alphas:
        # Spread of α, β across windows
        alpha_mean = sum(alphas) / len(alphas)
        beta_mean = sum(betas) / len(betas)
        alpha_spread = max(alphas) - min(alphas)
        beta_spread = max(betas) - min(betas)
        alpha_rel_spread = mp.fabs(alpha_spread / alpha_mean) if alpha_mean != 0 else mp.mpf("inf")
        beta_rel_spread = mp.fabs(beta_spread / beta_mean) if beta_mean != 0 else mp.mpf("inf")

        print(f"  Kernel coefficient stability:")
        print(f"    α mean        = {mp.nstr(alpha_mean, 10)}")
        print(f"    α rel spread  = {float(alpha_rel_spread * 100):.4f}%")
        print(f"    β mean        = {mp.nstr(beta_mean, 10)}")
        print(f"    β rel spread  = {float(beta_rel_spread * 100):.4f}%")
        print()
    else:
        alpha_mean = beta_mean = mp.mpf("nan")
        alpha_rel_spread = beta_rel_spread = mp.mpf("inf")

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()

    constant_kernel_holds = (alpha_rel_spread < mp.mpf("0.01")
                             and beta_rel_spread < mp.mpf("0.01"))
    if constant_kernel_holds:
        print(f"  ✓ CONSTANT-KERNEL depth-2 recurrence HOLDS on bias-")
        print(f"    corrected c_k. Kernel: α ≈ {mp.nstr(alpha_mean, 8)}, "
              f"β ≈ {mp.nstr(beta_mean, 8)}.")
        print()
        print(f"    This means the generating function F(u) for the c_k is")
        print(f"    a RATIONAL FUNCTION with denominator")
        print(f"      1 - α · u - β · u²")
        print(f"    The kernel (α, β) IS the structural data of F.")
        print(f"    PR #1786's depth-d sweep refuted the constant kernel on")
        print(f"    RAW c_k (which were biased); the BIAS-CORRECTED c_k DO")
        print(f"    satisfy the recurrence. This is the open keystone of")
        print(f"    the ck-dk registry §3.")
    else:
        print(f"  ✗ Constant-kernel depth-2 recurrence does NOT hold on")
        print(f"    bias-corrected c_k (spread > 1% in α or β).")
        print(f"    α rel spread: {float(alpha_rel_spread * 100):.2f}%")
        print(f"    β rel spread: {float(beta_rel_spread * 100):.2f}%")
        print()
        print(f"    Implications: the generating function (confirmed by 6.a)")
        print(f"    is NOT a simple rational with degree-2 denominator. It")
        print(f"    might be higher-degree rational, transcendental (e.g.")
        print(f"    cosh — see probe 6.b), or admit a q-dependent kernel")
        print(f"    that varies with the recurrence depth.")
    print()

    builder.add_data("ck_bias_corrected", {str(k): mp.nstr(v, 25) for k, v in ck_corr.items()})
    builder.add_data("kernel_fits", [
        {"window_k": w_k, "alpha": mp.nstr(a, 25), "beta": mp.nstr(b, 25)}
        for w_k, a, b in zip(windows, alphas, betas)
    ])
    builder.add_data("kernel_stability", {
        "alpha_mean": mp.nstr(alpha_mean, 25),
        "beta_mean": mp.nstr(beta_mean, 25),
        "alpha_rel_spread_pct": float(alpha_rel_spread * 100),
        "beta_rel_spread_pct": float(beta_rel_spread * 100),
        "constant_kernel_holds_on_corrected": constant_kernel_holds,
    })

    # `probe_6c_decisively_resolved` (computed=1, expected=1) was a tautology:
    # it recorded that the fit loop finished and could not fail either way —
    # its own source text says "either way", which is exactly the property an
    # assertion must not have. Demoted to data alongside the verdict it was
    # standing in for.
    builder.add_data("probe_6c_resolved", {
        "resolved": True,
        "constant_kernel_holds_on_corrected": constant_kernel_holds,
        "meaning": "the sliding-window depth-2 fit ran and returned a "
                   "verdict; the verdict itself is in kernel_stability",
        "recorded_not_gated": True,
        "has_independent_expected_value": False,
    })
    builder.add_data("u_subst_literal_cross_check", {
        "literal_in_source": mp.nstr(U_SUBST, 12),
        "b_times_hbar_q_sq_at_canonical_q0": mp.nstr(u_closed, 30),
        "abs_deviation": mp.nstr(u_literal_dev, 8),
        "rel_deviation": mp.nstr(u_literal_dev / u_closed, 8),
    })
    builder.add_assertion(
        "u_subst_literal_is_correct_rounding_of_b_hbar_q_sq",
        computed=mp.nstr(U_SUBST, 30),
        expected=mp.nstr(u_closed, 30),
        tolerance=U_SUBST_LITERAL_HALF_ULP,
        source="The hardcoded U_SUBST = 0.00852 vs b·ℏ_q² rebuilt from "
               "q_parameter.Q_50_DIGIT_STR by closed form — the literal a "
               "reader types and the substrate value it is supposed to "
               "stand for, computed without reference to each other. "
               "Tolerance is half an ulp of the literal's last significant "
               "digit, so a repin that moves u past 0.008515 / 0.008525 "
               "trips it.",
    )
    builder.add_caveat(
        "PRECISION (recorded, not repaired): U_SUBST is a 3-significant-figure "
        f"literal, {mp.nstr(u_literal_dev / u_closed, 4)} relative from the "
        "50-digit b·ℏ_q². The bias correction c_k − c_{k+1}·u is a NEAR "
        "CANCELLATION at these c_k (c_{k+1}/c_k ≈ 1/u), so that relative error "
        "does not stay at 1e-4 in c_k_corr. Fixing it changes the numbers and "
        "so belongs to a re-run of probe 6.a/6.c together, not to this drain."
    )
    builder.add_caveat(
        "PREMISE UNDER DOUBT (recorded, not repaired): the upstream "
        "qbeta-decay-sdp-extended-ck.witness.json now records all nine c_k as "
        "unresolved (null) — dividing a fixed accuracy floor by u^k "
        "manufactures c_k with ratio exactly 1/u. Both PR #1786's refutation "
        "on raw c_k and this probe's refutation on corrected c_k were "
        "computed from those numbers, so the committed verdict is provisional "
        "until they are re-derived. This producer now refuses to run against "
        "nulls rather than crashing inside mpmath."
    )

    builder.save()
    print(f"  Witness: qbeta-ck-q-difference-kernel-on-corrected-probe.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
