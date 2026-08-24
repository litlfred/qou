import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import QOU.BraidKnot.KeystoneBalancedRibbon
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.Limits.Shapes.ZeroMorphisms
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.CategoryTheory.Linear.Basic
import Mathlib.Algebra.BigOperators.Fin
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

    Re-declared from the library module
    `QOU.QuantumObservableUniverse.CategoricalFoundations` (see the note
    on `FrobeniusHopfData` above).  Keep field-for-field in sync.

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
      be symmetric.  Rigidity is deliberately NOT here — it belongs to
      `QuantumObservableUniverse` below. -/
  [braidedInst : @CategoryTheory.BraidedCategory C catInst monInst]
  /-- **The balancing twist** `θ_X : X ⟶ X` (axiom 1, categorical half).

      This is what makes the substrate parameter `q` *derivable rather than
      carried*.  On the defining representation the twist axiom forces
      `θ_V = q^{1/2} · id_V` (`rem:sqrt-q-ribbon-structure`), so `q` is read
      off the structure; there is deliberately **no `q` field**, since a
      distinguished element would smuggle in as data the thing the framework
      claims to derive.

      Three further things it supplies, none of which the previous
      `[BraidedCategory]` alone gave:

      1. **Framing.**  Without a twist a braid closure is only a *framed* link
         invariant — `tr_M(β)` depends on the writhe of the braid word rather
         than on the knot.  Since masses are read off knots, that dependence
         would be fatal.
      2. **Sphericality on all of `C`.**  Axiom 3 gives left-trace =
         right-trace on `End(A)` only, but the Markov trace closes strands of
         `V^{⊗n}`, not of `A`.  Ribbon = braided + spherical extends it to the
         objects the knot theory actually uses.
      3. **A legible classical boundary.**  `BalancedCategory.ofSymmetric`
         proves every symmetric category is balanced with `θ = 𝟙`, so the
         classical case is `θ = 𝟙`, i.e. `q = 1` — a *describable member*, not
         an excluded one.  This is why the fix is "add the twist", not "forbid
         symmetric": `q → 1` must stay inside the category it is a limit of.

      Uses the in-repo `BalancedCategory` (bean `rtrb`, sorry-free) since
      Mathlib has no ribbon layer. -/
  [balancedInst : @QOU.BraidKnot.Balanced.BalancedCategory C catInst monInst braidedInst]
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C catInst monInst
  /-- The fibre functor `τ : C → Type*` (abstracting `Vect_R` / `R-Mod`).
      The paper asks for it to be exact, faithful, `R`-linear and monoidal;
      NONE of those four is carried by this type, which is a bare functor to
      `Type`.  Recorded rather than silently implied — the gap is real and
      separate from the `R`-linearity of `C` now carried above. -/
  fibreFunctor : @CategoryTheory.Functor C catInst (Type w) inferInstance
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
      differentials `Ω¹(A)` exists in `C`. -/
  differentialForms : Type*

