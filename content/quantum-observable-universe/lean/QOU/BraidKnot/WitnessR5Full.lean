import Mathlib.Tactic
import QOU.BraidKnot.LightNucleus

/-!
# QOU.BraidKnot.WitnessR5Full

The R5-full SDP-search numerical certificate (PR #608) for a
light nucleus.  Mirrors the `R5FullWitness` class declared in
the content-block file
`content/quantum-observable-universe/braids-and-knots/conj-canonical-knot-id-sdp.lean`
into the Lake-tracked tree.

## What this module provides

- `R5FullWitness n` — typeclass with the empirical SDP-search
  data: α-gap, primal/dual objectives, optimal multiplicity ρ⋆.
- `StrictComplementarityCert n` — companion certificate (also
  mirroring the content-block declaration).

## Concrete instances

The `Helium3Witness` module (separate file) registers the
hardcoded numerical instance for `³He` with the values from
`r5-full-canonical-knot-solver.witness.json` (PR #608):
- `alpha_gap := 0`
- `rho_star := 3`
- `min_block_eigs := [1.87, 0.53, 0.53]` (all positive, active
  set empty)

## References

- `r5-full-canonical-knot-solver.witness.json` (PR #608)
- `binding-k-solver.witness.json` (PR #604 deliverable 4)
-/

namespace QOU.BraidKnot

/-- **R5-full numerical witness** for nucleus `n`.  Records the
    empirical SDP-search outputs that PR #608's
    `r5_full_canonical_knot_solver.py` produces. -/
class R5FullWitness (n : LightNucleus) where
  /-- α-gap from the SDP search (PSD-feasible iff `= 0`). -/
  alpha_gap : ℝ
  /-- α-gap is non-negative (PSD-feasibility direction). -/
  alpha_gap_nonneg : 0 ≤ alpha_gap
  /-- Primal objective at the search winner. -/
  primal_obj : ℝ
  /-- Dual objective at the search winner. -/
  dual_obj : ℝ
  /-- Strong duality at the working precision (10⁻⁶ ≈ ε of
      double-precision SDP solver). -/
  duality_gap_le : |primal_obj - dual_obj| ≤ (10 : ℝ)⁻¹^6
  /-- The optimal multiplicity ρ⋆ (≥ 1). -/
  rho_star : ℕ
  /-- ρ⋆ is positive. -/
  rho_star_pos : 0 < rho_star

/-- **Strict-complementarity certificate** for nucleus `n`.
    Records the dual-side data from the SDP search that
    distinguishes active vs inactive constraints.  Mirrors the
    `StrictComplementarity` structure in the content-block
    file. -/
structure StrictComplementarityCert (n : LightNucleus)
    [_w : R5FullWitness n] where
  /-- Minimum eigenvalue across all Wedderburn blocks in the
      witness's `per_block_summary`. -/
  min_block_eig : ℝ
  /-- Minimum dual variable on the active set. -/
  min_dual_y_on_active : ℝ
  /-- Maximum dual variable on the inactive set. -/
  max_inactive_dual : ℝ
  /-- Either the active set is non-empty with positive duals, or
      the optimum lies in the strict interior. -/
  active_dual_pos_or_empty : 0 < min_dual_y_on_active ∨ 0 < min_block_eig
  /-- Inactive duals are exactly zero. -/
  inactive_dual_zero : max_inactive_dual = 0

end QOU.BraidKnot
