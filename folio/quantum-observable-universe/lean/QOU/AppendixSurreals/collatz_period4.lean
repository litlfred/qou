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

/-- Over an integral domain where `2q² + 3q + 2 ≠ 0`, any `EOEO` 4-cycle forces
    `q · P₁ = 1` (so `P₁ = q⁻¹` is the fundamental 2-cycle traversed twice). -/
theorem qcollatz_period4_EOEO_reduces_to_two_cycle {R : Type*} [CommRing R] [IsDomain R]
    (q P0 P1 P2 P3 : R) (hd : 2 * q ^ 2 + 3 * q + 2 ≠ 0)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = (q ^ 2 + q + 1) * P1 + 1)
    (h3 : P3 * (q + 1) = P2)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) :
    q * P1 = 1 := by
  have heq := qcollatz_period4_EOEO q P0 P1 P2 P3 h1 h2 h3 h4
  have hfac : (2 * q ^ 2 + 3 * q + 2) * (q * P1 - 1) = 0 := by
    linear_combination heq
  rcases mul_eq_zero.mp hfac with h0 | h0
  · exact absurd h0 hd
  · linear_combination h0

/-- Height obstruction at `q = 1` for word `EEEO`: if `φ : R →+* ℤ` evaluates `q` to `1`,
    then `qcollatz_period4_EEEO` maps to `13 · φ(P₃) = 1` in `ℤ`, which has no solution. -/
theorem qcollatz_period4_EEEO_no_cycle_at_one {R : Type*} [CommRing R]
    (φ : R →+* ℤ) (q : R) (hq1 : φ q = 1) (P0 P1 P2 P3 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = P1) (h3 : P3 * (q + 1) = P2)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) : False := by
  have heq := congrArg φ (qcollatz_period4_EEEO q P0 P1 P2 P3 h1 h2 h3 h4)
  simp only [map_mul, map_add, map_pow, map_one, map_ofNat, hq1] at heq
  omega

/-- Height obstruction at `q = 1` for word `EEOO`: if `φ : R →+* ℤ` evaluates `q` to `1`,
    then `qcollatz_period4_EEOO` maps to `7 · φ(P₂) = 5` in `ℤ`, which has no solution. -/
theorem qcollatz_period4_EEOO_no_cycle_at_one {R : Type*} [CommRing R]
    (φ : R →+* ℤ) (q : R) (hq1 : φ q = 1) (P0 P1 P2 P3 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = P1)
    (h3 : P3 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) : False := by
  have heq := congrArg φ (qcollatz_period4_EEOO q P0 P1 P2 P3 h1 h2 h3 h4)
  simp only [map_mul, map_add, map_pow, map_ofNat, hq1] at heq
  omega

/-- Height obstruction at `q = 1` for word `EOOO`: if `φ : R →+* ℤ` evaluates `q` to `1`,
    then `qcollatz_period4_EOOO` maps to `11 · φ(P₁) = -19` in `ℤ`, which has no solution. -/
theorem qcollatz_period4_EOOO_no_cycle_at_one {R : Type*} [CommRing R]
    (φ : R →+* ℤ) (q : R) (hq1 : φ q = 1) (P0 P1 P2 P3 : R)
    (h1 : P1 * (q + 1) = P0) (h2 : P2 * (q + 1) = (q ^ 2 + q + 1) * P1 + 1)
    (h3 : P3 * (q + 1) = (q ^ 2 + q + 1) * P2 + 1)
    (h4 : P0 * (q + 1) = (q ^ 2 + q + 1) * P3 + 1) : False := by
  have heq := congrArg φ (qcollatz_period4_EOOO q P0 P1 P2 P3 h1 h2 h3 h4)
  simp only [map_mul, map_add, map_sub, map_neg, map_pow, map_one, map_ofNat, hq1] at heq
  omega

end QOU.AppendixSurreals
