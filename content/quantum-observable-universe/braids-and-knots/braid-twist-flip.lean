import QOU.Basic
import Mathlib.Data.Fin.Basic


/-!
# QOU.BraidTwistFlip

The twist and flip generators σ₁, σ₂ of the **trefoil monodromy group S₃**.

The trefoil-knot group is `B₃ = ⟨σ₁,σ₂ | σ₁σ₂σ₁ = σ₂σ₁σ₂⟩`; the branched-cover
monodromy sends it onto the symmetric group `S₃ ≅ D₃` (the `SU(2)`/`Dic₃` lift
is `def:su2-generators`). The two generators are involutions satisfying the
**braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂`, and their product `σ₁σ₂` is the order-3
3-cycle. They do **not** commute: an earlier version asserted the Klein
four-group `V₄`, which is wrong — `S₃` has no `V₄` subgroup or quotient
(`4 ∤ 6`), and commuting involutions violate the braid relation.

A faithful `S₃` action on the four spectral resolvents must fix one resolvent
and permute the other three by the standard representation (`S₃` has no faithful
action on four points). Here `σ₁ = (w₁ w₂)`, `σ₂ = (w₂ w₃)`, with `w₄` the fixed
resolvent; the index of the fixed resolvent is a labelling convention. Pure
combinatorics — no archimedean structure (§7c).

LaTeX label: `def:braid-twist-flip`

## References

- [manuscript] Chapter 4, §Braid involutions
-/

namespace QOU

/-- The twist generator `σ₁ = (w₁ w₂)`: `0 ↔ 1`, with `2` and `3` fixed. -/
-- Ref: [manuscript] Chapter 4
def twistPerm : Fin 4 → Fin 4
  | ⟨0, _⟩ => ⟨1, by omega⟩
  | ⟨1, _⟩ => ⟨0, by omega⟩
  | ⟨2, _⟩ => ⟨2, by omega⟩
  | ⟨3, _⟩ => ⟨3, by omega⟩

/-- The flip generator `σ₂ = (w₂ w₃)`: `1 ↔ 2`, with `0` and `3` fixed. -/
-- Ref: [manuscript] Chapter 4
def flipPerm : Fin 4 → Fin 4
  | ⟨0, _⟩ => ⟨0, by omega⟩
  | ⟨1, _⟩ => ⟨2, by omega⟩
  | ⟨2, _⟩ => ⟨1, by omega⟩
  | ⟨3, _⟩ => ⟨3, by omega⟩

/-- Twist is an involution: `σ₁² = id`. -/
-- Ref: [manuscript] Chapter 4
theorem twistPerm_involution (i : Fin 4) : twistPerm (twistPerm i) = i := by
  fin_cases i <;> rfl

/-- Flip is an involution: `σ₂² = id`. -/
-- Ref: [manuscript] Chapter 4
theorem flipPerm_involution (i : Fin 4) : flipPerm (flipPerm i) = i := by
  fin_cases i <;> rfl

/-- **Braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂` — the defining relation of `B₃`, and the
    reason `⟨σ₁,σ₂⟩ ≅ S₃` rather than `V₄` (commuting involutions would fail it). -/
-- Ref: [manuscript] Chapter 4
theorem twist_flip_braid (i : Fin 4) :
    twistPerm (flipPerm (twistPerm i)) = flipPerm (twistPerm (flipPerm i)) := by
  fin_cases i <;> rfl

/-- The composite `σ₁σ₂` has order dividing 3: `(σ₁σ₂)³ = id`. -/
-- Ref: [manuscript] Chapter 4
theorem twist_flip_pow_three (i : Fin 4) :
    twistPerm (flipPerm (twistPerm (flipPerm (twistPerm (flipPerm i))))) = i := by
  fin_cases i <;> rfl

/-- `σ₁σ₂ ≠ id`, so its order is exactly 3 (a genuine 3-cycle), not 1. -/
-- Ref: [manuscript] Chapter 4
theorem twist_flip_ne_id : ∃ i : Fin 4, twistPerm (flipPerm i) ≠ i := by
  decide

/-- Both generators fix the fourth resolvent — the structurally forced `S₃`
    fixed point of a faithful action on four resolvents. -/
-- Ref: [manuscript] Chapter 4
theorem w4_fixed :
    twistPerm ⟨3, by omega⟩ = ⟨3, by omega⟩ ∧ flipPerm ⟨3, by omega⟩ = ⟨3, by omega⟩ :=
  ⟨rfl, rfl⟩

end QOU
