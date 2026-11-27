import Mathlib.Data.Nat.Choose.Vandermonde
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Zify
import Mathlib.Tactic.IntervalCases

set_option autoImplicit false

/-!
# Falling-factorial moments of `C(n,k)²` and the depth-2 tail collapse

Combinatorial half of the depth-2 tail `ν_{n−2}(n)` (bean `qou-swk4`, audit
`docs/audits/2026-11-27-covariance-kernel-depth-two-tail.md`).

1. **Moments.** `Σ_k C(n,k)²·(n−k)_j = (n)_j · C(n + (n−j), n)` (`sum_choose_sq_mul_descFactorial`),
   from the absorption identity `(n−k)_j·C(n,k) = (n)_j·C(n−j,k)` and Vandermonde.
2. **Collapse.** With `g(k) = (n−k−2)(k−1)(k−2)` and `W(k) = 6·ω₃` of the shape
   `(n−k, 3, 1^{k−3})` written as a polynomial in `k`,
   `(n−3)·Σ_{k=0}^{n} g(k)²·W(k)·C(n,k)² = 2(n−2)³(n−5)·Q(n)·C(2n−8, n−4)` for `n ≥ 4`
   (`depthTwo_sum_collapse`), `Q` the sextic of `YoungDiagramTailThirdInstance`.

Everything here is over `ℕ`, `ℤ` and `ℚ`; nothing archimedean.
-/

namespace QOU.BraidsAndKnots.DepthTwoBinomialMoments

open Finset

/-! ## 1. Falling-factorial moments -/

/-- The falling factorial `m.descFactorial j`, cast to `ℤ`, is `∏_{i<j} (m − i)`. -/
theorem descFactorial_cast_int (m : ℕ) : ∀ j : ℕ,
    ((m.descFactorial j : ℕ) : ℤ) = ∏ i ∈ range j, ((m : ℤ) - i)
  | 0 => by simp
  | j + 1 => by
    rw [Nat.descFactorial_succ, prod_range_succ, Nat.cast_mul, descFactorial_cast_int m j]
    by_cases h : j ≤ m
    · rw [Nat.cast_sub h]; ring
    · have h0 : m.descFactorial j = 0 := Nat.descFactorial_eq_zero_iff_lt.mpr (by omega)
      rw [← descFactorial_cast_int m j, h0]; simp

/-- `(N − k)·C(N, k) = N·C(N − 1, k)`. -/
theorem sub_mul_choose (N k : ℕ) : (N - k) * N.choose k = N * (N - 1).choose k := by
  cases N with
  | zero => simp
  | succ M =>
      have h := Nat.choose_mul_succ_eq M k
      simp only [Nat.add_sub_cancel]
      rw [mul_comm, ← h]; ring

/-- **Absorption**: `(n − k)_j · C(n, k) = (n)_j · C(n − j, k)`. -/
theorem descFactorial_sub_mul_choose (n k : ℕ) : ∀ j : ℕ,
    (n - k).descFactorial j * n.choose k = n.descFactorial j * (n - j).choose k
  | 0 => by simp
  | j + 1 => by
    have ih := descFactorial_sub_mul_choose n k j
    have hs := sub_mul_choose (n - j) k
    have e1 : n - k - j = n - j - k := by omega
    have e2 : n - j - 1 = n - (j + 1) := by omega
    rw [e2] at hs
    rw [Nat.descFactorial_succ, Nat.descFactorial_succ, e1]
    calc (n - j - k) * (n - k).descFactorial j * n.choose k
        = (n - j - k) * ((n - k).descFactorial j * n.choose k) := by ring
      _ = (n - j - k) * (n.descFactorial j * (n - j).choose k) := by rw [ih]
      _ = n.descFactorial j * ((n - j - k) * (n - j).choose k) := by ring
      _ = n.descFactorial j * ((n - j) * (n - (j + 1)).choose k) := by rw [hs]
      _ = (n - j) * n.descFactorial j * (n - (j + 1)).choose k := by ring

