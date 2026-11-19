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
import Mathlib.Algebra.Ring.Invertible
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace QOU.BraidsAndKnots

variable {R : Type*} [CommRing R]

/-- **The Legendre reflection `μ ↦ -μ - 1`** on the order parameter `μ` of the
    associated-Legendre factor `(n - μ)(n + μ + 1)`. -/
def legendreReflect (μ : R) : R := -μ - 1

/-- `legendreReflect` is an involution: `legendreReflect (legendreReflect μ) = μ`. -/
@[simp]
theorem legendreReflect_involutive (μ : R) :
    legendreReflect (legendreReflect μ) = μ := by
  unfold legendreReflect
  ring

/-- The associated-Legendre order-ladder factor `(n - μ)(n + μ + 1)` is invariant
    under the Legendre reflection `μ ↦ -μ - 1`. -/
theorem legendre_ladder_reflect_invariant (n μ : R) :
    (n - legendreReflect μ) * (n + legendreReflect μ + 1) =
    (n - μ) * (n + μ + 1) := by
  unfold legendreReflect
  ring

/-- In division-free form, `2 * β = 1` iff `2 * (legendreReflect β) = -3`. -/
theorem two_mul_legendreReflect_eq_neg_three_iff (β : R) :
    2 * legendreReflect β = -3 ↔ 2 * β = 1 := by
  unfold legendreReflect
  constructor <;> (intro h; linear_combination -h)

/-- When `2` is invertible in `R`, `legendreReflect` exchanges `1/2 = ⅟(2 : R)`
    and `-3/2 = -3 * ⅟(2 : R)`. -/
theorem legendreReflect_half [Invertible (2 : R)] :
    legendreReflect (⅟(2 : R)) = -3 * ⅟(2 : R) ∧
    legendreReflect (-3 * ⅟(2 : R)) = ⅟(2 : R) := by
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self (2 : R)
  unfold legendreReflect
  refine ⟨?_, ?_⟩
  · linear_combination h2
  · linear_combination h2

/-- The toroidal locus is valid at `2α = -1` and `2β = 1`.
    No `IsDomain` and no `Invertible 2` is needed: the hypothesis `2 * α = -1`
    already exhibits `-α` as an inverse of `2`. -/
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

/-- **Validity on both Legendre-reflected branches (`2β = 1 ∨ 2β = -3`):**
    whenever `2 * α = -1` and `2 * β = 1 ∨ 2 * β = -3`, the ladder factor reproduces
    `d² - 1` for every `d : R`. -/
theorem toroidal_locus_valid_both (α β : R) (hα : 2 * α = -1)
    (hβ : 2 * β = 1 ∨ 2 * β = -3) (d : R) :
    (d + α - β) * (d + α + β + 1) = d ^ 2 - 1 := by
  rcases hβ with h1 | h3
  · exact toroidal_locus_valid α β hα h1 d
  · rw [← legendre_ladder_reflect_invariant (d + α) β]
    have h1 : 2 * legendreReflect β = 1 := by
      unfold legendreReflect
      linear_combination -h3
    exact toroidal_locus_valid α (legendreReflect β) hα h1 d

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

/-- **Two-way equivalence (`↔`) in division-free form over any integral domain `R`:**
    `(∀ d : R, (d + α - β)(d + α + β + 1) = d² - 1) ↔ 2α = -1 ∧ (2β = 1 ∨ 2β = -3)`. -/
theorem toroidal_locus_iff_mul [IsDomain R] (α β : R) :
    (∀ d : R, (d + α - β) * (d + α + β + 1) = d ^ 2 - 1) ↔
      2 * α = -1 ∧ (2 * β = 1 ∨ 2 * β = -3) :=
  ⟨toroidal_locus_forced α β, fun ⟨hα, hβ⟩ => toroidal_locus_valid_both α β hα hβ⟩

/-- **Two-way equivalence (`↔`) in explicit half-integer form (`-1/2`, `1/2`, `-3/2`):**
    When `2` is invertible in the domain `R` (in particular for any field of
    characteristic zero), the ladder identity holds for all `d : R` if and only if
    `α = -⅟(2 : R)` and `β = ⅟(2 : R) ∨ β = legendreReflect (⅟(2 : R))` (`= -3 * ⅟(2 : R)`). -/
theorem toroidal_locus_iff [IsDomain R] [Invertible (2 : R)] (α β : R) :
    (∀ d : R, (d + α - β) * (d + α + β + 1) = d ^ 2 - 1) ↔
      α = -⅟(2 : R) ∧ (β = ⅟(2 : R) ∨ β = legendreReflect (⅟(2 : R))) := by
  have h2 : (2 : R) * ⅟(2 : R) = 1 := mul_invOf_self (2 : R)
  rw [toroidal_locus_iff_mul, (legendreReflect_half (R := R)).1]
  refine and_congr ?_ (or_congr ?_ ?_)
  · constructor
    · intro hα
      linear_combination ⅟(2 : R) * hα - α * h2
    · intro hα
      linear_combination 2 * hα - h2
  · constructor
    · intro hβ
      linear_combination ⅟(2 : R) * hβ - β * h2
    · intro hβ
      linear_combination 2 * hβ + h2
  · constructor
    · intro hβ
      linear_combination ⅟(2 : R) * hβ - β * h2
    · intro hβ
      linear_combination 2 * hβ - 3 * h2

end QOU.BraidsAndKnots
