---
# qou-vud6
title: No checker reads ACROSS blocks for epistemic-status agreement — intro said 'not assumed', proof said 'is the axiom'
status: completed
type: task
priority: normal
created_at: 2026-08-15T00:23:28Z
updated_at: 2026-08-15T00:45:18Z
---


## The observed failure

In #5021 the Ch9 §1 arc shipped with two blocks disagreeing about the epistemic
status of the SAME result:

  interactions-are-pairwise-intro.md      "forced by the braiding rather than assumed"
  pairwise-interaction-decomposition-proof.md  "Part 1 is the hexagon axiom, solved for c_{X⊗Y,Z}"

Three blocks apart, in one section, contradicting each other. Nothing flagged it.
A reader on the guided path (intro → proposition) never reaches the correction.

## Why no existing checker catches it

Every status-bearing checker is PER-BLOCK: the `.qa.json` sidecar model scores a
block against its own source hashes. `conjectural-propagation-audit.ts` walks
`uses[]` for KIND propagation (conjecture → provable), which is adjacent but
different — it checks block kinds, not prose claims about provenance.

## Sketch

A checker that, for each block B and each block C in B's section or `uses[]`
cone, flags when B's prose asserts derivation of X while C's prose calls X an
axiom / definitional / assumed. High-recall + agent-confirmed, like the other
vacuity classes — the verdict is a judgement call, so it needs the review-ledger
pattern (`docs/audits/lean-vacuity-review-ledger.json`), not a hard gate.

Cheaper first cut: flag any block whose prose contains a derivation claim
("derived", "not assumed", "forced by") about a term that a block in its `uses[]`
cone marks as an axiom.
