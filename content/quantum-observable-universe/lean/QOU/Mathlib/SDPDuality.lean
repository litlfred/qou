import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.Spectrum
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

/-- `tr(diag(d) * M) = ∑ dᵢ Mᵢᵢ`. -/
private lemma trace_diagonal_mul' [DecidableEq (Fin n)]
    (d : Fin n → ℝ) (M : Matrix (Fin n) (Fin n) ℝ) :
    (diagonal d * M).trace = ∑ i, d i * M i i := by
  simp only [Matrix.trace, Matrix.diag, diagonal_mul]

/-- Diagonal entries of a PSD matrix are nonneg: `Mᵢᵢ ≥ 0`. -/
private lemma psd_diag_nonneg
    (M : Matrix (Fin n) (Fin n) ℝ) (hM : M.PosSemidef) (i : Fin n) :
    0 ≤ M i i := by
  have h := hM.2 (fun j => if j = i then 1 else 0)
  simp only [star_trivial, dotProduct, mulVec] at h
  have key : ∀ x : Fin n, (if x = i then (1 : ℝ) else 0) *
      ∑ y : Fin n, M x y * (if y = i then 1 else 0) =
      if x = i then M i i else 0 := by
    intro x
    by_cases hx : x = i
    · subst hx; simp [Finset.sum_ite_eq']
    · simp [hx]
  simp_rw [key] at h
  simp [Finset.sum_ite_eq'] at h
  exact h

/-- **`tr(SX) ≥ 0` for PSD S and X.**
    Proof: spectral decomposition `S = U diag(λ) U*` with `λᵢ ≥ 0`,
    trace cyclicity gives `tr(SX) = tr(diag(λ) · U*XU)`,
    `U*XU` is PSD (by `conjTranspose_mul_mul_same`),
    then `Σ λᵢ (U*XU)ᵢᵢ ≥ 0` since both factors are nonneg. -/
theorem traceInner_nonneg_of_posSemidef
    (S X : Matrix (Fin n) (Fin n) ℝ)
    (hS : Matrix.PosSemidef S) (hX : Matrix.PosSemidef X) :
    0 ≤ traceInner S X := by
  classical
  unfold traceInner
  let ev := hS.1.eigenvalues
  let U : Matrix (Fin n) (Fin n) ℝ := hS.1.eigenvectorUnitary
  have hev_nn : ∀ i, 0 ≤ ev i := hS.eigenvalues_nonneg
  have hspec : S = U * diagonal ev * star U := by
    have := hS.1.spectral_theorem
    rw [show RCLike.ofReal ∘ ev = ev from funext fun _ => rfl] at this
    exact this
  have hP : (star U * X * U).PosSemidef := by
    show (Uᴴ * X * U).PosSemidef
    exact hX.conjTranspose_mul_mul_same U
  have key : (S * X).trace = (diagonal ev * (star U * X * U)).trace := by
    conv_lhs => rw [hspec]
    simp only [mul_assoc]
    rw [trace_mul_comm U]
    simp only [mul_assoc]
  rw [key, trace_diagonal_mul']
  exact Finset.sum_nonneg fun i _ => mul_nonneg (hev_nn i) (psd_diag_nonneg _ hP i)

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
        linarith [traceInner_nonneg_of_posSemidef S X hS_psd hX_psd]

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
