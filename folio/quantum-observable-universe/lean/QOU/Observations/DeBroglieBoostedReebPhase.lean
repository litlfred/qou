import QOU.MathlibInfra.LorentzBoostPhase
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Lorentz-Boosted Compton/Reeb Phase and `q`-Deformed Double-Slit de Broglie Wavelength

Building on `QOU.MathlibInfra.LorentzBoostPhase`, this module derives the spatial de Broglie
wavelength `lambda_dB = 2π ħ / p = h / (γ m v)` inside QOU by Lorentz-boosting the rest-frame
meridian/Reeb Compton clock `ω₀ = m c² / ħ`, and proves how the `q`-exterior derivative
`d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d` stretches the horizontal interference fringe wavelength to
`lambda_q = q * lambda_dB` (`Δy_q = q * lambda_dB * L / d`) while the `q⁻² Δ` Hodge core broadens
the diffraction envelope by `q²` (§7c generic + `_real` specialization pattern).

Historical credit:
- Louis de Broglie (1924), *Recherches sur la théorie des quanta* (phase-harmony derivation of
  `λ = h / p` from Lorentz-boosted rest-frame clock `m c² = h ν₀`).
- Roger Bach, Damian Pope, Sy-Hwang Liou & Herman Batelaan (2013), *Controlled double-slit
  electron diffraction*, New J. Phys. 15, 033018.

-- Ref: [bach2013]
-- Ref: [rem:meridian-exceptional-divisor-note]
-- Ref: [def:double-slit-q-phase]
-/

namespace QOU.Observations.DeBroglieBoostedReebPhase

open QOU.MathlibInfra.LorentzBoostPhase

/-! ## 1. Generic `[Field R]` Boosted Reeb Phase and `d_q` Fringe-Wavelength Scaling -/

section GenericField

variable {R : Type*} [Field R]

/-- Effective `q`-deformed interference wavelength `lambda_q = q * lambda_dB`. -/
def qDeformedWavelength (q lambda_dB : R) : R :=
  q * lambda_dB

/-- Far-field `q`-deformed Young fringe spacing `Δy_q = q * lambda_dB * L / d`. -/
def qDeformedFringeSpacing (q lambda_dB L d : R) : R :=
  q * lambda_dB * L / d

/-- Classical `q⁻²` Hodge-core + `(1 - q⁻¹)²` Reeb spin-core envelope half-width
`w_q = q² * lambda_dB * L / a * (1 + (1 - q⁻¹)² * ratio)`. -/
def qDeformedEnvelopeWidth (q lambda_dB L a ratio : R) : R :=
  q ^ 2 * lambda_dB * L / a * (1 + (1 - q⁻¹) ^ 2 * ratio)

/-- **Boosted Reeb Clock Theorem (`ω₀ τ = E t / ħ - p x / ħ` & Mass-Shell):**
Under 1+1D Lorentz boost `τ = γ * (t - v * x / c²)` with `γ² * (1 - v² / c²) = 1`, the
rest-frame Compton/Reeb phase `ω₀ * τ` (`ω₀ = m c² / ħ`) decomposes into `E * t / ħ - p * x / ħ`
with `E² - (p * c)² = (m * c²)²`, `(E / p) * v = c²`, and spatial wavenumber `k_dB = p / ħ`. -/
theorem boosted_reeb_meridian_phase {c hbar γ m v : R}
    (hc : c ≠ 0) (hhbar : hbar ≠ 0) (hγ : γ ≠ 0) (hm : m ≠ 0) (hv : v ≠ 0)
    (hlorentz : γ ^ 2 * (1 - v ^ 2 / c ^ 2) = 1) (t x : R) :
    restComptonFreq m c hbar * properTime1D γ t v x c =
        relEnergy γ m c * t / hbar - relMomentum γ m v * x / hbar ∧
      (relEnergy γ m c) ^ 2 - (relMomentum γ m v * c) ^ 2 = (m * c ^ 2) ^ 2 ∧
      phaseVelocity (relEnergy γ m c) (relMomentum γ m v) * v = c ^ 2 ∧
      deBroglieWavenumber (relMomentum γ m v) hbar = (γ * m * v) / hbar := by
  refine ⟨lorentz_boost_phase_invariance hc hhbar γ m t v x,
    relativistic_mass_shell hc hlorentz m,
    deBroglie_phase_group_velocity hγ hm hv c,
    rfl⟩

