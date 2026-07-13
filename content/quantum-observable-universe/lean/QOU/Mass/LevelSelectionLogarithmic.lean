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

**Honest scope (AGENTS.md §"Axiomatization is NOT a Proof").** The combinatorial
core — a super-exponential lower bound on `w_std(k)` — is **not** proved here: a
faithful proof needs SYT + skew-tableau + Plancherel-measure Mathlib infrastructure
that does not yet exist (a multi-session build). It is carried as the **§3b
conjecture class** `TowerGeometricLowerBound` — a `Prop`-valued conditional
assumption with the growth base/constant `r, c` as **parameters** (so an instance is
a genuine proposition about fixed `r, c`, matching the repo's conditional-class
convention, e.g. `NaStokesKeystone.ProlongationPeriodMeanQuantumDim`). It is verified
`k ≤ 10` but has **no global instance** (the open state). This file proves only the
genuinely-provable **downstream** implication: given that lower bound plus extensive
(linear-in-`A`) binding, the exponential of the selected level is at most linear in
`A` — i.e. the level is at most logarithmic — so linear / bond-count selection is
excluded. That is the "conditional-proved ≠ premise-established" half.

Base ring `ℝ` (archimedean: `1 < r`, real order); no other archimedean input.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecificLimits.Normed

namespace QOU.Mass.LevelSelection

/-- **§3b conjecture class — the tower growth lower bound.** A geometric lower bound
`c · r^k ≤ w k` on the branched tower weight `w = w_std`, with base `r` and constant
`c` carried as **parameters** (`Prop`-valued, per the repo's conditional-class
convention). The *verified* statement is strictly stronger — **super-exponential**
growth (successive ratios strictly increasing, `1.38 → 2.88`, `k ≤ 10`;
`wlambda_wstd_growth_bound_probe.py`) — of which this geometric bound is a fortiori a
consequence, and which is all the logarithmic conclusion below needs.

This is the **open** combinatorial core: a faithful proof is the Mathlib-gap lemma
(a super-exponential lower bound on `𝔼_Planch[f^{λ/(2,1)}]`). Per §3b the honest
state is a content-bearing class with **no** fabricated instance; the fields carry
the conjecture's actual content (`one_lt_r`, `c_pos`, and the `∀ k` inequality),
never a `True` marker. -/
class TowerGeometricLowerBound (w : ℕ → ℝ) (r c : ℝ) : Prop where
  /-- `r > 1` — the bound is genuinely growing (the verified growth is
      super-exponential, with `r` effectively unbounded; any fixed `r > 1` is a
      valid — weaker — lower-bound base). -/
  one_lt_r : 1 < r
  /-- `c > 0` — positive leading constant. -/
  c_pos : 0 < c
  /-- The lower bound: `c · r^k ≤ w k` for every jet level `k`. -/
  lower_bound : ∀ k, c * r ^ k ≤ w k

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
theorem level_geometric_bound (w : ℕ → ℝ) (r c : ℝ) [T : TowerGeometricLowerBound w r c]
    (M : ℝ) (kA : ℕ → ℕ) (A : ℕ) (hext : w (kA A) ≤ M * (A : ℝ)) :
    c * r ^ (kA A) ≤ M * (A : ℝ) :=
  le_trans (T.lower_bound (kA A)) hext

/-- **Linear selection is excluded.** The `kA A = A` (linear) instance of the bound:
extensivity forces `c · r^A ≤ M · A` for every `A` — the exponential-vs-linear
inequality that fails for large `A` when `r > 1` (`r^A` outgrows any linear `M·A`).
So no linear level-selection rule is consistent with extensive binding; bond-count
`k = A(A−1)/2` is a fortiori excluded. -/
theorem linear_selection_bound (w : ℕ → ℝ) (r c : ℝ) [T : TowerGeometricLowerBound w r c]
    (M : ℝ) (A : ℕ) (hext : w A ≤ M * (A : ℝ)) :
    c * r ^ A ≤ M * (A : ℝ) :=
  le_trans (T.lower_bound A) hext

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
theorem no_linear_selection (w : ℕ → ℝ) (r c : ℝ) [T : TowerGeometricLowerBound w r c]
    (M : ℝ) (hext : ∀ A : ℕ, 1 ≤ A → w A ≤ M * (A : ℝ)) : False := by
  have hr := T.one_lt_r
  have hc := T.c_pos
  have hr0 : (0:ℝ) < r := by linarith
  have hlo := isLittleO_coe_const_pow_of_one_lt (R := ℝ) (r := r) hr
  have hε : (0:ℝ) < c / (2 * (|M| + 1)) := div_pos hc (by positivity)
  have hev := hlo.def hε
  have hev1 : ∀ᶠ A : ℕ in atTop, 1 ≤ A := eventually_atTop.2 ⟨1, fun A h => h⟩
  obtain ⟨A, hbnd, hA1⟩ := (hev.and hev1).exists
  have hA1' : (1:ℝ) ≤ (A:ℝ) := by exact_mod_cast hA1
  have hApos : (0:ℝ) < (A:ℝ) := by linarith
  have hrpos : (0:ℝ) < r ^ A := pow_pos hr0 A
  rw [Real.norm_eq_abs, Real.norm_eq_abs, abs_of_pos hApos, abs_of_pos hrpos] at hbnd
  have hcombine : c * r ^ A ≤ M * (A:ℝ) := le_trans (T.lower_bound A) (hext A hA1)
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

end QOU.Mass.LevelSelection
