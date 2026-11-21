import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import QOU.BraidKnot.SearchCoercivity

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

## Bounding every block length with one certificate

The top edge's blocks have every entry `≥ 1`, so a row whose tangent slope falls below
`ln q₀ / 2` contributes a strictly *negative* cap, the cumulative cap eventually drops below the
certified bound, and no longer block can reach it.  The **bottom** edge's class permits zero
entries, so its relaxation has `u ≥ 0`, every row cap is `≥ 0`, the cumulative cap is
non-decreasing — and that argument has no analogue.  Reusing it there would be a false
transfer, and the shape of the two classes is the whole of the difference.

What replaces it is a different move.  The bottom edge's per-row slope turns out to be
**independent of the block length** (the block rows above a given row and the undisplaced tail
above the block are one sum split at an arbitrary place), so a length-`T` program is the
restriction of a single program to its first `T` coordinates, and a certificate taken at an
ascent point *padded with zeros* bounds them all — at the cost of whatever the padded
coordinates are charged.

**They are not charged zero, and expecting that was the error here.**  `box_charge_eq_zero_of_nonpos`
says when a padded coordinate costs nothing, and the measurement says the hypothesis fails: in
the bottom frame every slope is *strictly positive*, being `∑_{i odd} gx(b₀ⱼ + i)` — the odd gaps
the one-body term reaches and the gap-2 ladder does not.  So the operative lemma is
`sum_charge_extend_le`, which bounds the padded block rather than deleting it; the charges decay
geometrically and the probe carries rows until the marginal one is negligible, then bounds the
remainder by its geometric tail instead of dropping it.  The zero version is kept because it is
the statement one reaches for first, and because its hypothesis — `g ≤ 0`, not `g < 0`, since a
padded coordinate may have gradient exactly zero and there the `if` takes the *opposite* branch
— is the part that is easy to get wrong when the situation does permit it.

| | |
|---|---|
| `box_mul_sub_le` | the linear term over `[lo, hi]` is maximised at an endpoint chosen by `sign g` |
| `boundary_charge_eq_zero` | on the lower boundary with `g < 0` the correct charge vanishes |
| `abs_charge_pos` | the absolute-value charge there does not |
| `sup_le_of_supergradient` | confinement + supergradient ⇒ an explicit bound on `F` |
| `box_charge_eq_zero_of_nonpos` | a padded coordinate (`g ≤ 0`, `w = lo`) is charged zero in both branches |
| `sum_charge_extend` | if every padded coordinate is charged zero the bound is unchanged |
| `sum_charge_extend_le` | and when they are not — the bottom edge's case — the bound grows by at most their total |
| `capped_lt_not_sufficient` | a capped maximum falling short of a bound proves nothing about the true one |

-- Ref: [leitner2026] `computations/deltalambda/rev_e_infinity_block_sup_relaxation_probe.py`
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

/-- **Padding a certificate is free.**  A coordinate whose gradient is non-positive and whose
reference point sits ON the lower box endpoint is charged exactly nothing — in *either* branch
of the sign split, which is why the hypothesis is `g ≤ 0` and not `g < 0`.

`boundary_charge_eq_zero` above is the strict case seen at a KKT-active coordinate.  This is the
one the length argument needs, because a padded coordinate may have gradient exactly `0`, and
there the `if` takes the *other* branch (`0 ≤ g`) and lands on `g * (hi - w)` — zero for a
different reason. -/
theorem box_charge_eq_zero_of_nonpos (g lo hi w : ℝ) (hg : g ≤ 0) (hw : w = lo) :
    (if 0 ≤ g then g * (hi - w) else g * (lo - w)) = 0 := by
  subst hw
  split_ifs with h
  · have : g = 0 := le_antisymm hg h
    simp [this]
  · ring

/-- **The same bound over a larger index set.**  Split the coordinates into the ones the ascent
point actually uses and the ones it was padded with; if every padded coordinate is charged zero,
the certificate's linear term is exactly the one computed over the used coordinates alone.

This is what turns a certificate at one block length into a certificate at every block length.
It is a statement about the *sum*, and it carries no analytic content — which is the point: the
analytic content is that the padded coordinates satisfy `box_charge_eq_zero_of_nonpos`, and that
is checked, not assumed. -/
theorem sum_charge_extend {ι κ : Type*} [Fintype ι] [Fintype κ] (g lo hi w : ι ⊕ κ → ℝ)
    (hz : ∀ b : κ, (if 0 ≤ g (Sum.inr b) then g (Sum.inr b) * (hi (Sum.inr b) - w (Sum.inr b))
                    else g (Sum.inr b) * (lo (Sum.inr b) - w (Sum.inr b))) = 0) :
    (∑ x, if 0 ≤ g x then g x * (hi x - w x) else g x * (lo x - w x))
      = ∑ a : ι, (if 0 ≤ g (Sum.inl a) then g (Sum.inl a) * (hi (Sum.inl a) - w (Sum.inl a))
                  else g (Sum.inl a) * (lo (Sum.inl a) - w (Sum.inl a))) := by
  rw [Fintype.sum_sum_type]
  simp [hz]

