---
# qou-ngac
title: 'Conjecture: motivic_perpetual_obstruction'
status: completed
type: task
priority: normal
created_at: 2026-08-10T20:02:49Z
updated_at: 2026-08-22T21:33:09Z
---

lifting-and-descent/motivic-perpetual-obstruction.lean: genuinely open conjecture.


## Closed 2026-08-22 — the file was right, the conclusion was not

This bean reads: *"lifting-and-descent/motivic-perpetual-obstruction.lean:
genuinely open conjecture."* The file did contain a `sorry`. But the block's
`lean.ref` was meant for
`lean/QOU/LiftingDescent/MotivicPerpetualObstruction.lean`, which proves it
sorry-free (`#print axioms` -> propext / Classical.choice / Quot.sound, no
`sorryAx`); the sibling was a **shadowing stub** carrying a superseded
two-parameter signature, and AGENTS.md §0a forbids keeping one when the real
formalisation exists.

Deleted in PR #5502, along with completing the `conj:` -> `thm:` rename the
owner's `1d3988bc31` had half-applied.

**Scope, so nobody over-reads this.** The theorem is *conditional*: it takes
the trace-growth bound as an explicit hypothesis. The empty-exception-set form
is discharged only for the concrete QOU instances (proton C=4, deuteron
C=-32). "Proved" here means the implication, not the premise.

Duplicate-in-substance of `qou-a5dr`, closed together.
