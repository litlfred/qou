---
# qou-7vht
title: The hook length formula at general n is what blocks finrank(H_n/rad) = catalan(n+1) — NOT the Catalan combinatorics (qou-7wf6 already closed that)
status: todo
type: task
priority: normal
created_at: 2026-09-27T05:30:10Z
updated_at: 2026-09-27T08:49:31Z
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



## Item 2 LANDED 2026-09-27 — the reindexing is done; item 1 (the HLF) is the single remaining gap

`QOU/SchurWeyl/TwoRowIdxReindex.lean` on branch
claude/tl-quotient-ringcon-lift-2026-09-26 (PR #7470), commit 2190a13745.
12 declarations, sorry-free, every n. Sweep 5 ok / 0 RED / 0 TIMEOUT /
0 UNVERIFIED, SWEEP_RC=0; all 12 print [propext, Classical.choice, Quot.sound],
no sorryAx; check-sidecars clean.

**This bean STAYS OPEN** (rule 13a): item 1 is an open mathematical gap.

### What landed

    twoRowIdxEquiv (n) : TwoRowIdx n ≃ Fin ((n+1)/2 + 1)

    finrank_traceQuot_eq_range_sum :
      finrank R (H_n(q)/rad(wtrace))
        = SUM over k in Finset.range ((n+1)/2 + 1) of twoRowDim (n+1-k) k ^ 2

plus `range_sum_pos` (the sum is strictly positive, so the identity is not 0 = 0,
inherited from finrank_traceQuot_pos and thence from traceQuot_one_ne_zero).

`twoRowDim m k := if h : k <= m then numStandardYoungTableaux (twoRow m k h) else 0`
-- total in (m, k) so it can be summed over a bare Finset.range, with
`twoRowDim_eq` stripping the dite under the hypothesis.

Forward map reads off the second row; backward is `ofSecondRow`, built from
`exists_partitionShape_eq` on `twoRow (n+1-k) k`. `ofSecondRow_secondRow` is where
`partitionShape_injective` is spent, which is what makes the `choose` in
`ofSecondRow` harmless.

### Almost nothing new was needed

`eq_twoRow_of_rowLen_two_eq_zero` (MarkovConventionD:60) already says any diagram
with `rowLen 2 = 0` IS a `twoRow (rowLen 0) (rowLen 1)`; `card_twoRow`,
`rowLen_twoRow_zero`/`_one`, `partitionShape_card_succ`,
`partitionShape_injective` and `exists_partitionShape_eq` were all present. Only
two small lemmas were missing:

- `rowLen_twoRow_two` -- three lines off `mem_twoRow`; OcneanuWeightBranching stops
  at `rowLen_twoRow_one`.
- `twoRow_congr` -- `twoRow` depends only on its two row lengths. Needed because
  `rw` CANNOT rewrite inside `twoRow`'s `k <= m` argument: the motive stops being
  type correct ("motive is not type correct: fun _a => twoRow (n + 1 - _a.rowLen 1)
  (_a.rowLen 1) ... = _a"). Goes through `subst` plus proof irrelevance instead.
  Worth remembering for anything that rewrites a diagram carrying a proof argument.

### Item 1 is unchanged and is now the ONLY gap

The hook length formula at general n. `finrank_traceQuot_eq_range_sum`'s summand is
`numStandardYoungTableaux (twoRow (n+1-k) k)`, a genuine tableau COUNT;
`dimHLF_two_row_sq_sum`'s is `dimHLF [n-k, k]`, a FORMULA VALUE
(`(sz l).factorial / prodHooks l`). Frame-Robinson-Thrall bridges them and is
absent from Mathlib, proved here only for n <= 4 (`l in shapesLE4`, by decide)
plus n = 5.

**Narrowing worth recording for whoever takes item 1: the GENERAL HLF is not
needed, only the TWO-ROW case.** And `dimHLF_two_row_eq_ballot (n k) (hk : 2*k <= n)`
already identifies `dimHLF [n-k, k]` with a ballot number, so the target is

    numStandardYoungTableaux (twoRow (n-k) k) = ballot n k

i.e. two-row SYT counted by the reflection principle -- a bounded bijection
(a SYT of a two-row shape is a ballot sequence: entry i goes in row 1 or row 2),
not the general FRT theorem. That is a materially smaller target than "prove the
hook length formula", and it is the one this arc actually needs. NOT attempted here.

### 🛑 TRAP found the same pass: a cross-branch shadow olean produces a green that means nothing

I wrote this file while still on the claude/seminormal-layer-generic-field branch,
where `WtraceRadicalSemisimple.lean` DOES NOT EXIST -- and it imports that module.
**lean-direct returned RC=0 AND the sweep reported "1 ok".** Both resolved the
import to a shadow olean built from the other branch; neither checks that an
imported module has a source file on the current branch.

So `scripts/lean-library-sweep.py` guards against a STALE olean, not against an
ABSENT source. A module whose import cone exists only in another branch's shadow
verifies clean on any branch.

And the fix has a second edge: after moving the file to the right branch, the
re-run SKIPPED it, because its olean from the wrong-branch run read as
snapshot-current. The honest figure required deleting that olean from the shadow
first. Any "N ok" on a module you just moved between branches is suspect until you
evict its olean.

Second cross-branch shadow false green this session; the first was switching
branches mid-sweep, which silently swapped which files the sweep compiled.



## ITEM 1 CLOSED 2026-09-27 — and the whole chain with it. Bean STAYS OPEN; see the bottom.

Commits 588c04293b (`TwoRowSYTBallot.lean`) and fa3b78040c
(`TraceQuotCatalan.lean`) on claude/tl-quotient-ringcon-lift-2026-09-26 (PR #7470).
Sorry-free; sweeps 57 ok and 67 ok, 0 RED / 0 TIMEOUT / 0 UNVERIFIED, SWEEP_RC=0;
every declaration [propext, Classical.choice, Quot.sound], no sorryAx.

### The blocker this bean named is gone

    numSYT_twoRow_eq_ballot (m k) (h : k <= m) :
      (numStandardYoungTableaux (twoRow m k h) : Z) = ballot (m + k) k

the TWO-ROW hook length formula at general m, k. Exactly the narrowed target this
bean recorded on landing item 2, and it needed NO Frame-Robinson-Thrall in general.

### And the chain closes

    finrank_traceQuot_eq_catalan :
      (finrank R (H_n(q)/rad(wtrace)) : Z) = catalan (n + 1)

for every n, composing:

  finrank_traceQuot -> ..._eq_range_sum -> numSYT_twoRow_eq_ballot
    -> dimHLF_two_row_eq_ballot -> dimHLF_two_row_sq_sum

### Route, for whoever reads this cold: a recursion, not the textbook bijection

The corpus already had BOTH halves of a recursion and nobody had put them together:

  branching_finset (YoungLatticeUpOperator)  #SYT mu = sum over cornerCells
  ballot_succ_succ (BallotNumbers)           ballot (n+1) (j+1) = ballot n (j+1) + ballot n j

plus isCornerCell_twoRow_iff (TwoRowCorners:123), which already gave the corners of
twoRow. New: cornerTwoRow + sum_cornerTwoRow_expand (the corner analogue of the
existing addableTwoRow pattern), the two eraseCornerOrSelf identities, the three
recursion cases, the induction.

**k = m is where it could have gone wrong and did not.** There (0, m-1) is NOT a
corner -- the cell below it is present -- so one term survives, and on the ballot
side the term that must vanish is ballot (2j+1) (j+1) = ballot_boundary_zero,
already proved for a different purpose. qou-7wf6 noted one lemma resolves both
cases of ITS argument; this is a third use, in a third argument.

**Induction shape:** OUTER on k, INNER on m from k upward (Nat.le_induction). An
induction on k alone cannot work -- the k < m step needs the result at the SAME k
with a smaller m.

**Truncated subtraction was the entire difficulty.** Three failures, one cause: rw
needs a syntactic match, Lean normalises n+1-1 to n in the goal but not inside a
lemma instance, and the `k <= m` proof carried by twoRow makes the motive ill-typed
when the index is rewritten. Restating every recursion lemma in SUCCESSOR form
(k = j+1, m = M+1, no subtraction) removes all three at once.

### NOT a duplication, and the distinction is this bean's whole subject

QOU/Mathlib/SYTBranching2Row.lean already had `dimHLF_branching_pair` -- the
branching recursion for the hook-length FORMULA. What was missing is the matching
recursion for `numStandardYoungTableaux`, the genuine COUNT. The corpus has had one
side of this bridge since August. Conflating formula with count is exactly the error
retracted earlier in this PR.

### 🛑 A DIMENSION, NOT AN ISOMORPHISM -- do not over-read this

catalan (n+1) = dim TL_n(delta), so the quotient has the right dimension AND (with
traceQuotEquiv) the right Wedderburn block structure. It is NOT an isomorphism with
TL_n(delta). That needs <U_i U_j U_i - v^2 U_i> = rad(tr_M), the open item
HeckeToTemperleyLieb records, and nothing here touches it.

The content block hecke-radical-is-temperley-lieb's sentence -- "a count of blocks
and a count of dimensions are not an isomorphism of algebras" -- REMAINS TRUE. What
is gone is the dimension OBSTRUCTION: the two sides were a count and a formula with
no bridge, and now they agree for every n.

### WHY THIS BEAN STAYS OPEN

Its titled subject is closed, but it carries two recorded findings that are NOT,
both owner decisions, and closing the bean would bury them:

1. `QOU/Mathlib/TwoRowDimCatalan.lean`'s docstring calls dimHLF_two_row_sq_sum "a
   statement about actual standard-Young-tableau counts". **That over-claim is now
   REPAIRABLE rather than merely flaggable** -- numSYT_twoRow_eq_ballot supplies
   exactly the missing identification, so the sentence could be made true by citing
   it instead of scoped down. Still outside PR #7470's tranche; still ask-first.
2. `TemperleyLiebWedderburn.lean:69` pairs key jones1985 with jones1987's DOI, and
   jones1987 -- the Annals paper holding the TL-quotient + Markov-trace
   construction -- carries no `library:` field, i.e. is not ingested.


## 2026-09-27 — ITEM 1's residual over-claim is now REPAIRED, not scoped. Bean still open on item 2.

Commit bca720d676 on claude/two-row-count-eq-dimhlf-2026-09-27 (PR #7481).

This bean's item 1 recorded that `QOU/Mathlib/TwoRowDimCatalan.lean`'s docstring
calls `dimHLF_two_row_sq_sum` "a statement about actual standard-Young-tableau
counts", and noted the over-claim had become REPAIRABLE rather than merely
flaggable once `numSYT_twoRow_eq_ballot` landed. That repair is done.

The missing tie, now proved:

    numSYT_twoRow_eq_dimHLF (m k) (h : k <= m) :
      (numStandardYoungTableaux (twoRow m k h) : Z) = (dimHLF [m, k] : N)

sorry-free, general m and k, [propext, Classical.choice, Quot.sound], no sorryAx.
Four lines: compose `dimHLF_two_row_eq_ballot` (August, formula <-> ballot) with
`numSYT_twoRow_eq_ballot` (#7470, count <-> ballot), taking n = m + k so that
n - k = m and 2k <= n reduces to k <= m. NO Frame-Robinson-Thrall, which stays
absent from Mathlib and proved here only for n <= 4 (decide) plus n = 5.

Placed in TwoRowSYTBallot.lean, which already owns the count<->ballot half; that
file gains `import QOU.Mathlib.TwoRowDimCatalan`. No cycle -- TwoRowDimCatalan
imports only BallotNumbers + SYTBranching2Row, neither of which reaches back.

### A total-function wrapper was deliberately NOT added

The tempting stronger form is a sum-of-squares over actual counts, which needs a
total `(m,k) -> count`. `twoRowDim` already is one, and reusing it would have been
WRONG here: it lives in QOU.SchurWeyl.TwoRowIdxReindex, which imports
WtraceRadicalSemisimple and so pulls R into a purely combinatorial statement.
Duplicating it in the Mathlib layer would put two spellings of one notion in the
corpus. The single bridging theorem needs neither, and check-sidecars confirms
both touched files remain "no R, generic OK".

### The docstring says MORE than it used to, not less

It now states the formula-vs-count distinction explicitly, cites the theorem, and
records that the counts reading is a COMPOSITION rather than something that file
proves. The old sentence's actual failure mode was inviting a reader to take the
counts reading as TwoRowDimCatalan's own result; scoping the sentence down would
have removed the claim but not that misreading.

### Scope

Exemption 2 of the 2026-09-07 ask-first override: the corpus fixes the answer (a
sorry-free theorem on main), so a reviewer checks the edit against that artifact
rather than against my reasoning. Two files, one theorem, one docstring -- not a
sweep.

### THIS BEAN STAYS OPEN (rule 13a)

Item 2 is untouched and is an owner judgement: TemperleyLiebWedderburn.lean:69
pairs key jones1985 with jones1987's DOI (10.2307/1971403) -- two different papers
(references.ts :3059 vs :2187) -- and jones1987, the Annals paper carrying the
TL-quotient + Markov-trace construction, has NO `library:` field, i.e. is not
ingested. Subject matter wants jones1987, but which half is the typo is not mine
to decide, and the ingestion is a separate uploads/ -> library/ step.
