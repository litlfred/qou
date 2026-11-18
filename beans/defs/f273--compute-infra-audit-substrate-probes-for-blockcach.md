---
# f273
title: 'Compute infra: audit substrate probes for BlockCache/LaurentQ wiring + slow sympy simplify/cancel hotspots (compute-audit)'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-28T06:54:32Z
updated_at: 2026-10-04T15:18:00Z
parent: qou-5vkl
---


**2026-06-28:** Audit done — docs/audits/2026-06-28-substrate-probe-compute-audit.md. Findings: (1) 7 probes duplicate Young machinery → z3a2; (2) sp.simplify hotspots in lever1_lw_depth2 (6) + lever1_qinvolution (5) → simplify→cancel (queued); (3) BlockCache/LaurentQ N/A to this pure-sympy probe family (relevant to pyhecke producers — separate sub-scope, deferred).



**2026-06-28 applied:** simplify→cancel done on both hotspots — lever1_lw_depth2 (migrated to young_qdim + 6 simplify→cancel) + lever1_qinvolution (5 simplify→cancel); both re-run allPassed/verdict IDENTICAL.

- **Round 94 PR (`litlfred/qou#8500`)**: Formalized `SubstrateProbeCancelHotspotLedger`, `canonicalSubstrateProbeCancelHotspotLedger`, `substrate_cancel_two_square_composition`, and `round_ninety_four_joint_certificate` in `QOU.Foundations.LeafOleanConeBatchingDeferredStructuralCleanupSiblingVerificationClassificationFamilyChainErrorPartitionSubstrateProbeCancelHotspot` with 80-dps witness (`HEAD = 37841388326f8fad43c7ffaa9f1c59e901153736`).
