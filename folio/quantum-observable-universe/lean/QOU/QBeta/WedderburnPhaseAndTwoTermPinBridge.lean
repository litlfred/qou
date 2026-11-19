import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Tactic.Positivity
import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

/-!
# Convention-D Wedderburn Phase Bridge, Jucys–Murphy Content Moments, and Two-Term Proton Pin (`qou-q2oa`, `qou-cds1`, `qou-j1e5`)

This module establishes the algebraic and real-analytic identities connecting:
1. **Section 1 (`qou-q2oa` — True Convention-D Wedderburn Weight `w_{(2,1)}(z_D)` vs Retracted `1/2 - z_D`)**:
   * In `DecayLadderConventionDPositivity.lean`, the affine phase coefficient `1/2 - z_D` is
     strictly negative for `q > 1` (`1/2 - z_D = -(2 q^3 - q^2 - 1)/(2(q^2 + 1)) < 0`), whereas the true
     Convention-D middle Wedderburn weight from `NucleonIdempotentModifiedTrace.lean` is strictly positive:
     `w_{(2,1)}(z_D) = q^2 / (q^2 + 1)^2 > 0`.
   * Theorem `w21_zD_sub_retractedPhaseCoeff` establishes the rational gap
     `w_{(2,1)}(z_D) - (1/2 - z_D) = (2 q^5 - q^4 + 2 q^3 - 1) / (2 (q^2 + 1)^2)`,
     with strict positivity `retractedPhaseCoeff_lt_w21_zD` and non-equality `w21_zD_ne_retractedPhaseCoeff`
     for all real `q ≥ 1`, and theorem `wedderburnAffinePhaseD_sub_assertedPhaseD` gives the phase difference
     between substituting the true weight `w_{(2,1)}(z_D)` versus the retracted coefficient `1/2 - z_D`
     into the affine formula `-h/4 - (h/2) y`.

2. **Section 2 (`qou-q2oa` → `qou-cds1` — Jucys–Murphy Content Moments & Mirror-Covariant Bar-Odd Projected Phase)**:
   * On `H_3(q)`, the classical Jucys–Murphy content sums `(3, 0, -3)` on `((3), (2,1), (1^3))` have
     normalized per-strand content eigenvalues `(+1, 0, -1)`, coinciding identically with the normalized
     transposition characters `χ^λ(τ) / f^λ = (+1, 0, -1)`.
   * Theorems `jmContentMomentD_eq_three_mul_w3_zD`, `jmContentMeanD_eq_transpositionMomentD`, and
     `jmContentMeanD_eq_one_sub_two_w21_zD` show that the Convention-D Jucys–Murphy content mean equals the
     transposition moment `Ξ_D = w_{(3)}(z_D) = (q^4 + 1)/(q^2 + 1)^2 = 1 - 2 w_{(2,1)}(z_D)`, and
     `jmContentMeanGPMTPos_eq_div` gives the GPMT-completed content mean closed form.
   * Definition `mirrorProjectedPhaseD` captures the unique mirror-covariant bar-odd projected Convention-D phase
     `mirrorProjectedPhaseD q = (z_D - 1)(q - q⁻¹)/2 - (q - q⁻¹)^2 / 4`, with its Wedderburn
     `w_{(3)}(z_D)` and `w_{(2,1)}(z_D)` representations (`mirrorProjectedPhaseD_eq_w3_form`,
     `mirrorProjectedPhaseD_eq_w21_form`), factored rational form (`mirrorProjectedPhaseD_eq_div`),
     and bar-odd mirror symmetry (`mirrorProjectedPhaseD_inv`).

