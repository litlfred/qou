---
# qou-6ers
title: Formalize multiplicative-integral/non-abelian Stokes for tm_transient_localisation
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-21T18:18:35Z
updated_at: 2026-11-17T08:19:19Z
parent: qou-c8p8
---



## Round 58 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8276 (`1909a7bd3bec6ebbdc594cc42f836c8a59fb6451`)
- **Module:** `QOU.Foundations.IsotypicBlockSpolyLaurentHolonomy` (`folio/quantum-observable-universe/lean/QOU/Foundations/IsotypicBlockSpolyLaurentHolonomy.lean`), wired into `QOU.lean`.
- **Theorem:** `flat_plaquette_holonomy_eq_one_and_gauge_invariant` — proves non-abelian multiplicative plaquette holonomy collapse `((hBot · hRight) · hTopInv) · hLeftInv = 1` under flat curvature `hBot · hRight = hLeft · hTop` and basepoint gauge conjugation invariance over a general non-commutative associative monoid `AssocMonoidCarrier G`, verified on `SU(2)` matrices at 80 dps in `isotypic-block-spoly-laurent-holonomy.witness.json`.
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
