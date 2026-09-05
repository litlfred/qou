# The hook/two-row reversal is an INTERIOR crossing, and it does not track `n/2`

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — A=2, 3, 4. Nothing wired, no witness, no fit.

## The question this closes

#6677 established that the per-dim majorant satisfies `hook(b) > two-row(b)` at small `b` and
`two-row(b) > hook(b)` at large `b` — the relation **changes sign**. But at both sizes then
measured the reversal sat at `b = ⌊n/2⌋`, which is *also* the last `b` at which a two-row shape
exists at all. Two readings fit two data points, and #6677 recorded the ambiguity rather than
picking one:

- **(i) boundary** — the two-row column simply ends before the hook can overtake it again, so the
  "reversal" is an artifact of where the column stops;
- **(ii) interior** — the two curves genuinely cross, and landing on the last `b` twice was
  coincidence of those sizes.

**A=4 separates them, and (i) is refuted.**

## The measurement

Probe: [`magnus_a4_crossing_sparse_probe.py`](../../computations/deltalambda/magnus_a4_crossing_sparse_probe.py)
(landed in #6710). `mp.dps = 65`, `mpf` throughout, precision asserted at every compute entry.

### A=4 (n=12), `⌊n/2⌋ = 6`

| b | hook per-dim | two-row per-dim | ratio | |
|---|---|---|---|---|
| 1 | 62105.983 | 62105.983 | 1.0 | same shape — forced, the cross-check |
| 2 | 50708.093 | 43907.244 | 1.154891 | |
| 3 | 28688.965 | 25677.635 | 1.117274 | |
| 4 | 13057.703 | 15754.936 | 0.8288007 | **crosses** |

The ratio falls below 1 at **`b = 4`**, strictly before the last comparable `b = 6`. Reading (i) is
dead: there is nothing at `b=4` that the boundary of the two-row column could explain, because that
column continues to `b = 5` and `b = 6`. The crossing is a genuine interior crossing of two decaying
curves, and `k = 5, 6` never had to be computed.

### The crossing point across all three sizes

| n | first `b` with two-row > hook | `⌊n/2⌋` | agree? |
|---|---|---|---|
| 6 | 3 | 3 | yes |
| 9 | 4 | 4 | yes |
| 12 | **4** | **6** | **no** |

The two coincided at the first two sizes and diverge at the third. That divergence *is* the result:
the crossing does not track `n/2`.

## The observation this leaves, with its sample size

Over `n = 6, 9, 12` the crossing sits at `b = 3, 4, 4` while `n` doubles — roughly **constant in
`b`**, not proportional to `n`. As a fraction it falls: `0.50, 0.44, 0.33`. If that holds, the hook
column drops below the two-row at a *fixed small* `b` independent of `n`.

Three sizes is three points. This is recorded as an observation, not a law, and the honest reading
is only the negative one it was measured for: **the crossing is not at the boundary, and it is not
at `n/2`.** Whether it is asymptotically constant, or merely growing slowly, is not decided here.

A second pattern, same caveat: the ratio's peak (always at `b = 2`) shrinks with `n` — `1.689`,
`1.245`, `1.155` — so the two columns are converging as `n` grows.

## What this means for the arc

#6669 found that five of seventeen candidate statistics come within one inversion of ordering
`tr_λ(X*X)/dim_λ`, all failing on the same hook-vs-two-row pair. #6677 showed the hook/two-row
relation reverses. This closes the remaining escape: the reversal is **not** an edge artifact that
a statistic could be excused from reproducing.

So the demand on any ordering statistic stands at full strength: it must reproduce a hook/two-row
relation that **changes sign at an interior `b` that does not track `n`**. That is a much stronger
constraint than monotonicity, and it is why hunting an eighth diagram statistic is not the right
next move.

## What is NOT established

- **A=2, 3, 4 only**, and A=4 is computed to `k = 4` — `k = 5, 6` were not run, because the crossing
  at `k=4` already decides the question. They are *not run*, not evidence for anything.
- **The sparse kernel is gated at A=2 and A=3**, where the dense implementation can also run
  (agreement 9.09e-66 and 1.92e-65, every `k`). It is the same algorithm at A=4, but that is an
  argument, not a measurement at that size.
- **Nothing here bounds anything.** The closed forms compute the trace of the positive element
  `X*X`; they do not majorize it.
- Whether the crossing point is asymptotically constant is **open**, and three sizes cannot settle
  it.
