import QOU.QuantumObservableUniverse.Instanton
import QOU.QuantumObservableUniverse.CRRealisation
import QOU.QuantumObservableUniverse.SubstrateParameter
import QOU.MathlibExt.MonoidalCalcVar

/-!
# §8  Gauge Theory Structures

Projective line object, fibre–adjoint involution, categorical connection,
module action, categorical action functional, variational equations,
and observations.

## Rank of the Einstein slot — retyped 2026-09-15 (owner-authorised, `qou-h0ou`)

`CategoricalVariationalData.einsteinTensor` and `.stressTensor`, and the
`CategoricalAction.gravity` term they are summed against, were typed
`(𝟙_ C) ⟶ (𝟙_ C)` — the **scalars** `End(𝟙_C)`.  Einstein's equation is a
rank-2 identity, and a scalar cannot state one; the three were tensors in name
only.

They are now `PairingSpace C fh.obj fh.obj = fh.obj ⊗ fh.obj ⟶ 𝟙_ C`, the field
space of `QOU.MathlibExt.MonoidalCalcVar`.  **The co-pairing needed to contract
back to a scalar is not invented for this change** — it is `fh.coevaluation`,
already a field of `FrobeniusHopfData`, and the field space already has a
canonical inhabitant, the Frobenius pairing `fh.mul ≫ fh.frobeniusForm`
(`frobeniusPairing` below).  `A` being self-dual is what makes
`fh.obj ⊗ fh.obj` the right pair of slots.

`gauge`, `gaugeCurrent` and `matter` are **unchanged** scalars: only the terms
entering `gravity = einsteinTensor + stressTensor` had to move, since that
equation's three terms must inhabit one additive group.  This is a typing
consequence, not a physical claim about which currents "are" tensors.

`variational_einstein_contracted` derives the old scalar Einstein equation from
the new rank-2 one against `fh.coevaluation`, so nothing previously statable is
lost; `MonoidalCalcVar.subsingleton_of_contract_reflects` is why the converse
fails.  No metric, curvature, stress-energy realisation or numerical constant
is introduced.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

open QOU.MathlibExt.MonoidalCalcVar (PairingSpace contract)

/-! ## §8  Missing Formalizations -/

/-- **Projective line object** `P(V) = G_q / T` in a monoidal category.
    LaTeX: `\label{def:projective-line-object}` -/
structure ProjectiveLineObject (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] where
  /-- The underlying object `P(V)` in `C`. -/
  obj : C
  /-- The Frobenius–Hopf object `A` whose coset this is. -/
  hopfObj : C
  /-- Base-point morphism `∞ : 𝟙 → P(V)`. -/
  basePoint : (𝟙_ C) ⟶ obj
  /-- Action morphism `ρ : A ⊗ P(V) → P(V)`. -/
  action : (hopfObj ⊗ obj) ⟶ obj
  /-- The coinvariant inclusion `P(V) ↪ A`. -/
  coinvariant_incl : obj ⟶ hopfObj
  /-- The coinvariant inclusion is a monomorphism. -/
  coinvariant_mono : ∀ (f g : (𝟙_ C) ⟶ obj),
    f ≫ coinvariant_incl = g ≫ coinvariant_incl → f = g

/-- **Fibre–adjoint-fibre involution** `σ : P(V) ↪ Ad(A)`.
    LaTeX: `\label{prop:fiber-adjoint-involution}` -/
