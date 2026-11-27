import Mathlib.Tactic

/-!
# Period-4 Skein-Collatz cycle exclusion (Front B, B1)

Extends the period-1/2/3 no-cycle results one period further. Each primitive
length-4 parity word (`EEEO`, `EEOO`, `EOEO`, `EOOO`, up to rotation; `EEEE` is
the all-even case handled uniformly elsewhere) pins the cycle value to a
**non-unit** multiple in the Skein ring `ℤ[q^{±1}]` (whose only units are `±q^n`),
so there is no nontrivial period-4 cycle — except `EOEO`, which forces
`q·P₁ = 1` and hence degenerates to the fundamental 2-cycle `{q⁻¹, 1+q⁻¹}`
(imprimitive), not a new period-4 orbit.

Convention (as in the period-3 lemmas): a step `Pᵢ → Pⱼ` satisfies
`Pⱼ·(q+1) = Pᵢ` (even) or `Pⱼ·(q+1) = (q²+q+1)·Pᵢ + 1` (odd). All identities are
proved by `linear_combination` over a generic `[CommRing R]` (§7c).
-/

namespace QOU.AppendixSurreals

/-- **Period-4, word `EEEO`.** Forces `q·(q³+4q²+5q+3)·P₃ = 1`; the coefficient is
    a non-unit in `ℤ[q^{±1}]`, so no `EEEO` 4-cycle. -/
theorem qcollatz_period4_EEEO {R : Type*} [CommRing R] (q P0 P1 P2 P3 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = P1) (h3 : P3 * (q + 1) = P2)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) :
    q * (q ^ 3 + 4 * q ^ 2 + 5 * q + 3) * P3 = 1 := by
  linear_combination h4 + (q + 1) * h1 + (q + 1) ^ 2 * h2 + (q + 1) ^ 3 * h3

/-- **Period-4, word `EEOO`.** Forces `q·(2q²+3q+2)·P₂ = q²+2q+2`; non-unit
    coefficient with no matching Skein element, so no `EEOO` 4-cycle. -/
theorem qcollatz_period4_EEOO {R : Type*} [CommRing R] (q P0 P1 P2 P3 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = P1)
    (h3 : P3 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) :
    q * (2 * q ^ 2 + 3 * q + 2) * P2 = q ^ 2 + 2 * q + 2 := by
  linear_combination (q + 1) ^ 2 * h1 + (q + 1) ^ 3 * h2 + (q ^ 2 + q + 1) * h3
    + (q + 1) * h4

/-- **Period-4, word `EOEO`.** Forces `q·(2q²+3q+2)·P₁ = 2q²+3q+2`, i.e. (over an
    integral domain) `q·P₁ = 1`: `P₁ = q⁻¹`, the fundamental 2-cycle traversed
    twice. So `EOEO` is imprimitive — not a new period-4 cycle. -/
theorem qcollatz_period4_EOEO {R : Type*} [CommRing R] (q P0 P1 P2 P3 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = (q ^ 2 + q + 1) * P1 + 1)
    (h3 : P3 * (q + 1) = P2)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) :
    q * (2 * q ^ 2 + 3 * q + 2) * P1 = 2 * q ^ 2 + 3 * q + 2 := by
  linear_combination (q + 1) ^ 3 * h1 + (q ^ 2 + q + 1) * h2
    + (q ^ 2 + q + 1) * (q + 1) * h3 + (q + 1) ^ 2 * h4

/-- **Period-4, word `EOOO`.** Forces
    `q·(q⁵+3q⁴+5q³+3q²−1)·P₁ = −(q⁴+3q³+6q²+6q+3)`; non-unit coefficient, so no
    `EOOO` 4-cycle. With the other words (and their rotations) this excludes every
    nontrivial period-4 cycle. -/
theorem qcollatz_period4_EOOO {R : Type*} [CommRing R] (q P0 P1 P2 P3 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = (q ^ 2 + q + 1) * P1 + 1)
    (h3 : P3 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) :
    q * (q ^ 5 + 3 * q ^ 4 + 5 * q ^ 3 + 3 * q ^ 2 - 1) * P1
      = -(q ^ 4 + 3 * q ^ 3 + 6 * q ^ 2 + 6 * q + 3) := by
  linear_combination -((q + 1) ^ 3 * h1 + (q ^ 2 + q + 1) ^ 2 * h2
    + (q + 1) * (q ^ 2 + q + 1) * h3 + (q + 1) ^ 2 * h4)

