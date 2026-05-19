/-!
# QOU.frobenius_dagger_positive_definite — `f† ∘ f > 0` for all `f ≠ 0`

**Proposition** ([`prop:positive-definite-dagger`](../../../quantum-observable-universe/quantum-universes/positive-definite-dagger.md)).

*Let `(𝐂, A, τ)` be a quantum universe with Frobenius pairing
`⟨a, b⟩ = ∫_A(μ(a ⊗ b))` and antipode `S`.  Define the* Frobenius
dagger *on morphisms by*

```
  f† = ∫_A ∘ μ(S(f) ⊗ −).
```

*Then `†` is a positive-definite involutive structure on `𝐂`:  for
every non-zero morphism `f : 𝟙 → X`, the composite `f† ∘ f` is a
positive element of `End(𝟙) ≅ R`.*

The Lean encoding records the positivity claim against an abstract
`FrobeniusDaggerContext` carrying the dagger operation and the
positivity predicate on the endomorphism ring `R`.

-- Ref: [manuscript] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
-/

namespace QOU

/-- Abstract context for the Frobenius-dagger positivity claim. -/
class FrobeniusDaggerContext where
  /-- The categorical object `X` (target of the morphism). -/
  X : Type
  /-- The endomorphism ring `End(𝟙) ≅ R`. -/
  R : Type
  /-- A morphism `f : 𝟙 → X` (encoded as a function-like type). -/
  Mor1X : Type
  /-- The Frobenius dagger `f†` applied to a morphism. -/
  dagger : Mor1X → (X → Mor1X)  -- abstract `† : (𝟙 → X) → (X → 𝟙)`
  /-- Composition `f† ∘ f : 𝟙 → 𝟙 ≅ R`. -/
  composeDaggerOriginal : Mor1X → R
  /-- The "is-non-zero" predicate on `Mor1X`. -/
  isNonzero : Mor1X → Prop
  /-- The "is-positive" predicate on `R`. -/
  isPositive : R → Prop

/-- **Frobenius dagger is positive definite** ([`prop:positive-definite-dagger`]).

    For every non-zero morphism `f : 𝟙 → X`, the composite
    `f† ∘ f` is a positive element of `End(𝟙)`. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
theorem frobenius_dagger_positive_definite
    [ctx : FrobeniusDaggerContext]
    (f : ctx.Mor1X) (h : ctx.isNonzero f) :
    ctx.isPositive (ctx.composeDaggerOriginal f) := by
  -- Manuscript derivation: positivity follows from the integral
  -- representation `f† ∘ f = ∫_A(S(f) ⊗ f)` plus the positive-
  -- definiteness of the Frobenius pairing on the underlying GNS
  -- representation. Concretisation requires the actual Frobenius
  -- algebra + GNS Hilbert-space structure.
  -- Ref: [manuscript] quantum-observable-universe/quantum-universes/positive-definite-dagger.md
  sorry

end QOU
