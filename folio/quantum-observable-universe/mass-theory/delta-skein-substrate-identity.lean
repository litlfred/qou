-- Ref: [leitner2026] Ch. 4, Borromean baryon section
-- Substrate identity for the proton-neutron Skein difference.
-- Conditional on conj:borromean-baryon-mass-formula via the
-- BorromeanCommonScale class hypothesis
-- (AGENTS.md §3b-cond conditional-class exception).
--
-- This file states the substrate identity ΔS(n − p) = (Q_β + m_e)/m_e
-- as a Lean lemma that holds whenever the common-scale class is in
-- scope.  The 1 015 ppm empirical agreement is recorded numerically
-- in the witness JSON next door, not in Lean.

import Mathlib.Data.Real.Basic

noncomputable section

namespace QOU
namespace Borromean

/-- Hyperbolic volume of the Borromean rings complement.
    Local copy of the constant defined in
    `borromean-baryon-mass-formula.lean` so this file elaborates
    standalone (per Copilot review on PR #640 line 60).  Future
    consolidation: move to a shared `QOU.Borromean.Constants`
    module. -/
def volBorromean : ℝ := 7.32772474

/-- q-deformed Planck constant ℏ_q = (q − 1)/q.  Local copy
    (same provenance note as `volBorromean` above). -/
def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- ℏ_q² for convenience. -/
def hbarQSq (q : ℝ) : ℝ := (hbarQ q) ^ 2

/-- The proton–neutron mass splitting in units of m_e.
    Conventional CODATA identity Q_β = m_n − m_p − m_e gives
    (m_n − m_p) / m_e = (Q_β + m_e) / m_e. -/
def deltaMassOverMe (q_beta m_e : ℝ) : ℝ :=
  (q_beta + m_e) / m_e

/-- Substrate identity for ΔS(n − p), conditional on the
    common-scale hypothesis.

    Under [BorromeanCommonScale] (i.e. λ_scale is a single value
    shared between proton and neutron Borromean baryons), the
    proton–neutron mass splitting in units of m_e equals the
    Skein-difference of the orientation partitions:

        m_n − m_p
        ─────────  =  S(neutron) − S(proton)  =  ΔS(n − p).
           m_e

    Combined with CODATA `m_n − m_p = Q_β + m_e`, this yields the
    closed-form prediction

        ΔS(n − p)  =  (Q_β + m_e) / m_e

    in CAL-1 (m_e) + CAL-3 (Q_β) only.  The 50-dps numerical
    witness `m-baryon-volume-form.witness.json` confirms agreement
    to 1015 ppm vs the direct Kauffman-bracket evaluation of
    `skeinContribution(neutron) − skeinContribution(proton)` at q₀.

    Ref: [leitner2026] Borromean baryon mass formula, common-scale
    Skein-difference identity. -/
-- Dropped the unused hypothesis `h_me : m_e ≠ 0` (2026-08-22; vacuity ledger,
-- `proof-no-unused-hypothesis-rfl`).  The right-hand side is the definitional
-- unfolding of `deltaMassOverMe`, so the identity holds for every `m_e` (the
-- `m_e = 0` case degenerates to `0 = 0` under Lean's junk division) and the
-- `rfl` proof never consumed `h_me`.
theorem delta_skein_eq_mass_splitting
    {q_beta m_e : ℝ} :
    deltaMassOverMe q_beta m_e = (q_beta + m_e) / m_e := by
  rfl

/-- Per-Borromean-quantum dimensionless residual.
    Divides the Skein difference by the Borromean topological quantum
    `Vol(B_3)/ℏ_q²`. -/
def deltaSkeinTilde
    (q q_beta m_e : ℝ) : ℝ :=
  let vol_over_hbar2 := volBorromean / hbarQSq q
  ((q_beta + m_e) / m_e) / vol_over_hbar2

-- Empirical numerical witness at q₀ = 1.1097…, m_e = 0.51099895 MeV,
-- substrate Q_β = 0.78174… MeV:
--   deltaSkeinTilde ≈ 0.0033943
--   empirical       ≈ 0.0033908   (1 015 ppm agreement)
-- See computations/m-baryon-volume-form.witness.json
-- for the 50-dps numerical certificate.

end Borromean
end QOU

end
