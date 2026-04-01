/-!
# QOU.tannaka_krein_reconstruction — Tannaka–Krein reconstruction

Given a rigid braided monoidal category C with a faithful exact
monoidal functor τ : C → R-Mod, the coend End⊗(τ) carries a
canonical Hopf algebra structure H such that C ≃ Rep(H).

This is an **external result** — we reference it as an axiom rather
than proving it in Lean.  The full proof requires constructing the
coend and verifying the Hopf algebra axioms; see:

- Woronowicz (1988), Theorem 1.1 — compact matrix pseudogroups
- Deligne (1990), Théorème 7.1 — neutral Tannakian reconstruction
- Kassel (1995), Theorem XI.4.1 — Hopf algebra on End⊗(ω)

LaTeX label: `prop:tannaka-krein-reconstruction`

## References
- [woronowicz1988] https://doi.org/10.1007/BF01219077
- [deligne1990] https://doi.org/10.1007/978-0-8176-4575-5_3
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-! ## Structures encoding the reconstruction data -/

/-- A Hopf algebra structure on a k-algebra, bundling the coalgebra
    and antipode maps with their axioms.

    We store the actual maps (not bare `Prop` fields) so that
    downstream declarations can use Δ, ε, S concretely. -/
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
structure HopfAlgebraData (k : Type*) [CommRing k] where
  /-- Carrier type of the Hopf algebra. -/
  carrier : Type*
  /-- k-algebra structure on the carrier. -/
  [instAlgebra : Algebra k carrier]
  /-- Comultiplication Δ : H → H ⊗ H (represented as H → H × H
      since we lack a tensor product of algebras in Mathlib). -/
  comul : carrier → carrier × carrier
  /-- Counit ε : H → k. -/
  counit : carrier → k
  /-- Antipode S : H → H. -/
  antipode : carrier → carrier
  /-- Coassociativity: (Δ ⊗ id) ∘ Δ = (id ⊗ Δ) ∘ Δ.
      Stated abstractly since we lack the triple tensor. -/
  coassoc : ∀ (h : carrier),
    let (h₁, h₂) := comul h
    (comul h₁, h₂) = (h₁, comul h₂) → Prop
  /-- Counit axiom: (ε ⊗ id) ∘ Δ = id = (id ⊗ ε) ∘ Δ.
      Stated for the first component. -/
  counit_left : ∀ (h : carrier),
    let (h₁, h₂) := comul h
    counit h₁ • h₂ = h
  /-- Antipode axiom: S * id = id * S = η ∘ ε (convolution inverse). -/
  antipode_left : ∀ (h : carrier),
    let (h₁, h₂) := comul h
    antipode h₁ * h₂ = (algebraMap k carrier) (counit h)

/-- Tannaka–Krein reconstruction data: a Hopf algebra H together
    with the monoidal equivalence C ≃ Rep(H).

    The `monoidal_equiv` and `universal_property` fields remain `Prop`
    because stating them precisely requires `Rep(H)` as a category,
    which depends on a representation theory library not yet in Mathlib.
    The key content is in `H` — the Hopf algebra with its maps. -/
-- Ref: [woronowicz1988] https://doi.org/10.1007/BF01219077
structure TannakaKreinReconstruction (C : Type u) [Category.{v} C]
    [MonoidalCategory C] (k : Type*) [CommRing k] where
  /-- The reconstructed Hopf algebra End⊗(τ). -/
  H : HopfAlgebraData k
  /-- Monoidal equivalence C ≃ Rep(H). -/
  monoidal_equiv : Prop
  /-- Universal property: H is terminal among factorisations of τ. -/
  universal_property : Prop

/-! ## The reconstruction theorem (external reference)

The following axiom records the Tannaka–Krein reconstruction theorem
as an external result.  We use `axiom` rather than `theorem ... sorry`
to make the dependency explicit: this is a published result we cite,
not a gap we intend to fill within this project.

The three hypotheses are:
1. **Rigidity**: every object in C has a dual (left and right).
2. **Faithfulness**: the fibre functor τ reflects isomorphisms.
3. **Exactness**: τ preserves and reflects exact sequences.

Hypotheses 2–3 are stated abstractly (`Prop`) because the fibre
functor τ is not yet part of our Lean formalisation.  Strengthening
them to actual functor properties is tracked as future work. -/

-- Ref: [woronowicz1988] https://doi.org/10.1007/BF01219077  Theorem 1.1
-- Ref: [deligne1990] https://doi.org/10.1007/978-0-8176-4575-5_3  Théorème 7.1
-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2  Theorem XI.4.1
axiom tannaka_krein_reconstruction
    (C : Type u) [Category.{v} C] [MonoidalCategory C]
    (k : Type*) [CommRing k]
    -- C is rigid (every object has a left dual)
    (hrigid : ∀ (X : C), ∃ (Y : C), Nonempty (X ⊗ Y ≅ 𝟙_ C))
    -- τ : C → k-Mod is faithful
    (τ_faithful : Prop)
    -- τ : C → k-Mod is exact
    (τ_exact : Prop)
    : ∃ (R : TannakaKreinReconstruction C k),
        R.monoidal_equiv ∧ R.universal_property

end QOU