/-- **The version the measurement actually needs.**  The padded coordinates are not free, so
they are *bounded* rather than deleted: whatever they are charged in total, the certificate over
the larger index set exceeds the one over `ι` by at most that.

This is the honest form of `sum_charge_extend`, and the two differ in exactly the way a
geometric tail differs from a vanishing one — which is the whole content of the bottom-edge
case, where every slope is strictly positive and only the *decay* is available. -/
theorem sum_charge_extend_le {ι κ : Type*} [Fintype ι] [Fintype κ] (g lo hi w : ι ⊕ κ → ℝ)
    (B : ℝ)
    (hB : (∑ b : κ, if 0 ≤ g (Sum.inr b) then g (Sum.inr b) * (hi (Sum.inr b) - w (Sum.inr b))
                    else g (Sum.inr b) * (lo (Sum.inr b) - w (Sum.inr b))) ≤ B) :
    (∑ x, if 0 ≤ g x then g x * (hi x - w x) else g x * (lo x - w x))
      ≤ (∑ a : ι, (if 0 ≤ g (Sum.inl a) then g (Sum.inl a) * (hi (Sum.inl a) - w (Sum.inl a))
                   else g (Sum.inl a) * (lo (Sum.inl a) - w (Sum.inl a)))) + B := by
  rw [Fintype.sum_sum_type]
  exact add_le_add_left hB _

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

/-- **The hypothesis `sum_charge_extend` assumes, discharged from monotonicity.**

`sum_charge_extend` is stated over *"if every padded coordinate is charged zero"*, and says in
its own docstring that the analytic content is elsewhere: *"the padded coordinates satisfy
`box_charge_eq_zero_of_nonpos`, and that is checked, not assumed."*  This is the lemma that
stops it being assumed, for the one reason the bottom-edge frame actually supplies.

The per-row gradient is `Γ j - c j - lam`, with `Γ` the row's tangent slope, `c j ≥ 0` the linear
wall cost, and `lam ≥ 0` the integrality-gap multiplier.  `Γ` is *antitone* in the row index, so
a single row `J` with `Γ J ≤ lam` forces the whole tail beyond it non-positive — one inequality
covers infinitely many coordinates, which is exactly what a certificate at every block length
needs.

Note `c` enters only through `0 ≤ c j`: subtracting a non-negative cost can only help, so the
bound does not depend on the wall's shape. -/
theorem gradient_nonpos_of_antitone_tail {J : ℕ} (Γ c : ℕ → ℝ) (lam : ℝ)
    (hmono : ∀ i j, i ≤ j → Γ j ≤ Γ i) (hc : ∀ j, 0 ≤ c j) (hJ : Γ J ≤ lam) :
    ∀ j, J ≤ j → Γ j - c j - lam ≤ 0 := by
  intro j hj
  have h1 : Γ j ≤ Γ J := hmono J j hj
  have h2 : 0 ≤ c j := hc j
  linarith

/-- **The composition: an antitone tail is charged exactly nothing.**  `gradient_nonpos_of_antitone_tail`
feeds `box_charge_eq_zero_of_nonpos` directly, so every padded row past `J` contributes zero to
the certificate's linear term — not a bounded amount, zero.

This is the fact the bottom-edge measurement reports (`padded charge 0.0, tail 0.0 [exactly zero
(g ≤ 0, lo = w = 0, Γ monotone)]`), and it is why `sum_charge_extend` rather than
`sum_charge_extend_le` is the operative form there. -/
theorem padded_tail_charge_eq_zero {J : ℕ} (Γ c lo hi w : ℕ → ℝ) (lam : ℝ)
    (hmono : ∀ i j, i ≤ j → Γ j ≤ Γ i) (hc : ∀ j, 0 ≤ c j) (hJ : Γ J ≤ lam)
    (hw : ∀ j, J ≤ j → w j = lo j) :
    ∀ j, J ≤ j →
      (if 0 ≤ Γ j - c j - lam then (Γ j - c j - lam) * (hi j - w j)
       else (Γ j - c j - lam) * (lo j - w j)) = 0 := by
  intro j hj
  exact box_charge_eq_zero_of_nonpos _ (lo j) (hi j) (w j)
    (gradient_nonpos_of_antitone_tail Γ c lam hmono hc hJ j hj) (hw j hj)

/-- **Antitonicity is load-bearing, not decoration.**  Without it a single row below `lam` says
nothing about the tail: take `Γ = (1, 2, 2, …)` and `lam = 1`.  Then `Γ 0 ≤ lam` holds and the
row-1 gradient is `+1`, so the tail is charged a positive amount and the certificate over the
padded index set is strictly larger than the one over the used coordinates.

