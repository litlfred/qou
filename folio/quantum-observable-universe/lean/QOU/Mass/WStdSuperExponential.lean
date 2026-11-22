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

## The class was unsatisfiable as stated; it now carries a threshold, and is inhabited

`LevelSelectionLogarithmic.TowerGeometricLowerBound` used to demand `c · r^k ≤ w k` for
**every** `k`.  At the real `w_std` that is false, and not marginally: `w_std(k) = 0` for
`k < 3`, because no diagram of fewer than three cells contains `(2,1)` and `fDimSkew` guards
on containment.  `not_towerGeometricLowerBound_wStd_of_lt_three` proves the refutation
outright, for every `r` and `c` — a structural exclusion with an invariant, not a failed
search, so no choice of constants could have repaired it.

The class therefore carries a threshold `k₀`, and `towerGeometricLowerBound_wStd` **inhabits
it at `k₀ = 3`**.  With that instance the level-selection exclusions apply to the actual
`w_std` rather than to an abstract `w`: `no_linear_selection_wStd` and
`no_superlinear_selection_wStd` below are those two theorems with nothing left conditional.

The honest positive statement is a **threshold** bound, and `wStd_geometric_from_three`
supplies one: `(1/30)·(√2)^k ≤ w_std(k)` for `k ≥ 3`, which is the class's `lower_bound` field
with `r = √2 > 1` and `c = 1/30 > 0` on that tail.  `k ≥ 3` is not an artifact — it is exactly
where `w_std` stops vanishing, so the bound covers the whole range on which any bound is
possible.  Everything downstream (`no_linear_selection`, `no_superlinear_selection`) already
works on a tail — they pick an `A` from an `atTop` filter — so the threshold class serves
them unchanged.

**A correction to my own first attempt, kept because the reasoning is the point.**  The first
version of this file proved the bound only from `k ≥ 9`, and its header said the threshold was
"an artifact of the crude step `4^k ≤ k!`" which could be lowered only by computing the six
values `w_std(3) … w_std(8)` — "a finite computation this file does not do".  **That was wrong
about the remedy.**  No value of `w_std` is needed: the threshold is set by the *constant*, and
weakening `c` from `1/9` to `1/30` moves the integer step from `4^k ≤ k!` (first true at
`k = 9`) to `9·4^k ≤ 100·k!` (first true at `k = 3`, and tight there: `576 ≤ 600`).  The
optimum over `k ≥ 3` of `k!/(81·4^k)` is attained at `k = 3` and equals `1/864`, so any
`c ≤ 1/√864 ≈ 0.0340` works; `1/30` is the round number under it.

Base ring `ℝ` (archimedean: `√2`, real order) — the wall is crossed only in the last two
results; everything above `wStd_sq_lower` is `ℕ`-combinatorial.

## References

- [leitner2026] bean `wsxl`, bean `qou-b21r`
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

/-- `9·4^k ≤ 100·k!` for `k ≥ 3` — the integer step behind the geometric bound.

Tight at the base: `9·4³ = 576` against `100·3! = 600`.  The weaker constant is what buys the
low threshold; the sharper `4^k ≤ k!` is first true only at `k = 9` (it fails at `k = 8`,
`65536 > 40320`), which is where an earlier version of this file had to start. -/
theorem nine_four_pow_le_hundred_factorial :
    ∀ d : ℕ, 9 * 4 ^ (d + 3) ≤ 100 * (d + 3).factorial := by
  intro d
  induction d with
  | zero => decide
  | succ n ih =>
    calc 9 * 4 ^ (n + 1 + 3) = 4 * (9 * 4 ^ (n + 3)) := by ring
      _ ≤ 4 * (100 * (n + 3).factorial) := Nat.mul_le_mul_left _ ih
      _ ≤ (n + 3 + 1) * (100 * (n + 3).factorial) := Nat.mul_le_mul_right _ (by omega)
      _ = 100 * ((n + 3) + 1).factorial := by rw [Nat.factorial_succ (n + 3)]; ring
      _ = 100 * (n + 1 + 3).factorial := rfl

/-- **`2^k/900 ≤ w_std(k)²` for `k ≥ 3`** — `wStd_sq_lower` with `k!` bounded below via
`nine_four_pow_le_hundred_factorial`. -/
theorem wStd_sq_ge_two_pow (k : ℕ) (hk : 3 ≤ k) : (2:ℝ) ^ k / 900 ≤ wStd k ^ 2 := by
  obtain ⟨d, rfl⟩ : ∃ d, k = d + 3 := ⟨k - 3, by omega⟩
  have hfac : (9:ℝ) * 4 ^ (d + 3) ≤ 100 * ((d + 3).factorial : ℝ) := by
    exact_mod_cast nine_four_pow_le_hundred_factorial d
  have hlow := wStd_sq_lower (d + 3) (by omega)
  refine le_trans ?_ hlow
  have hp : (0:ℝ) < 2 ^ (d + 3) := by positivity
  have h4 : (4:ℝ) ^ (d + 3) = 2 ^ (d + 3) * 2 ^ (d + 3) := by rw [← mul_pow]; norm_num
  have key1 : (2:ℝ) ^ (d + 3) / 900
      = (9 * (4:ℝ) ^ (d + 3)) / (8100 * 2 ^ (d + 3)) := by
    rw [h4]; field_simp; ring
  have key2 : ((d + 3).factorial : ℝ) / (81 * 2 ^ (d + 3))
      = (100 * ((d + 3).factorial : ℝ)) / (8100 * 2 ^ (d + 3)) := by
    field_simp; ring
  rw [key1, key2]
  gcongr

