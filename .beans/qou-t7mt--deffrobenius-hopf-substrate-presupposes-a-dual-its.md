---
# qou-t7mt
title: def:frobenius-hopf-substrate presupposes A-dual; its own Lean needs only MonoidalCategory
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T00:54:20Z
updated_at: 2026-08-16T10:30:37Z
---


## The mismatch

`def:frobenius-hopf-substrate` opens *"Let **C** be a rigid monoidal category"*,
and its axioms 4–5 phrase non-degeneracy as *"the induced map A → A^∨ is an
isomorphism"* / *"identifies A with its dual A^∨"*. That notation presupposes
`A^∨` exists, which is why the prose reaches for rigidity.

Its own Lean encoding does not. `FrobeniusHopfData` is declared over

    (C : Type u) [Category.{v} C] [MonoidalCategory C]

with **no** rigidity, and encodes non-degeneracy via `coevaluation` + the two
snake identities — which *construct* the self-duality of `A` rather than
presupposing an ambient dual. That is strictly weaker and is the reason axiom 3
(symmetric Frobenius) could stay at QU level after rigidity moved to the QOU
in #5021: the traces come from `A`'s own form, not from duals on **C**.

## Why this is not fixed unilaterally

Rewording axioms 4–5 changes what a *definition* says, and downstream blocks
cite it. The prose is not wrong — it is stronger than necessary. Options:

1. Weaken to "monoidal" and restate 4–5 via coev + snake, matching the Lean.
   Cleanest, and makes the substrate available at QU level as the Lean already
   assumes.
2. Weaken to "**C** monoidal with `A` dualizable" — smaller edit, keeps `A^∨`
   notation.
3. Leave as is and note that the substrate is a QOU-level object.

Author decision. Surfaced by the `qou-5r17` audit sweep for blocks asserting
**C** is rigid after #5021 relocated rigidity.

## Cleared in the same sweep (not defects)

- `hadron-operations-closure`, `categorical-linking-operation`,
  `categorical-neutrality-saturated-shells` — each states rigidity as its own
  hypothesis, and each is knot-closure work that genuinely needs duals.
- `q-dilogarithm-pentagon-associator` — its *"forced by the monoidal axioms"*
  claim is **earned**: `def:q-dilogarithm` establishes "the unique level-2
  primitive normalised by the pentagon relation", and the block self-hedges that
  the monodromy datum "remains open". Only the stray word *rigid* was wrong
  (pentagon coherence is a monoidal axiom); fixed in place.

QUEUED-BLOCKED 2026-08-15 (session qou-pq8k): not agent-actionable — the bean itself says 'Author decision' between three rewordings of def:frobenius-hopf-substrate axioms 4-5. Needs owner pick, not agent work.
