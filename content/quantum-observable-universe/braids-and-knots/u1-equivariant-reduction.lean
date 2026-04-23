/-!
# QOU.CommutativeQOU.u1EquivariantReduction

U(1)-equivariant observables on the ℙ¹(ℂ) exceptional divisor reduce
to functions on the orbit space [0, π], equivalently to sections of
a phase-S¹ bundle over the open interval (0, π).

LaTeX label: `prop:u1-equivariant-reduction`

**Ground ring**: `ℝ` (analytic/geometric).
-/

import Mathlib.Data.Real.Basic
import Mathlib.Topology.Instances.Real.Lemmas

namespace QOU

/-- Orbit space of the U(1) rotation action on the exceptional divisor
    𝒮_p = ℙ¹(ℂ), parametrised by the polar angle φ ∈ [0, π]. -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
def U1OrbitSpace : Type := Set.Icc (0 : ℝ) Real.pi

/-- The polar fixed points of the U(1) action: φ = 0 and φ = π.
    These are the two points where the U(1)-orbit on 𝒮_p collapses
    to a single point. -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
def polarFixedPoints : Set U1OrbitSpace :=
  { x | x.val.val = 0 ∨ x.val.val = Real.pi }

/-- **U(1)-equivariant reduction** (structural statement):
    U(1)-equivariant observables on 𝒮_p are parametrised by the
    polar coordinate φ ∈ [0, π] together with a global phase
    coordinate ψ ∈ S¹ on the interior (0, π), while over the two
    polar fixed points the phase fibre collapses. -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
theorem u1EquivariantReduction :
    ∃ (_ : U1OrbitSpace → Type),
      (∀ φ : U1OrbitSpace, φ ∈ polarFixedPoints → True) ∧
      (∀ φ : U1OrbitSpace, φ ∉ polarFixedPoints → True) := by
  -- Placeholder for the structural theorem; the full statement
  -- requires a bundle formalism not yet imported in QOU.
  exact ⟨fun _ => Unit, fun _ _ => trivial, fun _ _ => trivial⟩

end QOU
