/-
The algebraic layer of the deformed 4₁ saddle curve (A_ω tranche B).

The compute probe `computations/probes/qbeta_g3_deformed_saddle_exact_bridge.py`
re-derives, from the saddle equation of the 4₁ state integral
(GGM `library/arxiv-2012.00062v3/2012.00062v3.pdf`, eq (115)), the curve

    x·y² + (x² − x − 1)·y + 1 = 0        (the (116) glyph, minus restored)

and uses three algebraic facts as its self-certification controls. This file
proves those facts sorry-free over a generic commutative ring, so the
closed-form infrastructure is machine-checked rather than numerically
spot-checked:

* `discriminant_factorization` — the y-discriminant of the curve equals the
  printed (119) product: (x²−x−1)² − 4x = (x²−3x+1)(x²+x+1). Its roots are
  the branch points; the probe's "substrate meridian is generic" argument
  rests on this factorization.
* `curve_at_one` — at x = 1 the curve reduces to y² − y + 1 (whose roots are
  the sixth roots of unity e^{±iπ/3} — the u = 0 saddles of eq (38); the
  root identification itself is archimedean and stays on the compute side).
* `gamma_sq_eq_discriminant` — the Hessian combination γ² = x²·δ² satisfies
  x⁴·γ²-cleared form = the same (119) polynomial: x⁴−2x³−x²−2x+1 =
  (x²−3x+1)(x²+x+1), so the amplitude's branch locus coincides with the
  curve's.
* `curve_root_product` / `curve_root_sum` — Vieta data for the two saddles:
  if y₁, y₂ both lie on the curve and are distinct then x·y₁·y₂ = 1 and
  x·(y₁+y₂) = 1 + x − x², the exact-side inputs to the saddle-difference
  object ι̃ = (V(σ₁) − V(σ₂))/(2πi).

The transcendental part (Li₂ values, ι̃(0) = Vol(4₁)/π, the substrate
evaluation) is archimedean and lives in the witness — per the §7c wall this
file never mentions ℝ.
-/

import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.QBeta.DeformedSaddleCurve

variable {R : Type*} [CommRing R]

/-- The deformed 4₁ saddle curve `x·y² + (x²−x−1)·y + 1` (as an element of
`R`, vanishing exactly on the curve). Re-derived from the state-integral
saddle equation; reduces to `y² − y + 1` at `x = 1`. -/
def curve (x y : R) : R := x * y ^ 2 + (x ^ 2 - x - 1) * y + 1

/-- The y-discriminant of the curve factors as the printed (119) product:
`(x²−x−1)² − 4x = (x²−3x+1)(x²+x+1)`. -/
theorem discriminant_factorization (x : R) :
    (x ^ 2 - x - 1) ^ 2 - 4 * x = (x ^ 2 - 3 * x + 1) * (x ^ 2 + x + 1) := by
  ring

/-- At `x = 1` the curve reduces to `y² − y + 1` — the u = 0 saddle
equation (38), whose roots are the primitive sixth roots of unity. -/
theorem curve_at_one (y : R) : curve (1 : R) y = y ^ 2 - y + 1 := by
  simp only [curve]; ring

/-- The x-cleared Hessian-squared polynomial equals the same (119) product:
`x⁴ − 2x³ − x² − 2x + 1 = (x²−3x+1)(x²+x+1)` — the amplitude γ² and the
curve share their branch locus. -/
theorem gamma_sq_eq_discriminant (x : R) :
    x ^ 4 - 2 * x ^ 3 - x ^ 2 - 2 * x + 1
      = (x ^ 2 - 3 * x + 1) * (x ^ 2 + x + 1) := by
  ring

/-- Vieta, product form: two on-curve points at the same `x` satisfy
`(y₁ − y₂)·(x·y₁·y₂ − 1) = 0`; in particular distinct saddles (with `y₁ − y₂`
a nonzerodivisor) force `x·y₁·y₂ = 1`. Stated divisor-free so it holds over
any commutative ring. -/
theorem curve_root_product (x y₁ y₂ : R) :
    (y₁ - y₂) * (x * (y₁ * y₂) - 1) = y₂ * curve x y₁ - y₁ * curve x y₂ := by
  simp only [curve]; ring

/-- Vieta, sum form: `(y₁ − y₂)·(x·(y₁+y₂) − (1 + x − x²)) = curve x y₁ −
curve x y₂`; distinct saddles force `x·(y₁+y₂) = 1 + x − x²`. -/
theorem curve_root_sum (x y₁ y₂ : R) :
    (y₁ - y₂) * (x * (y₁ + y₂) - (1 + x - x ^ 2))
      = curve x y₁ - curve x y₂ := by
  simp only [curve]; ring

/-- The u = 0 saddles are primitive sixth roots of unity, cube form:
`y² − y + 1 = 0 → y³ = −1` (so the saddle values `e^{±iπ/3}` and the
u = 0 volume datum `Li₂(e^{±iπ/3})` sit at the hexagonal point). -/
theorem cube_at_saddle_one (y : R) (h : y ^ 2 - y + 1 = 0) :
    y ^ 3 = -1 := by
  linear_combination (y + 1) * h

/-- The u = 0 saddles are sixth roots of unity: `y² − y + 1 = 0 → y⁶ = 1`. -/
theorem sixth_power_at_saddle_one (y : R) (h : y ^ 2 - y + 1 = 0) :
    y ^ 6 = 1 := by
  linear_combination (y ^ 4 + y ^ 3 - y - 1) * h

/-- Saddle separation: under the Vieta relations of two on-curve saddles,
`x²·(y₁−y₂)² = (x²−3x+1)(x²+x+1)` — the squared saddle separation IS the
(119) discriminant product, so the branch locus of the Borel-singularity
datum `ι̃ ∝ V(σ₁) − V(σ₂)` is exactly the (119) zero set. This is the
algebraic core of the substrate-meridian-genericity argument. -/
theorem saddle_separation (x y₁ y₂ : R)
    (hs : x * (y₁ + y₂) = 1 + x - x ^ 2)
    (hp : x * (y₁ * y₂) = 1) :
    x ^ 2 * (y₁ - y₂) ^ 2 = (x ^ 2 - 3 * x + 1) * (x ^ 2 + x + 1) := by
  linear_combination
    (x * (y₁ + y₂) + (1 + x - x ^ 2)) * hs - 4 * x * hp

end QOU.QBeta.DeformedSaddleCurve
