---
# qou-pj82
title: 'GAP: CKM sector (4) — categorical flavour basis unposed; no mixing-matrix object'
status: in-progress
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-07-31T20:15:07Z
updated_at: 2026-10-10T18:10:00Z
parent: qou-20sx
blocked_by:
    - qou-y7vg
    - qou-x4qm
pr: 8232
---

## 🔥 Roast (2026-09-03, qou-bsu0)

(i) Needs a flavour basis — three generations as distinct objects of one category — and a mixing operator between mass and weak eigenstates. The corpus has neither; CKM is unposed (`sm-params-ckm.md`).
(ii) Excluded: nothing CKM-specific has been tested. Upstream: N = 2 cannot host the flavour multiplets (scope-b, `RowCapObstruction.lean`); eight N = 3 routes excluded with named invariants (`eightfold-n3-surface.md`, `OctonionicSu3RankObstruction.lean`); the H¹(base, Aut^⊗)/band formulation imports symmetric Tannakian duality the braiding provably lacks (`double_braiding_eq_one_iff`); the generation count is open (`qou-x4qm`).
(iii) Trap: a 3×3 unitary built from q-brackets or cos/sin(ln q₀) landing θ₁₂ = 13.0° — four targets against free integer slots is a fit; amphicheiral ⇒ δ_CP = 0 (`cp-violation-spectral-form.md`) is a constraint, not a derivation.
(iv) Next: not near-term; blocked on 4-A (`qou-y7vg`, stalled at "name the base") and generations.
(v) Forecast: nothing before an N = 3 construction; a refutation of 4-A would honestly move CKM to "imported".
Tower status [reading: qou-ggdk]: no attack at any order; under the ruling a mixing matrix is an operator on the flavour Wedderburn blocks of the full tower, not a number at q₀ — no formulation exists.

## 2026-10-10 — reparented under qou-20sx

Owner decision 7b (ofri, 2026-10-10): the electroweak (`8f-ew`) beans are grouped under `qou-20sx`, the electroweak front's node, instead of directly under the epic `qou-8lxd`. Only the parent changed. Status, scope and body are untouched.

## Implementation Note (PR #8232)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/HeavyQuarkDoubletObstructionFreezeOutTruncationWeinbergBlockNormCkmParameterCountAndNeutrinoZeroVolume.lean` and `computations/probes/heavy_quark_doublet_obstruction_freeze_out_truncation_weinberg_block_norm_ckm_parameter_count_and_neutrino_zero_volume_probe.py` (witness `computations/probes/heavy-quark-doublet-obstruction-freeze-out-truncation-weinberg-block-norm-ckm-parameter-count-and-neutrino-zero-volume.witness.json`, `5c9df8778eb7e1128541cebe1318fc29ba5b5b7e`).