/-- **Census → Lean bridge (`qcz16`), word `EEEO`.** Over `ℤ`, for any `1 ≤ q`
    and positive `1 ≤ P3`, no `EEEO` 4-cycle exists (`q(q³+4q²+5q+3)P₃ ≥ 13 > 1`). -/
theorem no_positive_period4_EEEO (q P0 P1 P2 P3 : ℤ)
    (hq : 1 ≤ q) (hP3 : 1 ≤ P3)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = P1) (h3 : P3 * (q + 1) = P2)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) : False := by
  have heq := qcollatz_period4_EEEO q P0 P1 P2 P3 h1 h2 h3 h4
  have hq2 : 0 ≤ q ^ 2 := sq_nonneg q
  have hq3 : 1 ≤ q ^ 3 := by nlinarith
  have hpoly : 13 ≤ q * (q ^ 3 + 4 * q ^ 2 + 5 * q + 3) := by nlinarith
  nlinarith

/-- **Census → Lean bridge (`qcz16`), word `EEOO`.** Over `ℤ`, for any `1 ≤ q`
    and positive `1 ≤ P2`, no `EEOO` 4-cycle exists. -/
theorem no_positive_period4_EEOO (q P0 P1 P2 P3 : ℤ)
    (hq : 1 ≤ q) (hP2 : 1 ≤ P2)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = P1)
    (h3 : P3 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) : False := by
  have heq := qcollatz_period4_EEOO q P0 P1 P2 P3 h1 h2 h3 h4
  have hq2 : 1 ≤ q ^ 2 := by nlinarith
  have hpoly : 0 < 2 * q ^ 2 + 3 * q + 2 := by nlinarith
  have hle : q * (2 * q ^ 2 + 3 * q + 2) * 1 ≤ q * (2 * q ^ 2 + 3 * q + 2) * P2 := by nlinarith
  nlinarith

/-- **Census → Lean bridge (`qcz16`), word `EOOO`.** Over `ℤ`, for any `1 ≤ q`
    and positive `1 ≤ P1`, no `EOOO` 4-cycle exists (LHS > 0 while RHS < 0). -/
theorem no_positive_period4_EOOO (q P0 P1 P2 P3 : ℤ)
    (hq : 1 ≤ q) (hP1 : 1 ≤ P1)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = (q ^ 2 + q + 1) * P1 + 1)
    (h3 : P3 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) : False := by
  have heq := qcollatz_period4_EOOO q P0 P1 P2 P3 h1 h2 h3 h4
  have hq2 : 1 ≤ q ^ 2 := by nlinarith
  have hq3 : 1 ≤ q ^ 3 := by nlinarith
  have hq4 : 1 ≤ q ^ 4 := by nlinarith
  have hq5 : 1 ≤ q ^ 5 := by nlinarith
  have hcoef : 11 ≤ q * (q ^ 5 + 3 * q ^ 4 + 5 * q ^ 3 + 3 * q ^ 2 - 1) := by nlinarith
  nlinarith

/-- **Census → Lean bridge (`qcz16`), word `EOEO`.** Over `ℤ`, for any `1 ≤ q`,
    an `EOEO` 4-cycle forces the fundamental 2-cycle equation `q * P1 = 1`. -/
theorem period4_EOEO_forces_fundamental (q P0 P1 P2 P3 : ℤ)
    (hq : 1 ≤ q)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = (q ^ 2 + q + 1) * P1 + 1)
    (h3 : P3 * (q + 1) = P2)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) :
    q * P1 = 1 := by
  have heq := qcollatz_period4_EOEO q P0 P1 P2 P3 h1 h2 h3 h4
  have hq2 : 1 ≤ q ^ 2 := by nlinarith
  have hpos : 0 < 2 * q ^ 2 + 3 * q + 2 := by nlinarith
  have hfac : (2 * q ^ 2 + 3 * q + 2) * (q * P1 - 1) = 0 := by linear_combination heq
  rcases mul_eq_zero.mp hfac with h0 | h1'
  · linarith
  · linarith

end QOU.AppendixSurreals
