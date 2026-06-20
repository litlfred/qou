/-!
# QOU.BraidKnot.wedderburn_trace_identity — `Σ_λ dim_q(λ)² = [n]_q!`

**Proposition** ([`prop:wedderburn-trace-identity`](../../../quantum-observable-universe/braids-and-knots/wedderburn-trace-identity.md)).

*For the Hecke algebra `H_n(R, q)` over `R` with parameter
`q ≠ 0, ±1`, the sum of squared quantum dimensions equals the
quantum factorial:*

```
  Σ_{λ ⊢ n} dim_q(λ)² = [n]_q!
```

*where `[n]_q! = [1]_q · [2]_q · … · [n]_q`.*

The Lean encoding records the identity as a `Finset.sum`-style
claim over the set of partitions of `n`.  Concretising
`dim_q : Partition → R` and `qFactorial : ℕ → R` to explicit
combinatorial constructions is downstream work.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/wedderburn-trace-identity.md
-/

namespace QOU.BraidKnot

/-- Abstract context for the Wedderburn trace identity. -/
class WedderburnTraceContext (n : ℕ) where
  /-- The Hecke parameter `q`. -/
  q : ℝ
  q_ne_zero : q ≠ 0
  q_ne_one : q ≠ 1
  q_ne_neg_one : q ≠ -1
  /-- Indexing type for partitions of `n`. -/
  Partition : Type
  /-- The set of partitions of `n` (as a `Finset` for summation). -/
  partitions : Finset Partition
  /-- The quantum dimension `dim_q(λ) : ℝ`. -/
  qDim : Partition → ℝ
  /-- The quantum factorial `[n]_q! : ℝ`. -/
  qFactorial : ℝ
  /-- Manuscript Wedderburn trace identity:
      `Σ_{λ ⊢ n} dim_q(λ)² = [n]_q!`. -/
  claim_wedderburn_trace :
    (partitions.sum fun lam => qDim lam ^ 2) = qFactorial

/-- **Wedderburn trace identity** ([`prop:wedderburn-trace-identity`]).

    `Σ_{λ ⊢ n} dim_q(λ)² = [n]_q!`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/wedderburn-trace-identity.md
def wedderburn_trace_identity
    {n : ℕ} [ctx : WedderburnTraceContext n] :
    (ctx.partitions.sum fun lam => ctx.qDim lam ^ 2) = ctx.qFactorial :=
  ctx.claim_wedderburn_trace

end QOU.BraidKnot
