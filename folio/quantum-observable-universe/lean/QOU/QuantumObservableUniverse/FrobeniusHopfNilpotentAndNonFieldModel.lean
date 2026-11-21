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

## The explicit model (`QOU.IdemLine`)

Over any commutative ring `R` (§7c: generic base ring, no `ℝ`), the category of
idempotents `Obj R` below carries a `FrobeniusHopfData` on every object `A = eR`
(`model`), with every structure morphism equal to `e`. It satisfies
`ConvolutionLeft`, and `σ = ε(1) = e`.

* `model_sharpness` — for `e ∉ {0, 1}`: `𝟙_A ≠ 0`, `A ≇ 𝟙`, `σ ≠ 0`,
  `σ` not invertible, hence the hypothesis `∀ σ, σ = 0 ∨ IsIso σ` of
  `dichotomy_of_scalars_field` fails.
* `splitPair_sharpness` — the instance `R = S × S`, `e = (1, 0)`, for any
  nontrivial commutative ring `S`.

## Scope (what this does and does not settle)

* The model's `A` is a **proper direct summand** of the unit, so it is a retract
  of `𝟙`, exactly as `retract_of_unit` requires of every model. It shows that
  the field hypothesis of the dichotomy is not necessary for its conclusion; it
  is **not** a "non-trivial substrate" in the sense of bean `qou-aawz`.
* `retract_of_unit` answers the first limit recorded in
  `FrobeniusHopfModelDichotomy` (the non-linear case) **for the convolution
  condition**: under `ConvolutionLeft`, `A` is a retract of `𝟙` in every
  monoidal category. The structure no longer carries `ConvolutionLeft`; what the
  anti-automorphism package alone permits is not addressed here.

No `sorry`, no new axioms (`#print axioms`: `propext`, `Classical.choice`,
`Quot.sound`).
-/



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


/-!
## The idempotent-line category of a commutative ring

`QOU.IdemLine.Obj R` has the idempotents `e` of a commutative ring `R` as
objects (`e` stands for the summand `eR`), morphisms `X ⟶ Y` the elements `r`
with `r · X.e · Y.e = r`, composition by multiplication, `X ⊗ Y = X.e · Y.e`,
unit `1`, and every coherence isomorphism given by the evident idempotent.
It is a full subcategory of `R`-modules up to equivalence, written out so that
every axiom is a ring identity among idempotents.

It is preadditive, monoidal preadditive and braided, and `End (𝟙) = R`.
-/

namespace QOU.IdemLine

universe w

/-- An idempotent `e` of `R`, standing for the summand `eR` of `R`. -/
@[ext] structure Obj (R : Type w) [CommRing R] where
  e : R
  idem : e * e = e

variable {R : Type w} [CommRing R]

theorem Obj.pow_eq (X : Obj R) (n : ℕ) : X.e ^ (n + 1) = X.e :=
  IsIdempotentElem.pow_succ_eq n X.idem
theorem Obj.pow2 (X : Obj R) : X.e ^ 2 = X.e := X.pow_eq 1
theorem Obj.pow3 (X : Obj R) : X.e ^ 3 = X.e := X.pow_eq 2
theorem Obj.pow4 (X : Obj R) : X.e ^ 4 = X.e := X.pow_eq 3
theorem Obj.pow5 (X : Obj R) : X.e ^ 5 = X.e := X.pow_eq 4
theorem Obj.pow6 (X : Obj R) : X.e ^ 6 = X.e := X.pow_eq 5
theorem Obj.pow7 (X : Obj R) : X.e ^ 7 = X.e := X.pow_eq 6
theorem Obj.pow8 (X : Obj R) : X.e ^ 8 = X.e := X.pow_eq 7
theorem Obj.pow9 (X : Obj R) : X.e ^ 9 = X.e := X.pow_eq 8
theorem Obj.pow10 (X : Obj R) : X.e ^ 10 = X.e := X.pow_eq 9
theorem Obj.pow11 (X : Obj R) : X.e ^ 11 = X.e := X.pow_eq 10
theorem Obj.pow12 (X : Obj R) : X.e ^ 12 = X.e := X.pow_eq 11
theorem Obj.pow13 (X : Obj R) : X.e ^ 13 = X.e := X.pow_eq 12
theorem Obj.pow14 (X : Obj R) : X.e ^ 14 = X.e := X.pow_eq 13
theorem Obj.pow15 (X : Obj R) : X.e ^ 15 = X.e := X.pow_eq 14
theorem Obj.pow16 (X : Obj R) : X.e ^ 16 = X.e := X.pow_eq 15

