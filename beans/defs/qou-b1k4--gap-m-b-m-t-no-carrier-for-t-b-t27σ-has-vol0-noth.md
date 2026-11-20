---
# qou-b1k4
title: 'GAP: m_b, m_t — no carrier for t; b = T(2,7)^σ has Vol=0; nothing derived at any order'
status: todo
type: task
priority: normal
tags:
    - sm-26
    - reorg-2026-10-04
    - 8f-mass
created_at: 2026-09-03T08:31:18Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
blocked_by:
    - qou-qpj9
    - qou-x4qm
pr: 8232
---

Per-term bean for the bottom and top masses (session qou-ggdk, bean qou-bsu0). The dictionary assigns b = T(2,7)^σ (`unmapped-torus-knots.md`) and reassigns the top's T_{3,4} slot to "Hopf² colour binding; 'top quark' label deprecated" (`knot-formula-table-table2-data.md:13`); `signedWrithe .top = 7` survives only in `MesonOperatorSelectionT3.lean`. Gate: qou-qpj9 (4-C) for b; for t additionally qou-x4qm (a carrier presupposes the generation structure). Sibling of the m_s/m_c bean.

## 🔥 Roast (2026-09-03)

(i) Needs a top carrier (none exists) and, for both, a mass map off a Vol = 0 torus carrier — the same content→hyperbolic-braid map as m_s/m_c.
(ii) Excluded: nothing b/t-specific has been tested. Inherited: composite-volume candidates miss the bottom by ~40 % (`charm-composite-volume.witness.json`, scope-a); torus carriers carry zero volume-density mass (#4589). The b↔μ, c↔τ pairing crosses SM doublets (c,s), (t,b) (`qou-ypl2`) — unresolved.
(iii) Trap: quarkonium-style "Vol ≈ 2 m_b" census matches; a winding-7 tower ratio tuned to m_b/m_c; any top number at all, since nothing exists to check it against.
(iv) Next: not near-term. In order: the 4-C braid map, the doublet-pairing ruling, then a top carrier.
(v) Forecast: the last two of the 26 to move.
Tower status [reading: qou-ggdk]: no attack of either kind exists; by construction any b/t mass must be a tower object (the order-zero volume term is identically zero on the carrier) — no full-tower formulation in the corpus.

## Implementation Note (PR #8232)
- Implemented in `folio/quantum-observable-universe/lean/QOU/Eightfold/HeavyQuarkDoubletObstructionFreezeOutTruncationWeinbergBlockNormCkmParameterCountAndNeutrinoZeroVolume.lean` and `computations/probes/heavy_quark_doublet_obstruction_freeze_out_truncation_weinberg_block_norm_ckm_parameter_count_and_neutrino_zero_volume_probe.py` (witness `computations/probes/heavy-quark-doublet-obstruction-freeze-out-truncation-weinberg-block-norm-ckm-parameter-count-and-neutrino-zero-volume.witness.json`, `5c9df8778eb7e1128541cebe1318fc29ba5b5b7e`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8232, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
