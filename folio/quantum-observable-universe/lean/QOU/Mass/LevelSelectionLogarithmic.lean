/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under MIT license. Authors: Claude (Anthropic).

# Level-selection is logarithmic — conditional on tower growth (GAP-A-3)

Formalises the **argument** of the conditional theorem in
`docs/audits/2026-07-11-wlambda-level-selection-log-structural.md`: the
brane-tower level-selection rule `k(A)` is **logarithmic** (`k ∝ A` and
`k ∝ bond-count` excluded), *conditional on* the (super-)exponential growth of the
branched tower weight `w_std(k) = 𝔼_Planch[f^{λ/(2,1)}]` established numerically in
`computations/deltalambda/wlambda_wstd_growth_bound_probe.py` (exact, `k ≤ 10`).

**Scope (updated 2026-09-02).** This header used to say the combinatorial core "is
**not** proved here: a faithful proof needs SYT + skew-tableau + Plancherel-measure
Mathlib infrastructure that does not yet exist (a multi-session build)", and that the
class had "**no global instance** (the open state)".

**Both statements are now false, and the second was false in a way worth naming.**

* The bound *is* proved, and it needed none of that infrastructure — see
  `QOU.Mass.WStd.wStd_geometric_from_three`, which routes through the skew branching
  rule and the up-operator identity (finite combinatorics on `YoungDiagram`).
* The class had no instance not merely because none had been supplied, but because in
  its previous `∀ k` form **it was unsatisfiable at the actual `w_std`**:
  `w_std(k) = 0` for `k < 3`, since no diagram of fewer than three cells contains
  `(2,1)` and `fDimSkew` guards on containment. `QOU.Mass.WStd` proves that refutation
  outright. The class therefore carries a **threshold `k₀`**, which is what makes it
  a true statement rather than a conditional over a falsehood.

The threshold costs the downstream theorems nothing: `no_linear_selection` and
`no_superlinear_selection` keep their statements verbatim, because both already select
their `A` from an `atTop` filter. `level_geometric_bound` and `linear_selection_bound`
gain an explicit `k₀ ≤ …` hypothesis.

What this file proves remains the **downstream** implication: given the lower bound plus
extensive (linear-in-`A`) binding, the exponential of the selected level is at most
linear in `A` — i.e. the level is at most logarithmic — so linear / bond-count selection
is excluded.

Base ring `ℝ` (archimedean: `1 < r`, real order); no other archimedean input.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecificLimits.Normed

namespace QOU.Mass.LevelSelection

/-- **The tower growth lower bound, above a threshold.** A geometric lower bound
`c · r^k ≤ w k` on the branched tower weight `w = w_std`, holding for `k ≥ k₀`, with
base `r`, constant `c` and threshold `k₀` carried as **parameters**.

**Why the threshold is not cosmetic.** This class previously demanded the bound for
*every* `k`, and in that form it is **false** at the real `w_std`: at `k = 0` it reads
`c ≤ w_std 0 = 0`, against `c_pos`. `QOU.Mass.WStd.not_towerGeometricLowerBound_wStd`
proves that refutation for every `r` and `c`, so no choice of constants repaired it —
the threshold is the fix. The vanishing is structural: no diagram of fewer than three
cells contains `(2,1)`, and `fDimSkew` guards on containment.

**Its intended instance is `k₀ = 3`** — exactly where `w_std` stops vanishing, so the
class covers the entire range on which any lower bound is possible. See
`QOU.Mass.WStd.towerGeometricLowerBound_wStd`.

