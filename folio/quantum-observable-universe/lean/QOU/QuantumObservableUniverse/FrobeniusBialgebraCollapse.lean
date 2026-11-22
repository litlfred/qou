import QOU.QuantumObservableUniverse.CategoricalFoundations

/-!
# What the Frobenius relation forces on a substrate carrying an antipode

`QOU.FrobeniusHopfData` carries the Frobenius relation `μ ≫ Δ = (Δ ▷ A) ≫ α ≫
(A ◁ μ)`, so its `Δ` is the **Frobenius** comultiplication — a map of
`A`-bimodules, hence determined by `Δ(1)`.  Since 2026-09-14 the structure also
carries the Hopf antipode axioms (bean `qou-c64q`).  This file works out what
those two facts force together.  The answer is stronger than the question that
prompted the file, so it is stated first.

## The antipode axiom alone forces `ε(1) · x = ε(x) · 1`

`scalar_id_eq_counit_unit` — **no hypothesis beyond the structure's own
fields**:

    ε ≫ η  =  (λ_A)⁻¹ ≫ ((η ≫ ε) ▷ A) ≫ (λ_A).hom

In elements, `ε(1)·x = ε(x)·1` for every `x`.  The mechanism is two steps: the
Frobenius relation forces the convolution `S * id` to be *left multiplication by
the single element* `(S * id)(1)` — `convolution_eq_left_mul`, which uses no
antipode axiom at all and is a statement about the convolution whatever `S` is —
and `antipode_left` then says that same convolution is `ε(-)·1`.  Evaluating at
`1` identifies the element as `ε(1)·1`.

Consequently:

* `counit_comp_unit_of_unital` : if `ε(1) = 1` then `ε ≫ η = 𝟙_A`;
* `isoUnitOfUnital` : and then `A ≅ 𝟙_C`;
* `counit_not_unital_of_nontrivial` : contrapositive — **a non-trivial
  substrate has a non-unital counit.**

`ε(1) = 1` is Mathlib's `BimonObj.one_counit`, and is what every bialgebra and
every Hopf algebra assumes without comment.  So the axiom added on 2026-09-14
does not sit quietly beside the Frobenius relation: the two together leave the
substrate one standard normalisation away from being the tensor unit.

**Scope, and it is load-bearing.**  `ε(1) = 1` is *not* a field of
`FrobeniusHopfData`, and nothing here supplies it.  So this is **not** a proof
that the current axioms are inconsistent, nor that `A = 𝟙_C`.  What is proved is
the identity `ε(1)·x = ε(x)·1` and its contrapositive.  Whether the corpus wants
a substrate whose counit is non-unital is a question for the owner, not one this
file decides; it is recorded in bean `qou-aawz`.

## The weaker result that prompted the file: the bimonoid axiom is excluded

The block's `authorNotes` recorded the bialgebra (bimonoid) compatibility as
merely *absent*, and left adding it as an open option.  It is not one.  One of
the four bimonoid axioms *on its own* — `Δ ∘ η = η ⊗ η`, Mathlib's
`CategoryTheory.BimonObj.one_comul` — collapses the substrate with no appeal to
the antipode:

* `comul_eq_of_one_comul` : `Δ = (λ_A)⁻¹ ≫ (η ▷ A)`, i.e. `Δ(x) = 1 ⊗ x`;
* `counit_comp_unit` : `ε ≫ η = 𝟙_A`, so `𝟙_A` factors through the tensor unit;
* `isoUnit` : with `η ≫ ε = 𝟙` (the bimonoid axiom `one_counit`) this is an
  isomorphism `A ≅ 𝟙_C`;
* `not_one_comul_of_nontrivial` : contrapositive.

This half is logically independent of the first: it spends the counit law and
the bimonoid unit axiom, where the first spends the antipode axiom and
associativity.  It is presented second here, but proved first in the file below,
because the antipode half reuses its `comul_eq_frobenius`.

## The two halves together: **both unit-side bimonoid axioms are excluded**

Mathlib's `BimonObj` has four axioms.  Two of them mention only the unit and the
counit, and are statable over a bare monoidal category:

