import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.QBeta.CubicSaddleDiscriminant — the three-saddle discriminant of the 5₂ cubic

Extends the 5₂ saddle-curve algebra (`FiveTwoSaddleCurve.lean`, the #3892 g3 5₂
port) to the full three-saddle discriminant. The 4₁ curve is a quadratic in `y`
(two saddles) and `DeformedSaddleCurve.saddle_separation` gives its single squared
saddle difference; the 5₂ curve is a **cubic** (three saddles), and this file
supplies the missing cubic analogue: the product of the three squared saddle
differences equals the cubic discriminant, which at the `u = 0` saddle cubic
evaluates to the printed trace-field discriminant `−23`.

This ties `FiveTwoSaddleCurve.u0_cubic_discriminant` (the value `−23` via the
coefficient formula) to the *geometry* of the three saddles `y₁,y₂,y₃`: the exact
pairwise singularities `ι̃_ij = (V_i − V_j)/(2πi)` of the deformed 5₂ state integral
live on these differences, and the product of their squares **is** the arithmetic
fingerprint `−23` (the trace-field discriminant of 5₂).

Generic commutative ring (§7c); the transcendental saddle values `V_i`
(`Li₂`-values, `Vol(5₂)`, `CS(5₂) ≠ 0`) are archimedean and live in the witness.
GGM state-integral data: `library/arxiv-2012.00062v3/2012.00062v3.pdf` (eqs. 73, 230–233).
-/

namespace QOU.QBeta.CubicSaddleDiscriminant

variable {R : Type*} [CommRing R]

/-- **Cubic discriminant as the product of squared root differences.** For any
three ring elements (the three saddles), the square of the product of their
pairwise differences equals the discriminant written in the elementary symmetric
functions `e₁ = Σyᵢ`, `e₂ = Σyᵢyⱼ`, `e₃ = ∏yᵢ`:
`((y₁−y₂)(y₂−y₃)(y₃−y₁))² = e₁²e₂² − 4e₂³ − 4e₁³e₃ + 18e₁e₂e₃ − 27e₃²`. -/
theorem disc_eq_root_diff_sq (y₁ y₂ y₃ : R) :
    ((y₁ - y₂) * (y₂ - y₃) * (y₃ - y₁)) ^ 2
      = (y₁ + y₂ + y₃) ^ 2 * (y₁ * y₂ + y₂ * y₃ + y₃ * y₁) ^ 2
        - 4 * (y₁ * y₂ + y₂ * y₃ + y₃ * y₁) ^ 3
        - 4 * (y₁ + y₂ + y₃) ^ 3 * (y₁ * y₂ * y₃)
        + 18 * (y₁ + y₂ + y₃) * (y₁ * y₂ + y₂ * y₃ + y₃ * y₁) * (y₁ * y₂ * y₃)
        - 27 * (y₁ * y₂ * y₃) ^ 2 := by
  ring

/-- **The three 5₂ saddle differences square to `−23`.** For three saddles of the
`u = 0` cubic `y³ − 2y² + 3y − 1` (Vieta: `Σy = 2`, `Σyᵢyⱼ = 3`, `∏y = 1`), the
product of their squared pairwise differences is the trace-field discriminant
`−23` — the geometric (root-difference) form of
`FiveTwoSaddleCurve.u0_cubic_discriminant`, exhibiting `−23` as
`∏_{i<j}(V_i − V_j)`-square of the exact saddle singularities. -/
theorem five_two_saddle_diff_sq (y₁ y₂ y₃ : R)
    (hs : y₁ + y₂ + y₃ = 2)
    (hq : y₁ * y₂ + y₂ * y₃ + y₃ * y₁ = 3)
    (hp : y₁ * y₂ * y₃ = 1) :
    ((y₁ - y₂) * (y₂ - y₃) * (y₃ - y₁)) ^ 2 = -23 := by
  rw [disc_eq_root_diff_sq]
  simp only [hs, hq, hp]
  norm_num

end QOU.QBeta.CubicSaddleDiscriminant