/-- **Horizontal `d_q` Scaling Stretches `lambda_dB` to `lambda_q = q * lambda_dB`:**
Applying the horizontal `q⁻¹` factor of `d_q = q⁻¹ d + (1 - q⁻¹) π_V ∘ d` to the geometric
path-length phase `two_pi * Δℓ / lambda_dB` yields `two_pi * Δℓ / (q * lambda_dB)`, identifying
the effective fringe wavelength `lambda_q = q * lambda_dB` and fringe spacing
`Δy_q = q * lambda_dB * L / d`. -/
theorem horizontal_dq_scales_deBroglie_wavelength {q lambda_dB : R}
    (hq : q ≠ 0) (hlam : lambda_dB ≠ 0) (two_pi Δℓ L d : R) :
    q⁻¹ * (two_pi * Δℓ / lambda_dB) = two_pi * Δℓ / qDeformedWavelength q lambda_dB ∧
      qDeformedFringeSpacing q lambda_dB L d = qDeformedWavelength q lambda_dB * L / d := by
  unfold qDeformedWavelength qDeformedFringeSpacing
  refine ⟨by field_simp, rfl⟩

/-- At `q = 1`, both the `q`-deformed fringe wavelength `lambda_q` and envelope half-width `w_q`
collapse to standard de Broglie–Fraunhofer diffraction (`lambda_dB` and `lambda_dB * L / a`). -/
theorem qDeformed_double_slit_at_one (lambda_dB L d a ratio : R) :
    qDeformedWavelength 1 lambda_dB = lambda_dB ∧
      qDeformedFringeSpacing 1 lambda_dB L d = lambda_dB * L / d ∧
      qDeformedEnvelopeWidth 1 lambda_dB L a ratio = lambda_dB * L / a := by
  unfold qDeformedWavelength qDeformedFringeSpacing qDeformedEnvelopeWidth
  refine ⟨one_mul lambda_dB, by ring, by simp⟩

end GenericField

/-! ## 2. Archimedean `ℝ` Realization (`2π ħ / (γ m v)` and `1 < q` Broadening) -/

section ArchimedeanReal

/-- Relativistic de Broglie wavelength `lambda_dB = 2π ħ / (γ m v)` over `ℝ`. -/
noncomputable def deBroglieWavelength_real (hbar γ m v : ℝ) : ℝ :=
  deBroglieWavelength (2 * Real.pi * hbar) (relMomentum γ m v)

/-- Archimedean `ℝ` specialization of `qDeformedFringeSpacing` (§7c `_real` pair). -/
noncomputable def qDeformedFringeSpacing_real (q lambda_dB L d : ℝ) : ℝ :=
  qDeformedFringeSpacing q lambda_dB L d

/-- Archimedean `ℝ` specialization of `qDeformedEnvelopeWidth` (§7c `_real` pair). -/
noncomputable def qDeformedEnvelopeWidth_real (q lambda_dB L a ratio : ℝ) : ℝ :=
  qDeformedEnvelopeWidth q lambda_dB L a ratio

/-- **Complete `ℝ` Double-Slit de Broglie + `d_q` Phase Theorem:**
1. `q⁻¹ * (2π Δℓ / lambda_dB) = 2π Δℓ / (q * lambda_dB)` where `lambda_dB = 2π ħ / (γ m v)`,
2. For `1 < q` and `0 < lambda_dB * L / d`, the `q`-deformed fringe spacing `Δy_q` strictly exceeds
   the `q = 1` de Broglie fringe spacing `lambda_dB * L / d`,
