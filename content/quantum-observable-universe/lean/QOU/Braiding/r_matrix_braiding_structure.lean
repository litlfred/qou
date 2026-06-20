/-!
# QOU.Braiding.r_matrix_braiding_structure — Yang-Baxter for the universal `R`-matrix

**Proposition** ([`prop:r-matrix-braiding-structure`](../../../quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.md)).

*The universal `R`-matrix
`R ∈ U_q(𝔰𝔲(2)) ⊗̂ U_q(𝔰𝔲(2))` satisfies the Yang–Baxter equation*

```
  R₁₂ · R₁₃ · R₂₃ = R₂₃ · R₁₃ · R₁₂
```

*and the braid operator `R̆ = P ∘ R` (with `P` the tensor swap)
gives a representation of the braid group on any tensor product of
finite-dimensional `U_q(𝔰𝔲(2))`-modules.*

The Lean encoding records the YBE as an equation on an abstract
`RMatrixBraidingContext` carrying the three-fold tensor product
maps `R₁₂, R₁₃, R₂₃`.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.md
-/

namespace QOU.Braiding

/-- Abstract context for the universal `R`-matrix and its Yang–Baxter
    equation. -/
class RMatrixBraidingContext where
  /-- The three-fold tensor product space `V ⊗ V ⊗ V`. -/
  V3 : Type
  /-- Multiplication on `V3` (composition of operators). -/
  comp : V3 → V3 → V3
  /-- The three `R`-matrix actions on the three pairs of strands. -/
  R12 : V3
  R13 : V3
  R23 : V3
  /-- Universal Yang–Baxter equation:
      `R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`. -/
  claim_yang_baxter :
    comp (comp R12 R13) R23 = comp (comp R23 R13) R12

/-- **Yang–Baxter equation for the universal `R`-matrix**
    ([`prop:r-matrix-braiding-structure`]).

    `R₁₂ ∘ R₁₃ ∘ R₂₃ = R₂₃ ∘ R₁₃ ∘ R₁₂`. -/
-- Ref: [drinfeld1985] V. Drinfeld, Hopf algebras and the quantum Yang-Baxter equation, 1985
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/r-matrix-braiding-structure.md
def r_matrix_braiding_structure
    [ctx : RMatrixBraidingContext] :
    ctx.comp (ctx.comp ctx.R12 ctx.R13) ctx.R23
      = ctx.comp (ctx.comp ctx.R23 ctx.R13) ctx.R12 :=
  ctx.claim_yang_baxter

end QOU.Braiding
