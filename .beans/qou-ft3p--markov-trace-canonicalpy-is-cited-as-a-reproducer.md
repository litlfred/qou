---
# qou-ft3p
title: markov_trace_canonical.py is cited as a reproducer but emits no witness
status: todo
type: task
created_at: 2026-08-15T20:40:26Z
updated_at: 2026-08-15T20:40:26Z
---


## What

`prf:categorical-mass-markov` tells the reader, in prose, how to reproduce its
convention C-vs-D comparison table:

> Reproduce with `python3 computations/markov/markov_trace_canonical.py`, whose
> prop-table check now gates at $10^{-40}$ rather than $10^{-9}$.

That script exists and has no `WitnessBuilder` — **it emits no witness.** So a
block that cites a reproducer has nothing it can put in `computation.witness`,
and its nine quoted values are traceable only by coincidence: they happen to
appear in `alpha-k-jones-markov-h3.witness.json`, `gram-matrix-dual.witness.json`
and others, which are not what the block is citing.

Found by `content/pipeline/witness-substitution-audit.ts --suggest` while
triaging the 190 `no-witness-declared` blocks (`qou-a28x`). It is the reason
"under-declared" and "declarable" had to be separated: this block is
under-declared and cannot be fixed by declaring anything.

## Why it matters beyond one block

A script cited as authoritative but emitting no witness is unfalsifiable by the
pipeline. The prose says its check "gates at 1e-40" — nothing records that it
ran, what it produced, or against which q0. The gate is real inside the script
and invisible outside it.

## Next

1. Add a `WitnessBuilder` to `markov_trace_canonical.py` recording the prop
   table (the C and D columns, the 4_1 closed form) and its tolerance.
2. Declare it on `prf:categorical-mass-markov`.
3. Then the block's nine literals become traceable to the thing it actually
   cites, rather than to unrelated files that share decimals.

Related: `qou-a28x` (the axis and the triage), `qou-2ixd` (the convention arc
that surfaced the table).