3. **Section 3 (Two-Term Proton Pin `q_{2t}`, `m_n - m_p` Residual Cancellation, and 4 Cartan QED Weightings)**:
   * Theorems `twoTerm_neutron_mass_residual_eq_qbeta_residual` and
     `bareCore_neutron_mass_residual_sub_proton_qed` establish that under the two-term proton pin
     `m_p^{QCD} + M_p^{QED,conn} = m_p^{exp}` and `m_n^{exp} = m_p^{exp} + m_e + Q_β^{exp}`, the consistent
     two-term neutron mass prediction `m_n^{2t} = (m_p^{QCD} + M_p^{QED,conn}) + m_e + (Q_β^{strong} + Δm_{QED}^{conn})`
     has residual identically equal to the two-term `Q_β` residual
     `(Q_β^{strong} + Δm_{QED}^{conn}) - Q_β^{exp}`, whereas omitting `M_p^{QED,conn}` from the proton core
     at `q_{2t}` shifts the neutron residual by `-M_p^{QED,conn}`.
   * Theorems `trConnBorromeanP_eq_one_third_trace_QAdjp`, `trConnBorromeanN_eq_one_third_trace_QAdjn_connected`,
     and `trConnDiffPlain_eq_one_third_trace_QAdj_connected_diff` bridge the per-strand connected rational traces
     directly to the 3×3 matrix traces in `NucleonWeightSpaceTwoTerm.lean`, followed by the closed-form
     differences between all 4 parameter-free Cartan QED weightings (`plain`, `KnKp`, `Kp3`, `q`).

Compute companion: `computations/qbeta/qbeta_wedderburn_phase_twoterm_pin_probe.py`
Witness: `computations/qbeta/qbeta-wedderburn-phase-twoterm-pin.witness.json`
-/

namespace QOU.QBeta.WedderburnPhaseAndTwoTermPinBridge

open Matrix
open QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.QBeta.CoshHolonomyAndGPMTBaseBridge

/-! ## Section 1: Discrepancy Between Retracted `1/2 - z_D` and True Wedderburn Weight `w_{(2,1)}(z_D)` -/

section RetractedVsTrueWedderburnWeight

variable {K : Type*} [Field K]

/-- The retracted non-Markov affine phase coefficient `κ(z) = 1/2 - z` from
`DecayLadderConventionDPositivity.lean`. -/
def retractedPhaseCoeff (z : K) : K := 1 / 2 - z

