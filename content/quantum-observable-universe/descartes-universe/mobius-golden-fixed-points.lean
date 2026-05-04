/-!
# QOU.Descartes.mobius_golden_fixed_points — Möbius fixed-point quartet

The baryon integration-limit transformation f(q) = (4 − q)/(4q + 3)
has fixed points at q = 1/φ and q = −φ, where φ = (1 + √5)/2.
Setting f(q) = q reduces to q² + q − 1 = 0, the minimal polynomial
of 1/φ over ℚ.

The bar-dual map g(q) = (q + 4)/(4q − 3) — obtained by the involution
q ↦ −q on both source and target — has fixed points {φ, −1/φ},
roots of q² − q − 1 = 0.  Together the two maps fix the golden
quartet {1/φ, −φ, φ, −1/φ}.

LaTeX label: `prop:mobius-golden-fixed-points`

## References

- [manuscript] §5/baryon-integration-limit
- [manuscript] §6/golden-skew-dual-node
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace QOU.Descartes

/-- The baryon integration-limit Möbius transformation. -/
noncomputable def mobiusLimit (q : ℝ) : ℝ := (4 - q) / (4 * q + 3)

/-- The fixed-point equation: f(q) = q iff q² + q − 1 = 0 (when 4q + 3 ≠ 0). -/
-- Ref: [manuscript] §5/baryon-integration-limit
theorem mobius_fixed_point_eq (q : ℝ) (h : 4 * q + 3 ≠ 0) :
    mobiusLimit q = q ↔ q ^ 2 + q - 1 = 0 := by
  unfold mobiusLimit
  constructor
  · intro heq
    have := div_eq_iff h |>.mp heq
    nlinarith
  · intro heq
    rw [div_eq_iff h]
    nlinarith

/-- Determinant of the Möbius matrix is −19. -/
-- Ref: [manuscript] §5/baryon-integration-limit
theorem mobius_det : (-1 : ℤ) * 3 - 4 * 4 = -19 := by norm_num

/-- Trace of the Möbius matrix is 2. -/
-- Ref: [manuscript] §5/baryon-integration-limit
theorem mobius_trace : (-1 : ℤ) + 3 = 2 := by norm_num

/-- The golden ratio reciprocal 1/φ = (√5 − 1)/2 satisfies q² + q − 1 = 0.

    This is the positive fixed point of the Möbius transformation. -/
-- Ref: [manuscript] §5/baryon-integration-limit
theorem golden_reciprocal_satisfies :
    let q := (Real.sqrt 5 - 1) / 2
    q ^ 2 + q - 1 = 0 := by
  simp only
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  field_simp
  nlinarith

/-- The negative golden ratio −φ = (−1 − √5)/2 satisfies q² + q − 1 = 0.

    This is the negative fixed point of the Möbius transformation. -/
-- Ref: [manuscript] §5/baryon-integration-limit
theorem neg_golden_satisfies :
    let q := (-1 - Real.sqrt 5) / 2
    q ^ 2 + q - 1 = 0 := by
  simp only
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  field_simp
  nlinarith

/-- The bar-dual Möbius transformation g(q) = (q + 4)/(4q − 3),
    obtained from f by the involution q ↦ −q on both source and target. -/
noncomputable def mobiusLimitDual (q : ℝ) : ℝ := (q + 4) / (4 * q - 3)

/-- The bar-dual fixed-point equation: g(q) = q iff q² − q − 1 = 0
    (when 4q − 3 ≠ 0). -/
-- Ref: [manuscript] §6/golden-skew-dual-node
theorem mobius_dual_fixed_point_eq (q : ℝ) (h : 4 * q - 3 ≠ 0) :
    mobiusLimitDual q = q ↔ q ^ 2 - q - 1 = 0 := by
  unfold mobiusLimitDual
  constructor
  · intro heq
    have := div_eq_iff h |>.mp heq
    nlinarith
  · intro heq
    rw [div_eq_iff h]
    nlinarith

/-- The bar-dual map g equals −f(−q): g(q) = −((4 − (−q))/(4·(−q) + 3)). -/
-- Ref: [manuscript] §6/golden-skew-dual-node
theorem mobiusLimitDual_eq_neg_f_neg (q : ℝ) (h : -4 * q + 3 ≠ 0) :
    mobiusLimitDual q = -(mobiusLimit (-q)) := by
  unfold mobiusLimitDual mobiusLimit
  have h' : 4 * q - 3 ≠ 0 := by
    intro hk
    apply h
    linarith
  field_simp
  ring

/-- The golden ratio φ = (1 + √5)/2 satisfies q² − q − 1 = 0. -/
-- Ref: [manuscript] §6/golden-skew-dual-node
theorem golden_satisfies_dual :
    let q := (1 + Real.sqrt 5) / 2
    q ^ 2 - q - 1 = 0 := by
  simp only
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  field_simp
  nlinarith

/-- The negative reciprocal −1/φ = (1 − √5)/2 satisfies q² − q − 1 = 0. -/
-- Ref: [manuscript] §6/golden-skew-dual-node
theorem neg_phiInv_satisfies_dual :
    let q := (1 - Real.sqrt 5) / 2
    q ^ 2 - q - 1 = 0 := by
  simp only
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)
  field_simp
  nlinarith

/-- **Möbius golden fixed points** (Proposition):

    The fixed points of f(q) = (4 − q)/(4q + 3) are exactly the roots
    of q² + q − 1 = 0, namely 1/φ and −φ where φ = (1 + √5)/2.

    The fixed points of the bar-dual g(q) = (q + 4)/(4q − 3) are
    exactly the roots of q² − q − 1 = 0, namely φ and −1/φ.

    Together, the two maps fix the golden quartet
    {1/φ, −φ, φ, −1/φ}. -/
-- Ref: [manuscript] §5/baryon-integration-limit
-- Ref: [manuscript] §6/golden-skew-dual-node
theorem mobius_golden_fixed_points :
    (∀ q : ℝ, 4 * q + 3 ≠ 0 →
        (mobiusLimit q = q ↔ q ^ 2 + q - 1 = 0)) ∧
    (∀ q : ℝ, 4 * q - 3 ≠ 0 →
        (mobiusLimitDual q = q ↔ q ^ 2 - q - 1 = 0)) :=
  ⟨fun q h => mobius_fixed_point_eq q h,
   fun q h => mobius_dual_fixed_point_eq q h⟩

end QOU.Descartes
