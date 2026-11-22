---
# qou-qsns
title: 'phi-q-tower-jsj-bridge: Open conjecture for Kashaev per-piece volume identification'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-12T10:23:22Z
updated_at: 2026-11-22T21:33:07Z
parent: qou-n4nr
---

## Round 74 Progress (`litlfred/qou`)
- **Lean module**: `folio/quantum-observable-universe/lean/QOU/QBeta/StateIntegralBridgeAndTwoBridgeLayeredNZBrick.lean` (`jsj_torus_decomposition_per_piece_volume_additivity`)
- **Summary**: Proved JSJ torus decomposition per-piece volume additivity `V_total = V1 + V2 + V3` with flat Seifert piece `V_seifert = 0`, strict piece dominance `V1 < V_total`, and positivity `0 < V_total`.
- **80-dps Probe & Witness**: `computations/probes/state_integral_bridge_and_two_bridge_layered_nz_brick_probe.py` -> `computations/probes/state-integral-bridge-and-two-bridge-layered-nz-brick.witness.json` (`scriptCommitSha: 5a0a98fc8762e45b734969dd4e71c7271737dbf3`, PR head `564a7f62489ee3d8fa99df6e5a109d1af0b09d37`)

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

No change. The Round 74 note ("JSJ per-piece volume additivity") proves `V1+V2+V3` adds up for real numbers; that is not the per-piece identification. Open PR, not on `main`.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: APPLIES.** Formal mathematics (volume conjecture, Lean hyperbolic/AJ infrastructure, Mathlib gaps). Checked its premises against owner-rulings.md on main: it uses none of the retired ones (σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, substrate-q₀ derivation, virtual photons, SM quark charges). Today's rulings (strand colour states, b = −qX on colour singlets with flavour trace values unchanged, convention D on the baryon sector, photon kept with fixed constant 1) do not reach knot-complement geometry. Its batch-PR notes (Nov 16–18 Round PRs) are all still open and unmerged as of 2026-11-22.
