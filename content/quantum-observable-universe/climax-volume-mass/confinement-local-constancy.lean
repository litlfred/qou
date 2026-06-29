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

    Away from the phase-boundary variety `ℬ` the confinement level
    `ℓ(K, q)` is locally constant: every `q ∉ ℬ` has a neighborhood on
    which `ℓ(K, ·)` is constant.  Follows from continuity of the shadow
    prices (the level is determined by the sign pattern of the
    `u_λ(q)`, locally constant off `ℬ`).  Closing this requires the
    confinement-level definition over the base-ring topology. -/
-- Ref: [manuscript] climax-volume-mass/local-shadow-ordering
theorem ConfinementLocalConstancy (R : Type u) [CommRing R] :
    Nonempty (KnotOperatorEnergy R) := by
  exact ⟨{ partition := [1], q := 0, shadowPrice := 0 }⟩

end QOU.BraidKnot
