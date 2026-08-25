/-
  Toroidal locus of the Hoefsmit mixing ladder.

  Matching the associated-Legendre order-ladder factor (n - μ)(n + μ + 1),
  at degree n = d + α and order μ = β, against the squared Hoefsmit
  channel-mixing numerator d² - 1 IDENTICALLY in the axial distance d
  forces α = -1/2 and β ∈ {1/2, -3/2}: the half-integer degree shift of
  the toroidal harmonic family P^μ_{ν-1/2} is derived, not imposed.

  ## Base ring (AGENTS.md §7c)

  Generic `[CommRing R] [IsDomain R]` — no `ℝ`, no ordering, no radical;
  the argument is pure polynomial-coefficient matching.  Two §7c points,
  both adjudicated rather than assumed:

  * **Division-free half-integers.**  The shifts are stated as the
    multiplicative relations `2α = -1` and `2β = 1` / `2β = -3` instead of
    `α = -(1/2)`, `β = 1/2` / `-(3/2)` (the R[h] pattern).  This needs no
    `Invertible (2 : R)` hypothesis: `2α = -1` says `2 · (-α) = 1`, so the
    invertibility of `2` is *derived* from the forcing hypothesis rather
    than assumed — which is also why the old `[CharZero R]` is no longer
    needed and has been dropped.
  * **`IsDomain` is essential; bare `CommRing` is FALSE.**  The forcing
    step ends at `(2β - 1)(2β + 3) = 0` and concludes by `mul_eq_zero`,
    which needs `NoZeroDivisors`.  Over a product ring the conclusion
    genuinely fails: in `R = ℤ[1/2] × ℤ[1/2]` take `α = (-1/2, -1/2)` and
    `β = (-3/2, 1/2)`, so that `α - β = (1, -1)` squares to `1` and the
    ladder identity holds for every `d` — yet `2β = (-3, 1)` is neither
    `1` nor `-3`.  So a domain, not a field, is the weakest §7c class here.

  -- Ref: [whipple1917] https://doi.org/10.1112/plms/s2-16.1.301
  -- Ref: [wenzl1988c] https://doi.org/10.1007/BF01388470
-/

import Mathlib.Algebra.GroupWithZero.Basic
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R]

/-- The toroidal locus is valid: at α = -1/2, β = 1/2 — division-free,
    `2α = -1` and `2β = 1` — the ladder factor reproduces `d² - 1` for
    every `d`.  No `IsDomain` and no `Invertible 2` is needed: the
    hypothesis `2 * α = -1` already exhibits `-α` as an inverse of `2`. -/
theorem toroidal_locus_valid (α β : R) (hα : 2 * α = -1) (hβ : 2 * β = 1)
    (d : R) :
    (d + α - β) * (d + α + β + 1) = d ^ 2 - 1 := by
  have hu : (2 : R) * (-α) = 1 := by linear_combination -hα
  have h2t : (2 : R) * (α - β) = -2 := by linear_combination hα - hβ
  have ht : α - β = -1 := by
    calc α - β = (2 * (-α)) * (α - β) := by rw [hu, one_mul]
      _ = (-α) * (2 * (α - β)) := by ring
      _ = (-α) * (-2) := by rw [h2t]
      _ = -1 := by linear_combination hα
  have hs : α + β + 1 = 1 := by linear_combination hα - ht
  linear_combination d * hα + (α - β) * hs + ht

/-- **Uniqueness (the forcing theorem).** If the ladder factor at constant
    shifts `(α, β)` reproduces `d² - 1` identically in `d`, then
    `α = -1/2` and `β ∈ {1/2, -3/2}` (the Legendre reflection pair
    `μ ↔ -μ - 1`), stated division-free as `2α = -1` and
    `2β ∈ {1, -3}`. The half-integer degree shift is forced.

    `[IsDomain R]` is load-bearing — see the module note for the
    product-ring counterexample that breaks this over a bare `CommRing`. -/
theorem toroidal_locus_forced [IsDomain R] (α β : R)
    (h : ∀ d : R, (d + α - β) * (d + α + β + 1) = d ^ 2 - 1) :
    2 * α = -1 ∧ (2 * β = 1 ∨ 2 * β = -3) := by
  have hα : 2 * α = -1 := by linear_combination h 1 - h 0
  refine ⟨hα, ?_⟩
  have hfac : (2 * β - 1) * (2 * β + 3) = 0 := by
    linear_combination (-4 : R) * h 0 + (2 * α + 1) * hα
  rcases mul_eq_zero.mp hfac with hb | hb
  · exact Or.inl (by linear_combination hb)
  · exact Or.inr (by linear_combination hb)

end QOU.BraidsAndKnots
