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

/-- Abstract Schur–Weyl decomposition context for atomic braid trace. -/
class SchurWeylMassContext (Z N : ℕ) where
  /-- Mass number `A = Z + N`. -/
  A : ℕ := Z + N
  /-- The Hecke parameter `q`. -/
  q : ℝ
  /-- Indexing type for partitions of `3A`. -/
  Partition : Type
  /-- Finite set of partitions of `3A`. -/
  partitions : Finset Partition
  /-- Schur function `s_λ(q, q⁻¹) : ℝ`. -/
  schurFunction : Partition → ℝ
  /-- `q`-hook product `H_q(λ) : ℝ`. -/
  qHookProduct : Partition → ℝ
  /-- Character of the atomic braid `𝒜` on irrep `λ`. -/
  chi_atomic : Partition → ℝ
  /-- Markov trace `tr_M(𝒜)`. -/
  trM_atomic : ℝ
  /-- The hook product is non-zero (generic `q`). -/
  qHookProduct_ne_zero : ∀ λ, qHookProduct λ ≠ 0
  /-- Manuscript Schur–Weyl decomposition identity. -/
  claim_schur_weyl_sum :
    trM_atomic = partitions.sum
      fun λ => schurFunction λ * chi_atomic λ / qHookProduct λ

/-- **Schur–Weyl decomposition of the atomic Markov trace**
    ([`prop:schur-weyl-mass-decomposition`]).

    `tr_M(𝒜) = Σ_λ s_λ(𝐪) · χ^λ(𝒜) / H_q(λ)`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/schur-weyl-mass-decomposition.md
def schur_weyl_mass_decomposition
    {Z N : ℕ} [ctx : SchurWeylMassContext Z N] :
    ctx.trM_atomic
      = ctx.partitions.sum
          fun λ => ctx.schurFunction λ * ctx.chi_atomic λ / ctx.qHookProduct λ :=
  ctx.claim_schur_weyl_sum

end QOU.BraidKnot
