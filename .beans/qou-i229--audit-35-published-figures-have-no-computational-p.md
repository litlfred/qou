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

## TRIAGE ROUND 1 (2026-09-05): 35 -> 32, and category (b) EXISTS after all

Two entries closed and a real defect found. Probes:
`substrate_consistency_window_q_from_alpha_em_probe.py` (3/3),
`published_figures_carry_a_retired_q0_probe.py` (4/4).

### (c) correct but unwitnessed — CLOSED, worked example

`1.11023043771` / `1.11023043782` in `substrate-consistency-window-table1-data`.
Every `alpha_EM`-inversion module in the tree is deprecated and the block's `.ts`
cites nothing computational, so this looked like the stale case. It is not:
inverting the bare form `alpha^-1 = q[9]_q[10]_q` at 40 dps gives
`1.11023043770666` (CODATA 2018) and `1.11023043781657` (2022) — the published
figures are the correct roundings, and the quoted `1.1e-10` shift is right too.
**Correct, derived, merely unwitnessed.** Producer now recorded.

One overstatement corrected en route: the block called that shift "six orders of
magnitude below the ±0.00002"; it is `1.82e5`, i.e. **five**.

### (b) STALE — FOUND, and it is four figures across two blocks

I wrote "of which none has yet been found". Wrong within the hour.

    q0_retired = 1.1099785955541805752815940796095093779932822799587

lives in eight `computations/_deprecated/` witnesses and one deprecated script,
**nowhere live**, and is neither anchor — proton `1.10997858275…`, muon
`1.10997859564…` — sitting *between* them, which is why nothing looked wrong.

    block                                figure           published        retired q0 gives
    hecke-log-decomposition-table-data   1 + q_0          2.10997859556    2.10997859555418
    hecke-log-decomposition-table-data   log(1 + q_0)     0.74667780313    0.746677803149403
    hecke-log-decomposition-table-data   log(1/hbar_q)    2.31181024982    2.31181024984889
    em-coupling-bring-zero-mode          q[9]_q[10]_q     136.823219654    136.823219654561

`q[9]_q[10]_q` is decisive — the quantum integers amplify, so the retired value
matches 11 significant figures against muon's 9 and proton's 7. On all four the
retired value is closest **by relative error**.

**Not recomputed.** The proton/muon choice is owner-gated (`q_parameter.py`:
"genuinely MIXED", "a blanket flip is WRONG", "do NOT change this default").
Both live values are tabulated in the block caveats; the substitution waits for a
ruling.

### 🛑 THIS CORRECTS THE SWEEP'S OWN HEADLINE

The bean above reports "Question 1: deprecated provenance — answered **NO**".
That answer tested for the literal decimal **string**, and is true at that level.
It is **misleading as read**: a figure that is a *function* of a retired constant
inherits its provenance without ever carrying its digits. Four such figures were
sitting in the corpus while the sweep reported the class clean.

So the string-level test is much weaker than its phrasing suggested, and the
derived-level question is **open, not answered**. The method that works is the
one used here: take a published figure, guess the closed form from its own
caption, and solve for the `q0` that reproduces it.

- [ ] Run the derived-provenance test on the remaining 28. Cheap per figure where
      the caption gives the closed form (`1 + q_0`, `log(1/hbar_q)`, …), and most
      of them do.
- [ ] Owner ruling: which anchor do `hecke-log-decomposition-table-data` and
      `em-coupling-bring-zero-mode` take? Then substitute.
