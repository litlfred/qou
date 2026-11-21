import QOU.Infra.Polylogarithm

/-!
# General Cl_3 orbit sum at every N

Compiled formalisation of `prop:cyclotomic-cl3-orbit-sum-general`.
Sibling docstub at `braids-and-knots/cyclotomic-cl3-orbit-sum-general.lean`.
-/

namespace QOU.BraidKnot.CyclotomicCl3OrbitSum

open QOU.Infra.Polylogarithm

/-- **The `N = 5` closed form** (the Bring / `ζ₅` row of
    `prop:cyclotomic-cl3-orbit-sum-general`): the predicted orbit sum
    evaluates to `-(24/25) · ζ(3)`.

    **Restated 2026-08-21** (vacuity ledger, `proof-no-trivial-true` /
    `reflexive-tautology`).  This read
    `∀ N, 2 ≤ N → cl3OrbitSumPredicted N zeta3 = cl3OrbitSumPredicted N zeta3`,
    closed by `rfl` — both binders decoration, the claim holding for every
    `N` and every `zeta3` with or without `2 ≤ N`.  Its own docstring
    conceded the RHS "equals itself by `rfl`", yet the name promised a
    general orbit-sum identity, so a reader grepping for whether that
    identity is established found a green `theorem`.

    What is genuinely derivable here is the arithmetic at the verified
    index — the same computation `defaultTheoremB.value_at_5` performs, so
    it needs no class instance.  The **general-`N`** identification of the
    predicted closed form with the analytic orbit sum `Σ_k Cl₃(2πk/N)`
    remains conditional content, carried by `TheoremB.agrees_at`; it is
    *not* proved here and this statement does not imply it. -/
theorem orbit_sum_at_five (zeta3 : ℝ) :
    cl3OrbitSumPredicted 5 zeta3 = -(24 / 25) * zeta3 := by
  unfold cl3OrbitSumPredicted
  field_simp
  ring

/-- Adding the scaled constant to the predicted orbit sum at five cancels to zero (`qou-jtge`). -/
theorem orbit_sum_at_five_add_eq_zero (zeta3 : ℝ) :
    cl3OrbitSumPredicted 5 zeta3 + (24 / 25) * zeta3 = 0 := by
  rw [orbit_sum_at_five zeta3]
  ring

end QOU.BraidKnot.CyclotomicCl3OrbitSum
