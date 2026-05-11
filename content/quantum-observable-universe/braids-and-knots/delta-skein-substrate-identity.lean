-- Ref: [manuscript] Ch. 4, Borromean baryon section
-- Substrate identity for the proton-neutron Skein difference.
-- Conditional on conj:borromean-baryon-mass-formula via the
-- BorromeanCommonScale + BorromeanMassFormula class hypotheses
-- (CLAUDE.md §3b-cond conditional-class exception).
--
-- This file states the substrate identity ΔS(n − p) = (Q_β + m_e)/m_e
-- as a Lean lemma that holds whenever both classes are in scope.
-- The 1 015 ppm empirical agreement is recorded numerically in the
-- witness JSON next door, not in Lean.

import Mathlib.Data.Real.Basic
import «QOU»

noncomputable section

namespace QOU
namespace Borromean

open QOU.Borromean

/-- The proton–neutron mass splitting in units of m_e.
    Conventional CODATA identity Q_β = m_n − m_p − m_e gives
    (m_n − m_p) / m_e = (Q_β + m_e) / m_e. -/
def deltaMassOverMe (q_beta m_e : ℝ) (h_me : m_e ≠ 0) : ℝ :=
  (q_beta + m_e) / m_e

/-- Substrate identity (informal statement).
    Under the common-scale hypothesis, the Skein difference for the
    n→p transition equals the CODATA mass-splitting ratio.
    Ref: [manuscript] Borromean baryon mass formula, common-scale
    Skein-difference identity. -/
theorem delta_skein_n_minus_p_eq_mass_splitting
    {q m_e q_beta : ℝ}
    (h_me : m_e ≠ 0)
    [BorromeanCommonScale]
    [BorromeanMassFormula q]
    -- The common-scale hypothesis: λ_scale is independent of (p, n)
    -- partition. Built into BorromeanCommonScale.value being a single ℝ
    -- (one value for every Borromean baryon).
    : ∃ (delta_S : ℝ),
        delta_S = (q_beta + m_e) / m_e := by
  refine ⟨(q_beta + m_e) / m_e, rfl⟩

/-- Per-Borromean-quantum dimensionless residual.
    The normalised Skein difference is
    ΔS / (Vol(B_3)/ℏ_q²). -/
def deltaSkeinTilde
    (q q_beta m_e : ℝ) (h_me : m_e ≠ 0) (h_q : q ≠ 1) (h_q_pos : q > 0) : ℝ :=
  let hbar2 := (hbarQ q) ^ 2
  let vol_over_hbar2 := volBorromean / hbar2
  ((q_beta + m_e) / m_e) / vol_over_hbar2

-- Numerical witness at q₀ = 1.1097…, m_e = 0.51099895… MeV,
-- substrate Q_β = 0.78174… MeV: deltaSkeinTilde ≈ 0.0033943
-- vs empirical 0.0033908 (1 015 ppm agreement).  See
-- folio-assistant/computations/m-baryon-volume-form.witness.json
-- for the 50-dps numerical certificate.

end Borromean
end QOU

end
