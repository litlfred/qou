---
# qou-7vht
title: The hook length formula at general n is what blocks finrank(H_n/rad) = catalan(n+1) — NOT the Catalan combinatorics (qou-7wf6 already closed that)
status: todo
type: task
priority: normal
created_at: 2026-09-27T05:30:10Z
updated_at: 2026-09-27T05:30:10Z
parent: qou-weeq
---

Found while extending PR #7470 (branch claude/tl-quotient-ringcon-lift-2026-09-26).
Nothing here is blocked on an owner decision; it is a measurement plus one
flagged-not-edited over-claim in a file outside that tranche.

## The chain, and where it actually stops

`WtraceRadicalSemisimple.finrank_traceQuot` (new, sorry-free, general n) gives

    finrank R (H_n(q)/rad(wtrace)) = SUM over lam in TwoRowIdx n of
                                     Fintype.card (StandardYoungTableau (partitionShape lam))^2

`TL_n(delta)` has dimension `catalan (n+1)`, so the dimension match a TL
identification needs is this sum against the Catalan number.

## What is NOT the blocker (I claimed it was, and retracted it)

The Catalan identity `SUM_{l(lam) <= 2} (f^lam)^2 = catalan n` IS PROVED AT
GENERAL n, sorry-free, since 2026-08-21:

  - `QOU.Mathlib.ballot_sq_sum_catalan` (QOU/Mathlib/BallotNumbers.lean:438) --
    reflection + Vandermonde, no induction, no tableau
  - `QOU.Mathlib.dimHLF_two_row_sq_sum` (QOU/Mathlib/TwoRowDimCatalan.lean:103)

Bean qou-7wf6, PR #5360, which closed qou-0cyu item G5.

I first wrote in a docstring that this identity was "proved nowhere in this corpus
at general n", citing `TemperleyLiebNormalForm.card_zero .. card_six` as decide at
seven values. Those seven are a DIFFERENT IDENTITY -- the planar-DIAGRAM count
`Fintype.card (NormalIdx m) = catalan (m+1)`. Retracted in f54b280e49.

## What IS the blocker: the hook length formula at general n

`dimHLF l := (sz l).factorial / prodHooks l`
(QOU/BraidKnot/IdentityIContentDecomposition.lean:948) is the hook-length
FORMULA. `finrank_traceQuot` counts `Fintype.card (StandardYoungTableau ...)`.
Identifying the two is Frame-Robinson-Thrall, and:

  - it is ABSENT FROM MATHLIB entirely. `Mathlib/Combinatorics/Young/*.lean`
    carries no hook length formula and not even `numStandardYoungTableaux` --
    that is a corpus definition.
  - in this corpus it is proved only for n <= 4:
    `QOU.Mathlib.SYTEnum.numStandardYoungTableaux_eq_dimHLF_le4`
    (QOU/Mathlib/SYTHookFormula.lean:37), whose hypothesis is literally
    `hmem : l in shapesLE4`, discharged by decide. Plus n = 5 in
    `QOU.Mathlib.SYTFrobeniusDim` (dimHLF_eq_frobeniusDim_5).

So the residue between `finrank_traceQuot` and `catalan (n+1)` is:

  1. HLF at general n -- research-grade, absent from Mathlib. THE gap.
  2. a reindexing of `TwoRowIdx n` (partitions of n+1 with rowLen 2 = 0) by
     second-row length, to meet `dimHLF_two_row_sq_sum`'s
     `SUM over k in Finset.range (n / 2 + 1)`. Bounded finite combinatorics.

Item 2 is worth doing on its own: it is cheap and it makes item 1 the single
named blocker rather than one of two.

## FLAGGED, NOT EDITED -- an over-claim in TwoRowDimCatalan

`QOU/Mathlib/TwoRowDimCatalan.lean`'s module docstring (line ~19) describes
`dimHLF_two_row_sq_sum` as

  "a statement about *actual standard-Young-tableau counts*, not about binomial
   coefficients. That is the form the Wedderburn accounting needs."

Under `dimHLF`'s definition that is an over-claim AT GENERAL n: it is a statement
about hook-length-formula VALUES, and their identification with actual counts is
exactly the n <= 4 bridge above. The second sentence is the consequential half --
the Wedderburn accounting needs genuine counts, and at general n this does not
supply them.

Left unedited deliberately: that file is not in PR #7470's tranche and the
2026-09-07 ask-first directive applies. It is a one-paragraph scoping fix, not a
retraction -- the theorem is correct as stated.

## A separate, unrelated citation defect found the same pass

`QOU/MathlibExt/TemperleyLiebWedderburn.lean:69` reads

    -- Ref: [jones1985] https://doi.org/10.2307/1971403

and the key and the DOI name DIFFERENT PAPERS. Measured in
content/schema/references.ts: `jones1985` is at :3059, "A polynomial invariant
for knots via von Neumann algebras" (Bull. AMS), ingested at
library/s0273-0979-1985-15304-2. DOI 10.2307/1971403 is at :2187 and belongs to
`jones1987`, "Hecke algebra representations of braid groups and link
polynomials" (Annals 126).

Subject-matter-wise the file (Wedderburn of TL_2/TL_3 via the Markov trace) wants
jones1987, so the DOI looks right and the key looks like the typo -- but that is
a judgement about what the author meant, not a corpus-derived fact, so it is NOT
fixed here. Two consistent repairs exist and choosing between them is a one-line
owner call. Note also that jones1987 carries no `library:` field, i.e. the Annals
paper containing the construction is NOT INGESTED -- a real gap on this arc's
critical path, since it is the primary source for the TL quotient + Markov trace.
