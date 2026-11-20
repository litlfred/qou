---
# qou-yq50
title: 'Content blocks for the 5_2 lane: ~180 probes + 34 Lean files have no narrative face in the paper'
status: todo
pr: 8289
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T07:22:26Z
updated_at: 2026-11-20T16:06:50Z
parent: b9cj
---


## Tranche 1 landed — three blocks in appendix-qvalues

The 5_2 lane had ~180 probes and 33 sorry-free Lean files and NO narrative face
anywhere in `content/`. First three blocks, chosen so each is backed by a
declaration that actually exists rather than by prose:

1. `prop:fivetwo-trace-field` -> `QOU.QBeta.FiveTwo.disc_eq_neg_23`.
   The saddle cubic's discriminant is -23, stated over a generic `CommRing`
   with the Vieta relations as hypotheses (§7c-clean: no ordering, no radical).
   Carries the corrected field, the Q(sqrt-23) resolvent, and the det(5_2)=7
   Alexander-layer distinction.
2. `prop:fivetwo-saddle-sum-rule` ->
   `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`.
   The dilogarithm trace over all three shapes closes to
   -pi^2/6 - (1/2)log^2 t + (2/3)(arg a - pi)^2. Sorry-free, and the existence
   quantifier is DISCHARGED (`SaddleRoots.ofRealRoot`, via IVT) rather than
   assumed.
3. `rem:fivetwo-bar-odd-arithmetic-home` (interprets block 1). Why the odd
   channel is confined to the sqrt(-23) line, why the question is asked on
   chiral 5_2 rather than amphichiral 4_1, and the qou-ynff retraction carried
   forward into the paper.

## Two things checked rather than asserted

- **The 2/3 in the sum rule.** I first wrote "forced by the pentagon and
  reflection identities" from the filenames. Wrong shape. Read the Lean: it
  descends from the branch relation `2*l_j - 3*m_j = 2*pi*i*eps_j` that the
  gluing equation `y^2 = (1-y)^3` imposes -- the 2 and 3 ARE the gluing
  exponents. Corrected before commit.
- **The sorry counts.** All 33 `FiveTwo*.lean` files scan as having `sorry`
  occurrences; every one is a docstring ASSERTING sorry-freeness. No actual
  `sorry` terms. Verified with both a strict and a loose pattern.

## Scope discipline in the blocks

Both propositions carry an explicit caveat naming what the Lean does NOT
discharge: for block 1, the S_3/A_3 Galois argument and the tower-law exclusion
are prose, not Lean; for block 2, the identity is bar-EVEN and supplies no
bar-odd action value. That second one matters -- the lane exists to chase the
bar-odd channel, and a strong bar-even result is exactly the kind of thing that
gets cited as progress on it.

## Next tranche candidates

The Stokes/DT-spectrum files (`FiveTwoStokesMatrixIdentities`,
`FiveTwoDTSpectrumSplit`), the level-seven ladder, and the Rogers/pentagon
machinery are all sorry-free and unnarrated.

## Tranche 2 — the chirality pair (2 blocks)

1. `prop:fivetwo-dt-spectrum-split` ->
   `QOU.QBeta.FiveTwoDTSpectrumSplit.symmetric_scalar_blind_to_chirality`.
   The DT spectrum {3,4} splits across chirality (4 in S+, 3 in S-), and NO
   tau-symmetric integer reading can recover the ordered datum -- universally
   quantified over g, so a structural exclusion rather than a failed search.
   Positively: the DT count is a bar-graded object; "no scalar serves the
   datum" and "the bar-odd part is nonzero" are the same statement. Includes
   the 4_1 contrast, which is the point: amphichirality collapses all four
   readings to 3, chirality separates them.

2. `prop:fivetwo-stokes-unimodular` ->
   `QOU.QBeta.FiveTwoStokes.Splus0_transpose_mul_Sminus0`.
   det S+(0) = det S-(0) = 1, (S+)^T S- = I to four orders, det W_{-1}(0) = -2.

## The trap I nearly walked into

`chirality_sum_seven` proves dt+ + dt- = 7. det(5_2) = 7. Those are different
sevens, and the temptation to link them is exactly the conflation that produced
the retracted 2026-07-18 audit (qou-ynff) in THIS lane. Checked the Lean before
writing: it uses the 7 only as one of four DISTINCT readings in
`readings_all_distinct` and makes no identification with the determinant. The
block now says so explicitly, so the next reader does not make the leap.

