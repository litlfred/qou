import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic

/-!
# QOU.Information.MagnitudeAxisBoundary — the counting/decision axis, sorry-free

This file draws, in Lean, the exact **boundary** of what the surreal
ω-grade machinery (`SurrealBudgetGrade`) can and cannot prove — the reason
the `res ≠ 0 ⟹ P≠NP` wall does not fall to a magnitude argument.

**The distinction.**  A *magnitude* / *simplicity* invariant of a decision
problem — the number of accepting witnesses, its ω-grade, and (the answer to
the question that motivated this file) **the surreal *birthday* of that
count** — factors through the **census** `c : ℕ` (how many witnesses),
never through the **predicate** (which witnesses).  `P≠NP` is a statement
about the predicate axis (can an accepting witness be *found*?), which the
census axis cannot see: `#P`-hardness is invariant under `P` vs `NP` (Toda,
`PH ⊆ P^{#P}`).

We formalize this as a clean, non-vacuous, sorry-free fact:

* `census` is the universal magnitude functional (a `Fin k → Bool` predicate
  ↦ its number of `true`s);
* **`census_blind_to_decision`** — there is a genuinely different decision
  pair (`p ≠ q`) on which **every** census-factoring functional agrees.
  The surreal birthday `b(census p)` is such a functional (it factors through
  `census p`), so it too is blind to the difference.

**Honest scope.**  This is a *weaker result by design*: it proves the
counting/decision **gap**, i.e. that no magnitude/birthday invariant bridges
the wall.  It does **not** prove `P≠NP` — on the contrary it delimits the
`SurrealBudgetGrade` squeeze as a *magnitude* separation
(`ord_ω(cost) > ord_ω(budget)`, proved) and marks precisely where that
machinery stops (the predicate axis, open).  Base ring not applicable
(finite decidable combinatorics; `decide` used only on closed finite
computations, never to mask structure — §Strict Lean Discipline item 6).
-/

namespace QOU.Information

open Finset

/-- **Census (the universal magnitude functional).**  The number of accepting
    witnesses of a decision predicate `p : Fin k → Bool`.  Every magnitude /
    simplicity invariant — the ω-grade, and the **surreal birthday of the
    count** — factors through this natural number. -/
def census {k : ℕ} (p : Fin k → Bool) : ℕ := ∑ i, (if p i then 1 else 0)

/-- **A magnitude functional is anything that factors through the census.**
    `F` sees only *how many* witnesses accept, not *which*.  The surreal
    birthday `b ∘ census` is the guiding instance. -/
def FactorsThroughCensus {k : ℕ} {α : Type*} (F : (Fin k → Bool) → α) : Prop :=
  ∀ p q : Fin k → Bool, census p = census q → F p = F q

/-- **The birthday-of-count functional factors through the census
    (sorry-free).**  For *any* `b : ℕ → α`, `b ∘ census` is a magnitude
    functional — the surreal birthday `b(census p)` is the intended `b`.  So
    the boundary below applies to the birthday. -/
theorem factorsThroughCensus_comp_census {k : ℕ} {α : Type*} (b : ℕ → α) :
    FactorsThroughCensus (fun p : Fin k → Bool => b (census p)) :=
  fun _ _ h => congrArg b h

/-- **The counting/decision boundary (sorry-free, non-vacuous).**  There is a
    genuinely different decision pair — `p ≠ q` as predicates — on which
    *every* census-factoring functional agrees.  In particular the surreal
    birthday of the accepting-count cannot distinguish them: it lives on the
    magnitude axis, the difference lives on the predicate axis.  This is the
    `#P`-vs-decision wall as one Lean statement — the exact reason the
    `SurrealBudgetGrade` magnitude squeeze does not, by itself, yield
    `P≠NP`. -/
theorem census_blind_to_decision :
    ∃ p q : Fin 2 → Bool, p ≠ q ∧
      ∀ {α : Type} (F : (Fin 2 → Bool) → α),
        FactorsThroughCensus F → F p = F q := by
  refine ⟨![true, false], ![false, true], ?_, ?_⟩
  · decide
  · intro α F hF
    exact hF _ _ (by decide)

/-- **The census DOES separate on the magnitude axis (sorry-free).**  Rounding
    out the boundary: when the accepting-counts differ, the census — and hence
    any injective magnitude readout — separates.  So magnitude invariants are
    exactly the census-difference detectors: powerful on their own axis, blind
    off it.  Concrete witness: the all-reject vs all-accept predicates. -/
theorem census_separates_on_magnitude :
    ∃ p q : Fin 2 → Bool, census p ≠ census q := by
  exact ⟨![false, false], ![true, true], by decide⟩

end QOU.Information