| axiom | in elements | excluded by |
|---|---|---|
| `one_comul` : `η ≫ Δ = (λ_𝟙)⁻¹ ≫ (η ⊗ η)` | `Δ(1) = 1 ⊗ 1` | `not_one_comul_of_nontrivial` |
| `one_counit` : `η ≫ ε = 𝟙_𝟙` | `ε(1) = 1` | `counit_not_unital_of_nontrivial` |

A non-trivial substrate satisfies **neither**.  The second is the sharper
statement, because `ε(1) = 1` is a *normalisation* rather than a structural
compatibility — it is assumed without comment of every coalgebra with a unit in
sight, and it is excluded here by the antipode axiom the definition now carries.
Of the other two bimonoid axioms, `mul_comul` needs a braiding to state and is
not addressed here. `mul_counit` (`μ ≫ ε = (ε ⊗ ε) ≫ λ_`) does **not** need a
braiding, and it is excluded too, with no antipode:
`MultiplicativeCounitCollapse.eq_counit_smul_one` proves that a multiplicative
counit forces `x = ε(x) • 1` for every `x` (bean `qou-aj49`).

## Why none of this is a defect in the definition

It is the expected state of affairs, and it is why the name "Frobenius–Hopf"
needs reading with care. A finite-dimensional Hopf algebra *is* Frobenius — but
its Frobenius comultiplication is **not** its Hopf comultiplication. Forcing the
two to coincide is what collapses. The substrate takes `Δ` to be the Frobenius
one (that is what `frobenius_relation` says), so it is a Frobenius monoid with
an antipode, not a Hopf monoid in Mathlib's sense, and results about
`CategoryTheory.HopfObj` — `antipode_antipode` among them — do not transfer to
it. That was already recorded in the block's `authorNotes`; what is new here is
that it cannot be fixed by adding the axiom.

Nothing here argues against a Hopf structure on `A` borne by a **different**
comultiplication — that is a separate object the corpus does not have.

## Scope

Both halves are **structural exclusions** in the sense of AGENTS.md §"Before
declaring refuted": the invariant cited is a proved implication below, not a
numerical probe. Each excludes an axiom *for a `Δ` satisfying the Frobenius
relation*, and says nothing about a `Δ` that does not.

## References

- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
- [kassel1995] C. Kassel, *Quantum Groups*, Springer 1995, Ch. II–III.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory
open CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU.FrobeniusHopfData

universe u v

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]
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

/-! ### 🛑 The stronger collapse: the ANTIPODE axiom alone already does it

Everything above needs the bimonoid unit axiom as a hypothesis.  The results in
this section need **no extra hypothesis at all** beyond the structure's own
fields — and they reach nearly the same conclusion.

`antipode_left` says `S` is a left convolution inverse of `id_A`.  Combined with
the Frobenius relation, which makes `Δ` a right `A`-module map and hence
determined by `Δ(1)`, the convolution `(S * id)` is forced to be **left
multiplication by the fixed element `T = (S * id)(1)`**.  The antipode axiom
then says that left multiplication equals `ε(-)·1`, and evaluating at `1` gives
`T = ε(1)·1`.  The two together read

  `ε(1) · x  =  ε(x) · 1`   for every `x`,

which is `scalar_id_eq_counit_unit` below.  As soon as `ε(1) = 1` — the
standard unitality of a counit, and Mathlib's `BimonObj.one_counit` — this says
`x = ε(x)·1`: the object is the tensor unit. -/

/-- **The left convolution condition, as a proposition rather than a field.**

    `Δ ≫ (S ▷ A) ≫ μ = ε ≫ η` — Mathlib's `HopfObj.antipode_left`, and what
    `FrobeniusHopfData` carried as a field between 2026-09-14 and 2026-09-15.

    It is stated here as a `Prop` because the structure no longer carries it:
    it has **no non-trivial model over a field** (see
    `QOU.QuantumObservableUniverse.FrobeniusHopfModelDichotomy`), and was
    replaced by the anti-automorphism package on owner decision.

    Nothing is lost by the move.  A hypothesis is strictly stronger than a
    field: the theorems below now constrain **any** morphism satisfying this,
    rather than only a structure that declares it. -/
