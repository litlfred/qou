import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Int.Basic


/-!
# QOU.ContactAffineChart

The contact affine chart U_ξ ⊂ P(V) is the open dense subset of states
with non-vanishing Reeb component. The affine coordinate is:

  Z([α]) = α_H / ι_ξ α

LaTeX label: `def:contact-affine-chart`

## References

- [leitner2026] Chapter 1

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ) names the
canonical indeterminate `q`. The affine coordinate `Z = α_H / ι_ξ α` is a
quotient, so its target is a *field* `R`; specialise via the fibre functor
`ι : R_q → ℝ, q ↦ q₀` (the substrate→archimedean wall) before taking the
deep-quantum archimedean limit.
-/

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable abbrev R_q := LaurentPolynomial ℤ

/-- The canonical indeterminate `q ∈ R_q`. -/
noncomputable def q_param : R_q := LaurentPolynomial.T 1

/-- Its inverse `q⁻¹ ∈ R_q`. -/
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- **Contact affine chart**: the open dense subset of P(V) where the
    Reeb contraction is non-vanishing.

    On U_ξ, the affine coordinate Z = α_H / ι_ξ α provides a
    stereographic projection for the projective line fibres. The
    coordinate components take values in a field `R` (the archimedean
    image of `R_q` under the fibre functor), so the quotient is defined. -/
-- Ref: [leitner2026] Chapter 1
structure ContactAffineChart (M : Type*) (R : Type*) [Field R] where
  /-- The base manifold point. -/
  point : M
  /-- The horizontal component α_H. -/
  horizontal : R
  /-- The Reeb contraction ι_ξ α (non-vanishing on U_ξ). -/
  reeb_contraction : R
  /-- Non-vanishing condition: ι_ξ α ≠ 0. -/
  reeb_nonzero : reeb_contraction ≠ 0

/-- The affine coordinate Z = α_H / ι_ξ α on the contact chart. -/
-- Ref: [leitner2026] Chapter 1
noncomputable def ContactAffineChart.affineCoord {M : Type*} {R : Type*} [Field R]
    (chart : ContactAffineChart M R) : R :=
  chart.horizontal / chart.reeb_contraction

/-- The affine coordinate is well-defined (denominator nonzero). -/
-- Ref: [leitner2026] Chapter 1
theorem ContactAffineChart.affineCoord_welldefined {M : Type*} {R : Type*} [Field R]
    (chart : ContactAffineChart M R) :
    chart.reeb_contraction ≠ 0 :=
  chart.reeb_nonzero

/-- The deep-quantum limit: `|Z|` is small when the Reeb contraction is
    large relative to the horizontal component (the archimedean image
    `R = ℝ` of the substrate, after the fibre functor). -/
-- Ref: [leitner2026] Chapter 1
theorem deep_quantum_limit {M : Type*} {R : Type*}
    [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    (chart : ContactAffineChart M R)
    (h_pos : 0 < |chart.horizontal|)
    (h_large : |chart.horizontal| * 1000 < |chart.reeb_contraction|) :
    |chart.affineCoord| < |chart.horizontal| / (|chart.horizontal| * 1000) := by
  unfold ContactAffineChart.affineCoord
  rw [abs_div]
  have hd : 0 < |chart.reeb_contraction| := lt_trans (by positivity) h_large
  apply div_lt_div_of_pos_left h_pos (by positivity) h_large

end QOU
