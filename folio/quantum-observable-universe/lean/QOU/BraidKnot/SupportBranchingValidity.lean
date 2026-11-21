import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Sort
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Support branching for the `Xbot` relaxation: what antitonicity does and does not license

`PenaltyFamilyCeiling` excludes the objective-penalty route for certifying an upper bound on
`Xbot` (bean `qou-as81`).  What remains is to change the *feasible set*: split each coordinate
into `u_j = 0` against `u_j ≥ 1`, so that a branch with support `S` relaxes to
`{u_j = 0, j ∉ S} ∩ {u_j ≥ 1, j ∈ S}` and the gap's mechanism — an arbitrarily small real
displacement on arbitrarily many rows — is cut off.  In general that is `2 ^ J` branches
(`J = JPAD = 26`).  The question this file answers is whether the antitonicity of the per-row
tangent slope `Gamma_j` cuts that to the `J + 1 = 27` initial segments `S = {0, …, k-1}`.

**It does not, on its own, and three facts say exactly where the line is.**

1. **A fixed-point supergradient certificate gains nothing from support branching**
   (`affine_box_max_eq_split_max`).  The probe's certificate bounds the branch by
   `F(w) + Σ_j max_{x_j} g_j (x_j - w_j)` at one ascent point `w`.  A linear function on
   `[0, U]` is maximised at an endpoint, and both endpoints `0` and `U` survive the split
   `{0} ∪ [1, U]`.  So per coordinate the split maximum *equals* the unsplit one, and a
   certificate taken at a single `w` returns the same number on every branch.  Branching can
   only help if `w` is re-optimised per branch — one concave solve per branch.  This is the
   observation recorded as unverified at the end of the 2026-10-10 turn; it is now a theorem.
2. **Antitone slopes do not make an initial segment optimal**
   (`antitone_slope_not_sufficient`).  Two concave rows with `Gamma_0 = 2 > Gamma_1 = 1`, but
   row 0 curving `30` times harder: on the branch `u ≥ 1` row 1 alone reaches `5/2` while
   row 0 alone never exceeds `-1`.  The best one-row support is `{1}`, not the initial segment
   `{0}`.  The slope at `u = 0` says nothing about the value at `u ≥ 1`, which is where a
   support branch lives.  So "naive initial-segment branching" is not a valid bound under the
   antitonicity hypothesis alone, whatever the per-row curvatures do.
3. **What *is* licensed: a separable branch bound with antitone row values**
   (`sum_le_sum_initial_segment`, `separable_branch_max_le_initial`).  If the branch bound is
   `Σ_{j ∈ S} c_j` and `c` is antitone, every support of size `k` is dominated by
   `{0, …, k-1}`, so the `2 ^ J` branches collapse to `J + 1`.  But note what the hypothesis
   costs: a separable bound needs **no** branching at all (take `S = {j : c_j > 0}`, itself an
   initial segment when `c` is antitone), and `G` is not separable — its pair terms
   `-eps(g + u_jp - u_j)` couple the rows, which is exactly why the probe's best bound comes
   from a coupled ascent and not from the per-row caps.

So the 27-branch reduction is valid for the bounds that do not need it, and unproved for the one
that does.  For the coupled `G` it would need an *exchange* property of `G` itself, which
`Gamma_j`'s antitonicity does not supply (fact 2).  Nothing here is about `G`'s numbers: every
statement is over an arbitrary real function, and the probe's figures enter nowhere.

-- Ref: [leitner2026] computations/deltalambda/rev_e_infinity_hessian_budget_probe.py
-/

namespace QOU.BraidKnot.SupportBranchingValidity

open Finset

/-! ## 1. A fixed-`w` supergradient certificate is invariant under the support split -/

/-- The unsplit per-coordinate certificate term: `max_{x ∈ [0, U]} g (x - w)`, attained at an
endpoint because the function is affine. -/
noncomputable def boxMax (g w U : ℝ) : ℝ := max (g * (0 - w)) (g * (U - w))

/-- The split per-coordinate term: `max` over `{0} ∪ [1, U]`, i.e. over the three candidate
points `0`, `1` and `U` (an affine function on `[1, U]` is maximised at `1` or `U`). -/
noncomputable def splitMax (g w U : ℝ) : ℝ :=
  max (g * (0 - w)) (max (g * (1 - w)) (g * (U - w)))

/-- Every point of the box is dominated by an endpoint — the reason `boxMax` is the box maximum. -/
theorem affine_le_boxMax {g w U x : ℝ} (hx0 : 0 ≤ x) (hxU : x ≤ U) :
    g * (x - w) ≤ boxMax g w U := by
  unfold boxMax
  rcases le_total 0 g with hg | hg
  · exact le_max_of_le_right (by nlinarith)
  · exact le_max_of_le_left (by nlinarith)

/-- **The split buys nothing at a fixed `w`.**  For `U ≥ 1` the maximum of `g (x - w)` over
`{0} ∪ [1, U]` equals its maximum over `[0, U]`: the extra candidate `x = 1` lies inside the box,
and both endpoints of the box survive the split. -/
theorem affine_box_max_eq_split_max {g w U : ℝ} (hU : 1 ≤ U) :
    splitMax g w U = boxMax g w U := by
  have h1 : g * (1 - w) ≤ boxMax g w U := affine_le_boxMax (by norm_num) hU
  unfold splitMax
  unfold boxMax at h1 ⊢
  apply le_antisymm
  · exact max_le (le_max_left _ _) (max_le h1 (le_max_right _ _))
  · exact max_le (le_max_left _ _) (le_trans (le_max_right _ _) (le_max_right _ _))

