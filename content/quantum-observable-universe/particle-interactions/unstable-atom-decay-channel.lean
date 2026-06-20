import QOU.Basic


/-!
# QOU.BraidKnot.UnstableAtom.decay_channel — uniquely-determined decay channel

The violated constraint γ*(K, q) is well-defined off the boundary
variety (where two shadow prices agree).

LaTeX: `\label{prop:unstable-atom-decay-channel}`
-/

namespace QOU.BraidKnot

universe u

/-- **Decay channel of an unstable atom is uniquely determined.**

    Off the boundary variety
    `B := { q : ∃ λ₁ ≠ λ₂, |y_{λ₁}(q)| = |y_{λ₂}(q)| }`,
    the violated constraint γ* is unique. -/
-- Ref: [manuscript] braids-and-knots/local-shadow-ordering
def UnstableAtom.decay_channel_unique
    {R : Type u} [CommRing R]
    (U₁ U₂ : UnstableAtom R)
    (h_knot : U₁.knot = U₂.knot)
    (h_q    : U₁.q    = U₂.q) :
    -- Stub: the decay channel γ*(K, q) ∈ partition is determined by
    -- the LP relaxation; uniqueness off the boundary variety.
    True := trivial

end QOU.BraidKnot