/-- **Vandermonde**: `Σ_{k ≤ n} C(n, k)·C(m, k) = C(n + m, n)`. -/
theorem sum_choose_mul_choose (n m : ℕ) :
    ∑ k ∈ range (n + 1), n.choose k * m.choose k = (n + m).choose n := by
  rw [Nat.add_choose_eq, Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  rw [← Finset.sum_range_reflect]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hk' : k ≤ n := Nat.lt_succ_iff.mp (mem_range.mp hk)
  have e1 : n + 1 - 1 - k = n - k := by omega
  rw [e1, Nat.choose_symm hk']

/-- **Falling-factorial moments of `C(n,k)²`**:
`Σ_{k ≤ n} C(n, k)²·(n − k)_j = (n)_j · C(n + (n − j), n)`. -/
theorem sum_choose_sq_mul_descFactorial (n j : ℕ) :
    ∑ k ∈ range (n + 1), n.choose k ^ 2 * (n - k).descFactorial j
      = n.descFactorial j * (n + (n - j)).choose n := by
  have h : ∀ k ∈ range (n + 1), n.choose k ^ 2 * (n - k).descFactorial j
      = n.descFactorial j * (n.choose k * (n - j).choose k) := by
    intro k _
    calc n.choose k ^ 2 * (n - k).descFactorial j
        = n.choose k * ((n - k).descFactorial j * n.choose k) := by ring
      _ = n.choose k * (n.descFactorial j * (n - j).choose k) := by
          rw [descFactorial_sub_mul_choose]
      _ = n.descFactorial j * (n.choose k * (n - j).choose k) := by ring
  rw [Finset.sum_congr rfl h, ← Finset.mul_sum, sum_choose_mul_choose]

/-- The `ℤ` form of the moments. -/
theorem sum_choose_sq_mul_descFactorial_int (n j : ℕ) :
    ∑ k ∈ range (n + 1), ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial j : ℕ) : ℤ))
      = ((n.descFactorial j : ℕ) : ℤ) * (((n + (n - j)).choose n : ℕ) : ℤ) := by
  have h := congrArg (fun z : ℕ => (z : ℤ)) (sum_choose_sq_mul_descFactorial n j)
  push_cast at h
  exact h


/-! ## 2. The depth-2 collapse -/

/-- `g(k) = (n − k − 2)(k − 1)(k − 2)`, i.e. `2(n − 2)` times `f^λ / C(n, k)` on the row-side
depth-2 carrier `(n − k, 3, 1^{k−3})`. -/
def depthTwoG (n k : ℤ) : ℤ := (n - k - 2) * (k - 1) * (k - 2)

/-- `W(k) = 6·ω₃` of the shape `(n − k, 3, 1^{k−3})`, as a polynomial in `k`. -/
def depthTwoW (n k : ℤ) : ℤ :=
  (n - k - 1) * (n - k) * (2 * (n - k) - 1) + 12 + (k - 2) * (k - 1) * (2 * k - 3) - 6
    - 3 * n * (n - 1)

/-- The `k`-th term `g(k)²·W(k)·C(n,k)²` of the unified depth-2 sum. -/
def depthTwoTerm (n k : ℕ) : ℤ :=
  depthTwoG n k ^ 2 * depthTwoW n k * (n.choose k : ℤ) ^ 2

/-- The sextic `Q(n) = n⁶ − 25n⁵ + 235n⁴ − 1067n³ + 2528n² − 3112n + 1680` over `ℤ`. -/
def sexticZ (x : ℤ) : ℤ :=
  x ^ 6 - 25 * x ^ 5 + 235 * x ^ 4 - 1067 * x ^ 3 + 2528 * x ^ 2 - 3112 * x + 1680

