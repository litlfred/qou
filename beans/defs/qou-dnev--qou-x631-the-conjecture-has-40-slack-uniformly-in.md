---
# qou-dnev
title: 'qou-x631: the conjecture has ~40% slack uniformly in k (A/B ~ 0.59) — tight order-theoretic tools are the wrong tools'
status: completed
type: task
priority: normal
created_at: 2026-09-07T11:42:36Z
updated_at: 2026-09-07T11:43:09Z
---

Probe: `computations/qbeta/qbeta_covariance_kernel_slack_probe.py`, 6 assertions.
Follows `qou-vilx`, which left *"attack G(s) directly"* as the surviving route.

Before looking for a sign-reversing involution I asked what one would have to
achieve. With the sign-split `G(s) = A(s) − B(s)`,
`A(s) = SUM_{chi>0}(f)^{1+s}|chi|`, `B(s) = SUM_{chi<0}(f)^{1+s}|chi|`, the
conjecture at s=1 is exactly `A(1) <= B(1)` and `A(0) = B(0)` is `G(0) = 0`.

## 1. The cancellation is bounded — R ≈ 4, flat in k

`R(k) = SUM|(f)^2 chi| / |SUM (f)^2 chi|` stays in **[3.32, 4.91]** over
6 <= k <= 30, exact Fractions, **with no growth in k**. `G(1)` is an order-one
fraction of the total absolute mass, not a delicate residual. An involution would
have to account for about three quarters of the mass — not all but a vanishing
sliver of it.

## 2. A/B ≈ 0.59 against a threshold of 1

| s | A/B |
|---|---|
| 0 | **1 exactly** |
| 0.25 | ~0.86 |
| 0.5 | ~0.75 |
| 1 | **[0.538, 0.662]**, centre ~0.59, no drift over 6 <= k <= 34 |

The conjecture needs only `A/B <= 1`. **It holds with ~40% of slack, uniformly
in k**, and the margin opens smoothly with the tilt rather than appearing at the
endpoint.

## 3. Why that indicts the eliminated routes

`qou-vilx` killed first-order and increasing-concave dominance because they fail
at k=18 and k=26 — by **0.0161 and 0.0011**. Set that against **40% of slack** in
the quantity actually wanted. Those are *tight, pointwise conditions on whole
distributions*, deployed against a *slack aggregate inequality*. They were far
stronger than necessary, which is exactly why an arbitrarily small local defect
destroyed them while the conjecture stood untouched. Same critique applies to FKG
and Chebyshev (`qou-r91v` items 2–3).

**Operational consequence: a LOSSY bound suffices** — roughly a factor 1.7 to
spare — and exact combinatorial matching is not required. That is a different
search from the one the epic has been running.

## 4. The mass is in the bulk

The largest |term| in `G(1)` is a **near-staircase at every k**: (3,2,1),
(4,3,2,1), (5,4,3,2,1), (6,5,4,3,2), (8,6,5,4,3) — typical Plancherel shapes, not
hooks or rectangles. Asserted as: >= 4 rows and >= 4 columns for every k >= 12. The
negativity lives in the limit-shape region, where Vershik–Kerov machinery is
strongest.

## What this is NOT

**Slack is not a proof and is not progress toward one** — `A/B <= 1` is still the
whole conjecture. What is established is a *budget*: how much a candidate argument
may lose. Recorded because the epic has eliminated five routes, four of them
(FKG, Chebyshev, FSD, ICV) tight conditions of exactly the kind this measurement
says are unnecessary.
