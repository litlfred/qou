import Mathlib.Algebra.Field.Defs
import Mathlib.Analysis.Complex.Basic


/-!
# QOU.BraidKnot.ImQPhysicalRole

Conjectural physical role of Im(q): a substrate moduli parameter
without current observable, three candidate roles (chirality,
phase-dual-to-CAL-2, non-Hermitian deformation).

Ref: [manuscript] conj:im-q-physical-role
Ref: [manuscript] rem:im-q-vs-p-skew

Generic statement: there exists no current QOU observable that
distinguishes Im(q) ≠ 0 from Im(q) = 0 at leading order under the
modulus projection.
-/

namespace QOU.BraidKnot.ImQPhysicalRole

/-- The default substrate convention sets Im(q) = 0. -/
noncomputable def default_q_real (q_real : ℝ) : ℂ := (q_real : ℂ)

/-- Under modulus projection (categorical mass formula), a mass
    observable `m(q) = |F(q)|` is invariant under q ↦ q̄ (complex
    conjugation) for any conjugation-equivariant `F` — in particular
    for a real-coefficient polynomial (e.g. the Markov trace), where
    `F(q̄) = F(q)̄` holds and is supplied here as the hypothesis `hF`. -/
-- Ref: [manuscript] conj:im-q-physical-role
theorem mass_observable_conj_invariance
    {F : ℂ → ℂ} (q : ℂ)
    (hF : F (starRingEnd ℂ q) = starRingEnd ℂ (F q)) :
    ‖F (starRingEnd ℂ q)‖ = ‖F q‖ := by
  rw [hF]
  exact Complex.norm_conj (F q)

/-- Three candidate roles for Im(q), enumerated for audit visibility. -/
inductive ImQCandidateRole
  | chirality_orientation
  | phase_dual_to_cal2
  | non_hermitian_deformation

/-- Conjecture: at most one candidate role is the physical
    interpretation; the framework currently does not pick one. -/
def im_q_observable_pairing (role : ImQCandidateRole) : Prop :=
  match role with
  | ImQCandidateRole.chirality_orientation     => True  -- pending CP-violation observable
  | ImQCandidateRole.phase_dual_to_cal2        => True  -- pending second independent CAL-2-like constraint
  | ImQCandidateRole.non_hermitian_deformation => True  -- pending categorical Γ (decay width) formula

end QOU.BraidKnot.ImQPhysicalRole
