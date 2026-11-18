import QOU.Mathlib.BallotNumbers
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination

/-!
# Two-row Hecke blocks: the Catalan count and nonvanishing quantum integers

Counting core of Step 4 of
`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`.

* `twoRow_sum_sq_eq_catalan`: with `f n k = C(n,k) − C(n,k−1)` — the number of standard Young tableaux of the two-row shape `(n − k, k)`
  (`QOU.SchurWeyl.TwoRowSYTBallot.numSYT_twoRow_eq_ballot`) — the sum of `(f n k)²` over the two-row
  shapes `0 ≤ k ≤ n/2` is the Catalan number `C_n` (a restatement of
  `QOU.Mathlib.ballot_sq_sum_catalan`, which proved it first). Read through Wedderburn,
  the two-row blocks of the Hecke algebra `H_n(q)` have total dimension
  `C_n = dim End_{gl₂}(V^{⊗n})`.
* `qint_num_ne_zero` / `qint_ne_zero`: over any field, if `q ≠ 0` and
  `q^(2m) ≠ 1` then the numerator `q^m − q⁻¹^m` of the quantum integer
  `[m]_q` is nonzero, and so is `[m]_q` itself when also `q² ≠ 1`. The quantum
  trace of a two-row minimal idempotent is a product of such quantum integers,
  hence nonzero under these hypotheses.
-/

namespace QOU.Mass.TwoRowCatalan

open Finset

/-- `f n k = C(n,k) − C(n,k−1)` (with `C(n,−1) = 0`): the number of standard
Young tableaux of the two-row shape `(n − k, k)`, by the hook formula. -/
def f (n k : ℕ) : ℤ :=
  (n.choose k : ℤ) - (if k = 0 then 0 else (n.choose (k - 1) : ℤ))


/-- `f` is the corpus ballot number `QOU.Mathlib.ballot`. -/
lemma f_eq_ballot (n k : ℕ) : f n k = QOU.Mathlib.ballot n k := by
  cases k with
  | zero => simp [f]
  | succ j => simp [f, QOU.Mathlib.ballot_succ]

/-- **Two-row Catalan identity.** `Σ_{0 ≤ k ≤ n/2} (C(n,k) − C(n,k−1))² = C_n`.
A restatement of `QOU.Mathlib.ballot_sq_sum_catalan` (proved there first); the count
`f n k = #SYT(n−k, k)` is `QOU.SchurWeyl.TwoRowSYTBallot.numSYT_twoRow_eq_ballot`. -/
theorem twoRow_sum_sq_eq_catalan (n : ℕ) :
    ∑ k ∈ Finset.range (n / 2 + 1), (f n k) ^ 2 = (catalan n : ℤ) := by
  simp only [f_eq_ballot]
  exact QOU.Mathlib.ballot_sq_sum_catalan n

/-- The quantum integer `[m]_q = (q^m − q⁻¹^m)/(q − q⁻¹)`. -/
def qint {K : Type*} [Field K] (q : K) (m : ℕ) : K :=
  (q ^ m - q⁻¹ ^ m) / (q - q⁻¹)

/-- The numerator of `[m]_q` is nonzero when `q ≠ 0` and `q^(2m) ≠ 1`. -/
theorem qint_num_ne_zero {K : Type*} [Field K] {q : K} (hq : q ≠ 0) {m : ℕ}
    (hm : 1 ≤ m) (h2m : q ^ (2 * m) ≠ 1) : q ^ m - q⁻¹ ^ m ≠ 0 := by
  have _ := hm
  intro h
  apply h2m
  have e : q ^ m = q⁻¹ ^ m := sub_eq_zero.mp h
  calc q ^ (2 * m) = q ^ m * q ^ m := by rw [two_mul, pow_add]
    _ = q ⁻¹ ^ m * q ^ m := by rw [← e]
    _ = 1 := by rw [← mul_pow, inv_mul_cancel₀ hq, one_pow]

/-- `[m]_q ≠ 0` when `q ≠ 0`, `q² ≠ 1` and `q^(2m) ≠ 1`. -/
theorem qint_ne_zero {K : Type*} [Field K] {q : K} (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    {m : ℕ} (hm : 1 ≤ m) (h2m : q ^ (2 * m) ≠ 1) : qint q m ≠ 0 := by
  unfold qint
  have hden : q ^ 1 - q⁻¹ ^ 1 ≠ 0 := qint_num_ne_zero hq le_rfl (by simpa using hq2)
  simp only [pow_one] at hden
  exact div_ne_zero (qint_num_ne_zero hq hm h2m) hden

/-- Vanishing difference form of `twoRow_sum_sq_eq_catalan`. -/
theorem twoRow_sum_sq_sub_catalan_eq_zero (n : ℕ) :
    (∑ k ∈ Finset.range (n / 2 + 1), (f n k) ^ 2) - (catalan n : ℤ) = 0 := by
  rw [twoRow_sum_sq_eq_catalan n, sub_self]

end QOU.Mass.TwoRowCatalan
