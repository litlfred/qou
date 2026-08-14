import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
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
# QOU.QuantumUniverse

Extracted from content/quantum-observable-universe/lean/ for content-block co-location.
Source: content/quantum-observable-universe/lean/QOU/QuantumUniverse.lean (monolithic)
-/

open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v w

/-- **Frobenius–Hopf data** in a monoidal category.

    An object `A` equipped with a Hopf algebra structure `(μ, η, Δ, ε, S)` and
    a Frobenius form `λ : A → 𝟙` such that the pairing `A ⊗ A → μ → A → λ → 𝟙`
    is non-degenerate and the Frobenius relation holds.

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
      evaluation `ev = μ ≫ λ : A ⊗ A → 𝟙`.  Together with `ev`, this
      exhibits `A` as self-dual in the monoidal category `C`. -/
  coevaluation : (𝟙_ C) ⟶ (obj ⊗ obj)
  /-- **Snake identity (left).**  The composite
      `A →[ρ⁻¹] A ⊗ 𝟙 →[A ◁ coev] A ⊗ (A ⊗ A) →[α⁻¹] (A ⊗ A) ⊗ A
       →[ev ▷ A] 𝟙 ⊗ A →[λ_] A`
      equals `id_A`, where `ev = μ ≫ λ`.  This is one half of the exact
      self-pairing making `A` self-dual. -/
  pairing_snake_left :
    (ρ_ obj).inv ≫ (obj ◁ coevaluation) ≫ (α_ obj obj obj).inv ≫
      ((mul ≫ frobeniusForm) ▷ obj) ≫ (λ_ obj).hom = 𝟙 obj
  /-- **Snake identity (right).**  The composite
      `A →[λ_⁻¹] 𝟙 ⊗ A →[coev ▷ A] (A ⊗ A) ⊗ A →[α] A ⊗ (A ⊗ A)
       →[A ◁ ev] A ⊗ 𝟙 →[ρ_] A`
      equals `id_A`. -/
  pairing_snake_right :
    (λ_ obj).inv ≫ (coevaluation ▷ obj) ≫ (α_ obj obj obj).hom ≫
      (obj ◁ (mul ≫ frobeniusForm)) ≫ (ρ_ obj).hom = 𝟙 obj
  /-- **Frobenius relation**: `μ ≫ Δ = (Δ ▷ A) ≫ α ≫ (A ◁ μ)`.
      Comultiplication is a bimodule map — the defining axiom of a
      Frobenius object in a monoidal category. -/
  frobenius_relation :
    mul ≫ comul = (comul ▷ obj) ≫ (α_ obj obj obj).hom ≫ (obj ◁ mul)

namespace FrobeniusHopfData

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C] (F : FrobeniusHopfData C)

/-- **Evaluation** `ev = μ ≫ ∫_A : A ⊗ A → 𝟙`.  Together with `coevaluation`
    and the two snake identities, this exhibits `A` as self-dual. -/
def ev : (F.obj ⊗ F.obj) ⟶ (𝟙_ C) := F.mul ≫ F.frobeniusForm

/-- **Left categorical trace** of `f : A → A`, obtained by closing the loop on
    the left: `𝟙 →[coev] A ⊗ A →[f ▷ A] A ⊗ A →[ev] 𝟙`. -/
def leftTrace (f : F.obj ⟶ F.obj) : (𝟙_ C) ⟶ (𝟙_ C) :=
  F.coevaluation ≫ (f ▷ F.obj) ≫ F.ev

/-- **Right categorical trace** of `f : A → A`, closing the loop on the right:
    `𝟙 →[coev] A ⊗ A →[A ◁ f] A ⊗ A →[ev] 𝟙`. -/
def rightTrace (f : F.obj ⟶ F.obj) : (𝟙_ C) ⟶ (𝟙_ C) :=
  F.coevaluation ≫ (F.obj ◁ f) ≫ F.ev

end FrobeniusHopfData

/-- **Quantum Universe** over a field `k`.

    A triple `(C, A, ω)` where `C` is a `k`-linear **braided** monoidal
    category, `A` is a Frobenius–Hopf object in `C`, and `ω` is a fibre
    functor.  The deformation parameter `q` is not part of the base
    definition; it enters via the substrate parameter
    (Definition 1.x, `SubstrateParameter`).

    **Rigidity is deliberately absent here.**  A quantum universe is
    braided but need not have duals; duals are imposed one level up, on
    `QuantumObservableUniverse`, where they carry the antiparticles and
    permit a strand to close into a knot.  Do not add a `RigidCategory`
    instance to this structure.

    LaTeX: `\label{def:quantum-universe}` -/
structure QuantumUniverse (k : Type*) [Field k] where
  /-- The monoidal category `C`. Represented as an opaque type with
      `Category` and `MonoidalCategory` instances. -/
  C : Type u
  [catInst : CategoryTheory.Category.{v} C]
  [monInst : CategoryTheory.MonoidalCategory C]
  /-- **Temporal braiding.**  The exchange of two adjacent systems is a
      process with a direction: `c_{V,W} : V ⊗ W ≅ W ⊗ V`, not required to
      be symmetric.  The hexagon identities are part of the class, and are
      what make an interaction independent of the order in which its
      pairwise crossings are written. -/
  [braidedInst : @CategoryTheory.BraidedCategory C catInst monInst]
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C catInst monInst
  /-- The fibre functor `ω : C → Type*` (abstracting `Vect_k`).
      An exact faithful `k`-linear monoidal functor. -/
  fibreFunctor : @CategoryTheory.Functor C catInst (Type w) inferInstance
  /-- **Faithfulness**: `ω` reflects equality of morphisms.
      If `ω.map f = ω.map g` then `f = g`. -/
  fibreFunctor_faithful : @CategoryTheory.Functor.Faithful C catInst (Type w) inferInstance
    fibreFunctor
  -- **Monoidality**: `ω` preserves the tensor product up to natural
  -- isomorphism.  Full `MonoidalFunctor` requires
  -- `Mathlib.CategoryTheory.Monoidal.Functor`; here we record the
  -- constraint as a Prop witness.
  /-- **Monoidality**: `ω(X ⊗ Y) ≅ ω(X) × ω(Y)` and `ω(𝟙) ≅ PUnit`.
      Encoded as: the image of the unit is inhabited. -/
  fibreFunctor_unit_inhabited : Nonempty (fibreFunctor.obj (𝟙_ C))
  /-- **Symmetric Frobenius** (axiom 3).  A closed loop has one amplitude:
      closing a worldline on the left and closing it on the right compute the
      same endomorphism of the unit.  Equivalently, the Frobenius form `∫_A`
      is symmetric and the Nakayama automorphism is trivial.

      This is a genuine restriction, not a consequence of axiom 2: a Frobenius
      algebra whose form is non-symmetric has `leftTrace ≠ rightTrace`, and
      then "the trace of a process" — hence any mass read off a trace — would
      depend on a drawing convention. -/
  frobenius_symmetric : ∀ f : frobHopf.obj ⟶ frobHopf.obj,
    frobHopf.leftTrace f = frobHopf.rightTrace f
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
      differentials `Ω¹(A)` exists as an object of `C`. -/
  differentialForms : C

end QOU
