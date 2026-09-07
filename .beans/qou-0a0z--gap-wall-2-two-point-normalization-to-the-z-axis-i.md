---
# qou-0a0z
title: 'GAP WALL-2: two-point normalization to the z-axis (isometry composition)'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:03:26Z
updated_at: 2026-08-16T14:01:53Z
---

T2 geodesic-uniqueness, WALL-2. Uses WALL-1 (LANDED: HyperbolicIsometryAffine.lean
— dilation, horizontal translation, height-fixing rotation, all dH-isometries).

EASY part (achievable now via WALL-1, ~5 lines): ONE point x ∈ upperH maps to the
z-axis point zpt (x 2) by the horizontal translation by b = -(x0,x1,0) (b_z=0);
dH preserved by dH_horizTranslation.

HARD/OPEN part (the substance): map TWO arbitrary points x,y ∈ upperH to z-axis
points SIMULTANEOUSLY by a composition of WALL-1 isometries + a boundary inversion
(dH_boundaryInversion, LANDED). Classical construction: after translating x to the
z-axis, the unique geodesic semicircle through x,y meets ∂H³ at two boundary points;
invert at one of them to send that geodesic to the vertical z-axis line, carrying
y to a z-axis point. Formalizing requires: existence/《construction》of the boundary
endpoints, the inversion center choice, and proving the image of y lands on
{p | p 0 = 0 ∧ p 1 = 0}. Genuinely involved (choosing the inversion center; the
semicircle→vertical-line image). This is the reduction WALL-5 transports uniqueness
through.

Depends conceptually on nothing (independent of WALL-3), but only USEFUL once
WALL-4 (z-axis uniqueness) exists to transport.



---
UPDATE 2026-08-16 (PR #5253): EASY one-point half CONFIRMED ALREADY LANDED on main as
exists_horizTranslation_to_zAxis (HyperbolicGeodesicZAxis.lean) — a horizontal translation
carries any p∈H³ onto zpt(p₂), dH-preserved. Nothing to do there.
REMAINING (unchanged, the substance): map TWO arbitrary points to z-axis points simultaneously
via a boundary inversion (dH_boundaryInversion, landed) composed with WALL-1 generators
(HyperbolicIsometryAffine, landed). Needs: construct the two boundary endpoints of the
geodesic semicircle through x,y; choose the inversion center at one endpoint; prove the image
of y lands on {p | p 0 = 0 ∧ p 1 = 0}. Genuinely involved (multi-day); independent of xidi
but only USEFUL once xidi (z-axis uniqueness) exists to transport.
