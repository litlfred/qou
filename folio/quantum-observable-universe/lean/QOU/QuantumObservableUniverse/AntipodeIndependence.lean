import QOU.QuantumObservableUniverse.CategoricalFoundations

/-!
# Historical record: the antipode WAS free data, and `S² = id` WAS independent

**This file is a record of a state the corpus has left.**  On 2026-09-14 the
owner decided to add the Hopf antipode axiom to `def:frobenius-hopf-substrate`
(beans `qou-c64q`, `qou-qjhc`).  `QOU.FrobeniusHopfData` now carries
`antipode_left` / `antipode_right`, and `QOU.FrobeniusHopfData.antipode_unique`
(in `QOU.QuantumObservableUniverse.AntipodeDetermined`) shows the antipode is
determined by the rest of the data.  **The hole described below is closed.**

What is kept here is the machine-checked statement of what was wrong, over a
structure `FrobeniusHopfDataPreAxiom` reproducing the pre-2026-09-14 shape of
`FrobeniusHopfData` exactly: eight data fields and three laws
(`pairing_snake_left`, `pairing_snake_right`, `frobenius_relation`).

The point it records: **`unit`, `counit` and `antipode` were mentioned by no
law.**  A field constrained by nothing is free data — no property of it is
derivable, and none is refutable — so `S² = id` was neither open nor false but
*independent of the definition*.  That is a third epistemic state, and it was
being filed as the first.

The prose said otherwise, which is how it survived: axiom 2 of the block read
*"with antipode `S : A → A` satisfying the Hopf compatibility
`ε ∘ μ = u ∘ (ε ⊗ ε)`"* — a condition in which `S` appears on neither side.
A QA reviewer had already flagged it in the block's own sidecar
(`frobenius-hopf-substrate.qa.json`, criterion `trap-nonspeakable`); this file
is the machine-checked form of that reading, and
`scripts/lean-structure-field-law-audit.py` is its mechanical detector.

## References

- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
- [kassel1995] C. Kassel, *Quantum Groups*, Springer 1995, Ch. III.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.AntipodeIndependence

universe u v

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C]

/-- **The pre-2026-09-14 shape of `QOU.FrobeniusHopfData`**, reproduced so the
    independence result below stays checkable after the live structure gained
    its algebra / coalgebra / antipode laws.

    Eight data fields; three laws.  `unit`, `counit` and `antipode` occur in
    none of the three. -/
structure FrobeniusHopfDataPreAxiom (C : Type u)
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C] where
  /-- The underlying object `A`. -/
  obj : C
  /-- Multiplication `μ : A ⊗ A ⟶ A`. -/
  mul : (obj ⊗ obj) ⟶ obj
  /-- Unit `η : 𝟙 ⟶ A`.  Constrained by no law below. -/
  unit : (𝟙_ C) ⟶ obj
  /-- Comultiplication `Δ : A ⟶ A ⊗ A`. -/
  comul : obj ⟶ (obj ⊗ obj)
  /-- Counit `ε : A ⟶ 𝟙`.  Constrained by no law below. -/
  counit : obj ⟶ (𝟙_ C)
  /-- Antipode `S : A ⟶ A`.  Constrained by no law below — the whole point. -/
  antipode : obj ⟶ obj
  /-- Frobenius form `λ : A ⟶ 𝟙`. -/
  frobeniusForm : obj ⟶ (𝟙_ C)
  /-- Coevaluation `𝟙 ⟶ A ⊗ A`. -/
  coevaluation : (𝟙_ C) ⟶ (obj ⊗ obj)
  /-- Snake identity (left). -/
  pairing_snake_left :
    (ρ_ obj).inv ≫ (obj ◁ coevaluation) ≫ (α_ obj obj obj).inv ≫
      ((mul ≫ frobeniusForm) ▷ obj) ≫ (λ_ obj).hom = 𝟙 obj
  /-- Snake identity (right). -/
  pairing_snake_right :
    (λ_ obj).inv ≫ (coevaluation ▷ obj) ≫ (α_ obj obj obj).hom ≫
      (obj ◁ (mul ≫ frobeniusForm)) ≫ (ρ_ obj).hom = 𝟙 obj
  /-- Frobenius relation. -/
  frobenius_relation :
    mul ≫ comul = (comul ▷ obj) ≫ (α_ obj obj obj).hom ≫ (obj ◁ mul)

