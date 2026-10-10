---
# qou-u452
title: 'B3: join QGevreyTaming''s growth side to QBridgeSystem''s algebra'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T06:35:11Z
updated_at: 2026-10-04T15:16:36Z
parent: qou-frzo
---

**RE-SCOPED and DOWNGRADED (2026-09-07): still coherent, but no longer on the path to the binding gap.**

B3 asked to join `QGevreyTaming`'s growth side to `QBridgeSystem`'s algebra. That join was motivated as a step toward extracting the binding's many-body term from q-Stokes data. **That motivation is now excluded** — `QOU/Mass/BindingNoAlienPlane.lean` (sorry-free) shows the binding kernel `L_K` is pure isoclinic, and Ramis–Sauloy §2.2 says pure modules are "irregular objects without wild monodromy", so there are no q-alien derivations on it to join anything to. The classical side is closed independently by `BindingGevreyHalf` (Gevrey-1/2 ⇒ level-1 Borel entire).

The join may still be worth having as general infrastructure — growth class and bridge algebra are genuinely two halves of one theory — but it is now speculative infrastructure with no named consumer, and it should not be worked ahead of `qou-dk8a` (the connection-matrix route, the one surviving crack) or `qou-vkg5` (the resurgent-series instance, which is the real open half of the scrapped `qou-rae2`).

Leaving `todo`, not scrapped: nothing here is refuted, only de-prioritised.
