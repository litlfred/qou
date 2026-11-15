---
# qou-52sn
title: Harden the 5_2 boundary-slope / connection-count data (SnapPy) — Route-A cross-knot gate currently uses literature-recalled values
status: completed
type: task
priority: normal
tags:
    - g3-aomega
created_at: 2026-08-11T00:35:00Z
updated_at: 2026-10-10T08:30:00Z
parent: qou-rt0a
---

The Route-A cross-knot refutation (qou-rt0a: 5_2 max boundary slope 10 ∉ DT {3,4}, so the slope=DT reading is refuted) rests on LITERATURE-recalled 5_2 data: boundary slopes {0,-4,-10}, #boundary-parabolic connections = 4. SnapPy was unavailable in the session. Verify with snappy.Manifold('5_2') (boundary_slopes / A-polynomial L-degree) before hardening the refutation. If the literature values are wrong the R2-refuted / R1-survives split may shift.

HARDENED 2026-09-07 without SnapPy: the 5_2 inputs are now DERIVED from the corpus's own A_{5_2} (two_bridge_cusp_rows_apoly_probe.py, #6985, Farey word RL, meridian by the Dehn-filling test). Slopes {-10,-4,0} (derived frame; the literature's {0,4,10} is the mirror), geometric L-degree 3, full 4 — equal to the recalled values, asserted in the Route-A probe (derived == recalled) and proved in RouteANewtonPolygonDT (a52_edge_slopes_in_0_m4_m10, fiveTwoMaxAbsSlope_derived, fiveTwoConnections_eq_four). R2 refuted / R1 survives is now unconditional on any recalled table. Audit: 2026-09-06-two-bridge-layering-from-farey-word.md §3b.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** Hardening landed and the Lean twin compiles. The full probe re-run takes over 5 min, so the 5₂ half was not reproduced on 2026-10-10. The witness stands.

Evidence: `two-bridge-cusp-rows-apoly.witness.json` (2026-09-07, dps 70, allPassed) passes `fivetwo_slopes_are_0_4_10_up_to_mirror` and `fivetwo_apoly_recovered`. `RouteANewtonPolygonDT.lean` is Mathlib-free, sorry-free, and compiled exit 0 with `lean425/bin/lean` (Lean 4.25; the repo pins 4.24). It contains `a52_edge_slopes_in_0_m4_m10`, `fiveTwoConnections_eq_four`. The probe re-run timed out at 300 s (exit 124) after all 4₁ assertions PASSed, before reaching 5₂.

Status: `completed` → `completed` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.
