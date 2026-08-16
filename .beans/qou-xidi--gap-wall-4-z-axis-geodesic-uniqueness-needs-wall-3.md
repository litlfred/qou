---
# qou-xidi
title: 'GAP WALL-4: z-axis geodesic uniqueness (needs WALL-3 lower bound)'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:03:26Z
updated_at: 2026-08-16T14:01:53Z
---

T2 geodesic-uniqueness, WALL-4. DEPENDS ON WALL-3 lower bound (bean qou-i0sr).

OPEN: a constant-speed IsHypMinimizer γ between two z-axis points (0,0,a),(0,0,b)
is pointwise the vertical segment vseg a b. Mechanism: equality in the WALL-3
lower-bound chain (qou-i0sr) is only attained when
 (i) ‖γ'(t)‖ = |(γ' t) 2| a.e. ⇒ the horizontal components of γ' vanish ⇒ γ's
     x,y coordinates are constant = 0 (they are 0 at the endpoints on the z-axis);
 (ii) z monotone (z' does not change sign) so |∫ (log∘z)'| = ∫ |(log∘z)'|;
 (iii) constant speed |z'|/z ≡ const pins z(t) = a·(b/a)^t exactly ⇒ γ = vseg.
Blocked until qou-i0sr lands (the equality-case analysis is meaningless without
the inequality it saturates). Then this is the strict-convexity / equality-case
argument: substantial but mechanical once the lower bound exists.

Landed prerequisite: HyperbolicGeodesicZAxis.lean has vseg, hypSpeed_vseg_eq
(constant speed), admissiblePath_vseg — the target the uniqueness pins to.



---
UPDATE 2026-08-16 (PR #5253): DEPENDENCY CLEARED, still OPEN. WALL-3 lower bound (qou-i0sr)
landed, so the EXACT z-axis distance dH_zpt = ofReal|log(b/a)| is now available, and
pathLenH_vseg_eq_dH gives vseg's minimal field. The certified metric (dH_eq_zero_eq, PR
#5253) is also available now.

REMAINING (the equality-case analysis; tractable but ~400-600 lines, NOT attempted this
session to avoid a stalled half-proof): a constant-speed IsHypMinimizer γ from zpt a to
zpt b equals vseg a b pointwise. Exact steps:
 (a) HORIZONTAL COLLAPSE. From minimality pathLenH γ = ofReal|log(b/a)| and the lower-bound
     chain ∫‖γ'‖/z ≥ ∫|z'|/z ≥ |∫z'/z| = |log(b/a)|, equality forces ∫(‖γ'‖-|z'|)/z = 0 with
     nonneg integrand ⇒ (Mathlib integral_eq_zero_iff_of_nonneg_ae) ‖γ'‖ = |z'| a.e. ⇒ the
     two horizontal components of γ' are 0 a.e. Each horizontal coord deriv is integrable
     (bounded by ‖γ'‖ = g·z, z bounded by height ceiling — REUSE height_le from PR #5253),
     so FTC-2 (intervalIntegral.integral_eq_sub_of_hasDerivAt) gives the coord constant;
     = 0 at t=0 (zpt a) ⇒ ≡ 0. [REUSE deriv_coord, abs_coord_le_norm, speedFn machinery.]
 (b) Z MONOTONE. Equality ∫|z'|/z = |∫z'/z| forces z'/z single-signed ⇒ z monotone.
 (c) CONSTANT-SPEED PINS z. constSpeed ‖γ'‖/z ≡ c ⇒ (with (a)) |z'|/z ≡ c ⇒ (log z)' ≡ ±c
     ⇒ z(t) = a·exp(±ct); endpoint z(1)=b pins ±c = log(b/a) ⇒ z = heightProfile ⇒ γ = vseg.
Mathlib tools confirmed present: integral_eq_zero_iff_of_nonneg_ae, ae_eq_of_ae_le_of_lintegral_le.
Blocker to closing the WALL (ykt7) is NOT xidi alone — 0a0z (boundary inversion) is also required.
