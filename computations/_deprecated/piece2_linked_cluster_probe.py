#!/usr/bin/env python3
"""
Piece 2: linked-cluster expansion structure.

The six-term theorem's T_1 + T_2 + T_3 + T_4 + T_5 + T_6 sum
implicitly assumes ADDITIVE structure — but the categorical-mass
expansion typically has linked-cluster (cumulant) structure where
T_3 includes a counterterm subtracting the disconnected part of
T_2 × T_2.

Naive additivity:        ρ_K |tr_M| = T_1 + T_2 + T_3 + ...
Cumulant expansion:      ρ_K |tr_M| = T_1 + κ_1 T_2 + κ_2 (T_3 - T_2²/2) + ...

This probe tests:
  (a) For atoms with multiple generators, what's the empirical
      ratio T_3 / T_2² across atoms? Constant ratio → linked-cluster.
  (b) Does T_2 - T_3/(2 T_2) (subtracting the disconnected piece)
      give a more universal value across atoms?

Reads paper-six-term-isotope-sweep.witness.json.

Output: piece2-linked-cluster.witness.json
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))


def main() -> int:
    print("=" * 96)
    print("  Piece 2: linked-cluster structure of T_2 (single-gen) and T_3 (pair-gen)")
    print("=" * 96)

    six_term = json.load(open(HERE / "paper-six-term-isotope-sweep.witness.json"))
    rows = [r for r in six_term["rows"] if "M_predicted" in r]

    print(f"\n  Per-atom T_2, T_3 from six-term sweep (li2q tower mode):")
    print(f"  {'atom':<6} {'A':>2} {'T_2':>10} {'T_3':>10} {'T_3/T_2':>10} {'T_3/T_2²':>10} {'T_3 - T_2²/2':>14}")
    print("  " + "-" * 80)
    pair_data = []
    for r in rows:
        T2 = r["term2_single_gen_tower"]
        T3 = r["term3_pair_gen_tower"]
        if T2 == 0:
            continue
        ratio_T3_T2 = T3 / T2
        ratio_T3_T2sq = T3 / (T2 ** 2) if T2 != 0 else None
        cumulant = T3 - (T2 ** 2) / 2
        print(f"  {r['isotope']:<6} {r['A']:>2} {T2:>10.4f} {T3:>10.4f} {ratio_T3_T2:>10.4f} "
              f"{ratio_T3_T2sq:>10.4f} {cumulant:>+14.4f}")
        pair_data.append({
            "atom": r["isotope"], "A": r["A"],
            "T_2": T2, "T_3": T3,
            "T_3_over_T_2": ratio_T3_T2,
            "T_3_over_T_2_squared": ratio_T3_T2sq,
            "cumulant_T_3_minus_half_T_2_squared": cumulant,
        })

    if pair_data:
        # Constant ratio test
        ratios_T3_T2 = [p["T_3_over_T_2"] for p in pair_data if p["T_3_over_T_2"] is not None]
        ratios_T3_T2sq = [p["T_3_over_T_2_squared"] for p in pair_data if p["T_3_over_T_2_squared"] is not None]
        if ratios_T3_T2:
            mean_r1 = sum(ratios_T3_T2) / len(ratios_T3_T2)
            range_r1 = (min(ratios_T3_T2), max(ratios_T3_T2))
            print(f"\n  T_3 / T_2 ratios across atoms:")
            print(f"    mean = {mean_r1:.4f},  range = {range_r1[0]:.4f}..{range_r1[1]:.4f}")
            spread = (range_r1[1] - range_r1[0]) / mean_r1 * 100
            print(f"    spread = {spread:.1f}%")
            if spread < 10:
                print(f"    → near-constant T_3/T_2 ratio: T_3 ≈ {mean_r1:.3f} · T_2")
                print(f"      Suggests T_3 is correlated with T_2 (linked-cluster structure).")

        if ratios_T3_T2sq:
            mean_r2 = sum(ratios_T3_T2sq) / len(ratios_T3_T2sq)
            range_r2 = (min(ratios_T3_T2sq), max(ratios_T3_T2sq))
            print(f"\n  T_3 / T_2² ratios across atoms:")
            print(f"    mean = {mean_r2:.4f},  range = {range_r2[0]:.4f}..{range_r2[1]:.4f}")
            spread2 = (range_r2[1] - range_r2[0]) / max(abs(mean_r2), 1e-12) * 100
            print(f"    spread = {spread2:.1f}%")
            if abs(mean_r2 - 0.5) < 0.05:
                print(f"    ★ T_3 ≈ T_2²/2 → CLASSIC CUMULANT structure!")
            if spread2 < 30:
                print(f"    → T_3 / T_2² is roughly constant — linked-cluster signature.")

    print(f"\n  Implication for the graded ρ_K expansion:")
    if ratios_T3_T2sq and abs(sum(ratios_T3_T2sq) / len(ratios_T3_T2sq) - 0.5) < 0.1:
        print(f"    The expansion has linked-cluster structure: T_3 ≈ T_2²/2")
        print(f"    This is the connected-cluster expansion's coupled-cumulant form.")
        print(f"    The proper unified formula:")
        print(f"      ρ_K |tr_M| = T_1 + (T_2 - T_2²/2) + ...  (NOT T_1 + T_2 + T_3 + ...)")
        print(f"    The 'pair-gen' is a DOUBLE-COUNTING CORRECTION, not an independent term.")
    else:
        print(f"    T_3 / T_2² varies significantly → not a simple cumulant relation.")
        print(f"    The atoms may have additional A-dependent structure that breaks")
        print(f"    pure linked-cluster behaviour.")

    witness = {
        "computation": "piece2-linked-cluster",
        "description": (
            "Piece 2 of the open functional-form problem: empirical "
            "investigation of linked-cluster structure between T_2 "
            "(single-gen brane tower) and T_3 (pair-gen brane tower) "
            "in the six-term theorem. Tests whether T_3 ≈ T_2²/2 "
            "(classic linked-cluster) holds across atoms — if yes, "
            "the ρ_K graded expansion needs cumulant form rather than "
            "naive additivity."
        ),
        "reference_blocks": [
            "prop:rho-k-graded-expansion",
            "thm:knot-mass-formula-unified",
        ],
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "rows": pair_data,
        "ratios_T3_T2": ratios_T3_T2 if pair_data else [],
        "ratios_T3_T2_squared": ratios_T3_T2sq if pair_data else [],
    }
    out = HERE / "piece2-linked-cluster.witness.json"
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
