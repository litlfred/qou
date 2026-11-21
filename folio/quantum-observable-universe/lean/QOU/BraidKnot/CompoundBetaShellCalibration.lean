import Mathlib.Tactic

/-!
# QOU.BraidKnot.CompoundBetaShellCalibration

**Canonical declaration** for content block at
[`quantum-observable-universe/particle-interactions/compound-beta-shell-calibration-interpretation.ts`](quantum-observable-universe/particle-interactions/compound-beta-shell-calibration-interpretation.ts).

Formalises the manuscript corollary that the shell sector introduces **no new
calibration**: the shell scale `E₀` equals the `H²` input `𝔔_β` of the
three-calibration discipline (alongside `H⁰ = m_e` and `H¹ = m_μ/m_e`), so
shell binding is *derived* from β-decay Q-values and level-3 shadow prices,
not independently fitted. Physical scales over `ℝ` (§7c archimedean).
-/

namespace QOU.BraidKnot

/-- The three-calibration data with the shell scale.

    A `definition` carrier: the three cohomological calibration inputs
    `H⁰ = m_e`, `H¹ = m_μ/m_e`, `H² = 𝔔_β`, and the shell scale `E₀`, pinned
    to `𝔔_β` (the `H²` input). -/
structure CompoundBetaShellCalibration where
  /-- `H⁰` calibration: electron mass `m_e`. -/
  H0 : ℝ
  /-- `H¹` calibration: the muon ratio `m_μ/m_e`. -/
  H1 : ℝ
  /-- `H²` calibration: the β-decay Q-value `𝔔_β`. -/
  H2 : ℝ
  /-- The shell scale `E₀`. -/
  E0 : ℝ
  /-- `E₀ = 𝔔_β` — the shell scale *is* the `H²` input. -/
  E0_eq : E0 = H2

namespace CompoundBetaShellCalibration

variable (C : CompoundBetaShellCalibration)

/-- **No new calibration:** the shell scale `E₀` coincides with the existing
    `H²` calibration `𝔔_β`; it is not an independent fourth input. -/
theorem E0_is_H2_input : C.E0 = C.H2 := C.E0_eq

/-- The calibration set stays a triple `{H⁰, H¹, H²}`: `E₀` is a member of it
    (equal to `H²`), never a fourth element. -/
theorem E0_mem_calibrations : C.E0 ∈ ({C.H0, C.H1, C.H2} : Set ℝ) := by
  rw [C.E0_eq]; simp

end CompoundBetaShellCalibration

/-- **De-axiomatisation (bean `lqft`).** `E₀ = 𝔔_β` is not a free assumption:
    the shell scale is *defined* to be the `H²` calibration input `𝔔_β` (the
    manuscript's "shell sector introduces no new calibration"). `ofCalibration`
    builds the record from the three calibration values with `E0 := H2`, so
    `E0_eq` is `rfl` — the "no fourth calibration" property is structural, not
    posited. (The numerical value of `𝔔_β` itself is fixed by the β-decay
    Q-value compute; that is a producer-side fact, orthogonal to this identity.) -/
def CompoundBetaShellCalibration.ofCalibration (m_e muRatio Qbeta : ℝ) :
    CompoundBetaShellCalibration where
  H0 := m_e
  H1 := muRatio
  H2 := Qbeta
  E0 := Qbeta
  E0_eq := rfl

/-- In a `ofCalibration` record the shell scale is definitionally the H² input. -/
theorem CompoundBetaShellCalibration.ofCalibration_E0
    (m_e muRatio Qbeta : ℝ) :
    (CompoundBetaShellCalibration.ofCalibration m_e muRatio Qbeta).E0 = Qbeta := rfl

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/compound-beta-shell-calibration-interpretation.ts

end QOU.BraidKnot