3. For `1 < q`, `0 < lambda_dB * L / a`, and `0 ≤ ratio`, the `q²`-scaled envelope half-width `w_q`
   strictly exceeds the `q = 1` Fraunhofer envelope width `lambda_dB * L / a`. -/
theorem boosted_reeb_double_slit_real {q hbar γ m v L d a ratio : ℝ}
    (hq1 : 1 < q) (hhbar : 0 < hbar) (hγ : 0 < γ) (hm : 0 < m) (hv : 0 < v)
    (hL : 0 < L) (hd : 0 < d) (ha : 0 < a) (hratio : 0 ≤ ratio) (Δℓ : ℝ) :
    let lambda_dB := deBroglieWavelength_real hbar γ m v
    q⁻¹ * (2 * Real.pi * Δℓ / lambda_dB) = 2 * Real.pi * Δℓ / (q * lambda_dB) ∧
      qDeformedFringeSpacing_real 1 lambda_dB L d < qDeformedFringeSpacing_real q lambda_dB L d ∧
      qDeformedEnvelopeWidth_real 1 lambda_dB L a ratio < qDeformedEnvelopeWidth_real q lambda_dB L a ratio := by
  intro lambda_dB
  have hq0 : 0 < q := lt_trans zero_lt_one hq1
  have hq_ne : q ≠ 0 := ne_of_gt hq0
  have hp_pos : 0 < relMomentum γ m v := by
    unfold relMomentum
    positivity
  have hlam_pos : 0 < lambda_dB := by
    show 0 < (2 * Real.pi * hbar) / relMomentum γ m v
    have hpi : 0 < Real.pi := Real.pi_pos
    positivity
  have hlam_ne : lambda_dB ≠ 0 := ne_of_gt hlam_pos
  have hphase := (horizontal_dq_scales_deBroglie_wavelength hq_ne hlam_ne (2 * Real.pi) Δℓ L d).1
  rw [qDeformedWavelength] at hphase
  refine ⟨hphase, ?_, ?_⟩
  · unfold qDeformedFringeSpacing_real qDeformedFringeSpacing
    have hbase : 0 < lambda_dB * L / d := by positivity
    have h1 : (1 : ℝ) * lambda_dB * L / d = lambda_dB * L / d := by ring
    have hq_form : q * lambda_dB * L / d = q * (lambda_dB * L / d) := by ring
    rw [h1, hq_form]
    exact lt_mul_of_one_lt_left hbase hq1
  · unfold qDeformedEnvelopeWidth_real
    rw [(qDeformed_double_slit_at_one lambda_dB L d a ratio).2.2]
    unfold qDeformedEnvelopeWidth
    have hbase_a : 0 < lambda_dB * L / a := by positivity
    have hq2 : 1 < q ^ 2 := by nlinarith
    have hspin : 0 ≤ (1 - q⁻¹) ^ 2 * ratio := mul_nonneg (sq_nonneg _) hratio
    have hfac : 1 < q ^ 2 * (1 + (1 - q⁻¹) ^ 2 * ratio) := by
      have hprod : 0 ≤ q ^ 2 * ((1 - q⁻¹) ^ 2 * ratio) := mul_nonneg (sq_nonneg q) hspin
      nlinarith
    have hrhs : q ^ 2 * lambda_dB * L / a * (1 + (1 - q⁻¹) ^ 2 * ratio) =
        (q ^ 2 * (1 + (1 - q⁻¹) ^ 2 * ratio)) * (lambda_dB * L / a) := by ring
    rw [hrhs]
    exact lt_mul_of_one_lt_left hbase_a hfac

end ArchimedeanReal

end QOU.Observations.DeBroglieBoostedReebPhase
