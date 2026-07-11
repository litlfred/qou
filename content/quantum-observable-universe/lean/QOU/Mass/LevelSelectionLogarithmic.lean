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
conjecture class** `TowerGeometricLowerBound` — a *content-bearing* class (a
parameter-quantified inequality, per §3b-tax, not an empty marker), verified
`k ≤ 10` but with **no global instance** (the open state). This file proves only the
genuinely-provable **downstream** implication: given that lower bound plus extensive
(linear-in-`A`) binding, the exponential of the selected level is at most linear in
`A` — i.e. the level is at most logarithmic — so linear / bond-count selection is
excluded. That is the "conditional-proved ≠ premise-established" half.

Base ring `ℝ` (archimedean: `1 < r`, real order); no other archimedean input.
-/
import Mathlib.Data.Real.Basic

namespace QOU.Mass.LevelSelection

/-- **§3b conjecture class — the tower growth lower bound.** A geometric lower bound
`c · r^k ≤ w k` (`r > 1`, `c > 0`) on the branched tower weight `w = w_std`. The
*verified* statement is strictly stronger — **super-exponential** growth (successive
ratios strictly increasing, `1.38 → 2.88`, `k ≤ 10`;
`wlambda_wstd_growth_bound_probe.py`) — of which a geometric lower bound is a
fortiori a consequence, and which is all the logarithmic conclusion below needs.

This is the **open** combinatorial core: a faithful proof is the Mathlib-gap lemma
(a super-exponential lower bound on `𝔼_Planch[f^{λ/(2,1)}]`). Per §3b the honest
state is a content-bearing class with **no** fabricated instance; the fields carry
the conjecture's actual content (`one_lt_r`, `c_pos`, and the `∀ k` inequality),
never a `True` marker. -/
class TowerGeometricLowerBound (w : ℕ → ℝ) where
  /-- Geometric base `> 1` (the verified growth is super-exponential, `r` unbounded;
      any fixed `r > 1` is a valid — weaker — lower-bound base). -/
  r : ℝ
  /-- Positive leading constant. -/
  c : ℝ
  /-- `r > 1` — the bound is genuinely growing. -/
  one_lt_r : 1 < r
  /-- `c > 0`. -/
  c_pos : 0 < c
  /-- The lower bound: `c · r^k ≤ w k` for every jet level `k`. -/
  lower_bound : ∀ k, c * r ^ k ≤ w k

/-- **Conditional theorem — the level's exponential is at most linear in `A`.**
Given the tower lower bound (`TowerGeometricLowerBound w`) and *extensive* binding
`w (kA A) ≤ M · A` at the selected level `kA A`, we get

  `c · r^(kA A) ≤ M · A`.

Since `r > 1`, this says `r^(kA A) ≤ (M/c)·A`, i.e. `kA A ≤ log_r((M/c)·A)` — the
level grows **at most logarithmically** in `A`. A linear rule `kA A = A` would force
`c · r^A ≤ M · A` (exponential ≤ linear), impossible for large `A`; bond-count
`A(A−1)/2` is worse. Both are excluded — matching the scale-free probe
(`k∝A` R²=0.67, `k∝`bonds R²=0.49 vs log-type R²≈0.88). Proved outright from the
class hypothesis (no further assumption). -/
theorem level_geometric_bound (w : ℕ → ℝ) [T : TowerGeometricLowerBound w]
    (M : ℝ) (kA : ℕ → ℕ) (A : ℕ) (hext : w (kA A) ≤ M * (A : ℝ)) :
    T.c * T.r ^ (kA A) ≤ M * (A : ℝ) :=
  le_trans (T.lower_bound (kA A)) hext

/-- **Linear selection is excluded.** The `kA A = A` (linear) instance of the bound:
extensivity forces `c · r^A ≤ M · A` for every `A` — the exponential-vs-linear
inequality that fails for large `A` when `r > 1` (`r^A` outgrows any linear `M·A`).
So no linear level-selection rule is consistent with extensive binding; bond-count
`k = A(A−1)/2` is a fortiori excluded. (The explicit logarithmic ceiling
`r^(kA A) ≤ (M/c)·A`, hence `kA A ≤ log_r((M/c)·A)`, is the immediate division of
`level_geometric_bound` by `c > 0`.) -/
theorem linear_selection_bound (w : ℕ → ℝ) [T : TowerGeometricLowerBound w]
    (M : ℝ) (A : ℕ) (hext : w A ≤ M * (A : ℝ)) :
    T.c * T.r ^ A ≤ M * (A : ℝ) :=
  le_trans (T.lower_bound A) hext

end QOU.Mass.LevelSelection
