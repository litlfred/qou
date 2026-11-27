import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import QOU.InformationTheory.UnifiedClockScaleLayers

/-!
# The energy-to-length map

Generic-field (§7c: zero `ℝ`, zero empirical literals, zero `sorry`) statement of the
map that turns a model energy into a model length. It is the information-theoretic route
asked for in the energy-scale thread (owner, 2026-11-27): *"Derive the general map from model
energies to lengths, then read the radius off it."*

## What is proved

1. **The map is forced up to one constant (`scaleCovariant_eq_inv`).** Any map `L : K → K`
   that is covariant under energy rescaling, `L (c * E) = c⁻¹ * L E` for every `c ≠ 0`,
   has the form `L E = L 1 / E`. No other functional form is available.
2. **The constant is the Layer-I action–speed product (`comptonLength`).** With
   `ℏ_q = 1 - q⁻¹` and `c_q = (q - 1)⁻¹` from `UnifiedClockScaleLayers` /
   `ReebLengthTimeAndLightConeEntropy`, the map is `ℓ_q(E) = ℏ_q · c_q / E`, and
   `ℏ_q · c_q = q⁻¹` exactly (`hbarQ_mul_causalSpeed`), so `ℓ_q(E) = 1 / (q · E)`
   (`comptonLength_eq`).
3. **Planck normalisation (`comptonLength_planckEnergy`).** At the Layer-I Planck energy
   `E_P := ℏ_q · c_q / ℓ_P` with `ℓ_P = 1`, the map returns `ℓ_P = 1`. So the internal unit
   system fixes the constant; nothing is chosen.
4. **Ratios carry no `q` and no calibration (`comptonLength_ratio`,
   `comptonLength_calibration_cancels`).** `ℓ_q(E₁) / ℓ_q(E₂) = E₂ / E₁`, and a Layer-III lab
   unit `L_cal` multiplies every length and cancels from every ratio.
5. **Information-count reading (`mlLength_eq`).** If an energy `E` allows at most
   `κ · E · T / ℏ_q` distinguishable state changes in time `T` (a Margolus–Levitin-type count
   with a dimensionless constant `κ > 0`), and a signal crosses `c_q · T` in that time, then the
   length per distinguishable change is `ℓ_q(E) / κ`. The count supplies only the constant `κ`.
   Its value (`π/2` for Margolus–Levitin, `1` for the Compton convention) is a convention of
   the count and is carried as a parameter, not chosen against any target.
6. **Bound states need a second input (`BekensteinSaturationConjecture`).** A radius is not
   `ℓ_q(E)` alone. The Bekenstein form `R ≥ S · ℓ_q(E) / κ_B` relates radius, energy and an
   entropy `S`. That the *inequality* bounds the dimensionless ratio `R / ℓ_q(E)` from below is
   proved (`radius_ratio_ge_of_bekenstein`). That a ground state *saturates* it is **not**
   proved; it is isolated as the zero-instance Rule-13a conjecture class
   `BekensteinSaturationConjecture`, from which `R / ℓ_q(E) = S / κ_B` follows sorry-free
   (`radius_ratio_of_saturation`).

## What is not claimed

* No numerical value of `q` is used. Deriving `q₀` is out of scope and forbidden.
* No radius is fitted. Converting `ℓ_q(E)` to femtometres needs the measured reduced Compton
  length of the energy unit, and that enters only at the comparison boundary (Layer III).
* The measured proton radius is about four proton reduced Compton lengths. This is a known
  coincidence. No construction in this file was selected with that number in view.

-- Ref: [leitner2026] information-theory, rem:spacetime-length-distance-layers
-- Ref: [margolus1998] Margolus & Levitin, Physica D 120 (1998), 188–195.
-- Ref: [bekenstein1981] Bekenstein, Phys. Rev. D 23 (1981), 287–298.
-/

namespace QOU.InformationTheory.EnergyLengthMap

