#!/usr/bin/env python3
"""qbeta_c_k_recursion_depth_sweep.py — depth-d sweep on the c_k
recurrence test, extending the PR #1713 / qbeta_habiro_q_difference_recurrence
result that depth-2 with constant kernel is refuted (relative spread
of α ≈ 318×, of β ≈ 765×).

For each depth d in {2, 3, 4, 5}, this probe:

  1. Builds linear systems from consecutive (d+1)-element windows of
     the SDP-extracted c_k:
         c_{k+1} = a_0·c_k + a_1·c_{k-1} + ... + a_{d-1}·c_{k+1-d}
     for k = d, d+1, ..., N−1. Each window gives d equations in d
     unknowns (a_0..a_{d-1}); solving each independent (d-window)
     starting at row k yields a kernel estimate.

  2. Reports the relative spread of each kernel coefficient across
     windows.  Small spread (≪ 1) = a constant-kernel depth-d
     recurrence HOLDS structurally; large spread = refutation at
     that depth.

  3. Tests the asymptotic-ratio hypothesis: PR #1713 data shows
     c_{k+1}/c_k → ~117 ≈ 1/h_q² at q_0 for k ≥ 7.  If the dominant
     eigenvalue of the recurrence kernel equals 1/h_q² exactly, this
     is the structural fingerprint.

The c_k beyond k = 4 are SDP-extracted from `qbeta-decay-sdp-extended-
ck.witness.json` — i.e. archimedean evaluations at q_0, possibly with
SDP roundoff above 50 dps.  This probe makes no claim about the
fibre-level Habiro element F(q) — it characterizes which (if any)
constant-kernel finite-depth structure the q_0-evaluated c_k support.

If a constant-kernel depth d* < ∞ recurrence holds, the Lean
`CKRecursion R` scaffold of
`prop:q-beta-c-k-recursion-from-habiro-q-difference` can be
instantiated with `depth = d*` and `kernel = (a_0, ..., a_{d*-1})`,
turning the framework into a concrete c_k predictor.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
# `_path_bridge` (imported above) already inserts the computations/ dir
# on sys.path, so the `_precision` / `witness_base` imports below resolve
# without a second `sys.path.insert(0, HERE.parent)`. Consolidated to a
# single path-mutation strategy per Copilot review on PR #1786.

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "65")
os.environ.setdefault("QOU_OUTPUT_DPS", "50")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(65)
import mpmath as mp  # noqa: E402
mp.mp.dps = 65

from witness_base import WitnessBuilder  # noqa: E402

Q_0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")
HBAR_Q = (Q_0 - 1) / Q_0
HBAR_Q_SQ = HBAR_Q ** 2
INV_HBAR_Q_SQ = 1 / HBAR_Q_SQ  # ≈ 117.4


def load_c_k() -> dict:
    p = HERE / "qbeta-decay-sdp-extended-ck.witness.json"
    w = json.loads(p.read_text())
    raw = w["data"]["c_k_extracted_50dps"]
    return {int(k.split("_")[1]): mp.mpf(v) for k, v in raw.items()}


def solve_depth_d_window(c_k: dict, k_start: int, d: int) -> tuple:
    """Solve for the d-vector kernel (a_0, ..., a_{d-1}) such that
    c_{k+1} = Σ_j a_j · c_{k-j}  for k = k_start, k_start+1, ..., k_start+d-1.
    Returns (kernel, residual) where residual = max abs error of the fit.

    If any required c_k index is missing (non-contiguous data),
    returns (None, inf) — same failure handling as a singular matrix.
    """
    # Pre-validate that every c_k index needed for this window is present.
    needed = {k_start + row + 1 for row in range(d)} | {
        k_start + row - j for row in range(d) for j in range(d)
    }
    if not needed.issubset(c_k.keys()):
        return None, mp.mpf("inf")
    A = mp.matrix(d, d)
    b = mp.matrix(d, 1)
    for row in range(d):
        k = k_start + row
        for j in range(d):
            A[row, j] = c_k[k - j]
        b[row, 0] = c_k[k + 1]
    try:
        x = mp.lu_solve(A, b)
    except (ZeroDivisionError, ValueError):
        return None, mp.mpf("inf")
    kernel = tuple(x[j, 0] for j in range(d))
    # Compute residual on the same window
    resid = mp.mpf(0)
    for row in range(d):
        k = k_start + row
        pred = sum(kernel[j] * c_k[k - j] for j in range(d))
        resid = max(resid, abs(pred - c_k[k + 1]))
    return kernel, resid


def kernel_spread(kernels: list) -> list:
    """For a list of kernel tuples (each of length d), return the
    relative spread (max − min) / mean(abs(values)) per coefficient.

    The mean-of-absolute-values normalisation is used (not the signed
    mean) so a coefficient oscillating around zero — e.g. (-100, +100)
    — still produces a finite, meaningful spread instead of dividing
    by a near-zero signed mean.
    """
    if not kernels:
        return []
    d = len(kernels[0])
    spreads = []
    for j in range(d):
        vals = [k[j] for k in kernels]
        m = sum(abs(v) for v in vals) / len(vals)
        if m == 0:
            spreads.append(mp.mpf("inf"))
            continue
        spread = (max(vals) - min(vals)) / m
        spreads.append(spread)
    return spreads


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "qbeta-c-k-recursion-depth-sweep",
        engine="python+mpmath",
        start_time=t0,
    )
    builder.set_description(
        "Depth-d sweep on the Q_β c_k constant-kernel recurrence "
        "test. Extends qbeta_habiro_q_difference_recurrence_probe "
        "(which refuted depth-2 with α-spread 318× / β-spread 765×) "
        "to depths d = 3, 4, 5. For each d, builds independent linear "
        "systems from consecutive (d+1)-element c_k windows, reports "
        "the relative spread of the kernel components across windows. "
        "Small spread = depth-d recurrence holds structurally. Also "
        "tests asymptotic-ratio hypothesis c_{k+1}/c_k → 1/h_q² at "
        "q_0. If a depth d* is found, the Lean CKRecursion R scaffold "
        "(prop:q-beta-c-k-recursion-from-habiro-q-difference) "
        "instantiates directly with that depth + kernel."
    )
    builder.set_content_block("prop:q-beta-c-k-recursion-from-habiro-q-difference")

    c_k = load_c_k()
    n_max = max(c_k.keys())
    n_min = min(c_k.keys())
    print("=" * 78)
    print(" Q_β c_k DEPTH-d RECURRENCE SWEEP")
    print("=" * 78)
    print()
    print(f"  c_k loaded: k = {n_min}..{n_max} from "
          "qbeta-decay-sdp-extended-ck.witness.json")
    print(f"  q_0           = {mp.nstr(Q_0, 15)}")
    print(f"  h_q² at q_0   = {mp.nstr(HBAR_Q_SQ, 15)}")
    print(f"  1/h_q²        = {mp.nstr(INV_HBAR_Q_SQ, 15)}  "
          "(asymptotic ratio target)")
    print()

    # ─ Per-depth sweep ──────────────────────────────────────────────
    results = {}
    for d in (2, 3, 4, 5):
        # k_start range is [n_min + d - 1, n_max - d + 1); each window
        # consumes 2d consecutive c_k values. n_windows is the loop count.
        n_windows = max(0, n_max - n_min - 2 * d + 2)
        print(f"  ── depth d = {d} ── ({n_windows} windows)")
        kernels = []
        residuals = []
        for k_start in range(n_min + d - 1, n_max - d + 1):
            ker, resid = solve_depth_d_window(c_k, k_start, d)
            if ker is None:
                continue
            kernels.append(ker)
            residuals.append(resid)
            print(f"    window k_start={k_start}: kernel = "
                  f"({', '.join(mp.nstr(x, 8) for x in ker)}) "
                  f"residual={mp.nstr(resid, 5)}")
        spreads = kernel_spread(kernels)
        for j, s in enumerate(spreads):
            print(f"    a_{j} relative spread across windows: "
                  f"{mp.nstr(s, 5)}")
        if not spreads:
            verdict = "INSUFFICIENT_DATA"
        elif all(s < 0.01 for s in spreads):
            verdict = "HOLDS"
        elif all(s < 1 for s in spreads):
            verdict = "near-match"
        else:
            verdict = "REFUTED"
        print(f"    → depth-{d} constant-kernel verdict: {verdict}")
        print()
        results[d] = {
            "kernels": [[mp.nstr(x, 15) for x in k] for k in kernels],
            "spreads": [mp.nstr(s, 15) for s in spreads],
            "verdict": verdict,
            "max_residual": mp.nstr(max(residuals) if residuals
                                    else mp.mpf("nan"), 10),
        }

    # ─ Asymptotic-ratio test ────────────────────────────────────────
    print("  ── asymptotic-ratio test ──")
    print(f"    target: c_{{k+1}}/c_k → 1/h_q² = "
          f"{mp.nstr(INV_HBAR_Q_SQ, 12)}")
    ratios = {}
    for k in sorted(c_k.keys())[:-1]:
        # Skip if c_k[k] is zero (division-by-zero) OR if c_k[k+1]
        # is missing (non-contiguous data; future-proofing for
        # gappy SDP extractions).
        if c_k[k] == 0 or (k + 1) not in c_k:
            continue
        r = c_k[k + 1] / c_k[k]
        ratios[k] = r
        deviation = (r - INV_HBAR_Q_SQ) / INV_HBAR_Q_SQ
        print(f"    r_{k}->{k+1} = {mp.nstr(r, 10):<18}  "
              f"dev from 1/h_q² = {mp.nstr(deviation, 5)}")
    # Asymptotic value (mean of last 3 ratios; guard against empty)
    last_ks = sorted(ratios.keys())[-3:]
    if not last_ks:
        asym = mp.mpf("nan")
        asym_dev = mp.mpf("nan")
        print("    (no ratios computed — insufficient c_k data)")
    else:
        asym = sum(ratios[k] for k in last_ks) / len(last_ks)
        asym_dev = (asym - INV_HBAR_Q_SQ) / INV_HBAR_Q_SQ
        print(f"    mean(last {len(last_ks)} ratios) = "
              f"{mp.nstr(asym, 12)}")
        print(f"    deviation from 1/h_q²: {mp.nstr(asym_dev, 5)}")
    print()

    # ─ Verdict ──────────────────────────────────────────────────────
    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print()
    for d, r in results.items():
        if r['spreads']:
            max_spread = float(max(mp.mpf(s) for s in r['spreads']))
            print(f"  depth-{d}: {r['verdict']:<18}  "
                  f"max coefficient spread = {max_spread:.3e}")
        else:
            print(f"  depth-{d}: {r['verdict']:<18}  "
                  "(no windows — need more c_k data)")
    print()
    print(f"  asymptotic ratio (last 3 mean): "
          f"{mp.nstr(asym, 8)}  vs  1/h_q² = "
          f"{mp.nstr(INV_HBAR_Q_SQ, 8)}  "
          f"({float(asym_dev * 100):.2f}% deviation)")
    print()

    # Save
    builder.add_data("depth_sweep_results",
                     {f"depth_{d}": r for d, r in results.items()})
    builder.add_data("asymptotic_ratio_test", {
        "target_1_over_hbar_q_sq": mp.nstr(INV_HBAR_Q_SQ, 25),
        "mean_last_3_ratios": mp.nstr(asym, 25),
        "deviation": mp.nstr(asym_dev, 15),
        "per_step_ratios": {str(k): mp.nstr(r, 25)
                            for k, r in ratios.items()},
    })

    # Meaningful invariants (not the per-run finding count, which is
    # information-only and was flagged by Copilot as non-enforcing).
    # Recorded as data:
    holding_depths = [d for d, r in results.items() if r["verdict"] == "HOLDS"]
    near_match_depths = [d for d, r in results.items()
                         if r["verdict"] == "near-match"]
    builder.add_data("verdict_summary", {
        "holding_depths": holding_depths,
        "near_match_depths": near_match_depths,
        "refuted_depths": [d for d, r in results.items()
                           if r["verdict"] == "REFUTED"],
        "insufficient_data_depths": [
            d for d, r in results.items()
            if r["verdict"] == "INSUFFICIENT_DATA"
        ],
    })
    # Real invariant: at least one (d, window) succeeded — i.e. the
    # sweep produced data, not just an empty pipeline.  Boolean
    # predicate so `|computed - expected| <= tolerance` enforces a
    # strict lower bound (tolerance = 0).
    total_windows = sum(len(r["kernels"]) for r in results.values())
    builder.add_data("total_windows_across_all_depths", total_windows)
    builder.add_assertion(
        "depth_sweep_produced_at_least_one_window",
        computed=int(total_windows >= 1),
        expected=1,
        tolerance=0,
        source=("Sanity invariant: the depth sweep must produce at "
                "least one fitted window across all depths d ∈ "
                "{2,3,4,5}. computed = 1 iff total_windows ≥ 1; "
                "expected = 1 with tolerance = 0 enforces a strict "
                "boolean predicate (no slack). The integer "
                "total_windows itself is recorded as data. Per-depth "
                "verdicts (HOLDS / near-match / REFUTED / "
                "INSUFFICIENT_DATA) are reported as data, not "
                "assertions."),
    )

    builder.save()
    print(f"\n  Witness: qbeta-c-k-recursion-depth-sweep.witness.json")
    print(f"  Holding depths: {holding_depths or '(none)'}")
    print(f"  Near-match depths: {near_match_depths or '(none)'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
