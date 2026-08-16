---
# qou-xidi
title: 'GAP WALL-4: z-axis geodesic uniqueness (needs WALL-3 lower bound)'
status: todo
type: task
created_at: 2026-08-16T13:03:26Z
updated_at: 2026-08-16T13:03:26Z
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