open QOU.InformationTheory.UnifiedClockScaleLayers

section GenericField

variable {K : Type*} [Field K]

/-! ### 1. The functional form is forced -/

/-- A map from energies to lengths is **scale covariant** when rescaling the energy by
`c ≠ 0` rescales the length by `c⁻¹`. -/
def ScaleCovariant (L : K → K) : Prop :=
  ∀ c E : K, c ≠ 0 → L (c * E) = c⁻¹ * L E

/-- **The form is forced.** A scale-covariant map is `E ↦ L 1 / E` on nonzero energies. -/
theorem scaleCovariant_eq_inv {L : K → K} (hL : ScaleCovariant L) {E : K} (hE : E ≠ 0) :
    L E = L 1 / E := by
  have h := hL E 1 hE
  rw [mul_one] at h
  rw [h, div_eq_inv_mul]

/-- Conversely, every map `E ↦ C / E` is scale covariant. -/
theorem scaleCovariant_div (C : K) : ScaleCovariant (fun E : K => C / E) := by
  intro c E hc
  simp only
  rw [div_eq_mul_inv, div_eq_mul_inv, mul_inv]
  ring

/-! ### 2. The constant is `ℏ_q · c_q` -/

/-- Layer-I causal speed `c_q = (q - 1)⁻¹` (Lieb–Robinson cone slope). -/
def causalSpeed (q : K) : K := (q - 1)⁻¹