/-- **The geometric bound: `(1/30)·(√2)^k ≤ w_std(k)` for `k ≥ 3`.**

This is exactly `TowerGeometricLowerBound.lower_bound` with `r = √2 > 1` and `c = 1/30 > 0`,
restricted to `k ≥ 3` — which is all that is possible, since `w_std` vanishes below it, and all
that `no_linear_selection` / `no_superlinear_selection` consume, since both pick their `A` from
an `atTop` filter. -/
theorem wStd_geometric_from_three (k : ℕ) (hk : 3 ≤ k) :
    (1/30 : ℝ) * Real.sqrt 2 ^ k ≤ wStd k := by
  have hb : (0:ℝ) ≤ (1/30 : ℝ) * Real.sqrt 2 ^ k := by positivity
  have hsqrt : (Real.sqrt 2) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hbsq : ((1/30 : ℝ) * Real.sqrt 2 ^ k) ^ 2 = (2:ℝ) ^ k / 900 := by
    rw [mul_pow, ← pow_mul, mul_comm k 2, pow_mul, hsqrt]
    ring
  have hle : ((1/30 : ℝ) * Real.sqrt 2 ^ k) ^ 2 ≤ wStd k ^ 2 := by
    rw [hbsq]; exact wStd_sq_ge_two_pow k hk
  have := Real.sqrt_le_sqrt hle
  rwa [Real.sqrt_sq hb, Real.sqrt_sq (wStd_nonneg k)] at this

/-! ### Why the class needs its threshold, and what inhabits it -/

/-- **No threshold below 3 is satisfiable, for any `r` and `c`.**

At `k = k₀ < 3` the class's own field reads `c · r^{k₀} ≤ w_std(k₀) = 0`, against `c_pos` and
`r > 0`. A structural exclusion with a named invariant (the `fDimSkew` containment guard), not
a scope-limited negative: no choice of constants repairs it, which is why the class carries a
threshold rather than better constants.

In particular the class's previous `∀ k` form — the `k₀ = 0` case here — was **false**, so
every result conditional on it was conditional on a falsehood. -/
theorem not_towerGeometricLowerBound_wStd_of_lt_three (r c : ℝ) (k₀ : ℕ) (hk₀ : k₀ < 3) :
    ¬ QOU.Mass.LevelSelection.TowerGeometricLowerBound wStd r c k₀ := by
  intro T
  have h := T.lower_bound k₀ le_rfl
  rw [wStd_eq_zero_of_lt_three k₀ hk₀] at h
  have hr : (0:ℝ) < r := lt_trans zero_lt_one T.one_lt_r
  nlinarith [T.c_pos, pow_pos hr k₀]

/-- **The class is inhabited at `k₀ = 3`** — the first threshold the previous result allows,
and exactly where `w_std` stops vanishing. -/
instance towerGeometricLowerBound_wStd :
    QOU.Mass.LevelSelection.TowerGeometricLowerBound wStd (Real.sqrt 2) (1/30) 3 where
  one_lt_r := by nlinarith [Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num), Real.sqrt_nonneg 2]
  c_pos := by norm_num
  lower_bound := wStd_geometric_from_three

/-! ### The exclusions, now about `w_std` itself

`no_linear_selection` and `no_superlinear_selection` were stated over an abstract `w : ℕ → ℝ`
with an uninhabited hypothesis, so neither could be applied to anything. These are those two
theorems at the actual branched tower weight, with nothing conditional left. -/

/-- **Linear level-selection is excluded, unconditionally, for the real `w_std`.** -/
theorem no_linear_selection_wStd (M : ℝ)
    (hext : ∀ A : ℕ, 1 ≤ A → wStd A ≤ M * (A : ℝ)) : False :=
  QOU.Mass.LevelSelection.no_linear_selection wStd (Real.sqrt 2) (1/30) 3 M hext

/-- **Super-linear selection — bond-count `A(A−1)/2` included — likewise.** -/
theorem no_superlinear_selection_wStd (M : ℝ) (kA : ℕ → ℕ) (A₀ : ℕ)
    (hsuper : ∀ A, A₀ ≤ A → A ≤ kA A)
    (hext : ∀ A, A₀ ≤ A → wStd (kA A) ≤ M * (A : ℝ)) : False :=
  QOU.Mass.LevelSelection.no_superlinear_selection wStd (Real.sqrt 2) (1/30) 3 M kA A₀ hsuper hext

end QOU.Mass.WStd
