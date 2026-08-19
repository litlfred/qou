---
# qou-4lft
title: 'SW-10: the root-of-unity regime — H_n(q) at q^2 = 1, where seminormal form fails'
status: todo
type: task
priority: normal
created_at: 2026-08-19T13:43:42Z
updated_at: 2026-08-19T13:44:28Z
parent: qou-59vq
---

## Why this exists

Every general-lambda result in the SchurWeyl tree carries `q != 0` and `q^2 != 1`
— over R exactly *q is not a root of unity*, the genericity [ram1997] and
[hoefsmit1974] presuppose. Filed 2026-08-19 when #5290 (`qou-t8qh`) closed the
last sorry in the tree, so that the excluded regime is a tracked item rather
than an unremarked hypothesis.

## This is NOT a hypothesis to relax by a better proof

At a root of unity the statements do not merely become harder — they become
FALSE in their current shape:

- `H_n(q)` is no longer semisimple, so there is no Wedderburn iso to
  `(+)_lambda M_{d_lambda}`.
- The partitions lambda |- n no longer index the irreducibles.
- `seminormalParam q d = (q - q^-1)/(1 - q^{-2d})` has a ZERO denominator
  whenever q^{2d} = 1, so the seminormal matrices do not exist at all; at
  q = -1 with even d it is 0/0.
- `Theta = barSymJMSum` acting by a scalar on a d_lambda-dimensional block is
  exactly the shape that fails.

The honest framing is therefore **a different statement for a different
regime**, via cellular / Specht theory (Graham-Lehrer, Dipper-James) rather
than seminormal form — cell modules exist at every q; irreducibility is
replaced by the radical quotient of the cellular bilinear form, and the
irreducibles are indexed by e-regular partitions where e = ord(q^2).

## Prerequisite check before anyone starts

Corpus-grep first: `SpechtStandardBasisCore.lean` and
`SpechtWedderburnCriterion.lean` under BraidKnot are substantial and may
already carry the cellular-side infrastructure this needs. Nothing should be
built here before that is measured.

## Priority

LOW for the QOU program. The physics evaluates at the substrate q0 ~ 1.10998,
which is not a root of unity, so nothing downstream is blocked by this. It is
filed for completeness of the mathematical arc, and because leaving an excluded
regime unnamed is how a hypothesis quietly becomes an assumption.
