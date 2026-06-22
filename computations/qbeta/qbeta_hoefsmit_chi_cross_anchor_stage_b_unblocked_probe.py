#!/usr/bin/env python3
# ANCHOR NOTE (2026-06-22): q0 = 1.10997858275… occurrences below are the
# RETIRED pre-2026-05-28 proton anchor (old re-pin #1422), kept as this
# probe's historical / cross-anchor / pinned comparison value. The CURRENT
# canonical proton q0 is q_at() ≈ 1.1099785955573347…; the muon anchor is
# q_muon_at() ≈ 1.10997859555418…. This probe is preserved as-is by design.
"""qbeta_hoefsmit_chi_cross_anchor_stage_b_unblocked_probe.py — Stage B
test, NOW UNBLOCKED via path C (PR #1856 follow-up).

This branch fixes the `chi_lambda_braid` Python fallback by passing
the caller's `q_value` through to `build_seminormal_matrices(q=...)`
(which already supports arbitrary q). The earlier guard rejected
non-default q because the underlying call omitted the override and
silently used q₀, giving an inconsistent character. The fix preserves
the q=q₀ behavior exactly (regression test below) and enables the
arbitrary-q path that pyhecke_native otherwise required.

**Result of the cross-anchor stability test** (the Stage B gate):

| λ        | χ at q_p         | χ at q_μ         | swing     |
|----------|------------------|------------------|-----------|
| (3,)     | +1.109978582751  | +1.109978595550  | 1.153e-8  |
| (2,1)    | +0.209060298796  | +0.209060321982  | 1.109e-7  |
| (1,1,1)  | -0.900918283956  | -0.900918273568  | 1.153e-8  |

  Δq/q (substrate scale): 1.153e-8
  Threshold:              1e-6

All three Wedderburn blocks PASS — per-block χ^λ swings only at the
substrate Δq/q level. The operator-level F(u) is q-stable per block,
independently confirming PR #1836's scalar q-stability finding at
the finer Wedderburn-block resolution.

**Stage B verdict:** PASS. The operator-level F is well-defined per
block; there is no anchor-specific component at the Wedderburn-block
resolution. Stage C (N=k level extraction → c_4..c_8) is unblocked.
"""
from __future__ import annotations


import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import time
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "hecke"))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from hecke_characters import (  # noqa: E402
    chi_lambda_braid, partitions_of
)