namespace FrobeniusHopfDataPreAxiom

/-! ### The three unconstrained fields -/

/-- Replace the antipode by an arbitrary endomorphism.  Every law is
    discharged by the *same* proof as in `F`, because no law mentions
    `antipode`. -/
def withAntipode (F : FrobeniusHopfDataPreAxiom C) (g : F.obj ⟶ F.obj) :
    FrobeniusHopfDataPreAxiom C :=
  { F with antipode := g }

/-- Replace the unit by an arbitrary morphism `𝟙 ⟶ A`. -/
def withUnit (F : FrobeniusHopfDataPreAxiom C) (g : (𝟙_ C) ⟶ F.obj) :
    FrobeniusHopfDataPreAxiom C :=
  { F with unit := g }

/-- Replace the counit by an arbitrary morphism `A ⟶ 𝟙`. -/
def withCounit (F : FrobeniusHopfDataPreAxiom C) (g : F.obj ⟶ (𝟙_ C)) :
    FrobeniusHopfDataPreAxiom C :=
  { F with counit := g }

@[simp] theorem withAntipode_obj (F : FrobeniusHopfDataPreAxiom C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).obj = F.obj := Eq.refl _

@[simp] theorem withAntipode_antipode (F : FrobeniusHopfDataPreAxiom C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).antipode = g := Eq.refl _

@[simp] theorem withAntipode_mul (F : FrobeniusHopfDataPreAxiom C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).mul = F.mul := Eq.refl _

@[simp] theorem withAntipode_comul (F : FrobeniusHopfDataPreAxiom C)
    (g : F.obj ⟶ F.obj) : (F.withAntipode g).comul = F.comul := Eq.refl _

@[simp] theorem withUnit_unit (F : FrobeniusHopfDataPreAxiom C)
    (g : (𝟙_ C) ⟶ F.obj) : (F.withUnit g).unit = g := Eq.refl _

@[simp] theorem withCounit_counit (F : FrobeniusHopfDataPreAxiom C)
    (g : F.obj ⟶ (𝟙_ C)) : (F.withCounit g).counit = g := Eq.refl _

/-! ### Independence -/

/-- **The antipode was unconstrained.**  If a property `P` of antipodes was
    provable for every such structure, then it held of *every* endomorphism of
    *every* one of them.

    Contrapositive, which is how this is read: to show a property of `S` was
    **not** derivable, it sufficed to exhibit one object with one endomorphism
    lacking it. -/
theorem antipode_property_vacuous
    (P : ∀ F : FrobeniusHopfDataPreAxiom C, (F.obj ⟶ F.obj) → Prop)
    (hP : ∀ F : FrobeniusHopfDataPreAxiom C, P F F.antipode)
    (F : FrobeniusHopfDataPreAxiom C) (g : F.obj ⟶ F.obj) :
    P (F.withAntipode g) g :=
  hP (F.withAntipode g)

/-- The same for the unit. -/
theorem unit_property_vacuous
    (P : ∀ F : FrobeniusHopfDataPreAxiom C, ((𝟙_ C) ⟶ F.obj) → Prop)
    (hP : ∀ F : FrobeniusHopfDataPreAxiom C, P F F.unit)
    (F : FrobeniusHopfDataPreAxiom C) (g : (𝟙_ C) ⟶ F.obj) :
    P (F.withUnit g) g :=
  hP (F.withUnit g)

/-- The same for the counit. -/
theorem counit_property_vacuous
    (P : ∀ F : FrobeniusHopfDataPreAxiom C, (F.obj ⟶ (𝟙_ C)) → Prop)
    (hP : ∀ F : FrobeniusHopfDataPreAxiom C, P F F.counit)
    (F : FrobeniusHopfDataPreAxiom C) (g : F.obj ⟶ (𝟙_ C)) :
    P (F.withCounit g) g :=
  hP (F.withCounit g)

