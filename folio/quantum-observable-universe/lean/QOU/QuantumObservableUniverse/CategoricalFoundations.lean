import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import QOU.BraidKnot.KeystoneBalancedRibbon
import Mathlib.CategoryTheory.Monoidal.Rigid.Basic
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.Limits.Shapes.ZeroMorphisms
import Mathlib.CategoryTheory.Limits.Shapes.Kernels
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
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] where
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
  /-- **Left unit law.**  `η ▷ A ≫ μ = λ_A`.  Axiom 1 of
      `def:frobenius-hopf-substrate` says `(μ, η)` make `A` an *associative
      unital* algebra object; this is half of "unital".

      Field shape matches `CategoryTheory.MonObj.one_mul` exactly, so
      `toMonObj` is a field-for-field transport. -/
  one_mul : unit ▷ obj ≫ mul = (λ_ obj).hom
  /-- **Right unit law.**  `A ◁ η ≫ μ = ρ_A`.  The other half of "unital". -/
  mul_one : obj ◁ unit ≫ mul = (ρ_ obj).hom
  /-- **Associativity.**  `(μ ▷ A) ≫ μ = α ≫ (A ◁ μ) ≫ μ` — the "associative"
      of axiom 1.  Matches `CategoryTheory.MonObj.mul_assoc`. -/
  mul_assoc : (mul ▷ obj) ≫ mul = (α_ obj obj obj).hom ≫ (obj ◁ mul) ≫ mul
  /-- **Left counit law.**  `Δ ≫ ε ▷ A = λ_A⁻¹`.  Axiom 2 says `(Δ, ε)` make
      `A` a *coassociative counital* coalgebra object; this is half of
      "counital".  Matches `CategoryTheory.ComonObj.counit_comul`. -/
  counit_comul : comul ≫ counit ▷ obj = (λ_ obj).inv
  /-- **Right counit law.**  `Δ ≫ A ◁ ε = ρ_A⁻¹`. -/
  comul_counit : comul ≫ obj ◁ counit = (ρ_ obj).inv
  /-- **Coassociativity.**  The "coassociative" of axiom 2.  Matches
      `CategoryTheory.ComonObj.comul_assoc`. -/
  comul_assoc :
    comul ≫ obj ◁ comul = comul ≫ (comul ▷ obj) ≫ (α_ obj obj obj).hom
  /-- **Antipode axiom 1 — `S` reverses multiplication.**
      `μ ≫ S = (S ⊗ S) ≫ β ≫ μ`, in elements `S(ab) = S(b)S(a)`.

      This is the braiding-carrying half of the antipode package and is why
      the structure now requires `[BraidedCategory C]`: "reverses" is not
      statable without a way to exchange the two tensor factors.  That is no
      new demand on the framework — `def:frobenius-hopf-substrate` already
      says the substrate is available at the level of a *quantum universe*,
      and `def:quantum-universe` is braided monoidal.

      **This axiom family REPLACED the convolution condition on 2026-09-15**
      (owner decision, beans `qou-c64q` / `qou-aawz`).  See the module
      docstring of `QOU.QuantumObservableUniverse.FrobeniusHopfModelDichotomy`
      for why: the convolution condition
      `Δ ≫ (S ▷ A) ≫ μ = ε ≫ η` — which is Mathlib's
      `HopfObj.antipode_left`, and which this structure carried from
      2026-09-14 to 2026-09-15 — has **no non-trivial model over a field**.
      It is not merely unsatisfied by the natural candidates; it forces
      `dim A ≤ 1`.

      The three theorems recording that are **not** deleted.  They are
      restated to take the convolution condition as an explicit hypothesis
      rather than to read it off a field, which is strictly stronger: they
      now constrain *any* morphism satisfying it, not only a structure that
      declares it. -/
  antipode_anti_mul :
    mul ≫ antipode =
      (antipode ⊗ₘ antipode) ≫ (CategoryTheory.BraidedCategory.braiding obj obj).hom ≫ mul
  /-- **Antipode axiom 2 — `S` reverses comultiplication.**
      `S ≫ Δ = Δ ≫ β ≫ (S ⊗ S)`, in elements
      `Δ(S x) = Σ S(x₂) ⊗ S(x₁)`. -/
  antipode_anti_comul :
    antipode ≫ comul =
      comul ≫ (CategoryTheory.BraidedCategory.braiding obj obj).hom ≫ (antipode ⊗ₘ antipode)
  /-- **Antipode axiom 3 — `S` fixes the unit.**  `η ≫ S = η`. -/
  antipode_unit : unit ≫ antipode = unit
  /-- **Antipode axiom 4 — `S` preserves the counit.**  `S ≫ ε = ε`. -/
  antipode_counit : antipode ≫ counit = counit
  /-- **Antipode axiom 5 — `S` is involutive.**  `S ≫ S = 𝟙_A`.

      On its own this pins nothing: `S = 𝟙_A` satisfies it, measured on
      `S₃` and `D₄` as well as on every abelian group tested
      (`computations/probes/frobenius_hopf_intermediate_axioms_probe.py`).
      It earns its place only alongside `antipode_anti_mul`, which `𝟙_A`
      fails whenever `A` is non-commutative. -/
  antipode_involutive : antipode ≫ antipode = 𝟙 obj
  /-- **Antipode axiom 6 — `S` preserves the Frobenius form.**
      `S ≫ λ = λ`, so the pairing `⟨a, b⟩ = λ(ab)` is `S`-invariant. -/
  antipode_frobeniusForm : antipode ≫ frobeniusForm = frobeniusForm