/-- The whole certificate, summed over the coordinates of any finite index set, is the same on
every branch: support branching at a fixed ascent point cannot lower it. -/
theorem certificate_split_eq {ι : Type*} (s : Finset ι) (g w U : ι → ℝ)
    (hU : ∀ j ∈ s, 1 ≤ U j) :
    ∑ j ∈ s, splitMax (g j) (w j) (U j) = ∑ j ∈ s, boxMax (g j) (w j) (U j) :=
  Finset.sum_congr rfl fun j hj => affine_box_max_eq_split_max (hU j hj)

/-! ## 2. Antitone slopes do not make an initial segment optimal -/

/-- Row 0: slope `2` at the origin, curvature `3`. -/
def row0 (v : ℝ) : ℝ := 2 * v - 3 * v ^ 2

/-- Row 1: slope `1` at the origin — smaller, so the slopes are antitone — curvature `1/10`. -/
noncomputable def row1 (v : ℝ) : ℝ := v - v ^ 2 / 10

/-- The slopes at the origin are antitone: `row0' 0 = 2 > 1 = row1' 0`.  Stated without the
derivative API: for every small step `0 < h ≤ 1/10`, row 0 is ahead of row 1, so its difference
quotient at the origin is larger. -/
theorem slopes_antitone {h : ℝ} (hh : 0 < h) (hh' : h ≤ 1 / 10) : row1 h < row0 h := by
  unfold row0 row1; nlinarith

/-- **Counterexample.**  On the branch `u ≥ 1`, row 1 alone reaches `5/2` (at `v = 5`), while
row 0 alone stays at or below `-1` everywhere on that branch.  So the best one-row support is
`{1}`, not the initial segment `{0}`, even though the slopes at the origin are antitone. -/
theorem antitone_slope_not_sufficient :
    ∃ v, 1 ≤ v ∧ ∀ v', 1 ≤ v' → row0 v' < row1 v := by
  refine ⟨5, by norm_num, fun v' hv' => ?_⟩
  unfold row0 row1
  nlinarith

/-! ## 3. What antitonicity does license: separable branch bounds -/

/-- **Initial segments dominate.**  If `c` is antitone on `ℕ`, any finite support `S` is
dominated by the initial segment of the same size.  Induction on the largest element `a`: the
rest of `S` lies in `range a`, so `|S| - 1 ≤ a` and `c a ≤ c (|S| - 1)`. -/
theorem sum_le_sum_initial_segment {c : ℕ → ℝ} (hc : Antitone c) (S : Finset ℕ) :
    ∑ j ∈ S, c j ≤ ∑ i ∈ range S.card, c i := by
  induction S using Finset.induction_on_max with
  | h0 => simp
  | step a s hlt ih =>
    have ha : a ∉ s := fun h => lt_irrefl a (hlt a h)
    -- every element of `s` is below `a`, so `s ⊆ range a` and `card s ≤ a`
    have hsub : s ⊆ range a := fun x hx => Finset.mem_range.mpr (hlt x hx)
    have hcard : s.card ≤ a := by simpa using Finset.card_le_card hsub
    rw [Finset.sum_insert ha, Finset.card_insert_of_notMem ha, Finset.sum_range_succ]
    have := hc hcard
    linarith

/-- **The `J + 1`-branch reduction, for separable bounds.**  If the bound on a branch with
support `S ⊆ range J` is `Σ_{j ∈ S} c_j` with `c` antitone, then its maximum over all `2 ^ J`
supports is attained on an initial segment `range k` with `k ≤ J`. -/
theorem separable_branch_max_le_initial {c : ℕ → ℝ} (hc : Antitone c) {J : ℕ} {S : Finset ℕ}
    (hS : S ⊆ range J) :
    ∃ k ≤ J, ∑ j ∈ S, c j ≤ ∑ i ∈ range k, c i := by
  refine ⟨S.card, ?_, sum_le_sum_initial_segment hc S⟩
  simpa using Finset.card_le_card hS

/-- **…and a separable bound needs no branching at all.**  With `c` antitone, the support
`{j < J : 0 < c j}` beats every support, and it is an initial segment.  So the reduction above
is real but only ever applies to bounds that did not need it. -/
theorem separable_branch_le_positive_part {c : ℕ → ℝ} {J : ℕ} {S : Finset ℕ}
    (hS : S ⊆ range J) :
    ∑ j ∈ S, c j ≤ ∑ j ∈ (range J).filter (fun j => 0 < c j), c j := by
  calc ∑ j ∈ S, c j ≤ ∑ j ∈ S.filter (fun j => 0 < c j), c j := by
        rw [← Finset.sum_filter_add_sum_filter_not S (fun j => 0 < c j)]
        have : ∑ j ∈ S.filter (fun j => ¬ 0 < c j), c j ≤ 0 :=
          Finset.sum_nonpos fun j hj => not_lt.mp (Finset.mem_filter.mp hj).2
        linarith
    _ ≤ ∑ j ∈ (range J).filter (fun j => 0 < c j), c j := by
        refine Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset_filter _ hS) ?_
        intro j hj _
        exact le_of_lt (Finset.mem_filter.mp hj).2

end QOU.BraidKnot.SupportBranchingValidity
