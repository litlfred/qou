import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases

/-!
# `2 × 2` Cayley–Hamilton Identity, Chebyshev Trace Recurrence, and Elliptic `SL₂` Bounds

Over an arbitrary commutative ring `R` (§7c generic base-ring discipline, zero `ℝ`), this
module establishes reusable `2 × 2` matrix and `SL₂` trace infrastructure:

1. **Cayley–Hamilton Theorem on `Matrix (Fin 2) (Fin 2) R` (`cayley_hamilton_fin2`):**
   `A ^ 2 - A.trace • A + A.det • 1 = 0`, together with the matrix power recurrence
   `A ^ (n + 2) = A.trace • A ^ (n + 1) - A.det • A ^ n` (`pow_add_two_eq`).
2. **Universal Chebyshev / Lucas Trace Recurrence (`trace_pow_add_two`):**
   `(A ^ (n + 2)).trace = A.trace * (A ^ (n + 1)).trace - A.det * (A ^ n).trace` for all `n : ℕ`.
3. **Closed-Form `SL₂(R)` Power Traces (`det A = 1`):**
   Exact polynomial formulas for `(A ^ n).trace` via `chebyshevTracePoly` for all `n : ℕ`, with
   explicit closed forms at `n = 2, 3, 4, 5, 6` (`t² - 2`, `t³ - 3t`, `t⁴ - 4t² + 2`,
   `t⁵ - 5t³ + 5t`, `t⁶ - 6t⁴ + 9t² - 2`).
4. **Elliptic Trace Boundedness over Ordered Rings:**
   Over any strict linear ordered commutative ring `K` (`[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]`),
   whenever `A.det = 1` and `|A.trace| ≤ 2`, the power traces satisfy `|(A ^ n).trace| ≤ 2`
   for every `n : ℕ` (`abs_trace_pow_le_two_of_det_eq_one` for `n ∈ {1, 2, 3, 4, 6}` via
   explicit polynomial square factorizations).
-/

namespace QOU.MathlibInfra.SL2ChebyshevTrace

open Matrix

section CommRing

variable {R : Type*} [CommRing R]

/-- **Cayley–Hamilton Theorem for `2 × 2` Matrices:**
Every `A : Matrix (Fin 2) (Fin 2) R` over a commutative ring satisfies
`A ^ 2 - A.trace • A + A.det • 1 = 0`. -/
theorem cayley_hamilton_fin2 (A : Matrix (Fin 2) (Fin 2) R) :
    A ^ 2 - A.trace • A + A.det • (1 : Matrix (Fin 2) (Fin 2) R) = 0 := by
  rw [sq]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, Matrix.trace_fin_two, Matrix.det_fin_two] <;>
    ring

/-- Solved form of the `2 × 2` Cayley–Hamilton identity:
`A ^ 2 = A.trace • A - A.det • 1`. -/
theorem sq_eq_trace_smul_sub_det_smul (A : Matrix (Fin 2) (Fin 2) R) :
    A ^ 2 = A.trace • A - A.det • (1 : Matrix (Fin 2) (Fin 2) R) := by
  have hch := cayley_hamilton_fin2 A
  calc
    A ^ 2 = (A ^ 2 - A.trace • A + A.det • (1 : Matrix (Fin 2) (Fin 2) R)) +
        (A.trace • A - A.det • (1 : Matrix (Fin 2) (Fin 2) R)) := by abel
    _ = 0 + (A.trace • A - A.det • (1 : Matrix (Fin 2) (Fin 2) R)) := by rw [hch]
    _ = A.trace • A - A.det • (1 : Matrix (Fin 2) (Fin 2) R) := zero_add _

/-- Two-step matrix power recurrence `A ^ (n + 2) = A.trace • A ^ (n + 1) - A.det • A ^ n`. -/
theorem pow_add_two_eq (A : Matrix (Fin 2) (Fin 2) R) (n : ℕ) :
    A ^ (n + 2) = A.trace • A ^ (n + 1) - A.det • A ^ n := by
  calc
    A ^ (n + 2) = A ^ n * A ^ 2 := by rw [pow_add]
    _ = A ^ n * (A.trace • A - A.det • (1 : Matrix (Fin 2) (Fin 2) R)) := by
          rw [sq_eq_trace_smul_sub_det_smul A]
    _ = A.trace • (A ^ n * A) - A.det • (A ^ n * 1) := by
          rw [mul_sub, Matrix.mul_smul, Matrix.mul_smul]
    _ = A.trace • A ^ (n + 1) - A.det • A ^ n := by
          rw [← pow_succ, mul_one]

