/-
Route 2 of the O'Hara selection question (beans `qou-99qc`, `qou-pzsi`, `qou-brfy`):
the traces in `Δ(2,4,5)` that `computations/probes/bring_route2/results.md` reports
"recognised by eye as elements of ℤ[φ]" are now proved.

Setting. `Δ(2,4,5)` is realised in `SL(2)` by two matrices `S`, `U` with

    det S = det U = 1,   tr S = 0,   tr U = φ,   tr (S U) = r,

where `φ² = φ + 1` (so `φ = 2cos(π/5)`) and `r² = 2` (so `r = ±2cos(π/4)`). No particular
matrices are chosen: every statement below holds for **every** such pair, over any
commutative ring, so it does not depend on the realisation the probe happened to use
(rigidity of the triangle group is not needed).

Results (the five `H₄`-words of `results.json`, with `U⁻¹ = U⁹`, `U⁻³ = U⁷`):

| word (probe row)                       | SL(2) trace |
|---|---|
| `U⁹`        (nuc11_interleaved, gluon_s0_s1, gluon_s0_s0) | `φ`   |
| `S U S U`   (nuc9)                     | `0`   |
| `U S U⁹ S`  (gluon_s1_s0)              | `-φ²` |
| `S U S U³`  (gluon_s1_s1)              | `φ²`  |
| `U⁷ S U² S` (nuc11_gen_grouped)        | `-2φ` |

So every `|tr|` lies in `ℤ[φ]`, and `r` enters only through `r² = 2`. Along the way
`U⁵ = -1` (`U` has order 10 in `SL(2)`, order 5 in `PSL(2)`) and `S² = -1`.

Scope. These are traces of the words the probe produced. Which braid each word comes from,
and whether those braids are the scored nucleon, is not claimed here: `results_signed.md`
withdraws the "seen candidate" reading (the scored nucleon is a sum of four braids).
-/
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.LinearCombination

namespace QOU.BringTriangle

open Matrix

variable {R : Type*} [CommRing R]

/-- Cayley–Hamilton for `2 × 2` matrices: `M² = (tr M) M - (det M) 1`. -/
theorem sq_eq_trace_smul_sub (M : Matrix (Fin 2) (Fin 2) R) :
    M * M = M.trace • M - M.det • (1 : Matrix (Fin 2) (Fin 2) R) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two, Matrix.det_fin_two] <;> ring

/-- The data of a `Δ(2,4,5)` realisation in `SL(2, R)`, in trace coordinates. -/
structure Delta245 (R : Type*) [CommRing R] where
  /-- the order-2 generator -/
  S : Matrix (Fin 2) (Fin 2) R
  /-- the order-5 generator (image of the Hecke translation) -/
  U : Matrix (Fin 2) (Fin 2) R
  /-- `φ = 2 cos(π/5)` -/
  φ : R
  /-- `r = ±2 cos(π/4)` -/
  r : R
  detS : S.det = 1
  detU : U.det = 1
  trS : S.trace = 0
  trU : U.trace = φ
  trSU : (S * U).trace = r
  φ_sq : φ ^ 2 = φ + 1
  r_sq : r ^ 2 = 2

namespace Delta245

variable (D : Delta245 R)

theorem S_sq : D.S * D.S = -1 := by
  rw [sq_eq_trace_smul_sub, D.trS, D.detS]; simp

theorem U_sq : D.U * D.U = D.φ • D.U - 1 := by
  rw [sq_eq_trace_smul_sub, D.trU, D.detU, one_smul]

theorem U_pow_two : D.U ^ 2 = D.φ • D.U - 1 := by rw [pow_two, U_sq]

theorem U_pow_three : D.U ^ 3 = D.φ • D.U - D.φ • 1 := by
  rw [pow_succ, U_pow_two, sub_mul, smul_mul_assoc, U_sq, one_mul, smul_sub, smul_smul,
    ← pow_two, D.φ_sq, add_smul, one_smul, smul_one_eq_diagonal]
  abel

theorem U_pow_four : D.U ^ 4 = D.U - D.φ • 1 := by
  rw [pow_succ, U_pow_three, sub_mul, smul_mul_assoc, U_sq, smul_mul_assoc, one_mul, smul_sub,
    smul_smul, ← pow_two, D.φ_sq, add_smul, one_smul]
  abel

/-- `U⁵ = -1`: `U` has order `10` in `SL(2)` and order `5` in `PSL(2)`. -/
theorem U_pow_five : D.U ^ 5 = -1 := by
  rw [pow_succ, U_pow_four, sub_mul, U_sq, smul_mul_assoc, one_mul]
  abel

theorem U_pow_seven : D.U ^ 7 = -(D.φ • D.U - 1) := by
  rw [show 7 = 5 + 2 by rfl, pow_add, U_pow_five, U_pow_two, neg_one_mul]