/-- The exact Layer-I identity `ℏ_q · c_q = q⁻¹`. -/
theorem hbarQ_mul_causalSpeed {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    hbarQ q * causalSpeed q = q⁻¹ := by
  have hs : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  unfold hbarQ causalSpeed
  field_simp

/-- **The energy-to-length map** `ℓ_q(E) = ℏ_q · c_q / E`. -/
def comptonLength (q E : K) : K := hbarQ q * causalSpeed q / E

/-- `ℓ_q(E) = 1 / (q · E)`. -/
theorem comptonLength_eq {q E : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    comptonLength q E = 1 / (q * E) := by
  unfold comptonLength
  rw [hbarQ_mul_causalSpeed hq0 hq1, one_div, mul_inv, div_eq_mul_inv]

/-- The map is scale covariant, so by `scaleCovariant_eq_inv` it is the unique such map with
constant `ℏ_q · c_q`. -/
theorem comptonLength_scaleCovariant (q : K) : ScaleCovariant (comptonLength q) := by
  intro c E hc
  exact scaleCovariant_div (hbarQ q * causalSpeed q) c E hc

/-! ### 3. Planck normalisation -/

/-- Layer-I Planck length, `ℓ_P = 1` (`normalisedCircuitLength`). -/
def planckLength : K := 1

/-- Layer-I Planck energy `E_P = ℏ_q · c_q / ℓ_P`. -/
def planckEnergy (q : K) : K := hbarQ q * causalSpeed q / planckLength

/-- `E_P = q⁻¹`. -/
theorem planckEnergy_eq {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) : planckEnergy q = q⁻¹ := by
  unfold planckEnergy planckLength
  rw [div_one, hbarQ_mul_causalSpeed hq0 hq1]

/-- **The map sends the Planck energy to the Planck length.** The constant of the map is fixed
by the internal unit system, not chosen. -/
theorem comptonLength_planckEnergy {q : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    comptonLength q (planckEnergy q) = planckLength := by
  rw [comptonLength_eq hq0 hq1, planckEnergy_eq hq0 hq1, mul_inv_cancel₀ hq0, div_one]
  rfl

/-! ### 4. Ratios -/

/-- **Length ratios are energy ratios inverted**, with no `q` left. -/
theorem comptonLength_ratio {q E₁ E₂ : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1)
    (h₁ : E₁ ≠ 0) (h₂ : E₂ ≠ 0) :
    comptonLength q E₁ / comptonLength q E₂ = E₂ / E₁ := by
  rw [comptonLength_eq hq0 hq1, comptonLength_eq hq0 hq1]
  field_simp

/-- **A lab unit cancels.** Multiplying every model length by a calibration `L_cal ≠ 0` leaves
every ratio unchanged. -/
theorem comptonLength_calibration_cancels {q E₁ E₂ Lcal : K} (hL : Lcal ≠ 0)
    (h₂ : comptonLength q E₂ ≠ 0) :
    (Lcal * comptonLength q E₁) / (Lcal * comptonLength q E₂) =
      comptonLength q E₁ / comptonLength q E₂ := by
  field_simp

/-- **Lengths in the CAL-1 unit.** Every model length is a multiple of the length of the unit
energy: `ℓ_q(E) = (E_unit / E) · ℓ_q(E_unit)`. With `E_unit` the CAL-1 energy (`m_e c²`),
`ℓ_q(E_unit)` is the reduced Compton length of the unit, the only place a measured length
enters, and the multiplier `E_unit / E` is a ratio of model energies. -/
theorem comptonLength_in_unit {q E Eu : K} (hq0 : q ≠ 0) (hq1 : q ≠ 1)
    (hE : E ≠ 0) (hu : Eu ≠ 0) :
    comptonLength q E = (Eu / E) * comptonLength q Eu := by
  rw [comptonLength_eq hq0 hq1, comptonLength_eq hq0 hq1]
  field_simp

/-! ### 5. The information-count reading -/

/-- Length per distinguishable state change: in time `T` an energy `E` allows
`κ · E · T / ℏ_q` changes, and a signal crosses `c_q · T`. -/
def mlLength (κ q E T : K) : K := (causalSpeed q * T) / (κ * E * T / hbarQ q)

/-- **The count supplies only a constant.** The length per distinguishable change is
`ℓ_q(E) / κ`, independent of `T`. -/
theorem mlLength_eq {κ q E T : K} (hκ : κ ≠ 0) (hE : E ≠ 0) (hT : T ≠ 0) (hq1 : q ≠ 1) :
    mlLength κ q E T = comptonLength q E / κ := by
  have hh : hbarQ q ≠ 0 := hbarQ_ne_zero hq1
  unfold mlLength comptonLength
  field_simp

end GenericField

/-! ### 6. Bound states: the Bekenstein form -/

section OrderedField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The Bekenstein-form inequality: a region of radius `R` holding a state of energy `E` and
entropy `S` satisfies `R ≥ S · ℓ_q(E) / κ_B`. Carried as a hypothesis, not asserted. -/
def BekensteinBound (κB q E S R : K) : Prop := S * comptonLength q E / κB ≤ R

/-- **The dimensionless radius is bounded below by the entropy.** -/
theorem radius_ratio_ge_of_bekenstein {κB q E S R : K}
    (hℓ : 0 < comptonLength q E) (h : BekensteinBound κB q E S R) :
    S / κB ≤ R / comptonLength q E := by
  unfold BekensteinBound at h
  rw [le_div_iff₀ hℓ]
  calc S / κB * comptonLength q E = S * comptonLength q E / κB := by ring
    _ ≤ R := h

/-- **Rule-13a conjecture class (zero instances).** A ground state of energy `E` and entropy
`S` saturates the Bekenstein form. No instance is constructed anywhere; the class names the
missing principle so that its consequences can be stated sorry-free. -/
class BekensteinSaturationConjecture (κB q E S R : K) : Prop where
  saturates : R = S * comptonLength q E / κB

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- Under saturation, the dimensionless radius is the entropy over `κ_B`. -/
theorem radius_ratio_of_saturation {κB q E S R : K} (hκ : κB ≠ 0)
    (hℓ : comptonLength q E ≠ 0) [h : BekensteinSaturationConjecture κB q E S R] :
    R / comptonLength q E = S / κB := by
  rw [h.saturates]
  field_simp

end OrderedField

end QOU.InformationTheory.EnergyLengthMap
