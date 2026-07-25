---
# qcz16
title: 'B6: census -> Lean bridge — "no positive cycle <= period N" as a Lean theorem'
status: todo
type: task
priority: low
parent: qcz14
created_at: 2026-07-25T03:30:00Z
updated_at: 2026-07-25T03:30:00Z
---

Lean-certify what the exact Python census (computations/qcollatz_cycle_census.py,
<= period 18) already established rigorously: no positive Skein-Collatz cycle up
to period N, for small concrete N. Route: encode the cycle-value formula
P0 = n_w/([2]_q^k - [3]_q^{k_odd}) per word and prove non-existence by
decide/native_decide over ℤ[q] for fixed small k, OR extend the per-word
period-2 linear_combination approach to period-3/4. LOW marginal value (census
is already rigorous); do only if a Lean stamp is wanted. Not blocking.