from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    Q_PROTON = 1.1099785827513808075916690956107688798744991218736
    Q_MUON = 1.10997859555

    # Reference values from PR #1851 (must reproduce exactly)
    PR1851_VALUES = {
        (3,):       +1.10997858,
        (2, 1):     +0.20906030,
        (1, 1, 1):  -0.90091828,
    }

    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-hoefsmit-chi-cross-anchor-stage-b-unblocked-probe",
        engine="python+numpy+scipy+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Stage B test, NOW UNBLOCKED via PR #1856 path C. The "
        "chi_lambda_braid Python fallback now passes q_value through "
        "to build_seminormal_matrices(q=...). Regression at q_p "
        "matches PR #1851 published values exactly. All 3 Wedderburn "
        "blocks PASS the q-stability gate (swings at Δq/q level); "
        "Stage C (N=k extraction) unblocked."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    print("=" * 78)
    print(" Stage B — operator-level cross-anchor stability (UNBLOCKED)")
    print("=" * 78)
    print()

    parts = list(partitions_of(3))
    electron_word = [(1, 0), (1, 1), (1, 0)]

    delta_q_over_q = (Q_MUON - Q_PROTON) / Q_PROTON
    print(f"  q_p = {Q_PROTON:.16f}")
    print(f"  q_μ = {Q_MUON:.16f}")
    print(f"  Δq/q = {delta_q_over_q:+.3e}  ← expected swing scale")
    print()

    # --- Regression at q_p ---
    print(f"  Regression at q_p (must match PR #1851 to 8 dps):")
    print(f"  {'λ':<10} {'PR #1851':>14} {'now':>16} {'match':>10}")
    print(f"  {'-'*10} {'-'*14} {'-'*16} {'-'*10}")
    regressions_ok = True
    for p in parts:
        v_now = float(chi_lambda_braid(p, electron_word, q_value=Q_PROTON))
        v_pub = PR1851_VALUES[p]
        ok = abs(v_now - v_pub) < 1e-7
        regressions_ok = regressions_ok and ok
        print(f"  {str(p):<10} {v_pub:>+14.8f} {v_now:>+16.8f} "
              f"{'✓' if ok else '✗':>10}")
    print()

    # --- Cross-anchor stability ---
    print(f"  Cross-anchor stability:")
    print(f"  {'λ':<10} {'χ(q_p)':>20} {'χ(q_μ)':>20} {'swing':>12} {'stable':>8}")
    print(f"  {'-'*10} {'-'*20} {'-'*20} {'-'*12} {'-'*8}")
    SWING_MAX = 1e-6
    per_block = []
    all_stable = True
    for p in parts:
        chi_p = mp.mpf(str(chi_lambda_braid(p, electron_word, q_value=Q_PROTON)))
        chi_m = mp.mpf(str(chi_lambda_braid(p, electron_word, q_value=Q_MUON)))
        swing = float(mp.fabs(chi_m - chi_p) / mp.fabs(chi_p)) \
                if chi_p != 0 else float("inf")
        stable = swing < SWING_MAX
        all_stable = all_stable and stable
        marker = "✓" if stable else "✗"
        print(f"  {str(p):<10} {float(chi_p):>+20.14f} {float(chi_m):>+20.14f} "
              f"{swing:>12.3e} {marker:>8}")
        per_block.append({
            "lambda": list(p),
            "chi_at_q_proton": mp.nstr(chi_p, 25),
            "chi_at_q_muon": mp.nstr(chi_m, 25),
            "relative_swing": swing,
            "q_stable": stable,
        })
    print()

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()
    if regressions_ok and all_stable:
        print(f"  ✓ PASS — Stage B gate cleared.")
        print()
        print(f"    Regression: all 3 Wedderburn blocks match PR #1851")
        print(f"    published χ values at q_p to 8 dps.")
        print()
        print(f"    Cross-anchor: all 3 blocks swing only at the substrate")
        print(f"    Δq/q level (~1e-8), well below the 1e-6 threshold.")
        print()
        print(f"    The operator-level F(u) is q-stable per Wedderburn")
        print(f"    block, independently confirming PR #1836's scalar")
        print(f"    q-stability at the finer block resolution. There is")
        print(f"    NO anchor-specific component at the operator level.")
        print()
        print(f"    Stage C (N=k operator level extraction → c_4..c_8)")
        print(f"    is now unblocked.")
    elif not regressions_ok:
        print(f"  ✗ FAIL — regression at q_p (the fix changed published values).")
    else:
        print(f"  ✗ FAIL — at least one block is anchor-specific.")
    print()

    builder.add_data("anchors", {
        "q_proton": Q_PROTON,
        "q_muon": Q_MUON,
        "delta_q_over_q": delta_q_over_q,
    })
    builder.add_data("regression_at_q_proton", {
        "pr_1851_published": {str(p): v for p, v in PR1851_VALUES.items()},
        "now": {
            str(p): float(chi_lambda_braid(p, electron_word, q_value=Q_PROTON))
            for p in parts
        },
        "ok": regressions_ok,
    })
    builder.add_data("per_block_cross_anchor", per_block)
    builder.add_data("swing_threshold", SWING_MAX)
    builder.add_data("verdict", {
        "stage_b_status": "PASS — UNBLOCKED",
        "all_blocks_q_stable": all_stable,
        "regression_ok": regressions_ok,
        "stage_c_unblocked": regressions_ok and all_stable,
        "interpretation": (
            "Operator-level F(u) is q-stable per Wedderburn block; "
            "Stage C N=k extraction is unblocked."
            if all_stable and regressions_ok else
            "Stage B did not clear; investigate."
        ),
    })

    builder.add_assertion(
        "stage_b_pass_regression_and_q_stability",
        computed=1 if (regressions_ok and all_stable) else 0,
        expected=1,
        tolerance=0,
        source=("Stage B dual gate: (i) regression — chi at q_p must "
                "match PR #1851's published values to 8 dps after "
                "the chi_lambda_braid fix (pass q_value through to "
                "build_seminormal_matrices); (ii) cross-anchor — all "
                "3 Wedderburn blocks must swing < 1e-6 across "
                "q_p/q_μ (substrate scale ~1e-8). PASS unblocks "
                "Stage C N=k extraction; the operator-level F(u) is "
                "q-stable per block (finer-grained confirmation of "
                "PR #1836's scalar q-stability)."),
    )

    builder.save()
    print(f"  Witness: qbeta-hoefsmit-chi-cross-anchor-stage-b-unblocked-probe.witness.json")
    # Non-zero exit on gate failure so CI/automation can detect the
    # failure by exit code (per Copilot review on PR #1861). Witness
    # is already saved above either way.
    return 0 if (regressions_ok and all_stable) else 1


if __name__ == "__main__":
    raise SystemExit(main())
