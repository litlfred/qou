-- Ref: [denef-loeser2001] Denef, Loeser, Geometry on Arc Spaces of Algebraic Varieties.
--   European Congress of Mathematics, Vol. I (Barcelona, 2000), 327-348.
-- Arc space L(X) of a variety X, identified with the recursive brane tower.
--
-- Canonical declaration lives in: lean/QOU/LiftingDescent.lean
-- This sibling is a documentation-mirror of the QOU library declaration.
import Mathlib.Logic.Basic

namespace QOU.LiftingDescent

/-- The **n-th jet scheme** `L_n(X)`. Carrier-only: truncation
    is a level-shifting map and lives on `JetTower`. -/
structure JetScheme (X : Type*) (n : Nat) where
  /-- Underlying scheme of the n-th jet space. -/
  Carrier : Type*

/-- A **jet tower** for `X`: the family `L_n(X)` together with
    the truncation maps `L_{n+1}(X) → L_n(X)`. -/
structure JetTower (X : Type*) where
  /-- The n-th jet scheme. -/
  level : (n : Nat) → JetScheme X n
  /-- The truncation map `L_{n+1}(X) → L_n(X)`. -/
  truncation : ∀ n, (level (n + 1)).Carrier → (level n).Carrier

/-- The **arc space** `L(X) = lim_{←n} L_n(X)`. Carries the
    formal data needed for motivic integration even when `X` is
    singular. -/
structure ArcSpace (X : Type*) (tower : JetTower X) where
  /-- The carrier of the arc space (inverse limit of jet schemes). -/
  Carrier : Type*
  /-- Projection to each finite jet level. -/
  projection : (n : Nat) → Carrier → (tower.level n).Carrier
  /-- Compatibility with truncation: trunc_n ∘ proj_{n+1} = proj_n. -/
  compatible : ∀ n a, tower.truncation n (projection (n + 1) a) = projection n a

end QOU.LiftingDescent
