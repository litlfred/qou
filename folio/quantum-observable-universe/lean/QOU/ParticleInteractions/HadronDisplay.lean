import QOU.KnotTheory
import QOU.Archimedean.GroundRing


/-!
# QOU.ParticleInteractions.HadronDisplay

Authoritative library home for the `Hadron` structure, previously
defined only inside the content-object display snippet
`particle-interactions/hadron.lean`.  Relocated here (2026-06-09 axiom
audit) so the companion `hadron-unique.lean` display file can `import`
the real structure and carry a genuinely type-checked uniqueness
statement.

Ground ring `R_q = ℤ[q, q⁻¹]` from `QOU.Archimedean.GroundRing`;
`BraidWord` from `QOU.KnotTheory`.

## References

- [leitner2026] §3, Definition: Hadron
- [jones1987] Hecke Algebra Representations of Braid Groups
-/

namespace QOU

/-- A **hadron**: a common base point on `S²` (spherical coordinates
    `θ, φ`) together with its constituent knot types (valence quarks
    in the knot picture), of which there must be at least two. -/
-- Ref: [leitner2026] §3, Definition: Hadron
structure Hadron where
  /-- Spherical coordinate `θ` of the common base point. -/
  theta : Archimedean.R_q
  /-- Spherical coordinate `φ` of the common base point. -/
  phi : Archimedean.R_q
  /-- The constituent knot types. -/
  constituents : List KnotTheory.BraidWord
  /-- A hadron must have at least 2 constituents. -/
  constituents_nonempty : constituents.length ≥ 2

/-- The common base point `(θ, φ)` on `S²`. -/
def basePoint (h : Hadron) : Archimedean.R_q × Archimedean.R_q :=
  (h.theta, h.phi)

end QOU
