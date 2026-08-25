import Mathlib.NumberTheory.ZetaValues

/-!
# The alternating `ζ(2)` — a Mathlib gap, and the Landen base value

Mathlib has `hasSum_zeta_two : Σ 1/n² = π²/6` but **no alternating analogue**.
Route 33 named `Li₂(−1) = −π²/12` as the one value standing between
`hasDerivAt_landenCombo` (the Landen leg's analytic core, proved) and Landen
itself. This file supplies it.

## The derivation

Split `Σ 1/(n+1)²` into even and odd index:

* odd index gives `Σ 1/(2k+2)² = ¼·Σ 1/(k+1)² = π²/24`;
* so even index gives `Σ 1/(2k+1)² = π²/6 − π²/24 = π²/8`.

The alternating series has the **same** two pieces with the even one negated,
so it sums to `−π²/8 + π²/24 = −π²/12`.

The indexing is the corpus's: `LiTwo x = Σ' x^{k+1}/(k+1)²`, so `LiTwo(−1)` is
literally `Σ' (−1)^{k+1}/(k+1)²` and the statement below matches it termwise.

This file imports **only Mathlib**, so it can go upstream unchanged — the same
discipline `ComplexDilogarithm.lean` follows.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.MathlibExt

open Real

private noncomputable def g (n : ℕ) : ℝ := (1 : ℝ) / ((n : ℝ) + 1) ^ 2

private theorem hg : HasSum g (π ^ 2 / 6) := by
  show HasSum (fun n : ℕ => (1 : ℝ) / ((n : ℝ) + 1) ^ 2) (π ^ 2 / 6)
  have hz := hasSum_zeta_two
  have h := (hasSum_nat_add_iff (f := fun n : ℕ => (1 : ℝ) / (n : ℝ) ^ 2) 1).mpr
    (by simpa using hz)
  simpa [one_div, Nat.cast_add, Nat.cast_one] using h

/-- `Σ 1/(n+1)² = π²/6`, in shifted indexing — the summability workhorse. -/
theorem hasSum_one_div_succ_sq :
    HasSum (fun n : ℕ => (1 : ℝ) / ((n : ℝ) + 1) ^ 2) (π ^ 2 / 6) := hg

theorem summable_one_div_succ_sq :
    Summable (fun n : ℕ => (1 : ℝ) / ((n : ℝ) + 1) ^ 2) := hasSum_one_div_succ_sq.summable

private theorem hgodd : HasSum (fun k : ℕ => g (2 * k + 1)) (π ^ 2 / 24) := by
  have h := hg.mul_left (1 / 4)
  have hfun : (fun k : ℕ => g (2 * k + 1)) = fun k : ℕ => (1 : ℝ) / 4 * g k := by
    funext k
    have hk : ((k : ℝ)) + 1 ≠ 0 := by positivity
    simp only [g, Nat.cast_add, Nat.cast_mul, Nat.cast_ofNat, Nat.cast_one]
    field_simp
    ring
  rw [hfun]
  convert h using 1
  ring

private theorem hgeven_sum : ∑' k : ℕ, g (2 * k) = π ^ 2 / 8 := by
  have hS : Summable (fun k : ℕ => g (2 * k)) :=
    hg.summable.comp_injective (mul_right_injective₀ (two_ne_zero' ℕ))
  have hcomb := hS.hasSum.even_add_odd hgodd
  have := hg.unique hcomb
  linarith

/-- **The alternating `ζ(2)`**: `Σ_{n≥1} (−1)^n/n² = −π²/12`, in the indexing the
corpus's `LiTwo` uses. Mathlib has `hasSum_zeta_two` but no alternating analogue. -/
theorem hasSum_alternating_zeta_two :
    HasSum (fun n : ℕ => (-1 : ℝ) ^ (n + 1) / ((n : ℝ) + 1) ^ 2) (-(π ^ 2 / 12)) := by
  set a : ℕ → ℝ := fun n => (-1 : ℝ) ^ (n + 1) / ((n : ℝ) + 1) ^ 2 with ha
  have hS : Summable (fun k : ℕ => g (2 * k)) :=
    hg.summable.comp_injective (mul_right_injective₀ (two_ne_zero' ℕ))
  have haeven : HasSum (fun k : ℕ => a (2 * k)) (-(π ^ 2 / 8)) := by
    have h := hS.hasSum.neg
    rw [hgeven_sum] at h
    refine h.congr_fun ?_
    intro k
    simp only [ha, g]
    rw [Odd.neg_one_pow ⟨k, by ring⟩]
    ring
  have haodd : HasSum (fun k : ℕ => a (2 * k + 1)) (π ^ 2 / 24) := by
    refine hgodd.congr_fun ?_
    intro k
    simp only [ha, g]
    rw [Even.neg_one_pow ⟨k + 1, by ring⟩]
  have h := haeven.even_add_odd haodd
  convert h using 1
  ring

end QOU.MathlibExt
