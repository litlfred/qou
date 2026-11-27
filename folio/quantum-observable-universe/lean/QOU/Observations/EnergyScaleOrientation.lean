/-
# Orientation of the two CAL-1 charts: framing against the bar-even part

Thread "Unify the log and mass-formula energy scales" (2026-11-27), owner decision A
("derive the orientation first"). Companion to `QOU.Observations.EnergyScaleBridge`. Probe:
`computations/probes/energy_scale_bridge/orientation_probe.py`. Audit:
`docs/audits/2026-11-27-energy-scale-bridge.md` §7.

The electron trace factors as `τ_e = q³ · y₃` with the framing-corrected trace
`y₃ = (q⁴ + 1)/(q² + 1)²`. This file proves, over a generic field:

* `y3_bar`: `y₃` is bar-invariant, `y₃(q⁻¹) = y₃(q)`.
* `omega_bar`: its Euler weight `ω = 4q²(q² − 1)/((q⁴ + 1)(q² + 1))` (which is `q ∂_q log y₃`;
  checked in the probe) is bar-odd, `ω(q⁻¹) = −ω(q)`.
* `y3_one`, `omega_one`: at `q = 1`, `y₃ = 1/2` and `ω = 0`.

With `β = ln q` this gives `L_e = ℓ_e + 3β` and `w_e = ω_e + 3`, where `ℓ_e = log y₃` is
bar-even and `3` is the writhe of `σ₀σ₁σ₀`. Then:

* `unit_signs_iff`: `L_e < 0 < w_e` holds iff `ℓ_e < −3β` and `−3 < ω_e`. In words, the
  log-chart unit takes its sign from the framing-free part, and the mass-chart unit takes it
  from the framing.
* `split_at_classical_limit`: at `q = 1` (`β = 0`, `ω = 0`) with `ℓ < 0` (it is `−ln 2`),
  both conditions hold. So the sign conflict is already present in the classical limit; it is
  not an accident of `q₀`.
* `framing_cell_zero`: a cell that is a pure framing difference has energy zero in any
  framing-free chart.

Which part should set the sign of energy is not decided here. No measured value enters.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.Observations.EnergyScaleOrientation

section Field

variable {R : Type*} [Field R]

/-- The framing-corrected electron trace `y₃ = (q⁴ + 1)/(q² + 1)²`. -/
def y3 (q : R) : R := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- The Euler weight of `y₃`, `ω = q ∂_q log y₃`. -/
def omega (q : R) : R := 4 * q ^ 2 * (q ^ 2 - 1) / ((q ^ 4 + 1) * (q ^ 2 + 1))

private theorem inv_pow_add_one (q : R) (n : ℕ) (hq : q ≠ 0) :
    q⁻¹ ^ n + 1 = (q ^ n + 1) / q ^ n := by
  have hn : q ^ n ≠ 0 := pow_ne_zero n hq
  rw [inv_pow, add_div, div_self hn, inv_eq_one_div, add_comm]

private theorem inv_pow_add_one_ne (q : R) (n : ℕ) (hq : q ≠ 0) (h : q ^ n + 1 ≠ 0) :
    q⁻¹ ^ n + 1 ≠ 0 := by
  rw [inv_pow_add_one q n hq]
  exact div_ne_zero h (pow_ne_zero n hq)

theorem y3_bar (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) : y3 q⁻¹ = y3 q := by
  unfold y3
  rw [inv_pow_add_one q 4 hq, inv_pow_add_one q 2 hq]
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  field_simp

theorem omega_bar (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) :
    omega q⁻¹ = -omega q := by
  unfold omega
  rw [inv_pow_add_one q 4 hq, inv_pow_add_one q 2 hq]
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hq4 : q ^ 4 ≠ 0 := pow_ne_zero 4 hq
  rw [show q⁻¹ ^ 2 - 1 = (1 - q ^ 2) / q ^ 2 by field_simp]
  field_simp
  ring

theorem y3_one : y3 (1 : R) = (1 + 1) / (1 + 1) ^ 2 := by
  unfold y3; norm_num

theorem omega_one : omega (1 : R) = 0 := by
  unfold omega; norm_num

/-- A cell that is a pure framing difference has zero framing-free log. -/
theorem framing_cell_zero (m ℓ : R) : m * (ℓ - ℓ) = 0 := by ring

end Field

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

theorem y3_one_half : y3 (1 : R) = 1 / 2 := by
  unfold y3; norm_num

