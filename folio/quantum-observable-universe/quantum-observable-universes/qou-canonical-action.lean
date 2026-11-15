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
up to a scalar λ ∈ R×, with gravity, gauge and matter terms.  (The
Dirac-squared decomposition is not stated here; see the note below.)

LaTeX label: `prop:qou-canonical-action`

## References

- [kock2004] https://doi.org/10.1017/CBO9780511615443
- [leitner2026] §2 Quantum Geometry
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
    [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C) where
  /-- The underlying categorical action, carrying the gravity, gauge,
      and matter term morphisms `tr(q·R_∫)`, `∫_A∘tr_A(F∧_q⋆_qF)`, and
      `∫_A(ψ*·𝒟_∇ψ)`. -/
  action : CategoricalAction C fh

/-! **The former `qou_canonical_action_dirac_sq` was vacuous** (removed
    2026-11-15). Its docstring claimed `𝒟_∇² = q · R_∫ + tr_A(F_∇ ∧_q ⋆_q F_∇)`,
    but its type was `x = x` (`gravity ≫ gauge = gravity ≫ gauge := rfl`).
    `CategoricalAction` carries no Dirac operator, so the identity cannot be
    stated yet. A real statement needs `𝒟_∇` as data. Recorded as open in bean
    `qou-n2un`. -/

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
    determined up to unique isomorphism by the duality data.

    **Composition side, 2026-09-15 (`qou-h0ou`).**  `s` was applied by
    *pre*-composition (`s.hom ≫ ca₁.action.gravity`).  That stopped
    typechecking when `CategoricalAction.gravity` was retyped to the rank-2
    pairing space `fh.obj ⊗ fh.obj ⟶ 𝟙_ C`: `s.hom` ends at `𝟙_ C`, which is
    no longer where `gravity` begins.

    It is now applied by *post*-composition, uniformly to all three terms.
    That is the side this docstring's own account of the rescaling asks for:
    the claim is that replacing `∫_A` by `λ·∫_A` sends `S_q ↦ λ·S_q`, and the
    Frobenius form is the **last** map into the unit in each term, so
    rescaling it composes on the right.  The uniformity the paragraph above
    promises ("applied uniformly to all three terms") is preserved — for the
    two terms that are already endomorphisms of `𝟙_ C` the two sides agree in
    any case, since `End(𝟙_C)` is commutative in a monoidal category, though
    nothing here needs or asserts that. -/
-- Ref: [leitner2026] §2, Proposition: Canonical action
-- Ref: [kock2004] Kock, "Frobenius Algebras and 2D Topological Quantum Field Theories," CUP LMS Student Texts 59, 2004
def qou_canonical_action_unique_up_to_scalar
    {C : Type u} [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.BraidedCategory C]
    (fh : FrobeniusHopfData C)
    (ca₁ ca₂ : QOUCanonicalAction C fh) : Prop :=
  -- The two actions' term-triples are related by a common unit
  -- automorphism `s` (the categorical scalar `λ`), applied on the side the
  -- Frobenius form sits on:
  --   ca₂.gravity = ca₁.gravity ≫ s.hom, etc.
  ∃ s : (𝟙_ C) ≅ (𝟙_ C),
    ca₂.action.gravity = ca₁.action.gravity ≫ s.hom ∧
    ca₂.action.gauge   = ca₁.action.gauge ≫ s.hom ∧
    ca₂.action.matter  = ca₁.action.matter ≫ s.hom

end QOU