/-- At Convention D (`z_D = q^3 / (q^2 + 1)`), the retracted affine coefficient equals
`-(2 q^3 - q^2 - 1) / (2 (q^2 + 1))`. -/
theorem retractedPhaseCoeff_zD_eq_div (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    retractedPhaseCoeff (zD q) = -(2 * q ^ 3 - q ^ 2 - 1) / (2 * (q ^ 2 + 1)) := by
  unfold retractedPhaseCoeff zD
  field_simp
  ring

/-- **Exact Rational Gap Between True `w_{(2,1)}(z_D)` and Retracted `1/2 - z_D`**:
`w_{(2,1)}(z_D) - (1/2 - z_D) = (2 q^5 - q^4 + 2 q^3 - 1) / (2 (q^2 + 1)^2)`. -/
theorem w21_zD_sub_retractedPhaseCoeff (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    w21 q (zD q) - retractedPhaseCoeff (zD q) =
      (2 * q ^ 5 - q ^ 4 + 2 * q ^ 3 - 1) / (2 * (q ^ 2 + 1) ^ 2) := by
  rw [w21_conventionD q hq2 hq4, retractedPhaseCoeff_zD_eq_div q hq2 h2]
  field_simp
  ring

/-- Positivity decomposition of the numerator `2 q^5 - q^4 + 2 q^3 - 1` around `q = 1`:
`2 q^5 - q^4 + 2 q^3 - 1 = (q - 1)(2 q^4 + q^3 + 3 q^2 + 3 q + 3) + 2`. -/
theorem w21_sub_retracted_numerator_decomp (q : K) :
    2 * q ^ 5 - q ^ 4 + 2 * q ^ 3 - 1 =
      (q - 1) * (2 * q ^ 4 + q ^ 3 + 3 * q ^ 2 + 3 * q + 3) + 2 := by
  ring

/-- The asserted unprojected Convention-D ladder phase `α_D(q) = (z_D - 1)(q - q⁻¹) / 2`. -/
def assertedPhaseD (q : K) : K :=
  (zD q - 1) * (q - q⁻¹) / 2

/-- The direct Wedderburn affine phase obtained by substituting the true middle weight
`w_{(2,1)}(z_D)` in place of `1/2 - z_D` in `-h/4 - (h/2) y`. -/
def wedderburnAffinePhaseD (q : K) : K :=
  -(q - q⁻¹) / 4 - (q - q⁻¹) / 2 * w21 q (zD q)

/-- Exact algebraic rewrite of `assertedPhaseD` in affine form with `retractedPhaseCoeff (zD q)`:
`α_D(q) = -(q - q⁻¹)/4 - ((q - q⁻¹)/2) · (1/2 - z_D)`. -/
theorem assertedPhaseD_eq_affine_retracted (q : K) (h2 : (2 : K) ≠ 0) :
    assertedPhaseD q =
      -(q - q⁻¹) / 4 - (q - q⁻¹) / 2 * retractedPhaseCoeff (zD q) := by
  unfold assertedPhaseD retractedPhaseCoeff
  have h4 : (4 : K) = 2 * 2 := by ring
  rw [h4]
  field_simp
  ring

/-- **Exact Phase Shift from Substituting True `w_{(2,1)}(z_D)` into the Affine Formula**:
`α_{Wed,aff}^D(q) - α_D(q) = -(q - q⁻¹)(2 q^5 - q^4 + 2 q^3 - 1) / (4 (q^2 + 1)^2)`. -/
theorem wedderburnAffinePhaseD_sub_assertedPhaseD (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    wedderburnAffinePhaseD q - assertedPhaseD q =
      -(q - q⁻¹) * (2 * q ^ 5 - q ^ 4 + 2 * q ^ 3 - 1) / (4 * (q ^ 2 + 1) ^ 2) := by
  rw [assertedPhaseD_eq_affine_retracted q h2]
  unfold wedderburnAffinePhaseD
  have hdiff :
      -(q - q⁻¹) / 4 - (q - q⁻¹) / 2 * w21 q (zD q) -
          (-(q - q⁻¹) / 4 - (q - q⁻¹) / 2 * retractedPhaseCoeff (zD q)) =
        -((q - q⁻¹) / 2) * (w21 q (zD q) - retractedPhaseCoeff (zD q)) := by
    ring
  rw [hdiff, w21_zD_sub_retractedPhaseCoeff q hq2 hq4 h2]
  have h4 : (4 : K) = 2 * 2 := by ring
  rw [h4]
  field_simp

/-- Over `ℝ`, for all `q ≥ 1`, the true Convention-D Wedderburn weight `w_{(2,1)}(z_D)` is strictly
greater than the retracted affine coefficient `1/2 - z_D`. -/
theorem retractedPhaseCoeff_lt_w21_zD {q : ℝ} (hq : 1 ≤ q) :
    retractedPhaseCoeff (zD q) < w21 q (zD q) := by
  have hq_pos : 0 < q := lt_of_lt_of_le zero_lt_one hq
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : (2 : ℝ) ≠ 0 := two_ne_zero
  rw [← sub_pos, w21_zD_sub_retractedPhaseCoeff q hq2 hq4 h2]
  have hnum : 0 < 2 * q ^ 5 - q ^ 4 + 2 * q ^ 3 - 1 := by
    rw [w21_sub_retracted_numerator_decomp q]
    have hqm1 : 0 ≤ q - 1 := sub_nonneg.mpr hq
    have hpoly : 0 ≤ 2 * q ^ 4 + q ^ 3 + 3 * q ^ 2 + 3 * q + 3 := by positivity
    nlinarith
  have hden : 0 < 2 * (q ^ 2 + 1) ^ 2 := by positivity
  exact div_pos hnum hden

/-- Over `ℝ`, for all `q ≥ 1`, the true Convention-D Wedderburn weight `w_{(2,1)}(z_D)` never equals
the retracted coefficient `1/2 - z_D`. -/
theorem w21_zD_ne_retractedPhaseCoeff {q : ℝ} (hq : 1 ≤ q) :
    w21 q (zD q) ≠ retractedPhaseCoeff (zD q) :=
  ne_of_gt (retractedPhaseCoeff_lt_w21_zD hq)

end RetractedVsTrueWedderburnWeight

/-! ## Section 2: Jucys–Murphy Content Moments & Mirror-Covariant Bar-Odd Projected Phase -/

section JucysMurphyMomentsAndMirrorProjectedPhase

variable {K : Type*} [Field K]

/-- Total classical Jucys–Murphy content moment on `H_3(q)` under Convention-D Wedderburn weights:
content sums are `c((3)) = 0 + 1 + 2 = +3`, `c((2,1)) = 0 + 1 - 1 = 0`, `c((1^3)) = 0 - 1 - 2 = -3`,
weighted by the block trace weights `(w_{(3)}(z_D), 2 w_{(2,1)}(z_D), w_{(1^3)}(z_D))`. -/
def jmContentMomentD (q : K) : K :=
  3 * w3 q (zD q) + 0 * (2 * w21 q (zD q)) + (-3) * w111 q (zD q)

/-- Per-strand normalized Jucys–Murphy content mean `<c̄>_D = (1/3) jmContentMomentD(q)` on `H_3(q)`:
normalized content eigenvalues `(+1, 0, -1)` coincide with the normalized transposition characters
`χ^λ(τ) / f^λ = (+1, 0, -1)`. -/
def jmContentMeanD (q : K) : K :=
  1 * w3 q (zD q) + 0 * (2 * w21 q (zD q)) + (-1) * w111 q (zD q)

/-- The `n`-independent Convention-D transposition moment `Ξ_D = w_{(3)}(z_D) - w_{(1^3)}(z_D)`
from `LadderPhaseFromWeights.lean`. -/
def transpositionMomentD (q : K) : K :=
  w3 q (zD q) - w111 q (zD q)

/-- Exact identity: `jmContentMomentD q = 3 · w_{(3)}(z_D)`. -/
theorem jmContentMomentD_eq_three_mul_w3_zD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    jmContentMomentD q = 3 * w3 q (zD q) := by
  unfold jmContentMomentD
  rw [w111_conventionD q hq2]
  ring

/-- Exact coincidence of the normalized Jucys–Murphy content mean `<c̄>_D` with the transposition
moment `Ξ_D` and with the single symmetric Wedderburn weight `w_{(3)}(z_D) = (q^4 + 1)/(q^2 + 1)^2`. -/
theorem jmContentMeanD_eq_transpositionMomentD (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    jmContentMeanD q = transpositionMomentD q ∧
      transpositionMomentD q = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  constructor
  · unfold jmContentMeanD transpositionMomentD
    ring
  · unfold transpositionMomentD
    rw [w3_conventionD q hq2 hq4, w111_conventionD q hq2, sub_zero]

/-- Expression of the normalized Jucys–Murphy content mean `<c̄>_D` purely in terms of the middle
nucleon Wedderburn weight `w_{(2,1)}(z_D)`:
`jmContentMeanD q = 1 - 2 · w_{(2,1)}(z_D)`. -/
theorem jmContentMeanD_eq_one_sub_two_w21_zD (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    jmContentMeanD q = 1 - 2 * w21 q (zD q) := by
  unfold jmContentMeanD
  rw [w111_conventionD q hq2]
  have hsum := weights_conventionD_sum_eq_one q hq2 hq4
  linear_combination hsum

/-- GPMT-completed per-strand Jucys–Murphy content / transposition moment where the killed `(1^3)`
sector is restored with positive modified quantum dimension magnitude `|d_D(S^{(1^3)})| = dMod111Abs q`:
`Ξ_{GPMT+}(q) = w_{(3)}(z_D) - |d_D(S^{(1^3)})|`. -/
def jmContentMeanGPMTPos (q : K) : K :=
  w3 q (zD q) - dMod111Abs q

/-- Exact rational closed form for `jmContentMeanGPMTPos q`:
`Ξ_{GPMT+}(q) = (q^8 + q^6 - q^5 + 2 q^4 - q^3 + q^2 + 1) / ((q^2 + 1)^2 (q^4 + q^2 + 1))`. -/
theorem jmContentMeanGPMTPos_eq_div (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    jmContentMeanGPMTPos q =
      (q ^ 8 + q ^ 6 - q ^ 5 + 2 * q ^ 4 - q ^ 3 + q ^ 2 + 1) /
        ((q ^ 2 + 1) ^ 2 * (q ^ 4 + q ^ 2 + 1)) := by
  have h4inv : (1 + q ^ 2 + q ^ 4) * (1 + q ^ 2 + q ^ 4)⁻¹ = 1 := by
    apply mul_inv_cancel₀
    have : 1 + q ^ 2 + q ^ 4 = q ^ 4 + q ^ 2 + 1 := by ring
    rw [this]; exact hq4
  unfold jmContentMeanGPMTPos
  rw [w3_conventionD q hq2 hq4, dMod111Abs_eq_div q]
  field_simp
  linear_combination -(1 + q ^ 4) * h4inv

/-- The unique mirror-covariant bar-odd projected Convention-D ladder phase
(`LadderPhaseMirrorCovariance.lean` §3–§4):
`α_D^{proj}(q) = α_D(q) - h^2 / 4 = (z_D - 1)(q - q⁻¹) / 2 - (q - q⁻¹)^2 / 4`. -/
def mirrorProjectedPhaseD (q : K) : K :=
  assertedPhaseD q - (q - q⁻¹) ^ 2 / 4

/-- **Wedderburn `w_{(3)}(z_D)` Loop-Mean Form of the Mirror-Projected Phase**:
`α_D^{proj}(q) = ((q - q⁻¹) / 4) · ((q + q⁻¹) · w_{(3)}(z_D) - 2)`. -/
theorem mirrorProjectedPhaseD_eq_w3_form (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    mirrorProjectedPhaseD q =
      (q - q⁻¹) / 4 * ((q + q⁻¹) * w3 q (zD q) - 2) := by
  have h4 : (4 : K) = 2 * 2 := by ring
  rw [w3_conventionD q hq2 hq4]
  unfold mirrorProjectedPhaseD assertedPhaseD zD
  rw [h4]
  field_simp
  ring

/-- **Wedderburn `w_{(2,1)}(z_D)` Form of the Mirror-Projected Phase**:
`α_D^{proj}(q) = ((q - q⁻¹) / 4) · ((q + q⁻¹)(1 - 2 w_{(2,1)}(z_D)) - 2)`. -/
theorem mirrorProjectedPhaseD_eq_w21_form (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    mirrorProjectedPhaseD q =
      (q - q⁻¹) / 4 * ((q + q⁻¹) * (1 - 2 * w21 q (zD q)) - 2) := by
  rw [mirrorProjectedPhaseD_eq_w3_form q hq hq2 hq4 h2]
  have hsum := weights_conventionD_sum_eq_one q hq2 hq4
  have hw3 : w3 q (zD q) = 1 - 2 * w21 q (zD q) := by linear_combination hsum
  rw [hw3]

/-- **Exact Rational Closed Form of `mirrorProjectedPhaseD q`**:
`α_D^{proj}(q) = (q^2 - 1)(q^4 - 2 q^3 - 2 q + 1) / (4 q^2 (q^2 + 1))`. -/
theorem mirrorProjectedPhaseD_eq_div (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    mirrorProjectedPhaseD q =
      (q ^ 2 - 1) * (q ^ 4 - 2 * q ^ 3 - 2 * q + 1) / (4 * q ^ 2 * (q ^ 2 + 1)) := by
  unfold mirrorProjectedPhaseD assertedPhaseD zD
  have h4 : (4 : K) = 2 * 2 := by ring
  rw [h4]
  field_simp
  ring

/-- **Exact Bar-Odd Mirror Symmetry of `mirrorProjectedPhaseD`**:
Under the bar involution `q ↦ q⁻¹`, `α_D^{proj}(q⁻¹) = -α_D^{proj}(q)`. -/
theorem mirrorProjectedPhaseD_inv (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    mirrorProjectedPhaseD q⁻¹ = -mirrorProjectedPhaseD q := by
  have hqi : q⁻¹ ≠ 0 := inv_ne_zero hq
  have hq2i : (q⁻¹) ^ 2 + 1 ≠ 0 := by
    intro hc
    apply hq2
    have hx : ((q⁻¹) ^ 2 + 1) * q ^ 2 = 1 + q ^ 2 := by
      rw [add_mul, inv_pow, inv_mul_cancel₀ (pow_ne_zero 2 hq), one_mul]
    rw [hc, zero_mul] at hx
    linear_combination -hx
  have h2inv : (1 + q ^ 2) * (1 + q ^ 2)⁻¹ = 1 := by
    apply mul_inv_cancel₀
    have : 1 + q ^ 2 = q ^ 2 + 1 := by ring
    rw [this]; exact hq2
  rw [mirrorProjectedPhaseD_eq_div q⁻¹ hqi hq2i h2, mirrorProjectedPhaseD_eq_div q hq hq2 h2]
  have h4 : (4 : K) = 2 * 2 := by ring
  rw [h4]
  field_simp
  linear_combination -(-1 + 2 * q + q ^ 2 - q ^ 4 - 2 * q ^ 5 + q ^ 6) * h2inv

end JucysMurphyMomentsAndMirrorProjectedPhase

/-! ## Section 3: Two-Term Proton Pin `q_{2t}`, `m_n - m_p` Residual Cancellation, and 4 Cartan QED Weightings -/

section TwoTermProtonPinAndCartanQEDWeightings

variable {R : Type*} [CommRing R]

/-- **Consistent Two-Term Neutron Mass Residual Identity**:
When the substrate parameter `q_{2t}` is pinned by the two-term proton mass identity
`m_p^{QCD} + M_p^{QED,conn} = m_p^{exp}` and the experimental neutron mass satisfies
`m_n^{exp} = m_p^{exp} + m_e + Q_β^{exp}`, the consistent two-term neutron mass prediction
`m_n^{2t} = (m_p^{QCD} + M_p^{QED,conn}) + m_e + (Q_β^{strong} + Δm_{QED}^{conn})`
has residual against `m_n^{exp}` identically equal to the two-term `Q_β` residual
`(Q_β^{strong} + Δm_{QED}^{conn}) - Q_β^{exp}`. -/
theorem twoTerm_neutron_mass_residual_eq_qbeta_residual
    (mp_qcd mp_qed_conn mp_exp me qbeta_strong dm_qed_conn qbeta_exp mn_exp : R)
    (hpin : mp_qcd + mp_qed_conn = mp_exp)
    (hmn_exp : mn_exp = mp_exp + me + qbeta_exp) :
    ((mp_qcd + mp_qed_conn) + me + (qbeta_strong + dm_qed_conn)) - mn_exp =
      (qbeta_strong + dm_qed_conn) - qbeta_exp := by
  rw [hpin, hmn_exp]
  ring

/-- **Inconsistent Bare-Proton-Core Evaluation at the Two-Term Pin `q_{2t}`**:
If `q_{2t}` satisfies `m_p^{QCD} + M_p^{QED,conn} = m_p^{exp}` but the neutron mass is evaluated
using only the bare strong proton core `m_p^{QCD}` without `M_p^{QED,conn}`, the neutron residual
is shifted down by `-M_p^{QED,conn}` (at `q_{2t}`, `-220.08 eV` or `-234.23 ppb` of `m_n`, moving
`+148.56 ppb` to `-85.67 ppb`). -/
theorem bareCore_neutron_mass_residual_sub_proton_qed
    (mp_qcd mp_qed_conn mp_exp me qbeta_strong dm_qed_conn qbeta_exp mn_exp : R)
    (hpin : mp_qcd + mp_qed_conn = mp_exp)
    (hmn_exp : mn_exp = mp_exp + me + qbeta_exp) :
    (mp_qcd + me + (qbeta_strong + dm_qed_conn)) - mn_exp =
      ((qbeta_strong + dm_qed_conn) - qbeta_exp) - mp_qed_conn := by
  have hmp : mp_qcd = mp_exp - mp_qed_conn := by linear_combination hpin
  rw [hmp, hmn_exp]
  ring

variable {K : Type*} [Field K]

/-- Per-strand connected 4th-order Borromean `V^3` proton charge trace
(`(1/3) · NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3`):
`tr_conn(p, V^3) = -2 (q^2 - 1)^4 (q^4 + q^2 + 1) / (27 q^6)`. -/
def trConnBorromeanP (q : K) : K :=
  -2 * (q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (27 * q ^ 6)

/-- Per-strand connected 4th-order Borromean `V^3` neutron charge trace
(`(1/3) · NucleonWeightSpaceTwoTerm.trace_QAdjn_borromeanV3_connected`):
`tr_conn(n, V^3) = +(q^2 - 1)^4 (2 q^4 - q^2 + 2) / (27 q^6)`. -/
def trConnBorromeanN (q : K) : K :=
  (q ^ 2 - 1) ^ 4 * (2 * q ^ 4 - q ^ 2 + 2) / (27 * q ^ 6)

/-- `'plain'` connected Borromean `(n - p)` QED trace difference:
`Δtr_conn^{plain}(V^3) = tr_conn(n, V^3) - tr_conn(p, V^3)`. -/
def trConnDiffPlain (q : K) : K :=
  trConnBorromeanN q - trConnBorromeanP q

/-- `'KnKp'` Cartan-weighted (`K_n^{⊗3} = q⁻¹`, `K_p^{⊗3} = q`) connected Borromean `(n - p)` QED trace difference:
`Δtr_conn^{KnKp}(V^3) = q⁻¹ · tr_conn(n, V^3) - q · tr_conn(p, V^3)`. -/
def trConnDiffKnKp (q : K) : K :=
  q⁻¹ * trConnBorromeanN q - q * trConnBorromeanP q

/-- `'Kp3'` proton-Cartan-weighted connected Borromean `(n - p)` QED trace difference:
`Δtr_conn^{Kp3}(V^3) = tr_conn(n, V^3) - q · tr_conn(p, V^3)`. -/
def trConnDiffKp3 (q : K) : K :=
  trConnBorromeanN q - q * trConnBorromeanP q

/-- `'q'` uniform Cartan-scaled connected Borromean `(n - p)` QED trace difference:
`Δtr_conn^{q}(V^3) = q · (tr_conn(n, V^3) - tr_conn(p, V^3))`. -/
def trConnDiffQ (q : K) : K :=
  q * trConnDiffPlain q

/-- Exact closed form of `trConnDiffPlain q`:
`Δtr_conn^{plain}(V^3) = (q^2 - 1)^4 (4 q^4 + q^2 + 4) / (27 q^6)`. -/
theorem trConnDiffPlain_eq_div (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnDiffPlain q =
      (q ^ 2 - 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4) / (27 * q ^ 6) := by
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  unfold trConnDiffPlain trConnBorromeanN trConnBorromeanP
  rw [h27]
  field_simp
  ring

/-- **Upstream Matrix-Trace Seam for `trConnBorromeanP`**:
`trConnBorromeanP q` equals `(1/3)` of the 3×3 proton adjacent-charge Borromean matrix trace
`trace ((Q12p + Q23p) * borromeanV3A q)` from `NucleonWeightSpaceTwoTerm.trace_QAdjp_borromeanV3`. -/
theorem trConnBorromeanP_eq_one_third_trace_QAdjp (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBorromeanP q =
      (1 / 3 : K) * trace ((Q12p + Q23p) * borromeanV3A q) := by
  have h9 : (9 : K) = 3 * 3 := by ring
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  rw [trace_QAdjp_borromeanV3 q hq h3]
  unfold trConnBorromeanP
  rw [h9, h27]
  field_simp
  ring

/-- **Upstream Matrix-Trace Seam for `trConnBorromeanN`**:
`trConnBorromeanN q` equals `(1/3)` of the connected 3×3 neutron adjacent-charge Borromean matrix trace
`trace ((Q12n + Q23n) * borromeanV3B q) + (2/9) * trace (borromeanV3B q)` from
`NucleonWeightSpaceTwoTerm.trace_QAdjn_borromeanV3_connected`. -/
theorem trConnBorromeanN_eq_one_third_trace_QAdjn_connected (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBorromeanN q =
      (1 / 3 : K) * (trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q)) := by
  have h9 : (9 : K) = 3 * 3 := by ring
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  rw [trace_QAdjn_borromeanV3_connected q hq h3]
  unfold trConnBorromeanN
  rw [h9, h27]
  field_simp
  ring

/-- **Upstream Matrix-Trace Seam for `trConnDiffPlain`**:
`trConnDiffPlain q` equals `(1/3)` of the connected `(n - p)` 3×3 matrix trace difference from
`NucleonWeightSpaceTwoTerm.trace_QAdj_connected_diff_borromeanV3`. -/
theorem trConnDiffPlain_eq_one_third_trace_QAdj_connected_diff (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnDiffPlain q =
      (1 / 3 : K) *
        ((trace ((Q12n + Q23n) * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q)) -
          trace ((Q12p + Q23p) * borromeanV3A q)) := by
  unfold trConnDiffPlain
  rw [trConnBorromeanN_eq_one_third_trace_QAdjn_connected q hq h3,
      trConnBorromeanP_eq_one_third_trace_QAdjp q hq h3]
  ring

/-- **Exact Closed-Form Difference Between `'KnKp'` and `'plain'` Cartan QED Weightings**:
`Δtr_conn^{KnKp}(V^3) - Δtr_conn^{plain}(V^3) = (q - 1)(q^2 - 1)^4 (2 q^5 - 2 q^4 + 2 q^3 + q^2 + 2 q - 2) / (27 q^7)`. -/
theorem trConnDiffKnKp_sub_plain (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnDiffKnKp q - trConnDiffPlain q =
      (q - 1) * (q ^ 2 - 1) ^ 4 * (2 * q ^ 5 - 2 * q ^ 4 + 2 * q ^ 3 + q ^ 2 + 2 * q - 2) / (27 * q ^ 7) := by
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  unfold trConnDiffKnKp trConnDiffPlain trConnBorromeanN trConnBorromeanP
  rw [h27]
  field_simp
  ring

/-- **Exact Closed-Form Difference Between `'Kp3'` and `'plain'` Cartan QED Weightings**:
`Δtr_conn^{Kp3}(V^3) - Δtr_conn^{plain}(V^3) = 2 (q - 1)(q^2 - 1)^4 (q^4 + q^2 + 1) / (27 q^6)`. -/
theorem trConnDiffKp3_sub_plain (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnDiffKp3 q - trConnDiffPlain q =
      2 * (q - 1) * (q ^ 2 - 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (27 * q ^ 6) := by
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  unfold trConnDiffKp3 trConnDiffPlain trConnBorromeanN trConnBorromeanP
  rw [h27]
  field_simp
  ring

/-- **Exact Closed-Form Difference Between `'q'` and `'Kp3'` Cartan QED Weightings**:
`Δtr_conn^{q}(V^3) - Δtr_conn^{Kp3}(V^3) = (q - 1)(q^2 - 1)^4 (2 q^4 - q^2 + 2) / (27 q^6)`. -/
theorem trConnDiffQ_sub_Kp3 (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnDiffQ q - trConnDiffKp3 q =
      (q - 1) * (q ^ 2 - 1) ^ 4 * (2 * q ^ 4 - q ^ 2 + 2) / (27 * q ^ 6) := by
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  unfold trConnDiffQ trConnDiffKp3 trConnDiffPlain trConnBorromeanN trConnBorromeanP
  rw [h27]
  field_simp
  ring

end TwoTermProtonPinAndCartanQEDWeightings

end QOU.QBeta.WedderburnPhaseAndTwoTermPinBridge
