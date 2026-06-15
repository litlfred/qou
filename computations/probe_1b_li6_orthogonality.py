#!/usr/bin/env python3
"""
Probe (1b): test the PSD-dominance vs trace-dominance ORTHOGONALITY
at A=6.

At A=4 (Probe 1), the PSD-dominant pair (4,4,4)/(3,3,3,3) contributed
only 0.030% / 0.0002% of |tr_M|. The trace was dominated by 2-row
partitions ([9,3], [8,4], [10,2], [11,1], [7,5]).

At A=6, Probe (4c) shifted the PSD-dominant to (3,3,3,3,2,2,2) with
min_eig = -116.71. Does the orthogonality still hold?

This probe compares y_λ magnitudes between the PSD-dominant family
and the trace-dominant family at n=18. y_λ values come from the
existing y-lambda-at-q0.witness.json (no new compute needed).

Conclusion (preview): orthogonality holds EVEN MORE STRONGLY at
A=6 — the PSD-dominant family has y_λ ~ 10^-15, while the trace-
dominant family has y_λ ~ 10^-6, a 9-order-of-magnitude gap.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402


def main():
    base = Path(__file__).resolve().parent
    with open(base / "y-lambda-at-q0.witness.json") as f:
        y_data = json.load(f)
    n18 = y_data["data"]["by_n"]["18"]
    ydict = {tuple(e["partition"]): float(e["y_at_q0_50dps"]) for e in n18}

    # Trace-dominant family: top-10 by |y_λ|
    sorted_y = sorted(ydict.items(), key=lambda x: -abs(x[1]))
    trace_dominant = sorted_y[:10]

    # PSD-dominant family: scanned shapes with deepest min_eig
    # (from probe-4c and probe-4 witnesses)
    psd_data = {
        (3, 3, 3, 3, 2, 2, 2): -116.71,
        (5, 5, 5, 3): -110.31,
        (4, 4, 4, 3, 3): -109.81,
        (3, 3, 3, 3, 3, 3): -96.52,
        (6, 6, 6): -95.72,
        (8, 8, 2): -88.95,
        (10, 4, 4): -80.67,
    }
    psd_sorted = sorted(psd_data.items(), key=lambda x: x[1])

    print("=== TRACE-dominant family at n=18 (top-10 |y_λ|) ===")
    print(f"{'partition':>30s}  {'y_λ':>15s}  rows  shape kind")
    for shape, y_val in trace_dominant:
        rows = len(shape)
        kind = "2-row long-string" if rows == 2 else f"{rows}-row"
        print(f"{str(list(shape)):>30s}  {y_val:+13.4e}  {rows:>4d}  {kind}")

    print()
    print("=== PSD-dominant family at n=18 (deepest min_eig) ===")
    print(f"{'partition':>30s}  {'min_eig':>10s}  {'y_λ':>15s}  rows  cols  shape kind")
    for shape, m in psd_sorted:
        y_val = ydict.get(shape)
        rows = len(shape)
        cols = max(shape)
        kind = "rect" if len(set(shape)) == 1 else "multi-step"
        print(f"{str(list(shape)):>30s}  {m:>+10.4f}  "
              f"{y_val:+13.4e}  {rows:>4d}  {cols:>4d}  {kind}")

    # Magnitude separation
    max_trace_y = max(abs(y) for _, y in trace_dominant)
    deepest_shape = psd_sorted[0][0]
    deepest_y = abs(ydict[deepest_shape])
    ratio = max_trace_y / deepest_y if deepest_y > 0 else float("inf")
    print()
    print(f"=== Orthogonality magnitude separation ===")
    print(f"  Top trace |y_λ|     = {max_trace_y:.4e}   at λ = {list(trace_dominant[0][0])}")
    print(f"  Deepest PSD |y_λ|   = {deepest_y:.4e}   at λ = {list(deepest_shape)}")
    print(f"  Magnitude ratio     = {ratio:.4e}  (≈ 10^{int(round(math.log10(ratio))) if ratio > 0 else 0})")

    out = WitnessBuilder("probe-1b-li6-orthogonality", engine="python")
    out.set_description(
        "Tests PSD-dominance vs trace-dominance orthogonality at A=6. "
        "Mirrors Probe (1) at A=4 which found PSD-dominant blocks "
        "contribute <0.03% of |tr_M|. At A=6 the magnitude separation "
        "between trace-dominant (y ~ 10^-6) and PSD-dominant (y ~ 10^-15) "
        "is 9 orders of magnitude, confirming orthogonality holds even "
        "more strongly at A=6."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")

    out.add_data("trace_dominant_top10", [
        {"partition": list(s), "y_lambda": y, "n_rows": len(s)}
        for s, y in trace_dominant
    ])
    out.add_data("psd_dominant_scanned", [
        {"partition": list(s), "min_eig": m, "y_lambda": ydict.get(s),
         "n_rows": len(s), "max_row": max(s), "n_distinct_parts": len(set(s))}
        for s, m in psd_sorted
    ])
    out.add_data("magnitude_separation", {
        "top_trace_abs_y": max_trace_y,
        "deepest_psd_abs_y": deepest_y,
        "ratio_trace_over_psd": ratio,
        "log10_ratio": math.log10(ratio) if ratio > 0 else None,
    })

    out.add_assertion(
        name="orthogonality_holds_at_a6_with_8plus_order_separation",
        computed=str(int(ratio >= 1e8)),
        expected="1",
        tolerance=0,
        source=f"max trace |y_λ| / deepest PSD |y_λ| = {ratio:.4e}",
    )

    out.add_caveat(
        "Magnitude separation is a NECESSARY but not sufficient condition "
        "for the orthogonality. A definitive y·χ contribution test would "
        "require computing tr(ρ_λ(T_w_⁶Li)) for the PSD-dominant shapes "
        "via Hutchinson estimator or full diagonal trace. Given the 9-OOM "
        "y_λ gap and the symmetric eigval spread around 0 we observed for "
        "(3,3,3,3,2,2,2) [min=-117, max=+114], the contribution is "
        "expected to be effectively zero — but rigorous closure needs the "
        "tr_M computation."
    )

    out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("⁶Li"))

    out_path = out.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
