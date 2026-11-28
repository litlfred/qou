import Mathlib.RingTheory.Derivation.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# The energy reading of a jet-level weight `ℏ_q^k`

The brane tower weights a level-`n` state by a power of `ℏ_q = 1 − q⁻¹`. This file computes what
such a factor does to the energy reading `U(m) = −q ∂_q log m` (`def:mass-identity`, energy
chart), with no `ℝ` and no measured value.

Setting: a field `F` with a derivation `D` and an element `q` with `D q = 1` (so `D = ∂_q` and
`q • D` is the Euler operator `q ∂_q`, the invariant vector field of `G_m`). Nothing here fixes `F`.

Results.
* `energy_mul`: `U` turns products into sums (the `G_m` logarithm), as in
  `QOU.MassTheory.EnergyReadingTower.invLogDeriv_mul`.
* `energy_hbar`: `U(ℏ_q) = −1/(q − 1)`.
* `energy_zpow`: `U(aⁿ) = n U(a)`.
* `energy_hbar_zpow_mul`: `U(ℏ_q^k · m) = U(m) − k/(q − 1)`.
* `energy_level_mul`: `U(ℏ_q^(−2n) · m) = U(m) + 2n/(q − 1)`.

So in the coordinate `t = q − 1` a level factor `ℏ_q^k` adds a simple pole at the classical point
`q = 1` with coefficient `−k`. The sign of the exponent is the sign of that pole. Which sign is
allowed is an extra condition (energy bounded below as `q → 1⁺`), treated in
`QOU.Transcendental.MassTheory.LevelWeightSign`; it is not derived here.

Why the power-series chart of `EnergyReadingTower` cannot see this: `ℏ_q = t/(1 + t)` has zero
constant term, so it is not a unit of `K⟦t⟧`. The level weight lives one step out, in the fraction
field, which is why this file works over a field.
-/

namespace QOU.MassTheory.LevelWeightEnergy

variable {k F : Type*} [CommRing k] [Field F] [Algebra k F]

/-- The energy reading `U(m) = −q D m / m` (with `D = ∂_q`, this is `−q ∂_q log m`). -/
def energy (D : Derivation k F F) (q m : F) : F := -(q * D m / m)

/-- `ℏ_q = 1 − q⁻¹`. -/
def hbar (q : F) : F := 1 - q⁻¹

/-- **`U` is additive on products** of nonzero factors. -/
theorem energy_mul (D : Derivation k F F) (q : F) {m n : F} (hm : m ≠ 0) (hn : n ≠ 0) :
    energy D q (m * n) = energy D q m + energy D q n := by
  unfold energy
  rw [Derivation.leibniz, smul_eq_mul, smul_eq_mul]
  field_simp
  ring

theorem hbar_ne_zero {q : F} (_hq0 : q ≠ 0) (hq1 : q ≠ 1) : hbar q ≠ 0 := by
  unfold hbar
  intro h
  apply hq1
  have h' : q⁻¹ = 1 := (sub_eq_zero.mp h).symm
  rw [← inv_inv q, h', inv_one]

/-- **`U(ℏ_q) = −1/(q − 1)`.** -/
theorem energy_hbar (D : Derivation k F F) {q : F} (hD : D q = 1) (hq0 : q ≠ 0) (hq1 : q ≠ 1) :
    energy D q (hbar q) = -1 / (q - 1) := by
  have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  unfold energy hbar
  rw [map_sub, Derivation.map_one_eq_zero, Derivation.leibniz_inv, hD, smul_eq_mul]
  field_simp
  ring

/-- **`U(aⁿ) = n U(a)`** for `a ≠ 0`, `n ∈ ℤ`. -/
theorem energy_zpow (D : Derivation k F F) (q : F) {a : F} (ha : a ≠ 0) (n : ℤ) :
    energy D q (a ^ n) = n * energy D q a := by
  unfold energy
  rw [Derivation.leibniz_zpow, zsmul_eq_mul, smul_eq_mul, zpow_sub_one₀ ha]
  have han : a ^ n ≠ 0 := zpow_ne_zero n ha
  field_simp

/-- **A level factor shifts the energy by a pole:** `U(ℏ_q^k · m) = U(m) − k/(q − 1)`. -/
theorem energy_hbar_zpow_mul (D : Derivation k F F) {q : F} (hD : D q = 1) (hq0 : q ≠ 0)
    (hq1 : q ≠ 1) {m : F} (hm : m ≠ 0) (j : ℤ) :
    energy D q (hbar q ^ j * m) = energy D q m - j / (q - 1) := by
  have hh := hbar_ne_zero hq0 hq1
  rw [energy_mul D q (zpow_ne_zero j hh) hm, energy_zpow D q hh, energy_hbar D hD hq0 hq1]
  ring

/-- **Level `n` with weight `ℏ_q^(−2n)`:** `U = U(m) + 2n/(q − 1)`. Pole coefficient `+2n`. -/
theorem energy_level_mul (D : Derivation k F F) {q : F} (hD : D q = 1) (hq0 : q ≠ 0)
    (hq1 : q ≠ 1) {m : F} (hm : m ≠ 0) (n : ℕ) :
    energy D q (hbar q ^ (-2 * (n : ℤ)) * m) = energy D q m + 2 * n / (q - 1) := by
  rw [energy_hbar_zpow_mul D hD hq0 hq1 hm]
  push_cast
  ring

/-- **Level `n` with the tower's weight `ℏ_q^(2n)`:** `U = U(m) − 2n/(q − 1)`. Pole coefficient
`−2n`, the opposite sign. -/
theorem energy_tower_level_mul (D : Derivation k F F) {q : F} (hD : D q = 1) (hq0 : q ≠ 0)
    (hq1 : q ≠ 1) {m : F} (hm : m ≠ 0) (n : ℕ) :
    energy D q (hbar q ^ (2 * (n : ℤ)) * m) = energy D q m - 2 * n / (q - 1) := by
  rw [energy_hbar_zpow_mul D hD hq0 hq1 hm]
  push_cast
  ring

end QOU.MassTheory.LevelWeightEnergy
