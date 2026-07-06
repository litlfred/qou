import QOU.Basic


/-!
# QOU.BraidKnot.ConfinementLocalConstancy — local constancy of confinement

The confinement level ℓ(K, q) is locally constant on Q ∖ ℬ; it changes
only at points of the phase-boundary variety ℬ.

LaTeX: `\label{prop:confinement-local-constancy}`
-/

namespace QOU.BraidKnot

universe u

/-- **Local constancy of confinement level off the phase boundary.**

    Let `R` carry a topology (the substrate parameter space `Q`), let
    `B : Set R` be the phase-boundary variety `ℬ`, and let
    `ℓ : R → ℤ` be the confinement level `ℓ(K, ·)` for a fixed knot.
    Away from `ℬ` the level is locally constant: every `q ∉ B` has an
    open neighborhood `U` on which `ℓ` is constant.

    Follows from continuity of the shadow prices (the level is
    determined by the sign pattern of the `u_λ(q)`, locally constant
    off `ℬ`).  Closing this requires the confinement-level definition
    over the base-ring topology, which is not yet formalised, so the
    statement is carried with a `sorry`. -/
-- Ref: [manuscript] climax-volume-mass/local-shadow-ordering
theorem ConfinementLocalConstancy
    (R : Type u) [TopologicalSpace R]
    (B : Set R) (ℓ : R → ℤ) (q : R) (hq : q ∉ B) :
    ∃ U : Set R, IsOpen U ∧ q ∈ U ∧ ∀ q' ∈ U, ℓ q' = ℓ q := by
  -- Ref: [manuscript] climax-volume-mass/local-shadow-ordering
  sorry

end QOU.BraidKnot
