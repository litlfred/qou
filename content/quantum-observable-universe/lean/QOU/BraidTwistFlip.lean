import Mathlib.Tactic

/-!
# QOU.BraidTwistFlip

**Canonical declaration** for content block at
[`quantum-observable-universe/braids-and-knots/braid-twist-flip.ts`](quantum-observable-universe/braids-and-knots/braid-twist-flip.ts).

Formalises the manuscript **definition** of the twist and flip generators
`σ₁, σ₂` of the trefoil monodromy group `S₃ ≅ D₃`, acting on the **three
branches** `𝐛 = (b₀, b₁, b₂)` of the cubic constraint (its Galois group). The
two generators are the reflections of `D₃`; their product `σ₁σ₂` is the order-3
rotation `α`, and they satisfy the dihedral relation `σ₁ α σ₁ = α⁻¹`, exhibiting
`D₃ ≅ S₃`.

The `S₃` acts on the three branches, not on the four spectral resolvents:
`S₃` has no faithful action on four points. The four resolvents carry the
conjugate pairs `(w₁,w₄)`, `(w₂,w₃)` and the ratios `η₁ = w₁/w₂`, `η₂ = w₃/w₄`,
on which the reflection swaps the pairs and the rotation cycles the branches
(`def:braid-group-action`; owner ruling, bean `qou-htv4` — the earlier
four-resolvent-with-one-fixed model is superseded). Pure combinatorics — generic
over any branch-coordinate type `α` (§7c: no archimedean structure needed).
-/

namespace QOU

/-- The three branches `𝐛 = (b₀, b₁, b₂)` of the cubic constraint — the carrier
    on which the trefoil monodromy `S₃` acts. -/
abbrev BraidTwistFlip (α : Type*) := α × α × α

namespace BraidTwistFlip

variable {α : Type*}

/-- The **twist** generator `σ₁` — the reflection `(b₀ b₁)`. -/
def twist (b : BraidTwistFlip α) : BraidTwistFlip α :=
  (b.2.1, b.1, b.2.2)

/-- The **flip** generator `σ₂` — the reflection `(b₁ b₂)`. -/
def flip (b : BraidTwistFlip α) : BraidTwistFlip α :=
  (b.1, b.2.2, b.2.1)

/-- Twist is an involution: `σ₁² = id`. -/
@[simp] theorem twist_involutive (b : BraidTwistFlip α) : twist (twist b) = b := rfl

/-- Flip is an involution: `σ₂² = id`. -/
@[simp] theorem flip_involutive (b : BraidTwistFlip α) : flip (flip b) = b := rfl

/-- **Braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂` — the defining relation of `B₃`,
    exhibiting `⟨σ₁,σ₂⟩ ≅ S₃`. -/
theorem twist_flip_braid (b : BraidTwistFlip α) :
    twist (flip (twist b)) = flip (twist (flip b)) := rfl

/-- The **rotation** `α = σ₁σ₂ : 𝐛 ↦ (b₂, b₀, b₁)` — the order-3 cyclic
    permutation of the three branches. -/
def rotation (b : BraidTwistFlip α) : BraidTwistFlip α := twist (flip b)

theorem rotation_apply (b : BraidTwistFlip α) : rotation b = (b.2.2, b.1, b.2.1) := rfl

/-- The rotation has order dividing 3: `α³ = id`. -/
@[simp] theorem rotation_pow_three (b : BraidTwistFlip α) :
    rotation (rotation (rotation b)) = b := rfl

/-- **Dihedral relation** `σ₁ α σ₁ = α⁻¹` (`= α²`): a reflection inverts the
    rotation, exhibiting `D₃ ≅ S₃`. -/
theorem twist_rotation_dihedral (b : BraidTwistFlip α) :
    twist (rotation (twist b)) = rotation (rotation b) := rfl

end BraidTwistFlip

end QOU