Stated as a refutation rather than a remark because a hypothesis nobody has shown to bite is
indistinguishable from one that does not. -/
theorem antitone_hypothesis_is_necessary :
    ¬ ∀ (Γ : ℕ → ℝ) (lam : ℝ), Γ 0 ≤ lam → ∀ j, 0 ≤ j → Γ j - lam ≤ 0 := by
  intro h
  have := h (fun j => if j = 0 then 1 else 2) 1 (by norm_num) 1 (Nat.zero_le 1)
  norm_num at this

/-! ## Machine-checked bridge to `SearchCoercivity`

`qou-hok7` noted that `SupergradientCertificate` previously named `SearchCoercivity` only in prose.
The two theorems below compose `SearchCoercivity.sub_le_mul_of_antitone_step` and
`SearchCoercivity.sum_ghatBot_frame_bound` directly with `box_mul_sub_le` so the linearisation
steps of `SearchCoercivity` feed the box-maximised supergradient certificate in Lean. -/

/-- **Single-pair bridge (`SearchCoercivity.sub_le_mul_of_antitone_step` + `box_mul_sub_le`).**
For `e` with antitone downward steps `δ` (`e m - e (m + 1) = δ m`), any displacement `D : ℕ` confined
to `[lo, hi]` satisfies the supergradient box bound around any reference point `w`. -/
theorem antitone_step_box_bound {e δ : ℕ → ℝ}
    (hstep : ∀ m, e m - e (m + 1) = δ m) (hδ : Antitone δ)
    (a D : ℕ) (w lo hi : ℝ) (hlo : lo ≤ (D : ℝ)) (hhi : (D : ℝ) ≤ hi) :
    e a - e (a + D) ≤ w * δ a + (if 0 ≤ δ a then δ a * (hi - w) else δ a * (lo - w)) := by
  have hlin := QOU.BraidKnot.SearchCoercivity.sub_le_mul_of_antitone_step hstep hδ a D
  have hbox := box_mul_sub_le (δ a) w lo hi (D : ℝ) hlo hhi
  have hid : (D : ℝ) * δ a = w * δ a + δ a * ((D : ℝ) - w) := by ring
  linarith

/-- **Multi-row frame bridge (`SearchCoercivity.sum_ghatBot_frame_bound` + `box_mul_sub_le`).**
For any displacement profile `u : ι → ℕ` respecting the upper-row gaps (`u a ≤ b0 j - b0 a` for
`b0 a < b0 j`) and confined to the box `[lo, hi]`, the total frame-linearised excess bounded by
`SearchCoercivity.sum_ghatBot_frame_bound` is bounded above by the supergradient box certificate at
reference `w` with slope `SearchCoercivity.ghatBot e δ b0`. -/
theorem sup_ghatBot_frame_certificate {ι : Type*} [Fintype ι]
    {e δ fi : ℕ → ℝ}
    (hfi : ∀ m, fi (m + 1) - fi m = e (m + 1))
    (he : Antitone e)
    (hstep : ∀ m, e m - e (m + 1) = δ m)
    (hδ : Antitone δ)
    (b0 u : ι → ℕ) (w lo hi : ι → ℝ)
    (hu : ∀ a j, b0 a < b0 j → u a ≤ b0 j - b0 a)
    (hlo : ∀ a, lo a ≤ (u a : ℝ))
    (hhi : ∀ a, (u a : ℝ) ≤ hi a) :
    (∑ a : ι,
      ((fi (b0 a + u a) - fi (b0 a))
        + (∑ j ∈ Finset.univ.filter (fun j => b0 j < b0 a),
            (e (b0 a - b0 j) - e (b0 a - b0 j + u a)))
        + (∑ j ∈ Finset.univ.filter (fun j => b0 a < b0 j),
            (e (b0 j - b0 a) - e (b0 j - b0 a - u a)))))
      ≤ (∑ a : ι, w a * QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a)
        + ∑ a : ι,
            if 0 ≤ QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a then
              QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a * (hi a - w a)
            else
              QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a * (lo a - w a) := by
  have hframe := QOU.BraidKnot.SearchCoercivity.sum_ghatBot_frame_bound hfi he hstep hδ b0 u hu
  have hsum :
      (∑ a : ι, (u a : ℝ) * QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a)
        ≤ (∑ a : ι, w a * QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a)
          + ∑ a : ι,
              if 0 ≤ QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a then
                QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a * (hi a - w a)
              else
                QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a * (lo a - w a) := by
    rw [← Finset.sum_add_distrib]
    refine Finset.sum_le_sum fun a _ => ?_
    have hbox := box_mul_sub_le (QOU.BraidKnot.SearchCoercivity.ghatBot e δ b0 a)
      (w a) (lo a) (hi a) (u a : ℝ) (hlo a) (hhi a)
    linarith
  exact le_trans hframe hsum

end QOU.BraidKnot.SupergradientCertificate
