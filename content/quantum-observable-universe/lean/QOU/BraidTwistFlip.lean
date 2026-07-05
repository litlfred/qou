import Mathlib.Tactic

/-!
# QOU.BraidTwistFlip

**Canonical declaration** for content block at
[`quantum-observable-universe/braids-and-knots/braid-twist-flip.ts`](quantum-observable-universe/braids-and-knots/braid-twist-flip.ts).

Formalises the manuscript **definition** of the twist and flip involutions
on a spectral-resolvent 4-tuple `𝐰 = (w₁,w₂,w₃,w₄)`, and the fact that they
generate the Klein four-group `V₄`. Pure combinatorics — generic over any
entry type `α` (§7c: no archimedean structure needed).
-/

namespace QOU

/-- A spectral-resolvent 4-tuple `𝐰 = (w₁, w₂, w₃, w₄)` — the carrier on
    which the twist and flip involutions act. -/
abbrev BraidTwistFlip (α : Type*) := α × α × α × α

namespace BraidTwistFlip

variable {α : Type*}

/-- The **twist** involution `σ₁ : (w₁,w₂,w₃,w₄) ↦ (w₂,w₁,w₄,w₃)`. -/
def twist (w : BraidTwistFlip α) : BraidTwistFlip α :=
  (w.2.1, w.1, w.2.2.2, w.2.2.1)

/-- The **flip** involution `σ₂ : (w₁,w₂,w₃,w₄) ↦ (w₄,w₃,w₂,w₁)`. -/
def flip (w : BraidTwistFlip α) : BraidTwistFlip α :=
  (w.2.2.2, w.2.2.1, w.2.1, w.1)

/-- Twist is an involution: `σ₁² = id`. -/
@[simp] theorem twist_involutive (w : BraidTwistFlip α) : twist (twist w) = w := rfl

/-- Flip is an involution: `σ₂² = id`. -/
@[simp] theorem flip_involutive (w : BraidTwistFlip α) : flip (flip w) = w := rfl

/-- Twist and flip commute — the group they generate is abelian (`V₄`). -/
theorem twist_flip_comm (w : BraidTwistFlip α) :
    twist (flip w) = flip (twist w) := rfl

/-- The composite `σ₁σ₂ : 𝐰 ↦ (w₃,w₄,w₁,w₂)` (manuscript). -/
theorem twist_flip_apply (w : BraidTwistFlip α) :
    twist (flip w) = (w.2.2.1, w.2.2.2, w.1, w.2.1) := rfl

/-- The composite is itself an involution, so `{id, σ₁, σ₂, σ₁σ₂}` is closed:
    `(σ₁σ₂)² = id`. Together with the two involution laws and commutativity
    this exhibits the Klein four-group. -/
@[simp] theorem twist_flip_involutive (w : BraidTwistFlip α) :
    twist (flip (twist (flip w))) = w := rfl

end BraidTwistFlip

end QOU
