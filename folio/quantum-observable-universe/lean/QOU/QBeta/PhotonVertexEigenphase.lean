/-
Copyright (c) 2026. All rights reserved.

# The V_(2,1) eigenphase of the photon vertex and of the γγ base V³

The photon's pair-production vertex is `V = σ₀σ₁⁻¹` (owner ruling 2026-11-20), and the
scored Q_β base is `V³` (`docs/audits/2026-11-20-qbeta-flavour-weight-split.md`). This file
computes the trace and determinant of `V` and `V³` on the two-dimensional Hecke block
`V_(2,1)`, using only the Hecke relation and the four character values that define that block.

Results (generic `[Field R]`, `h = q − q⁻¹`):

* `det_vertex`         : det V = 1.
* `trace_vertex`       : tr V = −(1 + h²).
* `trace_cube_of_det_one` : a 2×2 matrix with det 1 has tr M³ = (tr M)³ − 3 tr M.
* `two_sub_trace_vertex_cube` : 2 − tr V³ = h⁴ (h² + 3).
* `qInt_three_eq`      : h² + 3 = q² + 1 + q⁻² = [3]_q (symmetric q-integer).

Archimedean consequence (ordered field, after the wall):

* `vertex_cube_elliptic` : if h ≠ 0 and h² < 1 then −2 < tr V³ < 2. So V³ has a
  complex-conjugate pair of unit-modulus eigenvalues on V_(2,1); its eigenphase θ is real and
  satisfies 4 sin²(θ/2) = h⁴ [3]_q. A ladder factor built from that phase is a cosine, ≤ 1,
  and cannot supply a factor above 1.

No empirical input appears anywhere in this file.
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Chebyshev
import Mathlib.Tactic.FinCases
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse

namespace QOU.QBeta.PhotonVertexEigenphase

open Matrix

variable {R : Type*} [Field R]

/-- Cayley–Hamilton for 2×2 matrices of determinant one, at the third power. -/
theorem trace_cube_of_det_one (M : Matrix (Fin 2) (Fin 2) R) (hM : M.det = 1) :
    (M ^ 3).trace = M.trace ^ 3 - 3 * M.trace := by
  rw [Matrix.det_fin_two] at hM
  simp only [pow_succ, pow_zero, Matrix.one_mul, Matrix.trace_fin_two, Matrix.mul_apply,
    Fin.sum_univ_two]
  linear_combination (-3 * (M 0 0 + M 1 1)) * hM

/-- The data of the V_(2,1) block: two matrices satisfying the Hecke relation
`σ² = h σ + 1`, with the character values `χ(σ) = h`, `det σ = −1` and
`χ(σ₀σ₁) = −1`. -/
structure HeckeBlock (h : R) where
  S0 : Matrix (Fin 2) (Fin 2) R
  S1 : Matrix (Fin 2) (Fin 2) R
  hecke1 : S1 * S1 = h • S1 + 1
  tr0 : S0.trace = h
  det0 : S0.det = -1
  det1 : S1.det = -1
  tr01 : (S0 * S1).trace = -1

/-- `σ₁⁻¹ = σ₁ − h` in the block, so the vertex is `V = σ₀ (σ₁ − h)`. -/
def vertex {h : R} (B : HeckeBlock h) : Matrix (Fin 2) (Fin 2) R :=
  B.S0 * (B.S1 - h • (1 : Matrix (Fin 2) (Fin 2) R))

theorem S1_mul_inv {h : R} (B : HeckeBlock h) :
    B.S1 * (B.S1 - h • (1 : Matrix (Fin 2) (Fin 2) R)) = 1 := by
  rw [Matrix.mul_sub, B.hecke1, Matrix.mul_smul, Matrix.mul_one]
  abel

theorem det_vertex {h : R} (B : HeckeBlock h) : (vertex B).det = 1 := by
  have h1 := congrArg Matrix.det (S1_mul_inv B)
  rw [Matrix.det_mul, B.det1, Matrix.det_one] at h1
  have h2 : (B.S1 - h • (1 : Matrix (Fin 2) (Fin 2) R)).det = -1 := by
    linear_combination -h1
  rw [vertex, Matrix.det_mul, B.det0, h2]
  ring

theorem trace_vertex {h : R} (B : HeckeBlock h) : (vertex B).trace = -(1 + h ^ 2) := by
  rw [vertex, Matrix.mul_sub, Matrix.trace_sub, Matrix.mul_smul, Matrix.mul_one,
    Matrix.trace_smul, B.tr01, B.tr0, smul_eq_mul]
  ring

theorem two_sub_trace_vertex_cube {h : R} (B : HeckeBlock h) :
    2 - (vertex B ^ 3).trace = h ^ 4 * (h ^ 2 + 3) := by
  rw [trace_cube_of_det_one _ (det_vertex B), trace_vertex B]
  ring

/-- `h² + 3` is the symmetric quantum integer `[3]_q = q² + 1 + q⁻²`. -/
theorem qInt_three_eq (q qi : R) (hq : q * qi = 1) :
    (q - qi) ^ 2 + 3 = q ^ 2 + 1 + qi ^ 2 := by
  linear_combination (-2 : R) * hq

