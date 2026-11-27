import QOU.Core.TarskiSign
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.IntervalCases

/-!
# QOU.Core.TarskiSignKashaev — the figure-eight Kashaev value at `N = 5, 7`, signs decided

Bean `qou-rc4t`, worked instances of `QOU.Core.TarskiSign`, feeding bean
`qou-pc7n` (per-`N` certificates).

## The object

For `q` a primitive `N`-th root of unity the Kashaev invariant of the
figure-eight knot is `⟨4₁⟩_N = ∑_{k<N} (q;q)_k (q⁻¹;q⁻¹)_k`. Each factor is
`(1 - q^j)(1 - q^{-j}) = 2 - (q^j + q^{-j})`, and `q^j + q^{-j}` is the
Dickson polynomial `C_j(c)` in `c = q + q⁻¹` (`dicksonC`, proved in
`dicksonC_add_inv`). So `⟨4₁⟩_N` is the value at `c` of an integer polynomial,
`kashaevFigureEight c N`, defined over any commutative ring. It lies in
`ℚ(c) = ℚ(ζ_N)⁺`.

## The embedding is a sign prefix

The choice `ζ_N = e^{2πi/N}` is the choice of the largest root `c` of the
minimal polynomial `Ψ_N` of `ζ_N + ζ_N⁻¹`. For `N = 5` (`Ψ₅ = c² + c - 1`,
roots `≈ 0.618, -1.618`) and `N = 7` (`Ψ₇ = c³ + c² - 2c - 1`, roots
`≈ 1.247, -0.445, -1.802`) only one root is positive, so the embedding is the
single sign `+`: the hypothesis `0 < c`. No cosine and no `π` enter.

## Results (any ordered field `K`, no axiom, no `sorry`)

* `kashaevFigureEight_five`: `⟨4₁⟩₅ = 48 + 4c` in `ℤ[c]/(Ψ₅)`.
* `kashaevFigureEight_seven`: `⟨4₁⟩₇ = 103 + 25c + 11c²` in `ℤ[c]/(Ψ₇)`.
* `signPrefix_five`: the first four signs of `c₅` are `+ - + -`, each decided
  by one certificate, so `1/2 < c₅ ≤ 3/4` and `50 < ⟨4₁⟩₅ ≤ 51`.
* `signPrefix_seven`: the first four signs of `c₇` are `+ + - -`, so
  `1 < c₇ ≤ 3/2` and `139 < ⟨4₁⟩₇`.
* `kashaev_five_lt_seven`: `⟨4₁⟩₅ < ⟨4₁⟩₇`, for any two ordered fields holding
  the two roots.

Decision depths (the birthday of the deciding Gonshor window): the bracket
`50 < ⟨4₁⟩₅` needs depth 3; `⟨4₁⟩₅ ≤ 51` needs depth 4; `139 < ⟨4₁⟩₇` needs
depth 2. They are small because these claims are coarse; a sharper claim
costs one sign per halving of the window.

The values `≈ 50.47` and `≈ 151.28` are not used in any proof.

No empirical value enters this file.
-/

namespace QOU.Core.TarskiSignKashaev

open Finset QOU.Core.TarskiSign QOU.AppendixSurreals

/-! ### The Dickson polynomials and the Kashaev sum, over a commutative ring -/

section Ring

variable {R : Type*} [CommRing R]

/-- `C_j(c)`: the Dickson polynomial with `C_j(q + q⁻¹) = q^j + q^{-j}`. -/
def dicksonC (c : R) : ℕ → R
  | 0 => 2
  | 1 => c
  | j + 2 => c * dicksonC c (j + 1) - dicksonC c j

@[simp] theorem dicksonC_zero (c : R) : dicksonC c 0 = 2 := rfl
@[simp] theorem dicksonC_one (c : R) : dicksonC c 1 = c := rfl
theorem dicksonC_add_two (c : R) (j : ℕ) :
    dicksonC c (j + 2) = c * dicksonC c (j + 1) - dicksonC c j := rfl

/-- The figure-eight Kashaev sum `∑_{k<N} ∏_{j=1}^{k} (2 - C_j(c))`. -/
def kashaevFigureEight (c : R) (N : ℕ) : R :=
  ∑ k ∈ range N, ∏ j ∈ range k, (2 - dicksonC c (j + 1))

end Ring

/-- The Dickson identity `C_j(q + q⁻¹) = q^j + q^{-j}`. -/
theorem dicksonC_add_inv {F : Type*} [Field F] {q : F} (hq : q ≠ 0) (j : ℕ) :
    dicksonC (q + q⁻¹) j = q ^ j + q⁻¹ ^ j := by
  induction j using Nat.strong_induction_on with
  | _ j ih =>
    match j, ih with
    | 0, _ => norm_num [dicksonC]
    | 1, _ => simp [dicksonC]
    | j + 2, ih =>
      rw [dicksonC_add_two, ih (j + 1) (by omega), ih j (by omega)]
      have h : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
      linear_combination (q ^ j + q⁻¹ ^ j) * h

