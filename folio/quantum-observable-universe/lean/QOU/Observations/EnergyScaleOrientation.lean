/-
# Orientation of the two CAL-1 charts: framing against the bar-even part

Thread "Unify the log and mass-formula energy scales" (2026-11-27), owner decision A
("derive the orientation first"). Companion to `QOU.Observations.EnergyScaleBridge`. Probe:
`computations/probes/energy_scale_bridge/orientation_probe.py`. Audit:
`docs/audits/2026-11-27-energy-scale-bridge.md` §7.

The electron trace factors as `τ_e = q³ · y₃` with the framing-corrected trace
`y₃ = (q⁴ + 1)/(q² + 1)²`. This file proves, over a generic commutative ring with `q : Rˣ`
and cleared denominators (§7c base-ring discipline):

* `y3_bar`: `y₃` is bar-invariant, `y₃Num(q⁻¹) · y₃Den(q) = y₃Num(q) · y₃Den(q⁻¹)`.
* `omega_bar`: its Euler weight `ω = 4q²(q² − 1)/((q⁴ + 1)(q² + 1))` (which is `q ∂_q log y₃`;
  checked in the probe) is bar-odd, `ωNum(q⁻¹) · ωDen(q) = −(ωNum(q) · ωDen(q⁻¹))`.
* `y3_one`, `omega_one`: at `q = 1`, `2 · y₃Num(1) = y₃Den(1)` (`y₃(1) = 1/2`) and `ωNum(1) = 0`.

With `β = ln q` this gives `L_e = ℓ_e + 3β` and `w_e = ω_e + 3`, where `ℓ_e = log y₃` is
bar-even and `3` is the writhe of `σ₀σ₁σ₀`. Then over a strict ordered commutative ring:

* `unit_signs_iff`: `L_e < 0 < w_e` holds iff `ℓ_e < −3β` and `−3 < ω_e`. In words, the
  log-chart unit takes its sign from the framing-free part, and the mass-chart unit takes it
  from the framing.
* `split_at_classical_limit`: at `q = 1` (`β = 0`, `ω = 0`) with `ℓ < 0` (it is `−ln 2`),
  both conditions hold. So the sign conflict is already present in the classical limit; it is
  not an accident of `q₀`.
* `framing_cell_zero`: a cell that is a pure framing difference has energy zero in any
  framing-free chart.
* `no_single_chart`, `log_chart_np_delta_opposite`, `mass_chart_np_delta_opposite`: neither
  CAL-1 chart gets all three target signs, and for any invertible electron reading `u : Rˣ`
  the pure-power `n − p` cell and bar-even `Δ − N` cell have opposite signs.

Which part should set the sign of energy is not decided here. No measured value enters.
-/
import QOU.Observations.EnergyScaleBridge
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.Observations.EnergyScaleOrientation

open QOU.Observations.EnergyScaleBridge

section Ring

variable {R : Type*} [CommRing R]

/-- Numerator `q⁴ + 1` of the framing-corrected electron trace `y₃ = (q⁴ + 1)/(q² + 1)²`. -/
def y3Num (q : R) : R := q ^ 4 + 1

/-- Denominator `(q² + 1)²` of the framing-corrected electron trace `y₃`. -/
def y3Den (q : R) : R := (q ^ 2 + 1) ^ 2

/-- Numerator `4q²(q² − 1)` of the Euler weight `ω = q ∂_q log y₃`. -/
def omegaNum (q : R) : R := 4 * q ^ 2 * (q ^ 2 - 1)

/-- Denominator `(q⁴ + 1)(q² + 1)` of the Euler weight `ω = q ∂_q log y₃`. -/
def omegaDen (q : R) : R := (q ^ 4 + 1) * (q ^ 2 + 1)

