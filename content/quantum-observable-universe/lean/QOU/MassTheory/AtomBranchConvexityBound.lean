/-
# The atom element's trace is capped by its largest branch — a convexity bound

`atom_braid_word_3A` returns an element of `H_n(q)` **outside** `im(ρ)`, so it has
no closure. But `tr_M` is linear on `H_n(q)`, and each letter `c·σ_g + d·1`
expands over `{σ_g, σ_g⁻¹}` via `σ⁻¹ = σ − h`. So

    atom = Σ_b w_b · ρ(β_b),      tr_M(atom) = Σ_b w_b · J_{K_b}(q)

over genuine braids `β_b`.  **Measured** (`atom_branch_convexity_bound_probe.py`,
3 assertions): the weights are a **convex combination** — every `w_b > 0` and
`Σ_b w_b = 1` exactly — at `A = 1, 2, 4`.

This file proves what follows: a convex combination cannot exceed its largest
term.  So the atom element's trace is capped by its best branch, turning
`2^(2A+1)` separate questions into one.

## What is deliberately NOT proved here

**No volume statement.**  It is tempting to push the bound through the
correspondence the cheat sheet writes as `tr_M ~ exp(Vol)` and conclude
`Vol_eff(atom) ≤ max_b Vol(K_b)`.  **That step is not licensed and is not taken.**
The volume conjecture is an asymptotic in the **colour** `N` at a root of unity,

    lim_{N→∞} (2π/N)·log|J_N(K; e^{2πi/N})| = Vol(K),

not a pointwise bound on the ordinary Jones value at fixed `q`.  Using it as one
is refuted by the corpus's own numbers: every `2H` branch closure was measured
non-hyperbolic, so a pointwise `|J| ≤ exp(Vol) = 1` would force
`|tr_M(atom)| ≤ 1`, while the production proton value is `1.1458`.

So the theorem below is about **traces**, which is what it says, and the volume
reading is left open.  `-- Ref: [kashaev1995]`

## Provenance

The convexity is measured, not assumed here — it enters as the hypotheses
`hw`/`hsum`, so this file proves an implication and never asserts the premise.
-/
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Positivity

namespace QOU.MassTheory

open Finset

/-- **A convex combination cannot exceed its largest term.**

If the weights `w` are non-negative and sum to `1`, and every `t i` is bounded in
absolute value by `M`, then so is `∑ w i * t i`.  Stated for an arbitrary finite
index set, so it applies to the `2^(2A+1)` branch expansion without that
expansion being formalised. -/
theorem abs_convex_combination_le {ι : Type*} (s : Finset ι) (w t : ι → ℝ)
    (M : ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hsum : ∑ i ∈ s, w i = 1)
    (ht : ∀ i ∈ s, |t i| ≤ M) :
    |∑ i ∈ s, w i * t i| ≤ M := by
  calc |∑ i ∈ s, w i * t i|
      ≤ ∑ i ∈ s, |w i * t i| := Finset.abs_sum_le_sum_abs _ _
    _ = ∑ i ∈ s, w i * |t i| := by
        refine Finset.sum_congr rfl fun i hi => ?_
        rw [abs_mul, abs_of_nonneg (hw i hi)]
    _ ≤ ∑ i ∈ s, w i * M := by
        refine Finset.sum_le_sum fun i hi => ?_
        exact mul_le_mul_of_nonneg_left (ht i hi) (hw i hi)
    _ = M := by rw [← Finset.sum_mul, hsum, one_mul]

/-- **The pruning consequence.**  The atom element's Markov trace is bounded by
the largest branch trace.  Since the bound is a single `max` over branches, the
question "can the atom carrier be large?" reduces from `2^(2A+1)` independent
questions to one: *is any single branch large?* -/
theorem atom_trace_le_max_branch {ι : Type*} (s : Finset ι) (w J : ι → ℝ)
    (M : ℝ) (hw : ∀ i ∈ s, 0 ≤ w i) (hsum : ∑ i ∈ s, w i = 1)
    (hJ : ∀ i ∈ s, |J i| ≤ M) :
    |∑ i ∈ s, w i * J i| ≤ M :=
  abs_convex_combination_le s w J M hw hsum hJ

/-- The bound is **sharp**: a one-branch expansion attains it.  Recorded so the
theorem above cannot be mistaken for a strict inequality, and so a future
strengthening has to confront the equality case. -/
theorem atom_trace_bound_is_sharp (J : ℝ) :
    |∑ _i ∈ ({0} : Finset ℕ), (1 : ℝ) * J| = |J| := by
  simp

end QOU.MassTheory
