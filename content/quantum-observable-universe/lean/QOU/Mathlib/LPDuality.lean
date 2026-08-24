import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset

/-!
# LP Duality — finite-dimensional weak and strong duality

Weak and strong duality for finite-dimensional linear programs, stated over
`Fin k → ℝ` without any Matrix dependency.
-/

open Finset BigOperators

namespace QOU.Mathlib.LPDuality

variable {n m : ℕ}

/-- **Weak LP duality.** `∑ b_i y_i ≤ ∑ c_j x_j` for primal-feasible `x`
    and dual-feasible `y`. -/
theorem weak_duality
    (A : Fin m → Fin n → ℝ) (b : Fin m → ℝ) (c : Fin n → ℝ)
    (x : Fin n → ℝ) (y : Fin m → ℝ)
    (hx_pos : ∀ j, 0 ≤ x j)
    (hx_feas : ∀ i, b i ≤ ∑ j, A i j * x j)
    (hy_pos : ∀ i, 0 ≤ y i)
    (hy_feas : ∀ j, (∑ i, y i * A i j) ≤ c j) :
    (∑ i, b i * y i) ≤ (∑ j, c j * x j) := by
  -- Step 1: ∑ b_i y_i = ∑ y_i b_i
  have comm1 : ∑ i : Fin m, b i * y i = ∑ i : Fin m, y i * b i := by
    apply Finset.sum_congr rfl; intro i _; ring
  rw [comm1]
  -- Step 2: ∑ y_i b_i ≤ ∑ y_i (∑_j A_{ij} x_j)
  have step1 : (∑ i : Fin m, y i * b i) ≤ (∑ i : Fin m, y i * (∑ j : Fin n, A i j * x j)) :=
    Finset.sum_le_sum fun i _ => mul_le_mul_of_nonneg_left (hx_feas i) (hy_pos i)
  -- Step 3: middle term = ∑_j (∑_i y_i A_{ij}) x_j
  have step2 : (∑ i : Fin m, y i * (∑ j : Fin n, A i j * x j))
             = (∑ j : Fin n, (∑ i : Fin m, y i * A i j) * x j) := by
    simp_rw [Finset.mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl; intro j _
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl; intro i _; ring
  -- Step 4: ∑_j (∑_i y_i A_{ij}) x_j ≤ ∑_j c_j x_j
  have step3 : (∑ j : Fin n, (∑ i : Fin m, y i * A i j) * x j) ≤ (∑ j : Fin n, c j * x j) :=
    Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_right (hy_feas j) (hx_pos j)
  linarith

/-- **Strong LP duality** (certificate form). Given complementary slackness,
    `∑ c_j x_j = ∑ b_i y_i`. -/
theorem strong_duality
    (A : Fin m → Fin n → ℝ) (b : Fin m → ℝ) (c : Fin n → ℝ)
    (x : Fin n → ℝ) (y : Fin m → ℝ)
    (hx_slack : ∀ j, x j = 0 ∨ (∑ i, y i * A i j) = c j)
    (hy_slack : ∀ i, y i = 0 ∨ (∑ j, A i j * x j) = b i) :
    (∑ j, c j * x j) = (∑ i, b i * y i) := by
  -- Step 1: c_j x_j = (Aᵀy)_j x_j by primal CS
  have s1 : (∑ j : Fin n, c j * x j) = (∑ j : Fin n, (∑ i : Fin m, y i * A i j) * x j) := by
    apply Finset.sum_congr rfl; intro j _
    rcases hx_slack j with hj | hj
    · simp [hj]
    · rw [hj]
  -- Step 2: b_i y_i = y_i (Ax)_i by dual CS
  have s2 : (∑ i : Fin m, b i * y i) = (∑ i : Fin m, y i * (∑ j : Fin n, A i j * x j)) := by
    apply Finset.sum_congr rfl; intro i _
    rcases hy_slack i with hi | hi
    · simp [hi]
    · rw [hi]; ring
  -- Step 3: middle = middle (sum swap)
  have mid : (∑ j : Fin n, (∑ i : Fin m, y i * A i j) * x j)
           = (∑ i : Fin m, y i * (∑ j : Fin n, A i j * x j)) := by
    simp_rw [Finset.mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl; intro j _
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl; intro i _; ring
  linarith

end QOU.Mathlib.LPDuality
