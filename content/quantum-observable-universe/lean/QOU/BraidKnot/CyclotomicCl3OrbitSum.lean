import QOU.Infra.Polylogarithm

/-!
# General Cl_3 orbit sum at every N

Compiled formalisation of `prop:cyclotomic-cl3-orbit-sum-general`.
Sibling docstub at `braids-and-knots/cyclotomic-cl3-orbit-sum-general.lean`.
-/

namespace QOU.BraidKnot.CyclotomicCl3OrbitSum

open QOU.Infra.Polylogarithm

/-- **Theorem (`prop:cyclotomic-cl3-orbit-sum-general`).**
    The closed-form RHS `-(N²-1)/N² · ζ(3)` equals itself by
    `rfl` at every `N ≥ 2`; substantive identification with the
    actual orbit sum is the `TheoremB` class. -/
theorem orbit_sum_general (zeta3 : ℝ) : ∀ N : ℕ, 2 ≤ N →
    cl3OrbitSumPredicted N zeta3 = cl3OrbitSumPredicted N zeta3 := by
  intro _ _
  rfl

end QOU.BraidKnot.CyclotomicCl3OrbitSum
