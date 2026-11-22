/-
# File A1 — geodesic planes of `H³` through boundary points, keyed on `∂H³ = ℂ ∪ {∞}`.

This is the FROM-THE-VERTICES foundation for making the ideal tetrahedron a genuine
independent object (beans `qou-idvt`, `qou-473l`).  The design rule is
non-negotiable: **a face is defined from the ideal vertices, and the chord data is
DERIVED from it — never the reverse.**  So here a boundary point is an element of
the one-point compactification `∂H³ = OnePoint (ℝ × ℝ)` (the plane `z = 0` plus the
far point `∞`), and `geodesicPlaneThrough a b c` builds the totally-geodesic plane
of `H³` spanned by three boundary points — with NO reference to `chordHalfplane` /
`inscribedTriangle`.  File A2 then DERIVES the chords from these vertex-defined
faces, and File A3 proves the resulting ideal tetrahedron equals the chimney.

## The residual cited fact (now narrowed — see status update)

-- Ref: [thurston1978] Ch. 2 §2.3 p. 10 ("a hyperbolic two-plane is a Euclidean
--   sphere orthogonal to [the boundary]") / [ratcliffe] §4.6–4.7 / [benedetti-petronio] §A —
--   in the upper half-space model the totally-geodesic planes ARE the vertical
--   Euclidean planes (perpendicular to `∂H³`) and the Euclidean hemispheres
--   centred on `∂H³`.  This file ADOPTS the concrete model to define the faces.
--
-- **Status update (T2 metric backfill, drained to the corpus faces).**  The two
--   adoptions this comment used to lean on alongside — `HyperbolicVolume.hypVolume
--   := dx dy dz / z³` and `hypAngle` — are joined by a genuinely DERIVED distance
--   `dH` (`QOU.Archimedean.HyperbolicMetric`, an infimum of hyperbolic path
--   lengths), and the vertical-plane / hemisphere totally-geodesic property is now
--   PROVED sorry-free, conditional on a single named conjecture, for the CONCRETE
--   corpus faces themselves — `verticalPlane n d` (any unit normal, any offset) and
--   `hemisphere R` — in `QOU.Archimedean.TotallyGeodesicFaces`
--   (`verticalPlane_isTotallyGeodesic`, `hemisphere_isTotallyGeodesic`), which feeds
--   the DERIVED boundary isometries into `HyperbolicGeodesic.fixedSet_isTotallyGeodesic`.
--   `verticalPlaneThrough b c` is such a vertical plane, so the geodesic-ness of the
--   faces cut here is drained (modulo the one wall).  What remains cited/open is now
--   ONLY geodesic existence + uniqueness in `H³` (`HypMinimizerUnique`, bean
--   `qou-r111`); the *concrete-model* definitions here still carry no `axiom` and no
--   `sorry`.

## What is defined here

* `BdryPoint := OnePoint (ℝ × ℝ)` — a boundary point of `H³`; `∞` is the far point.
* `sarea u v w` — twice the signed area of the Euclidean triangle `(u,v,w)`; the
  building block of both the vertical-plane equation and its oriented half-space.
* `verticalPlaneThrough b c` — the vertical plane over the Euclidean line through
  the finite points `b, c`; this IS `geodesicPlaneThrough ∞ b c`.
* `geodesicPlaneThrough a b c` — the geodesic plane through three boundary points:
  a vertical plane when one argument is `∞`, and (for the Milnor-normalized target)
  the **unit hemisphere** when all three are finite.  The GENERAL finite-triple case
  is the circumscribed hemisphere of the three points; that general circumhemisphere
  is DEFERRED (a `TODO` below, NOT a `sorry`) because it is not needed for the
  normalized target, where the three finite vertices lie on the unit circle and
  their circumcircle is therefore the unit circle.

Archimedean (ℝ): coordinates, `Real.sqrt` via `hemisphere` — §7c.

  -- Ref: [milnor1982] Appendix (Milnor's normalized position: one face on the unit
  --   hemisphere, opposite vertex at `∞`)
  -- Ref: [thurston1978] Ch. 7 ; [ratcliffe] §4.6–4.7
  -- Ref: [leitner2026] beans qou-idvt (T2), qou-473l (T2 vertex-independence)
-/

import QOU.Archimedean.GeodesicFaceH3
import Mathlib.Topology.Compactification.OnePoint.Basic

namespace QOU.Archimedean

open scoped OnePoint

/-- **A boundary point of `H³`.**  `∂H³` is the plane `z = 0` (identified with
`ℝ × ℝ`, i.e. `ℂ`) together with the single far point `∞` — its one-point
compactification.  The four ideal vertices of an ideal tetrahedron are four
`BdryPoint`s. -/
abbrev BdryPoint := OnePoint (ℝ × ℝ)

/-- **Twice the signed area** of the Euclidean triangle `(u, v, w)` — equivalently
the 2-D cross product of `v - u` and `w - u`.  It vanishes exactly when `w` lies on
the line through `u` and `v`, and its sign says which side of that line `w` is on.
This single scalar carries both the vertical-plane equation (`= 0`) and its oriented
half-space (sign), so the whole vertical-face story is expressed through it. -/
def sarea (u v w : ℝ × ℝ) : ℝ :=
  (v.1 - u.1) * (w.2 - u.2) - (v.2 - u.2) * (w.1 - u.1)

/-- `sarea` written out as an affine functional of its last argument:
`sarea u v w = (u.2 − v.2)·w.1 + (v.1 − u.1)·w.2 + (u.1 v.2 − u.2 v.1)`. -/
theorem sarea_affine (u v w : ℝ × ℝ) :
    sarea u v w = (u.2 - v.2) * w.1 + (v.1 - u.1) * w.2 + (u.1 * v.2 - u.2 * v.1) := by
  simp only [sarea]; ring

/-- Swapping the two spanning points negates the signed area. -/
theorem sarea_swap (u v w : ℝ × ℝ) : sarea v u w = - sarea u v w := by
  simp only [sarea]; ring

/-! ### Vertical planes through `∞` and two finite boundary points -/

/-- **The vertical geodesic plane through `∞`, `b`, `c`** (`b, c` finite): the
Euclidean vertical plane over the line through `b` and `c` in `∂H³`.  A point of
`ℝ³` lies on it iff its horizontal projection is on that line, i.e. iff the signed
area of `(b, c, projection)` vanishes — at ANY height, which is what "vertical"
means.  (This is `geodesicPlaneThrough ∞ b c`; the geodesic classification above is
the sole cited input.) -/
def verticalPlaneThrough (b c : ℝ × ℝ) : Set (Fin 3 → ℝ) :=
  {p | sarea b c (p 0, p 1) = 0}

/-- **The oriented vertical half-space** cut by `verticalPlaneThrough b c`, on the
side of the far vertical line over the finite reference point `i`.  A point is in it
iff its projection lands strictly on the same side of the line `bc` as `i` does —
detected by the two signed areas having the same (nonzero) sign, i.e. positive
product.  In an ideal tetrahedron with a face through `∞, b, c`, the interior
reference `i` is the opposite (fourth) vertex, so this is the half-space "toward the
interior". -/
def verticalHalfSpaceThrough (b c i : ℝ × ℝ) : Set (Fin 3 → ℝ) :=
  {p | 0 < sarea b c i * sarea b c (p 0, p 1)}

/-- The oriented half-space lies on one side of its plane: on the plane the signed
area is `0`, so the defining strict product cannot be positive.  (A sanity link
between the half-space and its bounding geodesic plane, both defined from the same
two vertices.) -/
theorem verticalHalfSpaceThrough_disjoint_plane (b c i : ℝ × ℝ) :
    Disjoint (verticalHalfSpaceThrough b c i) (verticalPlaneThrough b c) := by
  rw [Set.disjoint_left]
  rintro p hp hpl
  simp only [verticalHalfSpaceThrough, Set.mem_setOf_eq] at hp
  simp only [verticalPlaneThrough, Set.mem_setOf_eq] at hpl
  rw [hpl, mul_zero] at hp
  exact lt_irrefl 0 hp

/-! ### The geodesic faces used downstream

The load-bearing geodesic faces are `verticalPlaneThrough` / `verticalHalfSpaceThrough`
(above) and `hemisphere` / `hemisphereExterior` (`GeodesicFaceH3`); `idealTetrahedron`
(`IdealTetFromVertices`) is their intersection.  A general
`geodesicPlaneThrough a b c` three-boundary-point constructor was removed as unused
infrastructure (nothing downstream consumed it, and its finite-triple slot was only
correct in Milnor normalization).  The upcoming hyperbolic-metric backfill (draining
the totally-geodesic *citation* into a *proof*) rebuilds this layer directly on the
metric. -/

end QOU.Archimedean
