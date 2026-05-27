import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic


/-!
# QOU.Braiding.CoulombCharge — Coulomb charge of a knot composite

The Coulomb charge Q(H) = ½(n₊(β) − n₋(β)) measures the crossing
asymmetry of a knot composite.  It governs the magnitude and sign
of the electromagnetic (Coulomb) correction to the crossing energy.

LaTeX label: `def:coulomb-charge`

## References

- [manuscript] Ch. 4, §10

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

namespace QOU.Braiding

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Coulomb Charge -/

/-- **Coulomb charge** of a knot composite with braid word β.

    Q(H) = ½(n₊(β) − n₋(β))

    where n₊, n₋ are the positive and negative crossing counts.

    - Q(H) > 0: net positive crossings, repulsive Coulomb contribution.
    - Q(H) = 0: electromagnetically neutral.
    - Q(H) < 0: net negative crossings, attractive Coulomb contribution. -/
-- Ref: [manuscript] Ch. 4, §10
structure CoulombCharge where
  /-- Number of positive crossings n₊. -/
  numPositive : ℕ
  /-- Number of negative crossings n₋. -/
  numNegative : ℕ

/-- The Coulomb charge value: Q = (n₊ − n₋) / 2. -/
noncomputable def CoulombCharge.value (C : CoulombCharge) : R_q :=
  ((C.numPositive : R_q) - C.numNegative) / 2

/-- A composite is electromagnetically neutral when Q(H) = 0,
    i.e., n₊ = n₋. -/
def CoulombCharge.isNeutral (C : CoulombCharge) : Prop :=
  C.numPositive = C.numNegative

/-- Neutral composites have zero Coulomb charge. -/
-- Ref: [manuscript] Ch. 4, §10
theorem CoulombCharge.neutral_iff_zero (C : CoulombCharge) :
    C.isNeutral ↔ C.value = 0 := by
  constructor
  · intro h
    simp [value, isNeutral] at h ⊢
    rw [h]; ring
  · intro h
    simp only [value, isNeutral] at h ⊢
    have h2 : (2 : R_q) ≠ 0 := by norm_num
    have h' : ((C.numPositive : R_q) - C.numNegative) / 2 = 0 := h
    rw [div_eq_zero_iff] at h'
    cases h' with
    | inl hsub =>
      have : (C.numPositive : R_q) = (C.numNegative : R_q) := sub_eq_zero.mp hsub
      exact_mod_cast this
    | inr h2z => exact absurd h2z h2

/-- The crossing energy Coulomb correction term is Q(H) · (q − q⁻¹).
    This is antisymmetric under q ↔ q⁻¹ and vanishes at q = 1. -/
-- Ref: [manuscript] Ch. 4, §10
noncomputable def CoulombCharge.coulombCorrection (C : CoulombCharge) (q : R_q) : R_q :=
  C.value * (q - q⁻¹)

/-- The Coulomb correction vanishes at q = 1 (undeformed limit). -/
-- Ref: [manuscript] Ch. 4, §10
theorem CoulombCharge.coulombCorrection_at_one (C : CoulombCharge) :
    C.coulombCorrection 1 = 0 := by
  simp [coulombCorrection, inv_one, sub_self, mul_zero]

/-- The Coulomb correction is antisymmetric: replacing q with q⁻¹
    flips the sign. -/
-- Ref: [manuscript] Ch. 4, §10
theorem CoulombCharge.coulombCorrection_antisymmetric
    (C : CoulombCharge) (q : R_q) (hq : q ≠ 0) :
    C.coulombCorrection q⁻¹ = -C.coulombCorrection q := by
  simp [coulombCorrection, inv_inv]
  ring

end QOU.Braiding
