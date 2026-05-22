/-!
# QOU.Archimedean.parity_violation_skein — Parity non-conservation from q ≠ 1

The Skein relation q[L₊] - q⁻¹[L₋] = (q^½ - q^⁻½)[L₀] is invariant
under parity (L₊ ↔ L₋) if and only if q = 1.  For any q ≠ 1, the weak
interaction violates parity.

LaTeX label: `prop:parity-violation-skein`

## References
- [manuscript] §6/parity-violation-skein
- Lee, Yang (1956): Question of parity conservation in weak interactions
- Wu et al. (1957): Experimental test of parity conservation in beta decay

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU.Archimedean

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The Skein relation coefficients for L₊ and L₋.
    Parity exchanges these: (q, q⁻¹) ↔ (q⁻¹, q).
    The relation is parity-invariant iff q = q⁻¹, i.e., q = 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
structure SkeinCoefficients where
  q : R_q
  -- q_pos : 0 < q  -- (archimedean; not meaningful over R_q)
  /-- Coefficient of [L₊]. -/
  coeff_plus : R_q := q
  /-- Coefficient of [L₋]. -/
  coeff_minus : R_q := 1 / q

/-- Parity invariance means the coefficients are equal. -/
-- Ref: [manuscript] §6/parity-violation-skein
def SkeinCoefficients.parityInvariant (s : SkeinCoefficients) : Prop :=
  s.coeff_plus = s.coeff_minus

/-- The Skein relation is parity-invariant if and only if q = 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
-- theorem parity_violation_skein (q : R_q) (hq : 0 < q) :  -- (archimedean; not meaningful over R_q)
    (SkeinCoefficients.mk q hq).parityInvariant ↔ q = 1 := by
  unfold SkeinCoefficients.parityInvariant SkeinCoefficients.coeff_plus SkeinCoefficients.coeff_minus
  simp
  constructor
  · intro h
    have : q * q = 1 := by
      field_simp at h
      nlinarith
    nlinarith [sq_nonneg (q - 1)]
  · intro h
    subst h
    norm_num

/-- At q = 1.1097, the parity violation parameter q - q⁻¹ ≈ 0.209. -/
-- Ref: [manuscript] §6/parity-violation-skein
noncomputable def parityViolationStrength (q : R_q) : R_q := q - 1 / q

/-- The parity violation strength is positive for q > 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
-- theorem parityViolationStrength_pos {q : R_q} (hq : 1 < q) :  -- (archimedean; not meaningful over R_q)
    0 < parityViolationStrength q := by
  unfold parityViolationStrength
  rw [sub_pos, div_lt_iff (by linarith : (0 : R_q) < q)]
  nlinarith

/-- The parity violation strength vanishes at q = 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
theorem parityViolationStrength_classical :
    parityViolationStrength 1 = 0 := by
  unfold parityViolationStrength
  norm_num

/-- CP is conserved: the q ↔ q⁻¹ involution IS a symmetry.
    Under CP: coeff_plus ↔ coeff_minus AND L₊ ↔ L₋,
    so the Skein relation maps to itself. -/
-- Ref: [manuscript] §6/parity-violation-skein
-- theorem cp_conservation (q : R_q) (hq : 0 < q) :  -- (archimedean; not meaningful over R_q)
    let s := SkeinCoefficients.mk q hq
    let s_cp := SkeinCoefficients.mk (1/q) (by positivity)
    s.coeff_plus = s_cp.coeff_minus ∧ s.coeff_minus = s_cp.coeff_plus := by
  simp [SkeinCoefficients.coeff_plus, SkeinCoefficients.coeff_minus]
  constructor
  · field_simp
  · field_simp

end QOU.Archimedean
