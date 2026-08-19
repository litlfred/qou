---
# qou-yq50
title: 'Content blocks for the 5_2 lane: ~180 probes + 34 Lean files have no narrative face in the paper'
status: todo
type: task
created_at: 2026-08-19T07:22:26Z
updated_at: 2026-08-19T07:22:26Z
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
