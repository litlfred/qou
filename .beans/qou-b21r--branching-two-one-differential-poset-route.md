---
# qou-b21r
title: 'branching_two_one: the differential-poset route (needs ONE lemma, not RSK)'
status: todo
type: task
priority: normal
tags:
    - lean
    - needs:combinatorics
created_at: 2026-08-30T14:46:08Z
updated_at: 2026-08-31T03:21:55Z
---

`RSKIdentitiesContext.branching_two_one` is the class's one remaining open field
(QOU/BraidKnot/YoungTableauStandard.lean). Its docstrings said it is "discharged by the RSK
correspondence", the open P1-P5 program. **That is probably wrong, and it is the same
mis-diagnosis that kept `sum_dimSYT_eq_involution` parked for weeks** (qou-jlam, qou-m3xr).

## The route

    G(mu, k) := sum_{|lam|=k} f^lam * f^{lam/mu},    claim  G(mu,k) = (k!/|mu|!) * f^mu

At mu = (2,1) -- f^mu = 2, |mu|! = 6 -- that is `3 * sum = k!`, i.e. branching_two_one verbatim.

Induction on k, base G(mu, |mu|) = f^mu (the only lam of size |mu| containing mu is mu):

    G(mu, k+1) = sum_lam f^lam * sum_{nu <. lam, nu >= mu} f^{nu/mu}   [skew branching]
               = sum_nu  f^{nu/mu} * sum_{lam .> nu} f^lam             [transpose]
               = sum_nu  f^{nu/mu} * (k+1) * f^nu                      [upSum_eq]
               = (k+1) * G(mu, k)

## Status of the three inputs

