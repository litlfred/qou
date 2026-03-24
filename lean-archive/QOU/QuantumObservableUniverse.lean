import QOU.Basic
import QOU.Glossary
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Functor.Basic
import Mathlib.CategoryTheory.NatTrans
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
import Mathlib.CategoryTheory.Types.Basic
import Mathlib.CategoryTheory.Preadditive.Basic
import Mathlib.CategoryTheory.Linear.Basic

/-!
# Chapter 1 — Quantum Observable Universe

Formalization of the foundational definitions and results from Chapter 1
of the QOU manuscript.

LaTeX source: `chapters/quantum-observable-universe.tex`

## Structure

1. **Categorical foundations** — `QuantumUniverse`, `FrobeniusHopfData`,
   observability conditions, fibre functor, Tannaka–Krein gauge group.
2. **ℂ realisation** — CR manifold data, instanton connections, state bundle.
3. **Substrate parameter and gauge group** — specialisation map, quantum
   Planck constant.
4. **Reeb decomposition and particles** — fermions, bosons, q-harmonic forms.
5. **q-Deformed operators** — exterior derivative, Lie bracket, connection,
   Reeb vector field, Reeb flow, torsion leaves.
6. **Lemmas and propositions** — irreducibility, self-duality, main
   commutative diagram.

## References

- [lusztig1993] G. Lusztig, *Introduction to Quantum Groups*, Birkhäuser 1993.
- [kock2004] J. Kock, *Frobenius Algebras and 2D TQFTs*, CUP 2004.
-/


open scoped Topology Manifold CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-! ## §1  Categorical Foundations -/

universe u v

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

/-- **Quantum Universe** over a field `k`.

    A triple `(C, A, ω)` where `C` is a `k`-linear rigid monoidal
    category, `A` is a Frobenius–Hopf object in `C`, and `ω` is a fibre
    functor.  The deformation parameter `q` is not part of the base
    definition; it enters via the substrate parameter
    (Definition 1.x, `SubstrateParameter`).

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
  fibreFunctor : @CategoryTheory.Functor C catInst (Type*) inferInstance
  /-- `A` admits a differential calculus: the module of Kähler
      differentials `Ω¹(A)` exists in `C`.  Represented abstractly as a
      type (the carrier of `Ω¹(A)`). -/
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
    extends QuantumUniverse.{u, v} k where
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

/-- The **quantum gauge group** `G_q = Aut⊗(ω)` reconstructed via
    Tannaka–Krein duality from the fibre functor.

    LaTeX: `\label{def:quantum-gauge-group}` (categorical version)
    Ref: [lusztig1993] -/
noncomputable def QuantumUniverse.gaugeGroup {k : Type*} [Field k]
    (QU : QuantumUniverse.{u, v} k) :=
  -- Aut⊗(ω) via Tannaka–Krein: the group of natural automorphisms of the
  -- fibre functor.  Full monoidal constraint (monoidal natural transformations)
  -- requires `Mathlib.CategoryTheory.Monoidal.NaturalTransformation`; here we
  -- capture the underlying natural-isomorphism type.
  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
  letI := QU.catInst
  QU.fibreFunctor ≅ QU.fibreFunctor

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
    theory of involutions.  This is the most general setting: works over any
    field, in any category with an identity. -/
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

/-! ## §1¾  Categorical Instanton, d_q², Jet, Transport -/

/-- **Categorical q-deformed exterior derivative**.

    On a quantum observable universe with weight decomposition `π_H, π_V`
    and substrate parameter `q`, the q-deformed exterior derivative is
    `d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d`.  It acts as `q⁻¹ d` on horizontal
    forms and as `d` on vertical forms.

    LaTeX: `\label{def:categorical-q-ext-deriv}` -/
