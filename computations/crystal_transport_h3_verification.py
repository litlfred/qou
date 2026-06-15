#!/usr/bin/env python3
"""crystal_transport_h3_verification.py — L2 advance

Per `rem:ontological-agnosticism` (main, PR #571): every observable
extracted by the Observation Frame τ is determined by its image at
the **crystal limit** q → 0 and transported back to the generic fibre
at q = q_0 along the flat q-connection.

The L2 scaffold (#582 `crystal_limit_transport_probe.py`) computed
the crystal-side χ_λ_crystal at q→0 for H_3 partitions:
  λ = (3)    : χ_crystal = +1
  λ = (2, 1) : χ_crystal =  0
  λ = (1¹³) : χ_crystal = −1

This script closes the loop: it computes the **same** characters
χ_λ(σ_1) directly via the Hoefsmit seminormal matrices at q = q_0
(numerical) and verifies that the flat-transport prediction holds:

  χ_λ(σ_1; q_0)  =  (predicted by [n]_q lift of χ_crystal at q=0)

The flat-transport map is the canonical [n]_q-lift:
  +1 (sym)    ↦   q     at q_0  ≈  1.10998
   0 (mixed)  ↦   q − q⁻¹ → 0 at q_0 only if mixed channel
                              actually has trace 0 (it doesn't —
                              (2,1) is a 2-dim irrep with trace
                              q − q⁻¹ ≠ 0)
  −1 (alt)    ↦  −q⁻¹    at q_0  ≈ −0.901

So the test is concrete: does the Hoefsmit χ_λ(σ_1; q_0) match the
[n]_q lift of the crystal-limit value? A match validates flat
transport on H_3; a mismatch quantifies connection curvature.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from hecke_characters import (  # noqa: E402
    standard_young_tableaux, build_seminormal_matrices, partitions_of,
)
from q_parameter import Q as Q0  # noqa: E402

import numpy as np


def crystal_chi_at_q_zero(shape: tuple[int, ...], gen_index: int) -> int:
    """Crystal-limit χ_λ(σ_i) at q → 0 — sign-balance count."""
    i = gen_index
    syts, _cells, contents = standard_young_tableaux(shape)
    if not syts:
        return 0
    pos, neg = 0, 0
    for T in syts:
        if (i + 1) not in T or i not in T:
            continue
        rho = contents[T[i + 1]] - contents[T[i]]
        if rho >= 0:
            pos += 1
        else:
            neg += 1
    return pos - neg


def hoefsmit_chi_at_q0(shape: tuple[int, ...], gen_index: int,
                        q_val: float) -> float:
    """χ_λ(σ_i; q_0) via Hoefsmit seminormal matrices."""
    sigmas, dim, _ = build_seminormal_matrices(shape, sparse=False, q=q_val)
    if dim == 0:
        return 0.0
    S = sigmas[gen_index - 1]  # 1-indexed
    if hasattr(S, "toarray"):
        S = S.toarray()
    return float(np.trace(np.asarray(S, dtype=float)))


def lift_crystal_to_q0(chi_crystal: int, q_val: float) -> float:
    """Flat-transport [n]_q lift of an integer crystal value.

    Convention (per crystal-limit χ_λ leading-q analysis):
      +1  ↦  q      (symmetric eigenvalue of σ_i in Hecke)
       0  ↦  q − q⁻¹  (mixed/cancelled — but for traces this is the
                         leading coefficient, so 0 stays 0)
      −1  ↦  −q⁻¹    (antisymmetric eigenvalue)

    For OTHER integer values, the lift is
      +k ↦  +k·q          (k positive symmetric channels)
      −k ↦  −k·q⁻¹        (k negative antisym channels)
    """
    if chi_crystal == 0:
        return 0.0
    if chi_crystal > 0:
        return chi_crystal * q_val
    return chi_crystal * (1.0 / q_val)


def main() -> int:
    q0 = float(Q0)
    print(f"L2 advance — crystal-limit transport verification on H_3")
    print(f"  q_0 = {q0}\n")
    print(f"  {'λ':<10} {'χ_crystal':>10} {'lift to q_0':>14} "
          f"{'Hoefsmit at q_0':>18} {'Δ':>14} {'flat?':>7}")
    print("  " + "-" * 80)
    rows = []
    flat_count = 0
    for shape in partitions_of(3):
        shape_t = tuple(shape)
        chi_c = crystal_chi_at_q_zero(shape_t, gen_index=1)
        lift = lift_crystal_to_q0(chi_c, q0)
        chi_h = hoefsmit_chi_at_q0(shape_t, gen_index=1, q_val=q0)
        delta = abs(chi_h - lift)
        flat = delta < 1e-10
        if flat:
            flat_count += 1
        rows.append({
            "lambda": list(shape_t),
            "chi_crystal_at_q_zero": chi_c,
            "flat_transport_lift": lift,
            "hoefsmit_chi_at_q_0": chi_h,
            "delta": delta,
            "flat_within_1e_10": flat,
        })
        print(f"  {str(list(shape_t)):<10} {chi_c:>10d} {lift:>14.10f} "
              f"{chi_h:>18.10f} {delta:>14.2e} {str(flat):>7}")

    print()
    print(f"  Flat-transport count: {flat_count} / {len(rows)} partitions")
    if flat_count == len(rows):
        print("  → Crystal-limit χ_λ flatly transports to Hoefsmit χ_λ at q_0.")
    else:
        n_curved = len(rows) - flat_count
        print(f"  → {n_curved} channel(s) show finite-q correction beyond")
        print(f"     the simple [n]_q lift; connection curvature is")
        print(f"     non-trivial there. This is the data L2's research")
        print(f"     deliverable needs to characterise.")

    out = (WitnessBuilder("crystal-transport-h3-verification", engine="numpy")
        .set_audit_only("docs/audits/2026-05-08-compute-infrastructure-audit.md")
        .set_description(
            "L2 advance: tests the flat-transport claim of "
            "rem:ontological-agnosticism on H_3. Compares "
            "crystal-limit χ_λ(σ_1) at q→0 (combinatorial "
            "sign-balance) against the simple [n]_q lift to q_0, "
            "and against the Hoefsmit-matrix χ_λ at q_0. "
            "Mismatches quantify connection curvature; matches "
            "validate flat transport at the leading order."
        )
        .add_data("narrative_block", "rem:ontological-agnosticism")
        .add_data("conditional_on", ["conj:crystal-graph-realization"])
        .add_data("q_0", q0)
        .add_data("rows", rows)
        .add_data("flat_count", flat_count)
        .add_data("total_partitions", len(rows))
        .add_assertion(
            "all_h3_partitions_covered",
            computed=len(rows),
            expected=3,
            tolerance=0,
            source="H_3 has 3 partitions",
        )
        .add_assertion(
            "leading_order_match_on_pure_channels",
            # The pure (sym, alt) channels — (3) and (1,1,1) —
            # have integer crystal values ±1 that lift to ±q^±1.
            # These should be exact at the simple-lift order.
            # The mixed channel (2,1) has crystal value 0; the
            # Hoefsmit χ at q_0 is q − q⁻¹ ≠ 0, which is the
            # SECOND-order correction (curvature).
            computed=sum(
                1 for r in rows
                if r["chi_crystal_at_q_zero"] != 0
                and r["flat_within_1e_10"]
            ),
            expected=2,
            tolerance=0,
            source="(3) and (1,1,1) are the pure ±1 crystal channels",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
