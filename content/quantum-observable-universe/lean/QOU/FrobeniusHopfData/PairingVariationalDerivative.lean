import Mathlib.Tactic.Ring
import Mathlib.LinearAlgebra.BilinearMap
import Mathlib.CategoryTheory.Linear.Basic
import QOU.FrobeniusHopfData.FrobeniusPairingCategorical

/-!
# A rank-2 field space for a variational derivative

## The gap this file addresses

`QOU/MathlibExt/MonoidalCalcVar.lean` declares

```
class HasAction (R : Type*) (C : Type u) … where
  action : ((𝟙_ C) ⟶ (𝟙_ C)) → R
```

whose **domain is the scalars** `End(𝟙_C)`.  A variational derivative is an
object on the *field space* — the thing being varied — so an action whose field
space is the scalars has a scalar derivative, and nothing in the type of
`HasAction` mentions the objects being paired at all.  Downstream,
`ExternalCurrents.einsteinTensor` (`MonoidalCalcVar.lean:89`) and
`CategoricalVariationalData.einsteinTensor`
(`QOU/QuantumObservableUniverse/GaugeTheory.lean:127`) are both typed
`(𝟙_ C) ⟶ (𝟙_ C)`: they are scalars carrying a tensor's name.

## What this file supplies

The field space that was missing.  A `FrobeniusPairingData` carries
`eval : dual ⊗ obj ⟶ 𝟙_ C` — a pairing, which is the categorical shape of a
rank-2 object — and in a `Preadditive`, `R`-linear category the *set* of such
pairings, `dual ⊗ obj ⟶ 𝟙_ C`, is an `R`-module.  That module is a genuine
field space, and §1 develops the variational calculus on it.

* **§1** is generic linear algebra over `{R} [CommRing R]`: a quadratic action
  on a module, its variational derivative, the exact Taylor identity that
  *defines* that derivative, degree-2 homogeneity, the Euler contraction, and
  polarization.  No limits are needed — for a quadratic functional the Gateaux
  derivative is algebraic, so the categorical calculus of variations is
  available in this case without any axiom.  (`MonoidalCalcVar` states that a
  categorical calculus of variations "does not yet exist in Lean/Mathlib" and
  axiomatises the equations of motion on that ground; for a quadratic action
  that is not so.)
* **§2** instantiates §1 at the pairing field space and contracts back to the
  scalars, which is where the corpus's `einsteinTensor` slot lives.

## The relation between the rank-2 object and the corpus's scalar

`contract η T = η ≫ T` composes a rank-2 field `T : dual ⊗ obj ⟶ 𝟙_ C` with a
**co-pairing** `η : 𝟙_ C ⟶ dual ⊗ obj` (index raising) and lands in
`𝟙_ C ⟶ 𝟙_ C`.  So the corpus's scalar is the *trace* of a rank-2 object, and
`contract` is `R`-linear (`contract` is built as a `LinearMap`, whose
`map_add'`/`map_smul'` fields are the content).

`subsingleton_of_contract_reflects` is the structural statement of the defect:
**if a scalar equation of contractions implied the corresponding rank-2
equation, uniformly in the co-pairing, then the pairing field space would have
at most one element.**  The witness is the degenerate co-pairing `η = 0`, for
which every rank-2 field contracts to the same scalar.  So a scalar-only
Einstein-shaped equation is strictly weaker than the rank-2 identity it is
named after, in any `Preadditive` monoidal category with more than one pairing.

## What is NOT claimed

* No gravitational content.  No metric, no curvature, no stress-energy, no
  Newton constant, no `8π`, no numerical constant of any kind.  This file is
  about whether the categorical setting supports a rank-2 variational calculus
  — which is a question about types and modules, not about gravity.
* No general Euler-Lagrange machinery.  §1 covers **quadratic** actions.  A
  higher-degree or non-polynomial action needs a genuine limit and is not
  addressed.
* `contract` uses a co-pairing `η : 𝟙_ C ⟶ dual ⊗ obj`, whose handedness is the
  opposite of the `coev : 𝟙_ C ⟶ obj ⊗ dual` in
  `FrobeniusPairingData.Nondegenerate`.  In a braided or rigid setting the two
  are transported into each other; that transport is **not** asserted here, and
  `η` is taken as a datum.
* Nothing here is wired into `MonoidalCalcVar` or `GaugeTheory`; those two
  files are untouched.  Retyping `HasAction.action` is a separate change.

## Base ring (§7c)

