/-!
# QOU.Descent — Descent along the brane tower

Descent is the reverse traversal of the tower: from level n to
level n-1 via the restriction morphism rₙ.

## References

- [leitner2026] §3 Lifting and Descent
-/

import Mathlib.Algebra.Module.Basic

namespace QOU

variable {R : Type*} [CommRing R]

/-- Descent data at a single level: the restriction map with retraction.

    LaTeX: `\label{def:descent}` -/
-- Ref: [leitner2026] §3, Definition: Descent
structure DescentData (M N : Type*) [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N] where
  /-- The restriction (descent) map rₙ : Aₙ → A_{n-1}. -/
  restriction : M →ₗ[R] N
  /-- The ascent embedding ℓₙ : A_{n-1} → Aₙ (jet prolongation). -/
  embedding : N →ₗ[R] M
  /-- Retraction: restriction ∘ embedding = id. -/
  retraction : restriction ∘ₗ embedding = LinearMap.id

end QOU