/-- The term `g²·W` written in the falling-factorial basis `(n − k)_j`, `j ≤ 8`. -/
theorem depthTwoTerm_expand (n k : ℕ) (hk : k ≤ n) :
    depthTwoTerm n k =
      (8*(n:ℤ)^7 - 96*(n:ℤ)^6 + 456*(n:ℤ)^5 - 1104*(n:ℤ)^4 + 1440*(n:ℤ)^3 - 960*(n:ℤ)^2
          + 256*(n:ℤ)) * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 0 : ℕ) : ℤ))
      + (-6*(n:ℤ)^7 + 58*(n:ℤ)^6 - 162*(n:ℤ)^5 - 106*(n:ℤ)^4 + 1432*(n:ℤ)^3 - 2976*(n:ℤ)^2
          + 2624*(n:ℤ) - 864) * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 1 : ℕ) : ℤ))
      + (2*(n:ℤ)^7 - 10*(n:ℤ)^6 - 66*(n:ℤ)^5 + 658*(n:ℤ)^4 - 2152*(n:ℤ)^3 + 3456*(n:ℤ)^2
          - 2752*(n:ℤ) + 864) * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 2 : ℕ) : ℤ))
      + (-14*(n:ℤ)^6 + 222*(n:ℤ)^5 - 1542*(n:ℤ)^4 + 6062*(n:ℤ)^3 - 14152*(n:ℤ)^2
          + 18304*(n:ℤ) - 10032) * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 3 : ℕ) : ℤ))
      + (42*(n:ℤ)^5 - 744*(n:ℤ)^4 + 5406*(n:ℤ)^3 - 19920*(n:ℤ)^2 + 36624*(n:ℤ) - 26256)
          * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 4 : ℕ) : ℤ))
      + (-68*(n:ℤ)^4 + 1114*(n:ℤ)^3 - 6802*(n:ℤ)^2 + 17924*(n:ℤ) - 16464)
          * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 5 : ℕ) : ℤ))
      + (62*(n:ℤ)^3 - 810*(n:ℤ)^2 + 3316*(n:ℤ) - 3888)
          * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 6 : ℕ) : ℤ))
      + (-30*(n:ℤ)^2 + 246*(n:ℤ) - 372)
          * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 7 : ℕ) : ℤ))
      + (6*(n:ℤ) - 12) * ((n.choose k : ℤ) ^ 2 * (((n - k).descFactorial 8 : ℕ) : ℤ)) := by
  simp only [descFactorial_cast_int, prod_range_succ, prod_range_zero, Nat.cast_sub hk]
  unfold depthTwoTerm depthTwoG depthTwoW
  push_cast
  ring


