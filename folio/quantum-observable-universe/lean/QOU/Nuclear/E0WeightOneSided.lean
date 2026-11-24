/-
# E₀'s weight and positive crossings (prereg Addendum 3)

Two facts used in `computations/probes/e0_weight/` Addendum 3.

* `jimboR_mul_sub`: in the 2-strand Jimbo representation, `R · (R − h·1) = 1` with `h = q − q⁻¹`.
  So `σ⁻¹ = σ − h` is a polynomial in `σ`. "Built from positive crossings only" therefore picks out
  nothing in the Hecke algebra itself; it is a property of braid **words**, not of elements.
* `smul_one_add_smul_jimboR_eq`: `a·1 + b·R` is a scalar matrix only if `b = 0`. So no
  combination of `1` and `σ` other than a constant is central, and `ℏ_q` is not the scalar of a
  one-sided skein relation the way `h` is for `σ − σ⁻¹ = h`.
* `ne_weight_of_vanish_neg_one`: a function that vanishes at `q = −1` is not the weight
  `w(q) = (q − 1)/q³`, since `w(−1) = 2`. Every increment the probe found with leading coefficient
  1 at `q = 1` has the factor `q + 1` (it is `h` times a trace), so this excludes all of them.

No empirical number enters. The variable `q` is formal (any field with `q ≠ 0`).
-/
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum

namespace QOU.QBeta.E0WeightOneSided

open Matrix

variable {K : Type*} [Field K]

/-- The 2-strand Jimbo R-matrix in the basis `11, 12, 21, 22`, with `h = q − q⁻¹`. -/
def jimboR (q : K) : Matrix (Fin 4) (Fin 4) K :=
  !![q, 0, 0, 0;
     0, 0, 1, 0;
     0, 1, q - q⁻¹, 0;
     0, 0, 0, q]

/-- **`σ⁻¹ = σ − h`.** `R · (R − h·1) = 1`, for every `q ≠ 0`. -/
theorem jimboR_mul_sub (q : K) (hq : q ≠ 0) :
    jimboR q * (jimboR q - (q - q⁻¹) • (1 : Matrix (Fin 4) (Fin 4) K)) = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [jimboR, Matrix.mul_apply, Fin.sum_univ_four, Matrix.one_apply] <;>
    field_simp

/-- The inverse crossing is `R − h·1`. -/
theorem jimboR_inv_eq (q : K) (hq : q ≠ 0) :
    (jimboR q)⁻¹ = jimboR q - (q - q⁻¹) • (1 : Matrix (Fin 4) (Fin 4) K) :=
  Matrix.inv_eq_right_inv (jimboR_mul_sub q hq)

/-- **`a + bσ` is a scalar only if `b = 0`.** Read off the `(12, 21)` entry. -/
theorem smul_one_add_smul_jimboR_eq (q a b c : K)
    (h : a • (1 : Matrix (Fin 4) (Fin 4) K) + b • jimboR q = c • 1) : b = 0 := by
  have := congrFun (congrFun h 1) 2
  simpa [jimboR, Matrix.one_apply] using this

/-- E₀'s weight `w = ℏ_q/q² = (q − 1)/q³`. -/
noncomputable def weight (q : K) : K := (q - 1) / q ^ 3

theorem weight_neg_one [CharZero K] : weight (-1 : K) = 2 := by
  unfold weight; norm_num

/-- **A function vanishing at `q = −1` is not the weight.** -/
theorem ne_weight_of_vanish_neg_one [CharZero K] (f : K → K) (hf : f (-1) = 0) :
    f ≠ weight := by
  intro h
  have := congrFun h (-1)
  rw [hf, weight_neg_one] at this
  norm_num at this

/-- In particular `h · g` is never the weight, for any `g` (here `h = (q − 1)(q + 1)/q`). -/
theorem skein_mul_ne_weight [CharZero K] (g : K → K) :
    (fun q : K => (q - q⁻¹) * g q) ≠ weight :=
  ne_weight_of_vanish_neg_one _ (by norm_num)

end QOU.QBeta.E0WeightOneSided
