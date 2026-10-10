---
# qou-m3xr
title: Prove YoungTableauStandard.sum_dimSYT_eq_involution
status: completed
type: task
created_at: 2026-08-04T01:55:41Z
updated_at: 2026-08-30T13:29:06Z
---



## CLOSED 2026-08-30 (PR #6164) — PROVED, and NOT by RSK

  QOU.Mass.sum_dimSYT_eq_involution_keystone (k) :
    (Sum p : Nat.Partition k, dimSYT p) = KeystoneC8SuperExpBound.involutionNumber k

That is the field's EXACT statement, sorry-free; #print axioms on the whole chain gives
[propext, Classical.choice, Quot.sound]. File: QOU/Mass/SumSYTEqInvolution.lean.

## This bean's own "Next step" was WRONG, and that is why it sat for four weeks

It read: "Infra-blocked: needs Mathlib theory that does not exist. Track upstream."
The premise -- that this needs RSK, which Mathlib lacks -- is false. Young's lattice is a
1-DIFFERENTIAL POSET, and that route proves the same identity with finite combinatorics on
YoungDiagram: no insertion, no bumping, no permutation<->tableau-pair bijection, nothing
from Mathlib beyond YoungDiagram itself. The chain actually used:

  numStandardYoungTableaux_branching     (already in the corpus, SYTBranchingRule)
  card_addableCells_eq_card_cornerCells_succ  (already in the corpus, YoungDiagramAddable)
  isCornerCell_addCell_iff               (NEW -- the corner-survival correspondence)
  upSum_eq                               (NEW -- the up-operator identity, by induction on |mu|)
  sum_numSYT_recurrence'                 (NEW -- s(n+2) = s(n+1) + (n+1) s(n), unconditional)
  numStandardYoungTableaux_bot + the two base cases  (NEW)

The one genuinely new mathematical step is `isCornerCell_addCell_iff`, and it is a
three-case split on ROW INDICES closed by omega, because `corner_iff` and `addable_iff`
(already present) reduce both notions to the row-length sequence.

LESSON, worth more than the theorem: "Mathlib lacks X, therefore blocked" is only sound
when X is actually REQUIRED. Here the standard textbook proof route (RSK) was mistaken for
the only route, and the bean recorded that mistake as an infra fact. Three docstrings in
content Lean repeated it (SWPeriodSuperExponential, BindingClassicalKernel,
YoungTableauStandard); all three are corrected in the same PR.

## Still open, do NOT read this as closing more than it does

* `branching_two_one`, the OTHER field of RSKIdentitiesContext, is untouched and open.
* The discharged field has not been REMOVED from the class -- that moves every consumer's
  signature and is a separate change.
* The corpus carries TWO definitions of the involution numbers (QOU.Mass.involutionNumber
  and QOU.BraidKnot.KeystoneC8SuperExpBound.involutionNumber). `involutionNumber_eq_keystone`
  bridges them; de-duplicating is a follow-up.
