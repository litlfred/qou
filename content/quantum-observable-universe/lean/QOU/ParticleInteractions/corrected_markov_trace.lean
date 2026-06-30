import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.corrected_markov_trace — `tr_M(σ₀σ₁σ₀) = h·z² + z`

Canonical Lean for content block
[`prop:corrected-markov-trace`](../../../quantum-observable-universe/particle-interactions/corrected-markov-trace.md).

*The Markov trace of the trefoil braid `σ₀σ₁σ₀` is `h·z² + z` — NOT the
naive multiplicative product `z³`, which is invalid for adjacent
generators.*  Confirmed by the canonical `pyhecke` Markov-trace engine
(`computations/corrected-markov-trace.witness.json`).

The `.md` proof reduces the trace by trace **cyclicity** plus the Markov
property (`thm:jones-markov-trace`): cyclically rewrite `σ₀σ₁σ₀ = σ₀²σ₁`
so the maximal-index generator `σ₁` sits once at the end, peel it
(multiplying by `z`), then apply the Hecke relation `σ₀² = h·σ₀ + 1`.
This file derives `h·z² + z` **from those steps as hypotheses** — none
of which asserts the conclusion.

A prior version peeled the *minimal*-index generator `σ₀` three times
(`z·z·z = z³`); that reduction is invalid (the Markov property peels the
top generator, not an interior one) and is corrected here.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/corrected-markov-trace.md
-/

namespace QOU.ParticleInteractions

/-- **Markov trace of the trefoil** `tr_M(σ₀ σ₁ σ₀) = h·z² + z`, derived
from the reduction steps of the `.md` proof.

The hypotheses are exactly those steps:

* `h_single  : trM_σ0 = z`                     (single generator),
* `h_hecke   : trM_σ0sq = h * z + 1`           (Hecke `σ₀² = h σ₀ + 1`,
                                                 so `tr(σ₀²) = h·z + 1`),
* `h_reduce  : trM_σ0σ1σ0 = z * trM_σ0sq`      (cyclicity `σ₀σ₁σ₀ = σ₀²σ₁`
                                                 then Markov-peel the top
                                                 generator `σ₁`).

From these, `tr_M(σ₀σ₁σ₀) = z·(h·z + 1) = h·z² + z` by substitution and
`ring`.  None of the hypotheses asserts the conclusion.

**Base ring (§7c).** A polynomial identity (`+`, `*`, substitution); no
inverse, no `Real.*`, no ordering.  Stated over a generic commutative
ring `{R : Type*} [CommRing R]`. -/
-- Ref: [manuscript] thm:jones-markov-trace (Markov reduction property)
theorem corrected_markov_trace {R : Type*} [CommRing R]
    (h z trM_σ0 trM_σ0sq trM_σ0σ1σ0 : R)
    (h_single : trM_σ0 = z)
    (h_hecke : trM_σ0sq = h * z + 1)
    (h_reduce : trM_σ0σ1σ0 = z * trM_σ0sq) :
    trM_σ0σ1σ0 = h * z ^ 2 + z := by
  rw [h_reduce, h_hecke]; ring

/-- **Corrected vs naive**: the trefoil Markov trace `h·z² + z` is NOT the
naive multiplicative product `z³` (whenever those two scalars differ).

Combines `corrected_markov_trace` with the inequality hypothesis
`h·z² + z ≠ z³`. -/
-- Ref: [manuscript] prop:corrected-markov-trace (multiplicativity invalid for adjacent generators)
theorem corrected_markov_trace_ne_naive {R : Type*} [CommRing R]
    (h z trM_σ0 trM_σ0sq trM_σ0σ1σ0 : R)
    (h_single : trM_σ0 = z)
    (h_hecke : trM_σ0sq = h * z + 1)
    (h_reduce : trM_σ0σ1σ0 = z * trM_σ0sq)
    (h_distinct : h * z ^ 2 + z ≠ z ^ 3) :
    trM_σ0σ1σ0 ≠ z ^ 3 := by
  rw [corrected_markov_trace h z trM_σ0 trM_σ0sq trM_σ0σ1σ0 h_single h_hecke h_reduce]
  exact h_distinct

end QOU.ParticleInteractions
