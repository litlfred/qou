import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity

/-!
# The q-NS cone binders carried no weight

Run:  `LEAN_PATH=<mathlib oleans> lean <this file>`  ->  exit 0.

Statements copied VERBATIM from `ConditionalCorollaries.lean` as it
stood before 2026-08-30, with the `[QAubinLions] …` instance binders
DELETED.  They all elaborate, so the binders discharged nothing: three
theorems named for the q-NS conjecture cone were proving elementary
facts about real numbers.

`critical_exponent_identity_is_rfl` is the sharpest: `#print axioms`
reports it depends on **no axioms at all**, and the statement it
reproduces — `(3 * 4 : ℕ) = 12` — was documented as "the cleared form
of `α = 4/3`".  Clearing `α = 4/3` gives `3α = 4`; no `α` appeared.

The last two show the "existence" corollaries were degenerate in a
second way: their bounds force the witness to `0`.

Bean `qou-hjf4`.  Fix in the same commit; see
`docs/audits/2026-08-30-conditional-cone-repair.md`. -/

theorem reeb_period_bound_no_binders (Ω ε : ℝ) (h_Ω : 0 ≤ Ω) (h_ε : 0 ≤ ε) :
    0 ≤ Ω * ε := mul_nonneg h_Ω h_ε

theorem enstrophy_cube_bound_no_binders (Z : ℝ) (h_Z : 0 ≤ Z) :
    0 ≤ Z ^ 3 := pow_nonneg h_Z 3

theorem rogue_zero_cost_no_binders (δ ε : ℝ) (h_ε : 0 < ε) :
    0 ≤ δ ^ 2 / ε := div_nonneg (sq_nonneg δ) (le_of_lt h_ε)

/-- Both `critical_exponent_identity` and
    `qNS_critical_exponent_with_compactness` state this, each behind class
    binders. It is `rfl`. -/
theorem critical_exponent_identity_is_rfl : (3 * 4 : ℕ) = 12 := rfl

/-- `regularity_breakdown_measure_exists` states `∃ μ, 0 ≤ μ ∧ μ ≤ 0`,
    i.e. `μ = 0`. -/
theorem breakdown_measure_forces_zero : ∃ μ : ℝ, 0 ≤ μ ∧ μ ≤ (0 : ℝ) :=
  ⟨0, le_refl 0, le_refl 0⟩

/-- `qAubinLions_K_exists` states `∃ K, 0 ≤ K ∧ K ≤ 2 * 0`, i.e. `K = 0`. -/
theorem aubin_K_forces_zero : ∃ K : ℝ, 0 ≤ K ∧ K ≤ 2 * (0 : ℝ) :=
  ⟨0, le_refl 0, by norm_num⟩

#print axioms reeb_period_bound_no_binders
#print axioms enstrophy_cube_bound_no_binders
#print axioms rogue_zero_cost_no_binders
#print axioms critical_exponent_identity_is_rfl
