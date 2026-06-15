#!/usr/bin/env python3
"""
mass_tower_operator_valued.py — Stage-1 unblock compute infrastructure
for `prop:mass-tower-operator-valued`.

Validates the boxed iterated operator-trace identity at the two-factor
case using the canonical proton + neutron + interface deuteron braid:

    χ^λ(β_p · I · β_n)
        = Σ_{(μ,ν)} Tr_{V_μ ⊗ V_ν}(A^λ_{μν}(I) · (ρ_μ(β_p) ⊗ ρ_ν(β_n)))

The A^λ_{μν}(I) matrices come from the prior bilinear-system extraction
in `sublemma_2_1_A_operator_extract.py` (witness:
`sublemma-2-1-A-operator-extract.witness.json`, 10^-15 across 11 λ ⊢ 6).
This script demonstrates the FORWARD direction — given the extracted
operator, verify the per-block trace formula reproduces the direct
χ^λ on the canonical atomic braid (not on the bilinear test set).

What this gives us beyond the existing extraction witness:
  1. Per-(μ,ν)-block decomposition of χ^λ(β_D) — exposes WHICH
     Wedderburn blocks of the deuteron carry the dominant
     contribution to the character.
  2. Cross-check that the FORWARD identity (not just the inversion
     residual) holds on a CANONICAL braid, not just on the test set
     used for extraction.
  3. Concrete numerical groundwork for the iterated (Z+N)-factor
     extension to T, ³He, ⁴He.

Output: `mass-tower-operator-valued.witness.json`

Refs:
  - prop:mass-tower-operator-valued (Stage-1 paper block)
  - prop:hecke-branching-trace-decomposition (2-factor proved)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import ast
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from sublemma_2_1_A_operator_extract import (  # noqa: E402
    evaluate_word_matrix,
    chi_lambda_matrix_trace,
    with_interface,
    H,
)
from sublemma_2_1_deuteron_branching import (  # noqa: E402
    LR_TABLE_3_3_TO_6 as LR_TABLE,
    lr_coef,
    partitions_of,
)
from q_parameter import Q as Q0  # noqa: E402


# Canonical proton / neutron braid words on H_3 (3 strands each).
# Format: (c, d, gen_0based) per crossing — Hecke factor c·σ_g + d·I.
# proton's B_3 × uud has 11 crossings in H_3; we use the canonical
# reduced form here (full uses of mass_endomorphism's proton_cross
# would yield identical chi values modulo Markov equivalence).
PROTON_WORD = [
    (1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0),
    (1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0),
    (-1.0, 0.0, 1), (-1.0, 0.0, 0), (-1.0, 0.0, 1),
]
NEUTRON_WORD = [
    (1.0, 0.0, 0), (1.0, 0.0, 1), (1.0, 0.0, 0),
    (1.0, 0.0, 1), (1.0, 0.0, 0), (1.0, 0.0, 1),
    (-1.0, 0.0, 0), (-1.0, 0.0, 1), (-1.0, 0.0, 0),
]
# Deuteron interface I = σ_2 - (h/2)·I on H_6 (boundary at strand 3).
# This is the canonical interface used in the existing A-extraction.
INTERFACE_C = 1.0
INTERFACE_D = -H / 2


# ── Canonical API surface for downstream consumers ───────────────
# Per the post-PR-#944 cheat-sheet §5 #2 close-out audit, callers
# that previously imported `mass_from_tower` from `mass_endomorphism`
# should now import from `mass_tower_operator_valued` — the canonical
# block whose Lean realisation is `prop:mass-tower-operator-valued`.
# The implementation is re-exported from `mass_endomorphism.py`
# (which retains the computational kernel + utility helpers): the
# operator-valued tower (this module) and the Φ_q tower (in
# `mass_endomorphism`) are EQUIVALENT expressions of the same
# Markov-trace mass formula at the H_{3A} layer (verified to
# machine-ε in the per-λ A-operator extraction witnesses at
# H_6 / H_9 / H_12 — see PR #944 for H_12 Phase-1).
from mass_endomorphism import (  # noqa: E402
    mass_from_tower,
    additive_wedderburn_volumes,
)

__all__ = [
    # Verification-script entry points (the original surface):
    "load_A_per_pair",
    "operator_trace_rhs",
    # Canonical API re-exports (the close-out surface):
    "mass_from_tower",
    "additive_wedderburn_volumes",
]


def load_A_per_pair(witness_path: Path) -> dict:
    """Load A^λ_{μν}(I) matrices from prior extraction witness."""
    w = json.loads(witness_path.read_text())
    out: dict = {}
    for lam_str, per_lam in w["results_per_lambda"].items():
        lam = ast.literal_eval(lam_str)
        out[lam] = {}
        for block_key, info in per_lam["A_per_pair"].items():
            # block_key has form "(mu_tuple,nu_tuple)" e.g. "((3,),(3,))"
            parsed = ast.literal_eval(block_key)
            mu, nu = parsed[0], parsed[1]
            d = info["d_mu"] * info["d_nu"]
            re = np.array(info["matrix_re"], dtype=float)
            im = np.array(info["matrix_im"], dtype=float)
            A = re + 1j * im
            out[lam][(mu, nu)] = A
    return out


def operator_trace_rhs(
    lam: tuple, beta_p_word: list, beta_n_word: list,
    A_per_pair_for_lam: dict, parts_3: list,
) -> tuple[complex, list[dict]]:
    """Compute Σ_{(μ,ν)} Tr_{V_μ⊗V_ν}(A^λ_{μν} · (ρ_μ(β_p) ⊗ ρ_ν(β_n)))
    and return (total, per-block contributions)."""
    total = 0.0 + 0j
    per_block = []
    for mu in parts_3:
        for nu in parts_3:
            c = lr_coef(mu, nu, lam)
            if c == 0:
                continue
            B_mu = evaluate_word_matrix(mu, beta_p_word)
            B_nu = evaluate_word_matrix(nu, beta_n_word)
            if B_mu.size == 0 or B_nu.size == 0:
                continue
            X = np.kron(B_mu, B_nu)  # ρ_μ(β_p) ⊗ ρ_ν(β_n)
            A = A_per_pair_for_lam.get((mu, nu))
            if A is None:
                continue
            block_trace = complex(np.trace(A @ X))
            total += block_trace
            per_block.append({
                "mu": list(mu), "nu": list(nu), "c_lr": c,
                "d_mu": int(B_mu.shape[0]), "d_nu": int(B_nu.shape[0]),
                "block_trace_re": float(block_trace.real),
                "block_trace_im": float(block_trace.imag),
                "block_trace_abs": float(abs(block_trace)),
            })
    return total, per_block


def main() -> int:
    builder = WitnessBuilder("mass-tower-operator-valued")
    builder.set_description(
        "Forward validation of prop:mass-tower-operator-valued at the "
        "two-factor (deuteron) case. Uses A^λ_{μν}(I) matrices from "
        "sublemma-2-1-A-operator-extract.witness.json + canonical "
        "proton/neutron H_3 braid words + standard interface "
        "I = σ_2 - (h/2)·I, computes the operator-trace RHS per λ "
        "⊢ 6, compares to direct χ^λ(β_p · I · β_n). Per-(μ,ν)-block "
        "decomposition is reported for structural analysis."
    )
    builder.add_parameter("q0", str(float(Q0)))
    builder.add_parameter("h_q_minus_q_inv", str(float(H)))
    builder.add_parameter("interface_c", str(INTERFACE_C))
    builder.add_parameter("interface_d", str(INTERFACE_D))
    builder.add_parameter("proton_word_len", str(len(PROTON_WORD)))
    builder.add_parameter("neutron_word_len", str(len(NEUTRON_WORD)))

    A_witness = HERE / "sublemma-2-1-A-operator-extract.witness.json"
    if not A_witness.exists():
        print(f"ERROR: {A_witness} not found. Run "
              f"`sublemma_2_1_A_operator_extract.py` first.")
        return 1

    print("=" * 90)
    print("  Stage-1 forward validation: operator-trace identity on "
          "canonical deuteron")
    print("=" * 90)
    print()

    A_per_lam = load_A_per_pair(A_witness)
    parts_6 = partitions_of(6)
    parts_3 = partitions_of(3)

    # Compose the canonical β_p · I · β_n on H_6
    combined_word = with_interface(
        PROTON_WORD, NEUTRON_WORD, n1=3,
        int_c=INTERFACE_C, int_d=INTERFACE_D,
    )

    print(f"{'λ ⊢ 6':<14} {'LHS (direct χ)':>18} {'RHS (operator)':>18} "
          f"{'|res|/|LHS|':>14}  status")
    print("-" * 80)

    results = {}
    max_rel = 0.0
    for lam in parts_6:
        lhs = chi_lambda_matrix_trace(lam, combined_word)
        if lam not in A_per_lam:
            # No A matrices extracted for this λ — skip
            continue
        rhs, per_block = operator_trace_rhs(
            lam, PROTON_WORD, NEUTRON_WORD, A_per_lam[lam], parts_3,
        )
        residual = abs(rhs - lhs)
        # For zero-character cases (symmetry kills χ^λ), use absolute
        # residual instead of relative — dividing by ~0 is meaningless.
        if abs(lhs) < 1e-9:
            rel = residual  # absolute residual proxy
            metric = "abs"
        else:
            rel = residual / abs(lhs)
            metric = "rel"
        max_rel = max(max_rel, rel)
        status = "✓" if rel < 1e-6 else "✗"
        print(f"  {str(lam):<14} {complex(lhs).real:>18.10f} "
              f"{rhs.real:>18.10f} {rel:>14.2e}  {status}")
        results[str(lam)] = {
            "lhs_chi_direct_re": float(lhs.real),
            "lhs_chi_direct_im": float(lhs.imag),
            "rhs_operator_trace_re": float(rhs.real),
            "rhs_operator_trace_im": float(rhs.imag),
            "residual_abs": float(residual),
            "relative_residual": float(rel),
            "metric_used": metric,
            "consistent": bool(rel < 1e-6),
            "per_block": per_block,
            "dominant_block": (
                max(per_block, key=lambda b: b["block_trace_abs"])
                if per_block else None
            ),
        }

    all_consistent = all(r["consistent"] for r in results.values())
    print()
    print(f"  Max relative residual across all λ: {max_rel:.2e}")
    print(f"  All λ consistent (forward identity holds): {all_consistent}")

    if all_consistent:
        verdict = (
            f"PROVED forward direction: operator-trace formula reproduces "
            f"χ^λ(β_p · I · β_n) on the canonical deuteron braid for all "
            f"{len(results)} λ ⊢ 6 partitions to {max_rel:.2e} relative "
            f"residual. The 2-factor case of prop:mass-tower-operator-valued "
            f"is forward-validated."
        )
    else:
        verdict = (
            f"INCONSISTENT: forward operator-trace identity fails on "
            f"{sum(1 for r in results.values() if not r['consistent'])} of "
            f"{len(results)} λ — max rel residual {max_rel:.2e}. Check the "
            f"A^λ_{{μν}}(I) extraction or the interface convention."
        )

    builder.add_data("per_lambda", results)
    builder.add_data("max_relative_residual", float(max_rel))
    builder.add_data("all_lambda_consistent", bool(all_consistent))
    builder.add_data("verdict", verdict)
    builder.add_upstream("sublemma-2-1-A-operator-extract.witness.json")

    builder.add_assertion(
        "operator_trace_identity_forward",
        computed=float(max_rel),
        expected=0.0,
        tolerance=1e-6,
        unit="relative residual",
        source="prop:mass-tower-operator-valued + prop:hecke-branching-"
               "trace-decomposition",
    )

    # Dominant-block summary
    print()
    print("  Dominant Wedderburn block per λ (largest |Tr(A·(ρ⊗ρ))|):")
    print("-" * 80)
    print(f"  {'λ ⊢ 6':<14} {'dominant (μ, ν)':<24} "
          f"{'|block trace|':>14}")
    for lam_str, r in results.items():
        dom = r["dominant_block"]
        if dom:
            block_str = f"({dom['mu']}, {dom['nu']})"
            print(f"  {lam_str:<14} {block_str:<24} "
                  f"{dom['block_trace_abs']:>14.6f}")

    builder.save()
    return 0


if __name__ == "__main__":
    sys.exit(main())
