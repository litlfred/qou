import Mathlib.Tactic
import QOU.BraidKnot.LightNucleus
import QOU.BraidKnot.WitnessR5Full

/-!
# QOU.BraidKnot.DeuteronWitness — placeholder R5-full witness for ²H

PR #608's R5-full search at L_max=8 returned `σ_2 σ_1^6 σ_2^{-1}`
as the deuteron winner — NOT the historical `6_2`.  This is the
"single-term cost function" failure: `B = m_e ρ |tr_M(T_w)|`
under-constrains the search and admits non-canonical PSD-feasible
candidates.

The full multi-term cost (T2-T6 of `thm:knot-mass-formula-unified`)
re-run is open work (PR #608 followup #1).  This module records a
PLACEHOLDER witness for ²H so the `R5FullWitness LightNucleus.deuterium`
typeclass resolves; concrete numerical values come from re-running
the search with the fixed cost function.

## What this module provides

- `instR5FullWitness_deuterium_placeholder` — placeholder witness
  with provisional values; flagged in the docstring as PENDING.

## Categorical significance

The instance lets downstream theorems compile under
`[R5FullWitness LightNucleus.deuterium]`, but the values are
provisional: closing the actual deuteron uniqueness (i.e.
showing the canonical knot is `6_2`) requires the multi-term
cost re-run.

## References

- `r5-full-canonical-knot-solver.witness.json` (current single-term)
- PR #608 followup #1 (multi-term cost wiring)
- `thm:knot-mass-formula-unified` (the full T2-T6 formula)
-/

namespace QOU.BraidKnot

/-- **Placeholder R5-full witness for ²H** — marks the multi-
    term cost dependency.  Provisional values: `α_gap = 0`
    (PSD-feasible), `ρ⋆ = 1` (single-term winner; will change
    under multi-term cost), strong-duality slack = 0.

    Intentionally NOT registered as a global `instance` (per
    Copilot review — placeholder values shouldn't be picked up
    silently by typeclass resolution).  Downstream theorems that
    need a deuteron witness must consume this `def` explicitly. -/
def witnessR5Full_deuterium_placeholder :
    R5FullWitness LightNucleus.deuterium where
  alpha_gap := 0
  alpha_gap_nonneg := le_refl 0
  primal_obj := 1
  dual_obj := 1
  duality_gap_le := by
    -- |1 - 1| = 0 ≤ 10⁻⁶ trivially; `simp` discharges it fully
    simp
  rho_star := 1
  rho_star_pos := by decide

end QOU.BraidKnot
