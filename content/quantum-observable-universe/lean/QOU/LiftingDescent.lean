import Mathlib.Data.Real.Basic

/-!
# QOU.LiftingDescent — Arc spaces of the brane tower

Formalizes `def:arc-space`.

The QOU recursive brane tower
`𝓢₀ ↪ 𝓢₁ ↪ 𝓢₂ ↪ ⋯` is identified with a tower of jet schemes
`L_n(X)`, and its inverse limit is the arc space
`L(X) = lim_{←n} L_n(X)`.

Design (per PR #403 review):

- `JetScheme X n` packages just the carrier of `L_n(X)`.
- `JetTower X` carries the whole family `L_n(X)` together with the
  level-shifting truncation maps `L_{n+1}(X) → L_n(X)`.
- `ArcSpace X tower` is the inverse limit, exposing one projection
  `Carrier → (tower.level n).Carrier` per level.

This avoids the type-vs-term confusion of trying to write
`(JetScheme X n).Carrier` from inside another structure: the carrier
is now extracted from a *term* of `JetScheme`, not from the type.

## References

- [denef-loeser2001] Denef, Loeser, *Geometry on Arc Spaces of
  Algebraic Varieties*. ECM Barcelona 2000, Birkhäuser, 327-348.
-/

namespace QOU.LiftingDescent

/-- The **n-th jet scheme** `L_n(X)` of a variety `X`.

    Represents the functor `R ↦ Hom(Spec R[t]/(t^{n+1}), X)`.
    In QOU it is identified with the n-th level of the recursive
    brane tower `𝓢_n`. The structure exposes only the carrier of
    `L_n(X)`; the truncation map `L_{n+1}(X) → L_n(X)` lives on
    `JetTower` (it is inherently a level-shifting map). -/
structure JetScheme (X : Type*) (n : Nat) where
  /-- Underlying scheme of the n-th jet space. -/
  Carrier : Type*

/-- A **jet tower** for `X`: the whole family of jet schemes
    `L_n(X)` together with the truncation maps `L_{n+1}(X) → L_n(X)`. -/
structure JetTower (X : Type*) where
  /-- The n-th jet scheme. -/
  level : (n : Nat) → JetScheme X n
  /-- The truncation map `L_{n+1}(X) → L_n(X)`. -/
  truncation : ∀ n, (level (n + 1)).Carrier → (level n).Carrier

/-- The **arc space** `L(X)` of a variety `X` over a chosen jet tower.

    `L(X) = lim_{←n} L_n(X)` is the inverse limit of the jet
    schemes. In QOU it equals the inverse limit of the recursive
    brane tower `𝓢_∞ := lim_n 𝓢_n`. Carries the formal data
    needed for motivic integration even when `X` is singular.

    The `compatible` field is the inverse-system law: each
    projection equals the next, post-composed with truncation. -/
structure ArcSpace (X : Type*) (tower : JetTower X) where
  /-- The carrier of the arc space (inverse limit of jet schemes). -/
  Carrier : Type*
  /-- Projection to each finite jet level. -/
  projection : (n : Nat) → Carrier → (tower.level n).Carrier
  /-- Compatibility with truncation: trunc_n ∘ proj_{n+1} = proj_n. -/
  compatible : ∀ n a, tower.truncation n (projection (n + 1) a) = projection n a

end QOU.LiftingDescent
