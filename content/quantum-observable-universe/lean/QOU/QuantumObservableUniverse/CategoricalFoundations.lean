import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.Limits.Shapes.ZeroMorphisms
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fintype.Basic
import Mathlib.CategoryTheory.NatTrans
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.Real.Basic

/-!
# §1  Categorical Foundations

Core categorical structures for the Quantum Observable Universe:
`FrobeniusHopfData`, `QuantumUniverse`, `QuantumObservableUniverse`,
and the Tannaka–Krein gauge group.

LaTeX source: `chapters/quantum-observable-universe.tex`, §1.

## References

- [lusztig1993] G. Lusztig, *Introduction to Quantum Groups*, Birkhäuser 1993.
- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-! ## §1  Categorical Foundations -/

universe u v w

/-- The standard category structure on `Type w`, with morphisms as functions.
    Defined locally because `Mathlib.CategoryTheory.Types` does not exist
    at the pinned Mathlib commit (f897ebcf). -/
instance : CategoryTheory.Category.{w} (Type w) where
  Hom X Y := X → Y
  id _ := _root_.id
  comp f g := g ∘ f
  id_comp _ := rfl
  comp_id _ := rfl
  assoc _ _ _ := rfl

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

/-- **Quantum Universe** over a commutative ring `R`.

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
structure QuantumUniverse (R : Type*) [CommRing R] where
  /-- The monoidal category `C`. Represented as an opaque type with
      `Category` and `MonoidalCategory` instances. -/
  C : Type u
  [catInst : CategoryTheory.Category.{v} C]
  [monInst : CategoryTheory.MonoidalCategory C]
  /-- **Hom-sets are abelian groups.**  Carried because the paper's
      `R`-linearity (below) presupposes it, and because two axiom-4 fields
      need it: the zero morphism for block orthogonality, and a finite sum
      for block completeness.

      Note this REPLACES a bare `HasZeroMorphisms` field.  `Preadditive`
      supplies zero morphisms already, so carrying both would put two
      `HasZeroMorphisms` instances on `C` and make `p_b ≫ p_b' = 0`
      ambiguous. -/
  [preInst : @CategoryTheory.Preadditive C catInst]
  /-- **`C` is `R`-linear.**  Every hom-set is an `R`-module and composition
      is `R`-bilinear — verbatim `def:rigid-monoidal-category`, and what
      `def:quantum-universe` means by "an `R`-linear braided monoidal
      category".

      This is `CategoryTheory.Linear`, which takes `Preadditive` as a
      prerequisite; the two are a stack, not alternatives. -/
  [linInst : @CategoryTheory.Linear R _ C catInst preInst]
  /-- **Temporal braiding.**  The exchange of two adjacent systems is a
      process with a direction: `c_{V,W} : V ⊗ W ≅ W ⊗ V`, not required to
      be symmetric.  The hexagon identities are part of the class, and are
      what make an interaction independent of the order in which its
      pairwise crossings are written. -/
  [braidedInst : @CategoryTheory.BraidedCategory C catInst monInst]
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C catInst monInst
  /-- The fibre functor `τ : C → Type*` (abstracting `Vect_R` / `R-Mod`).
      The paper asks for it to be exact, faithful, `R`-linear and monoidal;
      NONE of those four is carried by this type, which is a bare functor to
      `Type`.  Recorded rather than silently implied — the gap is real and
      separate from the `R`-linearity of `C` now carried above. -/
  fibreFunctor : @CategoryTheory.Functor C catInst (Type*) inferInstance
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
  /-- **The ground ring is `End(𝟙_C)`.**  The block data below lands in `R`
      rather than in `End(𝟙_C)`, which presumes the two agree.  That is a
      genuine extra assumption, NOT a consequence of `R`-linearity:
      `Linear R C` supplies only a ring map `R → End(𝟙_C)`, `r ↦ r • 𝟙`,
      and its being bijective needs `𝟙` simple.  Carried explicitly so the
      assumption is visible instead of hiding in a docstring.

      Surfaced on the paper side in `def:quantum-universe`. -/
  unitEndEquiv : R ≃+* CategoryTheory.End (𝟙_ C)
  /-- **Wedderburn semisimplicity** (axiom 4).  The substrate has *channels*:
      `A` decomposes into finitely many blocks that do not mix, and no block
      is degenerate.

      Encoded here: a `Fintype` of blocks, an idempotent endomorphism of `A`
      per block, their mutual orthogonality, their completeness, and
      invertibility of each block's Frobenius weight and quantum dimension.

      **`blocks` indexes the NON-NEGLIGIBLE blocks, and vanishing elsewhere is
      permitted.**  `dimQ_isUnit` below is therefore a specification of what
      `blocks` ranges over, NOT a prohibition on the ambient category.  This
      matters at a root of unity (and in char p), where some `dim_q(λ)` really
      does vanish: those λ are *negligible* — they form a tensor ideal, the
      categorical trace kills anything factoring through them, and the standard
      construction quotients by that ideal (semisimplification) before reading
      off blocks.  Read as a prohibition, the field would exclude the
      root-of-unity categories outright; read as an index specification, it
      says the decomposition is that of the semisimplified quotient.

      The corpus already relies on this shape elsewhere: `y_(1^3) ≡ 0` in
      `h3-markov-wenzl-weights` (the Temperley-Lieb quotient kills the 3-row
      partition), and `tr_M = Σ_λ y_λ χ^λ` sums over all λ with zero weights on
      some.  That vanishing is a DIFFERENT mechanism from negligibility — a row
      cap at generic q, not a root-of-unity phenomenon — but it is the same
      pattern, and it is why no sum over blocks needs re-indexing here.

      Orthogonality needs a zero morphism and completeness needs a finite
      sum; both come from the `Preadditive` instance field above.

      `frobWeight` and `dimQ` land in `R` via `unitEndEquiv`, which is
      carried as a field rather than left to a docstring — see its comment
      for why `R`-linearity alone does not supply it (bean `qou-w1g8`).

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
  /-- **Blocks do not mix.**  Distinct central idempotents are orthogonal, so a
      state resolving into one channel has no component in another.  This is the
      half of semisimplicity that costs only a zero morphism. -/
  centralIdem_orthogonal : ∀ b b', b ≠ b' → centralIdem b ≫ centralIdem b' = 0
  /-- **The blocks span.**  `Σ_λ p_λ = 𝟙_A`: every state resolves into the
      channels, with nothing left over.  Together with orthogonality this is
      what "Wedderburn decomposition" means; without it the blocks could sit
      inside `A` without exhausting it.

      This is the field the axiom's NAME promised and its TYPE did not
      deliver.  It needs the finite sum that `Preadditive` supplies. -/
  centralIdem_complete : ∑ b, centralIdem b = 𝟙 frobHopf.obj
  /-- The Frobenius weight `∫_A p_λ` of each block. -/
  frobWeight : blocks → R
  /-- Every block's Frobenius weight is a **unit**: none is invisible to the
      trace.  `IsUnit`, not `≠ 0` — the paper says "invertible in `R`", and
      over a ring those differ (`2 ≠ 0` in `ℤ`, and `2` is not a unit).  The
      two coincide only over a field, which is why `≠ 0` survived while the
      base ring was one. -/
  frobWeight_isUnit : ∀ b, IsUnit (frobWeight b)
  /-- The quantum dimension `dim_q(λ)` of each block. -/
  dimQ : blocks → R
  /-- Every block's quantum dimension is a **unit**: each can be normalised
      against.  `IsUnit` for the same reason as `frobWeight_isUnit`. -/
  dimQ_isUnit : ∀ b, IsUnit (dimQ b)
  /-- `A` admits a differential calculus: the module of Kähler
      differentials `Ω¹(A)` exists in `C`.  Represented abstractly as a
      type (the carrier of `Ω¹(A)`). -/
  differentialForms : Type*