/-- Each Kashaev factor is a norm: `(1 - q^j)(1 - q^{-j}) = 2 - C_j(q + q⁻¹)`.
So `kashaevFigureEight (q + q⁻¹) N = ∑_{k<N} (q;q)_k (q⁻¹;q⁻¹)_k`. -/
theorem kashaev_factor {F : Type*} [Field F] {q : F} (hq : q ≠ 0) (j : ℕ) :
    (1 - q ^ j) * (1 - q⁻¹ ^ j) = 2 - dicksonC (q + q⁻¹) j := by
  rw [dicksonC_add_inv hq]
  have : q ^ j * q⁻¹ ^ j = 1 := by rw [← mul_pow, mul_inv_cancel₀ hq, one_pow]
  linear_combination this

/-! ### Exact values modulo the minimal polynomial -/

section Values

variable {R : Type*} [CommRing R]

/-- `⟨4₁⟩₅ = 48 + 4c` modulo `Ψ₅ = c² + c - 1`. -/
theorem kashaevFigureEight_five (c : R) (hc : c ^ 2 + c - 1 = 0) :
    kashaevFigureEight c 5 = 48 + 4 * c := by
  simp only [kashaevFigureEight, sum_range_succ, prod_range_succ, sum_range_zero,
    prod_range_zero, dicksonC_add_two, dicksonC_one, dicksonC_zero, zero_add]
  linear_combination
    (c ^ 8 - 3 * c ^ 7 - 7 * c ^ 6 + 24 * c ^ 5 + 12 * c ^ 4 - 50 * c ^ 3
      - 11 * c ^ 2 + 14 * c + 21) * hc

/-- `⟨4₁⟩₇ = 103 + 25c + 11c²` modulo `Ψ₇ = c³ + c² - 2c - 1`. -/
theorem kashaevFigureEight_seven (c : R) (hc : c ^ 3 + c ^ 2 - 2 * c - 1 = 0) :
    kashaevFigureEight c 7 = 103 + 25 * c + 11 * c ^ 2 := by
  simp only [kashaevFigureEight, sum_range_succ, prod_range_succ, sum_range_zero,
    prod_range_zero, dicksonC_add_two, dicksonC_one, dicksonC_zero, zero_add]
  linear_combination
    (c ^ 18 - 3 * c ^ 17 - 17 * c ^ 16 + 54 * c ^ 15 + 118 * c ^ 14 - 401 * c ^ 13
      - 433 * c ^ 12 + 1591 * c ^ 11 + 908 * c ^ 10 - 3657 * c ^ 9 - 1071 * c ^ 8
      + 4948 * c ^ 7 + 546 * c ^ 6 - 3822 * c ^ 5 + 182 * c ^ 4 + 1491 * c ^ 3
      - 323 * c ^ 2 - 138 * c + 76) * hc

end Values

/-! ### Signs decided by certificates -/

section Signs

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- A coefficient list read as a function `ℕ → K` (zero past the end). -/
def coeffs (l : List K) : ℕ → K := fun i => l.getD i 0

/-! #### `N = 5`, `Ψ₅ = c² + c - 1` -/

/-- Sign 2 of `c₅`: `c ≤ 1`. Certificate: `Ψ₅(1 + t) = 1 + 3t + t²`. -/
theorem five_le_one {c : K} (hc : c ^ 2 + c - 1 = 0) : ¬ (1 : K) < c := by
  refine not_lt.mpr (lt_of_excluded_up (p := fun x => x ^ 2 + x - 1) hc
    (fun x hx => ?_)).le
  have h := taylorUp_pos (m := (1 : K)) (n := 2) (c := coeffs [1, 3, 1]) hx
    (by intro i hi; interval_cases i <;> norm_num [coeffs]) (by norm_num [coeffs])
  have e : taylorUp (1 : K) 2 (coeffs [1, 3, 1]) x = x ^ 2 + x - 1 := by
    simp [taylorUp, coeffs, sum_range_succ]; ring
  rw [e] at h; exact h.ne'

