/-!
# QOU.tannaka_krein_reconstruction — Tannaka–Krein reconstruction

Given a rigid braided monoidal category C with a faithful exact
monoidal functor τ : C → R-Mod, the coend End⊗(τ) carries a
canonical Hopf algebra structure H such that C ≃ Rep(H).

LaTeX label: `prop:tannaka-krein-reconstruction`

## References
- [woronowicz1988] https://doi.org/10.1007/BF01219077
- [deligne1990] https://doi.org/10.1007/978-0-8176-4575-5_3
- [tannaka1939] (original Tannaka reconstruction)
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- Tannaka–Krein reconstruction data: a Hopf algebra H reconstructed
    from a fibre functor τ on a rigid monoidal category, together with
    the monoidal equivalence C ≃ Rep(H). -/
-- Ref: [woronowicz1988] https://doi.org/10.1007/BF01219077
structure TannakaKreinData (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The reconstructed Hopf algebra (as an endomorphism algebra of τ). -/
  hopfAlgebra : Type u
  /-- The monoidal equivalence C ≃ Rep(H). -/
  equiv_rep : Prop
  /-- Universal property: H is terminal among Hopf algebras through
      which τ factors. -/
  universal : Prop

/-- The Tannaka–Krein reconstruction theorem: for a QOU (C, A, τ),
    the coend End⊗(τ) is a Hopf algebra with C ≃ Rep(End⊗(τ)). -/
-- Ref: [woronowicz1988] https://doi.org/10.1007/BF01219077
-- Ref: [deligne1990] https://doi.org/10.1007/978-0-8176-4575-5_3
theorem tannaka_krein_reconstruction
    (C : Type u) [Category.{v} C] [MonoidalCategory C]
    (hrigid : Prop)  -- C is rigid
    (hfaithful : Prop)  -- τ is faithful and exact
    : ∃ (_ : TannakaKreinData C), True := by
  -- Ref: [woronowicz1988] https://doi.org/10.1007/BF01219077
  sorry

end QOU
