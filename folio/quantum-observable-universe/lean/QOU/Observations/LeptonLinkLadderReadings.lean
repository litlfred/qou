/-
# Ring masses of the least-crossing link ladder (Hopf, T(2,4), Whitehead)

Thread "Derive the electron's categorical weight" (2026-11-28). Candidate word set from the tau
thread (card to the owner): the least-crossing non-split prime two-component closures of odd
3-braids, `e = σ₁σ₂σ₁` (Hopf, lk 1), `μ = σ₁⁴σ₂⁻¹` (T(2,4), lk 2),
`τ = σ₁²σ₂⁻¹σ₁σ₂⁻¹` (Whitehead link, lk 0). Audit §19.

Read under `def:mass-identity` as it stands (N = 2, ring trace, braid class; §18), over any field:
* `mass_e`, `mass_mu`, `mass_tau`: the three ring masses
  `(q²+1)(q⁴+1)/q⁶`, `(q²+1)(q⁸+q⁴−q²+1)/q¹²`, `(q²+1)(q¹⁰−q⁸+2q⁶−q⁴+2q²−1)/q⁸`.
* `mass_at_one`: all three equal `4 = 2^c` at `q = 1` (two components each).
The energy readings `U(1) = 3·lk` are 3, 6, 0 (general theorem, `RingMassLinkingThreeStrand`).
The values are not compared with any measurement.
-/
import QOU.Observations.MassReadingForced
import Mathlib.Tactic

namespace QOU.Observations.LeptonLinkLadderReadings

open QOU.QBeta.WeightSpaceMarkov QOU.Observations.MassReadingForced

variable {R : Type*} [Field R]

/-- `e = σ₁σ₂σ₁` (Hopf link). -/
def mE (q : R) : R := (q ^ 2 + 1) * (q ^ 4 + 1) / q ^ 6

/-- `μ = σ₁⁴σ₂⁻¹` (`T(2,4)`). -/
def mMu (q : R) : R := (q ^ 2 + 1) * (q ^ 8 + q ^ 4 - q ^ 2 + 1) / q ^ 12

/-- `τ = σ₁²σ₂⁻¹σ₁σ₂⁻¹` (Whitehead link). -/
def mTau (q : R) : R :=
  (q ^ 2 + 1) * (q ^ 10 - q ^ 8 + 2 * q ^ 6 - q ^ 4 + 2 * q ^ 2 - 1) / q ^ 8

theorem mass_e (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    massWord q 3 (r21a q * r21b q * r21a q) = mE q :=
  massWord_e q hq h2

theorem mass_mu (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    massWord q 3 (r21a q * r21a q * r21a q * r21a q * r21bInv q) = mMu q :=
  massWord_tau q hq h2

theorem mass_tau (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    massWord q 1 (r21a q * r21a q * r21bInv q * r21a q * r21bInv q) = mTau q := by
  simp [massWord, mTau, MassReadingForced.y3, MassReadingForced.y21, r21a, r21bInv_eq, Matrix.trace_fin_two]
  field_simp
  ring

/-- At `q = 1` each mass is `4 = 2²` (two components). -/
theorem mass_at_one : mE (1 : R) = 4 ∧ mMu (1 : R) = 4 ∧ mTau (1 : R) = 4 := by
  refine ⟨?_, ?_, ?_⟩ <;> simp [mE, mMu, mTau] <;> norm_num

end QOU.Observations.LeptonLinkLadderReadings
