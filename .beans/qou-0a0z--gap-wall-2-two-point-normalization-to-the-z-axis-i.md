---
# qou-0a0z
title: 'GAP WALL-2: two-point normalization to the z-axis (isometry composition)'
status: completed
type: task
priority: normal
created_at: 2026-08-16T13:03:26Z
updated_at: 2026-09-05T09:21:00Z
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


---

## CLOSED 2026-09-05 — WALL-2 landed sorry-free six days after this bean's last update

The bean's "HARD/OPEN part (the substance)" — carry TWO arbitrary points of `H³`
to the z-axis simultaneously — was **derived** in `c44c39dc669` (2026-08-21),
whose own subject says `bean qou-0a0z CLOSED`. The status was never moved.

Live on `main` `262ee53eeea`, in
`content/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicNormalization.lean`:

| declaration | line | what it is |
|---|---|---|
| `exists_normalization_vertical` | 136 | the shared-horizontal-part case |
| `exists_normalization_general_isom` | 276 | distinct horizontal parts, exposing the isometry |
| `exists_normalization_general` | 394 | the plain existence form |
| `exists_normalization` | — | **unconditional**, by case split on shared vs distinct |

**Sorry-free, verified rather than asserted:** `grep -n sorry` on that file
returns 11 hits and **all eleven are the string "sorry-free" inside docstrings**
— there is no `sorry` term. The landing commit records `#print axioms` on all
three new theorems giving `[propext, Classical.choice, Quot.sound]` only, no
`sorryAx`.

The construction avoided the step this bean called "genuinely involved
(multi-day)": no explicit geodesic-endpoint construction was needed. The
endpoint algebra reduces to the single sphere identity
`‖p − ξ‖² = 2R(α − (c−R))` with `ξ = (c−R)·u`, so only sphere membership of the
two interior points is required — the composition is
`T₃ ∘ T₂ ∘ T₁` (horizontal translation, boundary inversion at the near ideal
endpoint, horizontal translation), assembled through `IsDHIsometry.comp`.

Consumed downstream by `QOU.Archimedean.TotallyGeodesicUnconditional` (its
header cites WALL-2 as `HyperbolicNormalization.exists_normalization` /
`exists_normalization_isom`), which is the transport this bean said WALL-2
existed to feed.