namespace FrobeniusHopfData

variable {C : Type u} [CategoryTheory.Category.{v} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
  (F : FrobeniusHopfData C)

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

/-- Alias for `FrobeniusHopfData`: the distinguished object `A` of a quantum
    universe `(C, A, τ)` is called the **Frobenius–Hopf aether** in the
    monograph (`\label{def:frobenius-hopf-substrate}`, cf. [thomson1867]). -/
abbrev FrobeniusHopfAether (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] :=
  FrobeniusHopfData C

/-- **Quantum Universe** over a commutative ring `R`.

    A triple `(C, A, ω)` where `C` is a `k`-linear **braided** monoidal
    category, `A` is a Frobenius–Hopf object in `C`, and `ω` is a fibre
    functor.  The deformation parameter `q` is not part of the base
    definition; it enters via the substrate parameter
    (Definition 1.x, `ArchimedeanSubstrateField`).

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
  frobHopf : @FrobeniusHopfData C catInst monInst braidedInst
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
  /-- **The ground ring is `End(𝟙_C)`.**  Scalar invariants of the unit object
      land in `R` rather than in `End(𝟙_C)`, which presumes the two agree.  That
      is a genuine extra assumption, NOT a consequence of `R`-linearity:
      `Linear R C` supplies only a ring map `R → End(𝟙_C)`, `r ↦ r • 𝟙`,
      and its being bijective needs `𝟙` simple.  Carried explicitly so the
      assumption is visible instead of hiding in a docstring.

      Surfaced on the paper side in `def:quantum-universe`. -/
  unitEndEquiv : R ≃+* CategoryTheory.End (𝟙_ C)
  /-- **`A` admits a universal first-order calculus.**  `Ω¹(A)` is a
      kernel of the multiplication `μ : A ⊗ A ⟶ A` in `C`: an object with a
      morphism `ι : Ω¹(A) ⟶ A ⊗ A` such that `ι ≫ μ = 0`.

      This is the noncommutative universal calculus, not Mathlib's
      `KaehlerDifferential` (which needs a commutative algebra and is the
      quotient `I/I²` of this kernel).  In `ModuleCat R`, for an algebra
      `A`, it is realised by `QOU.MathlibExt.UniversalDifferentials.Ω1`.

      Carried as a fork plus its universal property rather than as a
      `HasKernels C` instance: the paper needs this one kernel, not every
      kernel in `C`.  It replaces a bare `differentialForms : Type*`, which
      any type satisfied. -/
  differentialForms : CategoryTheory.Limits.KernelFork frobHopf.mul
  /-- The fork `differentialForms` is a limit: `Ω¹(A)` *is* the kernel of
      `μ`, not merely some object mapping into `A ⊗ A` and killed by `μ`. -/
  differentialForms_isLimit : CategoryTheory.Limits.IsLimit differentialForms

attribute [instance] QuantumUniverse.catInst QuantumUniverse.monInst
  QuantumUniverse.preInst QuantumUniverse.linInst QuantumUniverse.braidedInst
  QuantumUniverse.balancedInst

/-- **Wedderburn Semisimple Block Decomposition Data** for a Frobenius–Hopf
    substrate or a finite-strand endomorphism quotient slice (such as the
    Iwahori–Hecke quotient `H_n(q)` in Chapter 5).

    Per the 2026-11-19 architectural ruling, global finite Wedderburn
    semisimplicity is deferred out of `QuantumUniverse` and
    `QuantumObservableUniverse` to Chapter 5 (`braids-and-knots`) so that
    infinite Peter–Weyl coordinate algebras (such as `O(SU(2))`) and nilpotent
    jet thickenings satisfy the Quantum Universe axioms directly, while finite
    orthogonal central idempotent decompositions with invertible Frobenius
    weights and quantum dimensions are packaged in `SemisimpleBlockData U`.

    Encoded here: a `Fintype` of blocks, an idempotent endomorphism of `A`
    per block, their mutual orthogonality, their completeness, and
    invertibility of each block's Frobenius weight and quantum dimension.

    Given `SemisimpleBlockData U`, the co-Casimir trace identity
    `tr_M(C_dimQ) = Σ_λ 1/dim_q(λ)` follows by linearity of the trace over the
    central idempotents (`QOU.BraidKnot.frobenius_codim_universal`), and the
    Chern character factorisation `dim_q = ev ∘ ch` on `K₀` holds
    (`QOU.GrothendieckChern.dimQK0_eq_evDimQ_chernCharacter`). -/
structure SemisimpleBlockData {R : Type*} [CommRing R]
    (U : QuantumUniverse.{u, v} R) where
  /-- Finite index type of non-negligible Wedderburn blocks. -/
  blocks : Type v
  [blocksFintype : Fintype blocks]
  /-- The central idempotent `p_λ` of each block. -/
  centralIdem : blocks → (U.frobHopf.obj ⟶ U.frobHopf.obj)
  /-- Each `p_λ` is idempotent. -/
  centralIdem_idem : ∀ b, centralIdem b ≫ centralIdem b = centralIdem b
  /-- **Blocks do not mix.**  Distinct central idempotents are orthogonal, so a
      state resolving into one channel has no component in another. -/
  centralIdem_orthogonal : ∀ b b', b ≠ b' → centralIdem b ≫ centralIdem b' = 0
  /-- **The blocks span.**  `Σ_λ p_λ = 𝟙_A`: every state resolves into the
      channels, with nothing left over. -/
  centralIdem_complete : ∑ b, centralIdem b = 𝟙 U.frobHopf.obj
  /-- The Frobenius weight `∫_A p_λ` of each block. -/
  frobWeight : blocks → R
  /-- Every block's Frobenius weight is a **unit** in `R`. -/
  frobWeight_isUnit : ∀ b, IsUnit (frobWeight b)
  /-- The quantum dimension `dim_q(λ)` of each block. -/
  dimQ : blocks → R
  /-- Every block's quantum dimension is a **unit** in `R`. -/
  dimQ_isUnit : ∀ b, IsUnit (dimQ b)

attribute [instance] SemisimpleBlockData.blocksFintype

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
          `ε : Λ²V → 𝟙` preserved by the rigid dualities.  Formalised
          below under the **strong (iso) reading** — see the fields.

    LaTeX: `\label{def:quantum-observable-universe}` -/
structure QuantumObservableUniverse (R : Type*) [CommRing R]
    extends QuantumUniverse.{u, v} R where
  /-- **Rigidity** (condition 0): every object of `C` has left and right
      duals, with `ev`/`coev` satisfying the snake identities. -/
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
      That reduced adjoint is taken to land in `ker ε`; this field is part of
      the data and is not derived from a property of `ε`.  (An earlier
      justification read "the adjoint action preserves `ker ε` because `ε` is
      an algebra map".  A multiplicative counit is not available: it forces
      `x = ε(x) • 1` for every `x`, see
      `MultiplicativeCounitCollapse.eq_counit_smul_one`, bean `qou-aj49`.) -/
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
  /-- The exterior square `Λ²V` as an object of `C`.

      **This was previously a free field**, with nothing tying it to
      `fundamentalObj` — so condition (iii) said nothing about `V` at all.  The
      two fields below present it as a *quotient of* `V ⊗ V`, which is the
      weakest true statement that makes it `Λ²` of something rather than an
      arbitrary object.  Same defect and same repair as `adjointObj` above; see
      bean `qou-n1dj` item 3. -/
  exteriorSquare : C
  /-- The antisymmetrisation `π : V ⊗ V ↠ Λ²V`.  The corpus writes this arrow
      with a two-headed `↠` in `VolumeFromRigidity.projection` and in
      `lem:volume-from-rigidity`; the next field is that `↠`. -/
  exteriorSquareProj : (fundamentalObj ⊗ fundamentalObj) ⟶ exteriorSquare
  /-- `Λ²V` is a **quotient** of `V ⊗ V`.

      Deliberately no eigenvalue condition on the braiding.  In a braided
      category the braiding acts on the `q`-exterior square by `-q⁻¹`, not by
      `-1`, so demanding `β ≫ π = -π` would silently impose `q = 1` and rule
      out the quantum group the framework is about. -/
  exteriorSquare_epi : CategoryTheory.Epi exteriorSquareProj
  /-- **Volume constraint** (condition iii), under the **strong (iso)
      reading**: `ε : Λ²V ≅ 𝟙`.

      `def:quantum-observable-universe` writes "non-degenerate epimorphism",
      which admits two readings of unequal strength
      (`VolumeConstraintForcesFibreTwo.lean`):

      | reading | dimension statement | forces |
      |---|---|---|
      | epi onto `𝟙` | `C(N,2) ≠ 0` | `N ≥ 2` — admits the colour fibre `N = 3` |
      | **iso** `Λ²V ≅ 𝟙` | `C(N,2) = 1` | **`N = 2`** |

      The iso is taken because it is the reading under which the axiom does the
      job the corpus proof asks of it: `det(g)` is the scalar by which `g` acts
      on the **top** exterior power, so a constraint on `Λ²V` is a determinant
      constraint exactly when `2 = N`.  Under the weak reading `ε` constrains
      the second elementary symmetric function of the eigenvalues and the step
      to `det(g_V) = 1` does not go through.

      This also removes the vacuity: the previous field was a bare morphism,
      and `QuantumUniverse` supplies `Preadditive C`, so `volumeForm := 0`
      inhabited it for *any* `exteriorSquare`.  An iso cannot be zero unless
      the base ring is trivial — `volumeForm_ne_zero` below.

      LaTeX: `\label{eq:categorical-volume-constraint}` -/
  volumeIso : exteriorSquare ≅ (𝟙_ C)

/-! ### What the iso reading of condition (iii) buys

Three consequences, stated generically so they can be checked without a
`QuantumObservableUniverse` — of which this tree still has none.  Bean
`qou-n1dj` item 2 (which reading) and item 3 (the formalised condition was
vacuous).
-/

/-- **The volume form cannot be zero.**

This is the vacuity that bean `qou-n1dj` item 3 records.  With `volumeForm` a
bare morphism `Λ²V ⟶ 𝟙` and `Preadditive C` in scope, `volumeForm := 0`
inhabited condition (iii) for *any* `exteriorSquare`, so the formalised axiom
constrained nothing whatever.

Under the iso reading it cannot: `e.inv ≫ e.hom = 𝟙` collapses to `0` the
moment `e.hom = 0`, so a zero volume form forces `End (𝟙_ C)` to be trivial.
`QuantumUniverse.unitEndEquiv : R ≃+* End (𝟙_ C)` then carries that back to
`R`, which is why `volumeForm_ne_zero_of_nontrivial` below can state it as a
condition on the base ring rather than on the category. -/
theorem iso_unit_hom_ne_zero {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.Preadditive C] {X : C}
    (e : X ≅ (𝟙_ C)) (h : (CategoryTheory.CategoryStruct.id (𝟙_ C)) ≠ 0) :
    e.hom ≠ 0 := by
  intro he
  exact h (by simpa [he] using e.inv_hom_id.symm)

/-- **The volume form is epi, for free.**

The co-located sibling of `def:quantum-observable-universe` carries
`volumeForm_epi` as a *field* — "if two morphisms agree after precomposition
with `volumeForm`, they are equal" — and `su2-emergence.lean` takes the same
statement as an explicit hypothesis.  Under the iso reading neither is needed:
an isomorphism is epi. -/
theorem epi_of_iso_unit {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] {X : C} (e : X ≅ (𝟙_ C)) :
    CategoryTheory.Epi e.hom :=
  inferInstance

/-- **`V ⊗ V` surjects onto the unit.**

The composite of the antisymmetrisation `π : V ⊗ V ↠ Λ²V` with the volume
isomorphism.  This is the whole point of pairing the iso with the two new
`exteriorSquare` fields: the iso alone says `Λ²V ≅ 𝟙` for an object with no
stated relation to `V`, and `π` alone lets `Λ²V` be any quotient.  Together
they are a statement about the fundamental object.

It is the categorical shadow of `exteriorSquareDim_eq_one_iff`
(`VolumeConstraintForcesFibreTwo.lean`) and **not** a proof of it: getting from
here to `C(N,2) = 1` needs the fibre functor to be monoidal and to send
`exteriorSquare` to `Λ²(τ V)`, neither of which is available.  See the bean. -/
theorem epi_proj_comp_volume {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] {V X : C}
    (π : (V ⊗ V) ⟶ X) [CategoryTheory.Epi π] (e : X ≅ (𝟙_ C)) :
    CategoryTheory.Epi (π ≫ e.hom) :=
  CategoryTheory.epi_comp π e.hom

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
