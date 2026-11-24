/-
Copyright (c) 2026. All rights reserved.

# Why a braid word multiplies the proton and neutron sectors by one common factor

Observed in the γγ gluon-strand words (issue #8833): `ε_p / ε_n` is the same for every word.
The mechanism, in the steps this file proves:

* `jimboR_comm_coprodF` : the Jimbo R-matrix on two strands commutes with
  `Δ(F) = F ⊗ K + 1 ⊗ F`, the coproduct of the `U_q(sl₂)` lowering operator. So every braid
  word commutes with `Δⁿ(F)`.
* `lowerQuark_det`, `lowerQuark_isUnit_det` : on three quark strands `Δ³(F)` maps the
  one-down weight space to the two-down weight space by a `3 × 3` matrix of determinant
  `−(q² + 1)/q`, invertible when `q² + 1 ≠ 0`.
* `trace_eq_of_intertwine` : if an invertible `F` intertwines `Y₁` and `Y₂`
  (`F * Y₁ = Y₂ * F`), the traces agree. So a weight-preserving operator that commutes with
  `Δ³(F)` has the same trace `t` on both sectors.
* `epsP_eq_q_sq_mul_epsN` : with `K`-weights `q` and `q⁻¹` on the two sectors, `ε_p = q² ε_n`.

* `ptr_intertwines` : the `K`-weighted partial trace over extra (gluon) strands of an operator
  commuting with `Δ(F) = F ⊗ K + 1 ⊗ F` commutes with `F` on the remaining (quark) strands.

Not formalised here: lifting `jimboR_comm_coprodF` from two strands to `Δⁿ(F)` on `n` strands
(each `Rᵢ` commutes with the terms of `Δⁿ(F)` away from strands `i, i+1` because it preserves
weight, and with the two terms on them by the two-strand lemma). Checked exactly, word by word,
in `computations/probes/qbeta_shared_factor`.

Generic field, no ordering, no empirical input.
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic

namespace QOU.QBeta.QuarkWeightTrace

open Matrix

variable {R : Type*} [Field R]

/-- Jimbo R on two strands, basis `↑↑, ↑↓, ↓↑, ↓↓` (column = image of a basis vector). -/
def jimboR (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, q - q⁻¹, 0;
     0, 0, 0, q]

/-- `Δ(F) = F ⊗ K + 1 ⊗ F`, with `F` lowering `↑ ↦ ↓` and `K = diag(q, q⁻¹)`. -/
def coprodF (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![0, 0, 0, 0;
     1, 0, 0, 0;
     q, 0, 0, 0;
     0, q⁻¹, 1, 0]

theorem jimboR_comm_coprodF (q : R) (hq : q ≠ 0) :
    jimboR q * coprodF q = coprodF q * jimboR q := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [jimboR, coprodF, Matrix.mul_apply, Fin.sum_univ_four] <;> field_simp <;> ring

/-- `Δ³(F)` from the one-down quark sector (`↑↑↓, ↑↓↑, ↓↑↑`) to the two-down sector
(`↑↓↓, ↓↑↓, ↓↓↑`). -/
def lowerQuark (q : R) : Matrix (Fin 3) (Fin 3) R :=
  !![q⁻¹, 1, 0;
     1, 0, 1;
     0, 1, q]

theorem lowerQuark_det (q : R) (hq : q ≠ 0) : (lowerQuark q).det = -(q ^ 2 + 1) / q := by
  simp [lowerQuark, Matrix.det_fin_three]
  field_simp
  ring

theorem lowerQuark_isUnit_det (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    IsUnit (lowerQuark q).det := by
  rw [lowerQuark_det q hq, isUnit_iff_ne_zero]
  exact div_ne_zero (neg_ne_zero.mpr h2) hq

/-- An invertible intertwiner preserves the trace. -/
theorem trace_eq_of_intertwine {n : Type*} [Fintype n] [DecidableEq n]
    (F Y₁ Y₂ : Matrix n n R) (hF : IsUnit F.det) (h : F * Y₁ = Y₂ * F) :
    Y₁.trace = Y₂.trace := by
  have hY₂ : Y₂ = F * Y₁ * F⁻¹ := by
    rw [h, Matrix.mul_assoc, Matrix.mul_nonsing_inv _ hF, Matrix.mul_one]
  rw [hY₂, Matrix.trace_mul_comm, ← Matrix.mul_assoc, Matrix.nonsing_inv_mul _ hF,
    Matrix.one_mul]

/-- Proton sector: `K`-weight `q`, trace `t`, normalisation `D`. -/
def epsP (q t D : R) : R := q * t / D

/-- Neutron sector: `K`-weight `q⁻¹`, the same trace `t`, the same `D`. -/
def epsN (q t D : R) : R := q⁻¹ * t / D

theorem epsP_eq_q_sq_mul_epsN (q t D : R) (hq : q ≠ 0) :
    epsP q t D = q ^ 2 * epsN q t D := by
  unfold epsP epsN
  field_simp

/-- The whole chain on three quark strands: a weight-preserving operator whose sector blocks
are intertwined by `Δ³(F)` gives `ε_p = q² ε_n`. -/
theorem epsP_eq_q_sq_mul_epsN_of_intertwine (q D : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (Y₁ Y₂ : Matrix (Fin 3) (Fin 3) R) (h : lowerQuark q * Y₁ = Y₂ * lowerQuark q) :
    q * Y₁.trace / D = q ^ 2 * (q⁻¹ * Y₂.trace / D) := by
  rw [← trace_eq_of_intertwine _ _ _ (lowerQuark_isUnit_det q hq h2) h]
  exact epsP_eq_q_sq_mul_epsN q _ D hq

/-! ## Partial trace over extra strands -/

section PartialTrace

variable {a b : Type*} [Fintype a] [Fintype b] [DecidableEq a] [DecidableEq b]

/-- Partial trace over the second factor. -/
def ptr (N : Matrix (a × b) (a × b) R) : Matrix a a R := fun i j => ∑ β, N (i, β) (j, β)

/-- `B` acting on the second factor only (`1 ⊗ B`). -/
def onW (B : Matrix b b R) : Matrix (a × b) (a × b) R :=
  fun x y => if x.1 = y.1 then B x.2 y.2 else 0

/-- `A ⊗ B`. -/
def kr (A : Matrix a a R) (B : Matrix b b R) : Matrix (a × b) (a × b) R :=
  fun x y => A x.1 y.1 * B x.2 y.2

theorem onW_mul_apply (B : Matrix b b R) (M : Matrix (a × b) (a × b) R) (x y : a × b) :
    (onW B * M : Matrix (a × b) (a × b) R) x y = ∑ γ, B x.2 γ * M (x.1, γ) y := by
  simp only [onW, Matrix.mul_apply, Fintype.sum_prod_type, ite_mul, zero_mul]
  rw [Finset.sum_comm]
  simp

theorem mul_onW_apply (B : Matrix b b R) (M : Matrix (a × b) (a × b) R) (x y : a × b) :
    (M * onW B : Matrix (a × b) (a × b) R) x y = ∑ γ, M x (y.1, γ) * B γ y.2 := by
  simp only [onW, Matrix.mul_apply, Fintype.sum_prod_type, mul_ite, mul_zero]
  rw [Finset.sum_comm]
  simp [eq_comm]

theorem ptr_onW_mul_apply (B : Matrix b b R) (M : Matrix (a × b) (a × b) R) (i j : a) :
    ptr (onW B * M) i j = ∑ β, ∑ γ, B β γ * M (i, γ) (j, β) := by
  simp only [ptr, onW_mul_apply]

theorem ptr_kr_mul (A : Matrix a a R) (B : Matrix b b R) (M : Matrix (a × b) (a × b) R) :
    ptr (kr A B * M) = A * ptr (onW B * M) := by
  ext i j
  rw [Matrix.mul_apply]
  simp only [ptr_onW_mul_apply, Finset.mul_sum]
  simp only [ptr, kr, Matrix.mul_apply, Fintype.sum_prod_type]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
    Finset.sum_congr rfl fun _ _ => by ring

theorem ptr_mul_kr (A : Matrix a a R) (B : Matrix b b R) (M : Matrix (a × b) (a × b) R) :
    ptr (M * kr A B) = ptr (onW B * M) * A := by
  ext i j
  rw [Matrix.mul_apply]
  simp only [ptr_onW_mul_apply, Finset.sum_mul]
  simp only [ptr, kr, Matrix.mul_apply, Fintype.sum_prod_type]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun _ _ => ?_
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => by ring

theorem ptr_onW_comm (B : Matrix b b R) (M : Matrix (a × b) (a × b) R) :
    ptr (onW B * M) = ptr (M * onW B) := by
  ext i j
  simp only [ptr, onW_mul_apply, mul_onW_apply]
  rw [Finset.sum_comm]
  exact Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => mul_comm _ _

/-- **A partial trace of an intertwiner is an intertwiner.** If `M` on `V ⊗ W` commutes with
`Δ(F) = F_V ⊗ K_W + 1 ⊗ F_W`, then `Y = Tr_W((1 ⊗ K_W) M)` commutes with `F_V`. -/
theorem ptr_intertwines (FV : Matrix a a R) (KW FW : Matrix b b R)
    (M : Matrix (a × b) (a × b) R)
    (h : (kr FV KW + onW FW) * M = M * (kr FV KW + onW FW)) :
    FV * ptr (onW KW * M) = ptr (onW KW * M) * FV := by
  have h2 := congrArg ptr h
  simp only [Matrix.add_mul, Matrix.mul_add] at h2
  have hadd : ∀ N P : Matrix (a × b) (a × b) R, ptr (N + P) = ptr N + ptr P := by
    intro N P; ext i j; simp [ptr, Finset.sum_add_distrib]
  rw [hadd, hadd, ptr_kr_mul, ptr_mul_kr, ptr_onW_comm FW M] at h2
  exact add_right_cancel h2

end PartialTrace

end QOU.QBeta.QuarkWeightTrace
