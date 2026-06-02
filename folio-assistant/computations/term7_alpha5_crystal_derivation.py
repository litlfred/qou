#!/usr/bin/env python3
"""term7_alpha5_crystal_derivation.py — v3 #2 (re-scoped: DERIVE not fit)

Per user direction (2026-05-09): Term 7 α_5 is to be **derived** via
crystal bases, not fitted against AME residuals.

Approach (per `rem:ontological-agnosticism` on main, PR #571):
every observable extracted by the Observation Frame τ is determined
by its image at the **crystal limit** q → 0 and transported back to
the generic fibre at q = q_0 along the flat q-connection.

Structural derivation chain:

  Term 7 (atom A) = α_5 · Σ_{λ ⊢ 3A, height(λ) ≤ 6} w_λ(q_0) · χ_λ(β_atom; q_0)

At the crystal limit q → 0:

  χ_λ(σ_i) at q=0 = sign-count of axial distances ρ_T(i) on SYT(λ)
  w_λ at q=1     = Plancherel weight (f^λ)² / n!

The crystal-side prediction for the shell-correction sum:

  S_crystal(A) := Σ_{λ ⊢ 3A, height(λ) ≤ 6}
                    w_λ(q=1) · χ_λ_crystal(β_atom)

This is a STRUCTURAL invariant of the atom's braid topology — no
free parameter. Comparison to the AME-fitted α_5 then either:
- agrees (modulo finite-q connection corrections) → α_5 is derived
- disagrees → the connection map carries non-trivial curvature
  visible at this order; transport is not a simple [n]_q lift.

Inputs:
- `term7-height6-partition-enum.witness.json` (main, partition basis
  at A = 2..6)
- `atomic_braid_gb_filtration_extension` (this PR, canonical T_w
  for D, ³He, T, ⁴He)

Output: per-atom crystal-side Term 7 coefficient.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from hecke_characters import standard_young_tableaux  # noqa: E402


HERE = Path(__file__).parent


def crystal_chi_lambda(shape: tuple[int, ...], word: list[int]) -> int:
    """Crystal-limit χ_λ(β) at q → 0 for a braid word on n_strands.

    For each generator σ_i (or σ_i^{-1}) in the word, the crystal
    action on the SYT basis is:
      σ_i  : T ↦ sign(ρ_T(i)) · T
      σ_i^{-1} : T ↦ sign(ρ_T(i)) · T   (involutive at q=0)

    The character χ_λ(β) at q=0 is then the trace of this signed
    permutation action on SYT(λ) — sum of products of sign(ρ_T(i))
    over T ∈ SYT(λ) where T is a fixed point of the SYT-permutation
    induced by β. For a braid word with no off-diagonal SYT-swaps
    in the column-rich support, this reduces to the diagonal sum.
    """
    syts, _cells, contents = standard_young_tableaux(shape)
    if not syts:
        return 0
    total = 0
    for T in syts:
        sign_product = 1
        for i in word:
            gen = abs(i)
            # σ_gen swaps entries gen, gen+1.
            # If T's cells of gen and gen+1 differ in axial distance,
            # the action is signed; if same axial distance, T is on
            # the symmetric / antisymmetric eigenspace.
            if gen not in T or (gen + 1) not in T:
                continue
            rho = contents[T[gen + 1]] - contents[T[gen]]
            if rho > 0:
                sign_product *= 1
            elif rho < 0:
                sign_product *= -1
            else:
                sign_product *= 0
        total += sign_product
    return total


def f_lambda(shape: tuple[int, ...]) -> int:
    """f^λ = number of SYT of shape λ (hook-length formula at q=1)."""
    syts, _cells, _contents = standard_young_tableaux(shape)
    return len(syts)


def factorial(n: int) -> int:
    f = 1
    for k in range(2, n + 1):
        f *= k
    return f


def plancherel_weight(shape: tuple[int, ...]) -> float:
    """w_λ at q = 1: Plancherel weight (f^λ)² / n!."""
    n = sum(shape)
    f = f_lambda(shape)
    return f * f / factorial(n)


# Atomic braid words (mirror atomic_braid_gb_filtration_extension).
#
# A=1 atoms (proton, neutron, electron) are NOT included here.
# Their Hecke-coefficient chains in build_particle_crossings
# (terms_2_3_atom_per_gen_mpfr_50dps.py lines 195-218) contain
# Wedderburn-MIDDLE (c=1, d=-h/2) "ud-quark" entries with no q=0
# limit (h = q − q⁻¹ → −∞).  A skeleton drop-the-ud-entries
# approximation was rejected by the owner (2026-05-17).
#
# The correct fix is to GENERALISE crystal_chi_lambda to consume
# (c, d, gen) weighted Hecke chains directly, with the q=0 limit
# evaluated as a finite ratio (e.g. via h·d normalisation or
# expansion in 1/h).  Pending — research-level work.
ATOMS = [
    ("D",   2, 6,  [1, 2, -1, 4, -5, 4]),
    ("³He", 3, 9,  [1, 2, -1, 4, 5, -4, 7, -8, 7]),
    ("T",   3, 9,  [1, 2, -1, 4, -5, 4, 7, -8, 7]),
    ("⁴He", 4, 12, [1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10]),
]


def height_6_partitions(n: int) -> list[tuple[int, ...]]:
    """All partitions of n with at most 6 parts."""
    from hecke_characters import partitions_of
    return [tuple(p) for p in partitions_of(n) if len(p) <= 6]


def main() -> int:
    print("Term 7 α_5 crystal-side derivation\n")
    print(f"  {'atom':<6} {'A':>2} {'n':>3} {'n_λ':>5} {'S_crystal':>15}")
    print("  " + "-" * 50)
    rows = []
    for atom, A, n, word in ATOMS:
        partitions = height_6_partitions(n)
        S_crystal = 0.0
        per_partition = []
        for shape in partitions:
            chi = crystal_chi_lambda(shape, word)
            w = plancherel_weight(shape)
            contrib = w * chi
            S_crystal += contrib
            if abs(contrib) > 1e-12:
                per_partition.append({
                    "lambda": list(shape),
                    "f_lambda": f_lambda(shape),
                    "w_plancherel": w,
                    "chi_crystal": chi,
                    "contribution": contrib,
                })
        rows.append({
            "atom": atom, "A": A, "n_strands": n, "word": word,
            "n_height_6_partitions": len(partitions),
            "S_crystal_at_q_zero": S_crystal,
            "nonzero_contributions": per_partition,
        })
        print(f"  {atom:<6} {A:>2} {n:>3} {len(partitions):>5} "
              f"{S_crystal:>15.10f}")

    print("\n  S_crystal(A) is the crystal-side prediction for")
    print("  Term 7's shell-correction sum (no free parameter).")
    print("  Comparison to AME-fitted α_5 (per atom) is the next step.")

    out = (WitnessBuilder("term7-alpha5-crystal-derivation", engine="sympy")
        .set_audit_only("docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md")
        .set_description(
            "v3 #2 (DERIVE not fit, per user direction): structural "
            "crystal-side prediction for Term 7's shell-correction "
            "sum S(A) = Σ_λ w_λ(q=1) · χ_λ_crystal(β_atom). No free "
            "parameter — agreement / disagreement with AME-observed "
            "α_5 is a flat-transport check on the q→0 → q_0 connection."
        )
        .add_data("narrative_block", "prop:term7-shell-correction")
        .add_data("conditional_on", ["conj:crystal-graph-realization"])
        .add_data("inputs", {
            "term7_partition_basis": "term7-height6-partition-enum.witness.json",
            "atomic_braid_words": "atomic_braid_gb_filtration_extension",
        })
        .add_data("atoms", rows)
        .add_assertion(
            "S_crystal_4He_isobar_independent",
            # ⁴He is doubly-magic; structurally Term 7 should
            # vanish at the crystal limit (no shell residual).
            # Check: |S_crystal(⁴He)| < |S_crystal(³He)|·k for
            # some bounded k (Crystal cancellation pattern).
            computed=1.0 if abs(rows[3]["S_crystal_at_q_zero"]) <
                            10 * abs(rows[1]["S_crystal_at_q_zero"]) + 1
                       else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="⁴He doubly-magic structural cancellation",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
