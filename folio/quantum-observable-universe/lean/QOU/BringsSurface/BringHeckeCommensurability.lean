/-
Route 2 of the O'Hara selection question (beans `qou-99qc`, `qou-pzsi`):
the exact matrix facts behind `computations/probes/bring_route2/`.

* (L1) Conjugating the Hecke group `H₄ = ⟨S, U⟩` (`S : z ↦ -1/z`, `U : z ↦ z + √2`)
  by `D = diag(1, √2)` (the Möbius map `z ↦ z/√2`, up to scalar) sends `U` to the
  integral translation `T` and `S` to the Fricke involution `W₂ : z ↦ -1/(2z)`
  (projectively), and `W₂ T W₂⁻¹` is the lower-triangular generator of `Γ₀(2)`.
  So `H₄` is commensurable with `PSL(2,ℤ)` through `Γ₀(2)`.
* (L2) Under `σ₀ ↦ [[1,1],[0,1]]`, `σ₁ ↦ [[1,0],[-1,1]]`, the γγ core
  `(σ₀σ₁)³` maps to `-1`, so it is invisible in `PSL(2,ℤ)`.

Matrices are written as `Matrix (Fin 2) (Fin 2) R` over a commutative ring for
(L2); (L1) needs `√2`, so it is stated over `ℝ` (archimedean square root, §7c).
-/
import Mathlib.Data.Matrix.Mul
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Analysis.SpecialFunctions.Pow.Real

namespace QOU.BringHecke

open Matrix

section L2

variable {R : Type*} [CommRing R]

/-- Image of `σ₀`. -/
def tGen : Matrix (Fin 2) (Fin 2) R := !![1, 1; 0, 1]

/-- Image of `σ₁`. -/
def lGen : Matrix (Fin 2) (Fin 2) R := !![1, 0; -1, 1]

/-- (L2) The γγ core `(σ₀σ₁)³` maps to `-1`. -/
theorem gammaGamma_core_eq_neg_one :
    (tGen * lGen * (tGen * lGen) * (tGen * lGen) : Matrix (Fin 2) (Fin 2) R) = -1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [tGen, lGen, Matrix.mul_apply, Fin.sum_univ_two]

/-- The image of `σ₀σ₁` is not `±1`, so the core is a nontrivial element of
`SL(2,ℤ)` whose image in `PSL(2,ℤ)` is trivial. -/
theorem tl_ne_one [Nontrivial R] :
    (tGen * lGen : Matrix (Fin 2) (Fin 2) R) ≠ 1 := by
  intro h
  have := congrFun (congrFun h 0) 1
  simp [tGen, lGen, Matrix.mul_apply, Fin.sum_univ_two] at this

end L2

section L1

/-- `D = diag(1, √2)`, the Möbius map `z ↦ z/√2`. -/
noncomputable def dMat : Matrix (Fin 2) (Fin 2) ℝ := !![1, 0; 0, Real.sqrt 2]

/-- `D⁻¹ = diag(1, 1/√2)`. -/
noncomputable def dInv : Matrix (Fin 2) (Fin 2) ℝ := !![1, 0; 0, (Real.sqrt 2)⁻¹]

/-- Hecke translation `U : z ↦ z + √2`. -/
noncomputable def uHecke : Matrix (Fin 2) (Fin 2) ℝ := !![1, Real.sqrt 2; 0, 1]

/-- Hecke inversion `S : z ↦ -1/z`. -/
def sHecke : Matrix (Fin 2) (Fin 2) ℝ := !![0, -1; 1, 0]

/-- Fricke involution `W₂ : z ↦ -1/(2z)`, as the integral matrix `[[0,-1],[2,0]]`. -/
def fricke : Matrix (Fin 2) (Fin 2) ℝ := !![0, -1; 2, 0]

lemma sqrt2_ne : Real.sqrt 2 ≠ 0 := by positivity

theorem dInv_mul_d : dInv * dMat = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [dInv, dMat, Matrix.mul_apply, Fin.sum_univ_two]

/-- (L1a) `D U D⁻¹ = T`: the Hecke translation by `√2` becomes translation by `1`. -/
theorem conj_uHecke : dMat * uHecke * dInv = !![1, 1; 0, 1] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [dMat, uHecke, dInv, Matrix.mul_apply, Fin.sum_univ_two]

/-- (L1b) `D S D⁻¹ = √2⁻¹ · W₂`: `S` becomes the Fricke involution projectively. -/
theorem conj_sHecke : dMat * sHecke * dInv = (Real.sqrt 2)⁻¹ • fricke := by
  have h2 : Real.sqrt 2 * Real.sqrt 2 = 2 := Real.mul_self_sqrt (by norm_num)
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [dMat, sHecke, dInv, fricke, Matrix.mul_apply, Fin.sum_univ_two]
  field_simp
  linarith [h2]

/-- (L1c) `W₂ T W₂ = -2 · [[1,0],[-2,1]]`: conjugating the integral translation by the
Fricke involution gives, projectively, the lower generator of `Γ₀(2)`. -/
theorem fricke_conj_T :
    fricke * !![1, 1; 0, 1] * fricke = (-2 : ℝ) • !![1, 0; -2, 1] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [fricke, Matrix.mul_apply, Fin.sum_univ_two]

end L1

end QOU.BringHecke
