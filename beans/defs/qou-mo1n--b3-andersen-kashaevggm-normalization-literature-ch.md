---
# qou-mo1n
title: 'B3: Andersen-Kashaev/GGM normalization literature check — evidence tier only (parent qou-yh67)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T02:49:30Z
updated_at: 2026-10-04T15:16:36Z
parent: qou-n4nr
---


## E2 refinement (2026-08-15): the lit target is now sharper — find the
Andersen-Kashaev/GGM relation between the state-integral variable and the
meridian deformation (pins the bridge constant c up to convention), and
which normalization (V vs Phi=2V) the Kashaev/Ohtsuki tower expands.
Evidence tier only; feeds the OhtsukiNZBridgeScale lock equation.

## Round 74 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StateIntegralBridgeAndTwoBridgeLayeredNZBrick.lean` (`andersen_kashaev_potential_vs_complex_volume_bridge_ratio`)
- **Summary**: Proved Andersen-Kashaev potential vs complex-volume bridge-scale ratio `c_pot_sq = 2 * c_shape_sq` when `kappa_shape = 2 * kappa_pot` and `kappa_shape * c_shape_sq = kappa_pot * c_pot_sq` (`kappa_pot != 0`).
- **80-dps Probe & Witness**: `computations/probes/state_integral_bridge_and_two_bridge_layered_nz_brick_probe.py` -> `computations/probes/state-integral-bridge-and-two-bridge-layered-nz-brick.witness.json` (`scriptCommitSha: 5a0a98fc8762e45b734969dd4e71c7271737dbf3`, PR head `564a7f62489ee3d8fa99df6e5a109d1af0b09d37`)
