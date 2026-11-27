import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Quark charges: what is left to derive once isospin is derived

Owner ruling 2026-11-22: the quark charges `q_u, q_d` must be derived.

The corpus derives the isospin difference (`I₃(u) − I₃(d) = 1`, the writhe / `T³` map on the
nucleon doublet). If the charge is affine in `I₃` on quark strands, `Q = I₃ + c` (the
Gell-Mann–Nishijima form with one common hypercharge term `c = Y/2`), then `q_u − q_d = 1`, and
any ONE further linear condition fixes both charges. Each of the three natural conditions gives
the same answer `(2/3, −1/3)`. None of the three conditions is derived here; this file only
shows that exactly one is needed. Generic field of characteristic 0 (division by 3).
-/

namespace QOU.MassTheory.QuarkChargeReduction

variable {R : Type*} [Field R] [CharZero R]

/-- Affine-in-isospin charge: `q_u = 1/2 + c`, `q_d = −1/2 + c`. -/
def qu (c : R) : R := 1 / 2 + c
def qd (c : R) : R := -1 / 2 + c

theorem qu_sub_qd (c : R) : qu c - qd c = 1 := by unfold qu qd; ring

/-- Neutron (`udd`) neutral fixes `c = 1/6`. -/
theorem c_of_neutron_neutral (c : R) (h : qu c + 2 * qd c = 0) : c = 1 / 6 := by
  unfold qu qd at h; linear_combination h / 3

/-- Proton (`uud`) charge `+1` fixes `c = 1/6`. -/
theorem c_of_proton_one (c : R) (h : 2 * qu c + qd c = 1) : c = 1 / 6 := by
  unfold qu qd at h; linear_combination h / 3

/-- Hydrogen neutral with electron charge `−1` fixes `c = 1/6`. -/
theorem c_of_hydrogen (c : R) (h : (2 * qu c + qd c) + (-1) = 0) : c = 1 / 6 := by
  unfold qu qd at h; linear_combination h / 3

/-- With `c = 1/6`: `q_u = 2/3`, `q_d = −1/3`. -/
theorem charges_of_c (c : R) (hc : c = 1 / 6) : qu c = 2 / 3 ∧ qd c = -1 / 3 := by
  subst hc; unfold qu qd; constructor <;> ring

/-- Without a hypercharge term (`c = 0`, charge = isospin alone) the neutron has charge
`−1/2`, so isospin alone cannot give a neutral neutron. -/
theorem neutron_charge_c_zero : qu (0 : R) + 2 * qd 0 = -1 / 2 := by unfold qu qd; ring

end QOU.MassTheory.QuarkChargeReduction
