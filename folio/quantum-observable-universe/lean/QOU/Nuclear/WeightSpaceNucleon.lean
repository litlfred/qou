import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Data.Matrix.Mul
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-!
# Nucleon energy from the weight-space trace of β_Bor (prereg Addendum 14)

`V = ⟨u, d⟩` with `u` of weight `+1`, `d` of weight `−1`. The Hecke-normalised `Ř` is
`uu ↦ q uu`, `dd ↦ q dd`, `ud ↦ du`, `du ↦ ud + h du`. On `V^{⊗3}` the weight space `m = +1` has
basis `(uud, udu, duu)` and `m = −1` has basis `(ddu, dud, udd)`. The matrices below are `σ₀`, `σ₁`
restricted to those spaces (column `j` = image of basis vector `j`). `σ⁻¹ = σ − h` by the Hecke
relation, and β_Bor = (σ₀σ₁⁻¹)³.

* `hecke_plus0`, `hecke_plus1`, `hecke_minus0`, `hecke_minus1`: each matrix satisfies
  `σ² = hσ + 1` when `q² = hq + 1`, so `σ − h` is its inverse.
* `braid_plus`, `braid_minus`: `σ₀σ₁σ₀ = σ₁σ₀σ₁` on both spaces.
* `trace_plus_eq_minus`: the trace of β_Bor on `M_{+1}` equals that on `M_{−1}`, using only
  `q² = hq + 1`.
* `trace_plus_closed`: with `h = q − q⁻¹` that trace is
  `−(q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1)/q⁶`.
* `np_eq_cell`: with nucleon weight `q^m · T` and energy `−E₀ log w`, `E_n − E_p = 2 E₀ log q`.

Premise (G), that the nucleon Gibbs weight is this weight-space trace, is a premise, not derived.
No measured value appears here.
-/

namespace QOU.QBeta.WeightSpaceNucleon

open Matrix

section Generic

variable {R : Type*} [Field R]

/-- `σ₀` on `M_{+1}`, basis `(uud, udu, duu)`. -/
def sPlus0 (q h : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; 0, 0, 1; 0, 1, h]
/-- `σ₁` on `M_{+1}`. -/
def sPlus1 (q h : R) : Matrix (Fin 3) (Fin 3) R := !![0, 1, 0; 1, h, 0; 0, 0, q]
/-- `σ₀` on `M_{−1}`, basis `(ddu, dud, udd)`. -/
def sMinus0 (q h : R) : Matrix (Fin 3) (Fin 3) R := !![q, 0, 0; 0, h, 1; 0, 1, 0]
/-- `σ₁` on `M_{−1}`. -/
def sMinus1 (q h : R) : Matrix (Fin 3) (Fin 3) R := !![h, 1, 0; 1, 0, 0; 0, 0, q]

/-- `σ₀ σ₁⁻¹` with `σ₁⁻¹ = σ₁ − h`, on `M_{+1}`, multiplied out. -/
def stepPlus (q h : R) : Matrix (Fin 3) (Fin 3) R := !![-(h * q), q, 0; 0, 0, q - h; 1, 0, h * q - h ^ 2]
/-- `σ₀ σ₁⁻¹` on `M_{−1}`, multiplied out. -/
def stepMinus (q h : R) : Matrix (Fin 3) (Fin 3) R := !![0, q, 0; h, -(h ^ 2), q - h; 1, -h, 0]

theorem stepPlus_eq (q h : R) :
    sPlus0 q h * (sPlus1 q h - h • (1 : Matrix (Fin 3) (Fin 3) R)) = stepPlus q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sPlus0, sPlus1, stepPlus, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> ring

theorem stepMinus_eq (q h : R) :
    sMinus0 q h * (sMinus1 q h - h • (1 : Matrix (Fin 3) (Fin 3) R)) = stepMinus q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sMinus0, sMinus1, stepMinus, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;>
    ring

theorem hecke_plus0 (q h : R) (hH : q ^ 2 = h * q + 1) :
    sPlus0 q h * sPlus0 q h = h • sPlus0 q h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sPlus0, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | ring1 | linear_combination hH | linear_combination (-1 : R) * hH

