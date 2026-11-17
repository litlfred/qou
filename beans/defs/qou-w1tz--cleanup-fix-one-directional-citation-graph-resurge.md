---
# qou-w1tz
title: 'Cleanup: fix one-directional citation graph — resurgence/compute thread rarely cites the surreal/Écalle home back (utilization audit E2/G5 partially done)'
status: in-progress
type: task
priority: low
tags:
    - alien-habiro
    - reorg-2026-10-04
created_at: 2026-07-18T17:09:31Z
updated_at: 2026-10-04T15:25:47Z
parent: qou-frzo
---

The surreal appendix reaches into resurgence but the resurgence/compute thread almost never cites def:ecalle-borel-resummation back (before 2026-07-12 wiring: only 2 corpus mentions of Écalle-Borel). Also 'st'/'ord_ω'/Δ_ω/Stokes-constant register status. Verify the 2026-07-12/13 wiring pass (Option A + E2) actually landed on main: notation Table 10 rows for st/ord_ω, three-Borels collision entry, uses[] edges from resurgence blocks (q-beta-c3-continuum-geometry, phi-q-aj-machinery-identification) to the def block. Backfill any missing edge. Refs: 2026-07-13-alien-calculus-surreal-integration-review.md Option A, borel-alien-calculus-utilization-audit E1/E2.

## Round 71 Progress (`litlfred/qou#8246`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StrandNormalizationChiralityAndMagnusBridgeBrick.lean` (`ecalle_borel_stokes_bridge_bi_directional_pairing_invariance`)
- **Summary**: Proved bi-directional pairing between the surreal Ecalle-Borel resummation jump `S_omega_f = f_reg + delta_omega_f` and the coefficient-plane alien derivative `delta_omega_f = A_omega * f_reg`.
- **80-dps Probe & Witness**: `computations/probes/strand_normalization_chirality_and_magnus_bridge_brick_probe.py` -> `computations/probes/strand-normalization-chirality-and-magnus-bridge-brick.witness.json` (`scriptCommitSha: bf27f37259a48fea2b98340ccf2912cea35c83cc`, PR head `641d009e3ad3b5a36bfab308cf07ceb158eb2c62`)
- **PR**: https://github.com/litlfred/qou/pull/8246 (`status: in-progress` pending merge)
