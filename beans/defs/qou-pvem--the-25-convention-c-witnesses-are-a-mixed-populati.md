---
# qou-pvem
title: 'DEAD_TOL is a global constant, but noise depends on the witness''s own precision'
status: completed
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-23T00:00:00Z
---

<!-- FILENAME HAZARD: this file is named for a DIFFERENT bean. The
     "25 convention-C witnesses are a mixed population" body was written first on
     branch claude/conv-c-shared-root-2026-08-16 (PR #5168) under this id and
     filename; commit 0ab493a49a then overwrote it with the DEAD_TOL bean below,
     reusing both. Only the DEAD_TOL bean reached main. The mixed-population bean
     is recovered at `qou-a6yh`; nothing here relates to it. -->

<!-- front-matter added 2026-08-23. This file had none, so it carried no id, no
     status and no title, and was invisible to the tracker despite being an open,
     measured, actionable item. Body preserved verbatim below. Re-verified today:
     DEAD_TOL = 1e-30 is still live in BOTH scripts/convention-c-witness-audit.py:85
     and computations/live_channels.py:91, and the named witness
     computations/alpha/alpha-k-jones-markov-h12.witness.json still exists. -->

## Sub-class: float64 noise below DEAD_TOL — real, but it moves one file

`DEAD_TOL = 1e-30` sits far below float64 epsilon. A witness computed in
float64 under convention **D** cannot produce an exact zero for the 3+-row
weights; it produces ~1e-17 residue, which the structural test then reports as
a live weight. `alpha-k-jones-markov-h12.witness.json` shows
`[10,1,1] y_lambda = 1.9384536406840746e-18` — that is machine noise, not a
convention-C weight.

Measured across every witness in the tree:

| | |
|---|---|
| structural hits **below** 1e-12 (float64 noise) | **22,863** in 6 files |
| structural hits **above** 1e-12 (real weights) | **11,235** in 51 files |
| files that would **clear** at a float64-aware tolerance | **1** |

So the effect is real and dominates the raw hit count, but it changes the
verdict for exactly one witness: `alpha-k-jones-markov-h12`. The other five
noisy files also carry genuine weights (0.0227449… on `[1,1,1]`, 0.0101334…
on `[4,1,1]`) and stay convention C on their own merits.

**Worth fixing anyway, for the reason the count shows.** 22,863 spurious hits
inflate every summary the detector prints, and a reader who learns that most
hits are noise stops reading the hits. But it must be sold as a
*precision* fix, not as work-list reduction: it removes one file.

The right form is not a blanket tolerance raise — that would hide a genuinely
small weight. It is to compare against the witness's own recorded precision:
a value below the float64 epsilon of a float64-computed witness is noise; the
same value in a 50-dps witness is a real number. `DEAD_TOL` cannot express
that, because it is a single global constant.

### Pattern note

Third time in this arc that a plausible mechanism turned out to have small
scope: the shared `z` (2 of 25), the load-bearing retraction, and now this
(1 file). The difference is that this one was measured before it was claimed.

---

## RESOLVED 2026-08-23 — fixed at the producer, and the causal model here was wrong

Re-measured against `main` today. Every number in this bean has moved, and the
proposed fix should **not** be implemented.

### The concrete instance is gone

The falsifiable atom this bean rests on — `alpha-k-jones-markov-h12.witness.json`
showing `[10,1,1] y_lambda = 1.9384536406840746e-18` — now reads `'0.0'`, an
exact zero. Fixed by [`424e9343c9`](https://github.com/litlfred/qou/commit/424e9343c9)
*"snap proved-zero blocks to exact 0 — front 12 -> 11"*, at the **producer**.

That is the resolution AGENTS.md prescribes: *"Never make a red run green by
widening a baseline. Fix at the producer."* This bean proposed the opposite side
— a detector-side, precision-aware tolerance. Anyone reading it cold could
implement that and be working against the discipline, so it is worth saying
plainly: **the detector was never at fault.**

### The sub-class is empty corpus-wide

| | bean-era claim | measured 2026-08-23 |
|---|---|---|
| structural hits **below** 1e-12 | 22,863 in 6 files | **0 in 0 files** |
| structural hits above 1e-12 | 11,235 in 51 files | 293 raw / **122 in 4 files** as the audit reports them |
| files that would clear at a float64-aware tolerance | 1 | **0** |

The four survivors are `chi-helium-3-h9`, `chi-helium-4-h12`, `chi-tritium-h9`
and `derived-chi-catalogue`. Smallest weight among them is **3.08e-11**, in a
witness declaring `dps: 50` — roughly 39 orders above its own arithmetic floor.
Real weights, convention C on their own merits, exactly as this bean predicted
for the other five files.

### The causal model was wrong, and that is why the fix would not have worked

This bean attributes the residue to the **storage format**: *"a witness computed
in float64 under convention D cannot produce an exact zero … it produces ~1e-17
residue"*, and prescribes comparing a value *"against the witness's own recorded
precision"*.

The producer commit records what it actually was: **solver residue from a 77×77
linear system**, and the producer *was already convention D* — its Markov
parameter is `z = q₀³/(q₀²+1)`. So the flag was a false positive with a third
cause, and the residue came from the **algorithm**, not the arithmetic format.

That distinction breaks the proposed fix. Recorded precision tells you the
arithmetic floor; it tells you nothing about **conditioning**. A 50-dps solve of
an ill-conditioned system also returns residue far above its nominal epsilon, so
a precision-aware `DEAD_TOL` would have passed this witness through unchanged
while giving a false sense that the class was handled. The commit makes the same
calibration point from the other end: `DEAD_TOL = 1e-30` was set for *underflow*
(`1e-300`), and a linear solve delivers `1e-18` — "same detector, different
numerical route."

### Standing observation, not a work item

The general worry — that one global constant cannot express "is this small
number noise?" — is sound, and `DEAD_TOL = 1e-30` is still live in both
`scripts/convention-c-witness-audit.py:85` and `computations/live_channels.py:91`.
But there is currently **no instance** of it misjudging anything, and the right
correction when one appears is at the producer that emitted the residue, not at
the threshold that reported it. Reopen only with a live case in hand.
