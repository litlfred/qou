/-
# Saturation ρ-cap: the isospin-even exchange cumulant caps ρ_A ≤ C(A,2)

For the isospin-even complete-graph exchange matrix `I + m(J − I)` on `A`
nucleons (the strong sector is isospin-blind, see
`QOU.MassTheory.IsospinMirrorInvariance`), the exact spectrum
`{1 + (A−1)m, (1−m)^{×(A−1)}}` gives the determinant
`det_A = (1 + (A−1)m)(1−m)^{A−1}`, so the connected cumulant
`b_A = −ln det_A` is extensive and *saturates* (`b_A/A → −ln(1−m)`).
Saturation, however, caps the binding-magnitude ratio: for every
`m ∈ [0,1]`, `ρ_A = b_A/b_2 ≤ C(A,2) = A(A−1)/2`.

Because `b_2 = −ln(1−m²) > 0`, the bound `ρ_A ≤ C(A,2)` is equivalent to
the **log-free polynomial** form `det_A ≥ (1−m²)^{C(A,2)}`.  This file
machine-verifies the two decisive instances:

  A=3:  (1+2m)(1−m)² ≥ (1−m²)³   ⟺ ρ₃ ≤ 3
  A=4:  (1+3m)(1−m)³ ≥ (1−m²)⁶   ⟺ ρ₄ ≤ 6

The isospin-corrected strong targets `ρ_strong(3) ≈ 3.8 > 3` and
`ρ_strong(4) ≈ 13 > 6` exceed these caps, so the isospin-even cumulant
cannot reach the strong ρ for **any** `m ∈ [0,1]` — a scope-(b)
structural exclusion of the saturation route (PR #4004).  Base ring `ℝ`
per §7c (the statement is an ordering inequality on `0 ≤ m ≤ 1`).

Each cap reduces, via an exact `ring` factorisation, to a product of
manifestly non-negative factors on `[0,1]`.
-/
import Mathlib.Tactic

namespace QOU.MassTheory

/-- **A=3 saturation cap** (log-free): `det₃ = (1+2m)(1−m)² ≥ (1−m²)³`,
equivalently `ρ₃ ≤ 3`.  The exact factorisation
`(1+2m)(1−m)² − (1−m²)³ = m³(1−m)²(2+m)` exhibits the gap as a product of
non-negative factors on `[0,1]`. -/
theorem saturation_rho_cap_three (m : ℝ) (h0 : 0 ≤ m) (_h1 : m ≤ 1) :
    (1 - m ^ 2) ^ 3 ≤ (1 + 2 * m) * (1 - m) ^ 2 := by
  have key : (1 + 2 * m) * (1 - m) ^ 2 - (1 - m ^ 2) ^ 3
      = m ^ 3 * (1 - m) ^ 2 * (2 + m) := by ring
  nlinarith [mul_nonneg (mul_nonneg (pow_nonneg h0 3) (sq_nonneg (1 - m)))
    (by linarith : (0 : ℝ) ≤ 2 + m), key]

/-- **A=4 saturation cap** (log-free): `det₄ = (1+3m)(1−m)³ ≥ (1−m²)⁶`,
equivalently `ρ₄ ≤ 6`.  The ⁴He strong target `ρ_strong(4) ≈ 13` exceeds
this cap of `6`, so the isospin-even cumulant cannot supply the ⁴He
binding magnitude for any `m`.  The gap factorises as
`m³(1−m)³·h(m)` with `h(m) = 8 + 6m − 6m² − 8m³ + 3m⁵ + m⁶`, and
`h(m) = 8(1−m) + 6(m−m²) + 8(m−m³) + 3m⁵ + m⁶ ≥ 0` on `[0,1]`. -/
theorem saturation_rho_cap_four (m : ℝ) (h0 : 0 ≤ m) (h1 : m ≤ 1) :
    (1 - m ^ 2) ^ 6 ≤ (1 + 3 * m) * (1 - m) ^ 3 := by
  have hm2 : 0 ≤ m - m ^ 2 := by nlinarith [mul_nonneg h0 (sub_nonneg.2 h1)]
  have hm3 : 0 ≤ m - m ^ 3 := by
    nlinarith [mul_nonneg (mul_nonneg h0 (sub_nonneg.2 h1))
      (by linarith : (0 : ℝ) ≤ 1 + m)]
  have hh : 0 ≤ 8 + 6 * m - 6 * m ^ 2 - 8 * m ^ 3 + 3 * m ^ 5 + m ^ 6 := by
    nlinarith [sub_nonneg.2 h1, hm2, hm3, pow_nonneg h0 5, pow_nonneg h0 6]
  have key : (1 + 3 * m) * (1 - m) ^ 3 - (1 - m ^ 2) ^ 6
      = m ^ 3 * (1 - m) ^ 3 * (8 + 6 * m - 6 * m ^ 2 - 8 * m ^ 3 + 3 * m ^ 5 + m ^ 6) := by
    ring
  nlinarith [mul_nonneg (mul_nonneg (pow_nonneg h0 3)
    (pow_nonneg (sub_nonneg.2 h1) 3)) hh, key]

end QOU.MassTheory
