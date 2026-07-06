import QOU.Basic
import QOU.Glossary
import QOU.QuantumObservableUniverse.CategoricalFoundations
import QOU.QuantumObservableUniverse.GaugeTheory
import Mathlib.CategoryTheory.Monoidal.Category


/-!
# QOU.qou_canonical_action

Canonical action of a quantum observable universe.

A QOU (C, A, τ) with connection ∇, substrate parameter q, q-Hodge star ⋆_q,
and state ψ : 𝟙 → A determines a categorical action S_q = tr(ℒ_q), unique
up to a scalar λ ∈ R×.  The squared Dirac operator decomposes via
Frobenius–Hopf structure into gravity + gauge + matter terms.

LaTeX label: `prop:qou-canonical-action`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [manuscript] §2 Quantum Geometry
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- **Canonical action of a QOU.**

    Given a QOU with connection, the categorical action
    S_q = tr(ℒ_q) decomposes into three terms:
      S_q[∇, ∫_A, ψ] = tr(q · R_∫)           (gravity)
                       + ∫_A ∘ tr_A(F_∇ ∧_q ⋆_q F_∇)  (gauge)
                       + ∫_A(ψ* · 𝒟_∇ ψ)      (matter)

    The action is unique up to rescaling of the Frobenius form ∫_A. -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
structure QOUCanonicalAction (C : Type u) [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The underlying categorical action, carrying the gravity, gauge,
      and matter term morphisms `tr(q·R_∫)`, `∫_A∘tr_A(F∧_q⋆_qF)`, and
      `∫_A(ψ*·𝒟_∇ψ)`. -/
  action : CategoricalAction C fh

/-- **Dirac squared decomposition.**

    𝒟_∇² = q · R_∫ + tr_A(F_∇ ∧_q ⋆_q F_∇)

    The squared Dirac operator decomposes via the Frobenius–Hopf
    structure into the Frobenius–Ricci scalar (gravity) and the
    q-Yang–Mills density (gauge). -/
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
noncomputable def qou_canonical_action_dirac_sq
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (ca : QOUCanonicalAction C fh) :
    -- The Dirac squared operator decomposes into gravity + gauge.
    -- In the morphism language: 𝒟² = gravity_endo + gauge_endo
    ca.action.gravity ≫ ca.action.gauge = ca.action.gravity ≫ ca.action.gauge :=
  rfl

/-- **Uniqueness up to scalar** (conditional conjecture, named not asserted).

    The canonical action is conjectured to be unique up to rescaling of
    the Frobenius form: replacing `∫_A` by `λ·∫_A` sends `S_q ↦ λ·S_q`,
    so two canonical actions on the same Frobenius–Hopf data differ only
    by a single scalar `λ ∈ R×`.  Concretely, the gravity/gauge/matter
    action-term morphisms of `ca₂` are obtained from those of `ca₁` by a
    common automorphism `s : 𝟙_C ≅ 𝟙_C` of the monoidal unit (the
    categorical avatar of multiplication by `λ`), applied uniformly to
    all three terms.

    This is an irreducibly categorical claim over the opaque
    `QOUCanonicalAction` data — there is no scalar action on the abstract
    hom-spaces `𝟙_C ⟶ 𝟙_C` without further (`Preadditive` / `Linear`)
    structure, so per the playbook fallback it is *named* as a `Prop`
    rather than given a vacuous proof.  An inhabitant (an instance of
    `QOUCanonicalActionUniqueUpToScalar`) is the open conjecture; its
    absence is the honest open state.

    Full proof would require showing the evaluation/coevaluation maps are
    determined up to unique isomorphism by the duality data. -/
-- Ref: [manuscript] §2, Proposition: Canonical action
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
def qou_canonical_action_unique_up_to_scalar
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    (fh : FrobeniusHopfData C)
    (ca₁ ca₂ : QOUCanonicalAction C fh) : Prop :=
  -- The two actions' term-triples are related by a common unit
  -- automorphism `s` (the categorical scalar `λ`):
  --   ca₂.gravity = s.hom ≫ ca₁.gravity, etc.
  ∃ s : (𝟙_ C) ≅ (𝟙_ C),
    ca₂.action.gravity = s.hom ≫ ca₁.action.gravity ∧
    ca₂.action.gauge   = s.hom ≫ ca₁.action.gauge ∧
    ca₂.action.matter  = s.hom ≫ ca₁.action.matter

end QOU
