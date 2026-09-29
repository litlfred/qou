---
# qou-0ubf
title: 'Session: P≠NP gap inventory refresh — re-measure the cluster against main, correct the stale 2026-07-25 semisimplicity row'
status: in-progress
type: epic
priority: normal
created_at: 2026-08-29T16:32:33Z
updated_at: 2026-08-29T16:33:12Z
---

## Finding: the standing plan points at the wrong build

Re-measured on `main` @ `df81b22be4`. Two corrections to the 2026-07-25 status audit,
now written into that file as a 🛑 note and consolidated in
`docs/audits/2026-08-29-pneqnp-gap-inventory-refresh.md`.

1. **The rank ladder went past n=2.** `HeckeH3Semisimple.lean` and
   `HeckeH4Semisimple.lean` both prove `IsSemisimpleRing` at their rank by
   transport along an explicit Wedderburn iso. H4 is **det-free** — the 24x24 Gram
   det is sympy-verified but Lean-out-of-reach — so the rung was reached WITHOUT
   the determinant §5 item 1 tells you to go get.

2. **The general-n gap is no longer the T_w basis.**
   `WenzlSchurElement.semisimple_of_substrate` gives semisimplicity at EVERY rank
   for Q>1, X<=0, and its Schur-element leg is computed: `schurElement_ne_zero`
   (line 231) is sorry-free with hypotheses `1 < Q` and `X <= 0` only — no class.

**NOT a discharge.** `semisimple_of_substrate` carries `[SchurElementCriterion]`,
itself instance-free, and per the 2026-08-21 audit that class and `WenzlCriterion`
state the same literature theorem from two angles. Citation COUNT unchanged; what
changed is that one feeding leg is proved for all n, so the residual is one named
theorem (Geck-Pfeiffer 7.2.6 = bean qou-0y6h) rather than a missing basis theory.

## Also measured

- Whole cone (Information/ Hecke/ MathlibExt/) is **sorry-free in code** — every
  `sorry` hit is a docstring.
- **All 16 conjecture carriers instance-free** — nothing laundered:
  QouPNeqNp, TraceFaithfulness, JetHorizonTransfer, ComplexityDictionary,
  WenzlCriterion, SchurElementCriterion, JonesComplexityCitations,
  ResidueFaithfulness, QouGCTObstruction, QOUTraceCountHard, PhotonicDecisionHard,
  MatchingFacts, CitedComplexity, QOUObstruction, IsOcneanuWeightSystem,
  WedderburnDecomp.

## Chippable, ranked (none crosses the wall)

1. `qou-0y6h` Geck-Pfeiffer det(Gram)=prod Schur — highest value, and CLOSER than
   the plan says because the Schur half is already proved for all n.
2. `qou-z0pr` wire proved n=2/3/4 semisimplicity into PNeqNpEquivalence — small,
   mechanical, currently not done.
3. `qou-h56b` WedderburnDecomp* name collision; the middle one has Prop-VARIABLE
   fields + a global trivial instance = live vacuity hazard found by TC search.
4. `qou-fpjy` `#print axioms` cannot see the Wenzl dependency — so 'no sorryAx
   therefore unconditional' is UNSOUND in this cluster. Worth a guard.
5. TL_n build item 1 (A_n presents S_n) — worthwhile as a Mathlib contribution,
   but NO LONGER P!=NP critical path.

## Unchanged

The wall (TraceFaithfulness / JetHorizonTransfer.transfer) is the Millennium
problem: refuted as a generic law (generic_transfer_false), blocked as uniform
(Razborov-Rudich), barred by algebrization (Aaronson-Wigderson). Do not fabricate.
