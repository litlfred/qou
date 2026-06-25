import Mathlib.Tactic
import QOU.HeckeAlgebra.Common
import QOU.HeckeAlgebra.QSubstrate
import QOU.BraidKnot.LightNucleus
import QOU.BraidKnot.WitnessR5Full
import QOU.BraidKnot.Helium3Witness
import QOU.BraidKnot.DeuteronWitness
import QOU.BraidKnot.TritiumWitness
import QOU.BraidKnot.MassFormulaCategorical

/-!
# QOU.BraidKnot.PerNucleusMassDerivation

Per-nucleus instantiation of the categorical mass formula
`M = ρ · m_e · |tr_M(T_w)|` for `{²H, ³H, ³He}`.  Combines the
`R5FullWitness` data (which fixes ρ⋆) with the abstract
`MassFormulaCategorical` to produce concrete Lean-typed mass
predictions.

## Mathematical content

For each light nucleus `n`:
- `ρ(n) := w.rho_star` (from the registered `R5FullWitness n`)
- `T_w(n)` is the canonical Hecke element (currently a
  placeholder element of `HeckeElement n.n₀` pending the
  algebra-evaluation port)
- `M_pred(n) := ρ(n) · m_e · |tr_M(T_w(n))|`

The numerical conversion to MeV uses
`m_e_MeV_codata := 0.51099895069` from
`MassFormulaCategorical`.

## What this module provides

- `nucleusMass n` — the categorical mass prediction at the
  Hecke-element level (placeholder T_w)
- `nucleusMassMeV n` — the MeV-converted prediction
- `nucleusMass_nonneg n` — non-negativity proof

## Open Lean port

The placeholder `T_w(n) := 0` ensures the mass is zero — the
real values come from the Hoefsmit-evaluated braid words once
that port lands.  This module captures the schematic structure;
concrete values follow.

## References

- `prop:atom-knot-mass-derivation` (the formula)
- `QOU.BraidKnot.MassFormulaCategorical` (the abstract formula)
- `QOU.BraidKnot.{Helium3,Deuteron,Tritium}Witness` (R5-full data)
-/

namespace QOU.BraidKnot.PerNucleusMassDerivation

noncomputable section

open QOU.HeckeAlgebra QOU.BraidKnot QOU.BraidKnot.MassFormulaCategorical

/-- **Cat-units electron mass** placeholder.  Real value comes
    from the proton chain's `m_e_Hecke ≈ 0.0007783` (per
    `derivation_chain.M_HECKE_PIPELINE_AT_Q0`).

    **`def` form (was previously an `axiom`).**  Discharged
    2026-06-07 by binding to the witness's approximate value
    `0.0007783`. The axiom previously committed to no value
    (only existence) and let downstream proofs use it
    opaquely; the only theorem that depended on `m_e_cat`
    semantically was `m_e_cat_pos`, which now follows by
    `norm_num` from the literal. Other consumers
    (`nucleusMass`, `nucleusMassMeV`) treat `m_e_cat` as a
    scalar and do not care about its exact value. A future
    refactor will rebind this `def` to the Hecke-port output
    once the categorical pipeline returns a Lean-typed real;
    every downstream proof continues to type-check unchanged.

    Until then, the literal acts as a *placeholder witness*
    (same role as the axiom, but with positivity provable). -/
noncomputable def m_e_cat : ℝ := 0.0007783

/-- **Theorem** (was previously an axiom; discharged 2026-06-07).
    Positivity of `m_e_cat` follows from the placeholder literal
    being positive. -/
theorem m_e_cat_pos : 0 < m_e_cat := by
  unfold m_e_cat
  norm_num

/-- **Placeholder T_w element** for nucleus `n` — currently the
    zero element of `HeckeElement n.n₀`. Real values come from
    `braidWordEval n.n₀ <bindingKWord n>` once the algebra
    evaluation map is concretely defined.

    The placeholder makes the mass formula type-check and gives
    a (vacuous, zero-valued) prediction; downstream theorems
    will substitute real T_w values. -/
def placeholder_T_w (n : LightNucleus) : HeckeElement n.n₀ :=
  -- Zero element; downstream theorems substitute real values.
  (0 : HeckeElement n.n₀)

/-- **Categorical mass prediction** for nucleus `n`, using the
    R5-full witness's `rho_star` and the placeholder T_w. -/
def nucleusMass (n : LightNucleus) [w : R5FullWitness n] : ℝ :=
  categoricalMass w.rho_star m_e_cat (placeholder_T_w n)

/-- **MeV-converted mass prediction**. -/
def nucleusMassMeV (n : LightNucleus) [w : R5FullWitness n] : ℝ :=
  categoricalMassMeV w.rho_star m_e_cat (placeholder_T_w n)

/-- The categorical mass prediction is non-negative. -/
theorem nucleusMass_nonneg (n : LightNucleus) [_w : R5FullWitness n] :
    0 ≤ nucleusMass n := by
  unfold nucleusMass
  exact categoricalMass_nonneg (le_of_lt m_e_cat_pos) _

/-- The MeV mass prediction is non-negative. -/
theorem nucleusMassMeV_nonneg (n : LightNucleus) [_w : R5FullWitness n] :
    0 ≤ nucleusMassMeV n := by
  unfold nucleusMassMeV
  exact categoricalMassMeV_nonneg (le_of_lt m_e_cat_pos) _

end  -- noncomputable section
end QOU.BraidKnot.PerNucleusMassDerivation
