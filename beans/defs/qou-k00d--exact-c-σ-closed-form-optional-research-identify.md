---
# qou-k00d
title: 'Exact c_σ closed form (OPTIONAL research): identify the numerical Whitehead prefactor c_σ≈0.5946 with a closed form (Reidemeister torsion / 1-loop invariant of the Whitehead complement). Off critical path; anti-fit discipline applies.'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T08:47:49Z
updated_at: 2026-11-22T21:15:45Z
parent: qou-n4nr
---

## Round 75 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/TwoRowFrobeniusStratumAndConnectedSumTraceBrick.lean` (`whitehead_one_loop_prefactor_torsion_inverse_square_root_lock`)
- **Summary**: Proved Whitehead one-loop prefactor lock `c_sigma_sq = 1 / 8` and `c_sigma_sq ^ 2 = 1 / 64` when `c_sigma_sq * (2 * tau_DG) = 1` and `tau_DG = 4`.
- **80-dps Probe & Witness**: `computations/probes/two_row_frobenius_stratum_and_connected_sum_trace_brick_probe.py` -> `computations/probes/two-row-frobenius-stratum-and-connected-sum-trace-brick.witness.json` (`scriptCommitSha: 2463220ce5c89b017aafd3bf4d0ccffbad829f4f`, PR head `9ae0c19dfa3265ac670ac5d85777be275271ab28`)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

Pointer: `qou-vdvS` (completed) gives the closed form for the whole `b = 1` family, `c_σ(W_{a,1,c,d}) = 2^{1/2−n}(n²+m²)^{−1/4}`. At the Whitehead link `n = m = 1` this is `2^{−3/4} = 0.594604…`, matching the numerical `c_σ ≈ 0.5946`. Not closing here: the value is derived on the Jones side in `qou-vdvS`, and whether a Lean statement of it exists has not been checked in this pass; the Round 75 note's `c_sigma_sq = 1/8` (from an assumed `tau_DG = 4`) contradicts `2^{−3/2}` and is a batch-PR artefact (open PR, not on `main`).