## Second correction carried into the paper

det W_{-1}(0) = **-2**, not +2. The matrix carries denominators of 6 from the
c-slot subtraction, so it is rational and the sign is real; an earlier framing
assumed a fitted integer +2. Recorded in the block rather than silently fixed,
because the "det +-2 phenomenon" is cited elsewhere.

## Authoring notes for the next tranche

- Convention check before writing math: `pmatrix` is used 176x in content .md
  vs `psmallmatrix` 4x -- use pmatrix. Markdown tables live in dedicated
  `<block>-table1-data.md` blocks, NOT inline in prose blocks; I converted a
  table to prose rather than risk it.
- `qa-sweep` lives in the folio-assistant clone after miga:
  `bun run folio-assistant/content/pipeline/qa-sweep.ts <block-path>`.

## Tranche 3 — the level-seven ladder, and the three sevens (2 blocks)

1. `prop:fivetwo-level-seven-ladder` ->
   `QOU.QBeta.FiveTwoLevelSevenLadder.sum_of_numerators`. Three five-term
   instances give the three Q(zeta_7)^+ numerators m = (17,5,-1); the 7 comes
   from the quadratic residues {1,2,4} mod 7 acting on the three real
   conjugates. `L` abstract, generic CommRing. Conditional on its hypotheses,
   which are NOT proved there (five-term, Landen, Route 8 transport).

2. `rem:fivetwo-three-sevens` (interprets the trace-field block). The reusable
   lesson of this whole arc.

## THREE distinct sevens, measured

| seven | layer | field |
|---|---|---|
| det(5_2) = 7 | abelian / Alexander | Q(sqrt-7) |
| dt+ + dt- = 7 | tau-even Stokes sum | none claimed |
| level 7 | cyclotomic | Q(zeta_7)^+ |

and the trace field is a FOURTH object (cubic, disc -23).

## The near-miss that makes a bare degree check insufficient

Computed rather than recalled:

    Q(zeta_7)^+ : x^3 - 2x^2 -  x + 1,  disc  49, totally real, CYCLIC
    trace field : x^3 - 2x^2 + 3x - 1,  disc -23, one real place, S_3

**Both cubic. Both minimal polynomials open `x^3 - 2x^2`.** Different fields.
So matching degree AND matching leading coefficients is worth nothing — which
is the sharper form of the qou-5gh6 lesson (where my own degree heuristic was
the over-claim). A degree check rules things OUT (tower law); it never rules
anything IN.

## An authoring pattern worth keeping

`char_seven_forces`: the ladder is stated CLEARED (7T = ...) not divided. Not
timidity about 7^-1 -- in characteristic 7 the hypotheses FORCE 3*L1 = 0, so
L1 = 0 and every target degenerates to 0 = 0. The divided form would be vacuous
exactly where it could not be stated. Clear the denominator; let the content sit
where the denominator is invertible.

## Tranche 4 — the envelope transport (1 block)

`prop:fivetwo-envelope-transport` ->
`QOU.QBeta.FiveTwoDeformedSaddle.envelopeS_total` (in FiveTwoTransport.lean --
note file name != namespace).

S(pi) - S(0) = pi^2, given continuity on [0,pi] and dS/dphi = 2phi off ONE
exceptional point (phi_0, where the discriminant vanishes, two root branches
collide, and no differentiable labelling exists through it).

## Two things worth having in the paper

1. **Why one exceptional point is not a fudge.** S is a SYMMETRIC function of
   the roots, so as a function of phi it needs no labelling at all -- well
   defined and continuous across phi_0 precisely where the branches swap. The
   labelling is needed only to differentiate term by term, a local operation.
   Reusable and not specific to 5_2: a symmetric function of a family of roots
   is insensitive to the monodromy that permutes them, so an obstruction to
   labelling the branches is NOT an obstruction to the symmetric total.

2. **Non-vacuity is PROVED.** `envelopeS_total_nonvacuous` exhibits
   S(phi) = phi^2 satisfying both hypotheses. Deliberately trivial -- it exists
   to rule out the vacuous reading, not to supply evidence, and the file says
   so. Good authoring practice and the honest counterpart to the AGENTS.md
   anti-vacuity discipline; worth copying.

## Scope carried into the block

