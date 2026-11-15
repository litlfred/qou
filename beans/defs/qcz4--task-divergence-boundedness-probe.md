---
# qcz4
title: 'Probe: q-Collatz divergence half — forward-orbit boundedness from Skein seeds'
status: completed
type: task
priority: medium
parent: qcz1
created_at: 2026-07-24T15:48:40Z
updated_at: 2026-07-24T16:25:26Z
---

The hard half. Reuse exact Laurent arithmetic (computations/qcollatz_cycle_census.py):
iterate C_q forward from many positive Skein seeds (P with P(-1) ∈ {0,-1}), track
a valuation/degree measure, test whether every orbit descends to the 2-cycle.
Emit a witness. Negative-outcome-friendly: either finds a divergent/rogue orbit
(major) or accumulates descent evidence with the v_[2]>=2 contact statistic.

DONE: forward-orbit probe (6045 seeds). KEY FINDING: domain {P(-1)∈{0,-1}} NOT forward-invariant — 6042/6045 escape (most in 1 step); 0 divergent, 0 rogue. Conjecture cone must be domain-stable (no classical analog). Encoded pos_domain_stable field in QCollatz.lean + narrative note + witness. Also qcz5 resolved: owner chose content-bearing template.
