/-
# File A2 — the ideal tetrahedron as an intersection of geodesic half-spaces,
#           built FROM its four ideal vertices.

Given a far vertex `∞` and three finite boundary vertices `P₁, P₂, P₃ ∈ ∂H³` on the
unit circle (Milnor's normalized position), the ideal tetrahedron is the
intersection of its four geodesic half-spaces, each oriented toward the interior:

* the face `{∞, P₂, P₃}` opposite `P₁` — the vertical half-space
  `verticalHalfSpaceThrough P₂ P₃ P₁` (toward `P₁`);
* the face `{∞, P₁, P₃}` opposite `P₂` — `verticalHalfSpaceThrough P₁ P₃ P₂`;
* the face `{∞, P₁, P₂}` opposite `P₃` — `verticalHalfSpaceThrough P₁ P₂ P₃`;
* the face `{P₁, P₂, P₃}` opposite `∞` — the **exterior of the unit hemisphere**
  (`hemisphereExterior 1`), the side of `geodesicPlaneThrough P₁ P₂ P₃ = hemisphere 1`
  that contains `∞` (points high above the cap).

**Every face is built from the vertices.**  The three vertical faces are the File-A1
`verticalHalfSpaceThrough` of pairs of vertices oriented by the opposite vertex; the
hemisphere face is the unit hemisphere, which is the geodesic plane through the three
finite vertices precisely because they lie on the unit circle
(`vertices_on_unit_hemisphere`).  Nothing here mentions `chordHalfplane` or
`inscribedTriangle` — those are DERIVED downstream (File A3), never assumed.

The geometric engine is `sarea_circlePoint_unit`: the signed area of a chord of the
unit circle against any point is `2 sin ψ · (cos ψ − w·nθ)` — the exact quantity a
`chordHalfplane` tests.  File A3 turns this into the region identity
`idealTetrahedron = chimney`.

Archimedean (ℝ): `sin`, `cos`, `Real.sqrt`, ordering — §7c.

  -- Ref: [milnor1982] Appendix ; [thurston1978] Ch. 7 ; [ratcliffe] §4.6–4.7
  -- Ref: [leitner2026] beans qou-idvt (T2), qou-473l (T2 vertex-independence)
-/

import QOU.Archimedean.IdealBoundaryGeodesicPlane
import QOU.Archimedean.OrthoschemeTiling

namespace QOU.Archimedean

open Real
open QOU.Archimedean.HyperbolicVolume

/-! ### The signed-area reduction — the one geometric identity everything rests on -/

/-- **The signed area of a unit-circle chord against a point is `2 sin ψ (cos ψ − w·nθ)`.**

For two points of the unit circle at central angles `u` and `u + 2ψ`, the chord's
perpendicular-bisector direction is `u + ψ` and it subtends half-angle `ψ`.  Testing
any `w` against the chord (its signed area) is `2 sin ψ` times `cos ψ − w·(cos(u+ψ),
sin(u+ψ))` — i.e. `2 sin ψ` times exactly the functional the chord half-plane
`{w · (cos(u+ψ), sin(u+ψ)) < cos ψ}` compares to `0`.  This is the bridge from the
vertex-defined `sarea` half-spaces (File A1) to the chord half-planes
(`OrthoschemeTiling`): it lets File A3 derive the chords from the faces. -/
theorem sarea_circlePoint_unit (u ψ : ℝ) (w : ℝ × ℝ) :
    sarea (circlePoint 1 u) (circlePoint 1 (u + 2 * ψ)) w
      = 2 * Real.sin ψ * (Real.cos ψ - (w.1 * Real.cos (u + ψ) + w.2 * Real.sin (u + ψ))) := by
  simp only [sarea, circlePoint]
  have e1 : Real.cos (u + 2 * ψ) = Real.cos (u + ψ) * Real.cos ψ - Real.sin (u + ψ) * Real.sin ψ := by
    rw [show u + 2 * ψ = (u + ψ) + ψ by ring, Real.cos_add]
  have e2 : Real.sin (u + 2 * ψ) = Real.sin (u + ψ) * Real.cos ψ + Real.cos (u + ψ) * Real.sin ψ := by
    rw [show u + 2 * ψ = (u + ψ) + ψ by ring, Real.sin_add]
  have e3 : Real.cos u = Real.cos (u + ψ) * Real.cos ψ + Real.sin (u + ψ) * Real.sin ψ := by
    have h := Real.cos_sub (u + ψ) ψ; rw [show (u + ψ) - ψ = u by ring] at h; exact h
  have e4 : Real.sin u = Real.sin (u + ψ) * Real.cos ψ - Real.cos (u + ψ) * Real.sin ψ := by
    have h := Real.sin_sub (u + ψ) ψ; rw [show (u + ψ) - ψ = u by ring] at h; exact h
  rw [e1, e2, e3, e4]
  linear_combination (2 * Real.sin ψ * Real.cos ψ) * Real.sin_sq_add_cos_sq (u + ψ)

/-! ### The hemisphere face, oriented toward `∞` -/

/-- **The exterior of the hemisphere of radius `R`** — its `∞`-side.  A point is in
it iff it sits strictly above the spherical cap `z = √(R² − x² − y²)`; because the far
vertex `∞` is reached by going upward, this is the side of the geodesic plane
`hemisphere R` that contains `∞`.  It is definitionally the floor condition of the
chimney (`IdealTetrahedronRegion`), which is what makes the File-A3 identification land
on the nose. -/
def hemisphereExterior (R : ℝ) : Set (Fin 3 → ℝ) :=
  {p | Real.sqrt (R ^ 2 - (p 0) ^ 2 - (p 1) ^ 2) < p 2}

/-- The hemisphere face and its `∞`-side exterior are disjoint: on the hemisphere the
cap height `√(R²−x²−y²)` EQUALS `z`, so the strict inequality of the exterior fails.
(A sanity link between the geodesic plane `hemisphere R` and the oriented half-space
`hemisphereExterior R` cut from it.) -/
theorem hemisphere_disjoint_hemisphereExterior {R : ℝ} :
    Disjoint (hemisphere R) (hemisphereExterior R) := by
  rw [Set.disjoint_left]
  rintro p hp hpe
  simp only [hemisphere, Set.mem_setOf_eq] at hp
  simp only [hemisphereExterior, Set.mem_setOf_eq] at hpe
  have hz : Real.sqrt (R ^ 2 - (p 0) ^ 2 - (p 1) ^ 2) = p 2 := by
    have : R ^ 2 - (p 0) ^ 2 - (p 1) ^ 2 = (p 2) ^ 2 := by linarith [hp.1]
    rw [this, Real.sqrt_sq hp.2.le]
  rw [hz] at hpe
  exact lt_irrefl _ hpe

/-! ### The ideal tetrahedron -/

/-- **The Milnor-normalized ideal tetrahedron with far vertex `∞` and three finite
vertices `P₁, P₂, P₃` on the unit circle**, as the intersection of its four geodesic
half-spaces, each oriented toward the interior.

Three vertical faces (each through `∞` and two finite vertices, oriented toward the
opposite vertex) and one hemisphere face (the unit hemisphere through the three finite
vertices, oriented toward `∞`).  This is an *independent* object: it is defined from
the four ideal vertices via File-A1 geodesic half-spaces, with **no** reference to
`chordHalfplane` or `inscribedTriangle`.  File A3 proves it equals the chimney.

The three finite vertices are taken on the unit circle (Milnor normalization), so the
hemisphere face is `hemisphere 1`; see `vertices_on_unit_hemisphere`.  For finite
vertices off the unit circle the hemisphere face would be their circumscribed
hemisphere — the deferred general case flagged in File A1. -/
def idealTetrahedron (P₁ P₂ P₃ : ℝ × ℝ) : Set (Fin 3 → ℝ) :=
  hemisphereExterior 1
    ∩ verticalHalfSpaceThrough P₂ P₃ P₁
    ∩ verticalHalfSpaceThrough P₁ P₃ P₂
    ∩ verticalHalfSpaceThrough P₁ P₂ P₃

/-- Membership in the ideal tetrahedron unfolded to its four half-space conditions. -/
theorem mem_idealTetrahedron {P₁ P₂ P₃ : ℝ × ℝ} {p : Fin 3 → ℝ} :
    p ∈ idealTetrahedron P₁ P₂ P₃ ↔
      p ∈ hemisphereExterior 1
      ∧ p ∈ verticalHalfSpaceThrough P₂ P₃ P₁
      ∧ p ∈ verticalHalfSpaceThrough P₁ P₃ P₂
      ∧ p ∈ verticalHalfSpaceThrough P₁ P₂ P₃ := by
  simp only [idealTetrahedron, Set.mem_inter_iff]
  tauto

/-- **The three finite vertices lie on the unit hemisphere's boundary circle** — the
justification that `hemisphere 1` is `geodesicPlaneThrough P₁ P₂ P₃` for the
normalized position (the vertices' circumcircle IS the unit circle).  Together with
the cited totally-geodesic classification (File A1), this is why the hemisphere face
of the tetrahedron is the unit hemisphere. -/
theorem vertices_on_unit_hemisphere (a : ℝ) :
    (circlePoint 1 a).1 ^ 2 + (circlePoint 1 a).2 ^ 2 = 1 := by
  simp only [circlePoint, one_mul]
  exact Real.cos_sq_add_sin_sq a

end QOU.Archimedean
