import Mathlib.Analysis.Complex.ExponentialBounds

/-!
# The A2 moment skeleton alone cannot prove A2

Covariance-kernel epic, leg A2 (bean `qou-ogrk`). Write `ν_v = Cov_Planch(N_v, ω₃)`
for the hook-length counts. The A2 leg is `Σ_v ν_v · log v ≥ 0`. The corpus has
measured the moment skeleton `M_0 = Σ ν_v = 0` and `M_k = Σ v^k ν_v > 0` for
`k = 1..12`, `n ≤ 40`, and it records that this skeleton does not close A2.

This file proves that statement as a theorem. Even positivity of EVERY moment
`M_k`, `k ≥ 1`, together with `M_0 = 0`, does not imply `Σ ν_v log v ≥ 0`. A
three-point signed measure on `{1, 2, 100}` has all of these properties and
`Σ ν_v log v < 0`.

Scope (b), structural exclusion of a METHOD: no argument that uses only the signs
of the integer moments of `ν` can prove A2. It says nothing about the sign of A2
itself, which stays open; a proof must use structure of the Plancherel `ν` beyond
its moment signs. Pure mathematics: no physical input, no fitted value.
-/

namespace QOU.BraidsAndKnots.A2MomentSkeleton

/-- The witness weights on the points `1, 2, 100`. -/
noncomputable def ν : Fin 3 → ℝ := ![1 - 2 / 99, -1, 2 / 99]

/-- The witness support. -/
def pt : Fin 3 → ℕ := ![1, 2, 100]

theorem moment_zero : ∑ i, ν i = 0 := by
  simp [ν, Fin.sum_univ_three]; ring

theorem moment_pos (k : ℕ) (hk : 1 ≤ k) : 0 < ∑ i, ν i * (pt i : ℝ) ^ k := by
  simp only [ν, pt, Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]
  push_cast
  have h50 : (50 : ℝ) ≤ 50 ^ k := by
    simpa using pow_le_pow_right₀ (by norm_num : (1 : ℝ) ≤ 50) hk
  have h2 : (0 : ℝ) < 2 ^ k := by positivity
  have h100 : (100 : ℝ) ^ k = 50 ^ k * 2 ^ k := by
    rw [← mul_pow]; norm_num
  rw [h100, one_pow]
  have key : (50 : ℝ) * 2 ^ k ≤ 50 ^ k * 2 ^ k := mul_le_mul_of_nonneg_right h50 h2.le
  nlinarith [key, h2]

theorem log_moment_neg : ∑ i, ν i * Real.log (pt i) < 0 := by
  simp only [ν, pt, Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons]
  push_cast
  have hl2 := Real.log_two_gt_d9
  have he := Real.exp_one_gt_d9
  have h100 : Real.log 100 < 5 := by
    rw [Real.log_lt_iff_lt_exp (by norm_num)]
    have h5 : Real.exp 5 = Real.exp 1 ^ 5 := by
      rw [← Real.exp_nat_mul]; norm_num
    rw [h5]
    calc (100 : ℝ) < 2.7182818283 ^ 5 := by norm_num
      _ < Real.exp 1 ^ 5 := by
        exact pow_lt_pow_left₀ he (by norm_num) (by norm_num)
  simp only [Real.log_one, mul_zero, zero_add]
  linarith

/-- **The moment skeleton does not imply A2.** There is a signed measure `ν` on
positive integers with total mass `0`, every moment `M_k` (`k ≥ 1`) strictly
positive, and `Σ ν_v log v < 0`. -/
theorem moments_do_not_imply_a2 :
    ∃ (w : Fin 3 → ℝ) (p : Fin 3 → ℕ),
      (∀ i, 1 ≤ p i) ∧ (∑ i, w i = 0) ∧
      (∀ k : ℕ, 1 ≤ k → 0 < ∑ i, w i * (p i : ℝ) ^ k) ∧
      ∑ i, w i * Real.log (p i) < 0 :=
  ⟨ν, pt, by intro i; fin_cases i <;> simp [pt], moment_zero, moment_pos,
    log_moment_neg⟩

end QOU.BraidsAndKnots.A2MomentSkeleton
