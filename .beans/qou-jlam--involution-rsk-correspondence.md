---
# qou-jlam
title: Involution RSK correspondence
status: completed
type: task
priority: normal
tags:
    - needs:combinatorics
created_at: 2026-08-24T06:44:05Z
updated_at: 2026-09-03T20:47:18Z
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


## CLOSED 2026-08-30 (PR #6164) — UpOperatorIdentity is PROVED

  QOU.Mathlib.upSum_eq :  upSum mu = (|mu| + 1) * numStandardYoungTableaux mu

sorry-free; #print axioms = [propext, Classical.choice, Quot.sound]. Transported to the
subtype form and used to discharge the hypothesis:

  QOU/Mathlib/YoungLatticeUpOperator.lean   (new)
    rowLen_eq_of_mem_iff                 a row length is pinned by its membership predicate
    rowLen_addCell / rowLen_eraseCorner  (mu + (a,b)).rowLen i = mu.rowLen i + [i = a], etc.
    isCornerCell_addCell_iff             THE lemma: IsCornerCell (mu+s) c <-> IsAddableCell (mu\c) s
    isCornerCell_of_addCell              c corner of mu+s, c != s  =>  c corner of mu
    isAddableCell_of_eraseCorner         s addable to mu\c, s != c  =>  s addable to mu
    eraseCorner_addCell_comm             (mu+s)\c = (mu\c)+s
    branching_finset                     branching over the Finset cornerCells, not the subtype
    pairTerm / numSYT_addCell_eq / sum_pairTerm_add / upSum_eq
  QOU/Mathlib/YoungLatticeCornerCount.lean
    sum_subtype_addable_eq_upSum, upOperatorIdentity_holds
    sum_numSYT_recurrence'               s(n+2) = s(n+1) + (n+1)*s(n), NO hypothesis

## The bean's own "why it is not cheap" was RIGHT about the obstacle and WRONG about the price

It said the re-association (s addable to mu, c corner of mu+s) -> (c corner of mu,
s addable to mu\c) IS the DU = UD + I bookkeeping. Correct, and that is exactly what
`isCornerCell_addCell_iff` is. What made it tractable was not a shortcut past the operator
argument but noticing that `corner_iff` and `addable_iff` (already in YoungDiagramAddable)
reduce BOTH notions to the row-length sequence. Then insertion and deletion are +1/-1 on
one row, and the re-association is a three-case split on the row indices (a = p, a = p+1,
neither), each closed by omega. The geometry: inserting s destroys the corner c exactly
when s is c's right or lower neighbour, and those are exactly the two positions where s
fails to be addable to mu\c.

Two devices did the Finset work:
* `pairTerm`, the summand made total in BOTH cells (0 off the good cases), so each order
  of summation ranges over the full addableCells/cornerCells and Finset.sum_comm applies
  with nothing to check;
* the identity arranged as  upSum mu + r(mu) f^mu = a(mu) f^mu + n f^mu  so that NO
  natural-number subtraction appears. n = 0 is not special-cased -- an empty corner set
  makes both new terms vanish on their own.

The operator-algebra route (D U = U D + I on Q[Young], read off D U^{m+1} 0 = (m+1) U^m 0)
was NOT taken: it needs the off-diagonal -- a statement about PAIRS of diagrams -- plus the
free-module setup. The direct induction needs neither.

## What this does and does not close

DOES: the recurrence s(n+2) = s(n+1) + (n+1) s(n), unconditionally.
DOES NOT: Sum_{lam |- n} f^lam = I(n) itself. That still needs the two base cases
s(0) = s(1) = 1 tied to involutionNumber's, and the induction identifying the two
sequences. Both are small next to what just landed, but they are not done, and no
artifact should say the involution identity is proved until they are. Follow-up: qou-jl2.



## 2026-09-03 — the 'zero consumers outside this file' measurement was WRONG
6164a8ab6e removed YoungDiagramAddCell.mem_addCell (s) (hs) (x) on the measured claim that mem_addCell had zero consumers outside the file. QOU/SchurWeyl/MarkovConventionD.lean:83 (rowLen_two_pos_addCell, landed 08-23 in d239feda97) called it with that argument order, so MarkovConventionD — and everything downstream: MarkovTraceInstance, the Feynman markov_identification instance — has been red on main since 08-30. Not caught because nothing rebuilds the library: lean-direct on a single file certifies against the oleans ON DISK, and the restored cache predates the change. Fixed on PR #6526 by calling the surviving YoungDiagramAddable.mem_addCell μ c x hc. TRAP: a grep for consumers must include the argument-order-different call shapes, and a 'zero consumers' claim needs a rebuild of the importers, not a grep.