The *measured* growth is strictly stronger than geometric — successive ratios strictly
increasing, `1.38 → 2.88` for `k ≤ 10` (`wlambda_wstd_growth_bound_probe.py`), and the
proved square bound `k!/(81·2^k) ≤ w_std(k)²` is genuinely super-exponential. The
geometric form here is the weaker shadow of that, and is all the logarithmic conclusion
below needs. -/
class TowerGeometricLowerBound (w : ℕ → ℝ) (r c : ℝ) (k₀ : ℕ) : Prop where
  /-- `r > 1` — the bound is genuinely growing (the verified growth is
      super-exponential, with `r` effectively unbounded; any fixed `r > 1` is a
      valid — weaker — lower-bound base). -/
  one_lt_r : 1 < r
  /-- `c > 0` — positive leading constant. -/
  c_pos : 0 < c
  /-- The lower bound: `c · r^k ≤ w k` for every jet level `k ≥ k₀`. -/
  lower_bound : ∀ k, k₀ ≤ k → c * r ^ k ≤ w k

/-- **Conditional theorem — the level's exponential is at most linear in `A`.**
Given the tower lower bound (`TowerGeometricLowerBound w r c`) and *extensive*
binding `w (kA A) ≤ M · A` at the selected level `kA A`, we get

  `c · r^(kA A) ≤ M · A`.

Dividing by `c > 0` gives `r^(kA A) ≤ (M/c)·A`; since `r > 1`, taking `log_r`
(monotone) then gives `kA A ≤ log_r((M/c)·A)` — the level grows **at most
logarithmically** in `A`. A linear rule `kA A = A` would force `c · r^A ≤ M · A`
(exponential ≤ linear), impossible for large `A`; bond-count `A(A−1)/2` is worse.
Both are excluded — matching the scale-free probe (`k∝A` R²=0.67, `k∝`bonds R²=0.49
vs log-type R²≈0.88). Proved outright from the class hypothesis. -/
theorem level_geometric_bound (w : ℕ → ℝ) (r c : ℝ) (k₀ : ℕ) [T : TowerGeometricLowerBound w r c k₀]
    (M : ℝ) (kA : ℕ → ℕ) (A : ℕ) (hk : k₀ ≤ kA A) (hext : w (kA A) ≤ M * (A : ℝ)) :
    c * r ^ (kA A) ≤ M * (A : ℝ) :=
  le_trans (T.lower_bound (kA A) hk) hext

/-- **Linear selection is excluded.** The `kA A = A` (linear) instance of the bound:
extensivity forces `c · r^A ≤ M · A` for every `A` — the exponential-vs-linear
inequality that fails for large `A` when `r > 1` (`r^A` outgrows any linear `M·A`).
So no linear level-selection rule is consistent with extensive binding; bond-count
`k = A(A−1)/2` is a fortiori excluded. -/
theorem linear_selection_bound (w : ℕ → ℝ) (r c : ℝ) (k₀ : ℕ) [T : TowerGeometricLowerBound w r c k₀]
    (M : ℝ) (A : ℕ) (hk : k₀ ≤ A) (hext : w A ≤ M * (A : ℝ)) :
    c * r ^ A ≤ M * (A : ℝ) :=
  le_trans (T.lower_bound A hk) hext

