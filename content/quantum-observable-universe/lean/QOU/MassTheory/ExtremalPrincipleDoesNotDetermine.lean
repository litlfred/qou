/-
ExtremalPrincipleDoesNotDetermine.lean — an extremal principle over an
underdetermined constraint carries ZERO information about which coordinate wins.
The cost decides, and the cost is a modelling choice.

WHY THIS EXISTS.  PR #5863 closed two fronts and suggested a triage heuristic:
*prefer candidate binding terms carrying a genuine extremal or structural
determinacy; treat a free continuous parameter with no optimum as a warning
sign.*  That heuristic is the author-authorised subject of bean `qou-pjq5`, and
the first task is to break it rather than apply it.

This file breaks half of it.  "Extremal" was doing no work.

THE CORPUS CASE.  Option D of the Δ_λ closure programme
(`docs/audits/2026-05-09-mass-table-fitting-audit.md`) minimised
`Σ_λ |Δ_λ|·w_λ` subject to the single binding constraint.  Under the Plancherel
cost it reproduced the pre-existing Occam answer exactly (L∞ = 1.91e-15); under
a Frobenius cost it selected a *different* partition (`λ = [6]`,
`Δ = −47.16`).  The audit's own verdict — *"moves the underdetermination to the
choice of cost rather than eliminating it"* — is what this file proves in
general.

WHAT IS PROVED.  For a single linear constraint `Σ aᵢxᵢ = b`, the cheapest
single-support solution at coordinate `i` costs `wᵢ·|b|/|aᵢ|`, so the ordering
between two coordinates is governed by `wᵢ/|aᵢ|` alone.  Since `a` and `b` are
fixed by the constraint and `w` is not, `both_orderings_achievable` shows BOTH
orderings are reachable by choosing `w` — for ANY constraint whatsoever.  The
extremum therefore determines nothing about which coordinate carries the answer.

WHAT THIS DOES NOT SAY.  It does not say LP methods are useless, and it does not
refute any particular candidate.  It says one thing precisely: *having an
optimum* is not the same as *being determined*, so an extremal principle earns
its place only when its objective is itself derived.  Whether any given
objective is derived is a separate question this file does not touch.

Over `ℝ` deliberately (AGENTS.md §7c): this is about orderings and absolute
values, so it is archimedean by nature.

@module QOU.MassTheory.ExtremalPrincipleDoesNotDetermine
-/

import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

set_option autoImplicit false

namespace QOU.MassTheory

/-- The cost of the single-support solution at a coordinate with constraint
coefficient `a` and cost weight `w`: put all the mass there (`x = b / a`) and
pay `w · |x|`. -/
noncomputable def singleSupportCost (w a b : ℝ) : ℝ := w * |b| / |a|

/-- The comparison between two coordinates depends on the constraint only
through `|aᵢ|`, and on the cost only through `wᵢ` — as the single ratio
`wᵢ / |aᵢ|`.  The target `b` cancels entirely. -/
theorem cost_lt_iff (w₁ w₂ a₁ a₂ b : ℝ) (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0) (hb : b ≠ 0) :
    singleSupportCost w₁ a₁ b < singleSupportCost w₂ a₂ b
      ↔ w₁ / |a₁| < w₂ / |a₂| := by
  have h1 : (0 : ℝ) < |a₁| := abs_pos.mpr ha₁
  have h2 : (0 : ℝ) < |a₂| := abs_pos.mpr ha₂
  have hbp : (0 : ℝ) < |b| := abs_pos.mpr hb
  have e₁ : singleSupportCost w₁ a₁ b = (w₁ / |a₁|) * |b| := by
    unfold singleSupportCost; field_simp
  have e₂ : singleSupportCost w₂ a₂ b = (w₂ / |a₂|) * |b| := by
    unfold singleSupportCost; field_simp
  rw [e₁, e₂, mul_lt_mul_iff_left₀ hbp]

/-- **The refutation.**  For ANY single constraint, both orderings of any two
coordinates are achievable by choosing the cost weights — so the extremum
carries no information about which coordinate wins.  The cost does, and the cost
is a modelling choice rather than a consequence of the constraint. -/
theorem both_orderings_achievable (a₁ a₂ b : ℝ)
    (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0) (hb : b ≠ 0) :
    (∃ w₁ w₂ : ℝ, 0 < w₁ ∧ 0 < w₂ ∧
        singleSupportCost w₁ a₁ b < singleSupportCost w₂ a₂ b) ∧
    (∃ w₁ w₂ : ℝ, 0 < w₁ ∧ 0 < w₂ ∧
        singleSupportCost w₂ a₂ b < singleSupportCost w₁ a₁ b) := by
  have h1 : (0 : ℝ) < |a₁| := abs_pos.mpr ha₁
  have h2 : (0 : ℝ) < |a₂| := abs_pos.mpr ha₂
  constructor
  · refine ⟨|a₁|, 2 * |a₂|, h1, by linarith, ?_⟩
    rw [cost_lt_iff _ _ _ _ _ ha₁ ha₂ hb]
    rw [div_self (ne_of_gt h1), mul_div_assoc, div_self (ne_of_gt h2)]
    norm_num
  · refine ⟨2 * |a₁|, |a₂|, by linarith, h2, ?_⟩
    rw [cost_lt_iff _ _ _ _ _ ha₂ ha₁ hb]
    rw [div_self (ne_of_gt h2), mul_div_assoc, div_self (ne_of_gt h1)]
    norm_num

/-- **The corpus instance in miniature.**  One constraint `x₁ + 2x₂ = 1`.  The
uniform cost `w = (1,1)` prefers coordinate 2; the reweighted cost `w = (1,4)`
prefers coordinate 1.  Same feasible set, same optimum *principle*, different
answer — which is Option D's Plancherel-vs-Frobenius split, stripped to two
coordinates. -/
theorem two_costs_two_minimisers :
    singleSupportCost 1 2 1 < singleSupportCost 1 1 1 ∧
    singleSupportCost 1 1 1 < singleSupportCost 4 2 1 := by
  constructor <;> norm_num [singleSupportCost]

/-- **Non-vacuity.**  The freedom is in the cost, not in the arithmetic: hold the
cost weights EQUAL and the constraint alone does decide, by `|aᵢ|`.  So the
theorem above is about the modelling choice, not about an ill-posed comparison. -/
theorem equal_costs_are_decided_by_the_constraint
    (w a₁ a₂ b : ℝ) (hw : 0 < w) (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0) (hb : b ≠ 0)
    (h : |a₂| < |a₁|) :
    singleSupportCost w a₁ b < singleSupportCost w a₂ b := by
  rw [cost_lt_iff _ _ _ _ _ ha₁ ha₂ hb]
  have h1 : (0 : ℝ) < |a₁| := abs_pos.mpr ha₁
  have h2 : (0 : ℝ) < |a₂| := abs_pos.mpr ha₂
  exact div_lt_div_of_pos_left hw h2 h

end QOU.MassTheory
