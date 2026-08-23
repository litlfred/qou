---
# qou-pvem
title: 'DEAD_TOL is a global constant, but noise depends on the witness''s own precision'
status: todo
type: task
priority: normal
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-08-23T00:00:00Z
---

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