Generic `{R : Type*} [CommRing R]` throughout.  The single `ℤ` occurrence is
the separating witness `value_does_not_determine_variation`, which needs a
concrete module to exhibit two fields with equal action and different
derivative; no `ℝ` and no archimedean tactic appears in this file.
-/

namespace QOU.Variational

universe v u

/-! ## §1  Quadratic actions on a field space -/

section FieldSpace

variable {R V : Type*} [CommRing R] [AddCommGroup V] [Module R V]

/-- A **quadratic action functional** on a field space `V`: a symmetric
    `R`-bilinear form.  The action of a field `e` is `form e e`.

    This is the shape `MonoidalCalcVar.HasAction` should have had: the domain of
    the functional is the field space, not the scalars. -/
structure QuadraticAction (R V : Type*) [CommRing R] [AddCommGroup V]
    [Module R V] where
  /-- The bilinear form whose diagonal is the action. -/
  form : V →ₗ[R] V →ₗ[R] R
  /-- The form is symmetric. -/
  form_symm : ∀ x y, form x y = form y x

namespace QuadraticAction

variable (Q : QuadraticAction R V)

/-- The action functional: a **scalar**, as an action should be. -/
def value (e : V) : R := Q.form e e

/-- The **variational derivative**, as a bilinear form on the field space.
    `Q.variation e : V →ₗ[R] R` is the derivative at the field `e`; `Q.variation`
    itself is rank-2 *because the field space is*, not by stipulation. -/
def variation : V →ₗ[R] V →ₗ[R] R := (2 : R) • Q.form

@[simp] lemma variation_apply (e δ : V) : Q.variation e δ = 2 * Q.form e δ := by
  simp [variation]

/-- **Exact Taylor identity.**  This is what makes `variation` *the* variational
    derivative rather than an arbitrary bilinear form: the first-order term of
    `value` at `e` in the direction `δ` is `variation e δ`, with the second-order
    remainder exactly `value δ`.  The identity fails for any other coefficient in
    `variation`, and its proof uses `form_symm`. -/
theorem value_add (e δ : V) :
    Q.value (e + δ) = Q.value e + Q.variation e δ + Q.value δ := by
  simp only [value, variation_apply, map_add, LinearMap.add_apply]
  rw [Q.form_symm δ e]
  ring

/-- **Degree-2 homogeneity.** -/
theorem value_smul (r : R) (e : V) : Q.value (r • e) = r ^ 2 * Q.value e := by
  simp only [value, map_smul, LinearMap.smul_apply, smul_eq_mul]
  ring

/-- **Euler contraction.**  Contracting the variational derivative at `e` with
    the field `e` itself returns the action, up to the degree factor `2`.  This
    is the sense in which a scalar is recovered from the rank-2 derivative — and
    the coefficient is what the statement asserts. -/
theorem euler (e : V) : Q.variation e e = 2 * Q.value e := by
  simp [value]

/-- **Polarization.**  The rank-2 derivative is recoverable from the action —
    but only from the action as a *function on the whole field space*, never
    from its value at a single field.  Compare
    `value_does_not_determine_variation`. -/
theorem polarization (e δ : V) :
    Q.variation e δ = Q.value (e + δ) - Q.value e - Q.value δ := by
  rw [Q.value_add e δ]; ring

/-! #### Existence constructors

A `structure` with no inhabitant leaves every downstream statement about it
vacuously satisfiable, so `QuadraticAction` gets an existence constructor before
anything is built on it. -/

/-- The quadratic action `e ↦ (ε e) ^ 2` attached to a linear functional `ε` on
    the field space.  This is the existence constructor: every field space
    carrying a functional carries an action.

    It is also the case that matters here.  `ε` is a **scalar** reading of a
    field, so this action is built entirely out of scalars — and
    `ofFunctional_variation` shows its variational derivative is a bilinear form
    on the field space all the same.  Rank-2-ness comes from *what is varied*,
    never from what the action's values are. -/
def ofFunctional (ε : V →ₗ[R] R) : QuadraticAction R V where
  form :=
    LinearMap.mk₂ R (fun x y => ε x * ε y)
      (fun x₁ x₂ y => by simp only [map_add]; ring)
      (fun c x y => by simp only [map_smul, smul_eq_mul]; ring)
      (fun x y₁ y₂ => by simp only [map_add]; ring)
      (fun c x y => by simp only [map_smul, smul_eq_mul]; ring)
  form_symm := fun x y => by simp only [LinearMap.mk₂_apply]; ring

@[simp] lemma ofFunctional_form (ε : V →ₗ[R] R) (x y : V) :
    (ofFunctional ε).form x y = ε x * ε y := rfl

