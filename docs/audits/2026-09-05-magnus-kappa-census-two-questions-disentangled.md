# The complete κ census: two questions I had been conflating

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — complete n=9 κ census. Nothing wired, no witness, no fit.

## The census

`κ(λ) = |Σ eig| / Σ|eig|` over all 30 shapes at n=9, eigenvalues at dps 65 (~1h45m, `mp.eig` ~dim³):

| b | κ envelope | Σ\|eig\|/dim env | √(F/dim) env | \|tr\|/dim env |
|---|---|---|---|---|
| 1 | 0.9361762 | 35.94216 | 68.69221 | 33.6482 |
| 2 | 0.5365369 | 24.71046 | 58.97699 | 13.25807 |
| 3 | 0.2755190 | 14.51644 | 40.88074 | 3.999554 |
| 4 | 0.1546549 | 10.99674 | 31.32419 | 1.700701 |
| 5 | 0.1265840 | 7.487255 | 24.60863 | 0.9477663 |
| 6 | 0.2506526 | 3.956402 | 14.54526 | 0.3236127 |
| 7 | 0.6852138 | 1.168892 | 5.617503 | 0.1782527 |
| **falls** | **1.37×** | **30.75×** | **12.23×** | **188.77×** |

**κ's envelope is U-shaped (minimum at `b=5`) and falls only 1.37×.**

## Two questions, and I had been answering one while asking the other

- **Where is the bound loose?** → **κ.** #6792 measured, per shape, that `1/κ` varies **80×** across
  shapes while the Cauchy–Schwarz factor varies **2.3×**. That stands and is unaffected.
- **Why does the bound miss the `b`-decay?** → **not κ.** Its envelope barely moves (1.37×) while
  `|tr|/dim` falls 188.77×.

These are different questions. "The slack is κ" (#6792) answers the first and I had been treating it
as an answer to the second.

## The envelope decomposition does not close — and the probe says so

The recomposition check reports `κ-fall × Σ|eig|-fall = 42.01` against `|tr|-fall = 188.77`. That is
not a contradiction: these are **envelopes of a product, not a product of envelopes**, so they agree
only if the extremes are attained on the same shapes. A 4.5× discrepancy says they are not.

**Consequence: the envelope is the wrong frame for attributing the decay.** Neither factor explains
it there — κ contributes 1.37× and the Cauchy–Schwarz step 2.51× (30.75/12.23), against a 15.5× gap
between the actual decay and the bound's.

## A canned conclusion I am NOT adopting

The probe prints *"κ does NOT decay monotonically … the missing factor is in the Cauchy–Schwarz step
instead"*. That text was written before #6792 and is **too glib**: CS is uniform at 2–4× per shape
(#6792) and loses only 2.51× at envelope level, nowhere near the 15.5× gap. The honest statement is
the one above — at envelope level the attribution does not close, and saying "it must be the other
factor" is exactly the reasoning that produced three earlier wrong mechanisms in this arc.

## What this means for the route

It makes the **Féray–Śniady** route (`arxiv-math-0701051v4`, in the library) *better* motivated, not
worse. Their Theorem 1 bounds the **normalized** character per shape,

```
|χ̂_λ(π)| ≤ [ a · max( r(λ)/n , c(λ)/n , |π|/n ) ]^{|π|}
```

— a per-shape statement, which is the frame where the decomposition does close, and whose
shape-dependence `max(rows, columns)/n` is the same axis on which hooks separate from everything
else (`r + c = n + 1` for a hook).

## What is NOT established

- **n=9, this atom word.** Nothing proved for general `n`.
- **FS is the symmetric group (`q = 1`)**; here `q ≈ 1.11` and the element is a sum of commutators,
  not a single permutation. It is a template, not a drop-in.
- **Nothing here bounds anything.** This is the completed measurement of a decomposition.
