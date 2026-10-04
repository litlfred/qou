---
# qou-ykt7
title: 'GAP WALL-5: assemble HypMinimizerUnique instance (needs WALL-2 + WALL-4)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-16T13:03:26Z
updated_at: 2026-10-04T15:19:33Z
parent: qou-c8p8
---

T2 geodesic-uniqueness, WALL-5 — the capstone. Produce the REAL instance
  instance : QOU.Archimedean.HypMinimizerUnique
in HyperbolicGeodesic.lean, making verticalPlaneFix_isTotallyGeodesic and
hemisphereFix_isTotallyGeodesic UNCONDITIONAL (drains T2 to zero cite).

STRICT: do NOT fabricate this instance. It is only valid once BOTH prerequisites
are genuinely proved:
 - WALL-4 (bean qou-i0sr→WALL-4): z-axis constant-speed minimiser uniqueness.
 - WALL-2: two-point normalization to the z-axis by a dH-isometry.
Assembly: given x,y ∈ upperH and two minimisers γ,δ, apply the WALL-2 normalizing
isometry Φ (a dH-isometry, so Φ∘γ, Φ∘δ are minimisers between z-axis points —
uses IsDHIsometry.pathLenH_comp + speed_comp, already in HyperbolicMetric.lean),
invoke WALL-4 to get Φ∘γ = Φ∘δ pointwise, then apply Φ⁻¹ (also a dH-isometry) to
conclude γ = δ. The transport is mechanical GIVEN WALL-2 + WALL-4.

Current honest state: HypMinimizerUnique is a content-bearing conjecture class with
NO instance (the wall is OPEN). Existence of minimisers is ALSO part of the wall
(WALL-3 lower bound qou-i0sr gives vseg's `minimal` field ⇒ existence on the z-axis;
WALL-2 transports existence to general points). Until WALL-2+WALL-4 land, the
instance stays absent and the classification stays conditional — as it is now.



---
UPDATE 2026-08-16 (PR #5253): STILL OPEN — instance deliberately NOT fabricated. Both
prerequisites remain open: xidi (z-axis constant-speed uniqueness, equality-case analysis)
and 0a0z (two-point boundary-inversion normalization). HypMinimizerUnique stays a
content-bearing conjecture class with NO instance (correct honest state). The assembly
(transport uniqueness through the normalizing isometry via IsDHIsometry.pathLenH_comp/
speed_comp) is mechanical GIVEN xidi+0a0z, but neither has landed, so the classification
(verticalPlaneFix/hemisphereFix_isTotallyGeodesic) stays conditional on [HypMinimizerUnique].
Landed toward the wall this session (PR #5253): dH is now a CERTIFIED METRIC (dH_eq_zero_eq,
unconditional) and the EXACT z-axis distance dH_zpt. These are the metric foundation the
uniqueness argument sits on, but do not by themselves close WALL-4/WALL-5.
