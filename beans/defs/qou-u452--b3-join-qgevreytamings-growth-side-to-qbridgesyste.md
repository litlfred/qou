---
# qou-u452
title: 'B3: join QGevreyTaming''s growth side to QBridgeSystem''s algebra'
status: todo
pr: 8199
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T06:35:11Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-frzo
---

**RE-SCOPED and DOWNGRADED (2026-09-07): still coherent, but no longer on the path to the binding gap.**

B3 asked to join `QGevreyTaming`'s growth side to `QBridgeSystem`'s algebra. That join was motivated as a step toward extracting the binding's many-body term from q-Stokes data. **That motivation is now excluded** — `QOU/Mass/BindingNoAlienPlane.lean` (sorry-free) shows the binding kernel `L_K` is pure isoclinic, and Ramis–Sauloy §2.2 says pure modules are "irregular objects without wild monodromy", so there are no q-alien derivations on it to join anything to. The classical side is closed independently by `BindingGevreyHalf` (Gevrey-1/2 ⇒ level-1 Borel entire).

The join may still be worth having as general infrastructure — growth class and bridge algebra are genuinely two halves of one theory — but it is now speculative infrastructure with no named consumer, and it should not be worked ahead of `qou-dk8a` (the connection-matrix route, the one surviving crack) or `qou-vkg5` (the resurgent-series instance, which is the real open half of the scrapped `qou-rae2`).

Leaving `todo`, not scrapped: nothing here is refuted, only de-prioritised.

## Progress (PR #8199)
- [x] Formalized in `folio/quantum-observable-universe/lean/QOU/MassTheory/RouteCDTChiralityAndQBridgeTaming.lean` (`0` `sorry`, `0` `axiom`, `0 CRITICAL, 0 advisory` across all 7 static vacuity/borrowed-name audits) and wired into `QOU.lean`.
- [x] Verified exact rational witness in `computations/probes/route-c-dt-chirality-and-qbridge-taming.witness.json` (`scriptHash: d89ffef0f347`, `scriptCommitSha: d6aa2e9463a3ba079ec1d472e356f34252ece779`, `allPassed: true`, `0` raw `float64` fields).
- [ ] Awaiting Merge Manager merge of PR #8199 (`1f4bf9af7d58a057599a62f5a8d42748dc742ea8`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8199, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
