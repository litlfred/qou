/-!
# QOU.LiftingDescent.ccg_cosimplicial_identities — cosimplicial identities

**Lemma** ([`lem:ccg-cosimplicial-identities`](../../../quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.md)).

*The coface maps `δⁱ` (composites of jet prolongation with Čech face
maps) and codegeneracy maps `σⁱ` (composites of descent with Čech
degeneracy maps) satisfy the cosimplicial identities*

```
  δʲ ∘ δⁱ = δⁱ ∘ δ^{j−1}    (i < j)
  σʲ ∘ σⁱ = σⁱ ∘ σ^{j+1}    (i ≤ j)
```

*plus the mixed identities, each case reducing to disjoint-support
commutation or to the retraction `𝔡_{n+1} ∘ ℓ_n = id`.*

The Lean encoding records the four identities as a `Prop`-valued
conjunction against an abstract `CosimplicialContext`.

-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.md
-/

namespace QOU.LiftingDescent

/-- Abstract context for the cosimplicial identities. -/
class CosimplicialContext where
  /-- The cosimplicial object at level `n` (abstract). -/
  Obj : ℕ → Type
  /-- Coface map `δⁱ : Obj n → Obj (n+1)`. -/
  delta : (n i : ℕ) → Obj n → Obj (n + 1)
  /-- Codegeneracy map `σⁱ : Obj (n+1) → Obj n`. -/
  sigma : (n i : ℕ) → Obj (n + 1) → Obj n

/-- **Cosimplicial identities** ([`lem:ccg-cosimplicial-identities`]).

    Two main identities (face-face, degeneracy-degeneracy). -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.md
theorem ccg_cosimplicial_identities
    [ctx : CosimplicialContext] (n i j : ℕ) (x : ctx.Obj n) (y : ctx.Obj (n + 2)) :
    -- Face-face: `δʲ ∘ δⁱ = δⁱ ∘ δ^{j−1}` for `i < j`.
    (i < j →
       ctx.delta (n + 1) j (ctx.delta n i x)
         = ctx.delta (n + 1) i (ctx.delta n (j - 1) x)) ∧
    -- Degeneracy-degeneracy: `σʲ ∘ σⁱ = σⁱ ∘ σ^{j+1}` for `i ≤ j`.
    (i ≤ j →
       ctx.sigma n j (ctx.sigma (n + 1) i y)
         = ctx.sigma n i (ctx.sigma (n + 1) (j + 1) y)) := by
  -- Manuscript proof: standard cosimplicial-identity verification.
  -- Concretisation requires the actual jet-prolongation /
  -- descent / Čech maps.
  -- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.md
  sorry

end QOU.LiftingDescent
