import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
# Certifying a concave maximum, and what a capped enumeration does not tell you

`SearchCoercivity` made the `e_inf` search *finite*.  This file is about the two steps that make
it *decided*, and about the one step of the argument that is not a step at all.

The objective `F` is concave, so it obeys the supergradient inequality at every point.  That
alone bounds nothing — the linear term `grad F(w) . (u - w)` is unbounded above on an unbounded
domain — so the search region is confined first, by an independent per-row bound, and the linear
term is then maximised over the resulting box.  `sup_le_of_supergradient` is that argument,
stated for an arbitrary `F`, `w`, gradient `g` and box: nothing here knows what the `REV_n`
objective is.

## The step that is easy to get wrong, and was

Maximising `g i * (u i - w i)` over `u i ∈ [lo i, hi i]` is a **case split on the sign of
`g i`** — at `hi i` when `g i ≥ 0` and at `lo i` when `g i < 0`.  Charging every coordinate
`|g i| * (hi i - w i)` regardless looks conservative and is not: it is a different quantity, and
in the measured case it is larger by a factor of `2.25e11`, which turns a certificate with slack
`6.4e-12` into one with slack `1.447` — still true, and useless.

`boundary_charge_eq_zero` and `abs_charge_pos` isolate why.  At the optimum the constrained
coordinates sit ON the lower boundary with strictly negative gradients (correct KKT behaviour,
not a convergence failure).  For such a coordinate the correct charge `g * (lo - w)` is
**exactly zero** when `w = lo`, while `|g| * (hi - lo)` is **strictly positive**.  The whole
factor lives in that one case.

## What a capped enumeration is evidence for

`Xbot` — the bottom edge of the `e_inf` staircase — is tabulated by enumerating profiles with a
cap on their length.  A capped maximum is a **lower** bound on the true one, so observing
`capped < other` says nothing whatever about `true ≤ other`.  `capped_lt_not_sufficient` is that
non-implication, with an explicit witness: `cap = 0 ≤ true = 2`, `cap = 0 < other = 1`, and
`2 ≤ 1` is false.

The corpus recorded one observation in favour of `Xbot(s) <= Xblock(s)` — *"the top is higher by
0.01982 at `s = 13`"* — and it is precisely of that shape, with the bottom table's row cap
saturated at the point of measurement.  Lifting the cap makes the two tables exactly equal there
(`rev_e_infinity_g1_bottom_edge_cap_probe.py`, 5/5).  The inequality is neither proved nor
refuted by any of it; what the probe removes is the appearance of support.

| | |
|---|---|
| `box_mul_sub_le` | the linear term over `[lo, hi]` is maximised at an endpoint chosen by `sign g` |
| `boundary_charge_eq_zero` | on the lower boundary with `g < 0` the correct charge vanishes |
| `abs_charge_pos` | the absolute-value charge there does not |
| `sup_le_of_supergradient` | confinement + supergradient ⇒ an explicit bound on `F` |
| `capped_lt_not_sufficient` | a capped maximum falling short of a bound proves nothing about the true one |

-- Ref: [manuscript] `computations/deltalambda/rev_e_infinity_block_sup_relaxation_probe.py`
-/

namespace QOU.BraidKnot.SupergradientCertificate

open Finset

/-- **The box maximisation.**  Over `x ∈ [lo, hi]`, the linear term `g * (x - w)` is largest at
`hi` when `g` is non-negative and at `lo` when it is negative.

This is the load-bearing case split of the certificate.  Both branches are needed: replacing the
`g < 0` branch by anything that does not evaluate at `lo` gives a valid but far weaker bound. -/
theorem box_mul_sub_le (g w lo hi x : ℝ) (h1 : lo ≤ x) (h2 : x ≤ hi) :
    g * (x - w) ≤ if 0 ≤ g then g * (hi - w) else g * (lo - w) := by
  split_ifs with hg
  · nlinarith
  · push_neg at hg
    nlinarith

/-- **Why the case split is worth `2.25e11`.**  A coordinate pinned to the lower boundary
(`w = lo`) with a strictly negative gradient contributes **exactly nothing** to the slack. -/
theorem boundary_charge_eq_zero (g lo hi : ℝ) (hg : g < 0) :
    (if 0 ≤ g then g * (hi - lo) else g * (lo - lo)) = 0 := by
  rw [if_neg (not_le.mpr hg)]
  ring

/-- The absolute-value charge at the same point is strictly positive — so the two differ by the
whole of it, not by a refinement. -/
theorem abs_charge_pos (g lo hi : ℝ) (hg : g < 0) (h : lo < hi) :
    0 < |g| * (hi - lo) := by
  have hga : 0 < |g| := abs_pos.mpr (ne_of_lt hg)
  have : 0 < hi - lo := sub_pos.mpr h
  positivity

/-- **The certificate.**  If `F` obeys a supergradient inequality at `w`, and every `u` that
reaches the incumbent `V` is confined to the box `∏ [lo i, hi i]`, then `F` is bounded above
everywhere by an explicit number: the incumbent, or `F w` plus the box-maximised linear term.

Neither hypothesis mentions concavity by name — `hconc` is what concavity *supplies*, and
`hbox` is what an independent coercivity bound supplies.  The conclusion holds at every `u`,
including those outside the box, which is the point: outside it, `F u < V`. -/
theorem sup_le_of_supergradient {ι : Type*} [Fintype ι]
    (F : (ι → ℝ) → ℝ) (w g lo hi : ι → ℝ) (V : ℝ)
    (hconc : ∀ u, F u ≤ F w + ∑ i, g i * (u i - w i))
    (hbox : ∀ u, V ≤ F u → ∀ i, lo i ≤ u i ∧ u i ≤ hi i)
    (u : ι → ℝ) :
    F u ≤ max V (F w + ∑ i, if 0 ≤ g i then g i * (hi i - w i) else g i * (lo i - w i)) := by
  by_cases hV : V ≤ F u
  · refine le_trans (hconc u) (le_trans (add_le_add_left ?_ (F w)) (le_max_right _ _))
    refine Finset.sum_le_sum fun i _ => ?_
    obtain ⟨h1, h2⟩ := hbox u hV i
    exact box_mul_sub_le (g i) (w i) (lo i) (hi i) (u i) h1 h2
  · exact le_trans (le_of_lt (not_le.mp hV)) (le_max_left _ _)

/-- **A capped maximum falling short proves nothing about the true one.**  `cap ≤ true` and
`cap < other` are jointly satisfiable with `¬ (true ≤ other)`, so the inference is invalid.

This is the shape of the corpus's sole recorded evidence for `Xbot(s) ≤ Xblock(s)`: a bottom
table whose enumeration cap was saturated at the measured point. -/
theorem capped_lt_not_sufficient :
    ∃ cap true_ other : ℝ, cap ≤ true_ ∧ cap < other ∧ ¬ (true_ ≤ other) :=
  ⟨0, 2, 1, by norm_num, by norm_num, by norm_num⟩

/-- The direction that *is* valid: a capped maximum is a lower bound on the true one, so a capped
value EXCEEDING a bound does refute the bound.  Only the refuting direction survives. -/
theorem capped_gt_is_sufficient {cap true_ other : ℝ} (hle : cap ≤ true_) (h : other < cap) :
    ¬ (true_ ≤ other) := by
  intro hcon
  linarith

end QOU.BraidKnot.SupergradientCertificate
