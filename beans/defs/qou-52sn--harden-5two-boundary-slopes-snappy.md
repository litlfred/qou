---
# qou-52sn
title: Harden the 5_2 boundary-slope / connection-count data (SnapPy) — Route-A cross-knot gate currently uses literature-recalled values
status: completed
type: task
priority: normal
tags:
    - g3-aomega
created_at: 2026-08-11T00:35:00Z
updated_at: 2026-09-07T09:35:37Z
parent: qou-rt0a
---

The Route-A cross-knot refutation (qou-rt0a: 5_2 max boundary slope 10 ∉ DT {3,4}, so the slope=DT reading is refuted) rests on LITERATURE-recalled 5_2 data: boundary slopes {0,-4,-10}, #boundary-parabolic connections = 4. SnapPy was unavailable in the session. Verify with snappy.Manifold('5_2') (boundary_slopes / A-polynomial L-degree) before hardening the refutation. If the literature values are wrong the R2-refuted / R1-survives split may shift.

HARDENED 2026-09-07 without SnapPy: the 5_2 inputs are now DERIVED from the corpus's own A_{5_2} (two_bridge_cusp_rows_apoly_probe.py, #6985, Farey word RL, meridian by the Dehn-filling test). Slopes {-10,-4,0} (derived frame; the literature's {0,4,10} is the mirror), geometric L-degree 3, full 4 — equal to the recalled values, asserted in the Route-A probe (derived == recalled) and proved in RouteANewtonPolygonDT (a52_edge_slopes_in_0_m4_m10, fiveTwoMaxAbsSlope_derived, fiveTwoConnections_eq_four). R2 refuted / R1 survives is now unconditional on any recalled table. Audit: 2026-09-06-two-bridge-layering-from-farey-word.md §3b.
