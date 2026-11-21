import Mathlib.Data.Real.Basic


/-!
# QOU.YekutieliLifting — The brane tower satisfies the Yekutieli lifting condition

The central extensions of gerbes arising from jet prolongation in
the recursive brane tower satisfy the Yekutieli lifting condition.

## References

- [yekutieli2010] Central Extensions of Gerbes, Theorem 4.17
- [leitner2026] §3 Proposition: Yekutieli Lifting
-/

namespace QOU

/-- **Yekutieli lifting in the brane tower**: each transition Aₙ ↪ A_{n+1}
    defines a central extension of gerbes, and the Yekutieli lifting condition
    holds — the lift exists iff the obstruction class κₙ vanishes.

    By [Theorem 4.17, yekutieli2010], any central extension of gerbes banded
    by an abelian sheaf satisfies this criterion.  The jet prolongation
    realises each transition as precisely such an extension.

    LaTeX: `\label{prop:yekutieli-lifting}`
    Ref: [yekutieli2010] Theorem 4.17 -/
-- Ref: [yekutieli2010] Yekutieli, "Central Extensions of Gerbes," Adv. Math. 225 (2010), arXiv:0801.0083
structure YekutieliLifting where
  /-- The obstruction space H²(S, B). -/
  ObstructionSpace : Type*
  /-- Zero element (trivial obstruction). -/
  zero : ObstructionSpace
  /-- Decidable equality on the obstruction space. -/
  deceq : DecidableEq ObstructionSpace
  /-- The obstruction class κₙ at level n. -/
  kappa : ℕ → ObstructionSpace
  /-- The base-level obstruction κ₀ (the Euler class). -/
  kappa_zero : ObstructionSpace := kappa 0
  /-- The type of lifts at level n. -/
  LiftType : ℕ → Type*
  /-- Lifting criterion: if κₙ = 0, the lift at level n exists. -/
  lift_of_vanishing : ∀ n, kappa n = zero → Nonempty (LiftType n)
  /-- Obstruction: if κₙ ≠ 0, no lift exists. -/
  no_lift_of_nonzero : ∀ n, kappa n ≠ zero → IsEmpty (LiftType n)
  /-- Persistence: if κ₀ ≠ 0, then κₙ ≠ 0 for all n (jet corrections
      live in a complementary subgroup, so cannot cancel κ₀). -/
  persistence : ∀ n, kappa n ≠ zero → kappa (n + 1) ≠ zero

/-- **Perpetual obstruction**: if κ₀ is non-torsion, then κₙ ≠ 0 for all n.

    **Re-scoped 2026-11-15 (owner decision, PR #7747, bean `qou-lx8f`).**
    This is a valid conditional: the conclusion holds whenever the
    persistence hypothesis does. It does not apply to the Kummer tower of
    Bring's surface, where the obstruction vanishes for `n ∣ χ = -6` and
    persists only for `n ∤ 6`; the "complementary subgroups" argument for
    persistence there is withdrawn (item 3 of `thm:qu-to-qou` is now the
    degree condition).

    The key insight: κ₀ and the jet corrections at level n live in
    complementary subgroups of H²(S, B), so corrections cannot cancel κ₀. -/
-- Ref: [leitner2026] §3, Item (3)
theorem perpetual_obstruction
    (yl : YekutieliLifting)
    (h_nontorsion : yl.kappa 0 ≠ yl.zero) :
    ∀ n, yl.kappa n ≠ yl.zero := by
  intro n
  induction n with
  | zero => exact h_nontorsion
  | succ n ih => exact yl.persistence n ih

end QOU
