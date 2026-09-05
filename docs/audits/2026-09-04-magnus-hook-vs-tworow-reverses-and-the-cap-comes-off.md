# The hook/two-row relation reverses with `b`, and lifting the dim cap strengthened the hook result

**Date:** 2026-09-04 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — A=2 and A=3. Nothing wired, no witness, no fit.

## Summary

1. **The dim cap comes off, and the hook column survives it.** #6587's hook monotonicity was measured
   over the 4 hooks under `dim ≤ 50`; the reduced-Burau closed form reaches **all 7 hooks at n=9**,
   and per-dim monotonicity holds across the complete column including the three shapes no previous
   probe could evaluate. The cap was not hiding a violation — a real possibility that had to be
   checked, not assumed.
2. **`hook(b)` vs `two-row(b)` reverses with `b`**, at both sizes. So the #6669 blocking pair is
   *not* an instance of a systematic hook-above-two-row ordering.
3. **Both closed forms are verified against each other**, not only against the quantity they are
   derived from: at `b=1` the shape `(n−1,1)` is simultaneously a hook and a two-row, and the two
   independent reductions agree to 3.21e-139.

## The measurement

Probe: [`magnus_hook_vs_tworow_crossing_probe.py`](../../computations/deltalambda/magnus_hook_vs_tworow_crossing_probe.py).
Exact `mpf`, `dps 140`.

```
hook:     tr_(n−b,1^b)(X*X) = −c²·q^{(2L+4)(1−b)}·Σ_{a,b'} Σ_± ± e_b(μ(word))     (#6556)
          (n−1)×(n−1) reduced Burau,        dim = C(n−1, b)
two-row:  tr_(n−b,b)(X*X)   = ‖X|_{W_b}‖_F² − ‖X|_{W_(b−1)}‖_F²                   (#6587)
          sectors of the fixed 4×4 Ř,       dim = C(n,b) − C(n,b−1)
```

Neither builds the seminormal irrep, so neither is bound by the `dim ≤ 50` cap that made every
earlier probe in this arc skip 17 of 28 shapes at `n=9`.

### A=3 (n=9)

| b | hook λ | dim | per-dim | two-row λ | dim | per-dim | | in cap? |
|---|---|---|---|---|---|---|---|---|
| 1 | `(8,1)` | 8 | 4718.6197 | `(8,1)` | 8 | 4718.6197 | same shape | both |
| 2 | `(7,1,1)` | 28 | 3478.2851 | `(7,2)` | 27 | 2793.0993 | hook > | both |
| 3 | `(6,1,1,1)` | 56 | 1671.2349 | `(6,3)` | 48 | 1498.5567 | hook > | two-row only |
| 4 | `(5,1⁴)` | 70 | 581.16326 | `(5,4)` | 42 | 981.20482 | **two-row >** | two-row only |
| 5 | `(4,1⁵)` | 56 | 134.62753 | — | | | | neither |
| 6 | `(3,1⁶)` | 28 | 14.319006 | — | | | | hook only |
| 7 | `(2,1⁷)` | 8 | 0.43542929 | — | | | | hook only |

### A=2 (n=6)

| b | hook | per-dim | two-row | per-dim | |
|---|---|---|---|---|---|
| 1 | `(5,1)` | 320.77993 | `(5,1)` | 320.77993 | same shape |
| 2 | `(4,1,1)` | 174.18411 | `(4,2)` | 103.15377 | hook > |
| 3 | `(3,1,1,1)` | 47.264492 | `(3,3)` | 53.564432 | **two-row >** |

## 1. The verification that licenses the out-of-cap rows

Extending a formula past the range where it was checked is how a measured identity becomes an
assumed one, so the probe refuses to print out-of-cap values until both gates pass:

| gate | A=2 | A=3 |
|---|---|---|
| every in-cap value vs the direct seminormal `tr_λ(X*X)` | 6.67e-139, 10 shapes | 2.06e-138, 11 shapes |
| the two **independent** reductions vs each other at `b=1` | 1.86e-139, dims 5/5 | 3.21e-139, dims 8/8 |

The second gate is the stronger one: it checks the two reductions against *one another* rather than
against the object they are both derived from, so an error common to the derivation of one of them
would not pass it.

## 2. The hook column, complete

`4718.62 > 3478.29 > 1671.23 > 581.16 > 134.63 > 14.32 > 0.435` — strictly decreasing per dimension
across **all 7** hooks at n=9, **3 of which were beyond the old cap**. #6587 could only say this of
the 4 under it. The two-row column is likewise monotone across all 4 of its shapes (none was ever
out of cap).

This is a strengthening, not a new claim: the same quantity, the same monotonicity, now over the
whole column rather than a dimension-selected subset. A dimension-selected subset is exactly the
kind of sample that can flatter a trend, so it was worth the check.

## 3. The reversal, and where it sits

`hook(b) > two-row(b)` at `b = 2, 3` and `two-row(b) > hook(b)` at `b = 4` (A=3); hook at `b=2`,
two-row at `b=3` (A=2). **The relation changes sign.**

Consequence for #6669: the blocking pair `(7,1,1)`/`(7,2)` is not an instance of a systematic
ordering that a statistic could be built to respect. Any statistic ordering the per-dim majorant
must reproduce a hook/two-row relation that **reverses with `b`** — a materially stronger demand
than monotonicity, and one that no simple diagram invariant is going to satisfy by accident. That
is a better reason to stop hunting an eighth candidate than "seven have failed".

**Where it reverses is suggestive, and the sample is two.** In both cases the reversal occurs at
`b = ⌊n/2⌋` — the *last* `b` at which a two-row exists at all, where `(n−b, b)` is as square as it
can be. So this may be a **boundary effect of the two-row column** rather than a crossing in the
interior. Two sizes cannot distinguish those, and this is recorded as an observation with its
sample size attached, not as a rule.

## What is NOT established

- **A=2 and A=3 only.** The out-of-cap values are exact evaluations of formulas verified in-cap and
  against each other — stronger than extrapolation, but not a proof of either closed form.
- **Nothing here bounds anything.** The closed forms compute the trace of the positive element
  `X*X`; they do not majorize it. The bound on the hook column is still #6587's.
- At `b = n−1` the Burau form returns `−1.7e-141` (A=3) / `−4.7e-141` (A=2). That is roundoff at
  dps 140 against a true zero, not a negative majorant; those rows are excluded from the
  monotonicity check rather than clamped.
- Whether the reversal is a boundary effect or an interior crossing is **open** and needs a third
  size.
