import QOU.QuantumObservableUniverse.Structures
import QOU.GroundRingCore
import Mathlib.CategoryTheory.Linear.Basic

/-!
# §1¾  Categorical Instanton, d_q², Jet, Transport

The q-deformed exterior derivative `d_q`, categorical instantons,
jet objects, jet prolongation, and the categorical transport equation.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-! ## §1¾  Categorical Instanton, d_q², Jet, Transport -/

/-- **Categorical q-deformed exterior derivative**.

    On a quantum observable universe with weight decomposition `π_H, π_V`
    and substrate parameter `q`, the q-deformed exterior derivative is
    `d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d`.

    LaTeX: `\label{def:categorical-q-ext-deriv}` -/
structure CategoricalQExtDeriv (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A` in `C`. -/
  frobHopf : @FrobeniusHopfData C _ _
  /-- The classical differential `d : Ωᵏ(A) → Ωᵏ⁺¹(A)`. -/
  d_classical : frobHopf.obj ⟶ frobHopf.obj
  /-- The vertical projection `π_V`. -/
  proj_V : frobHopf.obj ⟶ frobHopf.obj
  /-- The deformation parameter `q`, over the formal ground ring.

      Was `q : ℝ`. `def:substrate-parameter` puts the deformation parameter in
      `End(𝟙) ≅ R_q`, not in `ℝ`, and the co-located sibling had already made
      the move (bean `qou-u87j`); this copy is the one that had not. -/
  q : QOU.GroundRing.R_q
  /-- A two-sided inverse for `q`, carried as **data**.

      `R_q = ℤ[q, q⁻¹]` is a ring, not a field: it has no `Inv` instance, so
      `q⁻¹` cannot be *written* even though the indeterminate is invertible in
      it. Carrying the inverse explicitly, with its defining relation below, is
      **strictly stronger** than the `q_ne_zero` it replaces — over a ring,
      invertible is not implied by nonzero. And the block needs the stronger
      form: `d_q = q⁻¹ d + (1 − q⁻¹) π_V ∘ d` requires `q⁻¹` to *exist*, which
      `q ≠ 0` does not give. -/
  qinv : QOU.GroundRing.R_q
  /-- `qinv` is the inverse of `q`. Replaces the former `q_ne_zero`. -/
  q_mul_qinv : q * qinv = 1
  /-- Idempotency of the vertical projection: `π_V ∘ π_V = π_V`. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V

/-- The horizontal projection `π_H = id − π_V`. -/
def proj_H {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cqd : CategoricalQExtDeriv C) : cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  𝟙 _ - cqd.proj_V

/-- The q-deformed derivative `d_q` as a morphism: `q⁻¹ d + (1 − q⁻¹) π_V ≫ d`. -/
noncomputable def CategoricalQExtDeriv.dq {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear QOU.GroundRing.R_q C]
    (cqd : CategoricalQExtDeriv C) : cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  -- `q⁻¹` supplied by `qinv`; `R_q` has no `Inv` instance to write it with.
  cqd.qinv • cqd.d_classical + (1 - cqd.qinv) • (cqd.proj_V ≫ cqd.d_classical)

/-- When `q = 1`, `d_q` reduces to `d`. -/
theorem CategoricalQExtDeriv.dq_classical {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear QOU.GroundRing.R_q C]
    (cqd : CategoricalQExtDeriv C) (hq : cqd.q = 1) :
    cqd.dq = cqd.d_classical := by
  -- `q = 1` forces `qinv = 1` through the defining relation, rather than
  -- through `inv_one` (which needs an `Inv` instance `R_q` does not have).
  have hqinv : cqd.qinv = 1 := by
    have h := cqd.q_mul_qinv
    rw [hq, one_mul] at h
    exact h
  unfold CategoricalQExtDeriv.dq
  simp [hqinv, sub_self, zero_smul, one_smul, add_zero]

/-- **Categorical instanton**: a connection whose curvature is self-dual
    with respect to the q-Hodge star `⋆_q`.

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

/-!
**Lemma (Irreducibility from observability).**
LaTeX: `\label{lem:categorical-irreducible}`

A categorical instanton forces the adjoint hom-space `Hom(𝟙, Ad(A)) = 0`:
any anti-self-dual connection must be the zero connection, so there are no
non-trivial adjoint-valued observables.

**Axiom justification**: requires encoding the adjoint representation
`Ad(A) = A ⊗ A^∨` as a categorical construction and deriving
`Hom(𝟙, Ad(A)) = 0` from self-duality of the curvature. The adjoint-rep
functor (internal End) is not yet in Mathlib for general monoidal categories.

Classical counterpart: Donaldson–Kronheimer, *The Geometry of Four-Manifolds*,
§4.2 (irreducibility of anti-self-dual connections).

References:
- [manuscript] §1-quantum-observable-universe
- [donaldson1990] https://doi.org/10.1093/oso/9780198535539.001.0001
-/

/-- **Categorical irreducibility — typeclass.**
    Witnesses adjoint-rep vanishing for a specific
    `(C, frobHopf, adjointObj, inst)` choice rather than asserting
    it for *every* monoidal category. The conjectural content
    (encoding `Ad(A) = A ⊗ A^∨` and deriving `Hom(𝟙, Ad(A)) = 0`
    from self-duality) becomes a per-instance obligation visible
    at every use site. -/
class HasCategoricalIrreducibility {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    {frobHopf : FrobeniusHopfData C}
    (adjointObj : C)
    (_inst : CategoricalInstanton frobHopf) : Prop where
  /-- Vanishing of adjoint-rep observables. -/
  subsingleton : Subsingleton ((𝟙_ C) ⟶ adjointObj)

/-- **Default instance from a `Subsingleton` witness**.  When the
    Hom-space `(𝟙_ C) ⟶ adjointObj` is already known to be a
    `Subsingleton` (e.g. zero-object, terminal, or trivially
    discrete category), the irreducibility witness is automatic. -/
instance hasCategoricalIrreducibility_of_subsingleton
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    {frobHopf : FrobeniusHopfData C}
    (adjointObj : C)
    (inst : CategoricalInstanton frobHopf)
    [hsub : Subsingleton ((𝟙_ C) ⟶ adjointObj)] :
    HasCategoricalIrreducibility adjointObj inst :=
  ⟨hsub⟩

/-- **Categorical irreducibility** (per-instance form).
    Use this lemma — backed by `HasCategoricalIrreducibility` —
    instead of the deprecated universal axiom. -/
theorem categorical_irreducible {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    {frobHopf : FrobeniusHopfData C}
    {adjointObj : C}
    (inst : CategoricalInstanton frobHopf)
    [h : HasCategoricalIrreducibility adjointObj inst] :
    Subsingleton ((𝟙_ C) ⟶ adjointObj) :=
  h.subsingleton

/-- **Proposition (Categorical self-duality).**
    LaTeX: `\label{prop:categorical-self-duality}`

    Any `CategoricalInstanton` is self-dual by construction: self-duality
    is encoded as a field of the structure.  This is a structural accessor
    theorem; for the derivation of self-duality from the variational
    principle see `variational_einstein`. -/
-- Ref: [manuscript] §1-quantum-observable-universe
theorem categorical_self_duality {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : @FrobeniusHopfData C _ _)
    (inst : @CategoricalInstanton C _ _ fh) :
    inst.hodge.IsSelfDual inst.curvature :=
  inst.self_dual

/-- **Classical limit of d_q².**
    LaTeX: `\label{prop:categorical-dq-squared}`

    When `q = 1`, `d_q²` vanishes whenever the classical `d²` vanishes.
    This is the classical-limit direction; for the non-vanishing direction
    (`d_q² ≠ 0` when `q ≠ 1`) see `categorical_dq_squared_nonvanishing`. -/
-- Ref: [manuscript] §1-quantum-observable-universe
theorem categorical_dq_squared_classical_limit {C : Type u}
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear QOU.GroundRing.R_q C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q = 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0) :
    cqd.dq ≫ cqd.dq = 0 := by
  rw [cqd.dq_classical hq]
  exact hd_sq

/-!
**Non-vanishing of d_q²** (the quantum correction).
LaTeX: `\label{prop:categorical-dq-squared-nonvanishing}`

When `q ≠ 1` and the classical `d² = 0`, the q-deformed `d_q²` is
non-zero: the deformation introduces a genuine curvature term.

**Axiom justification**: requires analysis of the scalar coefficient
`qinv²(1 − q)² ≠ 0` for the cross-term `π_V ∘ d ∘ π_V ∘ d`. The proof
is a direct computation once `Linear R_q C` provides scalar expansion,
but the cross-term non-vanishing hypothesis `hcross` is already hoisted.

The coefficient is written with the carried `qinv`, not `q⁻¹`: over
`R_q = ℤ[q, q⁻¹]` the notation `q⁻¹` does not exist (no `Inv` instance),
so the argument has to run off `q_mul_qinv` (bean `qou-u87j`).  `R_q` is
an integral domain and `qinv` is a unit, so `qinv² (1 − q)² ≠ 0` reduces
to `1 − q ≠ 0` — exactly the `q ≠ 1` hypothesis.  The former `ℝ` version
additionally needed `q ≠ 0` to write `q⁻¹` at all.

The hypothesis `hcross` represents the geometric content: the vertical
projection `π_V` does not commute with the classical differential `d`,
so the cross-term is generically non-zero.

Ref: Connes, *Noncommutative Geometry*, Ch IV (spectral deformations).

References:
- [manuscript] §1-quantum-observable-universe
- [connes1994] https://doi.org/10.1016/0022-4049(94)90126-0
-/

/-- **`d_q²` non-vanishing — typeclass.**
    Per-instance witness that the `q`-deformed curvature is
    non-zero for a specific `(C, cqd)` choice with the
    classical-vanishing and cross-term hypotheses already in
    scope. Replaces the universal axiom over all monoidal `C`. -/
class HasDqSquaredNonvanishing {C : Type u}
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear QOU.GroundRing.R_q C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q ≠ 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0)
    (hcross : cqd.proj_V ≫ cqd.d_classical ≫ cqd.proj_V ≫ cqd.d_classical ≠ 0) : Prop where
  /-- The non-vanishing conclusion. -/
  nonvanishing : cqd.dq ≫ cqd.dq ≠ 0

/-- **Default instance from a `Fact` witness on the non-vanishing**.
    When `Fact (cqd.dq ≫ cqd.dq ≠ 0)` is in scope (e.g. supplied
    by the geometric proof at the specific `cqd`), the
    `HasDqSquaredNonvanishing` instance follows. -/
instance hasDqSquaredNonvanishing_of_fact {C : Type u}
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear QOU.GroundRing.R_q C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q ≠ 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0)
    (hcross : cqd.proj_V ≫ cqd.d_classical ≫ cqd.proj_V ≫ cqd.d_classical ≠ 0)
    [hf : Fact (cqd.dq ≫ cqd.dq ≠ 0)] :
    HasDqSquaredNonvanishing cqd hq hd_sq hcross :=
  ⟨hf.out⟩

/-- **`d_q²` non-vanishing** (per-instance form). -/
theorem categorical_dq_squared_nonvanishing {C : Type u}
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear QOU.GroundRing.R_q C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q ≠ 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0)
    (hcross : cqd.proj_V ≫ cqd.d_classical ≫ cqd.proj_V ≫ cqd.d_classical ≠ 0)
    [h : HasDqSquaredNonvanishing cqd hq hd_sq hcross] :
    cqd.dq ≫ cqd.dq ≠ 0 :=
  h.nonvanishing

/-- **Categorical jet object**: `J¹(A) = A ⊗_C Ω¹(A)`.
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
  /-- **Exactness**: `kernelIncl ≫ jetEval = 0`. -/
  exact : kernelIncl ≫ jetEval = 0

theorem kernelIncl_exact {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) :
    cj.kernelIncl ≫ cj.jetEval = 0 :=
  cj.exact

/-- **Proposition (Jet prolongation).**
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

theorem categorical_jet_prolongation {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (cj : CategoricalJet C) (jp : CategoricalJetProlongation cj) :
    cj.jetEval ≫ jp.connection = jp.prolonged_connection ≫ cj.jetEval :=
  jp.commutes

/-- **Categorical transport equation**: `ℏ_q π_V(∇ψ) = Ĥ_q(ψ)`.
    (In LaTeX: `\hat{H}_q`; distinct from the q-shuffle Hopf algebra
    `\mathcal{H}_q` of Ch 2 and the hook-length product `H_q(λ)` of
    the knot chapter.)
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
  /-- The q-Hamiltonian `Ĥ_q` (LaTeX `\hat{H}_q`). -/
  hamiltonian : jet.jetObj ⟶ jet.jetObj
  /-- **Transport equation**: `π_V(∇ψ) = Ĥ_q`. -/
  transport_eq : proj_V_nabla = hamiltonian

/-- The transport equation implies `Ĥ_q − π_V ∇ = 0`. -/
theorem kernel_condition {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C]
    (ct : CategoricalTransport C) :
    ct.hamiltonian - ct.proj_V_nabla = 0 := by
  rw [ct.transport_eq]
  simp [sub_self]

end QOU
