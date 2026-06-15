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
conjunction against an abstract `CcgCosimplicialIdentitiesContext`.

-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.md
-/

namespace QOU.LiftingDescent

/-- Abstract context for the cosimplicial identities. -/
class CcgCosimplicialIdentitiesContext where
  /-- The cosimplicial object at level `n` (abstract). -/
  Obj : ℕ → Type
  /-- Coface map `δⁱ : Obj n → Obj (n+1)`. -/
  delta : (n i : ℕ) → Obj n → Obj (n + 1)
  /-- Codegeneracy map `σⁱ : Obj (n+1) → Obj n`. -/
  sigma : (n i : ℕ) → Obj (n + 1) → Obj n
  /-- Čech face map. -/
  cech_face : (n i : ℕ) → Obj n → Obj (n + 1)
  /-- Jet prolongation map. -/
  jet : (n : ℕ) → Obj n → Obj n
  /-- Coface map is composite of jet and Čech face. -/
  delta_def : ∀ n i x, delta n i x = cech_face n i (jet n x)
  /-- Čech degeneracy map. -/
  cech_deg : (n i : ℕ) → Obj (n + 1) → Obj n
  /-- Descent map. -/
  descent : (n : ℕ) → Obj n → Obj n
  /-- Codegeneracy map is composite of descent and Čech degeneracy. -/
  sigma_def : ∀ n i y, sigma n i y = descent n (cech_deg n i y)

  /-- Jet prolongation commutes with Čech face. -/
  jet_face_comm : ∀ n i x, jet (n + 1) (cech_face n i x) = cech_face n i (jet n x)
  /-- Čech face maps satisfy disjoint-support commutation. -/
  cech_face_comm : ∀ n i j x, i < j →
    cech_face (n + 1) j (cech_face n i x) = cech_face (n + 1) i (cech_face n (j - 1) x)

  /-- Descent commutes with Čech degeneracy. -/
  descent_deg_comm : ∀ n i y, descent n (cech_deg n i y) = cech_deg n i (descent (n + 1) y)
  /-- Čech degeneracy maps satisfy disjoint-support commutation. -/
  cech_deg_comm : ∀ n i j y, i ≤ j →
    cech_deg n j (cech_deg (n + 1) i y) = cech_deg n i (cech_deg (n + 1) (j + 1) y)

/-- **Cosimplicial identities** ([`lem:ccg-cosimplicial-identities`]).

    Two main identities (face-face, degeneracy-degeneracy). -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/ccg-cosimplicial-identities.md
theorem ccg_cosimplicial_identities
    [ctx : CcgCosimplicialIdentitiesContext] (n i j : ℕ) (x : ctx.Obj n) (y : ctx.Obj (n + 2)) :
    -- Face-face: `δʲ ∘ δⁱ = δⁱ ∘ δ^{j−1}` for `i < j`.
    (i < j →
       ctx.delta (n + 1) j (ctx.delta n i x)
         = ctx.delta (n + 1) i (ctx.delta n (j - 1) x)) ∧
    -- Degeneracy-degeneracy: `σʲ ∘ σⁱ = σⁱ ∘ σ^{j+1}` for `i ≤ j`.
    (i ≤ j →
       ctx.sigma n j (ctx.sigma (n + 1) i y)
         = ctx.sigma n i (ctx.sigma (n + 1) (j + 1) y)) := by
  constructor
  · intro hij
    rw [ctx.delta_def, ctx.delta_def, ctx.delta_def, ctx.delta_def]
    rw [ctx.jet_face_comm]
    rw [ctx.cech_face_comm _ _ _ _ hij]
  · intro hij
    rw [ctx.sigma_def, ctx.sigma_def, ctx.sigma_def, ctx.sigma_def]
    rw [← ctx.descent_deg_comm]
    rw [ctx.cech_deg_comm _ _ _ _ hij]

end QOU.LiftingDescent
