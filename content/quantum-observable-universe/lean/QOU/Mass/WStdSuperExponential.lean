import QOU.Mathlib.SkewBranchingTwoOne
import QOU.Mass.BindingGevreyHalf
import QOU.Mass.LevelSelectionLogarithmic

/-!
# `QOU.Mass.WStdSuperExponential` — `w_std` defined, and its growth made unconditional

`w_std(k) = ∑_{λ ⊢ k} W_λ · f^{λ/(2,1)}` (Plancherel weights `W_λ = (f^λ)²/k!`) is the
branched tower weight the level-selection argument turns on.  Three files reason about it —
`QOU/Mass/LevelSelectionLogarithmic.lean`, `QOU/Mass/CubeMomentLowerBound.lean`,
`QOU/Mass/BindingGevreyHalf.lean` — and until now **it had no Lean definition at all**: it
lived in docstrings, and every statement about it was either abstract in a function parameter
`w : ℕ → ℝ` or carried its two inputs as hypotheses.  `wStd` below is that definition.

## What is now unconditional

`BindingGevreyHalf.wstd_superexp_sq` proves `k!/(81·2^k) ≤ w_std(k)²` **from two hypotheses**
it explicitly declines to discharge — its docstring calls them "the open combinatorial core":

* **(A)** `∑_λ f^λ · f^{λ/(2,1)} = k!/3` — this is `branching_two_one`, proved in
  `QOU.Mathlib.SkewBranchingTwoOne` (bean `qou-b21r`).
* **(C)** `∑_λ f^{λ/(2,1)} ≤ I(k)` — `skew_le_straight` composed with
  `sum_dimSYT_eq_involution`, both already unconditional.

Both are now theorems, so `wStd_sq_lower` states the bound with **no hypotheses but `k ≥ 3`**.

## The class as stated cannot be instantiated, and that is a defect in the class

`LevelSelectionLogarithmic.TowerGeometricLowerBound w r c` demands `c · r^k ≤ w k` for
**every** `k`.  At the real `w_std` that is false, and not marginally: `w_std(k) = 0` for
`k < 3`, because no diagram of fewer than three cells contains `(2,1)` and `fDimSkew` guards
on containment.  `not_towerGeometricLowerBound_wStd` proves the refutation outright — it is a
structural exclusion with an invariant, not a failed search.

So the honest positive statement is a **threshold** bound, and `wStd_geometric_from_nine`
supplies one: `(1/9)·(√2)^k ≤ w_std(k)` for `k ≥ 9`, which is the class's `lower_bound` field
with `r = √2 > 1` and `c = 1/9 > 0` on that tail.  Everything downstream
(`no_linear_selection`, `no_superlinear_selection`) already works on a tail — they pick an `A`
from an `atTop` filter — so a threshold class would serve them unchanged.  Changing the class
is left to the author; this file does not edit it.

**The threshold 9 is an artifact of the crude step `4^k ≤ k!`, not of the mathematics.**
The true `w_std` is positive from `k = 3` on. Lowering the threshold needs the values
`w_std(3) … w_std(8)`, which is a finite computation this file does not do.

Base ring `ℝ` (archimedean: `√2`, real order) — the wall is crossed only in the last two
results; everything above `wStd_sq_lower` is `ℕ`-combinatorial.

## References

- [manuscript] bean `wsxl`, bean `qou-b21r`
-/

namespace QOU.Mass.WStd

open Finset QOU.Mathlib QOU.BraidKnot.YoungTableauStandard

/-- **The Plancherel-weighted branched tower weight**
`w_std(k) = (∑_{λ ⊢ k} (f^λ)² · f^{λ/(2,1)}) / k!`. -/
noncomputable def wStd (k : ℕ) : ℝ :=
  (∑ p : Nat.Partition k, (dimSYT p : ℝ) ^ 2 * (fDimSkew (partitionShape p) mu21 : ℝ))
    / (k.factorial : ℝ)

theorem wStd_nonneg (k : ℕ) : 0 ≤ wStd k := by
  refine div_nonneg (Finset.sum_nonneg (fun p _ => by positivity)) ?_
  exact_mod_cast Nat.zero_le _

/-! ### Vanishing below the shape's own size -/

/-- A diagram with fewer than three cells cannot contain `(2,1)`, so its skew count is `0`. -/
theorem fDimSkew_mu21_eq_zero_of_card_lt {Y : YoungDiagram} (h : Y.cells.card < 3) :
    fDimSkew Y mu21 = 0 :=
  fDimSkew_of_not_le (fun hle => by have := three_le_card hle; omega)

/-- **`w_std(k) = 0` for `k < 3`** — every term carries a `fDimSkew` that the containment
guard sends to zero. -/
theorem wStd_eq_zero_of_lt_three (k : ℕ) (hk : k < 3) : wStd k = 0 := by
  unfold wStd
  rw [Finset.sum_eq_zero (fun p _ => ?_), zero_div]
  rw [fDimSkew_mu21_eq_zero_of_card_lt
    (Y := partitionShape p) (by rw [partitionShape_card]; omega)]
  ring

/-! ### The unconditional square bound -/

/-- **`k!/(81·2^k) ≤ w_std(k)²`, unconditionally, for `k ≥ 3`.**

