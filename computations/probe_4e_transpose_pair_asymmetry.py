#!/usr/bin/env python3
"""
Probe (4e): quantify the bar-involution transpose-pair asymmetry.

For each transpose pair (λ, λ^T) at n=18, the bar involution swaps
them. If the bar acted as a symmetry of the obstruction structure,
we'd expect min_eig(ρ_λ) = min_eig(ρ_{λ^T}). Empirically, the
*tall-narrow* shape is consistently deeper than the *wide-short*
shape — sometimes by 20+ units.

This probe extracts all transpose-pair data from the aggressive
scan witness (probe_4d) and prior probes, computes the asymmetry
Δ = |min_eig(λ_tall)| − |min_eig(λ_wide)|, and reports the
empirical distribution. A non-zero average Δ is a structural
asymmetry the categorical derivation must explain.

Audit-only.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder


def transpose(p):
    if not p:
        return []
    m = max(p)
    return tuple(sum(1 for x in p if x >= i + 1) for i in range(m))


def main():
    base = Path(__file__).resolve().parent

    # Aggregate min_eig data from multiple witnesses (4, 4b, 4c, 4d if exists)
    all_min_eig = {}

    sources = [
        ("probe-1b-li6-orthogonality.witness.json", "psd_dominant_scanned"),
        ("probe-4-li6-rectangular-python-targeted.witness.json", "rectangular_pair_eigvals"),
        ("probe-4b-li6-non-rectangular-scan.witness.json", "scanned_partitions"),
        ("probe-4c-li6-large-d-scan.witness.json", "scanned_partitions"),
    ]
    for fname, key in sources:
        p = base / fname
        if not p.exists():
            continue
        with open(p) as f:
            w = json.load(f)
        data = w.get("data", {})
        items = data.get(key)
        if items is None:
            continue
        if isinstance(items, dict):
            for k, v in items.items():
                shape = tuple(v.get("shape", []))
                me = v.get("min_eig") or v.get("min_eig_lanczos")
                if shape and me is not None:
                    all_min_eig[shape] = me
        elif isinstance(items, list):
            for v in items:
                shape = tuple(v.get("shape", []) or v.get("partition", []))
                me = v.get("min_eig")
                if shape and me is not None:
                    all_min_eig[shape] = me

    # Also try probe-4d if witness exists
    p4d = base / "probe-4d-li6-aggressive-scan.witness.json"
    if p4d.exists():
        with open(p4d) as f:
            w = json.load(f)
        items = w.get("data", {}).get("all_scanned_partitions", [])
        for v in items:
            shape = tuple(v.get("shape", []))
            me = v.get("min_eig")
            if shape and me is not None:
                all_min_eig[shape] = me

    print(f"Aggregated min_eig data for {len(all_min_eig)} partitions at n=18\n")

    # Build transpose pairs where BOTH are in the data
    seen = set()
    pairs = []
    for shape, me in all_min_eig.items():
        if shape in seen:
            continue
        t = transpose(shape)
        if t == shape:
            # Self-conjugate, no asymmetry to measure
            continue
        if t in all_min_eig:
            t_me = all_min_eig[t]
            # Determine which is "tall narrow" (more rows, less max)
            rows_s = len(shape)
            rows_t = len(t)
            if rows_s > rows_t:
                tall, tall_me = shape, me
                wide, wide_me = t, t_me
            else:
                tall, tall_me = t, t_me
                wide, wide_me = shape, me
            asymm = abs(tall_me) - abs(wide_me)
            pairs.append({
                "tall_narrow": list(tall),
                "tall_min_eig": tall_me,
                "wide_short": list(wide),
                "wide_min_eig": wide_me,
                "asymmetry": asymm,
                "tall_n_rows": len(tall),
                "wide_n_rows": len(wide),
            })
            seen.add(shape)
            seen.add(t)

    pairs.sort(key=lambda p: -p["asymmetry"])

    print(f"Transpose pairs (both members scanned): {len(pairs)}")
    print(f"{'tall-narrow':>30s}  {'min_eig':>10s}  {'wide-short':>30s}  {'min_eig':>10s}  asymmetry")
    for p in pairs:
        print(f"{str(p['tall_narrow']):>30s}  {p['tall_min_eig']:>10.4f}  "
              f"{str(p['wide_short']):>30s}  {p['wide_min_eig']:>10.4f}  "
              f"{p['asymmetry']:+7.4f}")

    # Stats
    if pairs:
        asymmetries = [p["asymmetry"] for p in pairs]
        n_positive = sum(1 for a in asymmetries if a > 0)
        n_negative = sum(1 for a in asymmetries if a < 0)
        n_zero = sum(1 for a in asymmetries if abs(a) < 0.1)
        avg = sum(asymmetries) / len(asymmetries)
        max_asymm = max(asymmetries)
        min_asymm = min(asymmetries)
        print(f"\n=== Asymmetry stats ===")
        print(f"  n_pairs                = {len(pairs)}")
        print(f"  n_positive (tall deeper)  = {n_positive}/{len(pairs)} ({100*n_positive/len(pairs):.1f}%)")
        print(f"  n_negative (wide deeper) = {n_negative}/{len(pairs)} ({100*n_negative/len(pairs):.1f}%)")
        print(f"  n_~zero (|asymm| < 0.1)  = {n_zero}")
        print(f"  average asymmetry      = {avg:+.4f}")
        print(f"  max asymmetry          = {max_asymm:+.4f}")
        print(f"  min asymmetry          = {min_asymm:+.4f}")

    out = WitnessBuilder("probe-4e-transpose-pair-asymmetry", engine="python")
    out.set_description(
        "Quantifies the bar-involution transpose-pair asymmetry: for "
        "each pair (λ, λ^T), the *tall-narrow* shape's min_eig is "
        "consistently more negative than the *wide-short* shape's. "
        "The bar acts as a swap of shapes but the obstruction depth "
        "is NOT preserved — a non-trivial structural fact the "
        "categorical derivation must explain."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:psd-trace-orthogonality")

    out.add_data("transpose_pairs", pairs)
    if pairs:
        out.add_data("asymmetry_stats", {
            "n_pairs": len(pairs),
            "n_tall_narrow_deeper": n_positive,
            "n_wide_short_deeper": n_negative,
            "frac_tall_narrow_deeper": n_positive / len(pairs),
            "mean_asymmetry": avg,
            "max_asymmetry": max_asymm,
            "min_asymmetry": min_asymm,
        })
        out.add_assertion(
            name="tall_narrow_systematically_deeper",
            computed=str(int(n_positive > 0.7 * len(pairs))),
            expected="1",
            tolerance=0,
            source=f"{n_positive}/{len(pairs)} pairs have tall-narrow deeper",
        )

    out_path = out.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
