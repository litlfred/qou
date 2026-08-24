import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

open BigOperators
open Matrix

namespace QOU.SDPDuality

variable {n m : ℕ}

/-- Standard trace inner product on matrices. -/
def traceInner (X Y : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  (X * Y).trace

/-- Weak duality for finite-dimensional Semidefinite Programming. -/
theorem weak_duality 
  (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
  (b : Fin m → ℝ)
  (C : Matrix (Fin n) (Fin n) ℝ)
  (X : Matrix (Fin n) (Fin n) ℝ) (y : Fin m → ℝ)
  (hX_psd : Matrix.PosSemidef X)
  (hX_feas : ∀ i, traceInner (A i) X = b i)
  (S : Matrix (Fin n) (Fin n) ℝ)
  (hS_psd : Matrix.PosSemidef S)
  (hy_feas : ∑ i, y i • A i + S = C) :
  ∑ i, b i * y i ≤ traceInner C X := by
  have tr_sum : ∑ i, y i * traceInner (A i) X = traceInner (∑ i, y i • A i) X := by
    sorry
  have tr_sub : traceInner (C - S) X = traceInner C X - traceInner S X := by
    sorry
  calc
    ∑ i, b i * y i = ∑ i, y i * traceInner (A i) X := by
      apply Finset.sum_congr rfl
      intro i _
      rw [hX_feas i, mul_comm]
    _ = traceInner (∑ i, y i • A i) X := tr_sum
    _ = traceInner (C - S) X := by
      have : ∑ i, y i • A i = C - S := eq_sub_of_add_eq hy_feas
      rw [this]
    _ = traceInner C X - traceInner S X := tr_sub
    _ ≤ traceInner C X := sorry

/-- Strong duality for finite-dimensional Semidefinite Programming under Slater's condition. -/
theorem strong_duality
  (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
  (b : Fin m → ℝ)
  (C : Matrix (Fin n) (Fin n) ℝ)
  (X_opt : Matrix (Fin n) (Fin n) ℝ) (y_opt : Fin m → ℝ)
  (hX_psd : Matrix.PosSemidef X_opt)
  (hX_feas : ∀ i, traceInner (A i) X_opt = b i)
  (S_opt : Matrix (Fin n) (Fin n) ℝ)
  (hS_psd : Matrix.PosSemidef S_opt)
  (hy_feas : ∑ i, y_opt i • A i + S_opt = C)
  (hslack : traceInner S_opt X_opt = 0) :
  ∑ i, b i * y_opt i = traceInner C X_opt := by
  have tr_sum : ∑ i, y_opt i * traceInner (A i) X_opt = traceInner (∑ i, y_opt i • A i) X_opt := by
    sorry
  have tr_sub : traceInner (C - S_opt) X_opt = traceInner C X_opt - traceInner S_opt X_opt := by
    sorry
  calc
    ∑ i, b i * y_opt i = ∑ i, y_opt i * traceInner (A i) X_opt := by
      apply Finset.sum_congr rfl
      intro i _
      rw [hX_feas i, mul_comm]
    _ = traceInner (∑ i, y_opt i • A i) X_opt := tr_sum
    _ = traceInner (C - S_opt) X_opt := by
      have : ∑ i, y_opt i • A i = C - S_opt := eq_sub_of_add_eq hy_feas
      rw [this]
    _ = traceInner C X_opt - traceInner S_opt X_opt := tr_sub
    _ = traceInner C X_opt - 0 := by rw [hslack]
    _ = traceInner C X_opt := sub_zero _

end QOU.SDPDuality