/-- **Quantum Observable Universe** over a commutative ring `R`.

    A quantum universe that is **rigid** and satisfies three observability
    conditions:
    (0)   rigidity: every object has a dual.  This is the antiparticle
          condition — a dual is a worldline read backwards, `ev` and `coev`
          are pair annihilation and creation — and it is what lets a strand
          bend back on itself, hence what lets a braid close into a knot.
          It is imposed here rather than on `QuantumUniverse`.
    (i)   the Frobenius form on `A` is non-degenerate — an exact self-pairing,
          already enforced structurally by the snake identities in
          `FrobeniusHopfData`.
    (ii)  `Hom_C(𝟙, Ad(A))` is trivial — no non-trivial invariant adjoint
          morphisms.
    (iii) categorical volume constraint: the fundamental object `V` of
          categorical dimension 2 admits a non-degenerate epimorphism
          `ε : Λ²V → 𝟙` preserved by the rigid dualities.

    LaTeX: `\label{def:quantum-observable-universe}` -/
structure QuantumObservableUniverse (R : Type*) [CommRing R]
    extends QuantumUniverse.{u, v} R where
  /-- **Rigidity** (condition 0): every object of `C` has left and right
      duals, with `ev`/`coev` satisfying the snake identities. -/
  [rigidInst : @CategoryTheory.RigidCategory C catInst monInst]
  /-- The adjoint object `Ad(A)` in `C`, carrying the adjoint action of the
      Hopf algebra `A` on itself.  In a braided monoidal category this is
      constructed from `(A, μ, Δ, S)` and the braiding; here it is provided
      abstractly. -/
  adjointObj : C
  /-- **Adjoint vanishing** (condition ii): all morphisms `𝟙 → Ad(A)` in
      `C` are equal.  In an `R`-linear category this is equivalent to
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

/-- The **quantum gauge group** `G_q = Aut⊗(ω)` reconstructed via
    Tannaka–Krein duality from the fibre functor.

    LaTeX: `\label{def:quantum-gauge-group}` (categorical version)
    Ref: [lusztig1993] -/
noncomputable def QuantumUniverse.gaugeGroup {R : Type*} [CommRing R]
    (QU : QuantumUniverse.{u, v} R) :=
  -- Aut⊗(ω) via Tannaka–Krein: the group of natural automorphisms of the
  -- fibre functor.  Full monoidal constraint (monoidal natural transformations)
  -- requires `Mathlib.CategoryTheory.Monoidal.NaturalTransformation`; here we
  -- capture the underlying natural-isomorphism type.
  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
  letI := QU.catInst
  QU.fibreFunctor ≅ QU.fibreFunctor

end QOU
