import Mathlib.Tactic

/-!
# QOU.BraidKnot.schur_weyl_mass_decomposition — `tr_M(𝒜) = Σ_λ (s_λ/H_q(λ)) · χ^λ(𝒜)`

**Proposition** ([`prop:schur-weyl-mass-decomposition`](../../../quantum-observable-universe/braids-and-knots/schur-weyl-mass-decomposition.md)).

*Let `(Z, N)` be an atom with atomic braid `𝒜 ∈ H_{3A}(q)` on `3A`
strands, and let `V^{⊗ 3A} ≅ ⊕_{λ ⊢ 3A} S^λ ⊗ V_λ` be the
Schur–Weyl decomposition.  The Markov trace of the atomic braid
decomposes over partitions `λ ⊢ 3A`:*

```
  tr_M(𝒜) = Σ_{λ ⊢ 3A} (s_λ(𝐪) / H_q(λ)) · χ^λ(𝒜)
```

*where `s_λ` is the Schur function evaluated on `𝐪 = (q, q⁻¹)`,
`H_q(λ) = ∏_{x ∈ λ} [h_x(λ)]_q` is the `q`-hook product, and
`χ^λ` is the character of irrep `λ` of `H_{3A}(q)`.*

The Lean encoding records the sum identity against an abstract
`SchurWeylContext` carrying the Schur-Weyl data.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/schur-weyl-mass-decomposition.md
-/

namespace QOU.BraidKnot

/-- Abstract Schur–Weyl decomposition context for atomic braid trace.

    **Base ring (§7c).** The Schur–Weyl data — the Hecke parameter `q`,
    the Schur function `s_λ(q, q⁻¹)`, the `q`-hook product `H_q(λ)`, the
    character `χ^λ`, and the Markov trace — are rational functions of `q`
    over the coefficient field, and the decomposition is a field identity
    (`+`, `*`, `/`, with `H_q(λ) ≠ 0`). No `Real.*`, no ordering. The
    context is therefore stated over a generic field `(R : Type*) [Field R]`
    rather than specialised to `ℝ`. -/
class SchurWeylMassContext (R : Type*) [Field R] (Z N : ℕ) where
  /-- Mass number `A = Z + N`. -/
  A : ℕ := Z + N
  /-- The Hecke parameter `q`. -/
  q : R
  /-- Indexing type for partitions of `3A`. -/
  Partition : Type
  /-- Finite set of partitions of `3A`. -/
  partitions : Finset Partition
  /-- Schur function `s_λ(q, q⁻¹) : R`. -/
  schurFunction : Partition → R
  /-- `q`-hook product `H_q(λ) : R`. -/
  qHookProduct : Partition → R
  /-- Character of the atomic braid `𝒜` on irrep `λ`. -/
  chi_atomic : Partition → R
  /-- Markov trace `tr_M(𝒜)`. -/
  trM_atomic : R
  /-- The hook product is non-zero (generic `q`). -/
  qHookProduct_ne_zero : ∀ lam, qHookProduct lam ≠ 0
  /-- Manuscript Schur–Weyl decomposition identity. -/
  claim_schur_weyl_sum :
    trM_atomic = partitions.sum
      fun lam => schurFunction lam * chi_atomic lam / qHookProduct lam

/-- **Schur–Weyl decomposition of the atomic Markov trace**
    ([`prop:schur-weyl-mass-decomposition`]).

    `tr_M(𝒜) = Σ_λ s_λ(𝐪) · χ^λ(𝒜) / H_q(λ)`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/schur-weyl-mass-decomposition.md
def schur_weyl_mass_decomposition
    {R : Type*} [Field R] {Z N : ℕ} [ctx : SchurWeylMassContext R Z N] :
    ctx.trM_atomic
      = ctx.partitions.sum
          fun lam => ctx.schurFunction lam * ctx.chi_atomic lam / ctx.qHookProduct lam :=
  ctx.claim_schur_weyl_sum

end QOU.BraidKnot