/-- The unified depth-2 sum as a combination of the nine moments. -/
theorem depthTwo_sum_eq_moments (n : ℕ) :
    ∑ k ∈ range (n + 1), depthTwoTerm n k =
      (8*(n:ℤ)^7 - 96*(n:ℤ)^6 + 456*(n:ℤ)^5 - 1104*(n:ℤ)^4 + 1440*(n:ℤ)^3 - 960*(n:ℤ)^2 + 256*(n:ℤ)) * (((n.descFactorial 0 : ℕ) : ℤ) * (((n + (n - 0)).choose n : ℕ) : ℤ))
      + (-6*(n:ℤ)^7 + 58*(n:ℤ)^6 - 162*(n:ℤ)^5 - 106*(n:ℤ)^4 + 1432*(n:ℤ)^3 - 2976*(n:ℤ)^2 + 2624*(n:ℤ) - 864) * (((n.descFactorial 1 : ℕ) : ℤ) * (((n + (n - 1)).choose n : ℕ) : ℤ))
      + (2*(n:ℤ)^7 - 10*(n:ℤ)^6 - 66*(n:ℤ)^5 + 658*(n:ℤ)^4 - 2152*(n:ℤ)^3 + 3456*(n:ℤ)^2 - 2752*(n:ℤ) + 864) * (((n.descFactorial 2 : ℕ) : ℤ) * (((n + (n - 2)).choose n : ℕ) : ℤ))
      + (-14*(n:ℤ)^6 + 222*(n:ℤ)^5 - 1542*(n:ℤ)^4 + 6062*(n:ℤ)^3 - 14152*(n:ℤ)^2 + 18304*(n:ℤ) - 10032) * (((n.descFactorial 3 : ℕ) : ℤ) * (((n + (n - 3)).choose n : ℕ) : ℤ))
      + (42*(n:ℤ)^5 - 744*(n:ℤ)^4 + 5406*(n:ℤ)^3 - 19920*(n:ℤ)^2 + 36624*(n:ℤ) - 26256) * (((n.descFactorial 4 : ℕ) : ℤ) * (((n + (n - 4)).choose n : ℕ) : ℤ))
      + (-68*(n:ℤ)^4 + 1114*(n:ℤ)^3 - 6802*(n:ℤ)^2 + 17924*(n:ℤ) - 16464) * (((n.descFactorial 5 : ℕ) : ℤ) * (((n + (n - 5)).choose n : ℕ) : ℤ))
      + (62*(n:ℤ)^3 - 810*(n:ℤ)^2 + 3316*(n:ℤ) - 3888) * (((n.descFactorial 6 : ℕ) : ℤ) * (((n + (n - 6)).choose n : ℕ) : ℤ))
      + (-30*(n:ℤ)^2 + 246*(n:ℤ) - 372) * (((n.descFactorial 7 : ℕ) : ℤ) * (((n + (n - 7)).choose n : ℕ) : ℤ))
      + (6*(n:ℤ) - 12) * (((n.descFactorial 8 : ℕ) : ℤ) * (((n + (n - 8)).choose n : ℕ) : ℤ)) := by
  rw [Finset.sum_congr rfl fun k hk =>
    depthTwoTerm_expand n k (Nat.lt_succ_iff.mp (mem_range.mp hk))]
  simp only [Finset.sum_add_distrib, ← Finset.mul_sum, sum_choose_sq_mul_descFactorial_int]


