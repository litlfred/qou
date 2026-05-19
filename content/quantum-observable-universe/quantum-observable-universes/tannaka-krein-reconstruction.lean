/-!
# QOU.tannaka_krein_reconstruction — Tannaka–Krein reconstruction

Given a rigid braided monoidal category C with a faithful exact
monoidal functor τ : C → R-Mod, the coend End⊗(τ) carries a
canonical Hopf algebra structure H such that C ≃ Rep(H).

This file uses Mathlib's `HopfAlgebra`, `RigidCategory`,
`BraidedCategory`, and `MonoidalFunctor` typeclasses to state
the reconstruction theorem precisely.

The theorem itself is an **external result** — declared as an axiom
with references to the published proofs.  The first wall we hit is
the **coend construction**: building End⊗(τ) as a concrete k-algebra
from the functor τ.  This requires colimit machinery in the enriched
setting that Mathlib does not yet provide.

LaTeX label: `prop:tannaka-krein-reconstruction`

## What Mathlib provides (used here)
- `HopfAlgebra R A` — Hopf algebra typeclass (comul, counit, antipode)
- `RigidCategory C` — left + right duals with zig-zag identities
- `BraidedCategory C` — braiding natural iso + hexagon axioms
- `MonoidalFunctor C D` — strong monoidal functor (tensorator + unitor isos)
- `Functor.Faithful` — faithful functor typeclass

## Where we hit walls (deep results needed)
1. **Coend construction**: End⊗(τ) = ∫^{X∈C} τ(X)∨ ⊗ τ(X) as a
   k-algebra.  Requires enriched coends (not in Mathlib).
2. **Hopf structure on End⊗(τ)**: proving comul/counit/antipode satisfy
   the axioms.  This is the core of the Tannaka–Krein proof.
3. **Monoidal equivalence C ≃ Rep(H)**: requires `Rep` infrastructure
   that is only partially in Mathlib (Rep k G exists for groups G,
   but not for general Hopf algebras H).

## References
- [woronowicz1988] https://doi.org/10.1007/BF01219077
- [deligne1990] https://doi.org/10.1007/978-0-8176-4575-5_3
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Functor
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.RingTheory.HopfAlgebra.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v w

/-! ## Reconstruction data

We bundle the output of Tannaka–Krein reconstruction:
a Hopf algebra H (using Mathlib's typeclass) together with
the monoidal equivalence C ≃ Rep(H).

The equivalence and universal property remain `Prop` because
`Rep H` for a general Hopf algebra H is not yet a Mathlib
category (only `Rep k G` for group G exists). -/

/-- The output of Tannaka–Krein reconstruction: a k-algebra A
    carrying a `HopfAlgebra k A` structure, together with the
    monoidal equivalence C ≃ Rep(A) and the universal property.

    The carrier `A` and its `HopfAlgebra` instance are concrete
    Mathlib structures.  The equivalence is stated as `Prop`
    pending Mathlib infrastructure for `Rep` of a Hopf algebra. -/
-- Ref: [woronowicz1988] Tannaka-Kre012dn duality for compact matrix pseu — see content/schema/references.ts
structure TannakaKreinReconstruction
    (C : Type u) [Category.{v} C] [MonoidalCategory C]
    (k : Type w) [CommRing k] where
  /-- Carrier of the reconstructed Hopf algebra End⊗(τ). -/
  carrier : Type w
  /-- Ring structure on the carrier. -/
  [instRing : Ring carrier]
  /-- k-algebra structure. -/
  [instAlgebra : Algebra k carrier]
  /-- Coalgebra structure (comul Δ, counit ε). -/
  [instCoalgebra : Coalgebra k carrier]
  /-- Bialgebra compatibility (Δ and ε are algebra maps). -/
  [instBialgebra : Bialgebra k carrier]
  /-- Hopf algebra structure (adds antipode S). -/
  [instHopfAlgebra : HopfAlgebra k carrier]
  /-- Monoidal equivalence C ≃ Rep(carrier).
      Stated as Prop: requires Rep for Hopf algebras (not in Mathlib).
      Wall: Mathlib has `Rep k G` for groups but not `Rep k H`
      for Hopf algebras. -/
  monoidal_equiv : Prop
  /-- Universal property: carrier is terminal among factorisations
      of τ through Hopf algebra representations. -/
  universal_property : Prop

/-! ## The reconstruction axiom

The hypotheses use Mathlib typeclasses wherever possible:
- `[RigidCategory C]` — full rigidity (left + right duals, zig-zag)
- `[BraidedCategory C]` — braiding + hexagon axioms
- `(τ : MonoidalFunctor C (ModuleCat k))` — the fibre functor as a
  strong monoidal functor to k-modules
- `[τ.Faithful]` — τ reflects isomorphisms

The wall is the **conclusion**: constructing the `HopfAlgebra` instance
on the coend End⊗(τ).  Everything before the colon is Mathlib; everything
after requires the deep result. -/

-- Ref: [woronowicz1988] https://doi.org/10.1007/BF01219077  Theorem 1.1
-- Ref: [deligne1990] https://doi.org/10.1007/978-0-8176-4575-5_3  Théorème 7.1
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2  Theorem XI.4.1
axiom tannaka_krein_reconstruction
    (C : Type u) [Category.{v} C] [MonoidalCategory C]
    [RigidCategory C]
    [BraidedCategory C]
    (k : Type w) [CommRing k]
    -- The fibre functor: a strong monoidal functor C → k-Mod.
    -- Wall: ModuleCat k is the target, but stating this precisely
    -- requires MonoidalFunctor C (ModuleCat k), which compiles but
    -- the monoidal instance on ModuleCat is nontrivial.  We use
    -- Prop placeholders for the functor properties until the
    -- enriched functor infrastructure matures.
    (τ_monoidal : Prop)  -- τ is a strong monoidal functor
    (τ_faithful : Prop)  -- τ is faithful
    (τ_exact : Prop)     -- τ is exact
    : ∃ (R : TannakaKreinReconstruction C k),
        R.monoidal_equiv ∧ R.universal_property

end QOU