/-- The action of `ofFunctional ε` is the square of the scalar reading. -/
theorem ofFunctional_value (ε : V →ₗ[R] R) (e : V) :
    (ofFunctional ε).value e = (ε e) ^ 2 := by
  simp only [value, ofFunctional_form]; ring

/-- **An action built entirely from a scalar reading still has a rank-2
    variational derivative.**  `ofFunctional ε` never sees a field except through
    the scalar `ε e`, yet its derivative is the bilinear form
    `(e, δ) ↦ 2 · ε e · ε δ` on the field space.  So the corpus's scalar-valued
    `einsteinTensor` slot is not defensible on the ground that "the action is a
    scalar anyway": the action is a scalar in *both* shapes, and only the domain
    decides the rank of the derivative. -/
theorem ofFunctional_variation (ε : V →ₗ[R] R) (e δ : V) :
    (ofFunctional ε).variation e δ = 2 * ε e * ε δ := by
  simp only [variation_apply, ofFunctional_form]; ring

/-- Non-vacuity: every field space carries at least the zero action. -/
instance : Inhabited (QuadraticAction R V) := ⟨ofFunctional 0⟩

end QuadraticAction

end FieldSpace

/-! ### A separating witness

One scalar value of the action does not determine the variational derivative.
This is the precise reason a single scalar — which is what
`ExternalCurrents.einsteinTensor` is — cannot stand in for a rank-2 object. -/

/-- Multiplication on `ℤ`, as a bilinear form.  Used only as a witness. -/
def intMulForm : ℤ →ₗ[ℤ] ℤ →ₗ[ℤ] ℤ :=
  LinearMap.mk₂ ℤ (· * ·)
    (fun a₁ a₂ b => add_mul a₁ a₂ b)
    (fun c a b => by simp [mul_assoc])
    (fun a b₁ b₂ => mul_add a b₁ b₂)
    (fun c a b => by simp [mul_left_comm])

/-- **The value of the action does not determine its variational derivative.**
    Two fields with the same action have different derivatives, so no single
    scalar can carry the rank-2 content. -/
theorem value_does_not_determine_variation :
    ∃ (Q : QuadraticAction ℤ ℤ) (e₁ e₂ : ℤ),
      Q.value e₁ = Q.value e₂ ∧ Q.variation e₁ ≠ Q.variation e₂ := by
  refine ⟨⟨intMulForm, fun x y => by simp [intMulForm, mul_comm]⟩, 1, -1, ?_, ?_⟩
  · simp [QuadraticAction.value, intMulForm]
  · intro h
    have h1 := DFunLike.congr_fun h (1 : ℤ)
    simp [QuadraticAction.variation_apply, intMulForm] at h1

/-! ## §2  The pairing field space -/

section Categorical

open CategoryTheory MonoidalCategory QOU.FrobeniusHopfData

variable {R : Type*} [CommRing R]
variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
  [Linear R C]
variable (d : FrobeniusPairingData C)

/-- The **field space** of a Frobenius pairing datum: every pairing on the same
    `(dual, obj)` pair.  `Preadditive` makes it an additive group and
    `Linear R C` makes it an `R`-module, so `QuadraticAction` applies to it
    directly. -/
abbrev fieldSpace : Type v := d.dual ⊗ d.obj ⟶ 𝟙_ C

/-- The shape this file supplies: a quadratic action whose field space is the
    space of **pairings**.  Its `QuadraticAction.variation` is a bilinear form on
    pairings — a rank-2 object. -/
abbrev PairingFieldAction := QuadraticAction R (fieldSpace d)

/-- The shape `MonoidalCalcVar.HasAction` has: a functional on the **scalars**.
    Its `QuadraticAction.variation` is a bilinear form on `End(𝟙_C)`, and no
    choice of such an action can produce a functional on pairings, because
    neither `obj` nor `dual` occurs in its type. -/
abbrev ScalarFieldAction := QuadraticAction R (𝟙_ C ⟶ 𝟙_ C)

/-- **Contraction** of a rank-2 pairing field against a co-pairing
    `η : 𝟙_ C ⟶ dual ⊗ obj`, landing in the scalars `End(𝟙_C)` — which is where
    the corpus's `einsteinTensor` slot lives.  `R`-linearity is the content: the
    `map_add'` and `map_smul'` fields are what make this a trace rather than an
    arbitrary function. -/
