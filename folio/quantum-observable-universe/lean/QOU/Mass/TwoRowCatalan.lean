import Mathlib.Combinatorics.Enumerative.Catalan
import Mathlib.Data.Nat.Choose.Vandermonde
import Mathlib.Data.Nat.Choose.Central
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.LinearCombination

/-!
# Two-row Hecke blocks: the Catalan count and nonvanishing quantum integers

Counting core of Step 4 of
`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`.

* `twoRow_sum_sq_eq_catalan`: with `f n k = C(n,k) − C(n,k−1)` — by the hook
  formula the number of standard Young tableaux of the two-row shape
  `(n − k, k)` (not proved here) — the sum of `(f n k)²` over the two-row
  shapes `0 ≤ k ≤ n/2` is the Catalan number `C_n`. Read through Wedderburn,
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

/-- The shifted term equals `C(n, n+1−k)` on `0 ≤ k ≤ n+1`. -/
lemma shift_eq (n k : ℕ) (hk : k ≤ n + 1) :
    (if k = 0 then (0 : ℤ) else (n.choose (k - 1) : ℤ)) = (n.choose (n + 1 - k) : ℤ) := by
  rcases k with _ | j
  · simp
  · simp only [Nat.succ_ne_zero, if_false, Nat.add_sub_cancel]
    have hj : j ≤ n := by omega
    have : n + 1 - (j + 1) = n - j := by omega
    rw [this, Nat.choose_symm hj]

/-- Reflection antisymmetry `f n (n+1−k) = −f n k` for `k ≤ n+1`. -/
lemma f_reflect (n k : ℕ) (hk : k ≤ n + 1) : f n (n + 1 - k) = - f n k := by
  have h1 := shift_eq n k hk
  have h2 := shift_eq n (n + 1 - k) (by omega)
  have h3 : n + 1 - (n + 1 - k) = k := by omega
  unfold f
  rw [h1, h2, h3]
  ring

lemma f_sq_reflect (n k : ℕ) (hk : k ≤ n + 1) : f n (n + 1 - k) ^ 2 = f n k ^ 2 := by
  rw [f_reflect n k hk]; ring

/-- Vandermonde in range form: `C(2n, n+d) = Σ_{k<n+d+1} C(n,k)·C(n,n+d−k)`. -/
lemma vandermonde_range (n d : ℕ) :
    ((n + n).choose (n + d) : ℤ) =
      ∑ k ∈ range (n + d + 1), (n.choose k : ℤ) * (n.choose (n + d - k) : ℤ) := by
  rw [Nat.add_choose_eq, Finset.Nat.sum_antidiagonal_eq_sum_range_succ_mk]
  push_cast
  rfl

