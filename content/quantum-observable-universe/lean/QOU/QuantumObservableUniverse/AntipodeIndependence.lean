import QOU.QuantumObservableUniverse.CategoricalFoundations

/-!
# The antipode of `FrobeniusHopfData` is free data

`QOU.FrobeniusHopfData` carries eight data fields (`obj`, `mul`, `unit`,
`comul`, `counit`, `antipode`, `frobeniusForm`, `coevaluation`) and three
law fields (`pairing_snake_left`, `pairing_snake_right`,
`frobenius_relation`).  Three of the data fields — `unit`, `counit` and
`antipode` — are **mentioned by no law**.

This file records the consequence for the question *"does `S² = id` hold
for the QOU substrate?"*.  The answer is neither yes nor no: the
proposition is **independent of the definition as it stands**.  There is no
antipode axiom (`μ ∘ (S ⊗ id) ∘ Δ = η ∘ ε`) in `FrobeniusHopfData`, so `S`
is constrained by nothing and no property of it is derivable.

The theorems below make that statement machine-checked rather than
editorial:

* `withAntipode` replaces the antipode with an arbitrary endomorphism and
  still produces a `FrobeniusHopfData` — the same three proofs discharge
  the same three laws.
* `antipode_property_vacuous` turns that into the independence statement:
  any property provable of *every* substrate's antipode holds of *every*
  endomorphism of *every* substrate object.
* `involutive_of_sq_eq_id`, `endo_comm_of_sq_involutive` and
  `id_eq_zero_of_sq_eq_id` trace out what assuming `S ≫ S = 𝟙`
  as a theorem would cost: every endomorphism monoid of every
  Frobenius–Hopf object would be commutative of exponent two, and — as
  soon as the ambient category has zero morphisms — every Frobenius–Hopf
  object would be a zero object.

**This is not a refutation of `S² = id` as mathematics.**  It is a
statement about the present axioms.  Whether the intended substrate
satisfies `S² = id` depends on an antipode axiom that has not been
written down, and adding one is a change to `def:frobenius-hopf-substrate`
rather than a theorem about it.

## References

- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
- [lusztig1993] G. Lusztig, *Introduction to Quantum Groups*, Birkhäuser 1993.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C]

namespace FrobeniusHopfData

/-! ### The three unconstrained fields -/

/-- Replace the antipode by an arbitrary endomorphism of the same object.
    Every law of `FrobeniusHopfData` is discharged by the *same* proof as in
    `F`, because no law mentions `antipode`. -/
def withAntipode (F : FrobeniusHopfData C) (g : F.obj ⟶ F.obj) :
    FrobeniusHopfData C :=
  { F with antipode := g }

/-- Replace the unit by an arbitrary morphism `𝟙 ⟶ A`.  No law mentions
    `unit` either. -/
def withUnit (F : FrobeniusHopfData C) (g : (𝟙_ C) ⟶ F.obj) :
    FrobeniusHopfData C :=
  { F with unit := g }

/-- Replace the counit by an arbitrary morphism `A ⟶ 𝟙`.  No law mentions
    `counit` either. -/
def withCounit (F : FrobeniusHopfData C) (g : F.obj ⟶ (𝟙_ C)) :
    FrobeniusHopfData C :=
  { F with counit := g }

@[simp] theorem withAntipode_obj (F : FrobeniusHopfData C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).obj = F.obj := rfl

@[simp] theorem withAntipode_antipode (F : FrobeniusHopfData C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).antipode = g := rfl

@[simp] theorem withAntipode_mul (F : FrobeniusHopfData C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).mul = F.mul := rfl

@[simp] theorem withAntipode_comul (F : FrobeniusHopfData C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).comul = F.comul := rfl

@[simp] theorem withAntipode_frobeniusForm (F : FrobeniusHopfData C)
    (g : F.obj ⟶ F.obj) :
    (F.withAntipode g).frobeniusForm = F.frobeniusForm := rfl

@[simp] theorem withAntipode_coevaluation (F : FrobeniusHopfData C)
    (g : F.obj ⟶ F.obj) :
    (F.withAntipode g).coevaluation = F.coevaluation := rfl

@[simp] theorem withUnit_unit (F : FrobeniusHopfData C)
    (g : (𝟙_ C) ⟶ F.obj) : (F.withUnit g).unit = g := rfl

@[simp] theorem withCounit_counit (F : FrobeniusHopfData C)
    (g : F.obj ⟶ (𝟙_ C)) : (F.withCounit g).counit = g := rfl

/-! ### Independence -/

/-- **The antipode is unconstrained.**  If a property `P` of antipodes is
    provable for every `FrobeniusHopfData`, then it holds of *every*
    endomorphism of *every* Frobenius–Hopf object.

    Contrapositive, which is how this is used: to show that some property
    of `S` is **not** derivable from the axioms of `FrobeniusHopfData`, it
    suffices to exhibit one Frobenius–Hopf object with one endomorphism
    lacking it. -/
