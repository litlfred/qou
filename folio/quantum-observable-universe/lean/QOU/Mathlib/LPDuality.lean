import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

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


/-- **Duality-gap decomposition.** An unconditional identity: the primal-dual
    gap is exactly the sum of the primal complementary-slackness residuals
    `(c_j - (Aᵀy)_j) · x_j` and the dual ones `y_i · ((Ax)_i - b_i)`.

    No feasibility hypothesis is needed — this is algebra, and that is the
    point. A solver reports a `duality_gap` scalar; this identity lets a
    consumer *recompute* that gap from the emitted `x`, `y`, `A`, `b`, `c`
    alone, so the reported number becomes checkable rather than trusted.
    `weak_duality` above says the gap is non-negative under feasibility;
    this says *where it lives*. -/
theorem duality_gap_decomposition
    (A : Fin m → Fin n → ℝ) (b : Fin m → ℝ) (c : Fin n → ℝ)
    (x : Fin n → ℝ) (y : Fin m → ℝ) :
    (∑ j, c j * x j) - (∑ i, b i * y i)
      = (∑ j, (c j - ∑ i, y i * A i j) * x j)
        + (∑ i, y i * ((∑ j, A i j * x j) - b i)) := by
  have hswap : (∑ j : Fin n, (∑ i : Fin m, y i * A i j) * x j)
             = (∑ i : Fin m, y i * (∑ j : Fin n, A i j * x j)) := by
    simp_rw [Finset.mul_sum]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl; intro j _
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl; intro i _; ring
  have hp : (∑ j : Fin n, (c j - ∑ i : Fin m, y i * A i j) * x j)
          = (∑ j : Fin n, c j * x j)
            - (∑ j : Fin n, (∑ i : Fin m, y i * A i j) * x j) := by
    rw [← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl; intro j _; ring
  have hd : (∑ i : Fin m, y i * ((∑ j : Fin n, A i j * x j) - b i))
          = (∑ i : Fin m, y i * (∑ j : Fin n, A i j * x j))
            - (∑ i : Fin m, b i * y i) := by
    rw [← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl; intro i _; ring
  rw [hp, hd, hswap]
  ring

/-- **Certified gap bound.** If every primal slack residual and every dual
    slack residual is at most `ε ≥ 0` in the (signed) sense below, the gap is
    at most `(n + m) · ε`.

    This is the form a numerical consumer can discharge: it bounds the true
    gap by quantities it computes itself from the emitted certificate, with
    no appeal to the solver's own `duality_gap` field. -/
theorem duality_gap_le_of_residual_bounds
    (A : Fin m → Fin n → ℝ) (b : Fin m → ℝ) (c : Fin n → ℝ)
    (x : Fin n → ℝ) (y : Fin m → ℝ) (ε : ℝ)
    (hp : ∀ j, (c j - ∑ i, y i * A i j) * x j ≤ ε)
    (hd : ∀ i, y i * ((∑ j, A i j * x j) - b i) ≤ ε) :
    (∑ j, c j * x j) - (∑ i, b i * y i) ≤ (n : ℝ) * ε + (m : ℝ) * ε := by
  rw [duality_gap_decomposition A b c x y]
  have h1 : (∑ j : Fin n, (c j - ∑ i : Fin m, y i * A i j) * x j) ≤ (n : ℝ) * ε := by
    calc (∑ j : Fin n, (c j - ∑ i : Fin m, y i * A i j) * x j)
        ≤ ∑ _j : Fin n, ε := Finset.sum_le_sum fun j _ => hp j
      _ = (n : ℝ) * ε := by simp [Finset.sum_const, mul_comm]
  have h2 : (∑ i : Fin m, y i * ((∑ j : Fin n, A i j * x j) - b i)) ≤ (m : ℝ) * ε := by
    calc (∑ i : Fin m, y i * ((∑ j : Fin n, A i j * x j) - b i))
        ≤ ∑ _i : Fin m, ε := Finset.sum_le_sum fun i _ => hd i
      _ = (m : ℝ) * ε := by simp [Finset.sum_const, mul_comm]
  linarith


/-- **Zero slack residuals force zero duality gap (`qou-fr4d`).**
When every primal complementary-slackness residual `(c_j - (Aᵀy)_j) x_j` and every dual
residual `y_i ((Ax)_i - b_i)` vanishes, the primal-dual gap `∑ c_j x_j - ∑ b_i y_i` is zero. -/
theorem duality_gap_eq_zero_of_zero_residuals
    (A : Fin m → Fin n → ℝ) (b : Fin m → ℝ) (c : Fin n → ℝ)
    (x : Fin n → ℝ) (y : Fin m → ℝ)
    (hp : ∀ j, (c j - ∑ i, y i * A i j) * x j = 0)
    (hd : ∀ i, y i * ((∑ j, A i j * x j) - b i) = 0) :
    (∑ j, c j * x j) - (∑ i, b i * y i) = 0 := by
  rw [duality_gap_decomposition A b c x y]
  simp [hp, hd]

end QOU.Mathlib.LPDuality
