import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Group.Basic


/-!
# QOU.YekutieliLiftingCondition — Lifting condition for gerbe extensions

A rigid monoidal category 𝒞 satisfies the Yekutieli lifting condition
if every gerbe object can be lifted, with obstruction classified by
a single cohomology class κ ∈ H²(𝒮, ℬ).

The obstruction space is an abelian group (typically a cohomology group),
and vanishing of the obstruction is necessary and sufficient for the lift.

## References

- [yekutieli2010] Central Extensions of Gerbes, §3
- [leitner2026] §3
-/

namespace QOU

/-- The Yekutieli lifting condition for a category with gerbe structure.

    Given a central extension of gerbes
      1 → ℬ → 𝔊' → 𝔊 → 1
    banded by an abelian sheaf ℬ on a site 𝒮, each object x ∈ Ob(𝔊)
    has an obstruction class κ(x) ∈ H²(𝒮, ℬ), and x admits a lift
    to 𝔊' if and only if κ(x) = 0.

    LaTeX: `\label{def:yekutieli-lifting-condition}` -/
-- Ref: [yekutieli2010] §3, [leitner2026] §3
structure YekutieliLiftingCondition where
  /-- The obstruction space (representing H²(𝒮, ℬ)). -/
  ObstructionSpace : Type*
  /-- The obstruction space is an additive commutative group. -/
  [addCommGroup : AddCommGroup ObstructionSpace]
  /-- The obstruction map: each object (indexed by ℕ for the tower)
      gets an obstruction class in H²(𝒮, ℬ). -/
  obstruction : ℕ → ObstructionSpace
  /-- The type of lifts at level n. -/
  LiftType : ℕ → Type*
  /-- The lifting exists when the obstruction vanishes. -/
  lift_of_zero : ∀ n, obstruction n = 0 → Nonempty (LiftType n)
  /-- Non-zero obstruction prevents lifting. -/
  no_lift_of_nonzero : ∀ n, obstruction n ≠ 0 → IsEmpty (LiftType n)

attribute [instance] YekutieliLiftingCondition.addCommGroup

/-- An object lifts iff its obstruction is zero (the iff formulation).
    Combines lift_of_zero and no_lift_of_nonzero. -/
theorem YekutieliLiftingCondition.lift_iff
    (ylc : YekutieliLiftingCondition)
    (n : ℕ) :
    (ylc.obstruction n = 0) ↔ Nonempty (ylc.LiftType n) := by
  constructor
  · exact ylc.lift_of_zero n
  · intro ⟨_⟩
    by_contra h
    exact (ylc.no_lift_of_nonzero n h).elim ‹_›

end QOU
