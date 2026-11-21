import QOU.Basic
import Mathlib.Data.Fin.Basic


/-!
# QOU.BraidTwistFlip

The twist and flip generators `σ₁, σ₂` of the **trefoil monodromy group
`S₃ ≅ D₃`**, realized on the **three branches of the cubic constraint**
(`def:braid-group-action`, §Spectral S₃).

The trefoil-knot group is `B₃ = ⟨σ₁,σ₂ | σ₁σ₂σ₁ = σ₂σ₁σ₂⟩`; the branched-cover
monodromy sends it onto `S₃`, the Galois group of the cubic, which permutes the
three branches. The two braid generators are the reflections of `D₃`; their
product `σ₁σ₂` is the order-3 rotation `α` (the `SU(2)`/`Dic₃` lift is
`def:su2-generators`), and they satisfy the dihedral relation `σ₁ α σ₁ = α⁻¹`.

The `S₃` acts on the **three branches**, not on the four spectral resolvents:
`S₃` has no faithful action on four points (`4 ∤ 6`). The four resolvents carry
the two conjugate pairs `(w₁,w₄)`, `(w₂,w₃)` and the projective ratio
coordinates `η₁ = w₁/w₂`, `η₂ = w₃/w₄`, on which the reflection swaps the
conjugate pairs and the rotation cycles the three branches
(`def:braid-group-action`). An earlier version placed the action on the four
resolvents with one fixed; the branch action is the canonical one (owner ruling,
bean `qou-htv4`). Pure combinatorics — no archimedean structure (§7c).

LaTeX label: `def:braid-twist-flip`

## References

- [leitner2026] Chapter 4, §Braid involutions
-/

namespace QOU

/-- The twist generator `σ₁` — the reflection `(b₀ b₁)` of the three branches:
    `0 ↔ 1`, with branch `2` fixed. -/
-- Ref: [leitner2026] Chapter 4
def twistPerm : Fin 3 → Fin 3
  | ⟨0, _⟩ => ⟨1, by omega⟩
  | ⟨1, _⟩ => ⟨0, by omega⟩
  | ⟨2, _⟩ => ⟨2, by omega⟩

/-- The flip generator `σ₂` — the reflection `(b₁ b₂)` of the three branches:
    `1 ↔ 2`, with branch `0` fixed. -/
-- Ref: [leitner2026] Chapter 4
def flipPerm : Fin 3 → Fin 3
  | ⟨0, _⟩ => ⟨0, by omega⟩
  | ⟨1, _⟩ => ⟨2, by omega⟩
  | ⟨2, _⟩ => ⟨1, by omega⟩

/-- Twist is an involution: `σ₁² = id`. -/
-- Ref: [leitner2026] Chapter 4
theorem twistPerm_involution (i : Fin 3) : twistPerm (twistPerm i) = i := by
  fin_cases i <;> rfl

/-- Flip is an involution: `σ₂² = id`. -/
-- Ref: [leitner2026] Chapter 4
theorem flipPerm_involution (i : Fin 3) : flipPerm (flipPerm i) = i := by
  fin_cases i <;> rfl

/-- **Braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂` — the defining relation of `B₃`, and the
    reason `⟨σ₁,σ₂⟩ ≅ S₃` rather than `V₄` (commuting involutions would fail it). -/
-- Ref: [leitner2026] Chapter 4
theorem twist_flip_braid (i : Fin 3) :
    twistPerm (flipPerm (twistPerm i)) = flipPerm (twistPerm (flipPerm i)) := by
  fin_cases i <;> rfl

/-- The **rotation** `α = σ₁σ₂` — the order-3 cyclic permutation of the three
    branches (the `SU(2)`/`Dic₃` generator `α` of `def:su2-generators`). -/
-- Ref: [leitner2026] Chapter 4
def rotation (i : Fin 3) : Fin 3 := twistPerm (flipPerm i)

/-- The rotation has order dividing 3: `α³ = id`. -/
-- Ref: [leitner2026] Chapter 4
theorem rotation_pow_three (i : Fin 3) : rotation (rotation (rotation i)) = i := by
  fin_cases i <;> rfl

/-- `α ≠ id`, so the rotation has order exactly 3 — a genuine 3-cycle of the
    three branches, not the identity. -/
-- Ref: [leitner2026] Chapter 4
theorem rotation_ne_id : ∃ i : Fin 3, rotation i ≠ i := by
  decide

/-- **Dihedral relation** `σ₁ α σ₁ = α⁻¹` (`= α²`): a reflection inverts the
    rotation. Together with `α³ = id` and `σ₁² = id` this exhibits `D₃ ≅ S₃`. -/
-- Ref: [leitner2026] Chapter 4
theorem twist_rotation_dihedral (i : Fin 3) :
    twistPerm (rotation (twistPerm i)) = rotation (rotation i) := by
  fin_cases i <;> rfl

end QOU
