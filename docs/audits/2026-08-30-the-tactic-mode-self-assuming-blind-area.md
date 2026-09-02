# The self-assuming drain was sized over term-mode proofs only

**Date:** 2026-08-30 · **Beans:** `qou-z9ws` (sized the drain), `qou-24m2` (the earlier blindness) · **PR:** #6249

## What happened

Chasing the `infra-blocked` boilerplate (see the companion audit), one of the fourteen
targets — `QOU.ParticleInteractions.operator_selection_lp` — turned out not to be blocked on a
missing Mathlib LP-duality library at all. Its file docstring says the duality "is now
**proved, sorry-free**". It is neither proved nor, in the sense that matters, sorry-free of
content:

```lean
theorem operator_selection_lp … [ctx : OperatorSelectionLpContext R] :
    IsFeasible ctx.x_star ∧ (∀ x, IsFeasible x → objective ctx.x_star ≤ objective x)
      ∧ objective ctx.x_star = ctx.n_target * ctx.y_0_star := by
  refine ⟨ctx.x_star_feasible, ?_, ctx.zero_gap⟩
  intro x hx
  have hgap : … := ctx.zero_gap
  rw [hgap]
  exact OperatorSelectionLpContext.dual_bound_le_objective x hx
```

All three conjuncts come from class fields. This is AGENTS.md §3b-cond rule 5's
"self-assuming projection": the class carries the conclusion and the theorem projects it.
`#print axioms` is clean, which is exactly why the docstring's claim reads as true.

## It is NOT a bug in the existing detector

`scripts/lean-self-assuming-audit.py` does not flag it, and that is **correct behaviour**.
Its docstring lists the exclusion explicitly:

> Deliberately NOT flagged: proofs with a tactic block (`:= by ...`) — a `by exact h` may
> still be vacuous but needs elaboration to judge; out of scope here

`operator_selection_lp` is `:= by refine …`. A documented scope limit, not a blind spot. This
audit nearly reported it as one.

## What IS affected: the sizing

Bean `qou-z9ws` (completed 2026-08-30) sizes the drain as *"the 112 self-assuming projections
are ~102 independent defects"*, measured with that tool. Since the tool sees term-mode proofs
only, **112 is a floor over term-mode, not a corpus total.** Nothing in `qou-z9ws` is wrong;
the number simply has a scope that should travel with it.

## Probing the excluded area — and this probe's own blind spot

`scripts/lean-self-assuming-tactic-mode-audit.py` (new) reports **57 candidates** whose entire
tactic block cites nothing but projections off their own instance binders. Among them is
`shell_filling_lp_strong_duality`, the third cited sorry of `qou-vs2i` — another of the
fourteen `infra-blocked` beans.

**The 57 does not include `operator_selection_lp`.** The new scanner misses the case that
motivated it: its "no reference outside the binder" rule disqualifies any proof that
introduces a local, and `intro x hx` / `have hgap` is precisely what that proof does.

So the honest figures are:

| population | count | measured by |
|---|---|---|
| term-mode self-assuming | 112 (~102 independent) | `lean-self-assuming-audit.py` (`qou-z9ws`) |
| tactic-mode, no local introductions | 57 candidates | `lean-self-assuming-tactic-mode-audit.py` |
| tactic-mode WITH local introductions | **unmeasured** | — (contains `operator_selection_lp`) |

Quote 57 as a floor on a sub-class, and say which sub-class.

## The recurring shape

This is the same lesson the repo's detector-blindness taxonomy already carries: **a detector
sees one spelling.** What is new is how tight the loop was — a scanner written specifically to
cover a spelling the previous tool missed, missed its own motivating example, for a third
independent reason. Widening it needs a way to tell a local standing in for a field from a
local doing real work, which is the elaboration the term-mode tool declined for the same
reason. Recorded rather than fixed.

## Not done here

- The 57 candidates are **not triaged**; they are candidates, not verdicts.
- `operator_selection_lp`'s docstring still says "proved, sorry-free". Fixing it means
  deciding whether the class is legitimately §3b-cond (a genuine hypothesis) or a
  conclusion-carrier (a defect). That is a per-item judgement and belongs with the `qou-z9ws`
  drain, not in this PR.
