import Mathlib.Tactic
import Mathlib.LinearAlgebra.Matrix.Hermitian
import Mathlib.Analysis.Complex.Basic

/-!
# `Herm₂(ℂ) ≅ ℝ^{1,3}`: the determinant is the Minkowski form, and `SL₂(ℂ)` acts by isometries

Bean `qou-7ypv` (QFT-3, math-only core; epic `qou-3fjn`).

The real-linear map `toHerm : ℝ⁴ → M₂(ℂ)`,

  `(t, x, y, z) ↦ [[t + z, x − i y], [x + i y, t − z]]`,

* lands in the Hermitian matrices (`toHerm_isHermitian`),
* is injective and hits every Hermitian matrix (`toHerm_injective`, `exists_toHerm_of_isHermitian`),
  and is additive and real-homogeneous (`toHerm_add`, `toHerm_smul`), so it is a real-linear
  isomorphism `ℝ⁴ ≅ Herm₂(ℂ)`;
* turns the determinant into the Minkowski quadratic form `t² − x² − y² − z²` (`det_toHerm`).

For `A ∈ SL₂(ℂ)` the map `X ↦ A X A*` preserves Hermiticity and the determinant
(`conj_isHermitian`, `det_conj`), so `SL₂(ℂ)` acts on `ℝ^{1,3}` by Lorentz isometries; this is a
left action (`conj_mul`), and its kernel is exactly `{±1}` (`conj_trivial_iff`).

## Scope

Proved: the isomorphism, the isometry property and the kernel. **Not proved here**: that the image
of `SL₂(ℂ)` is all of `SO⁺(1,3)` (surjectivity of the double cover), nor that it lies in the
identity component. Those need a connectedness or generation argument and are left open in this
file rather than assumed.

No Schwinger propagator, worldline loop or Cutkosky threshold is formalised: those were dropped
from the bean when it was re-scoped to mathematics (owner card 2026-11-21).

Standard reference (not yet in the bibliography): Knapp, *Representation Theory of Semisimple Groups*, §II.3 (the
   `SL₂(ℂ) → SO⁺(1,3)` covering).
-/

namespace QOU.QFTMath.SpinorMinkowski

open Matrix Complex

/-- The Hermitian matrix of a Minkowski vector `(t, x, y, z)`. -/
noncomputable def toHerm (v : Fin 4 → ℝ) : Matrix (Fin 2) (Fin 2) ℂ :=
  !![(v 0 + v 3 : ℂ), (v 1 : ℂ) - (v 2 : ℂ) * I; (v 1 : ℂ) + (v 2 : ℂ) * I, (v 0 - v 3 : ℂ)]

/-- The Minkowski quadratic form `t² − x² − y² − z²`. -/
def minkowski (v : Fin 4 → ℝ) : ℝ := v 0 ^ 2 - v 1 ^ 2 - v 2 ^ 2 - v 3 ^ 2

theorem toHerm_isHermitian (v : Fin 4 → ℝ) : (toHerm v).IsHermitian := by
  ext a b
  fin_cases a <;> fin_cases b <;>
    simp [toHerm, Matrix.conjTranspose_apply, Complex.ext_iff]