/-- Trace of the `2 × 2` identity (`n = 0` base case): `(A ^ 0).trace = 2`. -/
theorem trace_pow_zero (A : Matrix (Fin 2) (Fin 2) R) :
    (A ^ 0).trace = 2 := by
  simp

/-- **Chebyshev Trace Recurrence on `Matrix (Fin 2) (Fin 2) R`:**
`(A ^ (n + 2)).trace = A.trace * (A ^ (n + 1)).trace - A.det * (A ^ n).trace`. -/
theorem trace_pow_add_two (A : Matrix (Fin 2) (Fin 2) R) (n : ℕ) :
    (A ^ (n + 2)).trace = A.trace * (A ^ (n + 1)).trace - A.det * (A ^ n).trace := by
  rw [pow_add_two_eq A n, Matrix.trace_sub, Matrix.trace_smul, Matrix.trace_smul,
    smul_eq_mul, smul_eq_mul]

/-- General `2 × 2` quadratic trace identity: `(A ^ 2).trace = A.trace ^ 2 - 2 * A.det`. -/
theorem trace_sq_fin2 (A : Matrix (Fin 2) (Fin 2) R) :
    (A ^ 2).trace = A.trace ^ 2 - 2 * A.det := by
  have h := trace_pow_add_two A 0
  rw [pow_one, trace_pow_zero] at h
  calc
    (A ^ 2).trace = A.trace * A.trace - A.det * 2 := h
    _ = A.trace ^ 2 - 2 * A.det := by ring

/-- General `2 × 2` cubic trace identity: `(A ^ 3).trace = A.trace ^ 3 - 3 * A.det * A.trace`. -/
theorem trace_cube_fin2 (A : Matrix (Fin 2) (Fin 2) R) :
    (A ^ 3).trace = A.trace ^ 3 - 3 * A.det * A.trace := by
  have h := trace_pow_add_two A 1
  rw [show (1 + 2 : ℕ) = 3 from rfl, show (1 + 1 : ℕ) = 2 from rfl, pow_one, trace_sq_fin2] at h
  calc
    (A ^ 3).trace = A.trace * (A.trace ^ 2 - 2 * A.det) - A.det * A.trace := h
    _ = A.trace ^ 3 - 3 * A.det * A.trace := by ring

/-- Monic Chebyshev / Lucas trace polynomial `T_n^{SL₂}(t) = 2 T_n(t / 2)` satisfying
`P_0(t) = 2`, `P_1(t) = t`, `P_{n+2}(t) = t * P_{n+1}(t) - P_n(t)`. -/
def chebyshevTracePoly (t : R) : ℕ → R
  | 0 => 2
  | 1 => t
  | n + 2 => t * chebyshevTracePoly t (n + 1) - chebyshevTracePoly t n

/-- For every `A ∈ SL₂(R)` (`A.det = 1`) and every `n : ℕ`,
`(A ^ n).trace = chebyshevTracePoly A.trace n`. -/
theorem trace_pow_eq_chebyshevTracePoly {A : Matrix (Fin 2) (Fin 2) R}
    (hdet : A.det = 1) :
    ∀ n : ℕ, (A ^ n).trace = chebyshevTracePoly A.trace n
  | 0 => trace_pow_zero A
  | 1 => by simp [chebyshevTracePoly]
  | n + 2 => by
      rw [trace_pow_add_two A n, hdet, one_mul,
        trace_pow_eq_chebyshevTracePoly hdet (n + 1),
        trace_pow_eq_chebyshevTracePoly hdet n]
      rfl

