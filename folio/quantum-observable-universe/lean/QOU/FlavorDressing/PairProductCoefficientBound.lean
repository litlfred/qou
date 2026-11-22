import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring.List
import Mathlib.Algebra.Order.BigOperators.Group.List
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.FlavorDressing.PairProductCoefficientBound — the ½ ceiling on a positive-weight pair product

The proton–neutron flavor split is `Δm_pn/M_N = leading·(1 + α·leading)`, where
`leading = (q−1)²(1−q⁻⁴)/3` is conjectured (`conj:flavor-split-substrate-mass`) and the **second-order
normalization** `α ≈ 0.929254` is the single open coefficient (see
`docs/audits/2026-06-29-flavor-split-partial-derivation.md`). One candidate mechanism is a
**multiplicative pair product** `1 + split = ∏_k (1 + s_k)` with `Σ_k s_k = leading`, whose cross-term
`Σ_{k<l} s_k s_l = α·leading²` supplies the second-order coefficient `α`.

This file proves the structural ceiling on that mechanism: for **any** finite list of **positive**
weights, the pairwise-product sum is strictly below half the square of the total, so

    α = (Σ_{k<l} s_k s_l) / (Σ_k s_k)²  <  1/2.

The equal-split value `(m−1)/(2m)` is the *maximum* of this ratio; unequal weighting only lowers it
(the sum-of-squares term grows). Since the measured `α ≈ 0.929254 > 1/2`, the positive-weight pair
product is **excluded** as the source of `α` — a scope-(b) structural exclusion via a proved
invariant. This sharpens Part 2a of the partial-derivation audit (which excluded only the *equal*-split
case and left "the swapped pair dominates" open: unequal dominance moves `α` the wrong way, toward `0`,
not toward `0.929`). The `α`-derivation must therefore live on the self-energy / geometric-series side
(`split = leading/(1 − leading)`, coefficient `1`), not the pair-count side.

This is a narrowing of an open problem, not a closure: `α ≈ 0.929` itself remains underived, and this
result does not move the L2 dashboard.

-- Ref: [leitner2026] docs/audits/2026-07-26-flavor-split-pair-product-half-ceiling.md
-/

namespace QOU.FlavorDressing

/-- Sum of pairwise products `Σ_{i<j} s_i s_j` over a list: each element times the sum of the
elements strictly after it. -/
def pairSum : List ℝ → ℝ
  | [] => 0
  | x :: t => x * t.sum + pairSum t

/-- The Newton identity `(Σ s)² = Σ s² + 2·(Σ_{i<j} s_i s_j)` (sorry-free, induction on the list). -/
theorem sq_sum_eq (s : List ℝ) :
    (s.sum) ^ 2 = (s.map (· ^ 2)).sum + 2 * pairSum s := by
  induction s with
  | nil => simp [pairSum]
  | cons x t ih =>
      simp only [List.sum_cons, List.map_cons, pairSum]
      ring_nf
      ring_nf at ih
      linarith [ih]

/-- **The ½ ceiling.** For a nonempty list of positive reals, the pairwise-product sum is strictly
less than half the square of the total: `2·pairSum s < (Σ s)²`. Equivalently the second-order
coefficient of any positive-weight multiplicative pair product satisfies
`α = pairSum s / (Σ s)² < 1/2`. Consequence: the measured flavor-split `α ≈ 0.929254 > 1/2` cannot
arise from such a product — the positive-weight pair-count mechanism is excluded (scope-(b)). -/
theorem pairSum_lt_half_sq {s : List ℝ} (hpos : ∀ x ∈ s, 0 < x) (hne : s ≠ []) :
    2 * pairSum s < (s.sum) ^ 2 := by
  have hqpos : 0 < (s.map (· ^ 2)).sum := by
    obtain ⟨a, ha⟩ := List.exists_mem_of_ne_nil s hne
    have hnn : ∀ y ∈ s.map (· ^ 2), 0 ≤ y := by
      intro y hy
      simp only [List.mem_map] at hy
      obtain ⟨z, _, rfl⟩ := hy
      positivity
    have hmem : a ^ 2 ∈ s.map (· ^ 2) := List.mem_map_of_mem ha
    have hpa : 0 < a ^ 2 := by have := hpos a ha; positivity
    exact lt_of_lt_of_le hpa (List.single_le_sum hnn _ hmem)
  have h := sq_sum_eq s
  linarith

end QOU.FlavorDressing