def contract (η : 𝟙_ C ⟶ d.dual ⊗ d.obj) :
    fieldSpace d →ₗ[R] (𝟙_ C ⟶ 𝟙_ C) where
  toFun T := η ≫ T
  map_add' := by intro T T'; simp
  map_smul' := by intro r T; simp

/-- Definitional unfolding, recorded for `simp`.  Not a mathematical claim. -/
@[simp] lemma contract_apply (η : 𝟙_ C ⟶ d.dual ⊗ d.obj) (T : fieldSpace d) :
    contract (R := R) d η T = η ≫ T := rfl

/-- **The scalar equation is the rank-2 equation modulo the kernel of the
    contraction.**  This is exactly what the corpus's scalar Einstein slot can
    express, and exactly what it loses. -/
theorem contract_eq_iff (η : 𝟙_ C ⟶ d.dual ⊗ d.obj) (G T : fieldSpace d) :
    contract (R := R) d η G = contract (R := R) d η T
      ↔ G - T ∈ LinearMap.ker (contract (R := R) d η) := by
  rw [LinearMap.mem_ker, map_sub, sub_eq_zero]

/-- **A scalar contraction cannot state a rank-2 identity.**  If equality of
    contractions implied equality of the rank-2 fields, uniformly in the
    co-pairing, then there would be at most one pairing `dual ⊗ obj ⟶ 𝟙_ C`.

    The invariant is `zero_comp`: the degenerate co-pairing `η = 0` contracts
    every rank-2 field to the same scalar, so it separates nothing.  Hence in any
    `Preadditive` monoidal category whose pairing space has two distinct
    elements, a scalar-valued Einstein-shaped equation is **strictly weaker**
    than the rank-2 identity it is named after. -/
theorem subsingleton_of_contract_reflects
    (h : ∀ (η : 𝟙_ C ⟶ d.dual ⊗ d.obj) (G T : fieldSpace d),
        contract (R := R) d η G = contract (R := R) d η T → G = T) :
    Subsingleton (fieldSpace d) :=
  ⟨fun G T => h 0 G T (by simp)⟩

/-- Contrapositive form: two distinct rank-2 fields that a contraction cannot
    tell apart. -/
theorem exists_contract_not_reflecting (G T : fieldSpace d) (hGT : G ≠ T) :
    ∃ η : 𝟙_ C ⟶ d.dual ⊗ d.obj,
      contract (R := R) d η G = contract (R := R) d η T ∧ G ≠ T :=
  ⟨0, by simp, hGT⟩

/-- **Existence constructor for `PairingFieldAction`**, built only from
    ingredients the corpus already has: contract a rank-2 pairing field against a
    co-pairing `η`, read the resulting scalar with `ε`, and square it.

    This is the wiring the corpus's `HasAction` could not carry.  `HasAction`
    has no instance anywhere, and could not usefully have one: its domain is
    `End(𝟙_C)`, so there is nothing to vary.  Here the same scalar data produces
    an action on the **pairings**, and `QuadraticAction.ofFunctional_variation`
    then gives it a rank-2 variational derivative. -/
def contractionAction (η : 𝟙_ C ⟶ d.dual ⊗ d.obj)
    (ε : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) : PairingFieldAction (R := R) d :=
  QuadraticAction.ofFunctional (ε.comp (contract (R := R) d η))

/-- The contraction action's value: the square of the scalar the corpus keeps. -/
theorem contractionAction_value (η : 𝟙_ C ⟶ d.dual ⊗ d.obj)
    (ε : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (T : fieldSpace d) :
    (contractionAction (R := R) d η ε).value T = (ε (η ≫ T)) ^ 2 := by
  simp only [contractionAction, QuadraticAction.ofFunctional_value,
    LinearMap.comp_apply, contract_apply]

/-- **The punchline, on the corpus's own ingredients.**  The action here is
    nothing but the corpus's scalar, squared — and its variational derivative is
    still a bilinear form on the rank-2 pairing field space.  Compare
    `ExternalCurrents.einsteinTensor`, which stores one value of `η ≫ T` and
    therefore cannot carry this. -/
theorem contractionAction_variation (η : 𝟙_ C ⟶ d.dual ⊗ d.obj)
    (ε : (𝟙_ C ⟶ 𝟙_ C) →ₗ[R] R) (T δ : fieldSpace d) :
    (contractionAction (R := R) d η ε).variation T δ
      = 2 * ε (η ≫ T) * ε (η ≫ δ) := by
  simp only [contractionAction, QuadraticAction.ofFunctional_variation,
    LinearMap.comp_apply, contract_apply]

end Categorical

end QOU.Variational
