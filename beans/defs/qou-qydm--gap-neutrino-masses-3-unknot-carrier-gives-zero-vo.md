---
# qou-qydm
title: 'GAP: neutrino masses (3) — unknot carrier gives zero Vol; no mechanism for nonzero splittings'
status: in-progress
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-07-31T20:15:08Z
updated_at: 2026-10-10T07:15:53Z
parent: qou-8lxd
blocked_by:
    - qou-x4qm
pr: 8232
---

## 🔥 Roast (2026-09-03, qou-bsu0)

(i) Needs a mass mechanism outside the volume–density chain, and a carrier that can carry lepton number.
(ii) Excluded: volume–density on any hyperbolic carrier — the minimum Vol(4₁) puts the scale ≥ ~260 MeV, ~10¹⁰ above 0.05 eV (scope-b, Cao–Meyerhoff; `neutrino-mass-volume-exclusion.witness.json`); the unknot gives Vol = CS = 0; and the unknot is amphichiral, so ν (L = +1) and ν̄ (L = −1) are the same knot — no function of unframed knot type reproduces the L table (scope-b, `LeptonNumberCarrierChirality.lean`, no axioms; `qou-kl39`). Exactly two repairs: a chiral carrier, or L on framed knots.
(iii) Trap: a seesaw with a hand-picked heavy scale; a satellite of the unknot chosen to hit Δm²; Dirac vs Majorana asserted.
(iv) Next: decide the carrier repair (framing = `def:strand-twist-datum`, the same object hypercharge wants); three masses then need three generations (`qou-x4qm`). Not near-term.
(v) Forecast: no splitting number without a new mechanism class; the carrier obstruction is the only tractable piece.
Tower status [reading: qou-ggdk]: ORDER-ZERO-ONLY — the exclusion is of the leading volume term on a Vol = 0 carrier; a tower-level correction (per-braid q-volume / Habiro tail of the unknot) is exactly the "mechanism outside the chain", and none is formulated.

## Implementation Note (PR #8232)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/HeavyQuarkDoubletObstructionFreezeOutTruncationWeinbergBlockNormCkmParameterCountAndNeutrinoZeroVolume.lean` and `computations/probes/heavy_quark_doublet_obstruction_freeze_out_truncation_weinberg_block_norm_ckm_parameter_count_and_neutrino_zero_volume_probe.py` (witness `computations/probes/heavy-quark-doublet-obstruction-freeze-out-truncation-weinberg-block-norm-ckm-parameter-count-and-neutrino-zero-volume.witness.json`, `5c9df8778eb7e1128541cebe1318fc29ba5b5b7e`).
