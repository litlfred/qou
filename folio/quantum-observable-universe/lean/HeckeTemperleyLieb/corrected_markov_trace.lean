import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Module.LinearMap.Defs
import Mathlib.Tactic.Ring

/-!
# QOU.ParticleInteractions.corrected_markov_trace — `tr_M(σ₀σ₁σ₀) = h·z² + z`

Canonical Lean for content block
[`prop:corrected-markov-trace`](../../../quantum-observable-universe/mass-theory/corrected-markov-trace.md).

**Corrected 2026-11-15.** This file used to derive `tr_M(σ₀σ₁σ₀) = z³`
from the hypothesis `tr_M(σ₀σ₁σ₀) = z · tr_M(σ₁σ₀)`. That hypothesis is
false: the Markov property `tr_M(x σ_n) = z · tr_M(x)` needs `x ∈ H_n`,
i.e. `σ_n` must be the maximal generator and must not occur in `x`. In
`σ₀σ₁σ₀` the outer `σ₀` is not maximal. The correct value is `h·z² + z`,
derived below from linearity, cyclicity, the Hecke relation and one
genuine application of the Markov property.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.ParticleInteractions

/-- **Markov trace of `σ₀σ₁σ₀`.** Let `tr : A → R` be `R`-linear, cyclic,
with `tr 1 = 1` and `tr σ₀ = z`, let `σ₀² = h•σ₀ + 1` (Hecke relation),
and let the Markov property hold for the word `σ₀² σ₁` (here `σ₀² ∈ H₂`
and `σ₁` is the maximal generator). Then `tr(σ₀σ₁σ₀) = h·z² + z`.

Proof: cyclicity gives `tr(σ₀σ₁σ₀) = tr(σ₀²σ₁)`; Markov gives
`z · tr(σ₀²)`; Hecke and linearity give `z · (h·z + 1)`. -/
-- Ref: [jones1987] https://doi.org/10.2307/1971403
theorem corrected_markov_trace {R A : Type*} [CommRing R] [Ring A] [Algebra R A]
    (tr : A →ₗ[R] R) (σ₀ σ₁ : A) (h z : R)
    (hecke : σ₀ * σ₀ = h • σ₀ + 1)
    (cyclic : ∀ a b : A, tr (a * b) = tr (b * a))
    (tr_one : tr 1 = 1) (tr_σ₀ : tr σ₀ = z)
    (markov : tr (σ₀ * σ₀ * σ₁) = z * tr (σ₀ * σ₀)) :
    tr (σ₀ * σ₁ * σ₀) = h * z ^ 2 + z := by
  have hc : tr (σ₀ * σ₁ * σ₀) = tr (σ₀ * σ₀ * σ₁) := by
    rw [cyclic (σ₀ * σ₁) σ₀, ← mul_assoc]
  rw [hc, markov, hecke, map_add, map_smul, tr_one, tr_σ₀, smul_eq_mul]
  ring

end QOU.ParticleInteractions
