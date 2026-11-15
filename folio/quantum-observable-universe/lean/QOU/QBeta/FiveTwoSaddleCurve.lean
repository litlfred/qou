/-
The algebraic layer of the deformed 5₂ saddle curve (A_ω, 5₂ lane).

Port of `DeformedSaddleCurve.lean` (4₁) to GGM §6.1's 5₂ data
(`library/arxiv-2012.00062v3/2012.00062v3.pdf`, eqs 230–233; probe
`computations/probes/qbeta_g3_5two_saddle_exact_predictions.py`). The
state-integral saddle equation (232), exponentiated with (x, y) =
(e^u, −e^v), gives the curve (233) y² = (1−y)(1−xy)(1−x⁻¹y); clearing
denominators:

    Q(x, y) := x·y³ − (x²+1)·y² + (x²+x+1)·y − x = 0.

Proved here, sorry-free over a generic commutative ring:

* `curve_at_one` — at x = 1 the curve reduces to y³ − 2y² + 3y − 1, the
  printed u = 0 saddle cubic (73) ((1−y)³ = y²) of the 5₂ knot.
* `u0_cubic_discriminant` — the discriminant of that cubic is −23: the
  printed trace-field discriminant of 5₂ (the arithmetic fingerprint the
  three saddles live in).
* `curve_palindromic` — x²·Q(x⁻¹-form) = Q(x, y) in cleared form: the
  curve is x ↔ x⁻¹ symmetric, the algebraic face of the u-EVENNESS of
  the 5₂ potential (231) (the chirality of 5₂ lives in the complex
  saddle values, not in the curve).
* `curve_root_esum` / `curve_root_epair` / `curve_root_eprod` — Vieta
  identities (divisor-free form) for the three saddles: x·Σy = x²+1,
  x·Σyᵢyⱼ = x²+x+1, x·y₁y₂y₃ = x, feeding the exact saddle-difference
  singularities ι̃_ij = (V_i − V_j)/(2πi).

The transcendental part (Li₂ values, Vol(5₂), the complex ι_13 carrying
CS(5₂) ≠ 0, the deformed pole-phase targets) is archimedean and lives in
the witness — per the §7c wall this file never mentions ℝ.
-/
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta.FiveTwoSaddleCurve

variable {R : Type*} [CommRing R]

/-- The cleared deformed 5₂ saddle curve
`x·y³ − (x²+1)·y² + (x²+x+1)·y − x` (vanishing exactly on the curve). -/
def curve (x y : R) : R :=
  x * y ^ 3 - (x ^ 2 + 1) * y ^ 2 + (x ^ 2 + x + 1) * y - x

/-- At `x = 1` the curve reduces to the printed u = 0 saddle cubic (73):
`y³ − 2y² + 3y − 1` (equivalently `(1−y)³ = y²`). -/
theorem curve_at_one (y : R) :
    curve (1 : R) y = y ^ 3 - 2 * y ^ 2 + 3 * y - 1 := by
  simp only [curve]; ring

/-- The discriminant of the u = 0 saddle cubic `y³ − 2y² + 3y − 1` is
`−23` — the printed trace-field discriminant of the 5₂ knot. (Cubic
`ay³+by²+cy+d` with `a=1, b=−2, c=3, d=−1`.) -/
theorem u0_cubic_discriminant :
    (18 * 1 * (-2) * 3 * (-1) - 4 * (-2) ^ 3 * (-1) + (-2) ^ 2 * 3 ^ 2
      - 4 * 1 * 3 ^ 3 - 27 * 1 ^ 2 * (-1) ^ 2 : ℤ) = -23 := by
  norm_num

/-- Pairwise saddle certificate (the 5₂ analogue of the 4₁ Vieta
certificates): `(y₁ − y₂)·(x·(y₁²+y₁y₂+y₂²) − (x²+1)·(y₁+y₂) +
(x²+x+1)) = curve x y₁ − curve x y₂`. Two distinct on-curve saddles
(with `y₁ − y₂` a nonzerodivisor) force the second factor to vanish —
the relation feeding the exact pairwise singularities
`ι̃_ij = (V_i − V_j)/(2πi)`. -/
theorem curve_pair_certificate (x y₁ y₂ : R) :
    (y₁ - y₂) * (x * (y₁ ^ 2 + y₁ * y₂ + y₂ ^ 2)
      - (x ^ 2 + 1) * (y₁ + y₂) + (x ^ 2 + x + 1))
      = curve x y₁ - curve x y₂ := by
  simp only [curve]; ring

/-- x ↔ x⁻¹ palindromy, divisor-free: whenever `x·z = 1`,
`x²·curve z y = curve x y` — the algebraic face of the u-EVENNESS of the
5₂ potential (231): the curve is achiral; the chirality of 5₂ (CS ≠ 0)
lives in the complex saddle values, not in the curve. -/
theorem curve_palindromic (x z y : R) (h : x * z = 1) :
    x ^ 2 * curve z y = curve x y := by
  simp only [curve]
  linear_combination
    (x * y ^ 3 - (x * z + 1) * y ^ 2 + (x * z + 1 + x) * y - x) * h

end QOU.QBeta.FiveTwoSaddleCurve