theorem U_pow_nine : D.U ^ 9 = D.φ • 1 - D.U := by
  rw [show 9 = 5 + 4 by rfl, pow_add, U_pow_five, U_pow_four, neg_one_mul, neg_sub]

theorem trace_one : (1 : Matrix (Fin 2) (Fin 2) R).trace = 2 := by
  simp

/-- `tr (S U S) = -φ`. -/
theorem trace_SUS : (D.S * D.U * D.S).trace = -D.φ := by
  rw [Matrix.trace_mul_comm, ← mul_assoc, S_sq, neg_one_mul, Matrix.trace_neg, D.trU]

/-- `tr (S U S U) = tr((SU)²) = r² - 2 = 0`. -/
theorem trace_SUSU : (D.S * D.U * D.S * D.U).trace = 0 := by
  have h := sq_eq_trace_smul_sub (D.S * D.U)
  rw [D.trSU, Matrix.det_mul, D.detS, D.detU, one_mul, one_smul] at h
  rw [show D.S * D.U * D.S * D.U = D.S * D.U * (D.S * D.U) by simp only [mul_assoc], h,
    Matrix.trace_sub, Matrix.trace_smul, D.trSU, trace_one, smul_eq_mul, ← pow_two, D.r_sq]
  ring

/-- `tr (U S S) = -φ`, the cyclic twin of `trace_SUS`. -/
theorem trace_USS : (D.U * D.S * D.S).trace = -D.φ := by
  rw [mul_assoc, S_sq, mul_neg_one, Matrix.trace_neg, D.trU]

/-- `tr (U S U S) = 0`. -/
theorem trace_USUS : (D.U * D.S * D.U * D.S).trace = 0 := by
  rw [show D.U * D.S * D.U * D.S = D.U * (D.S * D.U * D.S) by simp only [mul_assoc],
    Matrix.trace_mul_comm, show D.S * D.U * D.S * D.U = D.S * D.U * D.S * D.U from rfl,
    trace_SUSU]

/-! ### The five probe words -/

/-- `tr U⁹ = tr U⁻¹ = φ` (rows nuc11_interleaved, gluon_s0_s1, gluon_s0_s0). -/
theorem trace_U_inv : (D.U ^ 9).trace = D.φ := by
  rw [U_pow_nine, Matrix.trace_sub, Matrix.trace_smul, trace_one, D.trU, smul_eq_mul]; ring

/-- `tr (S U S U) = 0` (row nuc9: elliptic of order 2). -/
theorem trace_nuc9 : (D.S * D.U * D.S * D.U).trace = 0 := D.trace_SUSU

/-- `tr (U S U⁹ S) = -φ²` (row gluon_s1_s0). -/
theorem trace_gluon_s1_s0 : (D.U * D.S * D.U ^ 9 * D.S).trace = -D.φ ^ 2 := by
  rw [U_pow_nine, mul_sub, sub_mul, Matrix.trace_sub, mul_smul_comm, mul_one, smul_mul_assoc,
    Matrix.trace_smul, trace_USS, trace_USUS, smul_eq_mul]
  ring

/-- `tr (S U S U³) = φ²` (row gluon_s1_s1). -/
theorem trace_gluon_s1_s1 : (D.S * D.U * D.S * D.U ^ 3).trace = D.φ ^ 2 := by
  rw [U_pow_three, mul_sub, mul_smul_comm, mul_smul_comm, mul_one, Matrix.trace_sub,
    Matrix.trace_smul, Matrix.trace_smul, trace_SUSU, trace_SUS, smul_eq_mul, smul_eq_mul]
  ring

/-- `tr (U⁷ S U² S) = -2φ` (row nuc11_gen_grouped). -/
theorem trace_gen_grouped : (D.U ^ 7 * D.S * D.U ^ 2 * D.S).trace = -(2 * D.φ) := by
  have hSS := D.S_sq
  have e : D.U ^ 7 * D.S * D.U ^ 2 * D.S
      = -(D.φ ^ 2 • (D.U * D.S * D.U * D.S) - D.φ • (D.U * D.S * D.S)
          - D.φ • (D.S * D.U * D.S) + D.S * D.S) := by
    rw [U_pow_seven, U_pow_two]
    simp only [neg_mul, sub_mul, mul_sub, smul_mul_assoc, mul_smul_comm, one_mul, mul_one,
      mul_assoc, pow_two]
    simp only [smul_neg, smul_sub, smul_smul]
    abel
  rw [e, Matrix.trace_neg, Matrix.trace_add, Matrix.trace_sub, Matrix.trace_sub,
    Matrix.trace_smul, Matrix.trace_smul, Matrix.trace_smul, trace_USUS, trace_USS, trace_SUS,
    hSS, Matrix.trace_neg, trace_one]
  simp only [smul_eq_mul]
  linear_combination (-2 : R) * D.φ_sq

end Delta245

end QOU.BringTriangle
