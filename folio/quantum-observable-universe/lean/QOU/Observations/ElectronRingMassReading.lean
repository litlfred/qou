/-
# The ring-valued (framing-corrected) electron mass and its energy reading

Thread "Derive the electron's categorical weight", third part (2026-11-27, owner: "Look for
second derived factor. Which mass are you using? Ring version?"). Audit:
`docs/audits/2026-11-27-electron-categorical-weight.md` §9.

#9733 read the electron through its raw convention-D trace `τ_e = q³ y₍₃₎`. The corpus mass is
not the raw trace. `def:mass-identity` (mass-endomorphism/mass-identity.md) defines it as the
framing-corrected value `[2]ⁿ q^{−2w} ∫_A ρ(β)`, valued in the ring (owner ruling: mass in the
ring; `QOU.Core.MassInRing`). Over a generic field:

* `framing_pos_stab`, `framing_neg_stab`: the factor `[2] q^{∓2}` exactly cancels the
  convention-D Markov parameters `z_D = q³/(q²+1)` and `z̄_D = 1/(q(q²+1))`, so the correction is
  the one that makes the mass a braid-class invariant (both stabilisations).
* `massE_eq`: the electron (`n = 3`, `w = 3`) has ring mass `m_e = [4]/q³`,
  `[4] = q³ + q + q⁻¹ + q⁻³`. At `q = 1` it is `4 = 2^c`, `c = 2` components (`massE_one`).
* `q_mul_dMassE`: `q·m_e' = m_e·(D[4]/[4] − 3)`, with `D[4] = 3q³ + q − q⁻¹ − 3q⁻³`.
  So the thermodynamic energy reading `U = −q ∂_q log m` gives the electron
  `U_e = 3 − D[4]/[4]` (`uE`), and `uE_one`: `U_e(1) = 3`.
* `np_cell_U`: with `ε_n = q⁻² ε_p`, the readings differ by `+2`, so for `U_e > 0` the neutron
  lies above the proton.

So in the ring the writhe still gives the `3`: the framing correction does not remove it (it
flips the raw trace's `+3` to `−3`, and the energy sign `U = −∂_β log` makes it `+3` again). What
changes is the sign. Both the electron and the n−p cell are positive in this chart. No measured
value enters.
-/
import QOU.Observations.ElectronWeightAdditivity

namespace QOU.Observations.ElectronRingMassReading

open QOU.Observations.ElectronWeightAdditivity

variable {R : Type*} [Field R]

/-- Balanced `[4] = q³ + q + q⁻¹ + q⁻³`. -/
def qInt4 (q : R) : R := q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3

/-- `D[4] = q ∂_q [4] = 3q³ + q − q⁻¹ − 3q⁻³`. -/
def dqInt4 (q : R) : R := 3 * q ^ 3 + q - q⁻¹ - 3 * q⁻¹ ^ 3

/-- The framing-corrected (ring) mass of the electron: `[2]³ q^{−2·3} τ_e`. -/
def massE (q : R) : R := (q + q⁻¹) ^ 3 * (q ^ 6)⁻¹ * tauE q

/-- **Positive stabilisation:** `[2] q⁻² · z_D = 1`. -/
theorem framing_pos_stab (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (q + q⁻¹) * q⁻¹ ^ 2 * (q ^ 3 / (q ^ 2 + 1)) = 1 := by
  field_simp

/-- **Negative stabilisation:** `[2] q² · z̄_D = 1`. -/
theorem framing_neg_stab (q : R) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0) :
    (q + q⁻¹) * q ^ 2 * (1 / (q * (q ^ 2 + 1))) = 1 := by
  field_simp

/-- **The ring mass of the electron is `[4]/q³`.** -/
theorem massE_eq (q : R) (hq : q ≠ 0) (_h2 : q ^ 2 + 1 ≠ 0) :
    massE q = qInt4 q / q ^ 3 := by
  unfold massE tauE qInt4
  field_simp
  ring

/-- At `q = 1` the ring mass is `4 = 2^c` (two components). -/
theorem massE_one [CharZero R] : massE (1 : R) = 4 := by
  unfold massE tauE; norm_num

/-- The derivative of `[4]/q³`, written out. -/
def dMassE (q : R) : R :=
  ((3 * q ^ 2 + 1 - (q ^ 2)⁻¹ - 3 * (q ^ 4)⁻¹) * q ^ 3 - qInt4 q * (3 * q ^ 2)) / (q ^ 3) ^ 2

/-- **`q·m_e' = m_e·(D[4]/[4] − 3)`.** -/
theorem q_mul_dMassE (q : R) (hq : q ≠ 0) (h4 : qInt4 q ≠ 0) :
    q * dMassE q = qInt4 q / q ^ 3 * (dqInt4 q / qInt4 q - 3) := by
  have key : q * dMassE q = (dqInt4 q - 3 * qInt4 q) / q ^ 3 := by
    unfold dMassE dqInt4 qInt4
    field_simp
  rw [key]
  field_simp

/-- The electron's energy reading on the ring mass, `U_e = −q ∂_q log m_e = 3 − D[4]/[4]`. -/
def uE (q : R) : R := 3 - dqInt4 q / qInt4 q

/-- **`U_e(1) = 3`.** -/
theorem uE_one [CharZero R] : uE (1 : R) = 3 := by
  unfold uE dqInt4 qInt4; norm_num

/-- **n−p cell on the ring mass, thermodynamic sign.** If the readings are
`U = −q·ε'/ε` and `ε_n = q⁻² ε_p`, then `U_n − U_p = +2`. -/
theorem np_cell_U (q e e' : R) (hq : q ≠ 0) (he : e ≠ 0) :
    -(q * (-(2 * q⁻¹ ^ 3) * e + q⁻¹ ^ 2 * e') / (q⁻¹ ^ 2 * e)) - -(q * e' / e) = 2 := by
  field_simp
  ring

end QOU.Observations.ElectronRingMassReading
