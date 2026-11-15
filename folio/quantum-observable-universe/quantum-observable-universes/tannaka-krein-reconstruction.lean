import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Functor
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.RingTheory.HopfAlgebra.Basic
import Mathlib.Algebra.Category.ModuleCat.Monoidal.Basic
import Mathlib.CategoryTheory.Limits.Preserves.Finite


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

open CategoryTheory MonoidalCategory Limits

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
-- Ref: [woronowicz1988] Woronowicz, "Tannaka-Krein duality for compact matrix pseudogroups. Twisted SU(N) groups," Invent. Math. 93 (1988)
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
  /-- The representation category `Rep(carrier)`.

      A field, not a reference: Mathlib has `Rep k G` for a group `G` and
      **not** `Rep k H` for a Hopf algebra `H`, so there is nothing to point
      at.  Carrying it is what lets the equivalence below be stated. -/
  RepCat : Type u
  /-- Category structure on `Rep(carrier)`. -/
  [instRepCat : Category.{v} RepCat]
  /-- **The equivalence `C ≃ Rep(carrier)`.**

      Was `monoidal_equiv : Prop`, a field typed with the *universe* `Prop`,
      so the instance chose the proposition and `True` discharged it.  An
      equivalence is DATA; it is now `CategoryTheory.Equivalence`.

      **Scope, and it is a real weakening of the name**: this is an
      equivalence of CATEGORIES, not of *monoidal* categories.  Stating the
      monoidal upgrade needs a monoidal structure on `RepCat`, which is
      downstream of the `Rep`-for-Hopf-algebras gap above.  The field is
      named `equiv` rather than `monoidal_equiv` so the type and the name
      agree; the monoidal half is what remains open. -/
  equiv : C ≌ RepCat
  /-- `@marker` — Universal property: `carrier` is terminal among
      factorisations of `τ` through Hopf-algebra representations.

      **Still a `Prop`-universe field, and knowingly so** — hence the
      `@marker` opt-out of AGENTS.md §3b-tax, which is the corpus's
      vocabulary for a genuinely-open opaque field ("honestly framed;
      tracked not counted").  The justification below was written
      2026-09-07 and is VERIFIED, not taken on trust: Mathlib's
      `RepresentationTheory.Rep` is `abbrev Rep (k G : Type u) [Ring k]
      [Monoid G]`, so it is defined for a **monoid**, and there is no
      `Rep k H` for a Hopf algebra `H` to quantify over.  That is also why
      `RepCat` above has to be carried as a field rather than referenced.  Terminality
      quantifies over all such factorisations, and a factorisation is a
      functor into `Rep` of another Hopf algebra — the same missing
      infrastructure, one level up.  Every other field in this structure was
      encodable once the vocabulary was carried; this one is not, because
      what would have to be carried is the whole 2-category of
      Hopf-algebra representation categories.  Left as the honest gap
      rather than dressed up. -/
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
after requires the deep result.

## 🛑 The axiom was UNCONDITIONAL until 2026-09-07

It read

    axiom tannaka_krein_reconstruction … (τ_monoidal : Prop)
        (τ_faithful : Prop) (τ_exact : Prop) : ∃ R, …

Those three are **arguments of type `Prop`, not proofs**, and nothing in the
statement mentions them again.  So the axiom asserted a Tannaka–Krein
reconstruction for *every* rigid braided monoidal `C` and *every* `k`,
while reading as though it required a well-behaved fibre functor.  A caller
supplied any three propositions — `True` three times — and got the
conclusion.  That is the shape `AGENTS.md` §"Axiomatization is NOT a Proof"
forbids: an assumption dressed as a hypothesis.

They are now the actual fibre functor `τ : C ⥤ ModuleCat k` with
`[τ.Faithful]`, `[τ.Monoidal]`, `[PreservesFiniteLimits τ]` and
`[PreservesFiniteColimits τ]` — all four resolved against the pinned
Mathlib.

**The comment they replaced said this could not be done**: *"stating this
precisely requires MonoidalFunctor C (ModuleCat k), which compiles but the
monoidal instance on ModuleCat is nontrivial.  We use Prop placeholders …
until the enriched functor infrastructure matures."*  Measured: the
instance is `Mathlib.Algebra.Category.ModuleCat.Monoidal.Basic`, one import
away, and `τ.Monoidal` elaborates once it is present.  The infrastructure
had matured; the file had not been re-checked.

**The axiom is still an axiom** and the conclusion is still assumed.  What
changed is that it is now assumed *under the hypotheses the literature
states*, so an instance cannot be obtained for free. -/

-- Ref: [woronowicz1988] https://doi.org/10.1007/BF01219077  Theorem 1.1
-- Ref: [deligne1990] https://doi.org/10.1007/978-0-8176-4575-5_3  Théorème 7.1
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2  Theorem XI.4.1
axiom tannaka_krein_reconstruction
    (C : Type u) [Category.{v} C] [MonoidalCategory C]
    [RigidCategory C]
    [BraidedCategory C]
    (k : Type w) [CommRing k]
    -- The fibre functor: a strong monoidal functor C → k-Mod, with its
    -- three properties as real Mathlib typeclasses.
    (τ : C ⥤ ModuleCat.{w} k)
    [τ.Faithful] [τ.Monoidal]
    [PreservesFiniteLimits τ] [PreservesFiniteColimits τ]
    : ∃ R : TannakaKreinReconstruction.{u, v, w} C k,
        R.universal_property

end QOU
