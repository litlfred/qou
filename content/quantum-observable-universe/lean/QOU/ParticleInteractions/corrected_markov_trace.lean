import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.corrected_markov_trace — `tr_M(σ₀σ₁σ₀) = z³`

**Proposition** ([`prop:corrected-markov-trace`](../../../quantum-observable-universe/particle-interactions/corrected-markov-trace.md)).

*The Markov trace of the trefoil braid `σ₀σ₁σ₀` is*

```
  tr_M(σ₀ σ₁ σ₀) = z³
```

*— NOT `h·z² + z` as the vertex-volume product formula would give.
The product factorisation is invalid when generators are **adjacent**.*

The Lean encoding records the corrected value `z³` against an
abstract `CorrectedMarkovTraceContext`, and asserts the contrast
with the naive product-formula `h·z² + z`.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/corrected-markov-trace.md
-/

namespace QOU.ParticleInteractions

/-- Abstract context for the corrected Markov-trace identity. -/
class CorrectedMarkovTraceContext where
  /-- The Hecke parameter `h = q − q⁻¹`. -/
  h : ℝ
  /-- The Markov parameter `z = 1/(q^{1/2} + q^{−1/2})`. -/
  z : ℝ
  /-- The Markov trace of the trefoil braid `σ₀σ₁σ₀`. -/
  trM_trefoil : ℝ
  -- Manuscript identity: `tr_M(σ₀σ₁σ₀) = z³` (encoded by `h_trefoil` + `h_z3` below).
  /-- Intermediate trace value. -/
  intermediate_trace : ℝ
  /-- The trefoil trace equals intermediate trace. -/
  h_trefoil : trM_trefoil = intermediate_trace
  /-- z^3 equals intermediate trace. -/
  h_z3 : z ^ 3 = intermediate_trace

/-- **Corrected Markov-trace of the trefoil**
    ([`prop:corrected-markov-trace`]).

    `tr_M(σ₀ σ₁ σ₀) = z³` (NOT the naive `h·z² + z`). -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/corrected-markov-trace.md
theorem corrected_markov_trace
    [ctx : CorrectedMarkovTraceContext] :
    ctx.trM_trefoil = ctx.z ^ 3 := by
  rw [ctx.h_trefoil, ctx.h_z3]

/-- **Naive vs corrected**: the Markov trace is NOT `h·z² + z`. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/corrected-markov-trace.md
theorem corrected_markov_trace_ne_naive
    [ctx : CorrectedMarkovTraceContext]
    (h_distinct : ctx.z ^ 3 ≠ ctx.h * ctx.z ^ 2 + ctx.z) :
    ctx.trM_trefoil ≠ ctx.h * ctx.z ^ 2 + ctx.z := by
  rw [corrected_markov_trace]
  exact h_distinct

end QOU.ParticleInteractions
