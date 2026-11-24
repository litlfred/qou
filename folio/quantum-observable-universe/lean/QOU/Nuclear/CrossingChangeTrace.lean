/-
# A crossing change costs `h` times the smoothed trace

Bean `qou-99qc`, audit section 16. Owner choice "1 2" (2026-11-21): prove in Lean what can be
proved about the order at which an n/p splitting appears.

Every n/p construction on record changes crossings (`σ ↦ σ⁻¹`). In any algebra where a
generator satisfies the Hecke quadratic `g² = h·g + 1`, the inverse is `g - h` and a single
crossing change moves any linear functional by exactly `h` times its value on the smoothed
word. This is the algebraic kernel of the order counting in audit §16. It does not by itself
decide the order, because the smoothed traces can cancel.

## What is proved (generic commutative ring, generic algebra, no `sorry`)

* `inv_of_quadratic`: if `g * g = h • g + 1` then `g * (g - h • 1) = 1` and
  `(g - h • 1) * g = 1`.
* `crossing_change`: for every `R`-linear `tr : A →ₗ[R] R` and all `a b : A`,
  `tr (a * g * b) - tr (a * (g - h • 1) * b) = h * tr (a * b)`.

## What is NOT proved here

The closed form of the first-order term,
`tr(w) = 2^{-(n-c)} (1 + (2·writhe - 3·lk) (q - 1) + O((q-1)²))` for the `z_D` trace of an
`n`-strand braid whose closure has `c` components and total linking number `lk`. It is checked
exhaustively in `computations/qbeta/qbeta_splitting_first_order_linking_probe.py` (3 strands up
to length 7, 4 strands up to length 6), not proved. A Lean proof needs braid words, the
closure's component structure and a constructed Ocneanu trace on the Hecke tower, none of which
this file builds.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel

namespace QOU.QBeta.CrossingChangeTrace

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

theorem inv_of_quadratic {g : A} {h : R} (hg : g * g = h • g + 1) :
    g * (g - h • 1) = 1 ∧ (g - h • 1) * g = 1 := by
  constructor
  · rw [mul_sub, hg, mul_smul_comm, mul_one]; abel
  · rw [sub_mul, hg, smul_mul_assoc, one_mul]; abel

theorem crossing_change (tr : A →ₗ[R] R) (a b g : A) (h : R) :
    tr (a * g * b) - tr (a * (g - h • 1) * b) = h * tr (a * b) := by
  have e : a * (g - h • 1) * b = a * g * b - h • (a * b) := by
    rw [mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, mul_one]
  rw [e, map_sub, map_smul, smul_eq_mul]
  ring

end QOU.QBeta.CrossingChangeTrace
