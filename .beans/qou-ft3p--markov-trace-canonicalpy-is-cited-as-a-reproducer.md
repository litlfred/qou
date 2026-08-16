---
# qou-ft3p
title: markov_trace_canonical.py is cited as a reproducer but emits no witness
status: completed
type: task
priority: normal
created_at: 2026-08-15T20:40:26Z
updated_at: 2026-08-16T10:38:28Z
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

## Done

`markov_trace_canonical.py` now emits `markov-trace-canonical.witness.json` —
6 assertions at `1e-40`, all passing, plus `q0`, `z`, `h` and the figure-8
value symbolic and numeric.

Two other defects surfaced while adding it:

1. **The 1e-40 gate did not gate.** The prop table printed a tick/cross column
   and the script exited 0 regardless, so a convention flip would have shown as
   a row of crosses that nothing acted on — the same "a check that cannot fail
   is not a check" shape as `markov_trace_recursive`. Now `SystemExit(1)` on any
   failure.
2. **A stale convention-C annotation, inside the script cited as the
   reproducer.** The figure-8 line printed
   `(prop says ~ 0.182)` while computing `0.280195642272695`. `0.182304485938`
   is the **C** column of the very table this script reproduces; `0.280195642273`
   is the D column. The annotation stayed on C when the computation moved to D.

Declared on `prf:categorical-mass-markov`. Axis result for that block:
**4 unsourced-literal -> 0, no-witness-declared -> 0.**

The four that had remained were exactly the convention-C column, which is
correct — C is excised, nothing computes it, and no witness can carry it. That
column is now marked `<!-- literal-source: C column is preserved history, no
producer (qou-ft3p) -->` with the reasoning in the prose beside it.

Note on the marker: the first version ran to ~430 characters and did NOT
suppress the later table rows, because `MARKER_WINDOW` is 400 characters and
the check looks for the marker's OPENING within that span. Shortened the marker
and moved the explanation into the prose rather than widening the window — the
window is a deliberate scope line, not an accident.


---

## Summary of Changes (completed 2026-08-16)

`computations/markov/markov_trace_canonical.py` is cited **by name** in
`prf:categorical-mass-markov` as the way to reproduce its table, and emitted no
witness — so the block had nothing to put in `computation.witness`, and its nine
quoted values were traceable only by coincidence (they matched decimals in
`alpha-k-jones-markov-h3` and `gram-matrix-dual`, neither of which the block
cites). A script cited as authoritative while emitting nothing is unfalsifiable
by the pipeline: the 1e-40 gate was real inside the file and invisible outside it.

Done:
- `WitnessBuilder("markov-trace-canonical", engine="sympy")`, emitting
  `computations/markov/markov-trace-canonical.witness.json`, declared at
  `categorical-mass-markov-proof.ts:16`.
- Six prop-table assertions at 1e-40 — chosen over 1e-9 because at 50 dps a 1e-9
  gate would pass both a convention flip (C vs D differ by 0.11 on z) and an f64
  regression.
- `raise SystemExit(1 if failures else 0)`. It previously printed a tick column
  and exited 0 regardless, so a convention flip would have shown as a row of
  crosses that nothing acted on.
- Fixed a stale annotation while there: the figure-8 line read *"prop says
  ~0.182"*, which is the **convention-C** column of that same table. Under D the
  value is 0.280195642273. The annotation had stayed on C when the computation
  moved to D — the exact stale-annotation failure the table documents.

Verified: witness present (2481 bytes), declared in the block, producer carries
builder + assertions + exit gate. `engine` is `sympy`, not `mpmath+sympy`, which
`content_validate` rejected as outside the schema enum.
