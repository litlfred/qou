/-
QOU.Mass.LowerBoundCannotConstrainADifference — a lower bound on each of two
energies says *nothing whatever* about their difference.

Arc context (em-linking; beans `qou-o6ml`, `qou-0hdx`). The Freedman–He link
bound (Komendarczyk arXiv:0808.1533v1 eq. (43), p. 26; verified in this repo at
`library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:203-216`) is an
**inequality**:

  `E_{3/2}(X) ≥ (π/16)^{1/4} · (Σ_{k=1..n} ac(L_k, L)|Flux(X_k)|) · min_k |Flux(X_k)|`

The whole em-linking arc scores against `κ(A)`, which is built from a
**mirror-pair binding split** — a *difference* of two such energies, one for
`(Z, N)` and one for its mirror `(N, Z)`. Every use of eq. (43) in the arc
therefore reads it as an equality (saturation) without ever saying so.

This file measures what that assumption is carrying, and the answer is:
**everything.** From `B₁ ≤ E₁` and `B₂ ≤ E₂`, the difference `E₁ − E₂` is
completely unconstrained — for *any* target value `t` whatsoever there are
energies meeting both bounds whose difference is exactly `t`
(`diff_unconstrained`). The bound does not merely fail to *predict* the split;
it fails to *constrain* it, in either direction.

Three consequences, in the order that matters.

1. **Saturation is not one escape among three — it is prior to the others.**
   `FreedmanHeMirrorSplitChargeBlind.lean` scoped its result to the model class
   `{vertex-transitive carrier} × {charge-only flux} × {saturation}` and named
   three surviving escapes. That framing is **corrected here**: the first two
   are about the *shape* of `B`, and the shape of `B` is only relevant once `B`
   is being read as the energy. Without saturation there is nothing for a
   carrier or an `ac` to be the shape *of*.

2. **What would restore the constraint is an UPPER bound**, which eq. (43) does
   not supply. Given `B₁ ≤ E₁ ≤ U₁` and `B₂ ≤ E₂ ≤ U₂` the difference is
   pinned to `[B₁ − U₂, U₁ − B₂]` (`diff_bounded_of_upper`). Naming the missing
   ingredient precisely is the point: it is not "more topology", it is an upper
   bound on the energy of a knotted flux configuration.

3. **Under saturation the split is determined** (`diff_of_saturated`), which is
   what the arc has been assuming. Stated so the assumption is visible in the
   type rather than buried in a step.

Not measurable here, and said rather than left implicit: one might hope to show
saturation is *implausible* by computing how far `B` sits below the observed
energies. That cannot be done in this corpus — evaluating `B` needs a per-nucleus
carrier link, and `qou-5vhf` establishes the `A ≤ 4` carrier assignments are an
admitted AME-driven census search. So the size of the slack is **unmeasured**,
not measured-and-small.

Base ring: an ordering is genuinely required here (the statements are about `≤`
and about `max`), unlike the sibling `FreedmanHeMirrorSplitChargeBlind.lean`
which is pure ring algebra over a generic `CommRing`. Per AGENTS.md §7c that
makes a linearly-ordered additive group the right home — the weakest structure
admitting the construction, not `ℝ`. Spelled `[AddCommGroup R] [LinearOrder R]
[IsOrderedAddMonoid R]`: the older bundled `LinearOrderedAddCommGroup` is
deprecated in this Mathlib and is no longer a class, so it cannot be used as a
binder at all.
-/
import Mathlib.Algebra.Order.Group.Defs
import Mathlib.Order.MinMax
import Mathlib.Tactic.Abel

namespace QOU.Mass.LowerBoundCannotConstrainADifference

variable {R : Type*} [AddCommGroup R] [LinearOrder R] [IsOrderedAddMonoid R]

/-- **The result.** A lower bound on each of two quantities places *no*
constraint on their difference: for any target `t`, energies satisfying both
bounds exist whose difference is exactly `t`.

The witness is explicit — push `E₂` up until `E₁ = E₂ + t` clears `B₁` as well.
Since `E₂` may be taken arbitrarily large, `t` may be arbitrarily negative; since
`E₁` may be, `t` may be arbitrarily positive. -/
theorem diff_unconstrained (B₁ B₂ t : R) :
    ∃ E₁ E₂ : R, B₁ ≤ E₁ ∧ B₂ ≤ E₂ ∧ E₁ - E₂ = t := by
  refine ⟨max B₂ (B₁ - t) + t, max B₂ (B₁ - t), ?_, le_max_left _ _, by abel⟩
  have h : B₁ - t ≤ max B₂ (B₁ - t) := le_max_right _ _
  calc B₁ = (B₁ - t) + t := by abel
    _ ≤ max B₂ (B₁ - t) + t := add_le_add_right h t

/-- The same fact in the form the arc needs to hear it: **no** value of the
mirror split is excluded by the bound. Whatever the AME ladder had turned out to
be — constant, growing, falling, alternating — eq. (43) would have been
consistent with it. -/
theorem no_split_value_is_excluded (B₁ B₂ : R) :
    ∀ t : R, ∃ E₁ E₂ : R, B₁ ≤ E₁ ∧ B₂ ≤ E₂ ∧ E₁ - E₂ = t :=
  fun t => diff_unconstrained B₁ B₂ t

omit [LinearOrder R] [IsOrderedAddMonoid R] in
/-- **What the arc has been assuming.** If the bound is *saturated* — read as an
equality — the difference is determined by the bounds alone. This is the step
that has been taken silently; here it is, with `saturation` as a named
hypothesis. -/
theorem diff_of_saturated {E₁ E₂ B₁ B₂ : R} (h₁ : E₁ = B₁) (h₂ : E₂ = B₂) :
    E₁ - E₂ = B₁ - B₂ := by
  rw [h₁, h₂]

/-- **What would restore a constraint without saturation: an UPPER bound.**
Given two-sided bounds the difference is pinned to an interval. Eq. (43) supplies
only the lower half, so this names the missing ingredient exactly — not more
topology, but an upper bound on the energy of a knotted flux configuration. -/
theorem diff_bounded_of_upper {E₁ E₂ B₁ B₂ U₁ U₂ : R}
    (h₁ : B₁ ≤ E₁) (h₁' : E₁ ≤ U₁) (h₂ : B₂ ≤ E₂) (h₂' : E₂ ≤ U₂) :
    B₁ - U₂ ≤ E₁ - E₂ ∧ E₁ - E₂ ≤ U₁ - B₂ :=
  ⟨sub_le_sub h₁ h₂', sub_le_sub h₁' h₂⟩

omit [IsOrderedAddMonoid R] in
/-- The interval of `diff_bounded_of_upper` collapses to a point exactly when
both bounds are tight, recovering `diff_of_saturated`. So saturation is the
*extreme* case of the two-sided situation, not a mild simplification of it: it
assumes the upper bound coincides with the lower one. -/
theorem diff_eq_of_bounds_saturated {E₁ E₂ B₁ B₂ : R}
    (h₁ : B₁ ≤ E₁) (h₁' : E₁ ≤ B₁) (h₂ : B₂ ≤ E₂) (h₂' : E₂ ≤ B₂) :
    E₁ - E₂ = B₁ - B₂ :=
  diff_of_saturated (le_antisymm h₁' h₁) (le_antisymm h₂' h₂)

end QOU.Mass.LowerBoundCannotConstrainADifference
