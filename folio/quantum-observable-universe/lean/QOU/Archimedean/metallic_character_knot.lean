import Mathlib.Tactic

/-!
# QOU.Archimedean.metallic_character_knot — metallic atom iff 3 incompleteness conditions

**Proposition** ([`prop:metallic-character-knot`](../../../quantum-observable-universe/archimedean-universe/metallic-character-knot.md)).

*An atom `𝓐(p, n)` with electron cloud `𝓔 = p · T_{2,3}` partitioned
as `S₁ ⊔ … ⊔ S_k ⊔ R` (with `R` the residual sub-link) exhibits
metallic character iff:*

*(1) **Incompleteness**: `|R| < 2 · n_{k+1}²`.*

*(2) **Low crossing energy**: `𝐄_cross(R) ≪ 𝐄_cross(S_k)`.*

*(3) **Site availability**: `R` has at least one open linking site.*

-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/metallic-character-knot.md
-/

namespace QOU.Archimedean

/-- Abstract context for the metallic-atom characterisation. -/
class MetallicCharacterContext where
  /-- The atomic structure type. -/
  Atom : Type
  /-- The "is a metal" predicate. -/
  IsMetallic : Atom → Prop
  /-- The "outer-shell incompleteness" predicate (cond 1). -/
  OuterShellIncomplete : Atom → Prop
  /-- The "low crossing energy at outer shell" predicate (cond 2). -/
  LowOuterCrossingEnergy : Atom → Prop
  /-- The "has an open linking site" predicate (cond 3). -/
  HasOpenSite : Atom → Prop
  /-- Manuscript characterisation: an atom is metallic iff all three
      incompleteness conditions hold simultaneously. -/
  claim_metallic_iff : ∀ a : Atom,
    IsMetallic a ↔
      (OuterShellIncomplete a ∧ LowOuterCrossingEnergy a ∧ HasOpenSite a)

/-- **Metallic character iff 3 conditions** ([`prop:metallic-character-knot`]). -/
-- Ref: [leitner2026] quantum-observable-universe/archimedean-universe/metallic-character-knot.md
theorem metallic_character_knot
    [ctx : MetallicCharacterContext] (a : ctx.Atom) :
    ctx.IsMetallic a ↔
      (ctx.OuterShellIncomplete a ∧
       ctx.LowOuterCrossingEnergy a ∧
       ctx.HasOpenSite a) :=
  ctx.claim_metallic_iff a

end QOU.Archimedean