/-- The two unit signs, read through the framing decomposition `L_e = ℓ + kβ`, `w_e = ω + k`. -/
theorem unit_signs_iff (ℓ ω k β : R) :
    (ℓ + k * β < 0 ∧ 0 < ω + k) ↔ (ℓ < -(k * β) ∧ -k < ω) := by
  constructor
  · rintro ⟨h1, h2⟩; exact ⟨by linarith, by linarith⟩
  · rintro ⟨h1, h2⟩; exact ⟨by linarith, by linarith⟩

/-- At the classical limit (`β = 0`, `ω = 0`) a negative framing-free log and a positive
writhe give `L_e < 0 < w_e`: the sign conflict holds at `q = 1`. -/
theorem split_at_classical_limit (ℓ k : R) (hℓ : ℓ < 0) (hk : 0 < k) :
    ℓ + k * 0 < 0 ∧ 0 < (0 : R) + k := by
  constructor <;> simp <;> linarith

/-! ### Three cell types and the two charts

Write a cell as `L_X = ℓ_X + k_X β`, `w_X = ω_X + k_X`. Three types occur:

* a pure power (n − p, `τ_n = q⁻² τ_p`): `ℓ = ω = 0`, `k = −2`;
* a bar-even cell (Δ − N, `τ_Δ/τ_N = q² + q⁻²`): `k = 0`, `ℓ > 0`, `ω > 0` for `q > 1`;
* a bond letter `f < 1` that grows with `q`: `L_f < 0 < w_f`.

The target signs are n above p, Δ above N, and bonds binding (`E(f) < 0`). -/

/-- A bar-even cell with `ℓ > 0` lies below zero in the log chart (`L_e < 0`). -/
theorem even_cell_log_neg (m ℓ Le : R) (hm : 0 < m) (hℓ : 0 < ℓ) (hLe : Le < 0) :
    m * ℓ / Le < 0 :=
  div_neg_of_pos_of_neg (mul_pos hm hℓ) hLe

/-- A bar-even cell with `ω > 0` lies above zero in the mass chart (`w_e > 0`). -/
theorem even_cell_mass_pos (m ω we : R) (hm : 0 < m) (hω : 0 < ω) (hwe : 0 < we) :
    0 < m * ω / we :=
  div_pos (mul_pos hm hω) hwe

/-- Neither CAL-1 chart gets the three target signs. In the log chart Δ − N is negative; in the
mass chart n − p is negative. (Bonds unbind in both: `EnergyScaleBridge.bond_unbinds_*`.) -/
theorem no_single_chart (m β ℓΔ ωΔ Le we : R) (hm : 0 < m) (hβ : 0 < β)
    (hℓ : 0 < ℓΔ) (hω : 0 < ωΔ) (hLe : Le < 0) (hwe : 0 < we) :
    (0 < m * (-2 * β) / Le ∧ m * ℓΔ / Le < 0) ∧
    (m * (-2) / we < 0 ∧ 0 < m * ωΔ / we) := by
  refine ⟨⟨?_, even_cell_log_neg m ℓΔ Le hm hℓ hLe⟩, ⟨?_, even_cell_mass_pos m ωΔ we hm hω hwe⟩⟩
  · apply div_pos_of_neg_of_neg _ hLe
    nlinarith
  · apply div_neg_of_neg_of_pos _ hwe
    linarith

/-- **Electron-independent no-go.** For any nonzero unit `u` (any CAL-1 electron reading, either
sign), a pure-power cell `−2β` and a bar-even cell with `ℓ > 0` get opposite signs in the log
chart. Rereading the electron moves which of n − p and Δ − N is wrong, never both to right. -/
theorem log_chart_np_delta_opposite (β ℓ u : R) (hβ : 0 < β) (hℓ : 0 < ℓ) (hu : u ≠ 0) :
    ((-2 * β) / u) * (ℓ / u) < 0 := by
  rw [div_mul_div_comm]
  apply div_neg_of_neg_of_pos
  · nlinarith
  · exact mul_self_pos.mpr hu

/-- The same in the mass chart: the cells `−2` and `ω > 0` get opposite signs for any unit. -/
theorem mass_chart_np_delta_opposite (ω u : R) (hω : 0 < ω) (hu : u ≠ 0) :
    ((-2) / u) * (ω / u) < 0 := by
  rw [div_mul_div_comm]
  apply div_neg_of_neg_of_pos
  · linarith
  · exact mul_self_pos.mpr hu

end Ordered

end QOU.Observations.EnergyScaleOrientation