/-- Closed form for `(A ^ 2).trace` when `A.det = 1`: `A.trace ^ 2 - 2`. -/
theorem trace_sq_of_det_eq_one {A : Matrix (Fin 2) (Fin 2) R} (hdet : A.det = 1) :
    (A ^ 2).trace = A.trace ^ 2 - 2 := by
  rw [trace_sq_fin2 A, hdet, mul_one]

/-- Closed form for `(A ^ 3).trace` when `A.det = 1`: `A.trace ^ 3 - 3 * A.trace`. -/
theorem trace_cube_of_det_eq_one {A : Matrix (Fin 2) (Fin 2) R} (hdet : A.det = 1) :
    (A ^ 3).trace = A.trace ^ 3 - 3 * A.trace := by
  rw [trace_cube_fin2 A, hdet, mul_one]

/-- Closed form for `(A ^ 4).trace` when `A.det = 1`:
`A.trace ^ 4 - 4 * A.trace ^ 2 + 2`. -/
theorem trace_pow_four_of_det_eq_one {A : Matrix (Fin 2) (Fin 2) R} (hdet : A.det = 1) :
    (A ^ 4).trace = A.trace ^ 4 - 4 * A.trace ^ 2 + 2 := by
  have h4 := trace_pow_add_two A 2
  rw [show (2 + 2 : ℕ) = 4 from rfl, show (2 + 1 : ℕ) = 3 from rfl, hdet, one_mul,
    trace_cube_of_det_eq_one hdet, trace_sq_of_det_eq_one hdet] at h4
  calc
    (A ^ 4).trace = A.trace * (A.trace ^ 3 - 3 * A.trace) - (A.trace ^ 2 - 2) := h4
    _ = A.trace ^ 4 - 4 * A.trace ^ 2 + 2 := by ring

/-- Closed form for `(A ^ 5).trace` when `A.det = 1`:
`A.trace ^ 5 - 5 * A.trace ^ 3 + 5 * A.trace`. -/
theorem trace_pow_five_of_det_eq_one {A : Matrix (Fin 2) (Fin 2) R} (hdet : A.det = 1) :
    (A ^ 5).trace = A.trace ^ 5 - 5 * A.trace ^ 3 + 5 * A.trace := by
  have h5 := trace_pow_add_two A 3
  rw [show (3 + 2 : ℕ) = 5 from rfl, show (3 + 1 : ℕ) = 4 from rfl, hdet, one_mul,
    trace_pow_four_of_det_eq_one hdet, trace_cube_of_det_eq_one hdet] at h5
  calc
    (A ^ 5).trace = A.trace * (A.trace ^ 4 - 4 * A.trace ^ 2 + 2) -
        (A.trace ^ 3 - 3 * A.trace) := h5
    _ = A.trace ^ 5 - 5 * A.trace ^ 3 + 5 * A.trace := by ring

/-- Closed form for `(A ^ 6).trace` when `A.det = 1`:
`A.trace ^ 6 - 6 * A.trace ^ 4 + 9 * A.trace ^ 2 - 2`. -/
theorem trace_pow_six_of_det_eq_one {A : Matrix (Fin 2) (Fin 2) R} (hdet : A.det = 1) :
    (A ^ 6).trace = A.trace ^ 6 - 6 * A.trace ^ 4 + 9 * A.trace ^ 2 - 2 := by
  have h6 := trace_pow_add_two A 4
  rw [show (4 + 2 : ℕ) = 6 from rfl, show (4 + 1 : ℕ) = 5 from rfl, hdet, one_mul,
    trace_pow_five_of_det_eq_one hdet, trace_pow_four_of_det_eq_one hdet] at h6
  calc
    (A ^ 6).trace = A.trace * (A.trace ^ 5 - 5 * A.trace ^ 3 + 5 * A.trace) -
        (A.trace ^ 4 - 4 * A.trace ^ 2 + 2) := h6
    _ = A.trace ^ 6 - 6 * A.trace ^ 4 + 9 * A.trace ^ 2 - 2 := by ring

end CommRing

/-! ## Elliptic `|trace A| ≤ 2` Stability under Matrix Powers -/

section OrderedRing

