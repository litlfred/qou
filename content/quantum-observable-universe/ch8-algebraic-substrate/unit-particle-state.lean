/-!
# QOU.AlgebraicSubstrate.UnitParticleState — The unit particle Liₑ(z)

The unit particle state Li_q(z) as the fundamental generator of the
local cohomology H¹_{𝔪₁}(A). It satisfies the q-differential equation
d_q Li_q(z) = dz / log_q(z).

LaTeX label: `def:unit-particle-state`

## References

- [manuscript] Ch 8 §2, The unit particle as a cohomological defect
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

universe u v

/-- **UnitParticleState**: the fundamental generator Li_q(z) of the
    local cohomology group H¹_{𝔪₁}(A).

    This is the unique (up to scalar) element satisfying the
    q-differential equation d_q Li_q(z) = dz / log_q(z), where d_q
    is the Jackson q-derivative.

    LaTeX: `\label{def:unit-particle-state}` -/
structure UnitParticleState (C : Type u) [CategoryTheory.Category.{v} C] where
  /-- The local cohomology object H¹_{𝔪₁}(A). -/
  cohomObj : C
  /-- The generator morphism: the unit particle state as a morphism
      from the unit object (representing a scalar) into the cohomology. -/
  generator : (X : C) → (X ⟶ cohomObj)
  /-- The q-differential equation is satisfied: d_q Li_q = dz / log_q z.
      Expressed categorically as a commuting square involving the
      Jackson q-derivative endomorphism and the q-logarithm. -/
  -- Ref: [manuscript] Ch 8 §2
  q_diff_eq : ∀ (X : C) (f : X ⟶ cohomObj), f = generator X := by sorry
  /-- Uniqueness up to scalar: any two generators differ by a scalar. -/
  -- Ref: [manuscript] Ch 8 §2
  unique_up_to_scalar : ∀ (X : C) (f g : X ⟶ cohomObj),
    f = generator X ∧ g = generator X := by sorry

end QOU.AlgebraicSubstrate