* **upSum_eq** -- PROVED sorry-free (PR #6164), QOU/Mathlib/YoungLatticeUpOperator.lean.
* **the transposition** -- the same Finset.sum_comm manoeuvre `pairTerm` performs in that
  file; the device carries over directly.
* **skew branching** -- THE ONE OPEN INPUT. `f^{lam/mu} = sum over corners c of lam with
  c not in mu of f^{(lam-c)/mu}`, i.e. remove the largest entry of a skew SYT. Direct
  analogue of the proved QOU.Mathlib.numStandardYoungTableaux_branching, over
  `SkewStandardYoungTableau` (QOU/BraidKnot/YoungTableauStandard.lean:134, `fDimSkew`, which
  guards on containment and is 0 otherwise -- the guard matters, see
  `skewSYT_nonempty_of_not_le`: unguarded, branching_two_one is FALSE at k=3).

## Evidence, and its limit

`computations/combinatorics/branching_two_one_route_probe.py` confirms the identity EXACTLY
for k = 3..11 (exact integers, no float constructed).

**It does NOT verify skew branching.** The probe computes f^{lam/mu} BY that recursion, so it
assumes the open input. Read it as "the route's arithmetic is sound", not as a partial proof.
Stated explicitly because the whole point of this bean is that a plausible-sounding
justification was previously mistaken for an established one.

## Do not

* Do not record branching_two_one as proved, or the route as more than a route.
* Do not conclude from qou-jlam that "no RSK identity needs RSK". THIS one has a checked
  non-RSK route; that says nothing about the other RSK-family targets.
* Do not remove the containment guard on fDimSkew to simplify the sum -- it is what makes the
  statement true.

## Scale of the one open input, MEASURED (2026-08-30)

The skew branching rule is not a finishing touch. The straight-case machinery it must mirror
is ~443 lines across four files:

    172  QOU/Mathlib/SYTInsertMax.lean         insertMax: re-insert |mu| at a corner
    111  QOU/Mathlib/SYTEraseMax.lean          eraseMax: delete the max-value corner
     67  QOU/Mathlib/SYTBranchingBijection.lean  insertMax/eraseMax mutually inverse
     93  QOU/Mathlib/SYTBranchingRule.lean     Nat.card_congr + Nat.card_sigma

and the skew analogue is HARDER than a transliteration, for a specific reason: the two
structures certify their filling differently.

    StandardYoungTableau      bijOn : Set.BijOn entry mu.cells (Set.Icc 1 |mu|)
    SkewStandardYoungTableau  content : (outer.cells \ inner.cells).image (entry) = range card

`Set.BijOn` gives injectivity and surjectivity as separate, directly usable facts. The skew
`content` field gives a Finset image EQUALITY, from which both must be re-derived (card of
the image = card of the set forces injectivity on the skew region). Every step of insertMax /
eraseMax that currently cites bijOn needs that derivation first.

Note also the skew entries are 0-based (`range card`) while the straight ones are 1-based
(`Icc 1 card`); do not port index arithmetic without re-checking it.

Shape of the target:

    fDimSkew lam mu = sum over {c : IsCornerCell lam c, c not in mu} of fDimSkew (lam - c) mu

with the side condition that `mu <= lam - c` iff `c not in mu` (so the guard on fDimSkew keeps
the summand meaningful). Then G(mu,k) is a straightforward induction on top of upSum_eq.

Estimate: 300-500 lines of new Lean. Budget it as its own tranche; do NOT open it alongside
other work and do NOT land it with sorries (AGENTS.md zero-sorry default).


## PROGRESS 2026-08-31 — the erase-max step is PROVED

`QOU/Mathlib/SkewSYTMaxCorner.lean`, six lemmas, sorry-free, axioms
[propext, Classical.choice, Quot.sound]:

    skew_injOn          entry is injective on the skew region
    skew_mem_range      every skew entry is < |skew|
    skew_exists_of_lt   every value < |skew| is attained
    skew_right_mem      a skew cell's right neighbour, if in outer, is also skew
    skew_down_mem       likewise downward
    exists_max_corner   THE STEP: the maximal entry sits on a corner of outer OUTSIDE inner

## The scope note's "harder than a transliteration" reason is now a ONE-OFF cost, not per-site

The note said: StandardYoungTableau gives Set.BijOn (both halves directly usable), while
SkewStandardYoungTableau gives a Finset IMAGE EQUALITY from which both must be re-derived at
every site citing bijOn. The first three lemmas do that derivation ONCE. The remaining
development can cite them the way the straight case cites bijOn, so the multiplier the note
worried about does not apply.

## What is still open — do not read this as the branching rule

Proved here: the GEOMETRY of the erase direction. Not proved:
* the bijection between skew SYT of outer/inner with max at c, and skew SYT of (outer - c)/inner;
* `inner <= outer - c` as a YoungDiagram fact (exists_max_corner supplies its content --
  c is a corner and c is outside inner -- but the diagram-level statement is not assembled);
* the sum itself, f^{lam/mu} = sum over such c of f^{(lam-c)/mu};
* and then G(mu,k), which is the easy induction on top of upSum_eq.

Revised estimate for the remainder: the erase geometry was ~90 lines of the ~440. The insert
direction and the bijection are the bulk and are untouched.

The 0-based vs 1-based trap the note flagged is real and is recorded in the file header:
skew entries are `range n`, straight entries are `Icc 1 n`.


## 2026-08-31, second tranche — erase side COMPLETE, insert side ATTEMPTED AND NOT LANDED

`QOU/Mathlib/SkewSYTMaxCorner.lean` is now 12 declarations, zero sorries, axiom-clean. Added:

    le_eraseCorner_of_notMem      inner <= outer \ c  (what makes the smaller shape well-formed)
    skewCellsOf_eraseCorner       skew(outer \ c, inner) = skew(outer, inner).erase c
    card_skewCellsOf_eraseCorner  |skew(outer \ c, inner)| + 1 = |skew(outer, inner)|
    mem_eraseCorner_of_ne         a non-corner cell of outer survives deletion
    entry_lt_card_of_pos          S.entry i j < |skew| EVERYWHERE, not only on the skew region

`skewCellsOf_eraseCorner` was written with a `c not in inner` hypothesis; the unused-variable
linter showed it does no work and it is dropped. Carrying it would have implied the identity
depends on the corner being outside inner, and whoever assembles the bijection would have
threaded a hypothesis for nothing.

## skewInsertMax: attempted, NOT landed

The definition writes down easily -- put `|skew(outer \ c, inner)|` at `c`, keep `S`
elsewhere -- and its `zeros` field goes through. `row_strict`, `col_strict` and `content` did
not. Nothing was committed with a sorry.

TWO CONCRETE OBSTACLES, so the next attempt does not rediscover them:

1. **Do not `subst` the corner equality.** `subst h : (i,j2) = c` ELIMINATES `c`, and every
   later reference to `c` in that branch then fails to elaborate. Destructure the corner as
   explicit coordinates `(p, q)` in the theorem statement and case on `i = p`/`j = q` instead.
2. **`rw [mem_eraseCorner]` does not fire** on a goal `x in eraseCorner outer c hc` -- the
   lemma's LHS is diagram membership and does not match syntactically. Apply the iff as a TERM:
   `(mem_eraseCorner outer c hc x).mpr <hx, hne>`. `mem_eraseCorner_of_ne` now packages this,
   so callers should use it rather than re-deriving.

The `content` field is the largest remaining obligation: it must show
`image entry (skew(outer,inner)) = range (N+1)` from `S.content : image = range N` plus the new
value `N` at `c`. `card_skewCellsOf_eraseCorner` supplies the cardinality half.

## Honest state of the whole route

DONE: the erase geometry, and the diagram-level facts around it.
NOT DONE: skewInsertMax, the erase/insert bijection, the branching sum itself, and G(mu,k).
The remaining work is still the bulk. Do not read 12 sorry-free declarations as the branching
rule being close -- the hard direction has not started.
