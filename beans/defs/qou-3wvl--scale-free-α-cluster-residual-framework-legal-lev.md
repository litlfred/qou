---
# qou-3wvl
title: 'SCALE-FREE α-cluster residual (framework-legal lever, aligns 2026-08-02 FOREVER-GATE): the ratio law B(n_α)=n_α·B(4He) holds ~2% (n≤2), drifts +13% by 16O = the surface correction. Derive the scale-free surface/asymmetry residual (∝A^{-1/3} candidate) from the substrate — q0 cancels, outside the measurement ceiling. The dimensionful 29.8 MeV/α scale is GATED (numerology, do not fit).'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-02T19:34:13Z
updated_at: 2026-10-04T15:13:54Z
parent: qou-v2om
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 75 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/TwoRowFrobeniusStratumAndConnectedSumTraceBrick.lean` (`scale_free_alpha_cluster_ratio_q0_scale_cancellation`)
- **Summary**: Proved exact cancellation of the overall scale `s0 != 0` in the normalized `alpha`-cluster surface residual `(B(n_alpha) - n_alpha * B(1)) / B(1) = delta_surf / b_alpha`.
- **80-dps Probe & Witness**: `computations/probes/two_row_frobenius_stratum_and_connected_sum_trace_brick_probe.py` -> `computations/probes/two-row-frobenius-stratum-and-connected-sum-trace-brick.witness.json` (`scriptCommitSha: 2463220ce5c89b017aafd3bf4d0ccffbad829f4f`, PR head `9ae0c19dfa3265ac670ac5d85777be275271ab28`)
