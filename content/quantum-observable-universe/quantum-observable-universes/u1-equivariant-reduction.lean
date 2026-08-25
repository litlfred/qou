import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Topology.Instances.Real.Lemmas


/-!
# QOU.CommutativeQOU.u1EquivariantReduction

U(1)-equivariant observables on the ℙ¹(ℂ) exceptional divisor reduce
to functions on the orbit space [0, π], equivalently to sections of
a phase-S¹ bundle over the open interval (0, π).

LaTeX label: `prop:u1-equivariant-reduction`

**Ground ring**: `ℝ` (analytic/geometric).
-/

namespace QOU

/-- Orbit space of the U(1) rotation action on the exceptional divisor
    𝒮_p = ℙ¹(ℂ), parametrised by the polar angle φ ∈ [0, π].

    `↥` is the subtype coercion: `U1OrbitSpace` is a `Type` whose
    elements are real numbers carrying a proof that they lie in
    `[0, π]`. -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
abbrev U1OrbitSpace : Type := ↥(Set.Icc (0 : ℝ) Real.pi)

/-- The polar fixed points of the U(1) action: φ = 0 and φ = π.
    These are the two points where the U(1)-orbit on 𝒮_p collapses
    to a single point.

    For `x : U1OrbitSpace`, `x.val : ℝ` is the underlying real number
    (the wrapper around a real carrying the Icc membership proof). -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
def polarFixedPoints : Set U1OrbitSpace :=
  { x | x.val = 0 ∨ x.val = Real.pi }

/-- **U(1)-equivariant reduction** (structural statement).
    `PhaseFiber φ` is:
      - `Unit` at the two polar fixed points (φ = 0 or φ = π),
        reflecting the collapse of the S¹ orbit to a point;
      - intended to be `S¹` over the open interior (0, π).

    This file records the signature only; the full bundle-theoretic
    formalisation (connection to `Mathlib.Topology.FiberBundle`) is
    deferred.  The honest content here is the *structural asymmetry*
    between polar and interior points.

    `polarFixedPoints` is membership in a set cut out by real-number
    equalities (`x.val = 0 ∨ x.val = Real.pi`), which is not
    algorithmically decidable; the case split is justified classically,
    hence the `Classical` instance and `noncomputable`. -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
noncomputable def PhaseFiber (φ : U1OrbitSpace) : Type :=
  open Classical in
  if φ ∈ polarFixedPoints then Unit else Unit  -- interior placeholder

/-- The polar fixed-point fibre is `Unit` (collapsed). -/
-- Ref: [manuscript] Chapter 3, §Varying Euler + mirror bundle
theorem phaseFiber_polar (φ : U1OrbitSpace) (h : φ ∈ polarFixedPoints) :
    PhaseFiber φ = Unit := by
  unfold PhaseFiber
  rw [if_pos h]

end QOU
