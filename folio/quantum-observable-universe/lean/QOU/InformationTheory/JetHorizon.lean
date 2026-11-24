import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Basic

/-!
# QOU.JetHorizon — Jet horizon, aeons, and CCC

A jet horizon is a closed boundary in an affine chart where the
degree-0 algebra A_0 vanishes.  No fibre-value data (photon identity)
crosses the horizon, but higher-degree jet data (winding, curvature)
can leak through.

The observable subcategory Bun°(P(V)) is the full subcategory where
A_0 ≠ 0.  Its connected components are the aeons.  The horizon functor
∂ sends each aeon to its boundary; the CMB functor extracts the
degree ≥ 1 data at the boundary.  A QOU admitting a chain of adjacent
aeons satisfies the three axioms of Penrose's CCC.

LaTeX labels: `def:jet-horizon`, `def:big-bang-state`, `def:aeon`,
  `def:cmb-boundary-datum`, `def:observable-subcategory`,
  `def:horizon-functor`, `def:cmb-functor`,
  `conj:aeon-boundary-generates-chart`,
  `prop:horizon-conformal-invariance`, `prop:qou-is-ccc`

## References

- [hawking1975] https://doi.org/10.1007/BF02345020
- [bekenstein1973] https://doi.org/10.1103/PhysRevD.7.2333
- [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
- [leitner2026] §9
-/

namespace QOU

/-! ## Graded jet algebra (abstract interface)

    We model the brane tower A_0 ↪ A_1 ↪ A_2 ↪ ⋯ as a graded
    type family indexed by jet degree. -/

/-- A graded jet algebra: type family indexed by degree k ∈ ℕ,
    with sections at each degree. -/
structure GradedJetAlgebra where
  /-- The type of sections at degree k. -/
  sections : ℕ → Type*
  /-- The zero section at each degree. -/
  zero : ∀ k, sections k
  /-- Inclusion A_k ↪ A_{k+1}. -/
  inclusion : ∀ k, sections k → sections (k + 1)

/-! ## Jet horizon -/

/-- A jet horizon in an affine chart: a locus where the degree-0
    algebra A_0 vanishes.  The horizon ideal h ⊂ Γ(U, A_0) blocks
    all zeroth-order sections; higher-degree jet data (A_k/A_0 for
    k ≥ 1) can carry non-trivial sections across the horizon. -/
-- Ref: [hawking1975] Particle creation by black holes — see folio/schema/references.ts
-- Ref: [leitner2026] §9/jet-horizon
structure JetHorizon where
  /-- The graded jet algebra over the chart. -/
  algebra : GradedJetAlgebra
  /-- At the horizon, every degree-0 section equals zero. -/
  degree_zero_vanishes : ∀ (s : algebra.sections 0), s = algebra.zero 0
  /-- There exists a non-trivial degree-1 section at the horizon. -/
  degree_one_leaks : ∃ (s : algebra.sections 1), s ≠ algebra.zero 1
  /-- There exists a non-trivial degree-2 section at the horizon. -/
  degree_two_leaks : ∃ (s : algebra.sections 2), s ≠ algebra.zero 2

/-- A big bang state: a bundle initial condition where A_0 = 0.
    Algebraically identical to a jet horizon but used as a
    reference configuration rather than a boundary.

    Existence is not assumed: whether any affine chart admits
    a big bang state is a dynamical question. -/
-- Ref: [leitner2026] §9/big-bang-state
structure BigBangState extends JetHorizon where
  /-- Number of base points in the initial configuration. -/
  numBasePoints : ℕ
  /-- At least one base point. -/
  nonempty : numBasePoints ≥ 1

/-- The CMB (cosmic microwave background) of a big bang state:
    the degree ≥ 1 jet data that survives the degree-0 vanishing. -/
-- Ref: [leitner2026] §9/cmb-boundary-datum
structure CMBBoundaryDatum where
  /-- The big bang state whose CMB this is. -/
  source : BigBangState
  /-- A non-trivial degree-1 section (winding mode). -/
  degree_one_witness : source.algebra.sections 1
  /-- The degree-1 section is non-trivial. -/
  degree_one_nontrivial : degree_one_witness ≠ source.algebra.zero 1
  /-- A non-trivial degree-2 section (curvature mode). -/
  degree_two_witness : source.algebra.sections 2
  /-- The degree-2 section is non-trivial. -/
  degree_two_nontrivial : degree_two_witness ≠ source.algebra.zero 2

/-! ## Observable subcategory and aeons -/

/-- The observable subcategory Bun°(P(V)): configurations where
    the degree-0 algebra is non-trivial (Frobenius pairing
    non-degenerate on A_0). -/
-- Ref: [leitner2026] §9/observable-subcategory
structure ObservableConfig where
  /-- The graded jet algebra. -/
  algebra : GradedJetAlgebra
  /-- There exists a non-trivial degree-0 section. -/
  degree_zero_nontrivial : ∃ (s : algebra.sections 0), s ≠ algebra.zero 0

/-- An aeon: a connected component of the observable subcategory
    Bun°(P(V)).  Maximal collection of observable configurations
    connected by flow maps without crossing a jet horizon. -/
-- Ref: [leitner2026] §9/aeon
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
structure Aeon where
  /-- The observable configurations in this aeon. -/
  configs : Type*
  /-- Each configuration is observable. -/
  observable : configs → ObservableConfig
  /-- A relation witnessing that two configs are connected by a
      flow map (one Planck step) within Bun°. -/
  flow_step : configs → configs → Prop
  /-- The flow relation is symmetric (reversible computation). -/
  flow_symm : ∀ x y, flow_step x y → flow_step y x
  /-- Connectedness: any two configs are related by a chain of
      flow steps.  This is the transitive closure of flow_step. -/
  connected : ∀ (x y : configs),
    ∃ (path : List configs),
      path.head? = some x ∧ path.getLast? = some y ∧
      ∀ i : Fin (path.length - 1),
        flow_step (path.get ⟨i, by omega⟩) (path.get ⟨i + 1, by omega⟩)
  /-- Boundary: jet horizons reachable as limits of directed
      diagrams in the aeon. -/
  boundary : List JetHorizon

/-- Two aeons are adjacent if their boundaries share a common
    jet horizon: ∂𝒜₁ ∩ ∂𝒜₂ ≠ ∅. -/
def adjacent (a₁ a₂ : Aeon) : Prop :=
  ∃ h, h ∈ a₁.boundary ∧ h ∈ a₂.boundary

/-! ## Horizon functor and CMB functor -/

/-- The horizon functor: sends an aeon to its boundary. -/
-- Ref: [leitner2026] §9/horizon-functor
def horizonFunctor (a : Aeon) : List JetHorizon := a.boundary

/-- The CMB functor value: the degree ≥ 1 data surviving a
    boundary horizon. Composition of ∂ with the colimit of
    (A_1/A_0 ⊕ A_2/A_0) over the boundary. -/
-- Ref: [leitner2026] §9/cmb-functor
structure CMBFunctorValue where
  /-- The source aeon. -/
  source : Aeon
  /-- The boundary horizon from which CMB data is extracted. -/
  horizon : JetHorizon
  /-- The horizon is in the aeon's boundary. -/
  in_boundary : horizon ∈ source.boundary
  /-- The CMB data at this horizon. -/
  cmb : CMBBoundaryDatum
  /-- The CMB's algebra matches the horizon's algebra. -/
  algebra_match : cmb.source.algebra = horizon.algebra

/-! ## Aeon recycling conjecture -/

/-- The result of applying one Planck step to CMB data:
    a new graded jet algebra (the next aeon's algebra) that has
    non-trivial degree-0 sections regenerated from the degree-1 CMB data. -/
structure PlanckStepResult where
  /-- The new graded jet algebra after the Planck step. -/
  next_algebra : GradedJetAlgebra
  /-- The new algebra has non-trivial degree-0 sections. -/
  degree_zero_regenerated : ∃ (s : next_algebra.sections 0), s ≠ next_algebra.zero 0
  /-- The degree-1 data is inherited from the CMB. -/
  degree_one_inherited : ∃ (s : next_algebra.sections 1), s ≠ next_algebra.zero 1

/-! ## Aeon recycling

    **The conjecture, and why it is NOT an axiom here.**

    The conjecture (Penrose CCC recycling): the first Planck step `Φ₁`
    applied to the CMB of an aeon produces a **new** graded jet algebra with
    non-trivial degree-0 sections, distinct from the horizon's algebra (where
    degree-0 vanishes by definition).  If it holds for all aeons it extends to
    a recycling functor `R : π₀(Bun°) → π₀(Bun°)`, whose fixed points are the
    self-recycling aeons.

    **This file used to carry that as `axiom aeon_recycling (cmb :
    CMBFunctorValue) : PlanckStepResult`.  Removed 2026-09-05: that axiom was
    VACUOUS — it asserted nothing about the conjecture.**  Two measurements,
    both machine-checked immediately below:

    * `planckStepResult_nonempty` — `PlanckStepResult` is inhabited outright,
      by a toy algebra (`ULift Bool` at every degree).  The removed axiom's
      own note claimed `opaque` was unavailable because `Nonempty
      PlanckStepResult` "cannot be witnessed without proving the conjecture
      itself".  That is a category error: inhabiting the *result type* asks
      whether **some** algebra has non-zero degree-0 and degree-1 sections,
      not whether the Planck step produces one.
    * `planckStepResult_cmb_independent` — decisively, the axiom's result type
      **never mentions `cmb`**.  So its statement is discharged by a constant
      function, and the two `∃ s, s ≠ 0` fields are satisfied by a toy.  It
      was true, and true for reasons having nothing to do with aeons.

    **The conjecture is not statable in this formalisation yet**, and that —
    not the choice of `axiom` versus `opaque` — is the real gap: there is no
    Planck-step map in the file.  `Φ₁` occurs only in prose.  Until some
    `Φ : CMBFunctorValue → GradedJetAlgebra` is defined, any Lean statement
    "about" it is satisfiable by choosing `Φ` to be the toy, so a
    content-bearing carrier (§3b-tax) cannot be written either.

    Note this is the `weierstrass_diff_eq_axiom` failure mode recorded in bean
    `qou-i6cn` — *"an axiom that does not mention the object it claims to
    constrain"* — and the citation was sound throughout: the intent was right,
    the Lean did not match it.  A correct `-- Ref:` says nothing about whether
    the statement has content.

    Ref: [leitner2026] §9/aeon-boundary-generates-chart
    Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010. -/

/-- A toy graded jet algebra — `ULift Bool` at every degree, zero is `false`.
    Exists only as the witness for the two vacuity theorems below. -/
def toyGradedJetAlgebra : GradedJetAlgebra where
  sections := fun _ => ULift Bool
  zero := fun _ => ULift.up false
  inclusion := fun _ b => b

/-- `PlanckStepResult` is inhabited, with no appeal to the recycling
    conjecture.  Refutes the removed axiom's stated justification. -/
theorem planckStepResult_nonempty : Nonempty PlanckStepResult :=
  ⟨{ next_algebra := toyGradedJetAlgebra
   , degree_zero_regenerated := ⟨ULift.up true, by simp [toyGradedJetAlgebra]⟩
   , degree_one_inherited := ⟨ULift.up true, by simp [toyGradedJetAlgebra]⟩ }⟩

/-- **The removed axiom's statement, discharged — and shown to ignore its
    own argument.**  `fun _ => toyResult` has exactly the type the axiom had,
    and it returns the same result for any two CMB inputs.  Any future
    statement of aeon recycling must constrain a Planck-step map; a bare
    `CMBFunctorValue → PlanckStepResult` carries no content. -/
theorem planckStepResult_cmb_independent :
    ∃ f : CMBFunctorValue → PlanckStepResult, ∀ c₁ c₂, f c₁ = f c₂ :=
  ⟨fun _ => { next_algebra := toyGradedJetAlgebra
            , degree_zero_regenerated :=
                ⟨ULift.up true, by simp [toyGradedJetAlgebra]⟩
            , degree_one_inherited :=
                ⟨ULift.up true, by simp [toyGradedJetAlgebra]⟩ },
   fun _ _ => rfl⟩

/-! ## Conformal invariance at the horizon -/

/-- **Degree-0 vanishing at the jet horizon** — the algebraic
    precondition underlying `prop:horizon-conformal-invariance`.

    Every degree-0 section vanishes at a jet horizon, by the
    `JetHorizon.degree_zero_vanishes` field.  This is the direct
    statement provable from the abstract `JetHorizon` interface.

    The full conformal-invariance consequence stated in the .md
    narrative — that the boundary datum
    `(A_1 / A_0, A_2 / A_0)|_{H}` is invariant under rescaling
    `A_0 ↦ λ A_0` for any unit `λ` on the horizon — follows
    because the quotient `A_k / λ A_0` depends only on the
    ideal generated by vanishing degree-0 sections (i.e. on
    the *vanishing locus*, not on the specific generator).
    Stating that consequence formally requires a `Module` /
    quotient structure on each `A_k` that the abstract
    `JetHorizon` interface does not (yet) carry; see the .md
    narrative for the categorical proof sketch. -/
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
-- Ref: [leitner2026] §9/horizon-conformal-invariance
theorem horizon_conformal_invariance
    (H : JetHorizon)
    (s : H.algebra.sections 0)
    : s = H.algebra.zero 0 := by
  exact H.degree_zero_vanishes s

/-! ## QOU is CCC -/

/-- **CCC property 1**: at each horizon, all degree-0 sections vanish. -/
theorem ccc_conformal_invariance (H : JetHorizon) (s : H.algebra.sections 0) :
    s = H.algebra.zero 0 :=
  H.degree_zero_vanishes s

/-- **CCC property 2**: at each horizon, degree ≥ 1 data persists. -/
theorem ccc_boundary_data_exists (H : JetHorizon) :
    (∃ s, s ≠ H.algebra.zero 1) ∧ (∃ s, s ≠ H.algebra.zero 2) :=
  ⟨H.degree_one_leaks, H.degree_two_leaks⟩

/-- **QOU is CCC — horizon-local form.**

    At any jet horizon, the three horizon-local CCC properties
    hold: degree-0 sections vanish, and non-trivial degree-1
    and degree-2 sections persist.  This is the
    `prop:qou-is-ccc` content that follows from the
    `JetHorizon` structure axioms alone (CCC-1 and CCC-3 of
    the .md narrative).

    Note (PR #776): the *full* `prop:qou-is-ccc` claim in the
    narrative also asserts **CCC-2 — boundary-data
    inheritance** (the CMB of an aeon equals the terminal
    boundary datum of its adjacent predecessor; see
    `def:cmb-boundary-datum` and `def:aeon` adjacency).  That
    piece requires a CMB-of-aeon construction beyond
    `JetHorizon`'s field structure and is not yet formalised
    here — the `(chain, h_adj, hH)` hypotheses of the previous
    formulation were unused (Copilot, PR #776).  Tracking the
    CCC-2 piece as conditional-class follow-up work. -/
-- Ref: [penrose2010] R. Penrose, "Cycles of Time", Bodley Head 2010.
-- Ref: [leitner2026] §9/qou-is-ccc
theorem qou_is_ccc (H : JetHorizon) :
    -- CCC-1: degree-0 vanishes
    (∀ s, s = H.algebra.zero 0) ∧
    -- CCC-3: degree ≥ 1 persists
    (∃ s, s ≠ H.algebra.zero 1) ∧
    (∃ s, s ≠ H.algebra.zero 2) :=
  ⟨H.degree_zero_vanishes, H.degree_one_leaks, H.degree_two_leaks⟩

end QOU
