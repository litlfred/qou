---
# qou-5h03
title: 'qou-x631: conditional-mean monotonicity is FALSE — a fifth monotone route dies; E[f|C2] is hump-shaped and the negativity is a high-C2 tail effect'
status: completed
type: task
priority: normal
created_at: 2026-09-07T12:30:53Z
updated_at: 2026-09-07T12:31:26Z
---

Probe: `computations/qbeta/qbeta_covariance_kernel_monotone_probe.py`, 6 assertions.
Follows `qou-dnev` (~40% slack ⟹ a lossy bound suffices). This tests the sharpest
lossy route available and eliminates it.

## The route, and why it looked like the one

`C_2(lam) = SUM_box c(box)^2`, and `chi^lam(3)/f^lam = (C_2 − C(k,2))/|C_3|`, so
`G(1) = (k!/|C_3|) · Cov_P(f, C_2)`. By the tower property
`Cov_P(f, C_2) = Cov_P(E[f|C_2], C_2)`, and `Cov(h(X), X) <= 0` for any
**decreasing** h. So:

> `c -> E_P[f^lam | C_2 = c]` monotone decreasing **⟹ the conjecture, outright.**

One-dimensional, so the k=18/26 failures that killed FSD and ICV don't apply. It
is also exactly the geometric intuition the epic has leaned on: rounder shapes
carry larger dimension and smaller content spread.

## It is false, and not narrowly

Exact rationals, `E[f|C_2=c] = SUM f^3 / SUM f^2` over each level set:

| k | levels | inversions | worst jump |
|---|---|---|---|
| 10 | 18 | 7 | 2.05× |
| 18 | 100 | 49 | 3.04× |
| 26 | 384 | **184** | **64.05×** |

About **half** of all consecutive pairs are inversions. Different failure mode
from FSD/ICV, which missed by 0.0161 and 0.0011 at two isolated k.

## And it survives no coarse-graining

Equal-Plancherel-mass bins, relative to bin 0 — non-monotone at 8 bins and even
at 4:

    k=26, 4 bins:  1.000  1.361  1.222  0.742
    k=26, 8 bins:  1.000  1.072  1.701  1.076  1.324  1.202  0.976  0.551

Not a noisy decrease — a **hump**. `E[f|C_2]` rises through the middle and falls
only in the top bin (asserted: for k>=14 the max is at an interior bin, the min at
the last).

## Where the negativity actually lives

`Cov_P(f,C_2) = SUM P(lam) f (C_2 − mu)`. The weight `(C_2 − mu)` is ~0 in the
middle, so the interior hump contributes almost nothing. **The negativity comes
from the top C_2 bin**, where the weight is most positive and `E[f|C_2]` is most
suppressed — high-spread partitions fail to supply the positive mass their weight
would otherwise give.

**So the target is a one-sided tail estimate: an upper bound on `E_P[f|C_2=c]`
for large c.** Strictly weaker than monotonicity, it is the shape Vershik–Kerov
large-deviation machinery actually produces, and it is not what any of the five
eliminated routes was trying to prove.

## An implementation cross-check, NOT independent evidence

Splitting by `sign(C_2 − mu)` gives 0.6008, 0.5727, 0.6223, 0.5779, 0.6068 at
k=12,16,20,24,28 — matching `qou-dnev`'s A/B to every printed digit. **That
agreement is guaranteed**: since `sign chi = sign(C_2 − mu)` the two sign classes
are the same partition of the lambdas and the ratios are equal by identity. It
checks that two separately written implementations agree, and nothing more.
Recorded because *"reproduced by an independent route"* is the natural and wrong
thing to say.

## The tally

Monotone-flavoured routes eliminated on this epic: **FKG** (`qou-r91v` item 2),
**Chebyshev comonotonicity** (item 3), **first-order** and **increasing-concave
dominance** (`qou-vilx`), and **conditional-mean monotonicity** (here). *The
conjecture is not a monotonicity phenomenon* — now a measured statement rather
than a run of bad luck.
