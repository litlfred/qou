---
# qou-pvem
title: 'The 25 convention-C witnesses are a mixed population (float64-noise sub-class)'
status: scrapped
type: task
created_at: 2026-08-16T01:42:22Z
updated_at: 2026-08-21T15:05:00Z
---

> **⚠ FRONTMATTER RECONSTRUCTED 2026-08-21.** This file had **no frontmatter at
> all** — no `---` block, no id, no `title`, no `status` — so it was invisible to
> `beans list` and could not be claimed or closed through the CLI. Cause: commit
> `0ab493a49` is a **cherry-pick** of `2227bead0` and adds 39 lines, `0` deleted.
> On the source branch that commit was an *append* to an existing bean; cherry-
> picked onto a branch where the bean had never been created, only the appended
> section landed and the file was born headerless. `2227bead0` is not in this
> clone and no other `*pvem*` blob exists in history, so the original header is
> **unrecoverable** — the fields above are reconstructed (title from the filename
> slug, which is itself truncated; `created_at` from the cherry-pick commit
> date). The body below §Original content is **byte-for-byte as committed**.


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

## Reasons for Scrapping (2026-08-21)

**The premise no longer holds. The population this bean describes is gone, and
the one file it said would clear has cleared — by a better route than the one
proposed.** Re-measured on `origin/main` @ `8ba73cc91`.

### 1. The float64-noise sub-class no longer exists

`scripts/convention-c-witness-audit.py`, run today:

| | this bean (2026-08-16) | today (2026-08-21) |
|---|---|---|
| structural hits | 34,098 (22,863 noise + 11,235 real) | **122** |
| files flagged structurally | 57 (6 noisy) | **4** |
| hits **below** 1e-12 (the noise class) | 22,863 | **0** |

Per-file minimum nonzero `y_lambda` in all four survivors:

```
chi-helium-3-h9-at-q0-50dps-matrix-m    min 8.694e-08   below 1e-12: 0
chi-helium-4-h12-at-q0-50dps-matrix-m   min 3.082e-11   below 1e-12: 0
chi-tritium-h9-at-q0-50dps-matrix-m     min 8.694e-08   below 1e-12: 0
derived-chi-catalogue                   min 1.000e+00   below 1e-12: 0
```

The smallest surviving weight is **3.08e-11 — nineteen orders above float64
epsilon**, and all four survivors are `50dps` witnesses, where float64 residue
cannot arise by construction. So the proposed fix (compare against the witness's
own recorded precision instead of a global `DEAD_TOL`) would today reclassify
**zero** entries. Its scope is not "one file"; it is nothing.

### 2. The one file it named was fixed at the producer, not the detector

This bean's own recommendation was *"not a blanket tolerance raise … compare
against the witness's own recorded precision"*. The corpus did something better:
it fixed the **root cause**. `computations/alpha/alpha_k_jones_markov_h12.py`
now snaps `ℓ(λ) ≥ 3` weights to exact `0` and keeps the solver residue as a
separate `dead_block_solve_residue` diagnostic, on the stated ground that under
convention D those blocks are exactly zero by Schur–Weyl on the two-dimensional
fibre — *"a theorem, not an approximation"* — so emitting residue
*"misrepresents a proved zero as a small number"*. Verified in the committed
witness: all **70** 3+-row entries read `0.0`, with `max_abs_residue`
`9.163718683397107e-18` preserved as a diagnostic. No information lost, and the
detector needed no change.

That is the correct resolution of the sub-class: a proved zero should be emitted
as zero by the producer, rather than taught to the detector as a tolerance.

### 3. `DEAD_TOL` is unchanged and that is now fine

`DEAD_TOL = 1e-30` still stands in both `scripts/convention-c-witness-audit.py:85`
and `computations/live_channels.py:91`. The general observation that a single
global constant cannot express per-witness precision **remains true in principle**
— it is simply no longer load-bearing, because no live witness sits in the gap.
If a float64-computed D witness is ever added, the producer-side snap above is
the pattern to follow, not a tolerance change.

### What is NOT scrapped

The four surviving structural witnesses are **genuine convention C** — real
weights, not noise — and belong to `qou-cdh3` (regenerate the convention-C
witnesses), together with the symbolic hit in
`y-lambda-macdonald-telescope.witness.json`. Scrapping this bean removes a
noise-tolerance work item; it does not clear those.

### Pattern note, extending the bean's own

The bean closed with: *"Third time in this arc that a plausible mechanism turned
out to have small scope … The difference is that this one was measured before it
was claimed."* That held, and it is why this is a clean scrap rather than a
retraction — the measurement was sound when taken, and re-measuring five days
later is what retired it. The scope shrank from "one file" to "zero files"
without anyone acting on the bean.
