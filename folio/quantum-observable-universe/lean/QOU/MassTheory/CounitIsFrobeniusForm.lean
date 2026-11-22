import QOU.QuantumObservableUniverse.CategoricalFoundations

/-!
# With coevaluation `η ≫ Δ`, the counit is the Frobenius form

`counit_eq_frobeniusForm_of_coev`: in every `FrobeniusHopfData`, if the coevaluation is
`η ≫ Δ` then `ε = λ`. The proof uses the left snake identity, the right counit law and the right
unit law, plus monoidal coherence. The braiding is never used, so this covers the braided case,
and it does not need the mirror Frobenius relation that `counit_snake_left_of_mirror` assumed.

So `λ = ε` is not a normalisation choice. It is forced once the coevaluation is `η ≫ Δ`, and it
does not fix the scale: `(λ, coev) ↦ (sλ, s⁻¹coev)` comes with `(Δ, ε) ↦ (s⁻¹Δ, sε)`, which keeps
`coev = η ≫ Δ` and `ε = λ`. Exact check on `H₂(q)`: `mn_counit_pairing_probe.py`, part A.

Element form: write `Δ(1) = Σ eᵢ ⊗ fᵢ`. The left snake gives `Σ λ(x eᵢ) fᵢ = x`, and the right
counit law gives `Σ eᵢ ε(fᵢ) = 1`, so `ε(x) = Σ λ(x eᵢ) ε(fᵢ) = λ(x)`.
-/

namespace QOU.MassTheory.CounitIsFrobeniusForm

open CategoryTheory MonoidalCategory

universe u v

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]

/-- If the coevaluation is `η ≫ Δ`, the counit equals the Frobenius form. -/
theorem counit_eq_frobeniusForm_of_coev (F : QOU.FrobeniusHopfData C)
    (hcoev : F.coevaluation = F.unit ≫ F.comul) : F.counit = F.frobeniusForm := by
  have hs := F.pairing_snake_left
  rw [hcoev] at hs
  have key : F.counit =
      ((ρ_ F.obj).inv ≫ (F.obj ◁ (F.unit ≫ F.comul)) ≫ (α_ F.obj F.obj F.obj).inv ≫
      ((F.mul ≫ F.frobeniusForm) ▷ F.obj) ≫ (λ_ F.obj).hom) ≫ F.counit := by
    rw [hs, Category.id_comp]
  rw [key]
  have e1 : (λ_ F.obj).hom ≫ F.counit = ((𝟙_ C) ◁ F.counit) ≫ (λ_ (𝟙_ C)).hom :=
    (leftUnitor_naturality F.counit).symm
  have e2 : ((F.mul ≫ F.frobeniusForm) ▷ F.obj) ≫ ((𝟙_ C) ◁ F.counit) =
      ((F.obj ⊗ F.obj) ◁ F.counit) ≫ ((F.mul ≫ F.frobeniusForm) ▷ (𝟙_ C)) :=
    (whisker_exchange _ _).symm
  have e3 : (F.obj ◁ (F.unit ≫ F.comul)) ≫ (F.obj ◁ (F.obj ◁ F.counit)) =
      (F.obj ◁ F.unit) ≫ (F.obj ◁ (ρ_ F.obj).inv) := by
    rw [← whiskerLeft_comp, ← whiskerLeft_comp, Category.assoc, F.comul_counit]
  simp only [Category.assoc]
  rw [e1, reassoc_of% e2, ← associator_inv_naturality_right_assoc, reassoc_of% e3]
  have e4 : (F.obj ◁ (ρ_ F.obj).inv) ≫ (α_ F.obj F.obj (𝟙_ C)).inv ≫
      ((F.mul ≫ F.frobeniusForm) ▷ (𝟙_ C)) ≫ (λ_ (𝟙_ C)).hom = F.mul ≫ F.frobeniusForm := by
    monoidal
  rw [e4, ← Category.assoc (F.obj ◁ F.unit), F.mul_one, Iso.inv_hom_id_assoc]

end QOU.MassTheory.CounitIsFrobeniusForm