open Filter Topology Asymptotics in
/-- **Linear selection is genuinely impossible (exponential beats linear).** The
`linear_selection_bound` inequality `c·r^A ≤ M·A` cannot hold for *all* `A ≥ 1`:
since `r > 1`, the geometric `c·r^A` eventually outgrows any linear `M·A`
(Mathlib's `isLittleO_coe_const_pow_of_one_lt`: `(A : ℝ) =o[atTop] r^A`). So no
extensive (linear-in-`A`) binding law is consistent with the tower lower bound —
the level-selection rule cannot be linear (nor bond-count `A(A−1)/2`, a fortiori).
This converts the file's "linear excluded" argument into an actual theorem.

Extensivity is required only for `A ≥ 1` (the physical regime); the `A = 0` case is
deliberately excluded — there it would collapse to a boundary artifact
(`w 0 ≥ c > 0` vs `M·0 = 0`) that does **not** capture the exponential-vs-linear
content. The proof genuinely uses the growth lemma, not the boundary. -/
theorem no_linear_selection (w : ℕ → ℝ) (r c : ℝ) (k₀ : ℕ) [T : TowerGeometricLowerBound w r c k₀]
    (M : ℝ) (hext : ∀ A : ℕ, 1 ≤ A → w A ≤ M * (A : ℝ)) : False := by
  have hr := T.one_lt_r
  have hc := T.c_pos
  have hr0 : (0:ℝ) < r := by linarith
  have hlo := isLittleO_coe_const_pow_of_one_lt (R := ℝ) (r := r) hr
  have hε : (0:ℝ) < c / (2 * (|M| + 1)) := div_pos hc (by positivity)
  have hev := hlo.def hε
  have hev1 : ∀ᶠ A : ℕ in atTop, 1 ≤ A ∧ k₀ ≤ A :=
    eventually_atTop.2 ⟨max 1 k₀, fun A h =>
      ⟨le_trans (le_max_left _ _) h, le_trans (le_max_right _ _) h⟩⟩
  obtain ⟨A, hbnd, hA1, hAk⟩ := (hev.and hev1).exists
  have hA1' : (1:ℝ) ≤ (A:ℝ) := by exact_mod_cast hA1
  have hApos : (0:ℝ) < (A:ℝ) := by linarith
  have hrpos : (0:ℝ) < r ^ A := pow_pos hr0 A
  rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos hApos, abs_of_pos hrpos] at hbnd
  have hcombine : c * r ^ A ≤ M * (A:ℝ) := le_trans (T.lower_bound A hAk) (hext A hA1)
  have habs : M ≤ |M| := le_abs_self M
  have hMc : (0:ℝ) < |M| + 1 := by positivity
  have step1 : M * (A:ℝ) ≤ (|M| + 1) * (A:ℝ) := by
    nlinarith [mul_nonneg (by linarith [habs] : (0:ℝ) ≤ |M| - M + 1) (le_of_lt hApos)]
  have step2 : (|M| + 1) * (A:ℝ) ≤ (|M| + 1) * ((c/(2*(|M|+1))) * r^A) :=
    mul_le_mul_of_nonneg_left hbnd (le_of_lt hMc)
  have hne : (|M| + 1) ≠ 0 := ne_of_gt hMc
  have step3 : (|M| + 1) * ((c/(2*(|M|+1))) * r^A) = (c/2) * r^A := by
    field_simp
  have final : c * r ^ A ≤ (c/2) * r ^ A :=
    calc c * r ^ A ≤ M * (A:ℝ) := hcombine
      _ ≤ (|M| + 1) * (A:ℝ) := step1
      _ ≤ (|M| + 1) * ((c/(2*(|M|+1))) * r^A) := step2
      _ = (c/2) * r ^ A := step3
  nlinarith [mul_pos hc hrpos, final]

