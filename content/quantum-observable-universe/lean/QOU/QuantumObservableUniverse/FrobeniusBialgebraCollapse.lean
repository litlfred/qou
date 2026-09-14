import QOU.QuantumObservableUniverse.CategoricalFoundations

/-!
# A Frobenius–Hopf substrate that is also a bialgebra is trivial

`QOU.FrobeniusHopfData` carries the Frobenius relation `μ ≫ Δ = (Δ ▷ A) ≫ α ≫
(A ◁ μ)`, so its `Δ` is the **Frobenius** comultiplication.  Since 2026-09-14 it
also carries the Hopf antipode axioms (bean `qou-c64q`).  It does **not** carry
the bimonoid (bialgebra) compatibility, and the block's `authorNotes` recorded
that as an open question for the owner.

**This file answers it, and the answer is that the axiom must not be added.**

One of the four bimonoid axioms *on its own* — `Δ ∘ η = η ⊗ η`, Mathlib's
`CategoryTheory.BimonObj.one_comul` — collapses the substrate:

* `comul_eq_of_one_comul` : `Δ = (λ_A)⁻¹ ≫ (η ▷ A)`, i.e. `Δ(x) = 1 ⊗ x`;
* `counit_comp_unit` : `ε ≫ η = 𝟙_A`, so `𝟙_A` factors through the tensor unit;
* `isoUnit` : with `η ≫ ε = 𝟙` (the bimonoid axiom `one_counit`) this is an
  isomorphism `A ≅ 𝟙_C`.

So a Frobenius–Hopf substrate satisfying two of the four bimonoid axioms is the
tensor unit. The framework's `A` is meant to be the quantum vacuum, not `𝟙`, so
the bimonoid compatibility is **excluded**, not merely absent.

## Why this is not a defect in the definition

It is the expected state of affairs, and it is why the name "Frobenius–Hopf"
needs reading with care. A finite-dimensional Hopf algebra *is* Frobenius — but
its Frobenius comultiplication is **not** its Hopf comultiplication. Forcing the
two to coincide is what collapses. The substrate takes `Δ` to be the Frobenius
one (that is what `frobenius_relation` says), so it is a Frobenius monoid with
an antipode, not a Hopf monoid in Mathlib's sense, and results about
`CategoryTheory.HopfObj` — `antipode_antipode` among them — do not transfer to
it. That was already recorded in the block's `authorNotes`; what is new here is
that it cannot be fixed by adding the axiom.

## The mechanism, in one line

The Frobenius relation makes `Δ` a map of `A`-bimodules, so `Δ` is determined by
`Δ(1)`; the bimonoid axiom sets `Δ(1) = 1 ⊗ 1`, which is degenerate; the counit
law then forces every `x` to equal `ε(x)·1`.

## Scope

This is a **structural exclusion** in the sense of AGENTS.md §"Before declaring
refuted": the invariant cited is the proved implication below, not a numerical
probe. It excludes the bimonoid compatibility *for a `Δ` satisfying the
Frobenius relation*. It says nothing against a Hopf structure on `A` carried by
a **different** comultiplication, which is a separate object the corpus does not
currently have.

## References

- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
- [kassel1995] C. Kassel, *Quantum Groups*, Springer 1995, Ch. II–III.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory
open CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.FrobeniusHopfData

universe u v

variable {C : Type u} [Category.{v} C] [MonoidalCategory C]
variable (F : QOU.FrobeniusHopfData C)

/-! ### Two spellings of the left unit law -/

/-- `𝟙 ≅ 𝟙 ⊗ A --η ▷ A--> A ⊗ A --μ--> A` is the identity (left-associated). -/
theorem unitor_unit_mul :
    ((λ_ F.obj).inv ≫ (F.unit ▷ F.obj)) ≫ F.mul = 𝟙 F.obj := by
  rw [Category.assoc, F.one_mul, Iso.inv_hom_id]

/-- The same, right-associated, which is the shape `simp` normalises to. -/
theorem unitor_unit_mul' :
    (λ_ F.obj).inv ≫ (F.unit ▷ F.obj) ≫ F.mul = 𝟙 F.obj := by
  rw [← Category.assoc, unitor_unit_mul]

/-- Expanding `Δ = id ≫ Δ` through the left unit and then substituting the
    Frobenius relation.  No hypothesis beyond the structure's own axioms. -/
