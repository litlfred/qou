/-
Copyright (c) 2026 Frederick Carl Leitner. All rights reserved.
-/
import QOU.MathlibExt.KLCoordinateLaurent

/-!
# QOU.BraidsAndKnots.ProtonNormaliserKLCoordinate

Carrier for `conj:proton-normaliser-kl-coordinate`.

The class `KLCoordinateConjecture u v` states the two conditions on the
coordinate `b = u·σ + v` over `ℤ[q, q⁻¹]` (`q = T 1`): `u` is a unit, and `b`
is bar-invariant. From them `unit_eq_pm_one` derives `u = ±1`, which is what
makes the derivative of the sign-block trace at `z_D` equal to `±q⁻³`
(`QOU.MassTheory.ProtonQ3Schur.kl_coordinate_derivative`).

What Lean does not carry: the identification that the observable `F_Bor` is
read in such a coordinate. That was the open part of the conjecture, and it is
retired (2026-11-21): the same conditions applied to the sign element give
`k = 0`, not `k = −3` (`QOU.MassTheory.ProtonQ3Slopes.sign_line_bar_fixed_iff`). The class
is satisfiable (`kl_element_meets_conditions`), so the conditions are
consistent; satisfiability does not prove the identification.
-/

namespace QOU.BraidsAndKnots.ProtonNormaliserKLCoordinate

open LaurentPolynomial QOU.MathlibExt.KLCoordinateLaurent

/-- The two conditions of `conj:proton-normaliser-kl-coordinate` on the
coordinate `b = u·σ + v`. -/
class KLCoordinateConjecture (u v : ℤ[T;T⁻¹]) : Prop where
  /-- `b` and `1` span `H₂` over `ℤ[q, q⁻¹]`. -/
  spans : IsUnit u
  /-- `b` is fixed by `σ ↦ σ⁻¹`, `q ↦ q⁻¹`. -/
  bar_invariant : IsBarInvariantCoord u v

/-- Under the conditions, the `σ`-coefficient is `±1`, so the coordinate is a
Kazhdan–Lusztig element `±(σ − q) + c`. -/
theorem unit_eq_pm_one (u v : ℤ[T;T⁻¹]) [h : KLCoordinateConjecture u v] :
    (u = 1 ∨ u = -1) ∧ ∃ c : ℤ[T;T⁻¹], invert c = c ∧ v = -u * T 1 + c :=
  (kl_coord_classification u v).mp ⟨h.spans, h.bar_invariant⟩

/-- The conditions are consistent: `C_s = σ − q` meets them. -/
theorem kl_element_meets_conditions : IsUnit (1 : ℤ[T;T⁻¹]) ∧ IsBarInvariantCoord 1 (-T 1) :=
  (kl_coord_classification 1 (-T 1)).mpr ⟨Or.inl rfl, 0, by simp, by ring⟩

end QOU.BraidsAndKnots.ProtonNormaliserKLCoordinate
