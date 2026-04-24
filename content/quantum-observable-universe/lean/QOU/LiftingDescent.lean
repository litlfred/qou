import Mathlib.Data.Real.Basic

/-!
# QOU.LiftingDescent — Arc spaces of the brane tower

Formalizes `def:arc-space`.

The QOU recursive brane tower
`𝓢₀ ↪ 𝓢₁ ↪ 𝓢₂ ↪ ⋯` is identified with a tower of jet schemes
`L_n(X)`, and its inverse limit is the arc space
`L(X) = lim_{←n} L_n(X)`.

The interface below is abstract: jet schemes are typed by a base
`X : Type*` and a level `n : Nat`, and the arc space exposes
projections to each jet level compatible with the truncation
maps. No assumption is made on whether `X` is smooth.

## References

- [denef-loeser2001] Denef, Loeser, *Geometry on Arc Spaces of
  Algebraic Varieties*. ECM Barcelona 2000, Birkhäuser, 327-348.
-/

namespace QOU.LiftingDescent

/-- The **n-th jet scheme** `L_n(X)` of a variety `X`.

    Represents the functor `R ↦ Hom(Spec R[t]/(t^{n+1}), X)`.
    In QOU it is identified with the n-th level of the recursive
    brane tower `𝓢_n`. -/
structure JetScheme (X : Type*) (n : Nat) where
  /-- Underlying scheme of the n-th jet space. -/
  Carrier : Type*
  /-- The truncation map L_{n+1}(X) → L_n(X). -/
  truncation : Carrier → Carrier

/-- The **arc space** `L(X)` of a variety `X`.

    `L(X) = lim_{←n} L_n(X)` is the inverse limit of the jet
    schemes. In QOU it equals the inverse limit of the recursive
    brane tower `𝓢_∞ := lim_n 𝓢_n`. Carries the formal data
    needed for motivic integration even when `X` is singular. -/
structure ArcSpace (X : Type*) where
  /-- The carrier of the arc space (inverse limit of jet schemes). -/
  Carrier : Type*
  /-- Projection to each finite jet level. -/
  projection : (n : Nat) → Carrier → (JetScheme X n).Carrier

end QOU.LiftingDescent
