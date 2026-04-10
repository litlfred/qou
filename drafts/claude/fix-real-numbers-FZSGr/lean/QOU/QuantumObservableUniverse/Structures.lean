import QOU.QuantumObservableUniverse.CategoricalFoundations
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.Tactic.Positivity

/-!
# §1⅓–§1½  Higher Forms, Involutive Structures, Abstract Hodge Theory

Auxiliary categorical structures used throughout the QOU:
higher differential forms, involutive (†-) structures,
positive-definite structures, Hodge involutions, and spin labels.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-! ## §1⅓  Higher Forms, Involutive and Positive-Definite Structures -/

/-- **Higher differential forms** `Ωᵏ(A) = ⋀ᵏ_A Ω¹(A)`.

    The graded `A`-bimodule of exterior powers of Kähler differentials,
    with `Ω⁰(A) = A` and `d : Ωᵏ → Ωᵏ⁺¹` satisfying `d² = 0`.

    LaTeX: `\label{def:higher-forms}` -/
structure HigherForms (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The underlying Frobenius–Hopf object `A`. -/
  frobHopf : @FrobeniusHopfData C _ _
  /-- The degree-`k` form object `Ωᵏ(A)` in `C`. -/
  formObj : ℕ → C
  /-- `Ω⁰(A) = A`. -/
  degree_zero : formObj 0 = frobHopf.obj
  /-- The differential `d : Ωᵏ(A) → Ωᵏ⁺¹(A)`. -/
  d : (k : ℕ) → formObj k ⟶ formObj (k + 1)

/-- **Involutive structure** (†-structure / *-structure) on a monoidal category.

    A contravariant endofunctor `† : C^op → C` that is the identity on objects,
    satisfies `f†† = f`, and is compatible with the monoidal structure.

    LaTeX: `\label{def:involutive-structure}` -/
structure InvolutiveStructure (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The involution on morphisms: `f† : Y ⟶ X` for `f : X ⟶ Y`. -/
  dagger : ∀ {X Y : C}, (X ⟶ Y) → (Y ⟶ X)
  /-- Involutivity: `f†† = f`. -/
  dagger_dagger : ∀ {X Y : C} (f : X ⟶ Y), dagger (dagger f) = f
  /-- Contravariance: `(g ∘ f)† = f† ∘ g†`. -/
  dagger_comp : ∀ {X Y Z : C} (f : X ⟶ Y) (g : Y ⟶ Z),
    dagger (f ≫ g) = dagger g ≫ dagger f
  /-- Identity: `id† = id`. -/
  dagger_id : ∀ (X : C), dagger (𝟙 X) = 𝟙 X

/-- `f†† = f` is the defining involutivity property. -/
theorem InvolutiveStructure.involutivity {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    (inv : InvolutiveStructure C) {X Y : C} (f : X ⟶ Y) :
    inv.dagger (inv.dagger f) = f :=
  inv.dagger_dagger f

/-- **Positive-definite structure** on an involutive monoidal category.

    The involution is positive-definite if for every non-zero
    `f : 𝟙 → X`, the composite `f ≫ f† : 𝟙 → 𝟙` is positive
    in `End(𝟙) ≅ R`.

    LaTeX: `\label{def:positive-definite-dagger}` -/
structure PositiveDefiniteStructure (C : Type u)
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    extends InvolutiveStructure C where
  /-- Positive-definiteness: for non-zero `f : 𝟙 → X`, `f ≫ f† ≠ 0`.
      (In an ℝ-linear category, this encodes positivity.) -/
  positive_definite : ∀ {X : C} (f : (𝟙_ C) ⟶ X),
    f ≠ 0 → f ≫ dagger f ≠ 0

/-! ## §1½  Abstract Hodge Theory -/

/-- An **involutive endomorphism** in a category, modeling the Hodge star
    operator `⋆`.  When `⋆² = id`, the eigenvalue decomposition
    `V = V⁺ ⊕ V⁻` (self-dual ⊕ anti-self-dual) follows from the spectral
    theory of involutions. -/
structure CatHodgeInvolution {C : Type u} [CategoryTheory.Category.{v} C]
    (X : C) where
  /-- The Hodge star operator `⋆ : X ⟶ X`. -/
  star : X ⟶ X
  /-- Involutivity: `⋆ ≫ ⋆ = id_X`. -/
  star_sq : star ≫ star = 𝟙 X

/-- A morphism `f : Y ⟶ X` is **self-dual** w.r.t. a categorical Hodge
    involution if `f ≫ ⋆ = f`, i.e. `f` lands in the `+1`-eigenspace. -/
def CatHodgeInvolution.IsSelfDual {C : Type u} [CategoryTheory.Category.{v} C]
    {X : C} (h : CatHodgeInvolution X) {Y : C} (f : Y ⟶ X) : Prop :=
  f ≫ h.star = f

/-- An **involution on a type** (concrete version for the ℂ realisation).
    Models the Hodge star acting pointwise on sections of a bundle. -/
structure HodgeInvolution (V : Type*) where
  /-- The Hodge star `⋆ : V → V`. -/
  star : V → V
  /-- Involutivity: `⋆(⋆(v)) = v` for all `v`. -/
  star_sq : ∀ v, star (star v) = v

/-- An element `v : V` is **self-dual** if `⋆(v) = v`. -/
def HodgeInvolution.IsSelfDual {V : Type*} (h : HodgeInvolution V)
    (v : V) : Prop :=
  h.star v = v

/-- An element `v : V` is **anti-self-dual** if `⋆(v) = -v`. -/
def HodgeInvolution.IsAntiSelfDual {V : Type*} [Neg V]
    (h : HodgeInvolution V) (v : V) : Prop :=
  h.star v = -v

/-- **Spin labels**: the simple objects of a quantum observable universe
    are indexed by half-integer spin labels `j ∈ {0, 1/2, 1, 3/2, ...}`,
    with `V_j` having categorical dimension `2j + 1`.

    LaTeX: `\label{def:spin-labels}` -/
structure SpinLabels where
  /-- The spin label `j`, represented as twice the spin (so `j = 0, 1, 2, 3, ...`
      corresponds to spin `0, 1/2, 1, 3/2, ...`). -/
  twice_j : ℕ
  /-- The categorical dimension of `V_j` is `2j + 1 = twice_j + 1`. -/
  cat_dim : ℕ := twice_j + 1

/-- The fundamental object has spin `1/2` and dimension `2`. -/
theorem SpinLabels.fundamental_dim : { twice_j := 1 : SpinLabels }.cat_dim = 2 := by rfl

/-- The adjoint object has spin `1` and dimension `3`. -/
theorem SpinLabels.adjoint_dim : { twice_j := 2 : SpinLabels }.cat_dim = 3 := by rfl

end QOU
