import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

namespace QOU.BraidsAndKnots

open scoped BigOperators

/-- Context for the Markov-trace (Plancherel) normalization of `H_n(q)`.

    **Restated 2026-08-22** (vacuity ledger, `proof-no-trivial-true` /
    `proof-no-self-assuming-projection`).  The class previously carried the
    single field `holds : (1 : ℝ) = 1` — provable by `rfl`, so it constrained
    no instance, and the theorem below projected it to conclude `(1 : ℝ) = 1`:
    vacuous with *or* without an instance.

    The fields now state the actual categorical input the block names — the
    Wedderburn block dimensions `d_λ`, the Plancherel weights `y_λ(q)`, and the
    normalization identity `∑_λ d_λ · y_λ = 1`.  The normalization is the lone
    conditional hypothesis (the Markov-trace normalization of `H_n(q)`, assumed
    here, not derived). -/
class PlancherelViaRecipeContext (ι : Type*) [Fintype ι] where
  /-- The Wedderburn block dimensions `d_λ`. -/
  d : ι → ℝ
  /-- The Plancherel weights `y_λ(q)`. -/
  y : ι → ℝ
  /-- Markov-trace normalization for `H_n(q)`: `∑_λ d_λ · y_λ(q) = 1`. -/
  normalization : ∑ i, d i * y i = 1

/-- **Plancherel via the recipe.**  From the Markov-trace normalization
    `∑_λ d_λ · y_λ(q) = 1` it follows that not every Wedderburn block
    contributes zero weight: some block `λ` has `d_λ · y_λ ≠ 0`.

    §3b-conditional on `PlancherelViaRecipeContext`: the normalization itself is
    assumed, not established.  The conclusion is *derived* from the hypothesis
    (a sum equal to `1 ≠ 0` cannot have all terms zero) rather than projected
    from a conclusion field, so this is not a self-assuming projection. -/
theorem plancherel_via_recipe {ι : Type*} [Fintype ι]
    [ctx : PlancherelViaRecipeContext ι] :
    ∃ i : ι, ctx.d i * ctx.y i ≠ 0 := by
  by_contra h
  push_neg at h
  have hz : ∑ i, ctx.d i * ctx.y i = 0 := Finset.sum_eq_zero fun i _ => h i
  rw [ctx.normalization] at hz
  exact one_ne_zero hz

end QOU.BraidsAndKnots