theorem hecke_plus1 (q h : R) (hH : q ^ 2 = h * q + 1) :
    sPlus1 q h * sPlus1 q h = h • sPlus1 q h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sPlus1, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | ring1 | linear_combination hH | linear_combination (-1 : R) * hH

theorem hecke_minus0 (q h : R) (hH : q ^ 2 = h * q + 1) :
    sMinus0 q h * sMinus0 q h = h • sMinus0 q h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sMinus0, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | ring1 | linear_combination hH | linear_combination (-1 : R) * hH

theorem hecke_minus1 (q h : R) (hH : q ^ 2 = h * q + 1) :
    sMinus1 q h * sMinus1 q h = h • sMinus1 q h + 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sMinus1, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | ring1 | linear_combination hH | linear_combination (-1 : R) * hH

/-- Braid relation on `M_{+1}`, given `q² = hq + 1`. -/
theorem braid_plus (q h : R) (hH : q ^ 2 = h * q + 1) :
    sPlus0 q h * sPlus1 q h * sPlus0 q h = sPlus1 q h * sPlus0 q h * sPlus1 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sPlus0, sPlus1, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | ring1 | linear_combination h * hH | linear_combination (-h) * hH

/-- Braid relation on `M_{−1}`, given `q² = hq + 1`. -/
theorem braid_minus (q h : R) (hH : q ^ 2 = h * q + 1) :
    sMinus0 q h * sMinus1 q h * sMinus0 q h = sMinus1 q h * sMinus0 q h * sMinus1 q h := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sMinus0, sMinus1, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | ring1 | linear_combination h * hH | linear_combination (-h) * hH

/-- The trace of β_Bor = (σ₀σ₁⁻¹)³ is the same on the weight spaces `m = ±1`. -/
theorem trace_plus_eq_minus (q h : R) (hH : q ^ 2 = h * q + 1) :
    trace ((sPlus0 q h * (sPlus1 q h - h • (1 : Matrix (Fin 3) (Fin 3) R))) ^ 3)
      = trace ((sMinus0 q h * (sMinus1 q h - h • (1 : Matrix (Fin 3) (Fin 3) R))) ^ 3) := by
  rw [stepPlus_eq, stepMinus_eq, pow_three, pow_three]
  simp only [stepPlus, stepMinus, Matrix.mul_fin_three, Matrix.trace_fin_three,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_cons,
    Matrix.head_fin_const, Matrix.tail_cons]
  linear_combination (-3 * h ^ 4) * hH

/-- Closed form of that trace when `h = q − q⁻¹`. -/
theorem trace_plus_closed (q : R) (hq : q ≠ 0) :
    trace ((sPlus0 q (q - q⁻¹) * (sPlus1 q (q - q⁻¹)
        - (q - q⁻¹) • (1 : Matrix (Fin 3) (Fin 3) R))) ^ 3)
      = -(q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6 := by
  rw [stepPlus_eq, pow_three]
  simp only [stepPlus, Matrix.mul_fin_three, Matrix.trace_fin_three,
    Matrix.of_apply, Matrix.cons_val', Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.empty_val', Matrix.cons_val_fin_one, Matrix.head_cons,
    Matrix.head_fin_const, Matrix.tail_cons]
  field_simp
  ring

end Generic

section Real

/-- Nucleon energy `E = −E₀ log(q^m T)`. -/
noncomputable def energy (E₀ q T : ℝ) (m : ℤ) : ℝ := -E₀ * Real.log (q ^ m * T)

/-- With the same weight-space trace `T > 0` for `p` (`m = +1`) and `n` (`m = −1`),
`E_n − E_p = 2 E₀ log q`: the n–p cell, with total weight `1` on the quark split. -/
theorem np_eq_cell (E₀ q T : ℝ) (hq : 0 < q) (hT : 0 < T) :
    energy E₀ q T (-1) - energy E₀ q T 1 = 2 * E₀ * Real.log q := by
  unfold energy
  have h1 : (0 : ℝ) < q ^ (1 : ℤ) := zpow_pos hq _
  have h2 : (0 : ℝ) < q ^ (-1 : ℤ) := zpow_pos hq _
  rw [Real.log_mul h2.ne' hT.ne', Real.log_mul h1.ne' hT.ne', Real.log_zpow, Real.log_zpow]
  push_cast
  ring

end Real

end QOU.QBeta.WeightSpaceNucleon
