/-
# Bar-reflection grid selection — archimedean instantiation at ℝ_{>0}

Wall-side (§7c) specialisation of
`QOU.AlgebraicSubstrate.BarReflectionGridSelection`: the multiplicative
group is the positive reals `{x : ℝ // 0 < x}`, the step is the
balanced half-step `q̃ = √q > 0`, and the generic classification's two
hypotheses are DISCHARGED here rather than assumed —

* `ℝ_{>0}` is 2-torsion-free (`posReal_two_torsion_free`): `x² = 1`
  with `x > 0` forces `x = 1`;
* the half-step exists (`sqrtPos`): `w = √q̃` satisfies `w² = q̃`.

The main theorem `grid_barInvariant_iff_unit_or_half` is therefore
UNCONDITIONAL over `ℝ_{>0}`: a theta-grid translate class
`u · q̃^ℤ ⊂ ℝ_{>0}` is invariant under the fibre bar reflection
`s ↦ q̃⁻¹/s` (`barReflect_eq_div`) iff it is the unit class `1 · q̃^ℤ`
or the half-step class `√q̃ · q̃^ℤ` — the exact two-point narrowing of
the extension-circle continuum of the computational-time conjecture.
Selecting BETWEEN the two (and proving the distinguished extension is
atomic + bar-invariant at all) remains the conjecture's open content.

-- Ref: [leitner2026] predicted-spectra, conj:schwinger-measure-computational-time
--      (State after the representability and kernel-selection campaigns, 2026-08-01);
--      docs/audits/2026-08-01-ksel1-singularity-selection.md (half-step discriminant);
--      docs/audits/2026-08-01-ksel2-gns-favard-canonicity.md (extension circle).
-/

import Mathlib.Algebra.Order.Positive.Field
import Mathlib.Analysis.SpecialFunctions.Sqrt
import QOU.AlgebraicSubstrate.BarReflectionGridSelection

namespace QOU.Archimedean.BarReflectionGridSelectionReal

open QOU.AlgebraicSubstrate.BarReflectionGridSelection

/-- The multiplicative group of positive reals. -/
abbrev PosReal : Type := {x : ℝ // 0 < x}

/-- `ℝ_{>0}` is 2-torsion-free: a positive real square root of `1`
is `1`. Discharges the `htf` hypothesis of the generic
classification. -/
theorem posReal_two_torsion_free : ∀ x : PosReal, x ^ 2 = 1 → x = 1 := by
  rintro ⟨x, hx⟩ h
  have hval : x ^ 2 = 1 := congrArg Subtype.val h
  have : x = 1 := by nlinarith [sq_nonneg (x - 1), sq_nonneg (x + 1)]
  exact Subtype.ext this

/-- The half-step: for positive `v`, the positive square root, with
`(sqrtPos v)² = v`. Discharges the `hw` hypothesis of the generic
classification at `v = q̃`, giving the class of `q̃^{1/2}`. -/
noncomputable def sqrtPos (v : PosReal) : PosReal :=
  ⟨Real.sqrt v.val, Real.sqrt_pos.mpr v.property⟩

theorem sqrtPos_sq (v : PosReal) : sqrtPos v ^ 2 = v := by
  apply Subtype.ext
  have h : (sqrtPos v ^ 2).val = (sqrtPos v).val ^ 2 := rfl
  rw [h]
  exact Real.sq_sqrt v.property.le

/-- The bar reflection on `ℝ_{>0}` is division: `barReflect q̃ s = q̃⁻¹/s`
at the level of real values. -/
theorem barReflect_eq_div (v s : PosReal) :
    (barReflect v s).val = v.val⁻¹ / s.val := by
  rfl

/-- **The archimedean two-point narrowing (unconditional).** A
theta-grid class `u · q̃^ℤ` in `ℝ_{>0}` is bar-invariant iff it is the
unit class or the half-step class `√q̃ · q̃^ℤ`. -/
theorem grid_barInvariant_iff_unit_or_half (u v : PosReal) :
    grid u⁻¹ v = grid u v ↔
      (grid u v = grid 1 v ∨ grid u v = grid (sqrtPos v) v) :=
  grid_barInvariant_classification u v (sqrtPos v) (sqrtPos_sq v)
    posReal_two_torsion_free

end QOU.Archimedean.BarReflectionGridSelectionReal