theorem antipode_property_vacuous
    (P : ∀ F : FrobeniusHopfData C, (F.obj ⟶ F.obj) → Prop)
    (hP : ∀ F : FrobeniusHopfData C, P F F.antipode)
    (F : FrobeniusHopfData C) (g : F.obj ⟶ F.obj) :
    P (F.withAntipode g) g :=
  hP (F.withAntipode g)

/-- The same statement for the unit. -/
theorem unit_property_vacuous
    (P : ∀ F : FrobeniusHopfData C, ((𝟙_ C) ⟶ F.obj) → Prop)
    (hP : ∀ F : FrobeniusHopfData C, P F F.unit)
    (F : FrobeniusHopfData C) (g : (𝟙_ C) ⟶ F.obj) :
    P (F.withUnit g) g :=
  hP (F.withUnit g)

/-- The same statement for the counit. -/
theorem counit_property_vacuous
    (P : ∀ F : FrobeniusHopfData C, (F.obj ⟶ (𝟙_ C)) → Prop)
    (hP : ∀ F : FrobeniusHopfData C, P F F.counit)
    (F : FrobeniusHopfData C) (g : F.obj ⟶ (𝟙_ C)) :
    P (F.withCounit g) g :=
  hP (F.withCounit g)

/-! ### What `S ≫ S = 𝟙` would cost if it were a theorem -/

/-- If `S ≫ S = 𝟙` were derivable from the axioms of `FrobeniusHopfData`,
    then **every** endomorphism of **every** Frobenius–Hopf object would be
    an involution. -/
theorem involutive_of_sq_eq_id
    (h : ∀ F : FrobeniusHopfData C, F.antipode ≫ F.antipode = CategoryTheory.CategoryStruct.id F.obj)
    (F : FrobeniusHopfData C) (g : F.obj ⟶ F.obj) :
    g ≫ g = CategoryTheory.CategoryStruct.id F.obj :=
  h (F.withAntipode g)

end FrobeniusHopfData

omit [CategoryTheory.MonoidalCategory C] in
/-- A monoid in which every element squares to the identity is commutative,
    stated for the endomorphism monoid of an object of a category.  Pure
    category theory; no Frobenius–Hopf structure involved. -/
theorem endo_comm_of_sq_involutive {X : C}
    (hsq : ∀ f : X ⟶ X, f ≫ f = CategoryTheory.CategoryStruct.id X)
    (a b : X ⟶ X) : a ≫ b = b ≫ a := by
  have h3 := hsq (a ≫ b)
  have key : b ≫ a ≫ b = a := by
    calc b ≫ a ≫ b
        = (CategoryTheory.CategoryStruct.id X) ≫ (b ≫ a ≫ b) := by
          rw [CategoryTheory.Category.id_comp]
      _ = (a ≫ a) ≫ (b ≫ a ≫ b) := by rw [hsq a]
      _ = a ≫ ((a ≫ b) ≫ (a ≫ b)) := by simp only [CategoryTheory.Category.assoc]
      _ = a ≫ CategoryTheory.CategoryStruct.id X := by rw [h3]
      _ = a := CategoryTheory.Category.comp_id a
  calc a ≫ b = (b ≫ a ≫ b) ≫ b := by rw [key]
    _ = b ≫ a ≫ (b ≫ b) := by simp only [CategoryTheory.Category.assoc]
    _ = b ≫ a ≫ CategoryTheory.CategoryStruct.id X := by rw [hsq b]
    _ = b ≫ a := by rw [CategoryTheory.Category.comp_id]

/-- **The cost, part one.**  Were `S ≫ S = 𝟙` a theorem, the endomorphism
    monoid of every Frobenius–Hopf object would be commutative. -/
theorem endo_comm_of_antipode_sq_eq_id
    (h : ∀ F : FrobeniusHopfData C, F.antipode ≫ F.antipode = CategoryTheory.CategoryStruct.id F.obj)
    (F : FrobeniusHopfData C) (a b : F.obj ⟶ F.obj) : a ≫ b = b ≫ a :=
  endo_comm_of_sq_involutive (fun g => FrobeniusHopfData.involutive_of_sq_eq_id h F g) a b

/-- **The cost, part two.**  As soon as the ambient monoidal category has
    zero morphisms, `S ≫ S = 𝟙` as a theorem would force `𝟙_A = 0` for
    every Frobenius–Hopf object `A` — i.e. every Frobenius–Hopf object
    would be a zero object.  Take `g = 0` in `involutive_of_sq_eq_id`:
    `0 ≫ 0 = 0`, so `0 = 𝟙`. -/
theorem id_eq_zero_of_antipode_sq_eq_id
    [CategoryTheory.Limits.HasZeroMorphisms C]
    (h : ∀ F : FrobeniusHopfData C, F.antipode ≫ F.antipode = CategoryTheory.CategoryStruct.id F.obj)
    (F : FrobeniusHopfData C) :
    (0 : F.obj ⟶ F.obj) = CategoryTheory.CategoryStruct.id F.obj := by
  have := FrobeniusHopfData.involutive_of_sq_eq_id h F 0
  rwa [CategoryTheory.Limits.zero_comp] at this

end QOU