open Filter Topology Asymptotics in
/-- **Super-linear (incl. bond-count) selection is excluded too.** Generalises
`no_linear_selection`: for any level rule `kA` that is eventually at least linear
(`A ≤ kA A` for `A ≥ A₀`), extensive binding `w (kA A) ≤ M·A` on the same tail is
impossible — because `c·r^A ≤ c·r^{kA A}` (monotonicity, `r > 1`) reduces it to the same
geometric-beats-linear contradiction. In particular the **bond-count** rule
`kA A = A(A−1)/2` satisfies `A ≤ kA A` for `A ≥ 3`, so it is excluded (with `A₀ = 3`,
its physical deuteron-and-up regime) — discharging the "`A(A−1)/2` a fortiori excluded"
claim that `no_linear_selection`'s docstring only asserted in prose. The threshold `A₀`
plays the same honest role as the `A ≥ 1` restriction: it is the physical domain, not a
boundary artifact. -/
theorem no_superlinear_selection (w : ℕ → ℝ) (r c : ℝ) (k₀ : ℕ) [T : TowerGeometricLowerBound w r c k₀]
    (M : ℝ) (kA : ℕ → ℕ) (A₀ : ℕ) (hsuper : ∀ A, A₀ ≤ A → A ≤ kA A)
    (hext : ∀ A, A₀ ≤ A → w (kA A) ≤ M * (A : ℝ)) : False := by
  have hr := T.one_lt_r
  have hc := T.c_pos
  have hr0 : (0:ℝ) < r := by linarith
  have hlo := isLittleO_coe_const_pow_of_one_lt (R := ℝ) (r := r) hr
  have hε : (0:ℝ) < c / (2 * (|M| + 1)) := div_pos hc (by positivity)
  have hev := hlo.def hε
  have hev1 : ∀ᶠ A : ℕ in atTop, (A₀ ≤ A ∧ 1 ≤ A) ∧ k₀ ≤ A :=
    eventually_atTop.2 ⟨max (max A₀ 1) k₀, fun A h =>
      ⟨⟨le_trans (le_trans (le_max_left _ _) (le_max_left _ _)) h,
        le_trans (le_trans (le_max_right _ _) (le_max_left _ _)) h⟩,
       le_trans (le_max_right _ _) h⟩⟩
  obtain ⟨A, hbnd, ⟨hA0, hA1⟩, hAk⟩ := (hev.and hev1).exists
  have hA1' : (1:ℝ) ≤ (A:ℝ) := by exact_mod_cast hA1
  have hApos : (0:ℝ) < (A:ℝ) := by linarith
  have hrpos : (0:ℝ) < r ^ A := pow_pos hr0 A
  rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos hApos, abs_of_pos hrpos] at hbnd
  have hmono : c * r ^ A ≤ c * r ^ (kA A) :=
    mul_le_mul_of_nonneg_left (pow_le_pow_right₀ (le_of_lt hr) (hsuper A hA0)) (le_of_lt hc)
  have hcombine : c * r ^ A ≤ M * (A:ℝ) :=
    le_trans hmono (le_trans (T.lower_bound (kA A) (le_trans hAk (hsuper A hA0))) (hext A hA0))
  have habs : M ≤ |M| := le_abs_self M
  have hMc : (0:ℝ) < |M| + 1 := by positivity
  have step1 : M * (A:ℝ) ≤ (|M| + 1) * (A:ℝ) := by
    nlinarith [mul_nonneg (by linarith [habs] : (0:ℝ) ≤ |M| - M + 1) (le_of_lt hApos)]
  have step2 : (|M| + 1) * (A:ℝ) ≤ (|M| + 1) * ((c/(2*(|M|+1))) * r^A) :=
    mul_le_mul_of_nonneg_left hbnd (le_of_lt hMc)
  have hne : (|M| + 1) ≠ 0 := ne_of_gt hMc
  have step3 : (|M| + 1) * ((c/(2*(|M|+1))) * r^A) = (c/2) * r^A := by field_simp
  have final : c * r ^ A ≤ (c/2) * r ^ A :=
    calc c * r ^ A ≤ M * (A:ℝ) := hcombine
      _ ≤ (|M| + 1) * (A:ℝ) := step1
      _ ≤ (|M| + 1) * ((c/(2*(|M|+1))) * r^A) := step2
      _ = (c/2) * r ^ A := step3
  nlinarith [mul_pos hc hrpos, final]

/-- **Threshold specialization of `linear_selection_bound` (`qou-4h26`).**
Under `TowerGeometricLowerBound w r c k₀`, if `w k₀ ≤ M * (k₀ : ℝ)` then
`c * r ^ k₀ ≤ M * (k₀ : ℝ)`. -/
theorem linear_selection_bound_at_threshold (w : ℕ → ℝ) (r c : ℝ) (k₀ : ℕ)
    [T : TowerGeometricLowerBound w r c k₀] (M : ℝ) (hext : w k₀ ≤ M * (k₀ : ℝ)) :
    c * r ^ k₀ ≤ M * (k₀ : ℝ) :=
  linear_selection_bound w r c k₀ M k₀ (le_refl k₀) hext

end QOU.Mass.LevelSelection
