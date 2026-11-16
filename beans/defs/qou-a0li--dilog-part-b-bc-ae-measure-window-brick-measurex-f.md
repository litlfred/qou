---
# qou-a0li
title: 'dilog Part-B BC a.e.: measure-window brick — measure{x: frac(log(1/x)/log q_m)<eps_m} <~ eps_m (change-of-vars x=e^-u + periodicity), then measure_limsup_eq_zero + branch_gap_lower_of_fract close a.e. convergence'
status: in-progress
pr: 8220
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T00:25:18Z
updated_at: 2026-10-04T15:12:22Z
parent: qou-r9ih
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-01 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Progress Update (2026-11-16T22:11:55Z)
- Implemented machine-checked Lean 4 theorem in `folio/quantum-observable-universe/lean/QOU/QBeta/DilogPartBJointAndOhtsukiSaddleBrick.lean` and 80-dps `mpmath` / exact rational witness `computations/probes/dilog-part-b-joint-and-ohtsuki-saddle-brick.witness.json`.
- Opened PR https://github.com/litlfred/qou/pull/8220 (`4fed1eb1d2c9f99be67799649865fd4f3ddd3d6a`); keeping `status: in-progress` until PR merges.