/-- Archimedean side: on the real slice with `0 < h² < 1` the block of `V³` is elliptic. -/
theorem vertex_cube_elliptic {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {h : K} (B : HeckeBlock h) (hh : h ≠ 0) (hsmall : h ^ 2 < 1) :
    -2 < (vertex B ^ 3).trace ∧ (vertex B ^ 3).trace < 2 := by
  have key := two_sub_trace_vertex_cube B
  have hpos : 0 < h ^ 2 := by positivity
  have h4 : 0 < h ^ 4 * (h ^ 2 + 3) := by positivity
  have _ := hh
  constructor
  · have hx2 : h ^ 2 * h ^ 2 < 1 := by nlinarith
    have hlt : h ^ 4 * (h ^ 2 + 3) < 4 := by
      have e : h ^ 4 * (h ^ 2 + 3) = (h ^ 2 * h ^ 2) * (h ^ 2 + 3) := by ring
      rw [e]
      calc (h ^ 2 * h ^ 2) * (h ^ 2 + 3) < 1 * 4 :=
            mul_lt_mul'' hx2 (by linarith) (by positivity) (by positivity)
        _ = 4 := by norm_num
    linarith
  · linarith

/-! ### The whole γγ tower `V^{3k}`

The flavour split on a weight space `W ≅ V_3 ⊕ V_(2,1)` is
`ε_flavour(V^{3k}) = −h·(1 + tr_{V_(2,1)} V^{3k}) / [2]_q³` (σ acts as `q` on `V_3`, so `V`
acts as `1` there). The results below bound the bracket for every `k`: `|1 + tr V^{3k}| ≤ 3`.
So no member of the tower, and no average over it with non-negative weights summing to one,
exceeds `3h/[2]_q³`. -/

/-- Cayley–Hamilton: a 2×2 matrix of determinant one satisfies `M² = (tr M) M − 1`. -/
theorem sq_of_det_one (M : Matrix (Fin 2) (Fin 2) R) (hM : M.det = 1) :
    M * M = M.trace • M - 1 := by
  rw [Matrix.det_fin_two] at hM
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two] <;>
    first | linear_combination (-1 : R) * hM | ring

theorem trace_pow_add_two (M : Matrix (Fin 2) (Fin 2) R) (hM : M.det = 1) (n : ℕ) :
    (M ^ (n + 2)).trace = M.trace * (M ^ (n + 1)).trace - (M ^ n).trace := by
  rw [pow_add, sq, sq_of_det_one M hM, Matrix.mul_sub, Matrix.mul_smul, Matrix.mul_one,
    ← pow_succ, Matrix.trace_sub, Matrix.trace_smul, smul_eq_mul]

open Polynomial Polynomial.Chebyshev in
/-- `tr Mⁿ = 2 Tₙ(tr M / 2)` for a real 2×2 matrix of determinant one. -/
theorem trace_pow_eq_chebyshev (M : Matrix (Fin 2) (Fin 2) ℝ) (hM : M.det = 1) (n : ℕ) :
    (M ^ n).trace = 2 * (T ℝ (n : ℤ)).eval (M.trace / 2) := by
  have key : ∀ m : ℕ, (M ^ m).trace = 2 * (T ℝ (m : ℤ)).eval (M.trace / 2) ∧
      (M ^ (m + 1)).trace = 2 * (T ℝ ((m + 1 : ℕ) : ℤ)).eval (M.trace / 2) := by
    intro m
    induction m with
    | zero =>
      refine ⟨?_, ?_⟩
      · norm_num [Matrix.trace_one]
      · simp; ring
    | succ m ih =>
      refine ⟨ih.2, ?_⟩
      rw [trace_pow_add_two M hM, ih.1, ih.2]
      have e : ((m + 1 + 1 : ℕ) : ℤ) = (m : ℤ) + 2 := by push_cast; ring
      have e1 : ((m + 1 : ℕ) : ℤ) = (m : ℤ) + 1 := by push_cast; ring
      rw [e, e1, T_add_two]
      simp only [eval_sub, eval_mul, eval_X, eval_ofNat]
      ring
  exact (key n).1

/-- A real 2×2 matrix of determinant one with `|tr M| ≤ 2` has `|tr Mⁿ| ≤ 2` for all `n`. -/
theorem abs_trace_pow_le_two (M : Matrix (Fin 2) (Fin 2) ℝ) (hM : M.det = 1)
    (ht : |M.trace| ≤ 2) (n : ℕ) : |(M ^ n).trace| ≤ 2 := by
  obtain ⟨h1, h2⟩ := abs_le.mp ht
  have hc : Real.cos (Real.arccos (M.trace / 2)) = M.trace / 2 :=
    Real.cos_arccos (by linarith) (by linarith)
  rw [trace_pow_eq_chebyshev M hM n, ← hc, Polynomial.Chebyshev.T_real_cos, abs_mul]
  have hb := Real.abs_cos_le_one (((n : ℤ) : ℝ) * Real.arccos (M.trace / 2))
  rw [abs_two]
  linarith

/-- The γγ tower bracket: `|1 + tr_{V_(2,1)} V^{3k}| ≤ 3` for every `k`. -/
theorem tower_bracket_le_three {h : ℝ} (B : HeckeBlock h) (hh : h ≠ 0) (hsmall : h ^ 2 < 1)
    (k : ℕ) : |1 + (vertex B ^ (3 * k)).trace| ≤ 3 := by
  have hdet : (vertex B ^ 3).det = 1 := by rw [Matrix.det_pow, det_vertex B]; norm_num
  obtain ⟨l, u⟩ := vertex_cube_elliptic B hh hsmall
  have ht : |(vertex B ^ 3).trace| ≤ 2 := abs_le.mpr ⟨by linarith, by linarith⟩
  have hk := abs_trace_pow_le_two _ hdet ht k
  rw [← pow_mul] at hk
  calc |1 + (vertex B ^ (3 * k)).trace| ≤ |(1 : ℝ)| + |(vertex B ^ (3 * k)).trace| :=
        abs_add_le _ _
    _ ≤ 3 := by rw [abs_one]; linarith

end QOU.QBeta.PhotonVertexEigenphase
