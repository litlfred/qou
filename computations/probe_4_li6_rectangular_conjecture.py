#!/usr/bin/env python3
"""
Probe (4): test the rectangular-form conjecture on ⁶Li.

Per the dominant-partition audit (2026-05-25), the conjecture states
that for the canonical atom-braid `T_w(Z, N)` on `B_{3A}` with A ≥ 4,
the dominant Wedderburn partition forcing α* satisfies:

    `λ*^T` = A × 3 rectangle  ⟺  `λ*` = 3 × A rectangle

For ⁶Li (A=6, n_0=18), this predicts:

    `λ*` = (6, 6, 6)   d_λ = ?
    `λ*^T` = (3, 3, 3, 3, 3, 3)   d_λ = ?

This probe reads the ⁶Li certificate (after the Rust registry was
extended in this PR), identifies the dominant partition via
α* = 1/(1 − ε_min), and tests whether it matches the prediction.

Falsification rule: if dominant λ* is NOT (6, 6, 6), the rectangular-
form conjecture is falsified at A=6 (the FIRST testable extension
beyond ⁴He), and the Schur-Weyl correspondence observed at ⁴He is
either A=4-specific or a small-A coincidence.

Bound to `conj:atom-braid-exterior-algebra`. Audit-only.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder
from lean_uniqueness_refs import lean_uniqueness_ref


def alpha_star_from_min_eig(min_eig: float) -> float:
    if min_eig >= 0:
        return 1.0
    return 1.0 / (1.0 - min_eig)


def main() -> int:
    base = Path(__file__).resolve().parent
    witness_path = base / "joint-tower-sdp-rust.witness.json"

    with open(witness_path) as f:
        jt = json.load(f)

    li6 = next((c for c in jt.get("per_atom_certificates", [])
                if c.get("name") == "lithium6-canonical-3A"), None)
    if li6 is None:
        print("ERROR: lithium6-canonical-3A not found in witness "
              "(re-run joint-tower-sdp with ⁶Li registered).")
        return 1

    wb = li6.get("wedderburn_blocks", [])
    evaled = [b for b in wb if b.get("matrix_at_q_0_sym_eigvals")]
    if not evaled:
        print("ERROR: no Wedderburn blocks evaluated for ⁶Li "
              "(increase --max-dim-psd?).")
        return 1

    # Sort by min_eig ascending — most negative first.
    evaled_sorted = sorted(evaled, key=lambda b: b["min_eigenvalue"])
    dominant = evaled_sorted[0]
    dominant_part = dominant["partition"]
    dominant_min_eig = dominant["min_eigenvalue"]
    predicted_alpha = alpha_star_from_min_eig(dominant_min_eig)

    # Compute the transpose (Young-diagram conjugate)
    def transpose(p):
        if not p:
            return []
        m = max(p)
        return [sum(1 for x in p if x >= i + 1) for i in range(m)]

    dominant_T = transpose(dominant_part)

    # Predicted rectangular form: λ* = (6, 6, 6); λ*^T = (3, 3, 3, 3, 3, 3)
    PREDICTED_DOMINANT = [6, 6, 6]
    PREDICTED_TRANSPOSE = [3, 3, 3, 3, 3, 3]

    rectangle_match = (dominant_part == PREDICTED_DOMINANT
                       or dominant_T == PREDICTED_TRANSPOSE)
    almost_rectangle = (
        len(set(dominant_part)) == 1 or  # all parts equal
        len(set(dominant_T)) <= 2  # transpose has at most 2 distinct values
    )

    print(f"=== ⁶Li canonical atom-braid α* dominant partition ===\n")
    print(f"  Blocks evaluated: {len(evaled)}/{len(wb)}")
    print(f"  α* (witness):     {li6.get('psd_cone_alpha_star')}")
    print()
    print(f"  Predicted (rectangular conjecture):")
    print(f"    dominant λ*       = {PREDICTED_DOMINANT}")
    print(f"    dominant λ*^T     = {PREDICTED_TRANSPOSE}")
    print()
    print(f"  Observed:")
    print(f"    dominant λ*       = {dominant_part}   d_λ = {dominant['d_lambda']}")
    print(f"    dominant λ*^T     = {dominant_T}")
    print(f"    min_eig           = {dominant_min_eig:+.6e}")
    print(f"    α* (predicted)    = {predicted_alpha:.6f}")
    print()
    print(f"  RECTANGULAR MATCH:    {rectangle_match}")
    print(f"  ALMOST-RECTANGULAR:   {almost_rectangle}")
    print()

    # Top-5 most-negative
    print("  Top 5 most-negative min_eig:")
    for b in evaled_sorted[:5]:
        t = transpose(b["partition"])
        marker = "  ← rectangular" if (b["partition"] == PREDICTED_DOMINANT or
                                       t == PREDICTED_TRANSPOSE) else ""
        print(f"    {str(b['partition']):35s} d_λ={b['d_lambda']:>5d}  "
              f"min_eig={b['min_eigenvalue']:+.4e}  "
              f"λ^T={str(t):25s}{marker}")
    print()

    # Build witness
    out = WitnessBuilder("probe-4-li6-rectangular-conjecture", engine="python")
    out.set_description(
        "Tests the rectangular-form conjecture (dominant-partition audit "
        "2026-05-25) at the first heavier atom ⁶Li. Conjecture predicts "
        "dominant λ* = (6,6,6) with transpose (3,3,3,3,3,3) = 6 nucleons "
        "× 3 strands. Verifies/falsifies by reading the ⁶Li certificate "
        "after Rust registry extension."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-dominant-partition-nucleon-structure.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")

    top5 = [
        {
            "partition": b["partition"],
            "d_lambda": b["d_lambda"],
            "min_eig": b["min_eigenvalue"],
            "max_eig": b["max_eigenvalue"],
            "transpose": transpose(b["partition"]),
            "is_predicted_rectangle": (b["partition"] == PREDICTED_DOMINANT or
                                       transpose(b["partition"]) == PREDICTED_TRANSPOSE),
        }
        for b in evaled_sorted[:5]
    ]
    out.add_data("li6_dominant_data", {
        "n_blocks_evaluated": len(evaled),
        "n_blocks_total": len(wb),
        "alpha_star_witness": li6.get("psd_cone_alpha_star"),
        "alpha_star_predicted_from_min_eig": predicted_alpha,
        "dominant_partition": dominant_part,
        "dominant_transpose": dominant_T,
        "dominant_min_eig": dominant_min_eig,
        "predicted_dominant": PREDICTED_DOMINANT,
        "predicted_transpose": PREDICTED_TRANSPOSE,
        "rectangular_match": rectangle_match,
        "almost_rectangular": almost_rectangle,
        "top_5_most_negative_min_eig": top5,
    })

    out.add_assertion(
        name="li6_dominant_partition_matches_rectangular_conjecture",
        computed=str(int(rectangle_match)),
        expected="1",
        tolerance=0,
        source=f"dominant λ* = {dominant_part}, expected {PREDICTED_DOMINANT} (or transpose {PREDICTED_TRANSPOSE})",
    )

    if not rectangle_match:
        # Don't fail — falsification is a valid scientific result.
        out.add_caveat(
            f"FALSIFICATION: rectangular-form conjecture does NOT hold "
            f"at ⁶Li. Observed dominant λ* = {dominant_part} "
            f"(transpose {dominant_T}); predicted (6,6,6). The "
            f"Schur-Weyl correspondence observed at ⁴He appears to be "
            f"either A=4-specific or a small-A coincidence. The almost-"
            f"rectangular pattern (b) of the original conjecture may "
            f"still hold: dominant is {'almost-rectangle' if almost_rectangle else 'NOT almost-rectangle'}."
        )

    out.add_caveat(
        f"⁶Li has {len(evaled)}/{len(wb)} blocks evaluated under "
        f"--max-dim-psd 500. Skipped blocks may have more-negative "
        f"min_eig (forcing a different dominant partition). If "
        f"rectangle matches in the evaluated set, this is robust; if "
        f"NOT matching, increase --max-dim-psd to confirm the "
        f"falsification."
    )

    out.add_data("lean_uniqueness_ref", lean_uniqueness_ref("⁶Li"))
    out_path = out.save()
    print(f"Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
