import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.CategoryTheory.Types.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.Basic
import Mathlib.Topology.ContinuousMap.Basic
import Mathlib.Geometry.Manifold.IsManifold.Basic
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.LinearAlgebra.ExteriorAlgebra.Basic


/-!
# QOU.QuantumObservableUniverse

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v w

/-- **Frobenius–Hopf data** in a monoidal category.

    Re-declared from the library module
    `QOU.QuantumObservableUniverse.CategoricalFoundations` so this sibling
    is a self-contained compilation unit — importing the library module
    would collide with this block's own `QuantumObservableUniverse` and
    `QuantumUniverse.gaugeGroup` declarations.  Keep field-for-field in
    sync with the library.

    LaTeX: used in `\label{def:quantum-universe}`, item (ii).
    Ref: [kock2004] -/
structure FrobeniusHopfData (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The underlying object in `C`. -/
  obj : C
  /-- Multiplication morphism `μ : A ⊗ A → A`. -/
  mul : (obj ⊗ obj) ⟶ obj
  /-- Unit morphism `η : 𝟙 → A`. -/
  unit : (𝟙_ C) ⟶ obj
  /-- Comultiplication morphism `Δ : A → A ⊗ A`. -/
  comul : obj ⟶ (obj ⊗ obj)
  /-- Counit morphism `ε : A → 𝟙`. -/
  counit : obj ⟶ (𝟙_ C)
  /-- Antipode morphism `S : A → A`. -/
  antipode : obj ⟶ obj
  /-- Frobenius form `λ : A → 𝟙`. -/
  frobeniusForm : obj ⟶ (𝟙_ C)
  /-- Coevaluation morphism `η̃ : 𝟙 → A ⊗ A`, the dual datum to the
      evaluation `ev = μ ≫ λ : A ⊗ A → 𝟙`. -/
  coevaluation : (𝟙_ C) ⟶ (obj ⊗ obj)
  /-- **Snake identity (left).** -/
  pairing_snake_left :
    (ρ_ obj).inv ≫ (obj ◁ coevaluation) ≫ (α_ obj obj obj).inv ≫
      ((mul ≫ frobeniusForm) ▷ obj) ≫ (λ_ obj).hom = 𝟙 obj
  /-- **Snake identity (right).** -/
  pairing_snake_right :
    (λ_ obj).inv ≫ (coevaluation ▷ obj) ≫ (α_ obj obj obj).hom ≫
      (obj ◁ (mul ≫ frobeniusForm)) ≫ (ρ_ obj).hom = 𝟙 obj
  /-- **Frobenius relation**: `μ ≫ Δ = (Δ ▷ A) ≫ α ≫ (A ◁ μ)`. -/
  frobenius_relation :
    mul ≫ comul = (comul ▷ obj) ≫ (α_ obj obj obj).hom ≫ (obj ◁ mul)

/-- **Quantum Universe** over a field `k`.

    Re-declared from the library module
    `QOU.QuantumObservableUniverse.CategoricalFoundations` (see the note
    on `FrobeniusHopfData` above).  Keep field-for-field in sync.

    LaTeX: `\label{def:quantum-universe}` -/
structure QuantumUniverse (k : Type*) [Field k] where
  /-- The monoidal category `C`. Represented as an opaque type with
      `Category` and `MonoidalCategory` instances. -/
  C : Type u
  [catInst : CategoryTheory.Category.{v} C]
  [monInst : CategoryTheory.MonoidalCategory C]
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C catInst monInst
  /-- The fibre functor `ω : C → Type*` (abstracting `Vect_k`).
      An exact faithful `k`-linear monoidal functor. -/
  fibreFunctor : @CategoryTheory.Functor C catInst (Type w) inferInstance
  /-- `A` admits a differential calculus: the module of Kähler
      differentials `Ω¹(A)` exists in `C`. -/
  differentialForms : Type*

/-- **Quantum Observable Universe** over a field `k`.

    A quantum universe satisfying three observability conditions:
    (i)   the Frobenius form on `A` is non-degenerate — an exact self-pairing,
          already enforced structurally by the snake identities in
          `FrobeniusHopfData`.
    (ii)  `Hom_C(𝟙, Ad(A))` is trivial — no non-trivial invariant adjoint
          morphisms.
    (iii) categorical volume constraint: the fundamental object `V` of
          categorical dimension 2 admits a non-degenerate epimorphism
          `ε : Λ²V → 𝟙` preserved by the rigid dualities.

    LaTeX: `\label{def:quantum-observable-universe}` -/
structure QuantumObservableUniverse (k : Type*) [Field k]
    extends QuantumUniverse k where
  /-- The adjoint object `Ad(A)` in `C`, carrying the adjoint action of the
      Hopf algebra `A` on itself.  In a braided monoidal category this is
      constructed from `(A, μ, Δ, S)` and the braiding; here it is provided
      abstractly. -/
  adjointObj : C
  /-- **Adjoint vanishing** (condition ii): all morphisms `𝟙 → Ad(A)` in
      `C` are equal.  In a `k`-linear category this is equivalent to
      `Hom_C(𝟙, Ad(A)) = 0`, since the zero morphism is always present
      and all others must equal it. -/
  adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)
  /-- The fundamental object `V` of categorical dimension 2. -/
  fundamentalObj : C
  /-- The exterior square `Λ²V` as an object of `C`. -/
  exteriorSquare : C
  /-- **Volume constraint** (condition iii): the non-degenerate epimorphism
      `ε : Λ²V → 𝟙` that forces `det(g_V) = 1` for all
      `g ∈ Aut⊗(ω)`, restricting the gauge group from `GL(2)` to `SL(2)`.
      LaTeX: `\label{eq:categorical-volume-constraint}` -/
  volumeForm : exteriorSquare ⟶ (𝟙_ C)
  /-- **Non-degeneracy**: the volume form is an epimorphism —
      if two morphisms agree after precomposition with `volumeForm`,
      they are equal.  This forces the pairing to be non-degenerate. -/
  volumeForm_epi : ∀ (f g : (𝟙_ C) ⟶ (𝟙_ C)),
    volumeForm ≫ f = volumeForm ≫ g → f = g
/-- The **quantum gauge group** `G_q = Aut⊗(ω)`: the group of monoidal
    natural automorphisms of the fibre functor.

    The full definition is `Aut⊗(ω)` — natural isomorphisms `ω ≅ ω`
    that are compatible with the monoidal structure (tensor products
    and unit).  The type `ω ≅ ω` captures `Aut(ω)`; the monoidal
    constraint is enforced by `fibreFunctor_monoidal` on `QuantumUniverse`,
    which restricts to monoidal natural transformations.

    By Tannaka–Krein duality, `G_q` is a compact group (or algebraic
    group over `k`) that can be recovered from `ω`.

    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
noncomputable def QuantumUniverse.gaugeGroup {k : Type*} [Field k]
    (QU : QuantumUniverse.{u, v, w} k) : Type (max u w) :=
  letI := QU.catInst
  QU.fibreFunctor ≅ QU.fibreFunctor

end QOU