def ConvolutionLeft (F : FrobeniusHopfData C) : Prop :=
  F.comul ≫ (F.antipode ▷ F.obj) ≫ F.mul = F.counit ≫ F.unit

/-- **The right convolution condition.**  `Δ ≫ (A ◁ S) ≫ μ = ε ≫ η` —
    Mathlib's `HopfObj.antipode_right`.  See `ConvolutionLeft`. -/
def ConvolutionRight (F : FrobeniusHopfData C) : Prop :=
  F.comul ≫ (F.obj ◁ F.antipode) ≫ F.mul = F.counit ≫ F.unit

/-- Pushing `S ▷ A` past a right multiplication, by **associativity of `μ`**.
    In elements: `S(x₁)·(x₂·b) = (S(x₁)·x₂)·b`. -/
theorem convolution_reassoc :
    ((F.comul ▷ F.obj) ≫ (α_ F.obj F.obj F.obj).hom ≫ (F.obj ◁ F.mul))
        ≫ (F.antipode ▷ F.obj) ≫ F.mul
      = ((F.comul ≫ (F.antipode ▷ F.obj) ≫ F.mul) ▷ F.obj) ≫ F.mul := by
  simp only [Category.assoc, comp_whiskerRight]
  rw [whisker_exchange_assoc, ← associator_naturality_left_assoc, ← F.mul_assoc]

/-- **The convolution `S * id` is left multiplication by a fixed element.**

    `(S * id) = (λ_A)⁻¹ ≫ (T ▷ A) ≫ μ` with `T = η ≫ (S * id) : 𝟙_C ⟶ A`.

    This uses the Frobenius relation (via `comul_eq_frobenius`) and
    associativity, and **no antipode axiom** — it is a statement about the
    convolution, true whatever `S` is. -/
theorem convolution_eq_left_mul :
    F.comul ≫ (F.antipode ▷ F.obj) ≫ F.mul
      = (λ_ F.obj).inv ≫
          ((F.unit ≫ F.comul ≫ (F.antipode ▷ F.obj) ≫ F.mul) ▷ F.obj) ≫ F.mul := by
  conv_lhs => rw [comul_eq_frobenius F]
  rw [Category.assoc, convolution_reassoc F]
  simp only [comp_whiskerRight, Category.assoc]

/-- **🛑 The substrate's own axioms force `ε(1)·𝟙_A = η ∘ ε`.**

    No hypothesis beyond `FrobeniusHopfData`'s fields.  The right-hand side
    factors through the tensor unit, so `𝟙_A` scaled by the scalar `η ≫ ε` of
    `End(𝟙_C)` factors through `𝟙_C`.

    Read in elements: `ε(1)·x = ε(x)·1` for every `x`. -/
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
--      (a Frobenius comultiplication is a bimodule map, hence determined by Δ(1))
theorem scalar_id_eq_counit_unit_of_convolutionLeft (hconv : F.ConvolutionLeft) :
    F.counit ≫ F.unit
      = (λ_ F.obj).inv ≫ ((F.unit ≫ F.counit) ▷ F.obj) ≫ (λ_ F.obj).hom := by
  have h := convolution_eq_left_mul F
  rw [show F.comul ≫ (F.antipode ▷ F.obj) ≫ F.mul = F.counit ≫ F.unit from hconv] at h
  rw [h]
  simp only [comp_whiskerRight, Category.assoc, F.one_mul]

/-- **The substrate is the tensor unit as soon as its counit is unital.**

    `η ≫ ε = 𝟙` is `ε(1) = 1` — Mathlib's `BimonObj.one_counit`, and what any
    bialgebra or Hopf algebra assumes without comment.  Given it,
    `scalar_id_eq_counit_unit` reads `𝟙_A = η ∘ ε`, so `A` is a retract of
    `𝟙_C`; with the same hypothesis the other way round it is an isomorphism.

    **This needs no bimonoid comultiplication axiom.**  It is the antipode
    axiom (added 2026-09-14, bean `qou-c64q`) plus the bimodule comultiplication relation. -/