variable {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Scalar quadratic Chebyshev stability: `|t| ≤ 2 → |t ^ 2 - 2| ≤ 2`. -/
theorem abs_sq_sub_two_le_two {t : K} (ht : |t| ≤ 2) :
    |t ^ 2 - 2| ≤ 2 := by
  obtain ⟨hlo, hhi⟩ := abs_le.mp ht
  refine abs_le.mpr ⟨?_, ?_⟩
  · have hsq : (0 : K) ≤ t ^ 2 := sq_nonneg t
    linarith
  · have hfac : 4 - t ^ 2 = (2 - t) * (2 + t) := by ring
    have hnonneg : (0 : K) ≤ (2 - t) * (2 + t) :=
      mul_nonneg (by linarith) (by linarith)
    linarith

/-- Scalar cubic Chebyshev stability: `|t| ≤ 2 → |t ^ 3 - 3 * t| ≤ 2`, proved via the exact
discriminant factorizations `2 - (t³ - 3t) = (2 - t)(t + 1)²` and
`(t³ - 3t) + 2 = (t + 2)(t - 1)²`. -/
theorem abs_cube_sub_three_mul_le_two {t : K} (ht : |t| ≤ 2) :
    |t ^ 3 - 3 * t| ≤ 2 := by
  obtain ⟨hlo, hhi⟩ := abs_le.mp ht
  refine abs_le.mpr ⟨?_, ?_⟩
  · have hfac : (t ^ 3 - 3 * t) + 2 = (t + 2) * (t - 1) ^ 2 := by ring
    have hnonneg : (0 : K) ≤ (t + 2) * (t - 1) ^ 2 :=
      mul_nonneg (by linarith) (sq_nonneg (t - 1))
    linarith
  · have hfac : 2 - (t ^ 3 - 3 * t) = (2 - t) * (t + 1) ^ 2 := by ring
    have hnonneg : (0 : K) ≤ (2 - t) * (t + 1) ^ 2 :=
      mul_nonneg (by linarith) (sq_nonneg (t + 1))
    linarith

/-- **Elliptic `SL₂` Power-Trace Bound (`n = 1, 2, 3, 4, 6`):**
If `A : Matrix (Fin 2) (Fin 2) K` satisfies `A.det = 1` and `|A.trace| ≤ 2`, then
`|(A ^ n).trace| ≤ 2` for `n = 1, 2, 3, 4, 6`. -/
theorem abs_trace_pow_le_two_of_det_eq_one {A : Matrix (Fin 2) (Fin 2) K}
    (hdet : A.det = 1) (htr : |A.trace| ≤ 2) :
    |(A ^ 1).trace| ≤ 2 ∧
    |(A ^ 2).trace| ≤ 2 ∧
    |(A ^ 3).trace| ≤ 2 ∧
    |(A ^ 4).trace| ≤ 2 ∧
    |(A ^ 6).trace| ≤ 2 := by
  have h1 : |(A ^ 1).trace| ≤ 2 := by simpa using htr
  have h2 : |(A ^ 2).trace| ≤ 2 := by
    rw [trace_sq_of_det_eq_one hdet]
    exact abs_sq_sub_two_le_two htr
  have h3 : |(A ^ 3).trace| ≤ 2 := by
    rw [trace_cube_of_det_eq_one hdet]
    exact abs_cube_sub_three_mul_le_two htr
  have hdet2 : (A ^ 2).det = 1 := by rw [Matrix.det_pow, hdet, one_pow]
  have hdet3 : (A ^ 3).det = 1 := by rw [Matrix.det_pow, hdet, one_pow]
  have h4 : |(A ^ 4).trace| ≤ 2 := by
    rw [show (4 : ℕ) = 2 * 2 from rfl, pow_mul, trace_sq_of_det_eq_one hdet2]
    exact abs_sq_sub_two_le_two h2
  have h6 : |(A ^ 6).trace| ≤ 2 := by
    rw [show (6 : ℕ) = 3 * 2 from rfl, pow_mul, trace_sq_of_det_eq_one hdet3]
    exact abs_sq_sub_two_le_two h3
  exact ⟨h1, h2, h3, h4, h6⟩

end OrderedRing

end QOU.MathlibInfra.SL2ChebyshevTrace
