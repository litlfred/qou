/-
# Binding q-Gaussian Habiro element — the `(q−1)`-order tower continues (`L₆`, `L₇`)

`QOU.Mass.BindingQGaussianHabiro` (PR #2899) certified the numerator `(q−1)`-order of the binding
q-Gaussian log-coefficients through `L₅`: `L₃, L₄ ∼ (q−1)²` and `L₅ ∼ (q−1)⁴`. This file extends
the tower to `L₆` and `L₇`, confirming the order law `e_m = 2⌊(m−1)/2⌋`:

    L₆ numerator = (q−1)⁴ · cofactor    (order e₆ = 4)
    L₇ numerator = (q−1)⁶ · cofactor    (order e₇ = 6 — the (q−1)⁶ tier)

So the q-Gaussian skeleton (`L₁ z + L₂ z²`) approximates the binding period EGF to ever-higher
order in `(q−1)`: each pair of log-degrees gains two more powers of `(q−1)`, the suppressed Habiro
tail. The numerator polynomials are the exact symbolic outputs of
`computations/substrate/lever1_binding_habiro_qexponential.py`; this file certifies their
`(q−1)`-divisibility by `ring` (machine-checked), citing the compute for provenance.

Generic base ring `[CommRing R]` (formal fibre parameter `q`, no archimedean structure, §7c).
Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md §"Stage 5"
-/
import Mathlib.Tactic

namespace QOU.Mass.BindingHabiroNumeratorTower

variable {R : Type*} [CommRing R]

/-- Expanded numerator of `L₆` (degree 26, palindromic). -/
def L6num (q : R) : R :=
  -q ^ 26 + 13 * q ^ 25 - 59 * q ^ 24 + 123 * q ^ 23 - 159 * q ^ 22 + 222 * q ^ 21
    - 345 * q ^ 20 + 419 * q ^ 19 - 459 * q ^ 18 + 575 * q ^ 17 - 693 * q ^ 16
    + 730 * q ^ 15 - 780 * q ^ 14 + 828 * q ^ 13 - 780 * q ^ 12 + 730 * q ^ 11
    - 693 * q ^ 10 + 575 * q ^ 9 - 459 * q ^ 8 + 419 * q ^ 7 - 345 * q ^ 6
    + 222 * q ^ 5 - 159 * q ^ 4 + 123 * q ^ 3 - 59 * q ^ 2 + 13 * q - 1

/-- Cofactor of `L₆` after removing `(q−1)⁴`. -/
def L6cof (q : R) : R :=
  -q ^ 22 + 9 * q ^ 21 - 17 * q ^ 20 - 3 * q ^ 19 - 32 * q ^ 18 + 35 * q ^ 17
    - 8 * q ^ 16 + 52 * q ^ 15 - 31 * q ^ 14 + 72 * q ^ 13 - 3 * q ^ 12 + 110 * q ^ 11
    - 3 * q ^ 10 + 72 * q ^ 9 - 31 * q ^ 8 + 52 * q ^ 7 - 8 * q ^ 6 + 35 * q ^ 5
    - 32 * q ^ 4 - 3 * q ^ 3 - 17 * q ^ 2 + 9 * q - 1

/-- **`L₆` carries `(q−1)⁴`** (order `e₆ = 4`). -/
theorem L6_factor (q : R) : L6num q = (q - 1) ^ 4 * L6cof q := by
  simp only [L6num, L6cof]; ring

/-- Expanded numerator of `L₇` (degree 34, palindromic). -/
def L7num (q : R) : R :=
  q ^ 34 - 17 * q ^ 33 + 114 * q ^ 32 - 402 * q ^ 31 + 858 * q ^ 30 - 1251 * q ^ 29
    + 1485 * q ^ 28 - 1806 * q ^ 27 + 2426 * q ^ 26 - 3226 * q ^ 25 + 3992 * q ^ 24
    - 4686 * q ^ 23 + 5341 * q ^ 22 - 5861 * q ^ 21 + 6176 * q ^ 20 - 6490 * q ^ 19
    + 6935 * q ^ 18 - 7178 * q ^ 17 + 6935 * q ^ 16 - 6490 * q ^ 15 + 6176 * q ^ 14
    - 5861 * q ^ 13 + 5341 * q ^ 12 - 4686 * q ^ 11 + 3992 * q ^ 10 - 3226 * q ^ 9
    + 2426 * q ^ 8 - 1806 * q ^ 7 + 1485 * q ^ 6 - 1251 * q ^ 5 + 858 * q ^ 4
    - 402 * q ^ 3 + 114 * q ^ 2 - 17 * q + 1

/-- Cofactor of `L₇` after removing `(q−1)⁶`. -/
def L7cof (q : R) : R :=
  q ^ 28 - 11 * q ^ 27 + 33 * q ^ 26 - 19 * q ^ 25 + 14 * q ^ 24 - 51 * q ^ 23
    + 27 * q ^ 22 - 105 * q ^ 21 + 14 * q ^ 20 - 159 * q ^ 19 + 3 * q ^ 18 - 215 * q ^ 17
    - 41 * q ^ 16 - 248 * q ^ 15 - 10 * q ^ 14 - 248 * q ^ 13 - 41 * q ^ 12 - 215 * q ^ 11
    + 3 * q ^ 10 - 159 * q ^ 9 + 14 * q ^ 8 - 105 * q ^ 7 + 27 * q ^ 6 - 51 * q ^ 5
    + 14 * q ^ 4 - 19 * q ^ 3 + 33 * q ^ 2 - 11 * q + 1

/-- **`L₇` carries `(q−1)⁶`** (order `e₇ = 6`) — the `(q−1)⁶` tier; the order law
`e_m = 2⌊(m−1)/2⌋` continues. -/
theorem L7_factor (q : R) : L7num q = (q - 1) ^ 6 * L7cof q := by
  simp only [L7num, L7cof]; ring

/-- Both higher log-coefficient numerators vanish at `q = 1` (the q-Gaussian skeleton is exact in
the classical limit, to order `(q−1)⁴` and `(q−1)⁶` respectively). -/
theorem L6num_vanishes_at_one : L6num (1 : R) = 0 := by rw [L6_factor]; ring
theorem L7num_vanishes_at_one : L7num (1 : R) = 0 := by rw [L7_factor]; ring

end QOU.Mass.BindingHabiroNumeratorTower
