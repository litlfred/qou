#!/usr/bin/env python3
"""
Identify which partition λ ⊢ n forces the small α* in the
Wedderburn-block PSD bisection per `solve_alpha_psd_letters`.

Per the witness `joint-tower-sdp-rust.witness.json` (post-R5.7-α,
PR #1283), the canonical atom-braid `T_w(Z, N)` has α* << 1 for
heavy atoms:

  deuteron-canonical-3A: α* = 0.193, gap = 0.807
  tritium-canonical-3A:  α* = 0.096, gap = 0.904
  helium3-canonical-3A:  α* = 0.091, gap = 0.909
  helium4-4He:           α* = 0.048, gap = 0.952

The α-bisection finds the largest α such that `α·ε + (1−α) ≥ 0`
for every eigenvalue ε across every block. The tightest constraint
is `ε_min ≤ 0` ⟹ α* = 1/(1 − ε_min). So the partition with the
MOST NEGATIVE min_eig forces α*.

This probe identifies the DOMINANT partitions per atom — the
critical irreducibles that the canonical T_w(Z, N) is most
"non-PSD" against. Structural meaning: these are the irreps that
the bar-anti-symmetric content of T_w lives in.

Bound to `conj:atom-braid-exterior-algebra` (PR #1271).
Audit-only.
"""

from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder


def alpha_star_from_min_eig(min_eig: float) -> float:
    """α* = 1/(1 − ε_min) if ε_min < 0; else 1."""
    if min_eig >= 0:
        return 1.0
    return 1.0 / (1.0 - min_eig)


def main() -> int:
    witness_path = Path(__file__).resolve().parent / "joint-tower-sdp-rust.witness.json"
    with open(witness_path) as f:
        w = json.load(f)

    target_atoms = [
        "deuteron-canonical-3A",
        "tritium-canonical-3A",
        "helium3-canonical-3A",
        "helium4-4He",
    ]

    out = WitnessBuilder("alpha-star-dominant-partitions", engine="python")
    out.set_description(
        "Identifies the partition λ ⊢ n forcing the smallest α* in each "
        "canonical atom-braid's Wedderburn-block PSD bisection. Per the "
        "α-bisection algebra (α·ε + (1−α) ≥ 0 ⟹ α ≤ 1/(1 − ε_min)), the "
        "partition with the most negative min_eig is the dominant "
        "constraint. Identifies which Wedderburn irreps the canonical "
        "atom-braid is most non-PSD against — structural fingerprint of "
        "where the bar-anti-symmetric content lives."
    )
    out.set_audit_only(
        "docs/audits/2026-05-25-option-e-crystal-weight-delta-lambda.md"
    )
    out.set_content_block("conj:atom-braid-exterior-algebra")

    all_results = {}
    for c in w["per_atom_certificates"]:
        name = c.get("name")
        if name not in target_atoms:
            continue
        wb = c.get("wedderburn_blocks") or []
        # Filter to evaluated blocks (non-empty eigvals)
        evaled = [b for b in wb if b.get("matrix_at_q_0_sym_eigvals")]
        if not evaled:
            continue

        # Sort by min_eig (most negative first)
        evaled_sorted = sorted(evaled, key=lambda b: b["min_eigenvalue"])

        dominant = evaled_sorted[0]
        min_eig = dominant["min_eigenvalue"]
        predicted_alpha = alpha_star_from_min_eig(min_eig)

        # Top-5 most negative
        top5 = [
            {
                "partition": b["partition"],
                "d_lambda": b["d_lambda"],
                "min_eig": b["min_eigenvalue"],
                "max_eig": b["max_eigenvalue"],
                "implied_alpha_cap": alpha_star_from_min_eig(b["min_eigenvalue"]),
            }
            for b in evaled_sorted[:5]
        ]

        result = {
            "name": name,
            "n_blocks_evaluated": len(evaled),
            "n_blocks_total": len(wb),
            "dominant_partition": dominant["partition"],
            "dominant_min_eig": min_eig,
            "predicted_alpha_star_from_min_eig": predicted_alpha,
            "top_5_most_negative_min_eig": top5,
        }
        all_results[name] = result

        print(f"=== {name} ===")
        print(f"  Blocks evaluated: {len(evaled)}/{len(wb)}")
        print(f"  Dominant partition: {dominant['partition']} (d_λ={dominant['d_lambda']})")
        print(f"  min_eig: {min_eig:+.6e}")
        print(f"  Predicted α* = 1/(1 − ε_min) = {predicted_alpha:.6f}")
        print(f"  Top 5 most-negative min_eig:")
        for b in top5:
            print(f"    {str(b['partition']):28s} d_λ={b['d_lambda']:>4d}  min_eig={b['min_eig']:+.4e}  → α ≤ {b['implied_alpha_cap']:.4f}")
        print()

    out.add_data("per_atom_dominant_partitions", all_results)

    # Headline assertion: predicted α* (from dominant partition) matches
    # the witness's reported α* to ≤ 1e-6
    all_match = True
    for atom, res in all_results.items():
        atom_cert = next(c for c in w["per_atom_certificates"] if c["name"] == atom)
        reported_alpha = atom_cert.get("psd_cone_alpha_star")
        predicted = res["predicted_alpha_star_from_min_eig"]
        if reported_alpha is not None:
            err = abs(predicted - reported_alpha)
            if err > 1e-6:
                all_match = False
                print(f"  MISMATCH {atom}: predicted {predicted:.10f} vs reported {reported_alpha:.10f}")

    out.add_assertion(
        name="dominant_partition_predicts_alpha_star",
        computed=str(int(all_match)),
        expected="1",
        tolerance=0,
        source="α* = 1/(1 − ε_min) per α-bisection algebra; cross-checks the cached α-solver in sdp_verifier.rs",
    )

    out.add_caveat(
        "α-bisection algebra: for α·ε + (1−α) ≥ 0, the tightest constraint "
        "is from the most-negative ε across all evaluated blocks. ⁴He has "
        "26/77 blocks evaluated under default --max-dim-psd 500 — the 51 "
        "skipped blocks may force a smaller α* if they have more-negative "
        "min_eig (would need higher --max-dim-psd to check)."
    )

    out_path = out.save()
    print(f"Witness: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
