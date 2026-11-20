import QOU.QuantumObservableUniverse.FrobeniusHopfModelDichotomy

/-!
# Nilpotent scalars, the retract theorem, and a split-ring model of `FrobeniusHopfData`

Bean `qou-blf1` (GS-3, epic `qou-uhx0`). Continues
`QOU.QuantumObservableUniverse.FrobeniusHopfModelDichotomy` (bean `qou-aawz`).

Throughout, `σ = η ≫ ε : 𝟙_C ⟶ 𝟙_C` is the scalar `ε(1)` (`unitCounit`), and
`scalarAct X τ = λ⁻¹ ≫ (τ ▷ X) ≫ λ` is the action of a scalar `τ` on an object.
Every result that uses the antipode takes the left convolution condition
`ConvolutionLeft` as an explicit hypothesis, exactly as the dichotomy file does;
the structure `FrobeniusHopfData` itself no longer carries it.

## Results

* `scalarAct_natural` — scalars are natural: `s_X(τ) ≫ f = f ≫ s_Y(τ)`.
* `scalarAct_whiskerRight` — `s_X(τ) ▷ Y = s_{X ⊗ Y}(τ)`, pure coherence.
* `id_eq_comul_mul_scalarAct` — `𝟙_A = Δ ≫ μ ≫ s_A(σ)`.
* `retract_of_unit` — **`A` is a retract of `𝟙_C`, with no hypothesis on the
  scalars**: `(Δ ≫ μ ≫ ε) ≫ η = 𝟙_A`. Neither `Preadditive` nor a field is
  used. This is strictly stronger than the two branches of
  `dichotomy_of_scalars_field`, both of which it implies.
* `id_eq_zero_of_unitCounit_nilpotent` — if `σ` is nilpotent in the ring
  `End (𝟙_C)`, then `𝟙_A = 0`. Covers Artinian local scalar rings, e.g. the
  dual numbers `k[ε]/(ε²)`.
* `dichotomy_of_scalars_nilpotent_or_isIso` — when every scalar is nilpotent or
  invertible, `A` is a zero object or `σ` is invertible.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

open CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.FrobeniusHopfData
universe u v
section scalar
variable {C : Type u} [Category.{v} C] [MonoidalCategory C]

/-- left scalar action -/
def scalarAct (X : C) (τ : (𝟙_ C : C) ⟶ 𝟙_ C) : X ⟶ X :=
  (λ_ X).inv ≫ (τ ▷ X) ≫ (λ_ X).hom

theorem scalarAct_comp (X : C) (τ τ' : (𝟙_ C : C) ⟶ 𝟙_ C) :
    scalarAct X τ ≫ scalarAct X τ' = scalarAct X (τ ≫ τ') := by
  simp [scalarAct]

@[reassoc]
theorem scalarAct_natural {X Y : C} (f : X ⟶ Y) (τ : (𝟙_ C : C) ⟶ 𝟙_ C) :
    scalarAct X τ ≫ f = f ≫ scalarAct Y τ := by
  simp only [scalarAct, Category.assoc]
  rw [← leftUnitor_naturality, ← whisker_exchange_assoc, leftUnitor_inv_naturality_assoc]

theorem scalarAct_whiskerRight (X Y : C) (τ : (𝟙_ C : C) ⟶ 𝟙_ C) :
    scalarAct X τ ▷ Y = scalarAct (X ⊗ Y) τ := by
  simp [scalarAct, leftUnitor_inv_whiskerRight, leftUnitor_whiskerRight, whiskerRight_tensor]

end scalar

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
variable (F : QOU.FrobeniusHopfData C)

/-- The scalar `σ = η ≫ ε = ε(1)`, typed as an element of the ring `End (𝟙_C)`. -/
def unitCounit : End (𝟙_ C : C) := F.unit ≫ F.counit

theorem id_eq_comul_mul_scalarAct (hconv : F.ConvolutionLeft) :
    𝟙 F.obj = F.comul ≫ F.mul ≫ scalarAct F.obj (F.unit ≫ F.counit) := by
  have hloop : F.comul ≫ ((F.counit ≫ F.unit) ▷ F.obj) ≫ F.mul = 𝟙 F.obj := by
    rw [comp_whiskerRight, Category.assoc, F.one_mul, ← Category.assoc, F.counit_comul,
      Iso.inv_hom_id]
  rw [← hloop, F.scalar_id_eq_counit_unit_of_convolutionLeft hconv]
  change F.comul ≫ (scalarAct F.obj (F.unit ≫ F.counit) ▷ F.obj) ≫ F.mul = _
  rw [scalarAct_whiskerRight, scalarAct_natural]

theorem retract_of_unit (hconv : F.ConvolutionLeft) :
    (F.comul ≫ F.mul ≫ F.counit) ≫ F.unit = 𝟙 F.obj := by
  have hs : scalarAct F.obj (F.unit ≫ F.counit) = F.counit ≫ F.unit :=
    (F.scalar_id_eq_counit_unit_of_convolutionLeft hconv).symm
  conv_rhs => rw [id_eq_comul_mul_scalarAct F hconv, hs]
  simp only [Category.assoc]

theorem id_eq_comp_scalarAct_pow (hconv : F.ConvolutionLeft) (n : ℕ) :
    ∃ M : F.obj ⟶ F.obj, 𝟙 F.obj = M ≫ scalarAct F.obj (F.unitCounit ^ n) := by
  induction n with
  | zero => exact ⟨𝟙 F.obj, by simp [scalarAct, pow_zero, End.one_def]⟩
  | succ k ih =>
    obtain ⟨M, hM⟩ := ih
    refine ⟨M ≫ F.comul ≫ F.mul, ?_⟩
    have h1 : 𝟙 F.obj = F.comul ≫ F.mul ≫ scalarAct F.obj F.unitCounit :=
      id_eq_comul_mul_scalarAct F hconv
    calc 𝟙 F.obj = M ≫ scalarAct F.obj (F.unitCounit ^ k) ≫ 𝟙 F.obj := by
          rw [Category.comp_id, ← hM]
      _ = M ≫ scalarAct F.obj (F.unitCounit ^ k) ≫ F.comul ≫ F.mul
            ≫ scalarAct F.obj F.unitCounit := by rw [← h1]
      _ = (M ≫ F.comul ≫ F.mul) ≫ scalarAct F.obj (F.unitCounit ^ (k + 1)) := by
          rw [scalarAct_natural_assoc F.comul, scalarAct_natural_assoc F.mul, scalarAct_comp,
            pow_succ', End.mul_def]
          simp only [Category.assoc]

theorem id_eq_zero_of_unitCounit_nilpotent [Preadditive C] [MonoidalPreadditive C]
    (hconv : F.ConvolutionLeft) (h : IsNilpotent F.unitCounit) :
    𝟙 F.obj = 0 := by
  obtain ⟨n, hn⟩ := h
  obtain ⟨M, hM⟩ := id_eq_comp_scalarAct_pow F hconv n
  rw [hM, hn]
  simp [scalarAct]

theorem dichotomy_of_scalars_nilpotent_or_isIso [Preadditive C] [MonoidalPreadditive C]
    (hconv : F.ConvolutionLeft)
    (hscal : ∀ σ : End (𝟙_ C : C), IsNilpotent σ ∨ IsIso σ) :
    𝟙 F.obj = 0 ∨ IsIso F.unitCounit := by
  rcases hscal F.unitCounit with h | h
  · exact Or.inl (F.id_eq_zero_of_unitCounit_nilpotent hconv h)
  · exact Or.inr h

end QOU.FrobeniusHopfData
