/-
# QOU.MassTheory.BranchConvexityBound

Bean `qou-6tcn`.  The invariant behind
`computations/meson/two_remaining_fronts_probe.py` §front 2, and behind the
corollary that `conj:inter-nucleon-channel-color-tube` cannot supply the
deuteron binding *magnitude*.

`atom-branch-convexity-bound` measures that the atom element of `H_n(q)` is a
**convex** combination of its branch closures — `∑_b |w_b| = 1` with every
`w_b > 0`.  Since `tr_M` is linear, `tr_M(atom) = ∑_b w_b tr_M(β_b)`.  What is
proved here is the consequence and, more importantly, **exactly which changes to
the construction escape it**:

* a different *weighting* over the same branches cannot exceed `max_b` — so the
  colour-tube refinement, whose own statement fixes `W ∈ ℚ_{≥0}` normalised to
  `∑ W = 1`, is inside the hypotheses and is bounded by the same number;
* a different *index set* can — which is what a satellite/cabling move does, since
  it replaces each strand by several and so lives in a larger algebra with a
  larger branch set.

That asymmetry is the whole content.  It is why the measured
`max_b tr_M(β_b) = 1.018275 < 1.491498 = √B_AME` closes the reweighting route
(scope (b)) while leaving the satellite route open.

**Base ring (AGENTS.md §7c).**  `ℝ` is genuine here, not gratuitous: the
content is an *inequality*, so an order is required.  Kept concrete rather than
carried over an ordered-field typeclass, because the traces being bounded are
real numbers and the ordered-field class names have drifted across Mathlib
versions; nothing in the proofs uses more than the ordered-field structure.

Imports are the six specific modules the proofs need, not the `Mathlib`
umbrella: the restored olean cache carries per-module oleans but no aggregate
`Mathlib.olean`, so an umbrella import does not resolve here.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.NormNum.Basic
import Mathlib.Tactic.FinCases

set_option autoImplicit false

namespace QOU.MassTheory

open Finset

variable {ι : Type*}

/-- **A convex combination is bounded by the largest term.**  With `t b` the
branch traces and `w` the branch weights, this is
`tr_M(atom) = ∑_b w_b tr_M(β_b) ≤ max_b tr_M(β_b)`. -/
theorem convex_comb_le_bound (s : Finset ι) (w t : ι → ℝ) (M : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hsum : ∑ i ∈ s, w i = 1)
    (hM : ∀ i ∈ s, t i ≤ M) :
    ∑ i ∈ s, w i * t i ≤ M := by
  calc ∑ i ∈ s, w i * t i
      ≤ ∑ i ∈ s, w i * M :=
        Finset.sum_le_sum fun i hi =>
          mul_le_mul_of_nonneg_left (hM i hi) (hw i hi)
    _ = M := by rw [← Finset.sum_mul, hsum, one_mul]

/-- **The exclusion.**  A target strictly above every branch value is
unreachable by any convex reweighting.  Applied: `M = 1.018275` is the measured
`max_b tr_M(β_b)` over the 32 deuteron branches and `target = 1.491498` is
`√B_AME`, so no reweighting — the colour-tube refinement included — gets there. -/
theorem not_reaches_of_bound_lt (s : Finset ι) (w t : ι → ℝ) (M target : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) (hsum : ∑ i ∈ s, w i = 1)
    (hM : ∀ i ∈ s, t i ≤ M) (h : M < target) :
    ∑ i ∈ s, w i * t i < target :=
  lt_of_le_of_lt (convex_comb_le_bound s w t M hw hsum hM) h

/-! ## Non-vacuity, and what escapes

Three guards.  The first two are AGENTS.md §3b-tax (satisfiable, load-bearing);
the third is the one that matters physically — it exhibits the escape. -/

/-- The hypotheses are satisfiable: a point mass is a convex combination. -/
theorem convex_comb_satisfiable (i : ι) [DecidableEq ι] (t : ι → ℝ) :
    ∑ j ∈ ({i} : Finset ι), (fun _ => (1 : ℝ)) j * t j = t i := by
  simp

/-- **Non-negativity is load-bearing.**  Drop `hw` and the bound fails: weights
`(2, -1)` still sum to `1`, but `2·1 + (-1)·0 = 2` exceeds `max = 1`.  So
`convex_comb_le_bound` is not a tautology about sums — it is convexity doing the
work, which is exactly what `atom-branch-convexity-bound` had to *measure*
(`every w_b > 0`) rather than assume. -/
theorem bound_fails_without_nonneg :
    ∃ (w t : Fin 2 → ℝ), ∑ i, w i = 1 ∧ (∀ i, t i ≤ 1) ∧ 1 < ∑ i, w i * t i := by
  refine ⟨![2, -1], ![1, 0], by norm_num [Fin.sum_univ_two], ?_, by
    norm_num [Fin.sum_univ_two]⟩
  intro i
  fin_cases i <;> norm_num

/-- **What escapes: a larger index set.**  The bound is relative to the branch
set it is taken over.  Enlarging that set can raise the maximum and admit values
the old bound excluded — here `2`, which no convex combination over `{0}` could
reach.

This is the satellite/cabling move in miniature.  A satellite replaces each
strand by several, so its branches are words in a *larger* algebra: not a
reweighting of the old branches but a different index set, outside the
hypotheses of `not_reaches_of_bound_lt`.  It is why front 2 closes the
reweighting route without touching the satellite route. -/
theorem larger_index_set_escapes_the_bound :
    ∃ (t : Fin 2 → ℝ) (w : Fin 2 → ℝ),
      (∀ i ∈ ({0} : Finset (Fin 2)), t i ≤ 1) ∧
      (∀ i, 0 ≤ w i) ∧ ∑ i, w i = 1 ∧ 1 < ∑ i, w i * t i := by
  refine ⟨![1, 2], ![0, 1], ?_, ?_, by norm_num [Fin.sum_univ_two], by
    norm_num [Fin.sum_univ_two]⟩
  · intro i hi
    fin_cases hi
    norm_num
  · intro i
    fin_cases i <;> norm_num

end QOU.MassTheory