/-- **The determinant is the Minkowski form.** -/
theorem det_toHerm (v : Fin 4 → ℝ) : (toHerm v).det = (minkowski v : ℂ) := by
  rw [Matrix.det_fin_two]
  simp only [toHerm, minkowski, of_apply, cons_val', cons_val_zero, cons_val_one,
    empty_val', cons_val_fin_one]
  push_cast
  ring_nf
  rw [I_sq]; ring

theorem toHerm_add (v w : Fin 4 → ℝ) : toHerm (v + w) = toHerm v + toHerm w := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [toHerm] <;> ring

theorem toHerm_smul (r : ℝ) (v : Fin 4 → ℝ) : toHerm (r • v) = (r : ℂ) • toHerm v := by
  ext a b; fin_cases a <;> fin_cases b <;> simp [toHerm] <;> ring

theorem toHerm_injective : Function.Injective toHerm := by
  intro v w h
  have h00 := congrFun (congrFun h 0) 0
  have h11 := congrFun (congrFun h 1) 1
  have h10 := congrFun (congrFun h 1) 0
  simp [toHerm, Complex.ext_iff] at h00 h11 h10
  funext k
  fin_cases k <;> simp <;> linarith [h00, h11, h10.1, h10.2]

/-- **Surjectivity onto `Herm₂(ℂ)`**: every Hermitian `2 × 2` matrix is `toHerm v`. -/
theorem exists_toHerm_of_isHermitian (X : Matrix (Fin 2) (Fin 2) ℂ) (hX : X.IsHermitian) :
    ∃ v, toHerm v = X := by
  have e00 : star (X 0 0) = X 0 0 := by simpa using congrFun (congrFun hX 0) 0
  have e11 : star (X 1 1) = X 1 1 := by simpa using congrFun (congrFun hX 1) 1
  have e01 : star (X 1 0) = X 0 1 := by simpa using congrFun (congrFun hX 0) 1
  have r00 : (X 0 0).im = 0 := by
    have := congrArg Complex.im e00; simp at this; linarith
  have r11 : (X 1 1).im = 0 := by
    have := congrArg Complex.im e11; simp at this; linarith
  refine ⟨![((X 0 0).re + (X 1 1).re) / 2, (X 1 0).re, (X 1 0).im,
    ((X 0 0).re - (X 1 1).re) / 2], ?_⟩
  ext a b
  fin_cases a <;> fin_cases b <;> simp [toHerm, Complex.ext_iff]
  · constructor <;> [ring; exact r00.symm]
  · rw [← e01]; simp
  · constructor <;> [ring; exact r11.symm]

/-- The `SL₂(ℂ)` action `X ↦ A X A*`. -/
noncomputable def conj (A X : Matrix (Fin 2) (Fin 2) ℂ) : Matrix (Fin 2) (Fin 2) ℂ := A * X * Aᴴ

theorem conj_isHermitian (A X : Matrix (Fin 2) (Fin 2) ℂ) (hX : X.IsHermitian) :
    (conj A X).IsHermitian := by
  unfold conj Matrix.IsHermitian
  rw [conjTranspose_mul, conjTranspose_mul, conjTranspose_conjTranspose, hX.eq, Matrix.mul_assoc]

/-- **Isometry**: for `det A = 1`, `det (A X A*) = det X`. -/
theorem det_conj (A X : Matrix (Fin 2) (Fin 2) ℂ) (hA : A.det = 1) : (conj A X).det = X.det := by
  unfold conj
  rw [det_mul, det_mul, det_conjTranspose, hA]; simp

/-- So `SL₂(ℂ)` preserves the Minkowski form of `ℝ^{1,3}`. -/
theorem minkowski_conj (A : Matrix (Fin 2) (Fin 2) ℂ) (hA : A.det = 1) (v w : Fin 4 → ℝ)
    (hw : toHerm w = conj A (toHerm v)) : minkowski w = minkowski v := by
  have := det_conj A (toHerm v) hA
  rw [← hw, det_toHerm, det_toHerm] at this
  exact_mod_cast this

/-- The action is a left action: `(AB)·X = A·(B·X)`. -/
theorem conj_mul (A B X : Matrix (Fin 2) (Fin 2) ℂ) : conj (A * B) X = conj A (conj B X) := by
  unfold conj; rw [conjTranspose_mul]; simp only [Matrix.mul_assoc]

/-- **The kernel is `{±1}`**: for `det A = 1`, `A` fixes every Hermitian matrix iff `A = ±1`. -/
theorem conj_trivial_iff (A : Matrix (Fin 2) (Fin 2) ℂ) (hA : A.det = 1) :
    (∀ X : Matrix (Fin 2) (Fin 2) ℂ, X.IsHermitian → conj A X = X) ↔ (A = 1 ∨ A = -1) := by
  constructor
  · intro h
    have hU : A * Aᴴ = 1 := by
      simpa [conj] using h 1 (by simp [Matrix.IsHermitian])
    have hU' : Aᴴ * A = 1 := mul_eq_one_comm.mp hU
    have hcomm : ∀ X : Matrix (Fin 2) (Fin 2) ℂ, X.IsHermitian → A * X = X * A := by
      intro X hX
      have := congrArg (· * A) (h X hX)
      simp only [conj, Matrix.mul_assoc, hU', Matrix.mul_one] at this
      exact this
    have hE : (!![1, 0; 0, 0] : Matrix (Fin 2) (Fin 2) ℂ).IsHermitian := by
      ext a b; fin_cases a <;> fin_cases b <;> simp [Matrix.conjTranspose_apply]
    have hS : (!![0, 1; 1, 0] : Matrix (Fin 2) (Fin 2) ℂ).IsHermitian := by
      ext a b; fin_cases a <;> fin_cases b <;> simp [Matrix.conjTranspose_apply]
    have c1 := hcomm _ hE
    have c2 := hcomm _ hS
    have a01 : A 0 1 = 0 := by
      have := congrFun (congrFun c1 0) 1; simp [Matrix.mul_apply, Fin.sum_univ_two] at this
      exact this.symm
    have a10 : A 1 0 = 0 := by
      have := congrFun (congrFun c1 1) 0; simp [Matrix.mul_apply, Fin.sum_univ_two] at this
      exact this
    have a11 : A 1 1 = A 0 0 := by
      have := congrFun (congrFun c2 0) 1; simp [Matrix.mul_apply, Fin.sum_univ_two] at this
      exact this.symm
    have hdet : A 0 0 * A 0 0 = 1 := by
      rw [Matrix.det_fin_two, a01, a10, a11] at hA; simpa using hA
    rcases mul_self_eq_one_iff.mp hdet with h0 | h0
    · left; ext a b; fin_cases a <;> fin_cases b <;> simp [a01, a10, a11, h0]
    · right; ext a b; fin_cases a <;> fin_cases b <;> simp [a01, a10, a11, h0]
  · rintro (rfl | rfl) X _ <;> simp [conj]

end QOU.QFTMath.SpinorMinkowski
