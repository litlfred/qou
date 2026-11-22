/-
  Planck time: t_P(q) = q / (q - 1) = 1 / ℏ_q.

  The minimal dynamical time unit of the QOU, defined as the
  period of one full Reeb circuit.

  Base ring (§7c).  Exactly two elements have to be inverted here:
  `q` (to form `ℏ_q = 1 - q⁻¹`) and `q - 1` (to form `t_P`).  Both
  are carried as explicit **units** `q d : Rˣ` with `↑d = ↑q - 1`,
  so the whole file lives over a generic `[CommRing R]` — the
  minimal home is the localisation `ℤ[q^{±1}][(q-1)^{-1}]`, not a
  field.  A field `R` with `q ≠ 0`, `q ≠ 1` is the special case
  `q := Units.mk0 q _`, `d := Units.mk0 (q - 1) _`, under which
  `planckTime = q / (q - 1)` and `planckTime = 1 / (1 - q⁻¹)`.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Algebra.Group.Units.Basic
import Mathlib.Tactic.Ring

namespace QOU

variable {R : Type*} [CommRing R]

/-- The quantum Planck constant `ℏ_q = 1 - q⁻¹`, for `q` a unit of
    the ground ring. -/
-- Ref: [leitner2026] Ch 8, Definition: Planck Time
def hbarQ (q : Rˣ) : R := 1 - ↑q⁻¹

/-- Planck time as a function of the substrate parameter `q`:
    `t_P = q / (q - 1)`, written division-free as `q · (q-1)⁻¹`
    with `q - 1` supplied as the unit `d`. -/
-- Ref: [leitner2026] Ch 8, Definition: Planck Time
def planckTime (q d : Rˣ) (_hd : (d : R) = (q : R) - 1) : R :=
  (q : R) * ↑d⁻¹

/-- `ℏ_q` is itself a unit whenever `q - 1` is, namely
    `ℏ_q = q⁻¹ · (q - 1)`. -/
-- Ref: [leitner2026] Ch 8, Definition: Planck Time
def hbarUnit (q d : Rˣ) (_hd : (d : R) = (q : R) - 1) : Rˣ := q⁻¹ * d

/-- The unit `hbarUnit` really has value `ℏ_q`. -/
-- Ref: [leitner2026] Ch 8, Definition: Planck Time
theorem hbarUnit_val (q d : Rˣ) (hd : (d : R) = (q : R) - 1) :
    ((hbarUnit q d hd : Rˣ) : R) = hbarQ q := by
  unfold hbarUnit hbarQ
  rw [Units.val_mul, hd, mul_sub, Units.inv_mul, mul_one]

/-- Planck time equals the reciprocal of the quantum Planck
    constant: `t_P = ℏ_q⁻¹`, stated as the inverse of the unit
    `hbarUnit` (whose value is `ℏ_q` by `hbarUnit_val`).  Over a
    field this is the familiar `planckTime = 1 / (1 - q⁻¹)`. -/
-- Ref: [leitner2026] Ch 8, Definition: Planck Time
theorem planckTime_eq_inv_hbar (q d : Rˣ) (hd : (d : R) = (q : R) - 1) :
    planckTime q d hd = ((hbarUnit q d hd)⁻¹ : Rˣ) := by
  unfold planckTime hbarUnit
  rw [mul_inv_rev, inv_inv, Units.val_mul]
  exact mul_comm _ _

/-- Planck length is identically 1: `ℏ_q · t_P = 1`. -/
-- Ref: [leitner2026] Ch 8, Definition: Planck Time
theorem planck_length_eq_one (q d : Rˣ) (hd : (d : R) = (q : R) - 1) :
    hbarQ q * planckTime q d hd = 1 := by
  unfold hbarQ planckTime
  have h1 : (↑q⁻¹ : R) * ↑q = 1 := q.inv_mul
  have h2 : (↑d : R) * ↑d⁻¹ = 1 := d.mul_inv
  calc (1 - (↑q⁻¹ : R)) * ((q : R) * ↑d⁻¹)
      = ((q : R) - (↑q⁻¹ : R) * ↑q) * ↑d⁻¹ := by ring
    _ = ((q : R) - 1) * ↑d⁻¹ := by rw [h1]
    _ = (↑d : R) * ↑d⁻¹ := by rw [hd]
    _ = 1 := h2

end QOU
