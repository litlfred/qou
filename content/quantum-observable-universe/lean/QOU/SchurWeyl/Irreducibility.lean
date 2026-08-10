import QOU.SchurWeyl.HoefsmitRep
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

/-!
# QOU.SchurWeyl — irreducibility of the seminormal representation (SW-5)

The shape-`(2,1)` seminormal representation `seminormalRep21 : H_3(q) →ₐ[ℝ] M_2(ℝ)`
(`HoefsmitRep.lean`) is **irreducible** for every `q ≠ 0`.  For a `2`-dimensional
representation, irreducibility is exactly the absence of a `1`-dimensional
invariant subspace, i.e. the absence of a **common eigenvector** of the two
generator images `S0`, `S1`.  We prove that directly:

* an `S0`-eigenvector is forced to be axis-aligned, because `S0 = diag(q, -q⁻¹)`
  has **distinct** eigenvalues (`q ≠ -q⁻¹` over `ℝ`, since `q + q⁻¹ ≠ 0`); but
* `S1` fixes neither axis — its off-diagonal entries `c₀₁ = 1` and
  `c₁₀ = (q⁴+q²+1)/(q²+1)² > 0` are nonzero — so no common eigenvector exists.

This is the concrete `d_λ = 2` case of SW-5 (bean `qou-jfr8`); the general-`λ`
irreducibility depends on the general seminormal construction (residual bean
`qou-im9l`) and is not proved here.

Base ring `ℝ` (archimedean: the seminormal matrices live over `ℝ`, §7c).

LaTeX label: `prop:seminormal21-irreducible`
-/

namespace QOU.SchurWeyl

open Matrix

section Irreducible21

variable (q : ℝ)

/-- `q + q⁻¹ ≠ 0` for real `q ≠ 0` (equivalently `q² ≠ -1`): the eigenvalues
`q` and `-q⁻¹` of `S0` are distinct. -/
private theorem q_add_inv_ne (hq : q ≠ 0) : q + q⁻¹ ≠ 0 := by
  intro h
  have h2 : q * q + 1 = 0 := by
    have hc := congrArg (· * q) h
    simp only [zero_mul, add_mul, inv_mul_cancel₀ hq] at hc
    linarith [hc]
  nlinarith [mul_self_nonneg q, h2]

/-- The `(1,0)` entry of `S1` is strictly positive, so `S1` does not fix the
first axis. -/
private theorem S1_c10_pos : (0 : ℝ) < (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 := by
  positivity

/-- **The seminormal `(2,1)` representation is irreducible** (`q ≠ 0`):
`S0` and `S1` have no common eigenvector, hence no common `1`-dimensional
invariant subspace, hence the `2`-dimensional representation is irreducible. -/
theorem seminormal21_no_common_eigenvector (hq : q ≠ 0) :
    ¬ ∃ v : Fin 2 → ℝ, v ≠ 0 ∧
      (∃ a : ℝ, (S0 q).mulVec v = a • v) ∧ (∃ b : ℝ, (S1 q).mulVec v = b • v) := by
  rintro ⟨v, hv, ⟨a, ha⟩, ⟨b, hb⟩⟩
  have ha0 := congrFun ha 0
  have ha1 := congrFun ha 1
  have hb0 := congrFun hb 0
  have hb1 := congrFun hb 1
  simp only [S0, S1, Matrix.mulVec, dotProduct, Fin.sum_univ_two,
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.of_apply,
    Pi.smul_apply, smul_eq_mul, zero_mul, zero_add, add_zero,
    one_mul] at ha0 ha1 hb0 hb1
  -- ha0 : q * v 0 = a * v 0
  -- ha1 : -q⁻¹ * v 1 = a * v 1
  -- hb0 : -1 / (q ^ 3 + q) * v 0 + v 1 = b * v 0
  -- hb1 : (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 * v 0 + q ^ 3 / (q ^ 2 + 1) * v 1 = b * v 1
  rw [Function.ne_iff] at hv
  obtain ⟨i, hi⟩ := hv
  fin_cases i
  · -- v 0 ≠ 0 : then a = q, forcing v 1 = 0, contradicting hb1.
    have hv0 : v 0 ≠ 0 := hi
    have haq : a = q := (mul_right_cancel₀ hv0 ha0).symm
    have hv1 : v 1 = 0 := by
      rw [haq] at ha1
      have h2 : (q + q⁻¹) * v 1 = 0 := by linear_combination -ha1
      rcases mul_eq_zero.mp h2 with h | h
      · exact absurd h (q_add_inv_ne q hq)
      · exact h
    rw [hv1, mul_zero, add_zero, mul_zero] at hb1
    -- hb1 : (q ^ 4 + q ^ 2 + 1) / (q ^ 2 + 1) ^ 2 * v 0 = 0
    rcases mul_eq_zero.mp hb1 with h | h
    · exact absurd h (ne_of_gt (S1_c10_pos q))
    · exact absurd h hv0
  · -- v 1 ≠ 0 : then a = -q⁻¹, forcing v 0 = 0, contradicting hb0.
    have hv1 : v 1 ≠ 0 := hi
    have haq : a = -q⁻¹ := (mul_right_cancel₀ hv1 ha1).symm
    have hv0 : v 0 = 0 := by
      rw [haq] at ha0
      have h2 : (q + q⁻¹) * v 0 = 0 := by linear_combination ha0
      rcases mul_eq_zero.mp h2 with h | h
      · exact absurd h (q_add_inv_ne q hq)
      · exact h
    rw [hv0, mul_zero, zero_add, mul_zero] at hb0
    -- hb0 : v 1 = 0
    exact absurd hb0 hv1

end Irreducible21

end QOU.SchurWeyl
