# The determinacy filter — calibrate before applying

**Date** 2026-08-27 · **Branch** `claude/determinacy-filter-binding-candidates-2026-08-27` ·
**Bean** `qou-pjq5` · **Status** IN PROGRESS — scaffold, no findings yet.

## The proposed filter, and why it is not yet trustworthy

PR [#5863](https://github.com/litlfred/qou/pull/5863) closed two fronts that came
out structurally opposite, and the contrast suggested a triage heuristic:

> **Prefer candidate binding terms that carry a genuine extremal or structural
> determinacy; treat a free continuous parameter with no optimum as a warning
> sign.**

The author has authorised testing it. **It is my own heuristic, generalised from
two cases, and that is exactly the shape of claim this repository's disciplines
exist to catch.** So the first task is not to apply it — it is to try to break
it.

## Two ways this could be worthless, both of which must be checked first

1. **It could be a tautology.** "Structural determinacy ⇒ determinate outcome"
   may be true by definition rather than by evidence. If every closed case is
   closed *because* something structural was found, and every open case is open
   *because* nothing structural has been found yet, the filter predicts nothing
   — it just re-describes the outcome after the fact.
2. **It could have false negatives.** If the corpus contains even one result that
   was successfully derived *despite* carrying a free continuous parameter with
   no optimum, the filter would have told an agent to deprioritise a route that
   worked.

## The test, in order

- **Step 1 — assemble the calibration set.** Every binding-term candidate in the
  corpus whose outcome is already settled, positive or negative.
- **Step 2 — classify each by the filter, blind to outcome where possible**, and
  compare against what actually happened. A filter that does not retro-predict
  the closed cases is a story, not a filter.
- **Step 3 — hunt counterexamples deliberately** (defect 2 above), and test the
  tautology charge (defect 1) by asking whether the classification could have
  been made *before* the outcome was known.
- **Step 4 — only if it survives**, apply it forward to the surviving candidates,
  and report the classification as a *triage suggestion* with its measured
  hit-rate attached, never as a verdict.

## What this will NOT do

It will not declare any candidate refuted. A triage heuristic cannot exclude
anything — only a proved invariant can (AGENTS.md §"Before declaring 'refuted'").
Any output here is scope (a) at most: a ranking suggestion carrying its own
error rate.
