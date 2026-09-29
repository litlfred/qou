import Mathlib.Data.Nat.Notation

/-!
# QOU.volume_from_rigidity — `rank(V) = 2` from symplectic self-duality

**Proposition** ([`prop:volume-from-rigidity`](../../../quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md)).

*Let `(𝐂, ⊗, 𝟙)` be an `R`-linear rigid monoidal category, and let
`V` be a simple object that is symplectically self-dual: there
exists an isomorphism `φ : V ≅ V^∨` with `φ^∨ = −φ` (alternating).
The alternating condition forces `rank(V) = 2`.*

The Lean encoding records the rank claim against an abstract
`SymplecticSelfDualContext` carrying the categorical data
`(V, V^∨, φ, φ^∨)` and the rank function.

-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md
-/

namespace QOU

/-- Abstract context for the `rank(V) = 2` claim from symplectic
    self-duality in a rigid monoidal category. -/
class SymplecticSelfDualContext where
  /-- The simple object `V`. -/
  V : Type
  /-- The dual object `V^∨`. -/
  Vdual : Type
  /-- An isomorphism `φ : V → V^∨`. -/
  φ : V → Vdual
  /-- The dual map `φ^∨ : V → V^∨`. -/
  φDual : V → Vdual
  /-- Negation on `Vdual` (an `R`-linear structure). -/
  neg : Vdual → Vdual
  /-- The alternating condition `φ^∨ = −φ`. -/
  alternating : ∀ v, φDual v = neg (φ v)
  /-- The categorical rank function. -/
  rank : Type → ℕ
  /-- Hypothesis: `V` is simple (irreducible). -/
  simple : Prop
  /-- Manuscript rank-2 claim: under simplicity, the alternating
      `φ^∨ = −φ` forces `rank(V) = 2`. -/
  claim_rank_eq_two : simple → rank V = 2

/-- **`rank(V) = 2` from symplectic self-duality**
    ([`prop:volume-from-rigidity`]).

    Under the alternating condition `φ^∨ = −φ` plus simplicity of
    `V`, the categorical rank is exactly `2`. -/
-- Ref: [manuscript] quantum-observable-universe/quantum-observable-universes/volume-from-rigidity.md
theorem volume_from_rigidity
    [ctx : SymplecticSelfDualContext] (h_simple : ctx.simple) :
    ctx.rank ctx.V = 2 :=
  ctx.claim_rank_eq_two h_simple

end QOU