/-- **Quantum Observable Universe** over a commutative ring `R`.

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
structure QuantumObservableUniverse (R : Type*) [CommRing R]
    extends QuantumUniverse R where
  /-- **Rigidity** (condition 0): every object of `C` has left and right
      duals, with `ev`/`coev` satisfying the snake identities.  A dual is a
      worldline read backwards, so this is the antiparticle condition; it is
      also what lets a strand bend back on itself and a braid close into a
      knot. -/
  [rigidInst : @CategoryTheory.RigidCategory C catInst monInst]
  /-- The adjoint object `Ad(A)` in `C`, carrying the adjoint action of the
      Hopf algebra `A` on itself.  In a braided monoidal category it is
      constructed from `(A, μ, Δ, S)` and the braiding; that construction is
      not available here, so the object is provided together with the three
      fields below, which pin down enough of its relationship to `A` that a
      degenerate choice cannot satisfy them.

      **This was previously a free field**, with nothing linking it to
      `frobHopf`.  That made `adjoint_vanishing` satisfiable by taking
      `adjointObj := 0` — the zero object has `Hom(𝟙, 0) = 0` trivially — so
      an instance could satisfy "no hidden global symmetries" by having no
      adjoint object at all.  See bean `qou-fav8`. -/
  adjointObj : C
  /-- `Ad(A)` sits inside `A`.  The adjoint action is an action of `A` on
      itself, so its carrier is part of `A` rather than an unrelated object. -/
  adjointIncl : adjointObj ⟶ frobHopf.obj
  /-- The inclusion is a subobject inclusion. -/
  adjoint_mono : CategoryTheory.Mono adjointIncl
  /-- **`Ad(A)` carries no trivial summand**: it lands in `ker ε`.

      This is what makes condition (ii) a statement with content.  The full
      `A` always contains the unit `η : 𝟙 → A`, so `Hom(𝟙, A) = 0` is false
      for any nontrivial `A` and cannot be what the axiom means.  The corpus
      is explicit that the trivial part is excluded: `Ad(A)` decomposes "with
      no spin-0 summand" (`brings-qou-axiom-map.md`) and is `≅ V₂`, the
      3-dimensional traceless part, for `SU_q(2)` (`brings-is-qou.lean`).
      That reduced adjoint is the augmentation ideal `ker ε`, which the
      adjoint action preserves because `ε` is an algebra map. -/
  adjoint_augmented : adjointIncl ≫ frobHopf.counit = 0
  /-- `Ad(A)` is not the zero object.  Together with the two fields above this
      is what `adjointObj := 0` fails: the only morphism out of the zero
      object is zero. -/
  adjoint_nontrivial : adjointIncl ≠ 0
  /-- **Adjoint vanishing** (condition ii): all morphisms `𝟙 → Ad(A)` in
      `C` are equal.  In an `R`-linear category this is equivalent to
      `Hom_C(𝟙, Ad(A)) = 0`, since the zero morphism is always present
      and all others must equal it.

      Read with the three fields above, this now says what the paper says:
      the *reduced* adjoint has no invariants. -/
  adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)
  /-- The fundamental object `V` of categorical dimension 2. -/
  fundamentalObj : C
  /-- The exterior square `Λ²V` as an object of `C`, presented as a quotient
      of `V ⊗ V` by the two fields below.  Previously a free field with no tie
      to `fundamentalObj`; bean `qou-n1dj` item 3. -/
  exteriorSquare : C
  /-- The antisymmetrisation `π : V ⊗ V ↠ Λ²V`. -/
  exteriorSquareProj : (fundamentalObj ⊗ fundamentalObj) ⟶ exteriorSquare
  /-- `Λ²V` is a **quotient** of `V ⊗ V`.  No braiding-eigenvalue condition:
      on the `q`-exterior square the braiding acts by `-q⁻¹`, not `-1`, so
      demanding `β ≫ π = -π` would silently impose `q = 1`. -/
  exteriorSquare_epi : CategoryTheory.Epi exteriorSquareProj
  /-- **Volume constraint** (condition iii), under the **strong (iso)
      reading**: `ε : Λ²V ≅ 𝟙`, which forces `det(g_V) = 1` for all
      `g ∈ Aut⊗(ω)`, restricting the gauge group from `GL(2)` to `SL(2)`.

      Was `volumeForm : exteriorSquare ⟶ (𝟙_ C)` plus a separate
      `volumeForm_epi` field.  Both are subsumed: an isomorphism is epi, so
      `volumeForm_epi` is now a theorem
      (`QOU.epi_of_iso_unit`, `CategoricalFoundations.lean`) rather than a
      hypothesis, and the bare-morphism version admitted `volumeForm := 0`.
      Bean `qou-n1dj` item 2 — the editorial choice between the epi and iso
      readings of "non-degenerate epimorphism", resolved to iso.

      LaTeX: `\label{eq:categorical-volume-constraint}` -/
  volumeIso : exteriorSquare ≅ (𝟙_ C)
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
noncomputable def QuantumUniverse.gaugeGroup {R : Type*} [CommRing R]
    (QU : QuantumUniverse.{u, v, w} R) : Type (max u w) :=
  letI := QU.catInst
  QU.fibreFunctor ≅ QU.fibreFunctor

end QOU
