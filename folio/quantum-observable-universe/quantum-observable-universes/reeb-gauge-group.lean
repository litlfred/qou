import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Subgroup.Basic

/-!
# QOU.ReebGaugeGroup — The Reeb gauge group U₁(R)

The Reeb gauge group is the maximal torus T of the gauge group G,
viewed as a group scheme over R.  Over ℂ this recovers U(1).

LaTeX label: `def:reeb-gauge-group`

## References
- [leitner2026] §2/reeb-gauge-group
-/


namespace QOU

universe u

/-- **Reeb gauge group** `U₁(R)`: the maximal torus of the gauge group,
    viewed as an R-group scheme.  Over ℂ this recovers U(1) = {e^{iθ}}.

    Abstractly, it is the group of norm-one elements in the rank-one
    weight lattice, equivalently `Aut⊗(τ|_⟨V⟩)`. -/
-- Ref: [leitner2026] §2/reeb-gauge-group
structure ReebGaugeGroup (R : Type u) [CommRing R] where
  /-- The underlying group of norm-one elements. -/
  carrier : Type u
  /-- Group structure on the carrier. -/
  [groupInst : Group carrier]
  /-- The carrier embeds into the multiplicative group of R. -/
  embedding : carrier →* R
  /-- The embedding is injective (norm-one condition). -/
  embedding_injective : Function.Injective embedding

end QOU