/-- `y₃` is bar-invariant (`q ↦ q⁻¹`) over any commutative ring (cross-multiplied). -/
theorem y3_bar (q : Rˣ) :
    y3Num (↑q⁻¹ : R) * y3Den (q : R) = y3Num (q : R) * y3Den (↑q⁻¹ : R) := by
  unfold y3Num y3Den
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := Units.mul_inv q
  calc
    ((↑q⁻¹ : R) ^ 4 + 1) * ((q : R) ^ 2 + 1) ^ 2
        = ((↑q⁻¹ : R) ^ 4 + ((q : R) * (↑q⁻¹ : R)) ^ 4) * ((q : R) ^ 2 + 1) ^ 2 := by
          rw [hq]; ring
    _ = ((q : R) ^ 4 + 1) * ((↑q⁻¹ : R) ^ 2 + ((q : R) * (↑q⁻¹ : R)) ^ 2) ^ 2 := by
          ring
    _ = ((q : R) ^ 4 + 1) * ((↑q⁻¹ : R) ^ 2 + 1) ^ 2 := by
          rw [hq]; ring

/-- `ω = q ∂_q log y₃` is bar-odd (`q ↦ q⁻¹`) over any commutative ring (cross-multiplied). -/
theorem omega_bar (q : Rˣ) :
    omegaNum (↑q⁻¹ : R) * omegaDen (q : R) = -(omegaNum (q : R) * omegaDen (↑q⁻¹ : R)) := by
  unfold omegaNum omegaDen
  have hq : (q : R) * (↑q⁻¹ : R) = 1 := Units.mul_inv q
  calc
    4 * (↑q⁻¹ : R) ^ 2 * ((↑q⁻¹ : R) ^ 2 - 1) * (((q : R) ^ 4 + 1) * ((q : R) ^ 2 + 1))
        = 4 * (↑q⁻¹ : R) ^ 2 * ((↑q⁻¹ : R) ^ 2 - ((q : R) * (↑q⁻¹ : R)) ^ 2) *
            ((q : R) * (↑q⁻¹ : R)) ^ 2 * (((q : R) ^ 4 + 1) * ((q : R) ^ 2 + 1)) := by
          rw [hq]; ring
    _ = -(4 * (q : R) ^ 2 * ((q : R) ^ 2 - 1) *
            (((↑q⁻¹ : R) ^ 4 + ((q : R) * (↑q⁻¹ : R)) ^ 4) *
              ((↑q⁻¹ : R) ^ 2 + ((q : R) * (↑q⁻¹ : R)) ^ 2))) := by
          ring
    _ = -(4 * (q : R) ^ 2 * ((q : R) ^ 2 - 1) *
            (((↑q⁻¹ : R) ^ 4 + 1) * ((↑q⁻¹ : R) ^ 2 + 1))) := by
          rw [hq]; ring

/-- At `q = 1`, `2 · y₃Num(1) = y₃Den(1)` (classical value `y₃(1) = 1/2`). -/
theorem y3_one : 2 * y3Num (1 : R) = y3Den (1 : R) := by
  unfold y3Num y3Den; ring

/-- At `q = 1`, `ωNum(1) = 0` and `ωDen(1) = 4` (classical value `ω(1) = 0`). -/
theorem omega_one : omegaNum (1 : R) = 0 ∧ omegaDen (1 : R) = 4 := by
  unfold omegaNum omegaDen; constructor <;> ring

/-- A cell that is a pure framing difference has zero framing-free log. -/
theorem framing_cell_zero (m ℓ : R) : m * (ℓ - ℓ) = 0 := by ring

end Ring

section Ordered

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

theorem y3_den_pos (q : R) : 0 < y3Den q := by
  unfold y3Den
  have h : 0 < q ^ 2 + 1 := by
    have hsq : 0 ≤ q ^ 2 := sq_nonneg q
    linarith
  exact sq_pos_of_pos h

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
theorem even_cell_log_neg (m ℓ : R) (Le : Rˣ)
    (hm : 0 < m) (hℓ : 0 < ℓ) (hLe : (Le : R) < 0) :
    m * ℓ * (↑Le⁻¹ : R) < 0 :=
  mul_neg_of_pos_of_neg (mul_pos hm hℓ) (unit_inv_neg Le hLe)

