---
# qcz16
title: 'B6: census -> Lean bridge — "no positive cycle <= period N" as a Lean theorem'
status: in-progress
pr: 8259
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T03:30:00Z
updated_at: 2026-10-04T15:25:46Z
parent: b9cj
---

Lean-certify what the exact Python census (computations/qcollatz_cycle_census.py,
<= period 18) already established rigorously: no positive Skein-Collatz cycle up
to period N, for small concrete N. Route: encode the cycle-value formula
P0 = n_w/([2]_q^k - [3]_q^{k_odd}) per word and prove non-existence by
decide/native_decide over ℤ[q] for fixed small k, OR extend the per-word
period-2 linear_combination approach to period-3/4. LOW marginal value (census
is already rigorous); do only if a Lean stamp is wanted. Not blocking.

- **Round 55 update (in-progress):** De-vacuified in PR `litlfred/qou#8259` (HEAD `1be723e4c3e702d48db833cb3bedc75e89004822`), verified with Lean 4.24.0 (`0` `sorry`, `0` vacuity hits) and 80-dps `mpmath` witness.
