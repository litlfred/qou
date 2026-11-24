import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# What an integrality penalty can buy, and why it is not enough

`SupergradientCertificate` bounds a concave maximum over a box.  The `Xbot` relaxation in
`rev_e_infinity_xbot_relaxation_probe` uses that machinery on a *penalised* objective: the
integer supremum of `G` is bounded by the real supremum of

    G_lam(u)  =  G(u) + lam * sum_j (u_j^2 - u_j) ,

valid because every integer `u_j >= 0` satisfies `u_j^2 >= u_j`, and still concave because
`+lam sum u^2` eats into `G`'s own `-(ln q0 / 2) sum u^2`.  Measured, the penalty is selected
non-trivially (`lam* = 0.010434072`, a fifth of the probe's concavity limit) and the resulting
all-`T` bound is `1.56363x` the enumerated maximum.  Closing the arc needs `1.1873x`.

This file is the formalize-first prune on that gap: **the whole penalty family is capped, and
the cap is below what the arc needs.**  Three steps, none of them about `G`:

1. **A bounded penalty buys at most its own depth** (`drop_le_of_bounded_penalty`).  If a bound
   `B` holds for `f + h` and `h >= -M`, then `f <= B + M`.  Contrapositively: driving the
   certified bound down by more than `M` is impossible, whatever `h` is.
2. **A separable penalty's depth is its per-coordinate depth times the coordinate count**
   (`sum_penalty_ge`).  So `M = J * d` with `d` the deepest a single row can be charged.
3. **The deepest admissible per-coordinate penalty is `-lam/4`** (`unit_penalty_ge_neg_quarter`),
   attained at a half-integer.  The quadratic penalty achieves exactly this on `[0, 1]`, and
   the *pointwise-optimal* admissible penalty — the sawtooth `lam * frac(u) * (frac(u) - 1)`,
   which vanishes at **every** non-negative integer rather than growing like `lam u^2` — can do
   no better per row (`sawtooth_le_quadratic_of_one_le` shows it is at least never worse).

Putting the three together gives `certified_floor`: if the unpenalised objective reaches `S`
somewhere and the penalty's depth is `M`, then **every** bound this family can certify is at
least `S - M`.  With the probe's own figures — `sup G ≥ 3.27708095409687544` from the `lam = 0`
ascent at `pe = 6` (KKT residual `9.4e-14`), `lam_max = ln q0 / 2`, `J = 26` — the depth is at
most `0.33910734` and the floor is `2.93797361 = 1.3603x` the enumerated maximum, while
`cut <= 32` needs `1.1873x` (`floor_exceeds_cut32_requirement`).

**The family is excluded, not merely short.**  Two things make the floor the right form rather
than the shortfall form I reached for first.  It is *charge-free*: it binds with the padded box
charge set to zero, so the padding lead — worth `0.100063`, and the other live candidate for
this gap — cannot rescue it.  And it does not bundle the charge into the quantity being closed,
which the shortfall arrangement (cap `0.3391` against the certificate's overshoot `0.8128`) did,
reporting a factor `2.4` where the honest figure is `2.1`.

`budget_needed_for_cut_32` is the falsifiable condition: the curvature budget would have to be
`>= 0.1096`, i.e. `2.1x` the limit the probe can justify (`2.87x` for parity with the G1 route).

**That condition has since been measured and it does not hold.**  `ln q0 / 2` is sufficient,
not measured; the true budget is `-lam_max(H_G)/2`, and over the Hessian of the probe's own
gradient the tightest sampled value is `0.0643955 = 1.2343x` the probe's limit, well under the
`2.1018x` required (`floor_at_measured_budget_exceeds_cut32`; the floor rises only from
`1.3603x` to `1.3235x`, against `1.1873x` needed).  A sampled point upper-bounds a budget that
is an infimum, so this **closes** the condition.  The exclusion is therefore no longer
conditional on the probe's sufficient bound — only on the sampling, which is stated with the
measurement.

## What this does and does not establish

It is a **scope-(b) exclusion of the objective-penalty route, conditional on the curvature
budget**: no choice of `lam`, and no choice of separable penalty at that `lam`, closes the gap.
It is **not** a statement that the concave route fails — `lam_max = ln q0 / 2` is a *sufficient*
concavity condition in the probe, not a measured budget (`G` carries extra negative curvature
from its gain functions), so exhibiting a larger admissible budget reopens the route.  That is
exactly what `budget_needed_for_cut_32` is for.  Nor does it bear on changing the *feasible
set* rather than the objective, which is where the remaining room is.

Arc: bean `qou-as81` (A1), epic `qou-3e6w`.
-/

namespace QOU.BraidKnot.PenaltyFamilyCeiling

/-- **A concave penalty is useless, which is why an admissible one must be convex somewhere.**
If `p` is concave and non-negative at the two ends of a cell, it is non-negative throughout —
so a penalty that is concave on `[0, ∞)` and valid at every non-negative integer satisfies
`p ≥ 0` everywhere, and `G + p ≥ G` makes the bound *worse* than the plain relaxation.

This is the structural reason the admissible family is shaped the way it is: a useful penalty
must have a convex region (so that it can dip below zero strictly inside a cell while vanishing
at the cell's integer ends), and its curvature is then capped by `G`'s own concavity.  The cap
is what `unit_penalty_ge_neg_quarter` turns into a depth, and the depth is what
`certified_floor` turns into an exclusion. -/
theorem concave_penalty_useless (p : ℝ → ℝ) (a b : ℝ) (t : ℝ)
    (hconc : ∀ x y : ℝ, ∀ u v : ℝ, 0 ≤ u → 0 ≤ v → u + v = 1 →
      u * p x + v * p y ≤ p (u * x + v * y))
    (ha : 0 ≤ p a) (hb : 0 ≤ p b) (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    0 ≤ p ((1 - t) * a + t * b) := by
  have hco := hconc a b (1 - t) t (by linarith) h0 (by ring)
  have h2 : 0 ≤ (1 - t) * p a := mul_nonneg (by linarith) ha
  have h3 : 0 ≤ t * p b := mul_nonneg h0 hb
  linarith

/-- **A bounded penalty buys at most its own depth.**  If `B` bounds the penalised objective
`f + h` everywhere and the penalty never dips below `-M`, then `B + M` bounds `f`.  Read the
other way: a certificate on `f + h` cannot be better than a certificate on `f` by more than
`M`, so `M` caps what the penalty is worth. -/
theorem drop_le_of_bounded_penalty {α : Type*} (f h : α → ℝ) (M B : ℝ)
    (hM : ∀ x, -M ≤ h x) (hB : ∀ x, f x + h x ≤ B) :
    ∀ x, f x ≤ B + M := by
  intro x
  have h1 := hM x
  have h2 := hB x
  linarith

/-- A separable penalty bounded below by `-d` on each coordinate is bounded below by
`-(card * d)` in total.  This is the step that makes the cap scale with the number of rows the
ascent actually carries — and no further, since a padded row sits at `u = 0`, where every
penalty in the family vanishes. -/
theorem sum_penalty_ge {ι : Type*} (s : Finset ι) (p : ι → ℝ) (d : ℝ)
    (hp : ∀ i ∈ s, -d ≤ p i) :
    -(s.card * d) ≤ ∑ i ∈ s, p i := by
  have := Finset.sum_le_sum hp
  simpa [Finset.sum_const, mul_comm, neg_mul] using this

/-- **The deepest an admissible per-coordinate penalty can dip is `-lam/4`.**  For `lam ≥ 0`,
`lam * t * (t - 1) ≥ -lam/4`, with equality at `t = 1/2`.  The constant is `1/4` and not
something larger because the penalty must vanish at both ends of the unit cell: it is zero at
`t = 0` and `t = 1` (validity at integer points), and its curvature is `2 lam` (the concavity
budget), which fixes the depth.

**No restriction on `t` is needed**, and that is worth stating rather than hiding behind a
`0 ≤ t ≤ 1` hypothesis the proof does not use: the inequality is `lam * (t - 1/2)^2 ≥ 0`, so it
holds for every real `t`.  The depth bound is therefore a property of the *cell shape* alone and
transfers to every cell of a sawtooth penalty without a per-cell argument. -/
theorem unit_penalty_ge_neg_quarter (lam t : ℝ) (hlam : 0 ≤ lam) :
    -(lam / 4) ≤ lam * (t * (t - 1)) := by
  nlinarith [mul_nonneg hlam (sq_nonneg (2 * t - 1))]

/-- The depth is attained: at the half-integer the penalty is exactly `-lam/4`.  Without this
the bound above could be vacuously loose, and the cap would not be the right number. -/
theorem unit_penalty_eq_neg_quarter (lam : ℝ) :
    lam * ((1 / 2 : ℝ) * ((1 / 2 : ℝ) - 1)) = -(lam / 4) := by ring

/-- The quadratic penalty is non-negative from `1` on, so beyond the first cell it **loosens**
the bound rather than tightening it.  This is what the sawtooth form avoids. -/
theorem quadratic_nonneg_of_one_le (lam u : ℝ) (hlam : 0 ≤ lam) (hu : 1 ≤ u) :
    0 ≤ lam * (u ^ 2 - u) := by
  have : 0 ≤ u ^ 2 - u := by nlinarith
  exact mul_nonneg hlam this

/-- A sawtooth penalty — one that vanishes at every non-negative integer — is never worse than
the quadratic one past the first cell, because it stays non-positive there while the quadratic
has gone non-negative.  Stated on the fractional part `t ∈ [0, 1]` of `u ≥ 1`.

Together with the fact that the two **coincide** on `[0, 1]` (both are `lam * u * (u - 1)`
there), this says the sawtooth dominates the quadratic pointwise — so it is the right member of
the family to take, and it still obeys the same `-lam/4` depth, hence the same cap. -/
theorem sawtooth_le_quadratic_of_one_le (lam u t : ℝ) (hlam : 0 ≤ lam) (hu : 1 ≤ u)
    (h0 : 0 ≤ t) (h1 : t ≤ 1) :
    lam * (t * (t - 1)) ≤ lam * (u ^ 2 - u) := by
  have hsaw : lam * (t * (t - 1)) ≤ 0 := by
    have : t * (t - 1) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos h0 (by linarith)
    exact mul_nonpos_of_nonneg_of_nonpos hlam this
  exact hsaw.trans (quadratic_nonneg_of_one_le lam u hlam hu)

/-- **A FLOOR, not merely a shortfall: no admissible penalty can certify below
`sup G - M`.**  If the unpenalised objective is known to reach `S` somewhere, and the penalty
never dips below `-M`, then every bound valid for the penalised objective is at least `S - M`.
This is the sharp form of the cap and the one the numeric theorems below use.

Why it matters that this is a floor rather than a shortfall: a *shortfall* statement compares
the cap against the overshoot of the measured certificate, which bundles the box charge in with
the relaxation gap and so understates the obstruction.  The floor is charge-free — it binds even
if the padded charge were driven to zero. -/
theorem certified_floor {α : Type*} (f h : α → ℝ) (x₀ : α) (S M B : ℝ)
    (hS : S ≤ f x₀) (hM : ∀ x, -M ≤ h x) (hB : ∀ x, f x + h x ≤ B) :
    S - M ≤ B := by
  have h1 := hM x₀
  have h2 := hB x₀
  linarith

/-- **The floor, with the probe's own numbers, exceeds what the arc needs.**  The `lam = 0`
ascent at `pe = 6` measured `sup G ≥ 3.27708095409687544` (KKT residual `9.4e-14`), and at the
concavity limit `lam_max = ln q0 / 2 = 0.0521703601597597...` over the ascent's `J = 26` rows
the deepest admissible separable penalty is `26 * lam_max / 4 = 0.33910734...`.  So every bound
this family can certify is at least `2.93797361 = 1.3603x` the enumerated maximum, while
`cut <= 32` needs `2.56436046289398077 = 1.1873x`.

The family is therefore **excluded**, not merely short — and excluded with the box charge set to
zero, so the padding lead cannot rescue it either. -/
theorem floor_exceeds_cut32_requirement :
    (2.5643604628939807681 : ℝ) < 3.27708095409687544 - 26 * (0.0521703601597597 / 4) := by
  norm_num

/-- **The budget was measured, and it does not reopen the route.**  `ln q0 / 2` is only a
sufficient concavity condition in the probe; the true budget is `-lam_max(H_G)/2`, since
`G + lam * sum (u^2 - u)` is concave exactly when `H_G + 2 lam I <= 0`.  Measured over the
Hessian of the probe's own gradient at `mp.dps = 60`
([`rev_e_infinity_hessian_budget_probe.py`](computations/deltalambda/rev_e_infinity_hessian_budget_probe.py)),
the tightest sampled value is `0.06439550031177121` at `pe = 0`, `T = JPAD = 26` —
`1.2343x` the probe's limit, against the `2.1018x` `budget_needed_for_cut_32` demands.

The floor at that budget is `3.27708095409687544 - 26 * 0.06439550031177121 / 4 =
2.858510202 = 1.3235x`, still above the `1.1873x` the arc needs, by `0.294149739`.  Since a
sampled point is an *upper* bound on a budget that is an infimum over the domain, and the
measured budget decreases with the row count and is still decreasing at `T = JPAD`, this
**closes** the reopening condition rather than merely failing to meet it.

Trap recorded with the measurement: the **diagonal** of `H_G` reads `lam <= 0.413049687
= 7.9173x`, which looks like a decisive reopening.  `lam_max(H_G) >= max_i H_ii`, so that is
also only an upper bound — and the cross terms (the pair gains) inflate it by `6.41x`. -/
theorem floor_at_measured_budget_exceeds_cut32 :
    (2.5643604628939807681 : ℝ) < 3.27708095409687544 - 26 * (0.06439550031177121 / 4) := by
  norm_num

/-- The falsifiable form, and the only thing that reopens the route: for the floor to drop to
the `cut <= 32` requirement the per-row depth `lam / 4` must satisfy
`26 * lam / 4 ≥ 3.27708095409687544 - 2.5643604628939807681`, hence `lam ≥ 0.1096`.  The probe
can justify `lam < ln q0 / 2 = 0.05218`, so the route needs a curvature budget `2.1x` larger
than the one it has.  `lam_max` is a *sufficient* concavity condition there, not a measured
budget — `G` carries extra negative curvature from its gain functions — so exhibiting a larger
admissible budget is a live and well-posed question.  Nothing here forbids it. -/
theorem budget_needed_for_cut_32 (lam : ℝ)
    (h : 3.27708095409687544 - 26 * (lam / 4) ≤ 2.5643604628939807681) :
    (0.1096 : ℝ) ≤ lam := by
  norm_num at h
  linarith

/-- And the *selected* `lam` is far weaker still: at `lam* = 0.010434072` the depth is
`26 * lam* / 4 = 0.0678214682`, so that program's floor is `3.20925948 = 1.4859x`.  `lam`'s
entire contribution — already exercised, already inside the measured `1.56363x` — is bounded by
`0.068`. -/
theorem selected_lam_floor :
    (3.2092 : ℝ) < 3.27708095409687544 - 26 * (0.010434072 / 4) := by
  norm_num

/-- Subtracting the threshold zero-point-one-zero-nine-six from the required curvature parameter yields a non-negative difference. -/
theorem budget_needed_for_cut_32_sub_nonneg (lam : ℝ)
    (h : 3.27708095409687544 - 26 * (lam / 4) ≤ 2.5643604628939807681) :
    0 ≤ lam - (0.1096 : ℝ) :=
  sub_nonneg.mpr (budget_needed_for_cut_32 lam h)

end QOU.BraidKnot.PenaltyFamilyCeiling