/-- `C(A, k)·(A − k) = C(A − 1, k)·A` in `ℚ`. -/
theorem choose_step_q (A k : ℕ) (hA : 1 ≤ A) (hk : k ≤ A) :
    ((A.choose k : ℕ) : ℚ) * ((A : ℚ) - k) = (((A - 1).choose k : ℕ) : ℚ) * A := by
  obtain ⟨N, rfl⟩ : ∃ N, A = N + 1 := ⟨A - 1, by omega⟩
  have h := Nat.choose_mul_succ_eq N k
  have h' := congrArg (fun z : ℕ => (z : ℚ)) h
  simp only [Nat.cast_mul, Nat.cast_sub hk, Nat.cast_add, Nat.cast_one] at h'
  simp only [Nat.add_sub_cancel, Nat.cast_add, Nat.cast_one]
  linarith [h']

/-- `C(N, k + 1)·(k + 1) = C(N, k)·(N − k)` in `ℚ`. -/
theorem choose_right_q (N k : ℕ) (hk : k ≤ N) :
    ((N.choose (k + 1) : ℕ) : ℚ) * ((k : ℚ) + 1) = ((N.choose k : ℕ) : ℚ) * ((N : ℚ) - k) := by
  have h := congrArg (fun z : ℕ => (z : ℚ)) (Nat.choose_succ_right_eq N k)
  simp only [Nat.cast_mul, Nat.cast_sub hk, Nat.cast_add, Nat.cast_one] at h
  exact h

/-- The linear algebra behind the collapse: the nine moments `(n)_j·C(2n − j, n)` reduce to
`C(2n − 8, n − 4)` through the step relations of `C(·, ·)`. Pure `ℚ` algebra, `n = x + 8`. -/
theorem collapse_algebra (x n B G1 G2 G3 D0 D1 D2 D3 D4 D5 D6 D7 D8 : ℚ) (hx : 0 ≤ x)
    (hn : n = x + 8)
    (g1 : G1 * (x + 5) = B * (x + 4)) (g2 : G2 * (x + 6) = G1 * (x + 3))
    (g3 : G3 * (x + 7) = G2 * (x + 2)) (g4 : D8 * (x + 8) = G3 * (x + 1))
    (r7 : D7 * (x + 1) = D8 * (2 * x + 9)) (r6 : D6 * (x + 2) = D7 * (2 * x + 10))
    (r5 : D5 * (x + 3) = D6 * (2 * x + 11)) (r4 : D4 * (x + 4) = D5 * (2 * x + 12))
    (r3 : D3 * (x + 5) = D4 * (2 * x + 13)) (r2 : D2 * (x + 6) = D3 * (2 * x + 14))
    (r1 : D1 * (x + 7) = D2 * (2 * x + 15)) (r0 : D0 * (x + 8) = D1 * (2 * x + 16)) :
    (n - 3) * ((8*n^7 - 96*n^6 + 456*n^5 - 1104*n^4 + 1440*n^3 - 960*n^2 + 256*n) * (1) * D0
        + (-6*n^7 + 58*n^6 - 162*n^5 - 106*n^4 + 1432*n^3 - 2976*n^2 + 2624*n - 864) * (1*(n - 0)) * D1
        + (2*n^7 - 10*n^6 - 66*n^5 + 658*n^4 - 2152*n^3 + 3456*n^2 - 2752*n + 864) * (1*(n - 0)*(n - 1)) * D2
        + (-14*n^6 + 222*n^5 - 1542*n^4 + 6062*n^3 - 14152*n^2 + 18304*n - 10032) * (1*(n - 0)*(n - 1)*(n - 2)) * D3
        + (42*n^5 - 744*n^4 + 5406*n^3 - 19920*n^2 + 36624*n - 26256) * (1*(n - 0)*(n - 1)*(n - 2)*(n - 3)) * D4
        + (-68*n^4 + 1114*n^3 - 6802*n^2 + 17924*n - 16464) * (1*(n - 0)*(n - 1)*(n - 2)*(n - 3)*(n - 4)) * D5
        + (62*n^3 - 810*n^2 + 3316*n - 3888) * (1*(n - 0)*(n - 1)*(n - 2)*(n - 3)*(n - 4)*(n - 5)) * D6
        + (-30*n^2 + 246*n - 372) * (1*(n - 0)*(n - 1)*(n - 2)*(n - 3)*(n - 4)*(n - 5)*(n - 6)) * D7
        + (6*n - 12) * (1*(n - 0)*(n - 1)*(n - 2)*(n - 3)*(n - 4)*(n - 5)*(n - 6)*(n - 7)) * D8)
      = 2 * (n - 2) ^ 3 * (n - 5)
        * (n ^ 6 - 25 * n ^ 5 + 235 * n ^ 4 - 1067 * n ^ 3 + 2528 * n ^ 2 - 3112 * n + 1680) * B := by
  subst hn
  have hM : (x + 1) * (x + 2) * (x + 4) ≠ 0 := by positivity
  have key : (x + 1) * (x + 2) * (x + 4) * (((x + 8) - 3) * ((8*(x + 8)^7 - 96*(x + 8)^6 + 456*(x + 8)^5 - 1104*(x + 8)^4 + 1440*(x + 8)^3 - 960*(x + 8)^2 + 256*(x + 8)) * (1) * D0
        + (-6*(x + 8)^7 + 58*(x + 8)^6 - 162*(x + 8)^5 - 106*(x + 8)^4 + 1432*(x + 8)^3 - 2976*(x + 8)^2 + 2624*(x + 8) - 864) * (1*((x + 8) - 0)) * D1
        + (2*(x + 8)^7 - 10*(x + 8)^6 - 66*(x + 8)^5 + 658*(x + 8)^4 - 2152*(x + 8)^3 + 3456*(x + 8)^2 - 2752*(x + 8) + 864) * (1*((x + 8) - 0)*((x + 8) - 1)) * D2
        + (-14*(x + 8)^6 + 222*(x + 8)^5 - 1542*(x + 8)^4 + 6062*(x + 8)^3 - 14152*(x + 8)^2 + 18304*(x + 8) - 10032) * (1*((x + 8) - 0)*((x + 8) - 1)*((x + 8) - 2)) * D3
        + (42*(x + 8)^5 - 744*(x + 8)^4 + 5406*(x + 8)^3 - 19920*(x + 8)^2 + 36624*(x + 8) - 26256) * (1*((x + 8) - 0)*((x + 8) - 1)*((x + 8) - 2)*((x + 8) - 3)) * D4
        + (-68*(x + 8)^4 + 1114*(x + 8)^3 - 6802*(x + 8)^2 + 17924*(x + 8) - 16464) * (1*((x + 8) - 0)*((x + 8) - 1)*((x + 8) - 2)*((x + 8) - 3)*((x + 8) - 4)) * D5
        + (62*(x + 8)^3 - 810*(x + 8)^2 + 3316*(x + 8) - 3888) * (1*((x + 8) - 0)*((x + 8) - 1)*((x + 8) - 2)*((x + 8) - 3)*((x + 8) - 4)*((x + 8) - 5)) * D6
        + (-30*(x + 8)^2 + 246*(x + 8) - 372) * (1*((x + 8) - 0)*((x + 8) - 1)*((x + 8) - 2)*((x + 8) - 3)*((x + 8) - 4)*((x + 8) - 5)*((x + 8) - 6)) * D7
        + (6*(x + 8) - 12) * (1*((x + 8) - 0)*((x + 8) - 1)*((x + 8) - 2)*((x + 8) - 3)*((x + 8) - 4)*((x + 8) - 5)*((x + 8) - 6)*((x + 8) - 7)) * D8)
      - 2 * ((x + 8) - 2) ^ 3 * ((x + 8) - 5)
        * ((x + 8) ^ 6 - 25 * (x + 8) ^ 5 + 235 * (x + 8) ^ 4 - 1067 * (x + 8) ^ 3
          + 2528 * (x + 8) ^ 2 - 3112 * (x + 8) + 1680) * B) = 0 := by
    linear_combination (8*(x + 1)*(x + 2)*(x + 4)^2*(x + 5)*(x + 6)^3*(x + 7)^2) * r0 + (-2*(x + 1)*(x + 2)*(x + 4)*(x + 5)*(x + 6)^3*(x + 8)*(3*x^3 + 56*x^2 + 331*x + 622)) * r1 + (2*(x + 1)*(x + 2)*(x + 4)*(x + 5)*(x + 6)^2*(x + 8)*(x^5 + 34*x^4 + 443*x^3 + 2788*x^2 + 8526*x + 10172)) * r2 + (-2*(x + 1)*(x + 2)*(x + 4)*(x + 6)^2*(x + 7)*(x + 8)*(5*x^5 + 115*x^4 + 1067*x^3 + 4987*x^2 + 11726*x + 11084)) * r3 + (2*(x + 1)*(x + 2)*(x + 6)^2*(x + 7)*(x + 8)*(11*x^6 + 257*x^5 + 2503*x^4 + 13037*x^3 + 38392*x^2 + 60744*x + 40408)) * r4 + (-2*(x + 1)*(x + 2)*(x + 6)^2*(x + 7)*(x + 8)*(12*x^6 + 257*x^5 + 2266*x^4 + 10565*x^3 + 27604*x^2 + 38496*x + 22368)) * r5 + (2*(x + 1)*(x + 6)^2*(x + 7)*(x + 8)*(7*x^7 + 158*x^6 + 1491*x^5 + 7584*x^4 + 22176*x^3 + 36280*x^2 + 29168*x + 8352)) * r6 + (-2*(x + 5)*(x + 6)^2*(x + 7)*(x + 8)*(x^7 + 11*x^6 + 3*x^5 - 387*x^4 - 1488*x^3 + 244*x^2 + 8768*x + 9216)) * r7 + (2*(x + 5)*(x + 6)^4*(x + 7)*(x^6 + 23*x^5 + 195*x^4 + 693*x^3 + 600*x^2 - 1640*x - 2224)) * g4 + (2*(x + 1)*(x + 5)*(x + 6)^4*(x^6 + 23*x^5 + 195*x^4 + 693*x^3 + 600*x^2 - 1640*x - 2224)) * g3 + (2*(x + 1)*(x + 2)*(x + 5)*(x + 6)^3*(x^6 + 23*x^5 + 195*x^4 + 693*x^3 + 600*x^2 - 1640*x - 2224)) * g2 + (2*(x + 1)*(x + 2)*(x + 3)*(x + 6)^3*(x^6 + 23*x^5 + 195*x^4 + 693*x^3 + 600*x^2 - 1640*x - 2224)) * g1
  exact sub_eq_zero.mp ((mul_eq_zero.mp key).resolve_left hM)


/-- **The depth-2 collapse for `n = m + 8`**:
`(n − 3)·Σ_k g(k)²·W(k)·C(n,k)² = 2(n − 2)³(n − 5)·Q(n)·C(2n − 8, n − 4)`. -/
theorem depthTwo_sum_collapse_add_eight (m : ℕ) :
    (((m + 8 : ℕ) : ℤ) - 3) * ∑ k ∈ range (m + 8 + 1), depthTwoTerm (m + 8) k
      = 2 * (((m + 8 : ℕ) : ℤ) - 2) ^ 3 * (((m + 8 : ℕ) : ℤ) - 5) * sexticZ ((m + 8 : ℕ) : ℤ)
        * (((2 * (m + 8) - 8).choose (m + 8 - 4) : ℕ) : ℤ) := by
  rw [depthTwo_sum_eq_moments]
  simp only [descFactorial_cast_int, prod_range_succ, prod_range_zero]
  rw [show m + 8 + (m + 8 - 0) = 2 * m + 16 by omega, show m + 8 + (m + 8 - 1) = 2 * m + 15 by omega,
    show m + 8 + (m + 8 - 2) = 2 * m + 14 by omega, show m + 8 + (m + 8 - 3) = 2 * m + 13 by omega,
    show m + 8 + (m + 8 - 4) = 2 * m + 12 by omega, show m + 8 + (m + 8 - 5) = 2 * m + 11 by omega,
    show m + 8 + (m + 8 - 6) = 2 * m + 10 by omega, show m + 8 + (m + 8 - 7) = 2 * m + 9 by omega,
    show m + 8 + (m + 8 - 8) = 2 * m + 8 by omega, show 2 * (m + 8) - 8 = 2 * m + 8 by omega,
    show m + 8 - 4 = m + 4 by omega]
  rw [← Int.cast_inj (α := ℚ)]
  push_cast
  unfold sexticZ
  push_cast
  have g1 := choose_right_q (2 * m + 8) (m + 4) (by omega)
  have g2 := choose_right_q (2 * m + 8) (m + 5) (by omega)
  have g3 := choose_right_q (2 * m + 8) (m + 6) (by omega)
  have g4 := choose_right_q (2 * m + 8) (m + 7) (by omega)
  rw [show m + 4 + 1 = m + 5 by omega] at g1
  rw [show m + 5 + 1 = m + 6 by omega] at g2
  rw [show m + 6 + 1 = m + 7 by omega] at g3
  rw [show m + 7 + 1 = m + 8 by omega] at g4
  have r0 := choose_step_q (2 * m + 16) (m + 8) (by omega) (by omega)
  have r1 := choose_step_q (2 * m + 15) (m + 8) (by omega) (by omega)
  have r2 := choose_step_q (2 * m + 14) (m + 8) (by omega) (by omega)
  have r3 := choose_step_q (2 * m + 13) (m + 8) (by omega) (by omega)
  have r4 := choose_step_q (2 * m + 12) (m + 8) (by omega) (by omega)
  have r5 := choose_step_q (2 * m + 11) (m + 8) (by omega) (by omega)
  have r6 := choose_step_q (2 * m + 10) (m + 8) (by omega) (by omega)
  have r7 := choose_step_q (2 * m + 9) (m + 8) (by omega) (by omega)
  rw [show 2 * m + 16 - 1 = 2 * m + 15 by omega] at r0
  rw [show 2 * m + 15 - 1 = 2 * m + 14 by omega] at r1
  rw [show 2 * m + 14 - 1 = 2 * m + 13 by omega] at r2
  rw [show 2 * m + 13 - 1 = 2 * m + 12 by omega] at r3
  rw [show 2 * m + 12 - 1 = 2 * m + 11 by omega] at r4
  rw [show 2 * m + 11 - 1 = 2 * m + 10 by omega] at r5
  rw [show 2 * m + 10 - 1 = 2 * m + 9 by omega] at r6
  rw [show 2 * m + 9 - 1 = 2 * m + 8 by omega] at r7
  push_cast at g1 g2 g3 g4 r0 r1 r2 r3 r4 r5 r6 r7
  have key := collapse_algebra (m : ℚ) ((m : ℚ) + 8)
    (((2 * m + 8).choose (m + 4) : ℕ) : ℚ) (((2 * m + 8).choose (m + 5) : ℕ) : ℚ)
    (((2 * m + 8).choose (m + 6) : ℕ) : ℚ) (((2 * m + 8).choose (m + 7) : ℕ) : ℚ)
    (((2 * m + 16).choose (m + 8) : ℕ) : ℚ) (((2 * m + 15).choose (m + 8) : ℕ) : ℚ)
    (((2 * m + 14).choose (m + 8) : ℕ) : ℚ) (((2 * m + 13).choose (m + 8) : ℕ) : ℚ)
    (((2 * m + 12).choose (m + 8) : ℕ) : ℚ) (((2 * m + 11).choose (m + 8) : ℕ) : ℚ)
    (((2 * m + 10).choose (m + 8) : ℕ) : ℚ) (((2 * m + 9).choose (m + 8) : ℕ) : ℚ)
    (((2 * m + 8).choose (m + 8) : ℕ) : ℚ) (Nat.cast_nonneg m) rfl
    (by linear_combination g1) (by linear_combination g2) (by linear_combination g3)
    (by linear_combination g4) (by linear_combination r7) (by linear_combination r6)
    (by linear_combination r5) (by linear_combination r4) (by linear_combination r3)
    (by linear_combination r2) (by linear_combination r1) (by linear_combination r0)
  linear_combination key


/-- **The depth-2 collapse** for every `n ≥ 4`:
`(n − 3)·Σ_{k ≤ n} g(k)²·W(k)·C(n,k)² = 2(n − 2)³(n − 5)·Q(n)·C(2n − 8, n − 4)`. -/
theorem depthTwo_sum_collapse (n : ℕ) (hn : 4 ≤ n) :
    ((n : ℤ) - 3) * ∑ k ∈ range (n + 1), depthTwoTerm n k
      = 2 * ((n : ℤ) - 2) ^ 3 * ((n : ℤ) - 5) * sexticZ (n : ℤ)
        * (((2 * n - 8).choose (n - 4) : ℕ) : ℤ) := by
  rcases Nat.lt_or_ge n 8 with hlt | hge
  · interval_cases n <;>
      simp [Finset.sum_range_succ, depthTwoTerm, depthTwoG, depthTwoW, sexticZ, Nat.choose]
  · obtain ⟨m, rfl⟩ : ∃ m, n = m + 8 := ⟨n - 8, by omega⟩
    exact depthTwo_sum_collapse_add_eight m

end QOU.BraidsAndKnots.DepthTwoBinomialMoments
