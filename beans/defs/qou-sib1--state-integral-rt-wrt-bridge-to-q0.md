---
# qou-sib1
title: 'FRONT-1: bridge RT/WRT value-map (roots of unity) to the state-integral q0 continuation'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T01:00:00Z
updated_at: 2026-10-04T15:19:23Z
parent: qou-n4nr
---

Owner picked front 1 ("overlap ok"). The selected keystone analytic route is the STATE INTEGRAL
(Faddeev/Garoufalidis-Kashaev): Habiro provably cannot reach q0 (|(q0;q0)_80|~7.3e140), state
integrals converge there (tau=b^2=-0.0166i in domain). DISTINCT ANGLE (mine): the WRT invariant HAS
a state-integral (Andersen-Kashaev Teichmuller-TQFT) representation, so bridge the salvaged RT/value-
map work (roots of unity, KeystoneLRAmplitudeReal/level-7, bwhk) to the q0 continuation. A sibling
(Opus 5 session) is actively on the pure Faddeev-quadrature side (commit 2aad4febd, qou-i85j) — per
parallel-exploration rules COORDINATE (post intent naming the parallel attempt + how the angle
differs) before/as I attack. Caveats from route-selection: convergence != W_lambda identification;
the AK evaluation theorem is at rational b^2 (roots of unity) and does NOT transfer to imaginary b^2.
NOT absolute-mass work (qou-exam): this is the W_lambda/ratio continuation, not m_p in MeV.

## Round 74 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StateIntegralBridgeAndTwoBridgeLayeredNZBrick.lean` (`faddeev_modular_b_squared_upper_half_plane_convergence_witness`)
- **Summary**: Proved upper-half-plane convergence condition `0 < -2 * u_r * u_i` for `-tau = -b^2` when `0 < u_r` and `u_i < 0`, plus norm-square factorization `(u_r^2 - u_i^2)^2 + (2 * u_r * u_i)^2 = (u_r^2 + u_i^2)^2`.
- **80-dps Probe & Witness**: `computations/probes/state_integral_bridge_and_two_bridge_layered_nz_brick_probe.py` -> `computations/probes/state-integral-bridge-and-two-bridge-layered-nz-brick.witness.json` (`scriptCommitSha: 5a0a98fc8762e45b734969dd4e71c7271737dbf3`, PR head `564a7f62489ee3d8fa99df6e5a109d1af0b09d37`)
