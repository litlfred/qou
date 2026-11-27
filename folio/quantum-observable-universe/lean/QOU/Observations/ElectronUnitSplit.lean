/-
# Why the two electron units differ by `τ_e/ℏ_q²`

Companion to `QOU.Observations.EnergyScaleMap` (W6, beans `qou-91w7`, `qou-6gf9`, issue #9164).
The corpus normalises the electron two ways:

* the trace pipeline, electron weight `τ_e = T(σ₀σ₁σ₀)`, the convention-D trace of the ruled
  electron word (`E0WeightCandidates.tau_electron`);
* the mass formula `m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²`, unit `m_e/ℏ_q²`, electron weight `ℏ_q²`.

Their units differ by `R = τ_e/ℏ_q²`. This file derives `R`:

* `electron_21_trace_zero`: the electron word has trace `0` in the `(2,1)` block, so
  `τ_e = q³ · y₍₃₎(q)` (`tau_electron_eq_framing_mul_y3`): framing `q³` (writhe 3) times the
  Ocneanu weight of the one-row block. The whole electron trace lives in that block.
* `y3_split`: `y₍₃₎ = 1/2 + h²/(2[2]²)`, `h = q − q⁻¹`, `[2] = q + q⁻¹`. The constant `1/2` is
  the classical value `2^{c−n}` (`traceD_one`, `c = 2`, `n = 3`).
* `y3_bar`: `y₍₃₎` is bar-invariant, which is why its departure from `1/2` is of order two.
* `y3_quantum_part_eq`: that order-two part is `ℏ_q² · q²(q+1)²/(2(q²+1)²)`.
* `unit_ratio_split`: hence `R = q³/(2ℏ_q²) + q⁵(q+1)²/(2(q²+1)²)` exactly.

And the gap on the mass-formula side:

* `product_weight_ne`: a chart whose weight is a product `V·ρ` cannot match a non-zero
  calibration on an object with `V = 0`. The ruled electron closes to the Hopf link, a torus
  link, whose hyperbolic volume is `0` (Thurston; cited, not formalised). So the mass formula's
  own rule gives the electron weight `0`, and its electron weight `ℏ_q²` is not of the formula's
  form: it is the CAL-1 placement, put in by hand.

Everything here is over a generic field (§7c). No numerical value enters.
-/
import QOU.Nuclear.E0WeightCandidates

namespace QOU.Observations.ElectronUnitSplit

open QOU.QBeta.WeightSpaceMarkov QOU.QBeta.E0WeightCandidates

variable {R : Type*} [Field R]

/-- `ℏ_q = 1 − q⁻¹`. -/
def hbar (q : R) : R := 1 - q⁻¹

/-- **The electron word has trace zero in the `(2,1)` block.** -/
theorem electron_21_trace_zero (q : R) (hq : q ≠ 0) :
    (r21a q * r21b q * r21a q).trace = 0 := by
  simp [r21a, r21b, Matrix.trace_fin_two]
  field_simp
  ring

/-- **`τ_e = q³ · y₍₃₎`**: framing times the one-row Ocneanu weight. -/
theorem tau_electron_eq_framing_mul_y3 (q : R) (hq : q ≠ 0) :
    tauD3 q (q ^ 3) (r21a q * r21b q * r21a q) = q ^ 3 * y3 q := by
  unfold tauD3
  rw [electron_21_trace_zero q hq]
  ring

/-- **`y₍₃₎ = 1/2 + h²/(2[2]²)`.** -/
theorem y3_split (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : R) ≠ 0) :
    y3 q = 1 / 2 + (q - q⁻¹) ^ 2 / (2 * (q + q⁻¹) ^ 2) := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  unfold y3
  field_simp
  ring

/-- **`y₍₃₎` is bar-invariant.** -/
theorem y3_bar (q : R) : y3 q⁻¹ = y3 q := by
  unfold y3
  rw [inv_inv, add_comm]

/-- **The order-two part of `y₍₃₎` is `ℏ_q² · q²(q+1)²/(2(q²+1)²)`.** -/
theorem y3_quantum_part_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : R) ≠ 0) :
    (q - q⁻¹) ^ 2 / (2 * (q + q⁻¹) ^ 2) =
      hbar q ^ 2 * (q ^ 2 * (q + 1) ^ 2 / (2 * (q ^ 2 + 1) ^ 2)) := by
  have hs : q + q⁻¹ ≠ 0 := by
    intro h; apply hq2; field_simp at h; linear_combination h
  unfold hbar
  field_simp
  ring

theorem hbar_ne_zero (q : R) (hq1 : q ≠ 1) : hbar q ≠ 0 := by
  unfold hbar
  intro h
  apply hq1
  have : q⁻¹ = 1 := by linear_combination -h
  simpa using congrArg (·⁻¹) this

/-- **The unit ratio, exactly:** `τ_e/ℏ_q² = q³/(2ℏ_q²) + q⁵(q+1)²/(2(q²+1)²)`. -/
theorem unit_ratio_split (q : R) (hq : q ≠ 0) (hq1 : q ≠ 1) (hq2 : q ^ 2 + 1 ≠ 0)
    (h2 : (2 : R) ≠ 0) :
    tauD3 q (q ^ 3) (r21a q * r21b q * r21a q) / hbar q ^ 2 =
      q ^ 3 / (2 * hbar q ^ 2) + q ^ 5 * (q + 1) ^ 2 / (2 * (q ^ 2 + 1) ^ 2) := by
  have hh := hbar_ne_zero q hq1
  rw [tau_electron_eq_framing_mul_y3 q hq, y3_split q hq hq2 h2,
    y3_quantum_part_eq q hq hq2 h2]
  field_simp

/-- **A product weight vanishing on the electron cannot match CAL-1.** If a chart's weight is
`V·ρ` and `V e = 0`, its value at `e` is `0`, so it is not a non-zero `m_e`. -/
theorem product_weight_ne {ι : Type*} (V ρ : ι → R) (unit me : R) (e : ι)
    (hV : V e = 0) (hme : me ≠ 0) : unit * (V e * ρ e) ≠ me := by
  rw [hV, zero_mul, mul_zero]
  exact hme.symm

end QOU.Observations.ElectronUnitSplit
