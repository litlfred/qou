/-
  H3: the ideal tetrahedron as a REGION in upper half-space.

  This is `qou-5gai` H3, the step between the measure (H1/H2) and the volume
  computation (H4).  It is deliberately a small file: the risk in this tier is
  getting the DEFINITION right rather than convenient, so what is here is the
  definition, the facts that pin it down, and nothing else.

  MILNOR'S NORMALIZATION, followed exactly (Appendix of [milnor1982], now in
  `library/`):

    "We will use the Beltrami upper half-space model, with metric
     ds² = (dx² + dy² + dz²)/z² and associated volume element dx dy dz/z³,
     where z > 0.  Let us position the ideal simplex Δ so that one of its faces
     lies in the hemisphere z = (1 − x² − y²)^{1/2}, and its opposite vertex
     lies at the infinite point.  Projecting Δ orthogonally to the unit disk in
     the x,y-plane, we obtain a triangle inscribed in this disk with angles
     α, β, γ."

  Two things that quote settles, and they are worth recording:

  * **It confirms H1's measure.**  `dx dy dz / z³` on `z > 0` is exactly
    `HyperbolicVolume.hypVolume` -- so the object H2's invariances were proved
    about is the one Milnor computes with, not a lookalike.
  * **It makes the region a "chimney".**  With the far vertex at infinity the
    solid is unbounded upward, so it is `{(x,y) ∈ T} × {z > hemisphere}` -- and
    that product shape is precisely what lets H4-2 apply Fubini and H4-1 do the
    vertical fibre.  The generalisation below (arbitrary base `T`, arbitrary
    radius `R`) costs nothing and avoids baking "triangle" in before it is
    needed.

  WHAT IS *NOT* HERE -- read before citing.

  * **No triangle, no angles, no tetrahedron.**  `chimney` is defined over an
    ARBITRARY base set.  That the base is a Euclidean triangle inscribed in the
    disk with angles `(α, β, γ)`, and that the resulting solid IS the ideal
    tetrahedron of those dihedral angles, is Milnor's geometric identification
    -- not proved here, and not provable without hyperbolic geometry Mathlib
    does not have.  So nothing below is a statement about ideal tetrahedra; it
    is a statement about a region of `ℝ³`.
  * **No volume is computed** (H4-2 onward).  This file supplies the region and
    its vertical fibres; the Fubini reduction and the Λ-sum are open.
  * **The obtuse case is not addressed.**  Milnor's subdivision-from-the-origin
    argument is stated for "if all three angles are acute"; when the
    circumcentre falls outside the triangle the corresponding piece enters with
    a MINUS sign.  Nothing here depends on that yet, but H4-3/H4-5 will, and it
    is the flagged place to go wrong (`qou-w3eg`).
  * **Nothing wired.**  No mass, binding, or substrate claim.

  Archimedean (ℝ): `sqrt`, ordering -- §7c.

  -- Ref: [milnor1982] Appendix (the normalization quoted above)
  -- Ref: [thurston1978] Ch. 7
  -- Ref: [manuscript] beans qou-5gai (H3), qou-w3eg, qou-idvt (T2)
-/

import QOU.Archimedean.HyperbolicVolumeMeasure

namespace QOU.Archimedean.HyperbolicVolume

open MeasureTheory Set

/-- **The solid over a base set, above the hemisphere of radius `R`.**

Milnor's normalized position uses `R = 1`; the radius is left free because it
costs nothing and H4-1 (`integral_Ioi_hemisphere`) is already stated at general
`R`.

The far vertex sits at infinity, so this is unbounded upward -- a "chimney" over
`T`, not a bounded solid. That product shape is what H4-2's Fubini consumes. -/
def chimney (T : Set (ℝ × ℝ)) (R : ℝ) : Set (Fin 3 → ℝ) :=
  {p | (p 0, p 1) ∈ T ∧ Real.sqrt (R ^ 2 - (p 0) ^ 2 - (p 1) ^ 2) < p 2}

/-- The base-projection map `(x,y,z) ↦ (x,y)`. -/
def baseProj (p : Fin 3 → ℝ) : ℝ × ℝ := (p 0, p 1)

theorem measurable_baseProj : Measurable baseProj :=
  (measurable_pi_apply 0).prodMk (measurable_pi_apply 1)

theorem measurableSet_chimney {T : Set (ℝ × ℝ)} (hT : MeasurableSet T) (R : ℝ) :
    MeasurableSet (chimney T R) := by
  have h1 : MeasurableSet {p : Fin 3 → ℝ | (p 0, p 1) ∈ T} :=
    measurable_baseProj hT
  have h2 : MeasurableSet
      {p : Fin 3 → ℝ | Real.sqrt (R ^ 2 - (p 0) ^ 2 - (p 1) ^ 2) < p 2} := by
    refine measurableSet_lt ?_ (measurable_pi_apply 2)
    exact Real.continuous_sqrt.measurable.comp
      ((measurable_const.sub ((measurable_pi_apply 0).pow_const 2)).sub
        ((measurable_pi_apply 1).pow_const 2))
  exact h1.inter h2

/-- **Every chimney sits in the upper half-space** -- with no hypothesis on the
base at all.

`Real.sqrt` is non-negative even where its argument is (so outside the disk the
floor degenerates to `z > 0`), which is exactly what makes this unconditional.
That is a genuine convenience of the `Real.sqrt` convention rather than an
accident: it means the region never silently escapes `H³`. -/
theorem chimney_subset_upperHalfSpace (T : Set (ℝ × ℝ)) (R : ℝ) :
    chimney T R ⊆ upperHalfSpace := by
  rintro p ⟨-, hz⟩
  exact lt_of_le_of_lt (Real.sqrt_nonneg _) hz

/-- **The vertical fibre of a chimney is exactly a ray** -- the shape H4-1
integrates.

This is the bridge between H3 and H4: `integral_Ioi_hemisphere` computes
`∫ z in Ioi (√(R² − d²)), z⁻³ = 1/(2(R² − d²))`, and this says that ray IS the
fibre. H4-2 then only has to justify integrating fibrewise (Fubini). -/
theorem chimney_fibre {T : Set (ℝ × ℝ)} {R : ℝ} {p : Fin 3 → ℝ} (hp : (p 0, p 1) ∈ T) :
    (p ∈ chimney T R) ↔ p 2 ∈ Ioi (Real.sqrt (R ^ 2 - (p 0) ^ 2 - (p 1) ^ 2)) := by
  simp only [chimney, Set.mem_setOf_eq, Set.mem_Ioi]
  exact ⟨fun h => h.2, fun h => ⟨hp, h⟩⟩

/-! ### Non-vacuity

`chimney` over an empty base, or with the floor above every height, would be
empty and every later statement about it vacuous. -/

/-- A point of the base, lifted high enough, is in the chimney -- so a chimney
over a nonempty base is nonempty. -/
theorem chimney_nonempty {T : Set (ℝ × ℝ)} {R : ℝ} (hT : T.Nonempty) :
    (chimney T R).Nonempty := by
  obtain ⟨⟨x, y⟩, hxy⟩ := hT
  refine ⟨![x, y, Real.sqrt (R ^ 2 - x ^ 2 - y ^ 2) + 1], ?_, ?_⟩
  · simpa using hxy
  · simp

end QOU.Archimedean.HyperbolicVolume