`BindingGevreyHalf.wstd_superexp_sq` supplies the inequality from two hypotheses its own
docstring calls "the open combinatorial core". Both are now theorems: (A) is
`branching_two_one_holds`, (C) is `skew_le_straight` composed with
`sum_dimSYT_eq_involution`. -/
theorem wStd_sq_lower (k : ℕ) (hk : 3 ≤ k) :
    (k.factorial : ℝ) / (81 * 2 ^ k) ≤ wStd k ^ 2 := by
  have hg : ∀ p ∈ (Finset.univ : Finset (Nat.Partition k)),
      (0:ℝ) ≤ (fDimSkew (partitionShape p) mu21 : ℝ) := fun _ _ => by positivity
  have hA : ∑ p : Nat.Partition k,
      (dimSYT p : ℝ) * (fDimSkew (partitionShape p) mu21 : ℝ) = (k.factorial : ℝ) / 3 := by
    have hc : (3:ℝ) * (∑ p : Nat.Partition k,
        (dimSYT p : ℝ) * (fDimSkew (partitionShape p) mu21 : ℝ)) = (k.factorial : ℝ) := by
      exact_mod_cast branching_two_one_holds k hk
    linarith
  have hC : ∑ p : Nat.Partition k, (fDimSkew (partitionShape p) mu21 : ℝ)
      ≤ (involutionNumber k : ℝ) := by
    have hn : (∑ p : Nat.Partition k, fDimSkew (partitionShape p) mu21) ≤ involutionNumber k := by
      rw [← sum_dimSYT_eq_involution k]; exact skew_le_straight k
    exact_mod_cast hn
  exact QOU.Mass.BindingGevreyHalf.wstd_superexp_sq Finset.univ _ _ k hg hA hC

/-! ### A geometric tail bound -/

/-- `4^k ≤ k!` for `k ≥ 9`.  (It is false at `k = 8`: `4^8 = 65536 > 40320 = 8!`.) -/
theorem four_pow_le_factorial : ∀ k : ℕ, 4 ^ (k + 9) ≤ (k + 9).factorial := by
  intro k
  induction k with
  | zero => decide
  | succ n ih =>
    calc 4 ^ (n + 1 + 9) = 4 * 4 ^ (n + 9) := by ring
      _ ≤ 4 * (n + 9).factorial := Nat.mul_le_mul_left _ ih
      _ ≤ (n + 9 + 1) * (n + 9).factorial := Nat.mul_le_mul_right _ (by omega)
      _ = (n + 1 + 9).factorial := (Nat.factorial_succ (n + 9)).symm

/-- **`2^k/81 ≤ w_std(k)²` for `k ≥ 9`** — `wStd_sq_lower` with `k!` bounded below by `4^k`. -/
theorem wStd_sq_ge_two_pow (k : ℕ) (hk : 9 ≤ k) : (2:ℝ) ^ k / 81 ≤ wStd k ^ 2 := by
  obtain ⟨d, rfl⟩ : ∃ d, k = d + 9 := ⟨k - 9, by omega⟩
  have hfac : (4:ℝ) ^ (d + 9) ≤ ((d + 9).factorial : ℝ) := by
    exact_mod_cast four_pow_le_factorial d
  have hlow := wStd_sq_lower (d + 9) (by omega)
  refine le_trans ?_ hlow
  have hp : (0:ℝ) < 2 ^ (d + 9) := by positivity
  have key : (2:ℝ) ^ (d + 9) / 81 = (4:ℝ) ^ (d + 9) / (81 * 2 ^ (d + 9)) := by
    rw [show (4:ℝ) ^ (d + 9) = 2 ^ (d + 9) * 2 ^ (d + 9) by rw [← mul_pow]; norm_num]
    field_simp
  rw [key]
  gcongr

/-- **The geometric tail bound: `(1/9)·(√2)^k ≤ w_std(k)` for `k ≥ 9`.**

This is exactly `TowerGeometricLowerBound.lower_bound` with `r = √2 > 1` and `c = 1/9 > 0`,
restricted to the tail — which is all `no_linear_selection` and `no_superlinear_selection`
consume, since both pick their `A` from an `atTop` filter. -/
theorem wStd_geometric_from_nine (k : ℕ) (hk : 9 ≤ k) :
    (1/9 : ℝ) * Real.sqrt 2 ^ k ≤ wStd k := by
  have h2 : (0:ℝ) ≤ Real.sqrt 2 := Real.sqrt_nonneg 2
  have hb : (0:ℝ) ≤ (1/9 : ℝ) * Real.sqrt 2 ^ k := by positivity
  have hsqrt : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hbsq : ((1/9 : ℝ) * Real.sqrt 2 ^ k) ^ 2 = (2:ℝ) ^ k / 81 := by
    rw [mul_pow, ← pow_mul, mul_comm k 2, pow_mul, hsqrt]
    ring
  have hle : ((1/9 : ℝ) * Real.sqrt 2 ^ k) ^ 2 ≤ wStd k ^ 2 := by
    rw [hbsq]; exact wStd_sq_ge_two_pow k hk
  have := Real.sqrt_le_sqrt hle
  rwa [Real.sqrt_sq hb, Real.sqrt_sq (wStd_nonneg k)] at this

/-! ### The class as stated is unsatisfiable -/

/-- **`TowerGeometricLowerBound wStd r c` is false for every `r` and `c`.**

The class demands `c · r^k ≤ w k` for **every** `k`; at `k = 0` that reads `c ≤ w_std 0 = 0`,
contradicting `c_pos`. This is a structural exclusion with a named invariant (the `fDimSkew`
containment guard), not a scope-limited negative: no choice of `r, c` can repair it, and the
fix has to be a threshold in the class rather than a better constant. -/
theorem not_towerGeometricLowerBound_wStd (r c : ℝ) :
    ¬ QOU.Mass.LevelSelection.TowerGeometricLowerBound wStd r c := by
  intro T
  have h0 := T.lower_bound 0
  rw [wStd_eq_zero_of_lt_three 0 (by norm_num), pow_zero, mul_one] at h0
  exact absurd h0 (not_le.mpr T.c_pos)

end QOU.Mass.WStd
