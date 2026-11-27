import Mathlib.Data.Real.Basic

/-!
# QOU.Braiding.non_self_intersection — categorical Möbius energy diverges at self-intersection

**Proposition** ([`prop:non-self-intersection`](../../../quantum-observable-universe/braids-and-knots/non-self-intersection.md)).

*Let `ϱ` be a knot embedding with categorical Möbius energy
`E_cat(ϱ)`, and let `q ≠ 1` be the substrate parameter.  The
non-cocommutativity of the Hopf structure at `q ≠ 1` provides a
categorical obstruction to self-intersection: the energy
`𝔪(ϱ)` diverges whenever two non-adjacent strands of `ϱ` approach
within the fibre `τ(A)`.*

The Lean encoding records the divergence claim as a `∀ M, ∃ ε,
distance < ε → energy > M` statement against an abstract
`NonSelfIntersectionContext`.

-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/non-self-intersection.md
-/

namespace QOU.Braiding

/-- Abstract context for the non-self-intersection divergence claim. -/
class NonSelfIntersectionContext where
  /-- The substrate parameter `q`, with `q ≠ 1`. -/
  q : ℝ
  q_ne_one : q ≠ 1
  /-- The categorical Möbius energy of a knot embedding `ϱ`. -/
  E_cat : ℝ → ℝ                     -- ϱ-parameter → ℝ
  /-- A "minimum strand separation" function for the embedding. -/
  strandSeparation : ℝ → ℝ          -- ϱ-parameter → minimum non-adjacent distance
  /-- Manuscript divergence claim: the categorical Möbius energy
      diverges as the strand separation shrinks. -/
  claim_energy_diverges : ∀ (M : ℝ),
    ∃ ε > 0, ∀ ϱ, strandSeparation ϱ < ε → M < E_cat ϱ

/-- **Energy diverges at self-intersection** ([`prop:non-self-intersection`]).

    For every threshold `M`, there exists a separation tolerance `ε`
    such that any knot whose strand separation is below `ε` has
    Möbius energy above `M`. -/
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/non-self-intersection.md
theorem non_self_intersection
    [ctx : NonSelfIntersectionContext] (M : ℝ) :
    ∃ ε > 0, ∀ ϱ, ctx.strandSeparation ϱ < ε → M < ctx.E_cat ϱ :=
  ctx.claim_energy_diverges M

end QOU.Braiding