theorem comul_eq_frobenius :
    F.comul = ((λ_ F.obj).inv ≫ (F.unit ▷ F.obj)) ≫
      ((F.comul ▷ F.obj) ≫ (α_ F.obj F.obj F.obj).hom ≫ (F.obj ◁ F.mul)) := by
  conv_lhs =>
    rw [show F.comul
        = ((λ_ F.obj).inv ≫ (F.unit ▷ F.obj)) ≫ (F.mul ≫ F.comul) by
      rw [← Category.assoc, unitor_unit_mul, Category.id_comp]]
  rw [F.frobenius_relation]

/-! ### The collapse -/

/-- **The comultiplication degenerates.**  Under the bimonoid unit axiom
    `Δ ∘ η = η ⊗ η`, the Frobenius relation forces `Δ = (λ_A)⁻¹ ≫ (η ▷ A)` —
    in elements, `Δ(x) = 1 ⊗ x`.

    The hypothesis is Mathlib's `CategoryTheory.BimonObj.one_comul` written out:
    the unit of the tensor-product monoid on `A ⊗ A` is `(λ_𝟙)⁻¹ ≫ (η ⊗ η)`,
    and unlike the `mul_comul` axiom it involves no braiding, so it is statable
    over a bare monoidal category. -/
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
--      (Δ is a bimodule map, hence determined by Δ(1))
theorem comul_eq_of_one_comul
    (h : F.unit ≫ F.comul
      = (λ_ (𝟙_ C)).inv ≫ (MonoidalCategory.tensorHom F.unit F.unit)) :
    F.comul = (λ_ F.obj).inv ≫ (F.unit ▷ F.obj) := by
  conv_lhs => rw [comul_eq_frobenius F]
  simp only [Category.assoc, ← comp_whiskerRight_assoc, h]
  simp [tensorHom_def, ← MonoidalCategory.whiskerLeft_comp, unitor_unit_mul']

/-- **The object collapses.**  `ε ≫ η = 𝟙_A`: the identity on `A` factors
    through the tensor unit, so `A` is a retract of `𝟙_C`.

    Together with `comul_eq_of_one_comul` this is the whole content: the
    counit law `Δ ≫ (A ◁ ε) = (ρ_A)⁻¹` cannot hold for the degenerate `Δ`
    unless every `x` equals `ε(x) · 1`. -/
theorem counit_comp_unit
    (h : F.unit ≫ F.comul
      = (λ_ (𝟙_ C)).inv ≫ (MonoidalCategory.tensorHom F.unit F.unit)) :
    F.counit ≫ F.unit = 𝟙 F.obj := by
  have key := F.comul_counit
  rw [comul_eq_of_one_comul F h] at key
  simp only [Category.assoc, ← whisker_exchange] at key
  rw [← Category.assoc, ← leftUnitor_inv_naturality, Category.assoc,
      unitors_inv_equal, ← rightUnitor_inv_naturality, ← Category.assoc] at key
  simpa using key =≫ (ρ_ F.obj).hom

/-- **`A ≅ 𝟙_C`.**  Adding the second unit-side bimonoid axiom
    `η ≫ ε = 𝟙` (Mathlib's `BimonObj.one_counit`) upgrades the retract to an
    isomorphism: the substrate object *is* the tensor unit. -/
noncomputable def isoUnit
    (h : F.unit ≫ F.comul
      = (λ_ (𝟙_ C)).inv ≫ (MonoidalCategory.tensorHom F.unit F.unit))
    (h' : F.unit ≫ F.counit = 𝟙 (𝟙_ C)) :
    F.obj ≅ 𝟙_ C where
  hom := F.counit
  inv := F.unit
  hom_inv_id := F.counit_comp_unit h
  inv_hom_id := h'

/-- **Contrapositive, which is the usable form.**  If the substrate object is
    *not* a retract of the tensor unit — i.e. `ε ≫ η ≠ 𝟙_A`, which is what
    "the quantum vacuum is not the trivial object" means — then the bimonoid
    unit axiom **fails**.

    So the bialgebra compatibility is not an open option for this definition:
    it is excluded by the Frobenius relation together with non-triviality. -/
theorem not_one_comul_of_nontrivial (hnt : F.counit ≫ F.unit ≠ 𝟙 F.obj) :
    F.unit ≫ F.comul
      ≠ (λ_ (𝟙_ C)).inv ≫ (MonoidalCategory.tensorHom F.unit F.unit) :=
  fun h => hnt (F.counit_comp_unit h)

end QOU.FrobeniusHopfData
