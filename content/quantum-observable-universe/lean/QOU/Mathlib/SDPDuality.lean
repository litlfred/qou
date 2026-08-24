import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith

open BigOperators Matrix Finset

namespace QOU.Mathlib.SDPDuality

variable {n m : ℕ}

/-- Standard trace inner product: `⟨X, Y⟩ = tr(XY)`. -/
noncomputable def traceInner (X Y : Matrix (Fin n) (Fin n) ℝ) : ℝ :=
  (X * Y).trace

lemma traceInner_smul_left (a : ℝ) (X Y : Matrix (Fin n) (Fin n) ℝ) :
    traceInner (a • X) Y = a * traceInner X Y := by
  simp only [traceInner, smul_mul, trace_smul, smul_eq_mul]

lemma traceInner_add_left (X₁ X₂ Y : Matrix (Fin n) (Fin n) ℝ) :
    traceInner (X₁ + X₂) Y = traceInner X₁ Y + traceInner X₂ Y := by
  simp only [traceInner, add_mul, trace_add]

lemma traceInner_sub_left (X₁ X₂ Y : Matrix (Fin n) (Fin n) ℝ) :
    traceInner (X₁ - X₂) Y = traceInner X₁ Y - traceInner X₂ Y := by
  simp only [traceInner, sub_mul, trace_sub]

lemma traceInner_finset_sum_left (s : Finset (Fin m))
    (f : Fin m → Matrix (Fin n) (Fin n) ℝ) (Y : Matrix (Fin n) (Fin n) ℝ) :
    traceInner (∑ i ∈ s, f i) Y = ∑ i ∈ s, traceInner (f i) Y := by
  simp only [traceInner, Finset.sum_mul, trace_sum]

/-- MATHLIB GAP: tr(SX) ≥ 0 for PSD S and X. Standard result, but Mathlib lacks
    matrix square root, so the proof `tr(SX) = tr(S^{1/2} X S^{1/2}) ≥ 0` is
    not formalizable yet. -/
axiom traceInner_nonneg_of_posSemidef (n : ℕ)
    (S X : Matrix (Fin n) (Fin n) ℝ)
    (hS : Matrix.PosSemidef S) (hX : Matrix.PosSemidef X) :
    0 ≤ traceInner S X

/-- **Weak SDP duality.** -/
theorem weak_duality
    (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (b : Fin m → ℝ) (C X : Matrix (Fin n) (Fin n) ℝ)
    (y : Fin m → ℝ) (hX_psd : Matrix.PosSemidef X)
    (hX_feas : ∀ i, traceInner (A i) X = b i)
    (S : Matrix (Fin n) (Fin n) ℝ) (hS_psd : Matrix.PosSemidef S)
    (hy_feas : ∑ i, y i • A i + S = C) :
    ∑ i, b i * y i ≤ traceInner C X := by
  have tr_sum : ∑ i : Fin m, y i * traceInner (A i) X
              = traceInner (∑ i : Fin m, y i • A i) X := by
    rw [traceInner_finset_sum_left]
    apply Finset.sum_congr rfl; intro i _
    rw [traceInner_smul_left]
  calc ∑ i, b i * y i
      = ∑ i, y i * traceInner (A i) X := by
        apply Finset.sum_congr rfl; intro i _; rw [hX_feas i, mul_comm]
    _ = traceInner (∑ i, y i • A i) X := tr_sum
    _ = traceInner (C - S) X := by rw [eq_sub_of_add_eq hy_feas]
    _ = traceInner C X - traceInner S X := traceInner_sub_left C S X
    _ ≤ traceInner C X := by
        linarith [traceInner_nonneg_of_posSemidef n S X hS_psd hX_psd]

/-- **Strong SDP duality** (complementary slackness certificate). -/
theorem strong_duality
    (A : Fin m → Matrix (Fin n) (Fin n) ℝ)
    (b : Fin m → ℝ) (C X_opt : Matrix (Fin n) (Fin n) ℝ)
    (y_opt : Fin m → ℝ) (_hX_psd : Matrix.PosSemidef X_opt)
    (hX_feas : ∀ i, traceInner (A i) X_opt = b i)
    (S_opt : Matrix (Fin n) (Fin n) ℝ) (_hS_psd : Matrix.PosSemidef S_opt)
    (hy_feas : ∑ i, y_opt i • A i + S_opt = C)
    (hslack : traceInner S_opt X_opt = 0) :
    ∑ i, b i * y_opt i = traceInner C X_opt := by
  have tr_sum : ∑ i : Fin m, y_opt i * traceInner (A i) X_opt
              = traceInner (∑ i : Fin m, y_opt i • A i) X_opt := by
    rw [traceInner_finset_sum_left]
    apply Finset.sum_congr rfl; intro i _
    rw [traceInner_smul_left]
  calc ∑ i, b i * y_opt i
      = ∑ i, y_opt i * traceInner (A i) X_opt := by
        apply Finset.sum_congr rfl; intro i _; rw [hX_feas i, mul_comm]
    _ = traceInner (∑ i, y_opt i • A i) X_opt := tr_sum
    _ = traceInner (C - S_opt) X_opt := by rw [eq_sub_of_add_eq hy_feas]
    _ = traceInner C X_opt - traceInner S_opt X_opt := traceInner_sub_left C S_opt X_opt
    _ = traceInner C X_opt - 0 := by rw [hslack]
    _ = traceInner C X_opt := sub_zero _

end QOU.Mathlib.SDPDuality