lemma sum_choose_sq (n : ℕ) :
    ∑ k ∈ range (n + 2), ((n.choose k : ℤ)) ^ 2 = ((n + n).choose n : ℤ) := by
  have h := vandermonde_range n 0
  simp only [Nat.add_zero] at h
  rw [h, Finset.sum_range_succ (n := n + 1)]
  simp only [Nat.choose_succ_self, Nat.cast_zero, zero_pow two_ne_zero, add_zero]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hk' : k ≤ n := Nat.lt_succ_iff.mp (Finset.mem_range.mp hk)
  rw [Nat.choose_symm hk']; ring

lemma sum_shift_sq (n : ℕ) :
    ∑ k ∈ range (n + 2), (if k = 0 then (0 : ℤ) else (n.choose (k - 1) : ℤ)) ^ 2
      = ((n + n).choose n : ℤ) := by
  rw [Finset.sum_range_succ', ← sum_choose_sq n, Finset.sum_range_succ (n := n + 1)]
  simp

lemma sum_cross (n : ℕ) :
    ∑ k ∈ range (n + 2),
        (n.choose k : ℤ) * (if k = 0 then (0 : ℤ) else (n.choose (k - 1) : ℤ))
      = ((n + n).choose (n + 1) : ℤ) := by
  rw [vandermonde_range n 1]
  refine Finset.sum_congr rfl fun k hk => ?_
  rw [shift_eq n k (Nat.lt_succ_iff.mp (Finset.mem_range.mp hk))]

/-- The full sum over `0 ≤ k ≤ n+1` is `2·C(2n,n) − 2·C(2n,n+1)`. -/
lemma full_sum (n : ℕ) :
    ∑ k ∈ range (n + 2), f n k ^ 2
      = 2 * ((n + n).choose n : ℤ) - 2 * ((n + n).choose (n + 1) : ℤ) := by
  have e : ∀ k, f n k ^ 2 = (n.choose k : ℤ) ^ 2
      + (if k = 0 then (0 : ℤ) else (n.choose (k - 1) : ℤ)) ^ 2
      - 2 * ((n.choose k : ℤ) * (if k = 0 then (0 : ℤ) else (n.choose (k - 1) : ℤ))) := by
    intro k; unfold f; ring
  simp only [e, Finset.sum_sub_distrib, Finset.sum_add_distrib, ← Finset.mul_sum,
    sum_choose_sq, sum_shift_sq, sum_cross]
  ring

/-- `C(2n,n) − C(2n,n+1) = catalan n`. -/
lemma catalan_eq_diff (n : ℕ) :
    ((n + n).choose n : ℤ) - ((n + n).choose (n + 1) : ℤ) = (catalan n : ℤ) := by
  have hc : ((n + 1 : ℕ) : ℤ) * (catalan n : ℤ) = ((n + n).choose n : ℤ) := by
    have := succ_mul_catalan_eq_centralBinom n
    rw [Nat.centralBinom_eq_two_mul_choose, two_mul] at this
    exact_mod_cast this
  have hs : ((n + n).choose (n + 1) : ℤ) * ((n : ℤ) + 1) = ((n + n).choose n : ℤ) * (n : ℤ) := by
    have := Nat.choose_succ_right_eq (n + n) n
    rw [show n + n - n = n by omega] at this
    exact_mod_cast this
  have hpos : ((n : ℤ) + 1) ≠ 0 := by positivity
  apply mul_left_cancel₀ hpos
  push_cast at hc
  linear_combination -hs - hc

/-- Pairing `k ↔ n+1−k`: the full sum is twice the sum over two-row shapes. -/
lemma full_eq_two_half (n : ℕ) :
    ∑ k ∈ range (n + 2), f n k ^ 2 = 2 * ∑ k ∈ range (n / 2 + 1), f n k ^ 2 := by
  set m := n / 2 + 1 with hm
  set r := n + 2 - m with hr
  have hsplit : n + 2 = m + r := by omega
  rw [hsplit, Finset.sum_range_add]
  -- reflect the upper half
  have hup : ∑ x ∈ range r, f n (m + x) ^ 2 = ∑ x ∈ range r, f n x ^ 2 := by
    rw [← Finset.sum_range_reflect (fun x => f n x ^ 2) r]
    refine Finset.sum_congr rfl fun x hx => ?_
    have hx' := Finset.mem_range.mp hx
    have h1 : r - 1 - x = n + 1 - (m + x) := by omega
    rw [h1, f_sq_reflect n (m + x) (by omega)]
  rw [hup]
  -- `r = m` (n even) or `r = m + 1` with a vanishing middle term (n odd)
  rcases Nat.even_or_odd n with ⟨t, ht⟩ | ⟨t, ht⟩
  · have : r = m := by omega
    rw [this]; ring
  · have hrm : r = m + 1 := by omega
    have hmid : f n m = 0 := by
      have := f_reflect n m (by omega)
      rw [show n + 1 - m = m by omega] at this
      linarith
    rw [hrm, Finset.sum_range_succ (fun x => f n x ^ 2) m, hmid]; ring

/-- **Two-row Catalan identity.** `Σ_{0 ≤ k ≤ n/2} (C(n,k) − C(n,k−1))² = C_n`. -/
theorem twoRow_sum_sq_eq_catalan (n : ℕ) :
    ∑ k ∈ Finset.range (n / 2 + 1), (f n k) ^ 2 = (catalan n : ℤ) := by
  have h := full_eq_two_half n
  rw [full_sum] at h
  have hc := catalan_eq_diff n
  linarith

/-! ### Quantum integers -/

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

end QOU.Mass.TwoRowCatalan