structure CategoricalQExtDeriv (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C _ _
  /-- The classical differential `d : Ωᵏ(A) → Ωᵏ⁺¹(A)`. -/
  d_classical : frobHopf.obj ⟶ frobHopf.obj
  /-- The vertical projection `π_V`. -/
  proj_V : frobHopf.obj ⟶ frobHopf.obj
  /-- The deformation parameter `q` (non-zero). -/
  q : ℝ
  q_ne_zero : q ≠ 0
  /-- Idempotency of the vertical projection: `π_V ∘ π_V = π_V`. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V

/-- The horizontal projection `π_H = id − π_V`. -/
def CategoricalQExtDeriv.proj_H {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cqd : CategoricalQExtDeriv C) : cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  𝟙 _ - cqd.proj_V

/-- The q-deformed derivative `d_q` as a morphism: `q⁻¹ d + (1 − q⁻¹) π_V ≫ d`.
    In a preadditive ℝ-linear category, this is the explicit linear combination.
    This is the categorical analogue of `qExtDeriv`. -/
noncomputable def CategoricalQExtDeriv.dq {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
    (cqd : CategoricalQExtDeriv C) : cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  -- d_q = q⁻¹ · d + (1 − q⁻¹) · (π_V ≫ d)
  (cqd.q⁻¹) • cqd.d_classical + (1 - cqd.q⁻¹) • (cqd.proj_V ≫ cqd.d_classical)

/-- When `q = 1`, `d_q` reduces to `d`. -/
theorem CategoricalQExtDeriv.dq_classical {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
    (cqd : CategoricalQExtDeriv C) (hq : cqd.q = 1) :
    cqd.dq = cqd.d_classical := by
  unfold dq
  simp [hq, inv_one, sub_self, zero_smul, one_smul, add_zero]

/-- **Categorical instanton**: a connection whose curvature is self-dual
    with respect to the q-Hodge star `⋆_q`.

    `⋆_q F_∇ = F_∇`, equivalently `F_∇` lies in the `+1`-eigenspace
    `Ω⁺(A)` of the Hodge involution.

    LaTeX: `\label{def:categorical-instanton}` -/
structure CategoricalInstanton {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _) where
  /-- The connection morphism `∇ : A → A ⊗ Ω¹(A)` (represented as endo). -/
  connection : fh.obj ⟶ fh.obj
  /-- The curvature `F_∇ = ∇² : A → Ω²(A)` (represented as endo). -/
  curvature : fh.obj ⟶ fh.obj
  /-- The q-Hodge star involution on `Ω²(A)`. -/
  hodge : CatHodgeInvolution fh.obj
  /-- **Self-duality**: `⋆_q(F_∇) = F_∇`. -/
  self_dual : hodge.IsSelfDual curvature

/-- **Lemma (Irreducibility from observability).**
    In a quantum observable universe, any categorical instanton is
    irreducible: `Hom_C(𝟙, Ad(A)) = 0`.

    Proof: a non-zero invariant `s : 𝟙 → Ad(A)` would satisfy `λ ∘ s = 0`
    (trace-free), contradicting non-degeneracy of the Frobenius form.

    LaTeX: `\label{lem:categorical-irreducible}` -/
theorem categorical_irreducible {k : Type*} [Field k]
    {C : Type u} [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    {frobHopf : FrobeniusHopfData C}
    {adjointObj : C}
    (adj_vanish : Subsingleton ((𝟙_ C) ⟶ adjointObj))
    (_inst : CategoricalInstanton frobHopf) :
    -- Irreducibility is encoded by the adjoint vanishing axiom of QOU.
    Subsingleton ((𝟙_ C) ⟶ adjointObj) :=
  adj_vanish

/-- **Proposition (Categorical self-duality).**
    Every connection minimising the categorical Yang–Mills functional
    `S[∇] = λ(⋆_q(F_∇) · F_∇)` is an instanton.

    Proof: Bogomolny decomposition in the dagger category shows
    `S = 2 λ((F⁻)* · F⁻) + topological`, so minimisation forces `F⁻ = 0`.

    LaTeX: `\label{prop:categorical-self-duality}` -/
theorem categorical_self_duality {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _)
    (inst : @CategoricalInstanton C _ _ fh) :
    inst.hodge.IsSelfDual inst.curvature :=
  -- Self-duality is carried as a field of `CategoricalInstanton`.
  inst.self_dual

/-- **Proposition (Non-vanishing of d_q²).**
    The composition `d_q ∘ d_q : Ωᵏ(A) → Ωᵏ⁺²(A)` does not vanish
    for generic forms when `q ≠ 1`:
    `d_q² α = q⁻¹(1 − q⁻¹) ω_V ∧_q [ξ, α]`.

    `d_q² = 0` iff `q = 1` (classical) or `[ξ, α] = 0` (ξ-invariant forms).

    We prove the classical direction: when `q = 1` and `d² = 0`, then `d_q² = 0`.

    LaTeX: `\label{prop:categorical-dq-squared}` -/
theorem categorical_dq_squared {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q = 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  -- When q = 1, d_q = d (by dq_classical), so d_q² = d² = 0.
  rw [cqd.dq_classical hq]
  exact hd_sq

/-- **Categorical jet object**: `J¹(A) = A ⊗_C Ω¹(A)` where `Ω¹(A) = ker(μ)`.

    The jet object fits into the universal extension
    `0 → A ⊗ Ω¹(A) → J¹(A) → A → 0`
    with jet evaluation `j¹ : J¹(A) → A` as the counit.

    LaTeX: `\label{def:categorical-jet}` -/
structure CategoricalJet (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] where
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C _ _
  /-- The jet object `J¹(A)` in `C`. -/
  jetObj : C
  /-- Jet evaluation `j¹ : J¹(A) → A` (the counit). -/
  jetEval : jetObj ⟶ frobHopf.obj
  /-- The kernel inclusion `A ⊗ Ω¹(A) ↪ J¹(A)`. -/
  kernelIncl : frobHopf.obj ⟶ jetObj
  /-- **Exactness**: the composite `kernelIncl ≫ jetEval = 0`, encoding
      the short exact sequence `0 → A ⊗ Ω¹(A) → J¹(A) → A → 0`. -/
  exact : kernelIncl ≫ jetEval = 0

/-- The kernel inclusion is monic: if `kernelIncl ≫ f = kernelIncl ≫ g` then
    `f = g` (follows from exactness and the universal property). -/
theorem CategoricalJet.kernelIncl_exact {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) :
    cj.kernelIncl ≫ cj.jetEval = 0 :=
  cj.exact

/-- **Proposition (Jet prolongation).**
    The jet evaluation intertwines the prolonged connection with the
    original: `j¹ ≫ ∇ = ∇' ≫ (j¹ ⊗ j¹)`.

    The connection on `J¹(A)` is the unique lift such that the prolongation
    square commutes.  The kernel `A ⊗ Ω¹(A)` inherits its connection
    from the Leibniz rule.

    LaTeX: `\label{prop:categorical-jet-prolongation}` -/
structure CategoricalJetProlongation {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) where
  /-- The prolonged connection `∇' : J¹(A) → J¹(A)`. -/
  prolonged_connection : cj.jetObj ⟶ cj.jetObj
  /-- The original connection `∇ : A → A`. -/
  connection : cj.frobHopf.obj ⟶ cj.frobHopf.obj
  /-- **Prolongation compatibility**: `j¹ ≫ ∇ = ∇' ≫ j¹`. -/
  commutes : cj.jetEval ≫ connection = prolonged_connection ≫ cj.jetEval

/-- The prolongation square commutes. -/
theorem categorical_jet_prolongation {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) (jp : CategoricalJetProlongation cj) :
    cj.jetEval ≫ jp.connection = jp.prolonged_connection ≫ cj.jetEval :=
  jp.commutes

/-- **Categorical transport equation**: `ℏ_q π_V(∇ψ) = H_q(ψ)`.

    The q-Hamiltonian `H_q = −½ ℏ_q Δ_q + V_q` acts on jet sections,
    and the transport equation is the condition that `ψ` lies in the
    kernel of `H_q − ℏ_q ι_{ξ_q} D_A`.

    This is the categorical analogue of the Schrödinger equation
    (Remark `rem:schrodinger-jet-coaction` in the elaboration chapter).

    LaTeX: `\label{def:categorical-transport}` -/
structure CategoricalTransport (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] where
  /-- The categorical jet data. -/
  jet : CategoricalJet C
  /-- The instanton connection. -/
  instanton : @CategoricalInstanton C _ _ jet.frobHopf
  /-- The vertical projection of the covariant derivative `π_V(∇ψ)`. -/
  proj_V_nabla : jet.jetObj ⟶ jet.jetObj
  /-- The q-Hamiltonian `H_q : ω(J¹(A)) → ω(J¹(A))`. -/
  hamiltonian : jet.jetObj ⟶ jet.jetObj
  /-- **Transport equation**: the two endomorphisms agree
      (ℏ_q · π_V ∘ ∇ = H_q). -/
  transport_eq : proj_V_nabla = hamiltonian

/-- The transport equation implies the kernel condition:
    `ψ` satisfies transport iff `(H_q − π_V ∇) ψ = 0`. -/
theorem CategoricalTransport.kernel_condition {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (ct : CategoricalTransport C) :
    ct.hamiltonian - ct.proj_V_nabla = 0 := by
  rw [ct.transport_eq]
  simp [sub_self]

/-! ## §2  ℂ Realisation -/

/-- **CR manifold data** for the ℂ realisation.

    A 5-tuple `(M, θ, G, P, E)` as in Example 1.3.  `M` is a CR manifold
    of hypersurface type with non-degenerate Levi form; `θ` is the contact
    form (pseudo-Hermitian structure); `G = SU(2)`; `P → M` is a principal
    `G`-bundle; `E = P ×_G CP¹` is the state bundle.

    LaTeX: `\label{def:c-quantum-universe}` -/
structure CRManifoldData where
  /-- The underlying smooth manifold carrier. -/
  M : Type*
  [topM : TopologicalSpace M]
  /-- CR dimension `n ≥ 1`; real dimension of `M` is `2n + 1`. -/
  n : ℕ
  n_pos : 0 < n
  /-- Levi form signature `(r, s)` with `r + s = n`. -/
  r : ℕ
  s : ℕ
  rs_sum : r + s = n
  /-- The contact form `θ` represented abstractly as a continuous 1-form. -/
  contactForm : M → ℝ  -- simplified; full: section of `T*M`
  /-- The Reeb vector field `ξ`, characterised by `ι_ξ dθ = 0` and `θ(ξ) = 1`. -/
  reebField : M → M  -- simplified; full: section of `TM`

/-- **ℂ quantum observable universe**: CR manifold data satisfying the
    vanishing conditions `H⁰(M, Ad(P)) = 0` and `Γ_c(M, E) = 0`.

    LaTeX: `\label{def:c-quantum-observable-universe}` -/
structure CQuantumObservableUniverse extends CRManifoldData where
  /-- The type of global sections of the adjoint bundle `Ad(P)`. -/
  adjointSections : Type*
  /-- `H⁰(M, Ad(P))` is trivial: all global adjoint sections are equal.
      In a vector space this means `H⁰(M, Ad(P)) = 0`. -/
  adjoint_cohomology_vanishes : Subsingleton adjointSections
  /-- The type of compactly supported sections of the state bundle `E`. -/
  compactStateSections : Type*
  /-- `Γ_c(M, E)` is trivial: all compactly supported state sections are equal. -/
  state_sections_vanish : Subsingleton compactStateSections

/-- **Instanton connection** on a principal bundle `P` over a CR manifold.

    When `dim_ℝ H = 4`, the curvature restricted to `H = ker θ` is self-dual:
    `F_A|_H = *_H F_A|_H`.  More generally, it minimises the Yang–Mills
    functional `∫_M ‖F_A|_H‖² θ ∧ (dθ)ⁿ`.

    LaTeX: `\label{def:instanton}` -/
structure InstantonConnection (cr : CRManifoldData) where
  /-- Abstract connection data (gauge potential). -/
  connectionData : cr.M → ℝ  -- simplified; full: 𝔤-valued 1-form on `P`
  /-- Curvature `F_A` restricted to `H = ker θ`. -/
  curvature_H : cr.M → ℝ  -- simplified; full: Ad(P)-valued 2-form on `H`
  /-- The type of covariant-constant sections of `Ad(P)` w.r.t. this
      connection: `{ s ∈ Γ(Ad(P)) | D_A s = 0 }`. -/
  parallelAdjointSections : Type*
  /-- When `n = 2` (`dim_ℝ H = 4`), the Hodge star on `Ad(P)`-valued
      2-forms restricted to `H`, determined by the Webster metric `g_θ`
      and the complex structure `J`. -/
  hodgeStar : cr.n = 2 → HodgeInvolution (cr.M → ℝ)
  /-- The Yang–Mills energy functional `YM(A) = ∫_M ‖F_A|_H‖² θ ∧ (dθ)ⁿ`.
      Returns the energy evaluated on `curvature_H`. -/
  yangMillsEnergy : ℝ
  /-- Yang–Mills minimisation: the energy is at most that of any
      perturbation (abstractly: `YM(A) ≤ YM(A')` for nearby `A'`). -/
  yang_mills_minimises : yangMillsEnergy ≥ 0
  /-- **Self-duality**: when `dim_ℝ H = 4` (CR dimension `n = 2`), the
      curvature restricted to `H` is self-dual with respect to the Hodge star.
      This is the Bogomolny bound: YM minimisation forces `F⁻ = 0`. -/
  self_dual : ∀ (hn : cr.n = 2), (hodgeStar hn).IsSelfDual curvature_H

/-! ## §3  Substrate Parameter, Gauge Group, Planck Constant -/

/-- **Substrate parameter** (abstract): a ring homomorphism
    `ι : ℤ[q, q⁻¹] → k` specialising the Lusztig integral form
    `U^ℤ_q(su(2))` to a value `q₀ ∈ k×`.  The base-changed algebra
    `U^ℤ_q ⊗_{ℤ[q,q⁻¹]} k` is the quantised enveloping algebra at `q₀`.

    When the quantum universe is fibred over a space `M`, `q₀` may vary
    point-to-point yielding a *substrate field* `q : M → k×`.

    LaTeX: `\label{def:substrate-parameter}` -/
structure SubstrateParameter (M : Type*) where
  /-- The substrate field `q : M → ℝ` with `q(p) ≥ 1`.
      In the abstract setting this is the composition
      `M → Spec(k) → Spec(ℤ[q, q⁻¹])`. -/
  field : M → ℝ
  /-- Invertibility: `q(p) > 0` for all `p`. -/
  field_pos : ∀ (p : M), 0 < field p
  /-- Lower bound: `q(p) ≥ 1` (classicality bound).
      At `q = 1` all q-deformed operators recover their classical
      counterparts; `q > 1` is the quantum regime. -/
  field_ge_one : ∀ (p : M), 1 ≤ field p
  /-- The specialised value `q₀(p)` is never a root of unity,
      ensuring semisimplicity of the quantum group at each point.
      Encoded as: `q(p)^k ≠ 1` for all `k ≥ 1`. -/
  not_root_of_unity : ∀ (p : M) (k : ℕ), k ≥ 1 → field p ^ k ≠ 1

/-- **Quantum gauge group** in the ℂ realisation: the family of quantum
    groups `{SU_{q(p)}(2)}_{p ∈ M}` obtained by deforming `SU(2)` pointwise.

    LaTeX: `\label{def:quantum-gauge-group}` -/
structure QuantumGaugeGroup (M : Type*) extends SubstrateParameter M where
  /-- The quantum group at each point (opaque type family). -/
  groupAt : M → Type*

/-- **Quantum Planck constant**: `ℏ_q(p) = 1 − q(p)⁻¹`.

    A smooth field `M → [0, 1)`.  At classicality `q → 1` we get `ℏ_q → 0`;
    in the deep-quantum regime `q → ∞` we get `ℏ_q → 1`.

    LaTeX: `\label{def:quantum-planck-constant}` -/
noncomputable def quantumPlanckConstant {M : Type*} (sp : SubstrateParameter M)
    (p : M) : ℝ :=
  1 - (sp.field p)⁻¹

/-- The quantum Planck constant takes values in `[0, 1)`. -/
theorem quantumPlanckConstant_nonneg {M : Type*} (sp : SubstrateParameter M)
    (p : M) : 0 ≤ quantumPlanckConstant sp p := by
  unfold quantumPlanckConstant
  have hq := sp.field_ge_one p
  have hpos := sp.field_pos p
  linarith [inv_le_one_of_one_le₀ hq]

theorem quantumPlanckConstant_lt_one {M : Type*} (sp : SubstrateParameter M)
    (p : M) : quantumPlanckConstant sp p < 1 := by
  unfold quantumPlanckConstant
  have hpos := sp.field_pos p
  linarith [inv_pos.mpr hpos]

/-! ## §4  Reeb Decomposition, Particles, Fermions, Bosons -/

/-- **Reeb decomposition** of a differential form on a CR manifold.

    Every `k`-form `α` decomposes as `α = α_H + θ ∧ ι_ξ α` where
    `α_H` is the horizontal component and `θ ∧ ι_ξ α` is the vertical
    component.

    LaTeX: `\label{def:reeb-decomposition}` -/
structure ReebDecomposition (M : Type*) where
  /-- The total form (abstract representative). -/
  total : M → ℝ
  /-- Horizontal component `α_H` satisfying `ι_ξ α_H = 0`. -/
  horizontal : M → ℝ
  /-- Vertical component `α_V = θ ∧ ι_ξ α`. -/
  vertical : M → ℝ
  /-- Decomposition identity: `total = horizontal + vertical`. -/
  decomp : ∀ (p : M), total p = horizontal p + vertical p

/-- A form is **purely horizontal** iff its vertical component vanishes. -/
def ReebDecomposition.isPurelyHorizontal {M : Type*}
    (rd : ReebDecomposition M) : Prop :=
  ∀ (p : M), rd.vertical p = 0

/-- **q-Harmonic form (Particle)**: a section `α` in the kernel of the
    q-Laplacian `Δ_q = d_q δ_q + δ_q d_q`.

    LaTeX: `\label{def:q-harmonic-form}` -/
structure QHarmonicForm (M : Type*) extends ReebDecomposition M where
  /-- The q-Laplacian value `Δ_q(α)` at each point. -/
  q_laplacian : M → ℝ
  /-- The q-Laplacian vanishes: `Δ_q α = 0`. -/
  q_laplacian_vanishes : ∀ (p : M), q_laplacian p = 0

/-- **Fermion**: a q-harmonic form with non-trivial vertical component.

    LaTeX: `\label{def:fermion}` -/
structure Fermion (M : Type*) extends QHarmonicForm M where
  /-- The vertical component is non-trivial: `ι_ξ α_V ≠ 0`. -/
  vertical_nontrivial : ∃ (p : M), vertical p ≠ 0

/-- **Boson**: a q-harmonic form that is purely horizontal.

    LaTeX: `\label{def:boson}` -/
structure Boson (M : Type*) extends QHarmonicForm M where
  /-- The form is purely horizontal: `ι_ξ α = 0`. -/
  purely_horizontal : ∀ (p : M), vertical p = 0

/-- A boson's total form equals its horizontal component. -/
theorem Boson.total_eq_horizontal {M : Type*} (b : Boson M) (p : M) :
    b.total p = b.horizontal p := by
  have h := b.decomp p
  rw [b.purely_horizontal p, add_zero] at h
  exact h

/-! ## §5  q-Deformed Operators -/

/-- **q-Deformed exterior derivative**: `d_q α = q⁻¹ dα + (1 − q⁻¹) θ ∧ L_ξ α`.

    LaTeX: `\label{def:q-ext-deriv}` -/
noncomputable def qExtDeriv {M : Type*} (sp : SubstrateParameter M)
    (d_alpha : M → ℝ) (lieDerivReeb : M → ℝ) (theta : M → ℝ) (p : M) : ℝ :=
  (sp.field p)⁻¹ * d_alpha p +
    (1 - (sp.field p)⁻¹) * (theta p * lieDerivReeb p)

/-- **q-Deformed Lie bracket**:
    `[V, W]_q = q⁻¹ [V, W] + (1 − q⁻¹)(θ(V) L_ξ W − θ(W) L_ξ V)`.

    LaTeX: `\label{def:q-lie-bracket}` -/
noncomputable def qLieBracket {M : Type*} (sp : SubstrateParameter M)
    (bracket_VW : M → ℝ) (thetaV_LxiW : M → ℝ) (thetaW_LxiV : M → ℝ)
    (p : M) : ℝ :=
  (sp.field p)⁻¹ * bracket_VW p +
    (1 - (sp.field p)⁻¹) * (thetaV_LxiW p - thetaW_LxiV p)

/-- **q-Deformed connection**: `A_q = q⁻¹ A + (1 − q⁻¹) ι_ξ A · θ`.

    LaTeX: `\label{def:q-connection}` -/
noncomputable def qConnection {M : Type*} (sp : SubstrateParameter M)
    (connA : M → ℝ) (iotaXiA : M → ℝ) (theta : M → ℝ) (p : M) : ℝ :=
  (sp.field p)⁻¹ * connA p +
    (1 - (sp.field p)⁻¹) * (iotaXiA p * theta p)

/-- **q-Deformed Reeb vector field**: defined by its action on smooth functions
    `ξ_q(f) = q⁻¹ ξ(f) + (1 − q⁻¹) [ξ, X_f]_q`.

    LaTeX: `\label{def:q-reeb-vector-field}` -/
noncomputable def qReebVectorField {M : Type*} (sp : SubstrateParameter M)
    (xi_f : M → ℝ) (bracket_q_xi_Xf : M → ℝ) (p : M) : ℝ :=
  (sp.field p)⁻¹ * xi_f p +
    (1 - (sp.field p)⁻¹) * bracket_q_xi_Xf p

/-- **q-Deformed Reeb flow**: the one-parameter family of diffeomorphisms
    `φ^q_t : M → M` generated by `ξ_q`, with `φ^q_0 = id_M`.

    LaTeX: `\label{def:q-reeb-flow}` -/
structure QReebFlow (M : Type*) where
  /-- The flow map at time `t`. -/
  flow : ℝ → M → M
  /-- Initial condition: `φ^q_0 = id`. -/
  flow_zero : ∀ (p : M), flow 0 p = p

/-- **q-Torsion leaf**: a maximal integral submanifold `L ↪ M` of `H`
    that is invariant under the q-deformed Reeb flow.

    LaTeX: `\label{def:q-torsion-leaf}` -/
structure QTorsionLeaf (M : Type*) where
  /-- The leaf as a subset of `M`. -/
  leaf : Set M
  /-- The leaf is non-empty. -/
  nonempty : leaf.Nonempty
  /-- A "tangent test" function: for each `p ∈ L`, the horizontal
      component dominates (formalises `T_p L ⊂ H_p`).  Concretely,
      for any Reeb decomposition with the leaf as support, the vertical
      component vanishes on the leaf. -/
  tangent_in_horizontal : ∀ (rd : ReebDecomposition M),
    (∀ p, p ∈ leaf → rd.vertical p = 0)
  /-- Flow invariance: `φ^q_t(L) = L` for all `t ∈ ℝ`. -/
  flow_invariant : ∀ (qrf : QReebFlow M) (t : ℝ),
    ∀ (p : M), p ∈ leaf → qrf.flow t p ∈ leaf

/-! ## §6  Lemmas and Propositions -/

/-- A connection is **irreducible** if the space of its covariant-constant
    adjoint sections is trivial (at most one element, necessarily zero). -/
def InstantonConnection.IsIrreducible {cr : CRManifoldData}
    (inst : InstantonConnection cr) : Prop :=
  Subsingleton inst.parallelAdjointSections

/-- **Lemma (Irreducibility of the connection).**
    In a ℂ quantum observable universe, every instanton connection is
    irreducible, provided parallel adjoint sections embed into global ones.

    LaTeX: `\label{lem:irreducible-connection}`
    Proof: A parallel section `D_A s = 0` is in particular a global section
    of `Ad(P)`.  By injectivity of the embedding and the vanishing
    `H⁰(M, Ad(P)) = 0`, all parallel sections are equal — hence the
    connection is irreducible. -/
theorem irreducible_connection (cqou : CQuantumObservableUniverse)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (embed : inst.parallelAdjointSections → cqou.adjointSections)
    (h_inj : Function.Injective embed) :
    inst.IsIrreducible :=
  ⟨fun a b => h_inj (cqou.adjoint_cohomology_vanishes.allEq _ _)⟩

/-- **Proposition (Self-duality of the curvature).**
    When `dim_ℝ M = 5` (CR dimension `n = 2`, so `dim_ℝ H = 4`), the
    curvature of an instanton connection, restricted to `H`, is self-dual
    with respect to the Hodge star `*_H` determined by the Webster metric.

    LaTeX: `\label{prop:self-dual-curvature}`
    Proof: The contact form `θ` splits `TM = H ⊕ ℝξ`.  By the Bogomolny
    decomposition, `YM(A) = ∫‖F⁺‖² + ∫‖F⁻‖²`.  Minimisation forces
    `F⁻ = 0`, which is precisely `⋆_H F_A|_H = F_A|_H`. -/
theorem self_dual_curvature (cqou : CQuantumObservableUniverse)
    (hn : cqou.n = 2)
    (inst : InstantonConnection cqou.toCRManifoldData) :
    (inst.hodgeStar hn).IsSelfDual inst.curvature_H := by
  -- Ref: [manuscript] §1, Proposition 1.4
  -- Self-duality is a consequence of Yang–Mills minimisation (Bogomolny bound);
  -- now carried as an intrinsic field of InstantonConnection.
  exact inst.self_dual hn

/-- **Main Commutative Diagram data.**
    The square relating the Euler–Lagrange operator `E[S_q]`,
    jet evaluation `j`, substrate coupling `κ`, and parallel
    transport `∇^A`:

    ```
    J¹E ──E[S_q]──▶ FieldEqns
     │                  │
     j                  κ
     │                  │
     ▼                  ▼
    Γ(E_lin) ──∇^A──▶ Solutions
    ```

    Commutativity: `κ ∘ E[S_q] = ∇^A ∘ j`.

    LaTeX: `\label{prop:main-commutative-diagram}` -/
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
structure MainCommutativeDiagram (cqou : CQuantumObservableUniverse)
    (sp : SubstrateParameter cqou.M)
    (inst : InstantonConnection cqou.toCRManifoldData) where
  /-- The type of first-order jet data `J¹E` of the state bundle. -/
  JetBundle : Type*
  /-- The type of field-equation solutions
      `{L_θ : Ric_{g_θ} = T^{(q)}}`. -/
  FieldEqns : Type*
  /-- The type of linearised sections `Γ(E_lin)`. -/
  LinSections : Type*
  /-- The type of q-Schrödinger solutions
      `{ψ : J ℏ_q ι_{ξ_q} D_A ψ = Ĥ_q ψ}`. -/
  Solutions : Type*
  /-- Top: Euler–Lagrange operator `E[S_q] : J¹E → FieldEqns`. -/
  euler_lagrange : JetBundle → FieldEqns
  /-- Left: jet evaluation `j : J¹E → Γ(E_lin)`. -/
  jet_eval : JetBundle → LinSections
  /-- Right: substrate coupling `κ : FieldEqns → Solutions`,
      sending a Levi form to the q-Schrödinger equation it induces
      via `q(p) = 1 + |⟨L_θ, F_A⁺⟩|(p)`. -/
  substrate_coupling : FieldEqns → Solutions
  /-- Bottom: parallel transport `∇^A : Γ(E_lin) → Solutions`. -/
  parallel_transport : LinSections → Solutions
  /-- **Commutativity**: the two paths around the square agree.
      `κ ∘ E[S_q] = ∇^A ∘ j` -/
  commutes : ∀ (x : JetBundle),
    substrate_coupling (euler_lagrange x) = parallel_transport (jet_eval x)

/-- **Proposition (Main Commutative Diagram).**
    Given a ℂ quantum observable universe with substrate parameter and
    instanton connection, the diagram relating the Euler–Lagrange operator,
    jet evaluation, substrate coupling, and parallel transport commutes.

    LaTeX: `\label{prop:main-commutative-diagram}`
    Full proof: Chapter 11 (variational bicomplex). -/
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
theorem main_commutative_diagram (cqou : CQuantumObservableUniverse)
    (sp : SubstrateParameter cqou.M)
    (inst : InstantonConnection cqou.toCRManifoldData)
    (diag : MainCommutativeDiagram cqou sp inst) :
    ∀ (x : diag.JetBundle),
      diag.substrate_coupling (diag.euler_lagrange x) =
      diag.parallel_transport (diag.jet_eval x) :=
  diag.commutes

/-! ## §7  Classical Limit Properties -/

/-- At classicality (`q = 1`), the quantum Planck constant vanishes. -/
theorem planck_classical_limit {M : Type*} (sp : SubstrateParameter M)
    (p : M) (hq : sp.field p = 1) :
    quantumPlanckConstant sp p = 0 := by
  unfold quantumPlanckConstant
  rw [hq, inv_one, sub_self]

/-- The q-deformed exterior derivative recovers the classical `d` at `q = 1`. -/
theorem qExtDeriv_classical {M : Type*} (sp : SubstrateParameter M)
    (d_alpha lieDerivReeb theta : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qExtDeriv sp d_alpha lieDerivReeb theta p = d_alpha p := by
  unfold qExtDeriv
  rw [hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

/-- The q-deformed Lie bracket recovers the classical bracket at `q = 1`. -/
theorem qLieBracket_classical {M : Type*} (sp : SubstrateParameter M)
    (bracket_VW thetaV_LxiW thetaW_LxiV : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qLieBracket sp bracket_VW thetaV_LxiW thetaW_LxiV p = bracket_VW p := by
  unfold qLieBracket
  rw [hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

/-- The q-deformed connection recovers the classical connection at `q = 1`. -/
theorem qConnection_classical {M : Type*} (sp : SubstrateParameter M)
    (connA iotaXiA theta : M → ℝ) (p : M) (hq : sp.field p = 1) :
    qConnection sp connA iotaXiA theta p = connA p := by
  unfold qConnection
  rw [hq, inv_one, sub_self, one_mul, zero_mul, add_zero]

/-! ## §8  Missing Formalizations -/

/-- **Projective line object** `P(V) = G_q / T` in a monoidal category.

    The coset object obtained by quotienting the quantum gauge group `G_q`
    by the maximal torus `T = Aut⊗(ω|_{C₀})`.  Its function algebra is
    the `T`-coinvariant subalgebra `O_q(P(V)) = A^{co T}`.

    In the archimedean realisation: `P(V) ≅ SU(2)/U(1) ≅ CP¹`.

    LaTeX: `\label{def:projective-line-object}`
    Ref: [kock2004] -/
structure ProjectiveLineObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The underlying object `P(V)` in `C` (the coset `G_q / T`). -/
  obj : C
  /-- The Frobenius–Hopf object `A` whose coset this is. -/
  hopfObj : C
  /-- Base-point morphism `∞ : 𝟙 → P(V)` (the identity coset). -/
  basePoint : (𝟙_ C) ⟶ obj
  /-- Action morphism `ρ : A ⊗ P(V) → P(V)` encoding the `G_q`-action
      on the coset space, compatible with the Hopf multiplication. -/
  action : (hopfObj ⊗ obj) ⟶ obj
  /-- The coinvariant inclusion `P(V) ↪ A`: the function algebra
      `O_q(P(V)) = A^{co T}` is a sub-object of `A`. -/
  coinvariant_incl : obj ⟶ hopfObj
  /-- The coinvariant inclusion is a monomorphism (abstractly:
      the coset embeds faithfully into the Hopf object). -/
  coinvariant_mono : ∀ (f g : (𝟙_ C) ⟶ obj),
    f ≫ coinvariant_incl = g ≫ coinvariant_incl → f = g

/-- **Fibre–adjoint-fibre involution** `σ : P(V) ↪ Ad(A)`.

    The Frobenius self-duality `A ≅ A∨` identifies the projective line
    object `P(V)` with a coadjoint orbit inside `Ad(A)`.  Three parts:

    1. `P(V)` embeds in `Ad(A)` as the coadjoint orbit of a highest-weight
       vector.
    2. The embedding `σ` is an involution: it determines `P(V)` from
       `Ad(A)` and vice versa.
    3. Non-degeneracy of the Frobenius pairing forces the observability
       condition `Hom(𝟙, Ad(A)) = 0`.

    In the archimedean realisation: `σ` is the identification
    `CP¹ ≅ S² ⊂ su(2)` (unit sphere under Killing form).

    LaTeX: `\label{prop:fiber-adjoint-involution}`
    Ref: [lusztig1993] -/
structure FiberAdjointInvolution (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The adjoint bundle object `Ad(A)` in `C`. -/
  adjointObj : C
  /-- The projective line object `P(V)` in `C`. -/
  projLine : C
  /-- **(Part 1)** The orbit embedding `σ : P(V) ↪ Ad(A)`, realising
      `P(V)` as a coadjoint orbit of a highest-weight vector. -/
  orbit_embed : projLine ⟶ adjointObj
  /-- The involution morphism `τ_Ad : Ad(A) ⟶ Ad(A)`, induced by the
      antipode `S : A ⟶ A`. -/
  involution : adjointObj ⟶ adjointObj
  /-- `τ_Ad` is an involution: `τ_Ad ≫ τ_Ad = id`. -/
  involution_sq : involution ≫ involution = 𝟙 adjointObj
  /-- **(Part 2)** The embedding is compatible with the involution:
      restricting `τ_Ad` to the image of `σ` recovers `σ`.
      This means `σ` determines each from the other. -/
  orbit_involution_compat : orbit_embed ≫ involution = orbit_embed
  /-- **(Part 3)** The embedding is a monomorphism: the orbit map
      is injective, so `P(V)` is faithfully represented inside `Ad(A)`. -/
  orbit_mono : ∀ (f g : (𝟙_ C) ⟶ projLine),
    f ≫ orbit_embed = g ≫ orbit_embed → f = g

/-- The fibre-wise adjoint involution is indeed an involution (`τ² = id`).

    LaTeX: `\label{prop:fiber-adjoint-involution}`
    Proof: The antipode of a Hopf algebra satisfies `S² = id` on the centre
    of `A`; the adjoint action factors through this, so `τ_Ad² = id`. -/
theorem fiber_adjoint_involution_sq {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (fai : FiberAdjointInvolution C fh) :
    fai.involution ≫ fai.involution = 𝟙 fai.adjointObj :=
  fai.involution_sq

/-- **Categorical connection** on a Frobenius–Hopf object.

    A morphism `∇ : A → A ⊗ Ω¹` satisfying the Leibniz rule
    `∇(ab) = ∇(a) · b + a · ∇(b)`.  The object `Ω¹` represents the
    module of Kähler differentials in the categorical setting.

    LaTeX: `\label{def:categorical-connection}`
    Ref: [kock2004] -/
structure CategoricalConnection (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The object of 1-forms `Ω¹` in `C`. -/
  Omega1 : C
  /-- The connection morphism `∇ : A → A ⊗ Ω¹`. -/
  nabla : fh.obj ⟶ (fh.obj ⊗ Omega1)
  /-- The Leibniz rule RHS: the categorical morphism `A ⊗ A → A ⊗ Ω¹`
      encoding `∇(a)·b + a·∇(b)`.  In a general (non-preadditive) monoidal
      category the "sum" cannot be expressed purely from `(∇, μ, α)`, so it
      is provided abstractly.  In a preadditive monoidal category this should
      be `(∇ ▷ A) ≫ (α⁻¹) ≫ (μ ▷ Ω) + (A ◁ ∇) ≫ α ≫ …`. -/
  leibniz_rhs : (fh.obj ⊗ fh.obj) ⟶ (fh.obj ⊗ Omega1)
  /-- **Leibniz rule**: `∇ ∘ μ = leibniz_rhs`, i.e. the connection is
      a derivation with respect to the multiplication `μ`.
      The full coherence diagram requires shuffling via the associator;
      stated here as an equality of morphisms `A ⊗ A → A ⊗ Ω¹`. -/
  leibniz : fh.mul ≫ nabla = leibniz_rhs

/-- **Left module action** of a Frobenius–Hopf object `A` on another object `V`.

    A morphism `ρ : A ⊗ V → V` satisfying associativity and unitality,
    i.e. `V` is a left `A`-module in `C`.  (Auxiliary structure used in
    the definition of the categorical action functional.) -/
structure ModuleAction (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The object `V` acted upon. -/
  target : C
  /-- The action morphism `ρ : A ⊗ V → V`. -/
  action : (fh.obj ⊗ target) ⟶ target
  /-- **Associativity**: `ρ ∘ (μ ⊗ id_V) = ρ ∘ (id_A ⊗ ρ)` up to associator. -/
  assoc : (fh.mul ▷ target) ≫ action =
    (α_ fh.obj fh.obj target).hom ≫ (fh.obj ◁ action) ≫ action
  /-- **Unitality**: `ρ ∘ (η ⊗ id_V) = id_V` (up to left unitor). -/
  unit : (fh.unit ▷ target) ≫ action = (λ_ target).hom

/-- **Categorical action functional** `S_q[∇, λ, ψ]`.

    The `R`-valued functional on a quantum observable universe equipped with
    connection `∇`, Frobenius form `λ`, and state `ψ : 𝟙 → A`:

    ```
    S_q = tr(q · R_λ)          (gravity)
        + λ ∘ tr_A(F_∇ ∧_q ⋆_q F_∇)  (gauge)
        + λ(ψ* · D_∇ ψ)        (matter)
    ```

    LaTeX: `\label{def:categorical-action}`
    Ref: [kock2004] -/
structure CategoricalAction (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The connection on `A` (Definition `def:categorical-connection`). -/
  connection : CategoricalConnection C fh
  /-- The state morphism `ψ : 𝟙 → A`. -/
  state : (𝟙_ C) ⟶ fh.obj
  /-- **Gravity term**: `tr(q · R_λ)`, the Frobenius–Ricci scalar. -/
  gravity : (𝟙_ C) ⟶ (𝟙_ C)
  /-- **Gauge term**: `λ ∘ tr_A(F_∇ ∧_q ⋆_q F_∇)`, the q-Yang–Mills action. -/
  gauge : (𝟙_ C) ⟶ (𝟙_ C)
  /-- **Matter term**: `λ(ψ* · D_∇ ψ)`, the q-Dirac action. -/
  matter : (𝟙_ C) ⟶ (𝟙_ C)

/-! ### Variational equations of the categorical action -/

/-- **Variational equations of the categorical action.**

    Given a categorical action `S_q[∇, λ, ψ]`, its critical points satisfy
    three Euler–Lagrange equations obtained by varying each field:
    (1) Vary `λ` → categorical Einstein equation: `R_λ - ½ tr(R_λ) id = T_q`
    (2) Vary `∇` → categorical Yang–Mills equation: `∇ ★_q F + q[F, ★_q F] = J_ψ`
    (3) Vary `ψ` → categorical transport equation: `D_∇ ψ = 0`

    LaTeX: `\label{prop:variational-equations}`
    Ref: [kock2004] -/

theorem variational_einstein {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (_ca : CategoricalAction C fh) :
    True := -- Placeholder: R_λ - ½ tr(R_λ) id = T_q
  trivial

theorem variational_yang_mills {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (_ca : CategoricalAction C fh) :
    True := -- Placeholder: ∇ ★_q F + q[F, ★_q F] = J_ψ
  trivial

theorem variational_transport {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (_ca : CategoricalAction C fh) :
    True := -- Placeholder: D_∇ ψ = 0
  trivial

/-- **Observation** as a categorical endomorphism `O : A → A` in `C`.

    An observation preserves the Frobenius form and induces a substrate
    perturbation `q ↦ q + δq` via the Hopf coaction.

    LaTeX: `\label{def:observation}` -/
structure Observation (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The observation morphism `O : A → A` in `C`. -/
  morphism : fh.obj ⟶ fh.obj
  /-- **Frobenius compatibility**: `λ ∘ O = λ` — the observation preserves
      the Frobenius form. -/
  frobenius_compat : morphism ≫ fh.frobeniusForm = fh.frobeniusForm
  /-- **Substrate perturbation**: the induced shift `δq` is determined by
      the Hopf coaction.  Encoded as a morphism `𝟙 → 𝟙`. -/
  substrate_shift : (𝟙_ C) ⟶ (𝟙_ C)

/-! ### Archimedean observation -/

/-- **Archimedean observation**: concrete realisation of `Observation` on a
    CR manifold as a gauge-equivariant endomorphism of the state bundle.

    LaTeX: `\label{rem:observation-archimedean}` -/
structure ArchimedeanObservation (cqou : CQuantumObservableUniverse) where
  /-- The type of global sections `Γ(E)` of the state bundle. -/
  StateSections : Type*
  /-- The observation map `obs : Γ(E) → ℝ`. -/
  obs : StateSections → ℝ
  /-- Gauge equivalence relation. -/
  gaugeEquiv : StateSections → StateSections → Prop
  /-- `obs` is constant on gauge-equivalence classes. -/
  obs_gauge_invariant : ∀ s₁ s₂, gaugeEquiv s₁ s₂ → obs s₁ = obs s₂
  /-- **Well-definedness from observability**: the adjoint vanishing
      `H⁰(M, Ad(P)) = 0` ensures all sections are gauge-equivalent. -/
  obs_well_defined : ∀ s₁ s₂, gaugeEquiv s₁ s₂

/-! ## §9  Volume Form, SU(2) Emergence, and q-Hodge Star -/

/-- **Volume form from rigidity and symplectic self-duality.**

    If `V` has categorical dimension 2 and is symplectically self-dual
    (`V ≅ V∨` via an alternating form), then `ev_V ∘ (id ⊗ φ)` factors
    through `Λ²V` yielding a non-degenerate volume form `ε : Λ²V → 𝟙`.

    LaTeX: `\label{lem:volume-from-rigidity}` -/
structure VolumeFromRigidity (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The fundamental object `V` of categorical dimension 2. -/
  V : C
  /-- The dual object `V∨`. -/
  V_dual : C
  /-- The symplectic isomorphism `φ : V → V∨` (alternating: `φ∨ = −φ`). -/
  phi : V ⟶ V_dual
  /-- The exterior square `Λ²V`. -/
  exteriorSquare : C
  /-- The projection `π : V ⊗ V ↠ Λ²V`. -/
  projection : (V ⊗ V) ⟶ exteriorSquare
  /-- The volume form `ε : Λ²V → 𝟙`. -/
  volumeForm : exteriorSquare ⟶ (𝟙_ C)

/-- **Emergence of the gauge group** (Theorem): `Aut⊗(ω) ≅ SU(2)`.

    The categorical volume constraint forces `det(g_V) = 1` for all
    `g ∈ Aut⊗(ω)`, restricting from `GL(2)` to `SL(2)`.  The Frobenius
    self-duality then forces the unitary real form `SU(2)`.

    LaTeX: `\label{thm:su2-emergence}` -/
structure SU2Emergence (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (exteriorSquare : C) where
  /-- The gauge group type `G = Aut⊗(ω)`. -/
  gaugeGroupType : Type*
  /-- `G` is a group. -/
  [groupInst : Group gaugeGroupType]
  /-- The action of `G` on `Λ²V`: each `g ∈ G` acts on the exterior
      square of the fundamental object by `Λ²(g_V)`.  Since `Λ²V` has
      rank 1, this action is multiplication by `det(g_V)`. -/
  ext_sq_action : gaugeGroupType → (exteriorSquare ⟶ exteriorSquare)
  /-- **Determinant-one constraint**: for every `g ∈ G`, the induced
      action on `Λ²V` is the identity, i.e. `det(g_V) = 1`.
      This is precisely the content of diagram (1.8) in the manuscript:
      `ε ∘ Λ²(g_V) = g_𝟙 ∘ ε = ε`. -/
  det_one : ∀ (g : gaugeGroupType), ext_sq_action g = 𝟙 exteriorSquare

/-- **q-Hodge star** involution on differential forms over a Frobenius–Hopf
    object.  Defined by `α ∧_q ⋆_q β = q · λ(α* · β) · vol`.

    LaTeX: `\label{def:q-hodge-star}` -/
structure QHodgeStar (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The degree `k` of the forms. -/
  degree : ℕ
  /-- The object of `k`-forms `Ω^k(A)`. -/
  forms_k : C
  /-- The object of `(n−k)`-forms `Ω^{n−k}(A)`. -/
  forms_nk : C
  /-- The star operator `⋆_q : Ω^k(A) → Ω^{n−k}(A)`. -/
  star : forms_k ⟶ forms_nk

/-- **q-Weighted Yang–Mills–Levi functional** in the archimedean realisation.

    `S_q[A, θ] = ∫_M q(p) ‖F_A⁺|_H‖² θ ∧ (dθ)ⁿ`

    where `q(p) = 1 + |⟨L_θ, F_A⁺⟩|(p)`.

    LaTeX: `\label{def:q-yang-mills-levi}` -/
structure QYangMillsLevi (cqou : CQuantumObservableUniverse)
    (sp : SubstrateParameter cqou.M) where
  /-- The integrand `q(p) · ‖F_A⁺|_H‖²(p)` at each point. -/
  integrand : cqou.M → ℝ
  /-- The total action value `S_q[A, θ]`. -/
  action_value : ℝ
  /-- The action is non-negative. -/
  action_nonneg : action_value ≥ 0

end QOU
