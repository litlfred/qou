import QOU.QuantumObservableUniverse.Structures
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
  /-- The deformation parameter `q` (non-zero). -/
  q : ℝ
  q_ne_zero : q ≠ 0
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
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
    (cqd : CategoricalQExtDeriv C) : cqd.frobHopf.obj ⟶ cqd.frobHopf.obj :=
  (cqd.q⁻¹) • cqd.d_classical + (1 - cqd.q⁻¹) • (cqd.proj_V ≫ cqd.d_classical)

/-- When `q = 1`, `d_q` reduces to `d`. -/
theorem CategoricalQExtDeriv.dq_classical {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
    (cqd : CategoricalQExtDeriv C) (hq : cqd.q = 1) :
    cqd.dq = cqd.d_classical := by
  unfold CategoricalQExtDeriv.dq
  simp [hq, inv_one, sub_self, zero_smul, one_smul, add_zero]

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

/-- **Categorical irreducibility — hypotheses of the manuscript proof.**

    Carries the two *inputs* of the argument in
    [`prf:categorical-irreducible`], parameterised by the inclusion
    `ι : Ad(A) ↪ A` of the adjoint object (`A` is self-dual, so
    `A ⊗ A^∨ ≃ A ⊗ A`; `ι` is the trace-free part sitting inside it):

    * **trace-freeness** — `∫_A` vanishes on `Ad(A)`, so it cannot
      separate two morphisms `𝟙 → Ad(A)`;
    * **non-degeneracy** — the observability axiom, stated as
      `Mono (ι ≫ ∫_A)`.

    Neither field is the conclusion `Subsingleton (𝟙 ⟶ Ad(A))`; the
    conclusion is *derived* from them in `categorical_irreducible` by
    cancelling the mono. They are of course jointly **equivalent** to it —
    that is what it means for the manuscript proof to be correct — but the
    equivalence runs through the cancellation step, which is the argument.
    Compare the field this class used to carry, which *was* the conclusion
    verbatim (see the removal note below).

    Stated in zero-free form (`s ≫ f = t ≫ f` rather than `s ≫ f = 0`)
    because `C` is not assumed to have zero morphisms. -/
class HasCategoricalIrreducibility {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    {frobHopf : FrobeniusHopfData C}
    (adjointObj : C)
    (adjointInclusion : adjointObj ⟶ frobHopf.obj)
    (_inst : CategoricalInstanton frobHopf) : Prop where
  /-- **Trace-freeness of `Ad(A)`.** `Ad(A)` is the trace-free part of
      `A ⊗ A^∨`, so the Frobenius form `∫_A` restricted along `ι` does not
      distinguish morphisms out of the unit: `∫_A ∘ ι ∘ s = ∫_A ∘ ι ∘ t`
      for all `s, t : 𝟙 → Ad(A)`. -/
  form_indistinguishes :
    ∀ s t : (𝟙_ C) ⟶ adjointObj,
      s ≫ adjointInclusion ≫ frobHopf.frobeniusForm
        = t ≫ adjointInclusion ≫ frobHopf.frobeniusForm
  /-- **Non-degeneracy of `∫_A` (observability axiom).** The restricted
      form `ι ≫ ∫_A` is a monomorphism. -/
  form_mono : CategoryTheory.Mono (adjointInclusion ≫ frobHopf.frobeniusForm)

/-! ### `hasCategoricalIrreducibility_of_subsingleton` — REMOVED 2026-08-23

    It read

        instance hasCategoricalIrreducibility_of_subsingleton …
            [hsub : Subsingleton ((𝟙_ C) ⟶ adjointObj)] :
            HasCategoricalIrreducibility adjointObj inst := ⟨hsub⟩

    and its hypothesis `Subsingleton ((𝟙_ C) ⟶ adjointObj)` is the
    conclusion of `categorical_irreducible` **verbatim**.  So the class was
    obtainable only by already holding what it asserts, and the accessor
    then handed it straight back — a caller who could synthesise the
    instance never needed the theorem.

    That circularity is what makes the §3b-cond carrier degenerate: the
    class is supposed to hold the *open* content, so an instance route that
    starts from the conclusion defeats it.  Removing the instance leaves
    `HasCategoricalIrreducibility` as an honest open carrier with no
    inhabitation route, which is the correct state for an unproved claim.
    Nothing synthesised it (0 references outside this file).

    Vacuity ledger, `proof-no-self-assuming-projection`.  The ledger's
    earlier evidence recorded this as an "UNINHABITED carrier … no instance
    exists"; that was wrong — the instance existed, and the defect is its
    circularity, not its absence. -/

/-! ### `HasCategoricalIrreducibility.subsingleton` — REPLACED 2026-08-23

    Removing the circular instance (above) left the class honest about
    *inhabitation* but not about *content*: its single field read

        subsingleton : Subsingleton ((𝟙_ C) ⟶ adjointObj)

    which is the conclusion of `categorical_irreducible` verbatim, and the
    theorem was `h.subsingleton`.  That is the §3b-cond item-5 degenerate
    shape — the class carried the conclusion, so the theorem derived
    nothing — and it is this file's `proof-no-self-assuming-projection`
    entry in the vacuity ledger.

    The block's own proof (`prf:categorical-irreducible`) states the
    argument: *"Since `Ad(A)` is the trace-free part of `A ⊗ A^*`, the
    Frobenius form `∫_A` vanishes on it … But `∫_A` is non-degenerate by
    the observability axiom, so `s = 0`."*  Neither of those is the
    conclusion, so the class now carries **them**, and the theorem
    performs the step the manuscript performs: cancel the mono. -/

/-- **Categorical irreducibility** (per-instance form,
    [`lem:categorical-irreducible`]).

    In a quantum observable universe, the adjoint-rep hom-space vanishes:
    `Hom(𝟙, Ad(A))` is a subsingleton.  Derived from the two hypotheses of
    `HasCategoricalIrreducibility` — trace-freeness of `Ad(A)` and
    non-degeneracy of `∫_A` — by cancelling the monomorphism, which is the
    manuscript proof of `prf:categorical-irreducible`. -/
theorem categorical_irreducible {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    {frobHopf : FrobeniusHopfData C}
    {adjointObj : C}
    {adjointInclusion : adjointObj ⟶ frobHopf.obj}
    (inst : CategoricalInstanton frobHopf)
    [h : HasCategoricalIrreducibility adjointObj adjointInclusion inst] :
    Subsingleton ((𝟙_ C) ⟶ adjointObj) := by
  haveI := h.form_mono
  exact ⟨fun s t => (CategoryTheory.cancel_mono _).mp (h.form_indistinguishes s t)⟩

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
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
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
`q⁻²(1 − q)² ≠ 0` for the cross-term `π_V ∘ d ∘ π_V ∘ d`. The proof
is a direct computation once `Linear ℝ C` provides scalar expansion,
but the cross-term non-vanishing hypothesis `hcross` is already hoisted.

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
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
    (cqd : CategoricalQExtDeriv C)
    (hq : cqd.q ≠ 1)
    (hd_sq : cqd.d_classical ≫ cqd.d_classical = 0)
    (hcross : cqd.proj_V ≫ cqd.d_classical ≫ cqd.proj_V ≫ cqd.d_classical ≠ 0) : Prop where
  /-- The non-vanishing conclusion. -/
  nonvanishing : cqd.dq ≫ cqd.dq ≠ 0

/-! ### `hasDqSquaredNonvanishing_of_fact` — REMOVED 2026-08-23

    It read `… [hf : Fact (cqd.dq ≫ cqd.dq ≠ 0)] : HasDqSquaredNonvanishing
    cqd hq hd_sq hcross := ⟨hf.out⟩` — the same circularity as above, since
    the `Fact` is the conclusion itself.

    It also made the three hypotheses decorative.  `HasDqSquaredNonvanishing`
    is parameterised by `hq : cqd.q ≠ 1`, `hd_sq : d_classical ≫ d_classical
    = 0` and `hcross : … ≠ 0`, and `categorical_dq_squared_nonvanishing`
    binds all three — so the statement reads as a substantive conditional.
    But this instance **ignored all three** and produced the class from the
    `Fact`, so on the only available inhabitation route none of them was
    ever load-bearing.

    Removed (0 references outside this file), leaving the class as an honest
    open carrier.  Whether `hq`/`hd_sq`/`hcross` actually imply the
    non-vanishing is the open question the file should answer; until it
    does, no instance should be derivable from the conclusion.

    Vacuity ledger, `proof-no-self-assuming-projection`. -/

/-- **`d_q²` non-vanishing** (per-instance form). -/
theorem categorical_dq_squared_nonvanishing {C : Type u}
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] [CategoryTheory.Linear ℝ C]
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
