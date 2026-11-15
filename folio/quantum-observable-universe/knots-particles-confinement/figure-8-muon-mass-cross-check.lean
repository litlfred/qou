-- Ref: [leitner2026] Ch. 4, CAL-2 numerical cross-check.
-- Verifies Vol(4_1) / ℏ_q² = m_μ / m_e at 50 dps.
--
-- The Lean statement records the formal identity; the 50-dps
-- numerical certificate lives in the witness JSON beside the
-- compute script.  In the Vol-form mass framework, the figure-8
-- (muon) sector is the degenerate limit of the Borromean (baryon)
-- formula with λ_scale = 1 and S = 0.

import Mathlib.Data.Real.Basic

noncomputable section

namespace QOU
namespace MuonVolForm

/-- Hyperbolic volume of the figure-8 knot complement
    `Vol(4_1) = 2 · Cl₂(π/3)` (Thurston / SnapPy). -/
def vol_4_1 : ℝ := 2.0298832128

/-- q-deformed Planck constant ℏ_q = (q − 1)/q. -/
def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- ℏ_q² for convenience. -/
def hbarQSq (q : ℝ) : ℝ := (hbarQ q) ^ 2

/-- The muon-to-electron mass ratio in the Vol-form ansatz.

    With λ_scale = 1 (no scaling) and S(4_1) = 0 (orientation
    trivial), the topological-mass formula
    `m_μ / m_e = Vol(K)/ℏ_q² · λ + S` reduces to
    `m_μ / m_e = Vol(4_1) / ℏ_q²`. -/
def muonRatioFromVol (q : ℝ) : ℝ :=
  vol_4_1 / hbarQSq q

/-- CAL-2 substrate identity (forward direction).

    The CAL-2 calibration defines q₀ as the unique real solution of
    `m_μ/m_e = Vol(4_1)/ℏ_q²`.  Evaluating both sides at q₀
    therefore gives equality by construction; the witness records
    the 50-dps numerical match to 1.45 × 10⁻³⁰ ppm.

    Ref: [leitner2026] CAL-2 in three-calibration-inputs. -/
theorem cal2_identity_pinned
    {q m_mu m_e : ℝ}
    (h_cal2 : m_mu / m_e = muonRatioFromVol q) :
    muonRatioFromVol q = m_mu / m_e := by
  exact h_cal2.symm

/-- Definitional form of the Vol-form muon ratio: `muonRatioFromVol q` is
    `Vol(4_1) / ℏ_q²` (the degenerate Borromean limit `λ_scale = 1`, `S = 0`).

    A definitional unfolding of `muonRatioFromVol`: the previous
    `muon_ratio_is_topological (q) (h_q_ne_one : q ≠ 1) : … := rfl` carried an
    **unused** `q ≠ 1` and a docstring claiming a reduction it did not derive.
    The substantive CAL-2 content is `cal2_identity_pinned` above.

    Ref: [leitner2026] figure-8 as Vol-form anchor. -/
theorem muonRatioFromVol_eq_vol_form (q : ℝ) :
    muonRatioFromVol q = vol_4_1 / hbarQSq q := by
  rfl

-- Numerical witness at q₀ = 1.1097…:
--   Vol(4_1) / ℏ_q²       = 206.7682830…
--   CODATA m_μ/m_e        = 206.7682830…
--   relative residual     = 1.45 × 10⁻³⁰ ppm
-- See computations/m-baryon-volume-form.witness.json.

end MuonVolForm
end QOU

end