structure FiberAdjointInvolution (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The adjoint bundle object `Ad(A)` in `C`. -/
  adjointObj : C
  /-- The projective line object `P(V)` in `C`. -/
  projLine : C
  /-- The orbit embedding `σ : P(V) ↪ Ad(A)`. -/
  orbit_embed : projLine ⟶ adjointObj
  /-- The involution morphism `τ_Ad : Ad(A) ⟶ Ad(A)`. -/
  involution : adjointObj ⟶ adjointObj
  /-- `τ_Ad` is an involution: `τ_Ad ≫ τ_Ad = id`. -/
  involution_sq : involution ≫ involution = 𝟙 adjointObj
  /-- Compatibility: `σ ≫ τ_Ad = σ`. -/
  orbit_involution_compat : orbit_embed ≫ involution = orbit_embed
  /-- The embedding is a monomorphism. -/
  orbit_mono : ∀ (f g : (𝟙_ C) ⟶ projLine),
    f ≫ orbit_embed = g ≫ orbit_embed → f = g

/-- **Categorical connection** on a Frobenius–Hopf object.
    LaTeX: `\label{def:categorical-connection}` -/
structure CategoricalConnection (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The object of 1-forms `Ω¹` in `C`. -/
  Omega1 : C
  /-- The connection morphism `∇ : A → A ⊗ Ω¹`. -/
  nabla : fh.obj ⟶ (fh.obj ⊗ Omega1)
  /-- The Leibniz rule RHS. -/
  leibniz_rhs : (fh.obj ⊗ fh.obj) ⟶ (fh.obj ⊗ Omega1)
  /-- **Leibniz rule**: `∇ ∘ μ = leibniz_rhs`. -/
  leibniz : fh.mul ≫ nabla = leibniz_rhs

/-- **Left module action** of `A` on another object `V`. -/
structure ModuleAction (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The object `V` acted upon. -/
  target : C
  /-- The action morphism `ρ : A ⊗ V → V`. -/
  action : (fh.obj ⊗ target) ⟶ target
  /-- **Associativity**. -/
  assoc : (fh.mul ▷ target) ≫ action =
    (α_ fh.obj fh.obj target).hom ≫ (fh.obj ◁ action) ≫ action
  /-- **Unitality**. -/
  unit : (fh.unit ▷ target) ≫ action = (λ_ target).hom

/-- **Categorical action functional** `S_q[∇, λ, ψ]`.
    LaTeX: `\label{def:categorical-action}` -/
structure CategoricalAction (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The connection on `A`. -/
  connection : CategoricalConnection C fh
  /-- The state morphism `ψ : 𝟙 → A`. -/
  state : (𝟙_ C) ⟶ fh.obj
  /-- **Gravity term**: `tr(q · R_λ)` — **rank-2**, a pairing on `A ⊗ A`.
      Retyped 2026-09-15: it is summed against the Einstein and stress terms,
      so it must live where a rank-2 identity can be stated. -/
  gravity : PairingSpace C fh.obj fh.obj
  /-- **Gauge term**: `λ ∘ tr_A(F_∇ ∧_q ⋆_q F_∇)`. -/
  gauge : (𝟙_ C) ⟶ (𝟙_ C)
  /-- **Matter term**: `λ(ψ* · D_∇ ψ)`. -/
  matter : (𝟙_ C) ⟶ (𝟙_ C)

/-! ### Variational equations of the categorical action -/

/-! The equations of motion for the categorical action are:
  - **Einstein**: `R_λ − ½ tr(R_λ) id = T_q`
  - **Yang–Mills**: `∇ ★_q F + q[F, ★_q F] = J_ψ`
  - **Transport**: `D_∇ ψ = 0`

  A full derivation requires a categorical calculus of variations
  (Euler–Lagrange machinery for monoidal categories), which is not yet
  available in Lean/Mathlib.  The morphisms `gravity`, `gauge`, `matter`
  in `CategoricalAction` represent the action *terms*; the equations
  of motion relate them to the external current densities and tensors.
  These are stated axiomatically below, pending formalization. -/

/-- **Variational EOM data**: the external morphisms appearing in the
    categorical equations of motion — the Einstein tensor, stress-energy
    tensor, and gauge current density. -/
structure CategoricalVariationalData (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh) where
  /-- The Einstein tensor `G_λ = R_λ − ½ tr(R_λ) id` — **rank-2**, a pairing
      on `A ⊗ A`.  Retyped 2026-09-15 (`qou-h0ou`): it was
      `(𝟙_ C) ⟶ (𝟙_ C)`, a scalar wearing a tensor's name. -/
  einsteinTensor : PairingSpace C fh.obj fh.obj
  /-- The stress-energy tensor `T_q = δS_matter / δg` — **rank-2**. -/
  stressTensor : PairingSpace C fh.obj fh.obj
  /-- The gauge current density `J_ψ`.  Unchanged: it is not summed against
      the Einstein term, so nothing forces it to move. -/
  gaugeCurrent : (𝟙_ C) ⟶ (𝟙_ C)

/-! ### Variational equations as a typeclass (Pattern 4)

The three variational equations of motion (Einstein, Yang–Mills,
transport) require a categorical calculus of variations not yet
available in Mathlib. Rather than asserting them universally for
*every* `(C, fh, ca, vd)`, we package them as a typeclass
`HasCategoricalEOM`. Callers must supply an instance to use the
identities, making the conjectural content visible at every use
site.

The classical (set-theoretic) versions of these equations follow
from Wald, Bleecker, and Kobayashi–Nomizu; the typeclass instances
will be discharged once the categorical Euler–Lagrange machinery
is formalised. -/

/-- **Categorical equations of motion — typeclass.**
    Witnesses the three variational identities for a specific
    `(C, fh, ca, vd)` choice, encoding the on-shell relations
    between action terms and external currents/tensors. -/
class HasCategoricalEOM {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh)
    (vd : CategoricalVariationalData C fh ca) : Prop where
  /-- **Einstein**: `G_λ + T_q = gravity` (Wald, *General
      Relativity*, Theorem 4.3.1). -/
  einstein : ca.gravity = vd.einsteinTensor + vd.stressTensor
  /-- **Yang–Mills**: `gauge = J_ψ` (Bleecker, *Gauge Theory and
      Variational Principles*, Ch VII). -/
  yang_mills : ca.gauge = vd.gaugeCurrent
  /-- **Transport**: `matter = 0` (Kobayashi–Nomizu Vol I, Ch II,
      parallel transport). -/
  transport : ca.matter = 0

/-- **Default instance from a Fact-bundled witness**: when each of
    the three variational identities is bundled into a `Fact`
    triple in scope (typically from a per-`(C, fh, ca, vd)`
    construction), the `HasCategoricalEOM` instance follows
    immediately. -/
instance hasCategoricalEOM_of_facts {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh)
    (vd : CategoricalVariationalData C fh ca)
    [hE : Fact (ca.gravity = vd.einsteinTensor + vd.stressTensor)]
    [hYM : Fact (ca.gauge = vd.gaugeCurrent)]
    [hT : Fact (ca.matter = 0)] :
    HasCategoricalEOM fh ca vd where
  einstein := hE.out
  yang_mills := hYM.out
  transport := hT.out

/-- **Einstein equation** (per-instance form).
    Use this lemma — backed by `HasCategoricalEOM` — instead of the
    deprecated universal axiom. -/
-- Ref: [leitner2026] §1-quantum-observable-universe
-- Ref: [wald1984] General Relativity — see folio/schema/references.ts
theorem variational_einstein {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh)
    (vd : CategoricalVariationalData C fh ca)
    [HasCategoricalEOM fh ca vd] :
    ca.gravity = vd.einsteinTensor + vd.stressTensor :=
  HasCategoricalEOM.einstein

/-- **Yang–Mills equation** (per-instance form). -/
-- Ref: [leitner2026] §1-quantum-observable-universe
-- Ref: [bleecker1981] Gauge Theory and Variational Principles — see folio/schema/references.ts
theorem variational_yang_mills {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh)
    (vd : CategoricalVariationalData C fh ca)
    [HasCategoricalEOM fh ca vd] :
    ca.gauge = vd.gaugeCurrent :=
  HasCategoricalEOM.yang_mills

/-- **Transport equation** (per-instance form). -/
-- Ref: [leitner2026] §1-quantum-observable-universe
-- Ref: [kobayashi1963] Kobayashi-Nomizu, Foundations of Differential Geometry, Vol. I (1963 Interscience; 1996 Wiley reprint = kobayashi1996), DOI 10.1002/9780470316559
theorem variational_transport {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C] [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh)
    (vd : CategoricalVariationalData C fh ca)
    [HasCategoricalEOM fh ca vd] :
    ca.matter = 0 :=
  -- `vd` must be supplied explicitly: unlike `einstein`/`yang_mills`, the
  -- goal `ca.matter = 0` does not mention `vd`, so it cannot be inferred
  -- from the expected type (v4.24.0 elaboration).
  HasCategoricalEOM.transport (vd := vd)

/-! ### The rank-2 field space and the bridge back to the scalars

Added 2026-09-15 with the retype (`qou-h0ou`).  Two things keep the retype
honest.  The field space is inhabited by something the substrate already
carries, so the new slots are not empty by construction; and the scalar
equation this file stated before the retype is *recoverable* from the rank-2
one, so the change is a refactor rather than a replacement.

The converse direction fails —
`MonoidalCalcVar.subsingleton_of_contract_reflects` shows that a contraction
which reflected equality uniformly in the co-pairing would force the field
space to be a subsingleton — so the rank-2 form is strictly stronger.
`coevaluation_contract_eq_iff` gives the exact residue for the particular
co-pairing used here. -/

/-- **The Frobenius pairing, as an element of the field space.**  The
    evaluation `ev = μ ≫ λ` is what the snake identities
    (`FrobeniusHopfData.pairing_snake_left` / `_right`) pair against
    `fh.coevaluation` to exhibit `A` as self-dual, and its type is
    `fh.obj ⊗ fh.obj ⟶ 𝟙_ C` verbatim — a `PairingSpace`.

    So the retyped Einstein and stress slots have an inhabitant supplied by the
    substrate itself; the rank-2 field space is not a wider type with nothing
    in it. -/
def frobeniusPairing {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.BraidedCategory C] (fh : FrobeniusHopfData C) :
    PairingSpace C fh.obj fh.obj :=
  fh.mul ≫ fh.frobeniusForm

/-- **Bridge (contracted form).**  Contracting the rank-2 Einstein identity
    against `fh.coevaluation` — the co-pairing `FrobeniusHopfData` already
    carries, not one introduced for this purpose — gives an identity in the
    scalars `End(𝟙_C)`.

    Derived, not assumed: the proof rewrites by `variational_einstein` and then
    uses additivity of `MonoidalCalcVar.contract`. -/
theorem variational_einstein_contracted {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh)
    (vd : CategoricalVariationalData C fh ca)
    [HasCategoricalEOM fh ca vd] :
    contract fh.coevaluation ca.gravity
      = contract fh.coevaluation vd.einsteinTensor
        + contract fh.coevaluation vd.stressTensor := by
  rw [variational_einstein fh ca vd, map_add]

/-- **Bridge (unfolded form).**  The same statement with the contraction
    written out, so that what is recovered is visibly the pre-retype Einstein
    equation: a morphism identity `𝟙_ C ⟶ 𝟙_ C` between the gravity scalar and
    the sum of the Einstein and stress scalars.

    This is the declaration to cite for "the scalar form was not lost". -/
theorem variational_einstein_scalar {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C]
    (fh : FrobeniusHopfData C)
    (ca : CategoricalAction C fh)
    (vd : CategoricalVariationalData C fh ca)
    [HasCategoricalEOM fh ca vd] :
    fh.coevaluation ≫ ca.gravity
      = fh.coevaluation ≫ vd.einsteinTensor
        + fh.coevaluation ≫ vd.stressTensor := by
  simpa using variational_einstein_contracted fh ca vd

/-- **What the bridge costs, exactly.**  Two rank-2 fields have the same
    contraction against `fh.coevaluation` precisely when their difference is
    killed by it.  So the scalar Einstein equation determines the rank-2 one
    only modulo that kernel, and `FrobeniusHopfData` carries no hypothesis
    making the kernel trivial — there is no epi condition on `coevaluation`
    anywhere in the structure.

    Stated as the residue rather than as a claim about `fh`, because which of
    the two holds is a property of the particular category and is not asserted
    here. -/
theorem coevaluation_contract_eq_iff {C : Type u}
    [CategoryTheory.Category.{v} C] [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.BraidedCategory C]
    [CategoryTheory.Preadditive C] (fh : FrobeniusHopfData C)
    (G T : PairingSpace C fh.obj fh.obj) :
    fh.coevaluation ≫ G = fh.coevaluation ≫ T
      ↔ fh.coevaluation ≫ (G - T) = 0 := by
  rw [CategoryTheory.Preadditive.comp_sub, sub_eq_zero]

/-- **Observation** as a categorical endomorphism `O : A → A`.
    LaTeX: `\label{def:observation}` -/
structure Observation (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C] [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The observation morphism `O : A → A`. -/
  morphism : fh.obj ⟶ fh.obj
  /-- **Frobenius compatibility**: `λ ∘ O = λ`. -/
  frobenius_compat : morphism ≫ fh.frobeniusForm = fh.frobeniusForm
  /-- **Substrate perturbation**: the induced shift `δq`. -/
  substrate_shift : (𝟙_ C) ⟶ (𝟙_ C)

/-! ### Archimedean observation -/

/-- **Archimedean observation**: concrete realisation on a CR manifold.
    LaTeX: `\label{rem:observation-archimedean}` -/
structure ArchimedeanObservation (cqou : CQuantumObservableUniverse) where
  /-- Global sections `Γ(S)` of the state bundle. -/
  StateSections : Type*
  /-- The observation map `obs : Γ(S) → ℝ`. -/
  obs : StateSections → ℝ
  /-- Gauge equivalence relation. -/
  gaugeEquiv : StateSections → StateSections → Prop
  /-- `obs` is constant on gauge-equivalence classes. -/
  obs_gauge_invariant : ∀ s₁ s₂, gaugeEquiv s₁ s₂ → obs s₁ = obs s₂
  /-- All sections are gauge-equivalent (from observability). -/
  obs_well_defined : ∀ s₁ s₂, gaugeEquiv s₁ s₂


/-! ### Removed 2026-08-30 — self-assuming projections

- `fiber_adjoint_involution_sq` — body was `fai.involution_sq`: the conclusion was the projected field
  verbatim, so the declaration restated its own hypothesis.

**Why removal.** The content stays in the class field each declaration
projected, which asserts the same proposition under the same hypotheses; only
the restatement goes. That is the vacuity ledger's recorded disposition for
this category — *"drop the pseudo-theorem and project the field at use sites"*
— and there were no use sites: each had **zero references anywhere in the
corpus**, including in this file. Bean `qou-z9ws`.
-/

end QOU