/-- Sign 3 of `c₅`: `1/2 < c`. Certificate: `-Ψ₅ = 4(1/2 - x)² + 6x(1/2 - x) + x²`
on `[0, 1/2]`. -/
theorem five_gt_half {c : K} (hc : c ^ 2 + c - 1 = 0) (h0 : 0 < c) : (1 / 2 : K) < c := by
  refine lt_of_excluded' (p := fun x => x ^ 2 + x - 1) (a := 0) hc h0.le
    (fun x hx0 hx1 => ?_)
  have h := bernstein_pos (a := (0 : K)) (b := 1 / 2) (n := 2) (c := coeffs [4, 6, 1])
    (by norm_num) hx0 hx1 (by intro i hi; interval_cases i <;> norm_num [coeffs])
    (by norm_num [coeffs]) (by norm_num [coeffs])
  have e : bernstein (0 : K) (1 / 2) 2 (coeffs [4, 6, 1]) x = -(x ^ 2 + x - 1) := by
    simp [bernstein, coeffs, sum_range_succ]; ring
  rw [e] at h
  intro h'; simp only at h'; linarith

/-- Sign 4 of `c₅`: `c ≤ 3/4`. Certificate: `Ψ₅ = 5(1 - x)² + 20(x - 3/4)(1 - x)
+ 16(x - 3/4)²` on `[3/4, 1]`. -/
theorem five_le_three_quarters {c : K} (hc : c ^ 2 + c - 1 = 0) :
    ¬ (3 / 4 : K) < c := by
  have h1 : c ≤ 1 := not_lt.mp (five_le_one hc)
  refine not_lt.mpr (lt_of_excluded (p := fun x => x ^ 2 + x - 1) (b := 1) hc h1
    (fun x hx0 hx1 => ?_)).le
  have h := bernstein_pos (a := (3 / 4 : K)) (b := 1) (n := 2) (c := coeffs [5, 20, 16])
    (by norm_num) hx0 hx1 (by intro i hi; interval_cases i <;> norm_num [coeffs])
    (by norm_num [coeffs]) (by norm_num [coeffs])
  have e : bernstein (3 / 4 : K) 1 2 (coeffs [5, 20, 16]) x = x ^ 2 + x - 1 := by
    simp [bernstein, coeffs, sum_range_succ]; ring
  rw [e] at h; exact h.ne'

/-- **The sign expansion of `c₅` begins `+ - + -`.** The embedding is the first
sign; each later sign is one certificate. -/
theorem signPrefix_five {c : K} (hc : c ^ 2 + c - 1 = 0) (h0 : 0 < c) :
    signPrefix c 4 = [Sign.plus, Sign.minus, Sign.plus, Sign.minus] := by
  have h1 := five_le_one hc
  have h2 := five_gt_half hc h0
  have h3 := five_le_three_quarters hc
  simp [signPrefix, follow, signAt, GonshorState.step, GonshorState.init, h0, h1]
  norm_num [h2, h3]
  exact not_lt.mp h3

/-- The Gonshor window after four signs: `1/2 < c₅ ≤ 3/4`, so
`50 < ⟨4₁⟩₅ ≤ 51`. -/
theorem kashaev_five_bracket {c : K} (hc : c ^ 2 + c - 1 = 0) (h0 : 0 < c) :
    50 < kashaevFigureEight c 5 ∧ kashaevFigureEight c 5 ≤ 51 := by
  rw [kashaevFigureEight_five c hc]
  have h2 := five_gt_half hc h0
  have h3 := not_lt.mp (five_le_three_quarters hc)
  constructor <;> linarith

/-- **`⟨4₁⟩₅`'s root is located with no axiom.** After two signs the window
`(0, 1]` has both bounds, so in an Archimedean field the Gonshor cut of `c₅`
is located (`TarskiSign.gonshorCut_located`): `[Coev E]` is not used. -/
theorem five_located [Archimedean K] {c : K} (hc : c ^ 2 + c - 1 = 0) (h0 : 0 < c) :
    (gonshorCut c).Located := by
  have h1 := five_le_one hc
  refine gonshorCut_located c (n := 2) ?_ ?_ <;>
    simp [follow, signAt, GonshorState.step, GonshorState.init, h0, h1]

/-! #### `N = 7`, `Ψ₇ = c³ + c² - 2c - 1` -/

/-- Sign 2 of `c₇`: `1 < c`. Certificate: `-Ψ₇ = (1 - x)³ + 5x(1 - x)²
+ 6x²(1 - x) + x³` on `[0, 1]`. -/
theorem seven_gt_one {c : K} (hc : c ^ 3 + c ^ 2 - 2 * c - 1 = 0) (h0 : 0 < c) :
    (1 : K) < c := by
  refine lt_of_excluded' (p := fun x => x ^ 3 + x ^ 2 - 2 * x - 1) (a := 0) hc h0.le
    (fun x hx0 hx1 => ?_)
  have h := bernstein_pos (a := (0 : K)) (b := 1) (n := 3) (c := coeffs [1, 5, 6, 1])
    (by norm_num) hx0 hx1 (by intro i hi; interval_cases i <;> norm_num [coeffs])
    (by norm_num [coeffs]) (by norm_num [coeffs])
  have e : bernstein (0 : K) 1 3 (coeffs [1, 5, 6, 1]) x
      = -(x ^ 3 + x ^ 2 - 2 * x - 1) := by
    simp [bernstein, coeffs, sum_range_succ]; ring
  rw [e] at h
  intro h'; simp only at h'; linarith

