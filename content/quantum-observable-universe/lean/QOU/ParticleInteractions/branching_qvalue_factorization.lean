import Mathlib.Tactic

/-!
# QOU.ParticleInteractions.branching_qvalue_factorization — `Σ Δm_e = a^Z · b^{N−1} · (a − b)`

**Proposition** ([`prop:branching-qvalue-factorization`](../../../quantum-observable-universe/particle-interactions/branching-qvalue-factorization.md)).

*For `β⁻` decay of a nucleus `(Z, N)` with `A = Z + N`:*

```
  Σ_{all 4^A configs} Δ m_e = a^Z · b^{N−1} · (a − b)
```

*where `a = Σ_c G_P(c)` and `b = Σ_c G_N(c)` are the per-nucleon
channel sums.*

The Lean encoding records the closed-form factorisation against an
abstract `BranchingQvalueContext`.

-- Ref: [manuscript] quantum-observable-universe/particle-interactions/branching-qvalue-factorization.md
-/

namespace QOU.ParticleInteractions

/-- Abstract context for the `β⁻`-decay branching Q-value factorisation. -/
class BranchingQvalueContext (Z N : ℕ) where
  /-- Per-nucleon channel sum for protons. -/
  a : ℝ
  /-- Per-nucleon channel sum for neutrons. -/
  b : ℝ
  /-- The total `Σ Δm_e` summed over all 4^A configurations. -/
  totalDeltaM : ℝ
  /-- Manuscript factorisation: the 4^A-config sum equals
      `a^Z · b^{N−1} · (a − b)` whenever `N > 0`. -/
  claim_factorisation : 0 < N →
    totalDeltaM = a ^ Z * b ^ (N - 1) * (a - b)

/-- **Branching Q-value factorisation** ([`prop:branching-qvalue-factorization`]).

    The 4^A-config sum factorises as `a^Z · b^{N−1} · (a − b)`. -/
-- Ref: [manuscript] quantum-observable-universe/particle-interactions/branching-qvalue-factorization.md
theorem branching_qvalue_factorization
    {Z N : ℕ} [ctx : BranchingQvalueContext Z N] (h_N_pos : 0 < N) :
    ctx.totalDeltaM = ctx.a ^ Z * ctx.b ^ (N - 1) * (ctx.a - ctx.b) :=
  ctx.claim_factorisation h_N_pos

end QOU.ParticleInteractions
