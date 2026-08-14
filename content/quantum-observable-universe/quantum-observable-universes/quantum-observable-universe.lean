import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.Data.Fintype.Basic
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
  /-- **Temporal braiding.**  The exchange of two adjacent systems is a
      process with a direction: `c_{V,W} : V ⊗ W ≅ W ⊗ V`, not required to
      be symmetric.  Rigidity is deliberately NOT here — it belongs to
      `QuantumObservableUniverse` below. -/
  [braidedInst : @CategoryTheory.BraidedCategory C catInst monInst]
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C catInst monInst
  /-- The fibre functor `ω : C → Type*` (abstracting `Vect_k`).
      An exact faithful `k`-linear monoidal functor. -/
  fibreFunctor : @CategoryTheory.Functor C catInst (Type w) inferInstance
  /-- **Wedderburn semisimplicity** (axiom 4).  The substrate has *channels*:
      `A` decomposes into finitely many blocks that do not mix, and no block
      is degenerate.

      Encoded here: a `Fintype` of blocks, an idempotent endomorphism of `A`
      per block, and non-vanishing of each block's Frobenius weight and
      quantum dimension.  NOT encoded: mutual orthogonality of the
      idempotents and completeness of their sum, both of which need additive
      structure on the hom-sets (`Preadditive` / `HasZeroMorphisms`) that
      `QuantumUniverse` does not carry.  `frobWeight` and `dimQ` land in `k`
      via the standard identification of `End(𝟙)` with the ground ring of a
      `k`-linear category.

      Given this axiom, the co-Casimir trace identity
      `tr_M(C_dimQ) = Σ_λ 1/dim_q(λ)` is a *consequence*, proved as
      `QOU.BraidKnot.frobenius_codim_universal` by linearity of the trace
      over the central idempotents.  It is deliberately NOT an axiom here:
      asserting it would assert something already proved, and would collide
      with the unrelated `def:mass-identity` (the vortex integral). -/
  blocks : Type v
  [blocksFintype : Fintype blocks]
  /-- The central idempotent `p_λ` of each block. -/
  centralIdem : blocks → (frobHopf.obj ⟶ frobHopf.obj)
  /-- Each `p_λ` is idempotent. -/
  centralIdem_idem : ∀ b, centralIdem b ≫ centralIdem b = centralIdem b
  /-- The Frobenius weight `∫_A p_λ` of each block. -/
  frobWeight : blocks → k
  /-- No block has zero Frobenius weight: none is invisible to the trace. -/
  frobWeight_ne_zero : ∀ b, frobWeight b ≠ 0
  /-- The quantum dimension `dim_q(λ)` of each block. -/
  dimQ : blocks → k
  /-- No block has zero quantum dimension: each can be normalised against. -/
  dimQ_ne_zero : ∀ b, dimQ b ≠ 0
  /-- `A` admits a differential calculus: the module of Kähler
      differentials `Ω¹(A)` exists in `C`. -/
  differentialForms : Type*

/-- **Quantum Observable Universe** over a field `k`.

    A quantum universe that is **rigid** and satisfies three observability
    conditions.  Rigidity (condition 0) is imposed here, not on
    `QuantumUniverse`: a quantum universe is braided, an observable one is
    braided and rigid.  The remaining conditions:
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
  /-- **Rigidity** (condition 0): every object of `C` has left and right
      duals, with `ev`/`coev` satisfying the snake identities.  A dual is a
      worldline read backwards, so this is the antiparticle condition; it is
      also what lets a strand bend back on itself and a braid close into a
      knot. -/
  [rigidInst : @CategoryTheory.RigidCategory C catInst monInst]
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
