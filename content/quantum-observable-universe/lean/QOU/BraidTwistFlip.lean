import Mathlib.Tactic

/-!
# QOU.BraidTwistFlip

**Canonical declaration** for content block at
[`quantum-observable-universe/braids-and-knots/braid-twist-flip.ts`](quantum-observable-universe/braids-and-knots/braid-twist-flip.ts).

Formalises the manuscript **definition** of the twist and flip generators
`σ₁, σ₂` on a spectral-resolvent 4-tuple `𝐰 = (w₁,w₂,w₃,w₄)`, and the fact that
they generate the **symmetric group `S₃ ≅ D₃`** — the trefoil monodromy group.
They are involutions satisfying the **braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂`, with
product `σ₁σ₂` the order-3 3-cycle. (An earlier version asserted the Klein
four-group `V₄`; that is wrong — `S₃` has no `V₄` subgroup or quotient, and
commuting involutions violate the braid relation.) The generators act as the
standard representation on `(w₁,w₂,w₃)` and fix `w₄`, the structurally forced
`S₃` fixed point of a faithful action on four resolvents. Pure combinatorics —
generic over any entry type `α` (§7c: no archimedean structure needed).
-/

namespace QOU

/-- A spectral-resolvent 4-tuple `𝐰 = (w₁, w₂, w₃, w₄)` — the carrier on
    which the twist and flip generators act. -/
abbrev BraidTwistFlip (α : Type*) := α × α × α × α

namespace BraidTwistFlip

variable {α : Type*}

/-- The **twist** generator `σ₁ = (w₁ w₂) : (w₁,w₂,w₃,w₄) ↦ (w₂,w₁,w₃,w₄)`. -/
def twist (w : BraidTwistFlip α) : BraidTwistFlip α :=
  (w.2.1, w.1, w.2.2.1, w.2.2.2)

/-- The **flip** generator `σ₂ = (w₂ w₃) : (w₁,w₂,w₃,w₄) ↦ (w₁,w₃,w₂,w₄)`. -/
def flip (w : BraidTwistFlip α) : BraidTwistFlip α :=
  (w.1, w.2.2.1, w.2.1, w.2.2.2)

/-- Twist is an involution: `σ₁² = id`. -/
@[simp] theorem twist_involutive (w : BraidTwistFlip α) : twist (twist w) = w := rfl

/-- Flip is an involution: `σ₂² = id`. -/
@[simp] theorem flip_involutive (w : BraidTwistFlip α) : flip (flip w) = w := rfl

/-- **Braid relation** `σ₁σ₂σ₁ = σ₂σ₁σ₂` — the defining relation of `B₃`, exhibiting
    `⟨σ₁,σ₂⟩ ≅ S₃`. -/
theorem twist_flip_braid (w : BraidTwistFlip α) :
    twist (flip (twist w)) = flip (twist (flip w)) := rfl

/-- The composite `σ₁σ₂ : 𝐰 ↦ (w₃,w₁,w₂,w₄)` is the order-3 3-cycle on the first
    three resolvents (manuscript). -/
theorem twist_flip_apply (w : BraidTwistFlip α) :
    twist (flip w) = (w.2.2.1, w.1, w.2.1, w.2.2.2) := rfl

/-- The composite has order dividing 3: `(σ₁σ₂)³ = id`. -/
@[simp] theorem twist_flip_pow_three (w : BraidTwistFlip α) :
    twist (flip (twist (flip (twist (flip w))))) = w := rfl

/-- The fourth resolvent is fixed by both generators. -/
@[simp] theorem twist_fixes_fourth (w : BraidTwistFlip α) : (twist w).2.2.2 = w.2.2.2 := rfl

end BraidTwistFlip

end QOU