/-- Had `S ≫ S = 𝟙` been derivable from the pre-axiom laws, **every**
    endomorphism of **every** such object would have been an involution. -/
theorem involutive_of_sq_eq_id
    (h : ∀ F : FrobeniusHopfDataPreAxiom C,
      F.antipode ≫ F.antipode = CategoryTheory.CategoryStruct.id F.obj)
    (F : FrobeniusHopfDataPreAxiom C) (g : F.obj ⟶ F.obj) :
    g ≫ g = CategoryTheory.CategoryStruct.id F.obj :=
  h (F.withAntipode g)

end FrobeniusHopfDataPreAxiom

/-! ### The cost of assuming `S² = id` under the pre-axiom reading

These two are pure category theory and remain true statements; note their
hypothesis quantifies over *every* object, which is what the old free-data
regime made cheap to satisfy and the current one does not. -/

omit [CategoryTheory.MonoidalCategory C] in
/-- A monoid in which every element squares to the identity is commutative,
    stated for the endomorphism monoid of an object of a category. -/
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

/-- **The cost, part one.**  Under the pre-axiom reading, `S ≫ S = 𝟙` as a
    theorem would have made every such endomorphism monoid commutative. -/
theorem endo_comm_of_antipode_sq_eq_id
    (h : ∀ F : FrobeniusHopfDataPreAxiom C,
      F.antipode ≫ F.antipode = CategoryTheory.CategoryStruct.id F.obj)
    (F : FrobeniusHopfDataPreAxiom C) (a b : F.obj ⟶ F.obj) : a ≫ b = b ≫ a :=
  endo_comm_of_sq_involutive
    (fun g => FrobeniusHopfDataPreAxiom.involutive_of_sq_eq_id h F g) a b

/-- **The cost, part two.**  With zero morphisms available, `S ≫ S = 𝟙` as a
    theorem would have forced `𝟙_A = 0` — every such object a zero object.
    Take `g = 0`: `0 ≫ 0 = 0`, so `0 = 𝟙`.

    🛑 **Scope.**  This argument substitutes `0` for the antipode and therefore
    needs `antipode` to be *free data*.  It applies to
    `FrobeniusHopfDataPreAxiom` and **not** to the current
    `QOU.FrobeniusHopfData`, whose antipode is determined
    (`QOU.FrobeniusHopfData.antipode_unique`) and so cannot be chosen. -/
theorem id_eq_zero_of_antipode_sq_eq_id
    [CategoryTheory.Limits.HasZeroMorphisms C]
    (h : ∀ F : FrobeniusHopfDataPreAxiom C,
      F.antipode ≫ F.antipode = CategoryTheory.CategoryStruct.id F.obj)
    (F : FrobeniusHopfDataPreAxiom C) :
    (0 : F.obj ⟶ F.obj) = CategoryTheory.CategoryStruct.id F.obj := by
  have := FrobeniusHopfDataPreAxiom.involutive_of_sq_eq_id h F 0
  rwa [CategoryTheory.Limits.zero_comp] at this

/-! ### Independence of `unit`, `counit`, and `frobeniusForm` in the 6-law package (`qou-k4zx`)

Bean `qou-k4zx` records two questions that the monomial-map group-algebra probe
(`frobenius_hopf_axiom_independence_probe.py`) could not separate:

1. **Why `antipode_unit` (`S(1) = 1`) is not redundant in general:** on a group
   algebra `k[G]` a monomial map `S` sends `1` to a basis group element, where
   being idempotent forces `S(1) = 1`. In a general algebra with a non-trivial
   idempotent `e ≠ 1` (such as `ℚ × ℚ` with `e = (1, 0)`), the projection
   `S(x, y) = (x, 0)` is an anti-multiplicative involution (`S(ab) = S(b)S(a)`)
   whose image of the unit `(1, 1)` is `(1, 0) ≠ (1, 1)`.