/-- Sign 3 of `c₇`: `c ≤ 2`. Certificate: `Ψ₇(2 + t) = 7 + 14t + 7t² + t³`. -/
theorem seven_le_two {c : K} (hc : c ^ 3 + c ^ 2 - 2 * c - 1 = 0) : ¬ (2 : K) < c := by
  refine not_lt.mpr (lt_of_excluded_up (p := fun x => x ^ 3 + x ^ 2 - 2 * x - 1) hc
    (fun x hx => ?_)).le
  have h := taylorUp_pos (m := (2 : K)) (n := 3) (c := coeffs [7, 14, 7, 1]) hx
    (by intro i hi; interval_cases i <;> norm_num [coeffs]) (by norm_num [coeffs])
  have e : taylorUp (2 : K) 3 (coeffs [7, 14, 7, 1]) x = x ^ 3 + x ^ 2 - 2 * x - 1 := by
    simp [taylorUp, coeffs, sum_range_succ]; ring
  rw [e] at h; exact h.ne'

/-- Sign 4 of `c₇`: `c ≤ 3/2`. Certificate on `[3/2, 2]` with Bernstein
coefficients `13, 70, 112, 56`. -/
theorem seven_le_three_halves {c : K} (hc : c ^ 3 + c ^ 2 - 2 * c - 1 = 0) :
    ¬ (3 / 2 : K) < c := by
  have h2 : c ≤ 2 := not_lt.mp (seven_le_two hc)
  refine not_lt.mpr (lt_of_excluded (p := fun x => x ^ 3 + x ^ 2 - 2 * x - 1) (b := 2)
    hc h2 (fun x hx0 hx1 => ?_)).le
  have h := bernstein_pos (a := (3 / 2 : K)) (b := 2) (n := 3)
    (c := coeffs [13, 70, 112, 56])
    (by norm_num) hx0 hx1 (by intro i hi; interval_cases i <;> norm_num [coeffs])
    (by norm_num [coeffs]) (by norm_num [coeffs])
  have e : bernstein (3 / 2 : K) 2 3 (coeffs [13, 70, 112, 56]) x
      = x ^ 3 + x ^ 2 - 2 * x - 1 := by
    simp [bernstein, coeffs, sum_range_succ]; ring
  rw [e] at h; exact h.ne'

/-- **The sign expansion of `c₇` begins `+ + - -`.** -/
theorem signPrefix_seven {c : K} (hc : c ^ 3 + c ^ 2 - 2 * c - 1 = 0) (h0 : 0 < c) :
    signPrefix c 4 = [Sign.plus, Sign.plus, Sign.minus, Sign.minus] := by
  have h1 := seven_gt_one hc h0
  have h2 := seven_le_two hc
  have h3 := seven_le_three_halves hc
  simp [signPrefix, follow, signAt, GonshorState.step, GonshorState.init, h0, h1]
  norm_num [h2, h3]
  exact ⟨not_lt.mp h2, not_lt.mp h3⟩

/-- The window after two signs, `1 < c₇`, already gives `139 < ⟨4₁⟩₇`; after
four signs `⟨4₁⟩₇ ≤ 165¼`. -/
theorem kashaev_seven_bracket {c : K} (hc : c ^ 3 + c ^ 2 - 2 * c - 1 = 0) (h0 : 0 < c) :
    139 < kashaevFigureEight c 7 ∧ kashaevFigureEight c 7 ≤ 661 / 4 := by
  rw [kashaevFigureEight_seven c hc]
  have h1 := seven_gt_one hc h0
  have h3 := not_lt.mp (seven_le_three_halves hc)
  constructor <;> nlinarith

/-- **A finite-`N` comparison, decided with no axiom:** `⟨4₁⟩₅ < ⟨4₁⟩₇`. The
two values live in different fields `ℚ(ζ₅)⁺` and `ℚ(ζ₇)⁺`; the comparison goes
through the rational separator `51 < 139` read off their Gonshor windows. -/
theorem kashaev_five_lt_seven {c₅ c₇ : K}
    (h₅ : c₅ ^ 2 + c₅ - 1 = 0) (h₅0 : 0 < c₅)
    (h₇ : c₇ ^ 3 + c₇ ^ 2 - 2 * c₇ - 1 = 0) (h₇0 : 0 < c₇) :
    kashaevFigureEight c₅ 5 < kashaevFigureEight c₇ 7 := by
  have := (kashaev_five_bracket h₅ h₅0).2
  have := (kashaev_seven_bracket h₇ h₇0).1
  linarith

end Signs

end QOU.Core.TarskiSignKashaev
