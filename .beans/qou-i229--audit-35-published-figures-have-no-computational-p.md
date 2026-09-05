---
# qou-i229
title: 'AUDIT: 35 published figures have no computational provenance anywhere in the repo'
status: todo
type: task
created_at: 2026-09-05T12:58:18Z
updated_at: 2026-09-05T12:58:18Z
---


Opened 2026-09-05 from `qou-qnqf`. Tool:
`scripts/unsourced-published-figures.py` (selftested, wired into nothing).

## Where this came from

`thm:markov-trace-factorization` published a transfer-matrix readout copied from
**deprecated** code — wrong on every bond — while a merged probe had already
recorded that exact readout as a trap. A defect can sit in a content block while
the correction sits in a probe. That prompted two mechanical questions.

## Question 1: deprecated provenance — answered NO, and the zero is real

**653 decimals live only in `computations/_deprecated/` and never in live code.
None of them reaches `content/`.** So no published figure has deprecated-only
numeric provenance. The readout defect was a *formula*, not a number, which is
why this test does not catch it — worth stating so nobody reads the zero as
covering the class it came from.

The detector selftests against an injected known positive and a fabricated
negative, per `qou-5pgl`: a detector without a known positive can report a whole
class clean, and this one would otherwise have reported exactly that.

## Question 2: no provenance at all — 35 of 333

**ROUNDING IS THE WHOLE DIFFICULTY, and getting it wrong inflates this 4x.**
Exact string matching reports 132; most are false, because a figure published at
one precision and computed at another does not string-match —
`0.00155060213`, `0.00155060`, `0.0015506` are three roundings of one quantity.
Allowing a source value to round to the published figure at its own decimal count
takes 132 → 35.

## THIS IS A CANDIDATE LIST, NOT A DEFECT LIST

The first candidate spot-checked is a **false positive, and correctly so**:
`0.00137748` in `flavor-split-habiro-derivation` is
`Δ_target = (m_n − m_p)/((m_p+m_n)/2)`, the experimental mass split from CODATA
masses. It is not computed anywhere because it should not be. Expect the same of
other AME/CODATA inputs and of values quoted from cited work. **Deciding any
entry needs a human reading its block; do not sweep off this list.**

Heaviest concentrations, as a starting point rather than a verdict:

    q-beta-spectral-bridge-table-data.md        4
    witness-substitution-audit.ts               2
    substrate-consistency-window-table1-data    2   (1.11023043771 / …782 — q-like
                                                     but NOT q0 = 1.10997858…)

The `substrate-consistency-window` pair is the one I would look at first: two
values differing in the 11th digit, both close to but distinct from `q0`, in a
table whose name says it is about the substrate window.

## One entry was mine, and fixing it is the worked example

`1.064088425325` was flagged — my own figure, published in the
`markov-trace-factorization` correction table earlier the same day, printed by a
probe but never recorded in its witness. Adding it and its two siblings to
`no_within_generator_noncommutativity_probe`'s witness took the count 36 → 35.
That is the shape of the fix where the fix is warranted: **witness the figure, do
not delete it.**

- [ ] Triage the 35. Per candidate: read the block, decide input vs computed vs
      stale, and either cite the source, witness the producer, or correct.
- [ ] Consider whether the tool should become a gate once the list is drained.
      It should NOT while the list stands — a gate red at 35 on arrival, with a
      known false-positive class in it, is one nobody can adopt.