/-- A bar-even cell with `ω > 0` lies above zero in the mass chart (`w_e > 0`). -/
theorem even_cell_mass_pos (m ω : R) (we : Rˣ)
    (hm : 0 < m) (hω : 0 < ω) (hwe : 0 < (we : R)) :
    0 < m * ω * (↑we⁻¹ : R) :=
  mul_pos (mul_pos hm hω) (unit_inv_pos we hwe)

/-- Neither CAL-1 chart gets the three target signs. In the log chart Δ − N is negative; in the
mass chart n − p is negative. (Bonds unbind in both: `EnergyScaleBridge.bond_unbinds_*`.) -/
theorem no_single_chart (m β ℓΔ ωΔ : R) (Le we : Rˣ) (hm : 0 < m) (hβ : 0 < β)
    (hℓ : 0 < ℓΔ) (hω : 0 < ωΔ) (hLe : (Le : R) < 0) (hwe : 0 < (we : R)) :
    (0 < m * (-2 * β) * (↑Le⁻¹ : R) ∧ m * ℓΔ * (↑Le⁻¹ : R) < 0) ∧
      (m * (-2) * (↑we⁻¹ : R) < 0 ∧ 0 < m * ωΔ * (↑we⁻¹ : R)) :=
  ⟨⟨np_cell_log_pos m β Le hm hβ hLe, even_cell_log_neg m ℓΔ Le hm hℓ hLe⟩,
    ⟨np_cell_mass_neg m we hm hwe, even_cell_mass_pos m ωΔ we hm hω hwe⟩⟩

/-- **Electron-independent no-go.** For any invertible unit `u : Rˣ` (any CAL-1 electron reading,
either sign), a pure-power cell `−2β` and a bar-even cell with `ℓ > 0` get opposite signs in the
log chart. Rereading the electron moves which of n − p and Δ − N is wrong, never both to right. -/
theorem log_chart_np_delta_opposite (β ℓ : R) (u : Rˣ) (hβ : 0 < β) (hℓ : 0 < ℓ) :
    ((-2 * β) * (↑u⁻¹ : R)) * (ℓ * (↑u⁻¹ : R)) < 0 := by
  have hu0 : (↑u⁻¹ : R) ≠ 0 := (u⁻¹).ne_zero
  have hu2 : 0 < (↑u⁻¹ : R) ^ 2 := sq_pos_of_ne_zero hu0
  have hneg : (-2 * β) * ℓ < 0 := by nlinarith
  have heq : ((-2 * β) * (↑u⁻¹ : R)) * (ℓ * (↑u⁻¹ : R)) =
      ((-2 * β) * ℓ) * (↑u⁻¹ : R) ^ 2 := by ring
  rw [heq]
  exact mul_neg_of_neg_of_pos hneg hu2

/-- The same in the mass chart: the cells `−2` and `ω > 0` get opposite signs for any unit. -/
theorem mass_chart_np_delta_opposite (ω : R) (u : Rˣ) (hω : 0 < ω) :
    ((-2 : R) * (↑u⁻¹ : R)) * (ω * (↑u⁻¹ : R)) < 0 := by
  have hu0 : (↑u⁻¹ : R) ≠ 0 := (u⁻¹).ne_zero
  have hu2 : 0 < (↑u⁻¹ : R) ^ 2 := sq_pos_of_ne_zero hu0
  have hneg : (-2 : R) * ω < 0 := by linarith
  have heq : ((-2 : R) * (↑u⁻¹ : R)) * (ω * (↑u⁻¹ : R)) =
      ((-2 : R) * ω) * (↑u⁻¹ : R) ^ 2 := by ring
  rw [heq]
  exact mul_neg_of_neg_of_pos hneg hu2

end Ordered

end QOU.Observations.EnergyScaleOrientation
