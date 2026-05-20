/-!
# QOU.frobenius_relation — Frobenius coassociativity relation

**Proposition** ([`prop:frobenius-relation`](../../../quantum-observable-universe/quantum-universes/frobenius-relation.md)).

*Let `(𝐂, A, τ)` be a quantum universe, with comultiplication
`Δ_μ : A → A ⊗ A` dual to the multiplication `μ : A ⊗ A → A`
under the Frobenius pairing.  Then the **Frobenius relation**
holds: the diagram*

```
    A ⊗ A  --[id ⊗ Δ_μ]-->  A ⊗ A ⊗ A
       |                       |
     [μ]                  [μ ⊗ id]
       v                       v
       A   --[Δ_μ]------->  A ⊗ A
```

*commutes, equivalently:*

```
  (μ ⊗ id) ∘ (id ⊗ Δ_μ) = Δ_μ ∘ μ.
```

The Lean encoding records the equality of the two compositions as
an equation between morphisms `A ⊗ A → A ⊗ A`.  The abstract
context carries `A`, `⊗`, `μ`, `Δ_μ`, and the composition; the
relation is a single equation between `A ⊗ A → A ⊗ A` maps.

-- Ref: [manuscript] quantum-observable-universe/quantum-universes/frobenius-relation.md
-/

namespace QOU

/-- Abstract context for the Frobenius relation. -/
class FrobeniusRelationContext where
  /-- The Frobenius-algebra object `A`. -/
  A : Type
  /-- The tensor product `A ⊗ A`. -/
  TensorAA : Type
  /-- The tensor product `A ⊗ A ⊗ A`. -/
  TensorAAA : Type
  /-- The multiplication `μ : A ⊗ A → A`. -/
  μ : TensorAA → A
  /-- The comultiplication `Δ_μ : A → A ⊗ A`. -/
  Δ_μ : A → TensorAA
  /-- The lifted multiplication `μ ⊗ id : A ⊗ A ⊗ A → A ⊗ A`. -/
  μ_tensor_id : TensorAAA → TensorAA
  /-- The lifted comultiplication `id ⊗ Δ_μ : A ⊗ A → A ⊗ A ⊗ A`. -/
  id_tensor_Δμ : TensorAA → TensorAAA

/-- **Frobenius relation** ([`prop:frobenius-relation`]).

    `(μ ⊗ id) ∘ (id ⊗ Δ_μ) = Δ_μ ∘ μ` as morphisms `A ⊗ A → A ⊗ A`. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-universes/frobenius-relation.md
theorem frobenius_relation [ctx : FrobeniusRelationContext] (x : ctx.TensorAA) :
    ctx.μ_tensor_id (ctx.id_tensor_Δμ x) = ctx.Δ_μ (ctx.μ x) := by
  -- Manuscript derivation: standard Frobenius coassociativity
  -- diagram chase, equivalent to the "snake identity" for Frobenius
  -- algebras (Kock, *Frobenius algebras and 2D topological quantum
  -- field theories*, 2004). Concretisation requires a real
  -- Mathlib `FrobeniusAlgebra` structure.
  -- Ref: [manuscript] quantum-observable-universe/quantum-universes/frobenius-relation.md
  -- Ref: [kock2004] Frobenius algebras and 2D TQFTs.
  sorry

end QOU
