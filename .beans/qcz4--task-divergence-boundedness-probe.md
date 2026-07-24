---
# qcz4
title: 'Probe: q-Collatz divergence half — forward-orbit boundedness from Skein seeds'
status: todo
type: task
priority: medium
parent: qcz1
created_at: 2026-07-24T15:48:40Z
updated_at: 2026-07-24T15:48:40Z
---

The hard half. Reuse exact Laurent arithmetic (computations/qcollatz_cycle_census.py):
iterate C_q forward from many positive Skein seeds (P with P(-1) ∈ {0,-1}), track
a valuation/degree measure, test whether every orbit descends to the 2-cycle.
Emit a witness. Negative-outcome-friendly: either finds a divergent/rogue orbit
(major) or accumulates descent evidence with the v_[2]>=2 contact statistic.