2. **Why `antipode_counit` (`ε ∘ S = ε`) and `antipode_frobeniusForm` (`λ ∘ S = λ`)
   are independent once `λ ≠ ε`:** on `k[G]` the counit and Frobenius form
   coincide (`λ = ε`), so each forces the other. On `ℚ × ℚ` with the factor-swap
   involution `S(x, y) = (y, x)` (which is an algebra/coalgebra anti-automorphism
   fixing `(1, 1)` and squaring to `id`), choosing a symmetric counit
   `ε(x, y) = x + y` and a non-degenerate asymmetric Frobenius form
   `λ(x, y) = x + 2y` satisfies `ε ∘ S = ε` while violating `λ ∘ S = λ`
   (and dually when `ε` and `λ` are exchanged). -/

/-- The idempotent projection `S(x, y) = (x, 0)` on `ℚ × ℚ`. -/
def idempotentProjAntipode (p : ℚ × ℚ) : ℚ × ℚ := (p.1, 0)

/-- **`idempotentProjAntipode` is anti-multiplicative (`S(ab) = S(b)S(a)`),
    yet violates `S(1) = 1` (`qou-k4zx`).** -/
theorem idempotentProjAntipode_anti_mul_not_unit :
    (∀ a b : ℚ × ℚ,
      idempotentProjAntipode (a.1 * b.1, a.2 * b.2) =
        ((idempotentProjAntipode b).1 * (idempotentProjAntipode a).1,
         (idempotentProjAntipode b).2 * (idempotentProjAntipode a).2)) ∧
    idempotentProjAntipode (1, 1) ≠ (1, 1) := by
  refine ⟨fun a b => ?_, ?_⟩
  · ext <;> simp [idempotentProjAntipode, mul_comm]
  · intro h
    have h2 : (0 : ℚ) = 1 := congrArg Prod.snd h
    norm_num at h2

/-- The factor-swap involution `S(x, y) = (y, x)` on `ℚ × ℚ`. -/
def swapAntipode (p : ℚ × ℚ) : ℚ × ℚ := (p.2, p.1)

/-- Symmetric linear functional `(x, y) ↦ x + y` on `ℚ × ℚ`. -/
def symLinearForm (p : ℚ × ℚ) : ℚ := p.1 + p.2

/-- Non-degenerate asymmetric linear functional `(x, y) ↦ x + 2y` on `ℚ × ℚ`. -/
def asymLinearForm (p : ℚ × ℚ) : ℚ := p.1 + 2 * p.2

/-- **Invariance of the pairing functional `λ` is independent of `antipode_counit`,
    `antipode_anti_mul`, `antipode_unit`, and `antipode_involutive` when `λ ≠ ε` (`qou-k4zx`).** -/
theorem pairingForm_independent_of_counit :
    (∀ a b : ℚ × ℚ,
      swapAntipode (a.1 * b.1, a.2 * b.2) =
        ((swapAntipode b).1 * (swapAntipode a).1,
         (swapAntipode b).2 * (swapAntipode a).2)) ∧
    swapAntipode (1, 1) = (1, 1) ∧
    (∀ a : ℚ × ℚ, swapAntipode (swapAntipode a) = a) ∧
    (∀ a : ℚ × ℚ, symLinearForm (swapAntipode a) = symLinearForm a) ∧
    ¬ (∀ a : ℚ × ℚ, asymLinearForm (swapAntipode a) = asymLinearForm a) := by
  refine ⟨fun a b => ?_, rfl, fun a => ?_, fun a => ?_, ?_⟩
  · ext <;> simp [swapAntipode, mul_comm]
  · ext <;> rfl
  · simp [swapAntipode, symLinearForm, add_comm]
  · intro h
    have h10 := h (1, 0)
    norm_num [swapAntipode, asymLinearForm] at h10

/-- **Dually, `antipode_counit` is independent of the pairing-functional invariance law (`qou-k4zx`).** -/
theorem counit_independent_of_pairingForm :
    (∀ a : ℚ × ℚ, symLinearForm (swapAntipode a) = symLinearForm a) ∧
    asymLinearForm (swapAntipode (1, 0)) ≠ asymLinearForm (1, 0) := by
  constructor
  · intro a
    change a.2 + a.1 = a.1 + a.2
    exact add_comm a.2 a.1
  · intro h
    norm_num [swapAntipode, asymLinearForm] at h

end QOU.AntipodeIndependence
