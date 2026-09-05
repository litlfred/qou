# The column-end rise does not need a square shape — it is a tail rise after a minimum

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` (rescoped) · **Scope:** (a) scope-limited — A=3,4,5 at
one q₀, single window `a=0` at A=3 and A=5, all ten windows at A=4. Nothing wired, no witness, no
fit.

## The question, and why it needed an odd `n`

At A=4 the per-window rise sits at `k=6` = `(6,6)`, which is **both** the square shape and the last
shape in the column. Those cannot be told apart at that size. Three readings fit equally:
*requires exact squareness*, *near-square*, *end of column*.

`n = 3A` is odd whenever `A` is odd, and an odd `n` has **no square two-row shape at all**. So A=5
(n=15, column `k = 0…7`, last shape `(8,7)`) can decide whether squareness is required.

**Its limit, stated before the run:** the square shape *is* the last shape whenever it exists, so no
experiment can place one in a column's interior. A=5 can refute *"requires exact squareness"*; it
cannot by itself separate *near-square* from *end of column* — unless the rise also appears at an
**interior** `k`, which is what happened.

## Result — squareness is not required, and neither is the column end

`|tr_λ(ρ[σ_0,σ_1])| / dim`, window `a=0`, A=5 (n=15):

| k | λ | dim | value | |
|---|---|---|---|---|
| 3 | (12,3) | 350 | 0.02368091 | |
| 4 | (11,4) | 910 | 0.005325532 | |
| 5 | (10,5) | 1638 | **0.004189112** | ← minimum |
| 6 | (9,6) | 2002 | 0.008089459 | rise ×1.93 — **interior, not square** |
| 7 | (8,7) | 1430 | 0.00988847 | rise ×1.22 — **last, not square** |

- **`(8,7)` rises and is not square** ⇒ *"requires exact squareness"* is **refuted**. No square shape
  exists anywhere in this column.
- **`(9,6)` rises and is interior** ⇒ *"end of column"* is **refuted too**. The rise begins before
  the last shape.

So the effect is a **tail rise after a minimum**, not an attribute of the square shape or of the
final entry. At A=5 the minimum is at `k=5` and everything after it rises.

## What this does NOT establish

- **One window at A=5.** `a=0` only; A=4's ten windows show the U-shape's minimum at `k=5` in 7 of
  10, at `k=4` in 2, at `k=3` in 1 — so "minimum at `k=5`" is a majority, **not** universal, and I am
  not asserting a fixed minimum location.
- **It is not universal across `A` either.** At A=3, window `a=0` **falls** into its last shape
  `(5,4)` — per-dim 0.109955 → 0.0928117 and raw 5.27783 → 3.89809. So the tail rise is absent at the
  smallest odd size, and the A=3 column (`k ≤ 4`) may simply be too short to have a tail.
- **No mechanism.** Why a minimum, and why there, is unexplained.
- **Nothing is bounded**, and this changes none of the arc's standing negatives.

## Two defects in the probe, both exposed by running it at a new size

Both were invisible at A=4, the only size it had been run at, and both are the same class: a
quantity computed correctly and **labelled by a hardcoded assumption**.

1. **A label that was right at exactly one size.** The square-end block was hardcoded to `k=5 → k=6`
   and titled `SQUARE END`. At A=5 that pair is `(10,5) → (9,6)` — neither square nor last — and the
   probe still printed `SQUARE END`. At A=3 the same indices raised `IndexError`, the column stopping
   at `k=4`. Now computed: `k_last = ⌊n/2⌋`, titled `SQUARE END (… is square)` for even `n` and
   `COLUMN END (… — n odd, NO square shape exists)` for odd. **A label correct at one size and
   silently wrong at every other is worse than no label**, because it reads as a finding.
2. **A global verdict from a one-window sample.** Run with `--windows 0`, the probe printed
   *"COLLECTIVE: no single window rises into k=4 — it is interference, and the local operator
   explains nothing"* — from **one** window, while at A=4 **6 of 10** windows do rise into `k=4`. It
   now refuses any LOCAL/COLLECTIVE verdict on a partial sample, reports the measured fraction, and
   prints the exact `--windows` line for a full run.

The second is the same shape as the degeneracy defect this probe already carries a guard for: a
comparison-based verdict rendered where the data cannot support one. That is now the third such
guard in this file, which is itself the finding — **this probe's verdicts have been wrong more often
than its numbers.**
