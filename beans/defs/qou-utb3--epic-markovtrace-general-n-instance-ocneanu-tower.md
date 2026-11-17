---
# qou-utb3
title: MarkovTrace general-n instance — Ocneanu tower route (unblocks TauFunctorReduction F-laws)
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-11-17T08:12:13Z
parent: qou-rtxm
---


Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: MarkovTrace general-n instance — Ocneanu tower route (unblocks TauFunctorReduction F-laws)


## Round 57 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8254 (`e9795825b5e02ba1c5315e9cbd5d10db4bc08957`)
- **Module:** `QOU.Foundations.OcneanuTowerConventionDRibbonClebschGordan` (`folio/quantum-observable-universe/lean/QOU/Foundations/OcneanuTowerConventionDRibbonClebschGordan.lean`), wired into `QOU.lean`.
- **Theorem:** `tower_peel_two_step_and_tensor_flaw` — proves two-step strand-tower peel reduction `tr((x · g_{n+1}) · g_n) = z² · tr(x)` and tensor F-law multiplicativity `tr(x · g_n) · tr(y · g_m) = z² · (tr(x) · tr(y))` over generic `GenericRingOps R`, verified at 80 dps in `ocneanu-tower-convention-d-ribbon-clebsch-gordan.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
