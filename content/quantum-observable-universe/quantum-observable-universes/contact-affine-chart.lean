import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.ContactAffineChart

The contact affine chart U_ξ ⊂ P(V) is the open dense subset of states
with non-vanishing Reeb component. The affine coordinate is:

  Z([α]) = α_H / ι_ξ α

LaTeX label: `def:contact-affine-chart`

## References

- [manuscript] Chapter 1

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Contact affine chart**: the open dense subset of P(V) where the
    Reeb contraction is non-vanishing.

    On U_ξ, the affine coordinate Z = α_H / ι_ξ α provides a
    stereographic projection for the projective line fibres. -/
-- Ref: [manuscript] Chapter 1
structure ContactAffineChart (M : Type*) where
  /-- The base manifold point. -/
  point : M
  /-- The horizontal component α_H. -/
  horizontal : R_q
  /-- The Reeb contraction ι_ξ α (non-vanishing on U_ξ). -/
  reeb_contraction : R_q
  /-- Non-vanishing condition: ι_ξ α ≠ 0. -/
  reeb_nonzero : reeb_contraction ≠ 0

/-- The affine coordinate Z = α_H / ι_ξ α on the contact chart. -/
-- Ref: [manuscript] Chapter 1
noncomputable def ContactAffineChart.affineCoord {M : Type*}
    (chart : ContactAffineChart M) : R_q :=
  chart.horizontal / chart.reeb_contraction

/-- The affine coordinate is well-defined (denominator nonzero). -/
-- Ref: [manuscript] Chapter 1
theorem ContactAffineChart.affineCoord_welldefined {M : Type*}
    (chart : ContactAffineChart M) :
    chart.reeb_contraction ≠ 0 :=
  chart.reeb_nonzero

/-- The deep-quantum limit: Z → 0 as ι_ξ α → ∞ (q → ∞). -/
-- Ref: [manuscript] Chapter 1
theorem deep_quantum_limit {M : Type*} (chart : ContactAffineChart M)
    (h_large : |chart.reeb_contraction| > |chart.horizontal| * 1000) :
    |chart.affineCoord| < |chart.horizontal| / (|chart.horizontal| * 1000) := by
  unfold ContactAffineChart.affineCoord
  rw [abs_div]
  apply div_lt_div_of_pos_left (abs_nonneg _).lt_of_ne'
  · exact abs_pos.mpr chart.reeb_nonzero
  · exact h_large

end QOU