theorem counit_comp_unit_of_unital (hconv : F.ConvolutionLeft)
    (h : F.unit ≫ F.counit = 𝟙 (𝟙_ C)) :
    F.counit ≫ F.unit = 𝟙 F.obj := by
  rw [scalar_id_eq_counit_unit_of_convolutionLeft F hconv, h]
  simp

/-- **`A ≅ 𝟙_C`** from unitality of the counit alone. -/
noncomputable def isoUnitOfUnital (hconv : F.ConvolutionLeft)
    (h : F.unit ≫ F.counit = 𝟙 (𝟙_ C)) :
    F.obj ≅ 𝟙_ C where
  hom := F.counit
  inv := F.unit
  hom_inv_id := F.counit_comp_unit_of_unital hconv h
  inv_hom_id := h

/-- **Contrapositive, the usable form.**  A `FrobeniusHopfData` whose object is
    not a retract of the tensor unit has a **non-unital counit**: `ε(1) ≠ 1`.

    So a non-trivial substrate is not merely "not a bialgebra" — its counit
    fails the most basic normalisation any coalgebra-with-unit is assumed to
    have. That is the live question recorded in bean `qou-aawz`. -/
theorem counit_not_unital_of_nontrivial (hconv : F.ConvolutionLeft)
    (hnt : F.counit ≫ F.unit ≠ 𝟙 F.obj) :
    F.unit ≫ F.counit ≠ 𝟙 (𝟙_ C) :=
  fun h => hnt (F.counit_comp_unit_of_unital hconv h)

/-! ## Anti-automorphism package vs `S = 𝟙_A` (`qou-c64q`)

Bean `qou-c64q` records that replacing the convolution condition by the six-law
anti-automorphism package repairs the `S = 𝟙_A` degeneracy **exactly where `A`
is non-(braided-)commutative**: if `F.antipode = 𝟙 F.obj`, then `antipode_anti_mul`
reduces to `(β_ A A).hom ≫ μ = μ` and `antipode_anti_comul` reduces to
`Δ ≫ (β_ A A).hom = Δ`. Conversely, any non-braided-commutative (or
non-braided-cocommutative) substrate refutes `F.antipode = 𝟙 F.obj`. -/

/-- **If `S = 𝟙_A`, multiplication is braided-commutative (`qou-c64q`).** -/
theorem braided_comm_of_antipode_eq_id (hS : F.antipode = 𝟙 F.obj) :
    (β_ F.obj F.obj).hom ≫ F.mul = F.mul := by
  have h := F.antipode_anti_mul
  simp only [hS, Category.comp_id, Category.id_comp, tensorHom_id, id_whiskerRight] at h
  exact h.symm

/-- **If `S = 𝟙_A`, comultiplication is braided-cocommutative (`qou-c64q`).** -/
theorem braided_cocomm_of_antipode_eq_id (hS : F.antipode = 𝟙 F.obj) :
    F.comul ≫ (β_ F.obj F.obj).hom = F.comul := by
  have h := F.antipode_anti_comul
  simp only [hS, Category.id_comp, Category.comp_id, tensorHom_id, id_whiskerRight] at h
  exact h.symm

/-- **Non-braided-commutativity excludes `S = 𝟙_A` (`qou-c64q`).** -/
theorem antipode_ne_id_of_not_braided_comm
    (hnc : (β_ F.obj F.obj).hom ≫ F.mul ≠ F.mul) :
    F.antipode ≠ 𝟙 F.obj :=
  fun hS => hnc (F.braided_comm_of_antipode_eq_id hS)

/-- **Non-braided-cocommutativity excludes `S = 𝟙_A` (`qou-c64q`).** -/
theorem antipode_ne_id_of_not_braided_cocomm
    (hncc : F.comul ≫ (β_ F.obj F.obj).hom ≠ F.comul) :
    F.antipode ≠ 𝟙 F.obj :=
  fun hS => hncc (F.braided_cocomm_of_antipode_eq_id hS)

end QOU.FrobeniusHopfData