/-- The morphisms `X ⟶ Y`: elements `r` with `r · X.e · Y.e = r`. -/
def homGroup (X Y : Obj R) : AddSubgroup R where
  carrier := {r | r * (X.e * Y.e) = r}
  zero_mem' := by simp
  add_mem' := by
    intro a b ha hb
    simp only [Set.mem_setOf_eq] at *
    rw [add_mul, ha, hb]
  neg_mem' := by
    intro a ha
    simp only [Set.mem_setOf_eq] at *
    rw [neg_mul, ha]

theorem mem_iff {X Y : Obj R} {r : R} : r ∈ homGroup X Y ↔ r * (X.e * Y.e) = r := Iff.rfl

/-- Normalise a ring identity in idempotents: expand, collapse powers, compare. -/
macro "idem_ring" : tactic =>
  `(tactic| (ring_nf; (try simp only [Obj.pow2, Obj.pow3, Obj.pow4, Obj.pow5, Obj.pow6, Obj.pow7, Obj.pow8, Obj.pow9, Obj.pow10, Obj.pow11, Obj.pow12, Obj.pow13, Obj.pow14, Obj.pow15, Obj.pow16]); (try ring_nf)))

theorem val_eq {X Y : Obj R} (f : homGroup X Y) : (f : R) = f * (X.e * Y.e) := f.2.symm

instance : Category (Obj R) where
  Hom X Y := homGroup X Y
  id X := ⟨X.e, by rw [mem_iff, X.idem, X.idem]⟩
  comp f g := ⟨(f : R) * g, by
    rw [mem_iff, val_eq f, val_eq g]; idem_ring⟩
  id_comp f := Subtype.ext (by
    show _ * (f : R) = f
    conv_rhs => rw [val_eq f]
    conv_lhs => rw [val_eq f]
    idem_ring)
  comp_id f := Subtype.ext (by
    show (f : R) * _ = f
    conv_rhs => rw [val_eq f]
    conv_lhs => rw [val_eq f]
    idem_ring)
  assoc f g h := Subtype.ext (by show (f : R) * g * h = f * (g * h); ring)

/-- The ring element underlying a morphism. -/
def v {X Y : Obj R} (f : X ⟶ Y) : R := (show ↥(homGroup X Y) from f).1

theorem v_mem {X Y : Obj R} (f : X ⟶ Y) : v f * (X.e * Y.e) = v f :=
  (show ↥(homGroup X Y) from f).2

theorem v_eq {X Y : Obj R} (f : X ⟶ Y) : v f = v f * (X.e * Y.e) := (v_mem f).symm

@[simp] theorem v_id (X : Obj R) : v (𝟙 X) = X.e := rfl
@[simp] theorem v_comp {X Y Z : Obj R} (f : X ⟶ Y) (g : Y ⟶ Z) : v (f ≫ g) = v f * v g := rfl

theorem hom_ext {X Y : Obj R} {f g : X ⟶ Y} (h : v f = v g) : f = g := Subtype.ext h

/-- Build a morphism from a ring element and its membership proof. -/
def mk {X Y : Obj R} (r : R) (h : r * (X.e * Y.e) = r) : X ⟶ Y := ⟨r, h⟩
@[simp] theorem v_mk {X Y : Obj R} (r : R) (h : r * (X.e * Y.e) = r) : v (mk (X := X) (Y := Y) r h) = r := rfl


/-! ### Additive structure -/

instance (X Y : Obj R) : AddCommGroup (X ⟶ Y) :=
  inferInstanceAs (AddCommGroup (homGroup X Y))

@[simp] theorem v_add {X Y : Obj R} (f g : X ⟶ Y) : v (f + g) = v f + v g := rfl
@[simp] theorem v_zero {X Y : Obj R} : v (0 : X ⟶ Y) = 0 := rfl

instance : Preadditive (Obj R) where
  add_comp _ _ _ f f' g := hom_ext (by simp only [v_comp, v_add]; ring)
  comp_add _ _ _ f g g' := hom_ext (by simp only [v_comp, v_add]; ring)

/-! ### Monoidal structure: `eR ⊗ fR = efR` -/

/-- Tensor product of idempotents. -/
def tens (X Y : Obj R) : Obj R :=
  ⟨X.e * Y.e, by rw [mul_mul_mul_comm, X.idem, Y.idem]⟩

/-- The unit object `1·R`. -/
def unitObj : Obj R := ⟨1, mul_one 1⟩

/-- An isomorphism whose two components carry the same element `r`, an idempotent
    equal to both endpoint idempotents. -/
def isoOfEq (X Y : Obj R) (h : X.e = Y.e) : X ≅ Y where
  hom := mk X.e (by rw [← h, X.idem, X.idem])
  inv := mk X.e (by rw [← h, X.idem, X.idem])
  hom_inv_id := hom_ext (by simp only [v_comp, v_mk, v_id]; exact X.idem)
  inv_hom_id := hom_ext (by simp only [v_comp, v_mk, v_id]; rw [X.idem, h])

@[simp] theorem v_isoOfEq_hom (X Y : Obj R) (h : X.e = Y.e) : v (isoOfEq X Y h).hom = X.e := rfl
@[simp] theorem v_isoOfEq_inv (X Y : Obj R) (h : X.e = Y.e) : v (isoOfEq X Y h).inv = X.e := rfl

instance : MonoidalCategoryStruct (Obj R) where
  tensorObj := tens
  whiskerLeft X _ _ f := mk (X.e * v f) (by
    show X.e * v f * ((X.e * _) * (X.e * _)) = X.e * v f
    rw [v_eq f]; idem_ring)
  whiskerRight f Y := mk (v f * Y.e) (by
    show v f * Y.e * ((_ * Y.e) * (_ * Y.e)) = v f * Y.e
    rw [v_eq f]; idem_ring)
  tensorHom f g := mk (v f * v g) (by
    show v f * v g * ((_ * _) * (_ * _)) = v f * v g
    rw [v_eq f, v_eq g]; idem_ring)
  tensorUnit := unitObj
  associator X Y Z := isoOfEq (tens (tens X Y) Z) (tens X (tens Y Z)) (mul_assoc _ _ _)
  leftUnitor X := isoOfEq (tens unitObj X) X (one_mul _)
  rightUnitor X := isoOfEq (tens X unitObj) X (mul_one _)

@[simp] theorem e_tensor (X Y : Obj R) : (X ⊗ Y).e = X.e * Y.e := rfl
@[simp] theorem e_unit : (𝟙_ (Obj R)).e = 1 := rfl
@[simp] theorem v_whiskerLeft (X : Obj R) {Y Z : Obj R} (f : Y ⟶ Z) : v (X ◁ f) = X.e * v f := rfl
@[simp] theorem v_whiskerRight {X Y : Obj R} (f : X ⟶ Y) (Z : Obj R) : v (f ▷ Z) = v f * Z.e := rfl
@[simp] theorem v_tensorHom {X Y X' Y' : Obj R} (f : X ⟶ Y) (g : X' ⟶ Y') :
    v (f ⊗ₘ g) = v f * v g := rfl
@[simp] theorem v_associator_hom (X Y Z : Obj R) : v (α_ X Y Z).hom = X.e * Y.e * Z.e := rfl
@[simp] theorem v_associator_inv (X Y Z : Obj R) : v (α_ X Y Z).inv = X.e * Y.e * Z.e := rfl
@[simp] theorem v_leftUnitor_hom (X : Obj R) : v (λ_ X).hom = 1 * X.e := rfl
@[simp] theorem v_leftUnitor_inv (X : Obj R) : v (λ_ X).inv = 1 * X.e := rfl
@[simp] theorem v_rightUnitor_hom (X : Obj R) : v (ρ_ X).hom = X.e * 1 := rfl
@[simp] theorem v_rightUnitor_inv (X : Obj R) : v (ρ_ X).inv = X.e * 1 := rfl

instance : MonoidalCategory (Obj R) where
  tensorHom_def f g := hom_ext (by
    simp only [v_tensorHom, v_comp, v_whiskerLeft, v_whiskerRight]
    rw [v_eq f, v_eq g]; idem_ring)
  id_tensorHom_id X Y := hom_ext (by simp)
  tensorHom_comp_tensorHom f₁ f₂ g₁ g₂ := hom_ext (by simp only [v_tensorHom, v_comp]; ring)
  whiskerLeft_id X Y := hom_ext (by simp only [v_whiskerLeft, v_id, e_tensor])
  id_whiskerRight X Y := hom_ext (by simp only [v_whiskerRight, v_id, e_tensor])
  associator_naturality f₁ f₂ f₃ := hom_ext (by
    simp only [v_tensorHom, v_comp, v_associator_hom]
    rw [v_eq f₁, v_eq f₂, v_eq f₃]; idem_ring)
  leftUnitor_naturality f := hom_ext (by
    simp only [v_whiskerLeft, v_comp, v_leftUnitor_hom, e_unit]
    rw [v_eq f]; idem_ring)
  rightUnitor_naturality f := hom_ext (by
    simp only [v_whiskerRight, v_comp, v_rightUnitor_hom, e_unit]
    rw [v_eq f]; idem_ring)
  pentagon W X Y Z := hom_ext (by simp; idem_ring)
  triangle X Y := hom_ext (by simp; idem_ring)

instance : MonoidalPreadditive (Obj R) where
  whiskerLeft_zero := hom_ext (by simp)
  zero_whiskerRight := hom_ext (by simp)
  whiskerLeft_add f g := hom_ext (by simp only [v_whiskerLeft, v_add]; ring)
  add_whiskerRight f g := hom_ext (by simp only [v_whiskerRight, v_add]; ring)

/-- The (symmetric) braiding: the identity element `X.e · Y.e`. -/
instance : BraidedCategory (Obj R) where
  braiding X Y := isoOfEq (X ⊗ Y) (Y ⊗ X) (mul_comm _ _)
  braiding_naturality_right X _ _ f := hom_ext (by
    simp only [v_whiskerLeft, v_whiskerRight, v_comp, v_isoOfEq_hom, e_tensor]
    rw [v_eq f]; idem_ring)
  braiding_naturality_left f Z := hom_ext (by
    simp only [v_whiskerLeft, v_whiskerRight, v_comp, v_isoOfEq_hom, e_tensor]
    rw [v_eq f]; idem_ring)
  hexagon_forward X Y Z := hom_ext (by simp; idem_ring)
  hexagon_reverse X Y Z := hom_ext (by simp; idem_ring)


@[simp] theorem v_braiding_hom (X Y : Obj R) : v (β_ X Y).hom = X.e * Y.e := rfl
@[simp] theorem v_braiding_inv (X Y : Obj R) : v (β_ X Y).inv = X.e * Y.e := rfl

/-! ### The Frobenius–Hopf model on an idempotent -/

/-- The morphism carried by the element `A.e`, between any two objects built from
    `A` and the unit. -/
def eHom (A : Obj R) {X Y : Obj R} (h : A.e * (X.e * Y.e) = A.e) : X ⟶ Y := mk A.e h

@[simp] theorem v_eHom (A : Obj R) {X Y : Obj R} (h : A.e * (X.e * Y.e) = A.e) :
    v (eHom A h : X ⟶ Y) = A.e := rfl

/-- **The model.** On the summand `A = eR`, every structure morphism — `μ`, `η`,
    `Δ`, `ε`, `S`, `λ`, `coev` — is the element `e`. -/
def model (A : Obj R) : QOU.FrobeniusHopfData (Obj R) where
  obj := A
  mul := eHom A (by simp only [e_tensor]; idem_ring)
  unit := eHom A (by simp only [e_unit]; idem_ring)
  comul := eHom A (by simp only [e_tensor]; idem_ring)
  counit := eHom A (by simp only [e_unit]; idem_ring)
  antipode := eHom A (by idem_ring)
  frobeniusForm := eHom A (by simp only [e_unit]; idem_ring)
  coevaluation := eHom A (by simp only [e_tensor, e_unit]; idem_ring)
  pairing_snake_left := hom_ext (by simp; idem_ring)
  pairing_snake_right := hom_ext (by simp; idem_ring)
  frobenius_relation := hom_ext (by simp; idem_ring)
  one_mul := hom_ext (by simp; idem_ring)
  mul_one := hom_ext (by simp; idem_ring)
  mul_assoc := hom_ext (by simp; idem_ring)
  counit_comul := hom_ext (by simp; idem_ring)
  comul_counit := hom_ext (by simp; idem_ring)
  comul_assoc := hom_ext (by simp; idem_ring)
  antipode_anti_mul := hom_ext (by simp; idem_ring)
  antipode_anti_comul := hom_ext (by simp; idem_ring)
  antipode_unit := hom_ext (by simp; idem_ring)
  antipode_counit := hom_ext (by simp; idem_ring)
  antipode_involutive := hom_ext (by simp; idem_ring)
  antipode_frobeniusForm := hom_ext (by simp; idem_ring)


@[simp] theorem v_unitCounit (A : Obj R) : v (model A).unitCounit = A.e := by
  show A.e * A.e = A.e
  exact A.idem

theorem model_convolutionLeft (A : Obj R) : (model A).ConvolutionLeft :=
  hom_ext (by simp [model]; idem_ring)

/-- `σ = ε(1)` is non-zero as soon as `e ≠ 0`. -/
theorem unitCounit_ne_zero (A : Obj R) (h : A.e ≠ 0) : (model A).unitCounit ≠ 0 := by
  intro hσ
  apply h
  rw [← v_unitCounit A, hσ, v_zero]

/-- `σ = ε(1)` is not invertible as soon as `e ≠ 1`. -/
theorem not_isIso_unitCounit (A : Obj R) (h : A.e ≠ 1) : ¬ IsIso (model A).unitCounit := by
  intro hiso
  apply h
  have h1 : v ((model A).unitCounit ≫ inv (model A).unitCounit) = 1 := by
    rw [IsIso.hom_inv_id]; rfl
  rw [v_comp, v_unitCounit] at h1
  calc A.e = A.e * (A.e * v (inv (model A).unitCounit)) := by rw [h1, mul_one]
    _ = A.e * v (inv (model A).unitCounit) := by rw [← mul_assoc, A.idem]
    _ = 1 := h1

/-- The object is not a zero object when `e ≠ 0`. -/
theorem id_ne_zero (A : Obj R) (h : A.e ≠ 0) : 𝟙 (model A).obj ≠ 0 := by
  intro h0
  apply h
  have := congrArg v h0
  simpa [model] using this

/-- The object is not isomorphic to the tensor unit when `e ≠ 1`. -/
theorem not_iso_unit (A : Obj R) (h : A.e ≠ 1) : IsEmpty ((model A).obj ≅ 𝟙_ (Obj R)) := by
  refine ⟨fun i => h ?_⟩
  have h1 : v (i.inv ≫ i.hom) = 1 := by rw [Iso.inv_hom_id]; rfl
  have hh : v i.hom * A.e = v i.hom := by
    have := v_mem i.hom
    simp only [e_unit, mul_one] at this
    exact this
  rw [v_comp] at h1
  calc A.e = v i.inv * v i.hom * A.e := by rw [h1, one_mul]
    _ = v i.inv * v i.hom := by rw [mul_assoc, hh]
    _ = 1 := h1

/-- **Sharpness of the field hypothesis.** For an idempotent `e ∉ {0, 1}`, the
    model satisfies `ConvolutionLeft`, is neither a zero object nor isomorphic to
    the unit, and its scalar `σ = ε(1)` is neither zero nor invertible — so the
    hypothesis `∀ σ, σ = 0 ∨ IsIso σ` of `dichotomy_of_scalars_field` fails. -/
theorem model_sharpness (A : Obj R) (h0 : A.e ≠ 0) (h1 : A.e ≠ 1) :
    (model A).ConvolutionLeft ∧ 𝟙 (model A).obj ≠ 0 ∧ IsEmpty ((model A).obj ≅ 𝟙_ (Obj R))
      ∧ (model A).unitCounit ≠ 0 ∧ ¬ IsIso (model A).unitCounit
      ∧ ¬ (∀ σ : (𝟙_ (Obj R) : Obj R) ⟶ 𝟙_ (Obj R), σ = 0 ∨ IsIso σ) := by
  refine ⟨model_convolutionLeft A, id_ne_zero A h0, not_iso_unit A h1,
    unitCounit_ne_zero A h0, not_isIso_unitCounit A h1, fun hall => ?_⟩
  rcases hall (model A).unitCounit with h | h
  · exact unitCounit_ne_zero A h0 h
  · exact not_isIso_unitCounit A h1 h

/-! ### The split ring `S × S` -/

/-- The idempotent `(1, 0)` of `S × S`. -/
def splitIdem (S : Type w) [CommRing S] : Obj (S × S) := ⟨(1, 0), by simp⟩

theorem splitIdem_ne_zero (S : Type w) [CommRing S] [Nontrivial S] : (splitIdem S).e ≠ 0 := by
  intro h
  have := congrArg Prod.fst h
  exact one_ne_zero this

theorem splitIdem_ne_one (S : Type w) [CommRing S] [Nontrivial S] : (splitIdem S).e ≠ 1 := by
  intro h
  have := congrArg Prod.snd h
  exact zero_ne_one this

/-- **An explicit non-zero, non-unit model over the split ring `S × S`**, for any
    nontrivial commutative ring `S`. -/
theorem splitPair_sharpness (S : Type w) [CommRing S] [Nontrivial S] :
    ∃ F : QOU.FrobeniusHopfData (Obj (S × S)),
      F.ConvolutionLeft ∧ 𝟙 F.obj ≠ 0 ∧ IsEmpty (F.obj ≅ 𝟙_ (Obj (S × S)))
        ∧ F.unitCounit ≠ 0 ∧ ¬ IsIso F.unitCounit :=
  let h := model_sharpness (splitIdem S) (splitIdem_ne_zero S) (splitIdem_ne_one S)
  ⟨model (splitIdem S), h.1, h.2.1, h.2.2.1, h.2.2.2.1, h.2.2.2.2.1⟩

end QOU.IdemLine