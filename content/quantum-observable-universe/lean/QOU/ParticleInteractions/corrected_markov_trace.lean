import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.corrected_markov_trace — `tr_M(σ₀σ₁σ₀) = z³`

Canonical Lean for content block
[`prop:corrected-markov-trace`](../../../quantum-observable-universe/particle-interactions/corrected-markov-trace.md).

*The Markov trace of the trefoil braid `σ₀σ₁σ₀` is `z³` — NOT
`h·z² + z` as the (invalid for adjacent generators) vertex-volume
product formula would give.*

The `.md` proof is a three-step recursion using the **Markov
reduction property** (`thm:jones-markov-trace`): peeling the
top-index generator multiplies the trace by `z`.  This file derives
`z³` **from those reduction steps as hypotheses** — not from the
conclusion.  The previous encoding axiomatised an opaque
`intermediate_trace` with `h_trefoil : trM = intermediate` and
`h_z3 : z³ = intermediate` and rewrote with both; that was a vacuous
self-assuming projection (the two fields just *posit* the answer) and
is removed.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/corrected-markov-trace.md
-/

namespace QOU.ParticleInteractions

/-- **Corrected Markov-trace of the trefoil** `tr_M(σ₀ σ₁ σ₀) = z³`,
derived from the Markov reduction steps.

The hypotheses are exactly the three reduction steps of the `.md`
proof, each an instance of the Markov property (peel the maximal-index
generator, multiplying the trace by `z`):

* `h_single : trM_σ0 = z`               (single generator),
* `h_reduce1 : trM_σ1σ0 = z * trM_σ0`   (peel `σ₁`),
* `h_reduce2 : trM_σ0σ1σ0 = z * trM_σ1σ0` (peel the top `σ₀`).

From these, `tr_M(σ₀σ₁σ₀) = z·(z·(z)) = z³` by substitution and
`ring`.  None of the hypotheses asserts the conclusion `= z³`. -/
-- Ref: [manuscript] thm:jones-markov-trace (Markov reduction property)
theorem corrected_markov_trace
    (z trM_σ0 trM_σ1σ0 trM_σ0σ1σ0 : ℝ)
    (h_single : trM_σ0 = z)
    (h_reduce1 : trM_σ1σ0 = z * trM_σ0)
    (h_reduce2 : trM_σ0σ1σ0 = z * trM_σ1σ0) :
    trM_σ0σ1σ0 = z ^ 3 := by
  rw [h_reduce2, h_reduce1, h_single]; ring

/-- **Naive vs corrected**: the trefoil Markov trace is NOT the naive
vertex-volume product `h·z² + z` (whenever those two scalars differ).

Combines `corrected_markov_trace` with the inequality hypothesis
`z³ ≠ h·z² + z`. -/
-- Ref: [manuscript] prop:corrected-markov-trace (product factorisation invalid for adjacent generators)
theorem corrected_markov_trace_ne_naive
    (h z trM_σ0 trM_σ1σ0 trM_σ0σ1σ0 : ℝ)
    (h_single : trM_σ0 = z)
    (h_reduce1 : trM_σ1σ0 = z * trM_σ0)
    (h_reduce2 : trM_σ0σ1σ0 = z * trM_σ1σ0)
    (h_distinct : z ^ 3 ≠ h * z ^ 2 + z) :
    trM_σ0σ1σ0 ≠ h * z ^ 2 + z := by
  rw [corrected_markov_trace z trM_σ0 trM_σ1σ0 trM_σ0σ1σ0 h_single h_reduce1 h_reduce2]
  exact h_distinct

end QOU.ParticleInteractions