The derivative is a HYPOTHESIS. What is formalised is the integration step
(hypothesis -> total pi^2, tolerating one exceptional point), NOT the
identification of the integrand. That identification is numerical (Route 30:
S' = 2phi per root to 4.6e-41, summed 9.2e-41) and is not formalised.

## Arc status: 8 blocks

trace-field, saddle-sum-rule, bar-odd-arithmetic-home, dt-spectrum-split,
stokes-unimodular, level-seven-ladder, three-sevens, envelope-transport.

Remaining sorry-free and unnarrated: FiveTwoRootStructure (26 thms),
FiveTwoDiscriminant, FiveTwoRogersReflection/RogersExtend, the pentagon
machinery (FiveTwoComplexPentagon has 119 decls but its headline is already
narrated as the sum rule), FiveTwoCyclotomicBloch, the Envelope* family,
FiveTwoBranch*/ArgSector/CutAvoidance (branch bookkeeping -- mostly
infrastructure rather than results).

HONEST ASSESSMENT: the high-value surface is largely covered. What remains is
mostly (a) infrastructure lemmas whose narrative face is already carried by the
results they support, and (b) FiveTwoRootStructure/Discriminant, which are the
root-existence and discriminant plumbing under the trace-field block. A tranche
5 would be real but thinner than 1-4.

## Tranche 5 — and I was WRONG that it would be thin

I predicted tranche 5 would be "real but noticeably thinner than 1-4". On
`FiveTwoDiscriminant` that was wrong, and the file is arguably the most
instructive of the eight.

`prop:fivetwo-discriminant-vanishes` ->
`QOU.QBeta.FiveTwoDiscriminant.exists_unit_circle_disc_zero`.

It is a REFUTATION. The transport argument had recorded a sub-gap closed on

    "the three branches never collide on the arc (min |disc| = 0.348)"

and stated the envelope theorem's implicit-function hypothesis as satisfied on
the same constant. Both false. 0.348 was a GRID minimum from a ~360-point scan;
the dip is narrow (|disc'| ~ 87) so refinement gives 0.068, 0.0068, 0.

**A minimum over samples bounds the samples, not the function** -- and that
constant had been carried into a proof step.

The refutation is short: disc is palindromic, so disc x = x^4 Q(x + 1/x) with
Q u = u^4 - 6u^3 + 7u^2 + 6u - 31; Q(-2) = 49 > 0 > -23 = Q(-1) gives an IVT
root at u ~ -1.4844, and |x|=1 is exactly x + 1/x real in [-2,2] which contains
(-2,-1). Verified the Q values and the root independently.

Conclusion survives, argument dies: S is symmetric over all roots, a collision
permutes them, and a symmetric function cannot notice a permutation. This is
WHY tranche 4's envelope block tolerates one exceptional point -- the tolerance
is the shape of the situation, not a hedge. The two blocks complete each other.

## Two -23s, separated

disc(1) = -23 IS the trace-field discriminant (at x=1 the curve degenerates to
the saddle cubic, `ggm_one`). Q(-1) = -23 is a COINCIDENCE -- Q takes that value
at u = -1, 1 and 2 alike, and only u=2 corresponds to x=1. Separated in the
block, per rem:fivetwo-three-sevens.

## Nine blocks. Remaining is now genuinely thin

FiveTwoRootStructure (the IVT root existence feeding the branch pinning) is real
but is infrastructure under the discriminant/envelope pair. The Rogers/pentagon
and Branch*/ArgSector/CutAvoidance families are bookkeeping whose narrative face
is carried by the results above.

## Round 57 Implementation Progress (PR #8289)
- **Status:** `in-progress` (per no-unilateral-closure policy)
- **PR:** https://github.com/litlfred/qou/pull/8289 (head `b1d29c3ac9e8ff1013e87a6f368591fb977a1ff3`, Commit 1 `85cf34f4dd33fa831b7480e3f2c9e1ff2e2f5c6d`)
- **Lean 4 Module & Theorems:** `QOU/AlphaEM/FiveTwoDiscriminantGluingAndHabiroDilogLadder.lean` (`five_two_cubic_discriminant_neg23_and_gluing_invariance`)
- **80-dps Witness:** `computations/probes/round57-fivetwo-discriminant-habiro-dilog-dglz-pentagon.witness.json` (`scriptHash: 3ee733fedb99`, `allPassed: true`, `0` raw `float64`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8289, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
