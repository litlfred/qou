---
# qou-jlam
title: Involution RSK correspondence
status: todo
type: task
priority: normal
tags:
    - needs:combinatorics
created_at: 2026-08-24T06:44:05Z
updated_at: 2026-08-30T03:29:36Z
parent: qou-vkmt
---

sum_dimSYT_eq_involution. RSK for involutions.

## UPDATE 2026-08-30 (PR #6052) — RSK is NOT the route, and the gap is now ONE identity

RSK symmetry (Schuetzenberger) is NOT needed. Young's lattice is a 1-differential poset,
and that route reaches the same recurrence with finite combinatorics on YoungDiagram --
no insertion, no bumping, no permutation<->tableau-pair bijection.

PROVED on the branch, all sorry-free and axiom-clean:

  QOU/Mathlib/YoungLatticeDifferential.lean
    card_addableCells_eq_card_cornerCells_add_one   a(mu) = r(mu) + 1
    mem_cornerCells_iff / mem_addableCells_iff      both families characterised
    card_cornerCells_eq_card_subtype                bridge to the branching index type
  QOU/Mathlib/YoungLatticeCornerCount.lean
    sum_cornerCells_succ_eq_sum_addableCells        unweighted DU = UD + I
    sum_numSYT_succ / _split                        weighted: s(n+1) = s(n) + sum f*r
    sum_numSYT_mul_corners_of_upOperator            sum f*r = (n+1)*s(n), conditionally
    sum_numSYT_recurrence                           s(n+2) = s(n+1) + (n+1)*s(n)

The last is EXACTLY the involution recurrence. With matching base cases it gives
Sum_{lam|-n} f^lam = I(n).

## THE ONE REMAINING OBLIGATION

  UpOperatorIdentity :  Sum_{lam = mu + box} #SYT(lam) = (|mu| + 1) * #SYT(mu)

the classical up-operator identity of Young's lattice. Carried as an explicit
hypothesis in YoungLatticeCornerCount; asserted nowhere. Zero counterexamples over
every partition of 0..9 (97 shapes) -- verification, not proof.

## WHY IT IS NOT CHEAP (do not budget it as a finishing touch)

I worked the proof. Induct on |mu|, branch each cover, and the double sum over
(s addable to mu, c corner of mu+s) must be re-associated as
(c corner of mu, s addable to mu\c). THAT RE-ASSOCIATION IS THE DU = UD + I
BOOKKEEPING ITSELF: the inner sum ranges over addables of mu, but the induction
hypothesis needs addables of mu\c, and those sets differ by exactly the correction
a(mu) = r(mu) + 1 measures. So the pointwise identity is not a shortcut past the
operator argument -- it IS the operator argument, localised. Better SHAPE for Lean
(pointwise rather than a rank sum), not cheaper.

Note also QOU.Mathlib.numStandardYoungTableaux_branching (SYTBranchingRule) is already
proved sorry-free -- do not rebuild it -- and partitionShapeEquiv
(SchenstedPartitionShape) already supplies Nat.Partition n =~ {mu // card = n}.

Also proved and reusable: cornerAddEquiv regrouped as sigma types (rankExchange), which
is what any further differential-poset work in this corpus will need. Its cost is real:
the composite equiv times out whnf at 200000 heartbeats, so it must be a top-level def
with a rfl projection lemma, and Fintype.sum_sigma needs its summand supplied
explicitly.
