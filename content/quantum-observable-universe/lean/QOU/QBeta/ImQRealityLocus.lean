/-
# `Q_β` real forces `Im q = 0` — on the substrate branch, and not off it

Bean `qou-c66b` (`conj:im-q-physical-role`), companion to the probe
`qbeta_imq_reality_locus_probe`. Sibling of
`QOU.QBeta.ImQCannotSupplyEllipticGenerator`, which closes the same
conjecture's phase-coordinate and non-Hermitian roles from the Kohno–Drinfeld
character; this file reaches the archimedean half of the same conclusion from a
**decay** observable instead.

## What is being formalised

`conj:im-q-physical-role` says the framework's observables are Im(q)-blind
because the mass formula projects through `|tr_M|`. That is true of the mass.
It is **not** true of `Q_β`, whose closed form carries the modulus on one
factor only:

    Q_β = m_e · |q² − 2q − 1| · (q + 1) / (2q³)          (E1, the printed form)
    Q_β = |Δ(net)| · E₀,  Δ(net) = h(h−2)/2,  E₀ = m_e/(q(q−1))   (E2, its derivation)

E1 is E2 simplified *using* `q` real and `q > 1` — only then is `(q²−1)`
positive and pullable out of the modulus — so extending E1 past that
hypothesis is not obviously the canonical complex extension. Both are
therefore carried, and the point of this file is that the answer does not
depend on which one is chosen.

Since `Q_β` is a measured Q-value in MeV, it is real, and `Im Q_β = 0` is one
real equation on the two real unknowns `(Re q, Im q)`. Writing `q = x + iy`,
the probe computes the imaginary parts exactly and their zero sets factor as

    E1:  y · (2x³ + 3x² + 2xy² − y²) = 0
    E2:  y · (2x − 1) = 0

Each has the trivial branch `y = 0` and one non-real branch. This file proves
that on the substrate branch — `Re q = q₀ ≈ 1.10998`, so certainly `1/2 < x` —
the non-real branch of **each** is empty, hence `y = 0`.

## Why the hypothesis `1/2 < x` is stated rather than dropped

Because it is not decoration. `im_e2_locus_is_nonempty` exhibits `x = 1/2`,
`y = 1` satisfying E2's equation with `y ≠ 0`, and `im_e1_locus_is_nonempty`
exhibits `x = -1`, `y = 1` for E1. So the conjecture's `Im q ≠ 0` really is
admissible somewhere in the complex `q`-plane; what the substrate branch
excludes is that it is admissible *there*. Bean `qou-c66b` asserted the
unqualified "requiring `Im Q_β = 0` forces `Im q = 0`" and that is too strong;
these two witnesses are the correction, and they are what stops the main
theorems from being a stronger claim than was measured.

## Scope

Scope-(b), citing the proved positivity below rather than a numerical
near-miss — but scoped to the **archimedean evaluation only**. `AGENTS.md`'s
fibre-vs-observable banner leaves `Im q` unconstrained at the fibre level and
nothing here touches that; the conjecture's chirality role (candidate (i)) is
likewise untouched. What is new is that `lusztig_q_0_imaginary_part_zero`'s
archimedean `Im q₀ = 0` now *follows* from an observable the framework already
carries, rather than being assumed.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

namespace QOU.QBeta

/-- **E2's non-real branch is empty for `1/2 < x`.** `Im[1/(q(q−1))]` has
numerator `−y(2x−1)` (up to the positive denominator `|q|²·|q−1|²`), and
`2x − 1 > 0` on the substrate branch. -/
theorem e2_branch_pos {x : ℝ} (hx : 1 / 2 < x) : 0 < 2 * x - 1 := by linarith

/-- **E1's non-real branch is empty for `1/2 < x`.** `Im[(q+1)/(2q³)]` has
numerator `−y(2x³ + 3x² + 2xy² − y²)`, and that cubic-in-`x` factor regroups as
`2x³ + 3x² + y²(2x − 1)`: a sum of three terms each positive once `x > 1/2`.
Note this holds for **every** `y`, which is what makes the branch empty rather
than merely small. -/
theorem e1_branch_pos {x y : ℝ} (hx : 1 / 2 < x) :
    0 < 2 * x ^ 3 + 3 * x ^ 2 + 2 * x * y ^ 2 - y ^ 2 := by
  have hx0 : 0 < x := by linarith
  have h1 : 0 < 2 * x - 1 := by linarith
  have hy : 0 ≤ y ^ 2 := sq_nonneg y
  nlinarith [mul_nonneg (le_of_lt h1) hy, mul_pos (mul_pos hx0 hx0) hx0,
    mul_pos hx0 hx0]

/-- **E2: `Im Q_β = 0 ↔ Im q = 0` on the substrate branch.** -/
theorem im_qbeta_zero_iff_e2 {x y : ℝ} (hx : 1 / 2 < x) :
    y * (2 * x - 1) = 0 ↔ y = 0 := by
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h | h
    · exact h
    · exact absurd h (ne_of_gt (e2_branch_pos hx))
  · rintro rfl; simp

/-- **E1: `Im Q_β = 0 ↔ Im q = 0` on the substrate branch.** -/
theorem im_qbeta_zero_iff_e1 {x y : ℝ} (hx : 1 / 2 < x) :
    y * (2 * x ^ 3 + 3 * x ^ 2 + 2 * x * y ^ 2 - y ^ 2) = 0 ↔ y = 0 := by
  constructor
  · intro h
    rcases mul_eq_zero.mp h with h | h
    · exact h
    · exact absurd h (ne_of_gt (e1_branch_pos hx))
  · rintro rfl; simp

/-- **The conclusion does not depend on which complex extension is taken.**
Stated as a disjunction on purpose: it is not that one needs *both* readings to
conclude, it is that *whichever* one is canonical the answer is the same. That
is what lets the result stand while `qou-c66b`'s question of which extension is
canonical remains open. -/
theorem im_q_zero_under_either_extension {x y : ℝ} (hx : 1 / 2 < x)
    (h : y * (2 * x ^ 3 + 3 * x ^ 2 + 2 * x * y ^ 2 - y ^ 2) = 0 ∨
         y * (2 * x - 1) = 0) : y = 0 := by
  rcases h with h | h
  · exact (im_qbeta_zero_iff_e1 hx).mp h
  · exact (im_qbeta_zero_iff_e2 hx).mp h

/-- **The `1/2 < x` hypothesis is load-bearing for E2**: at `x = 1/2` the
equation holds with `y = 1 ≠ 0`, so a real `Q_β` at complex `q` is admissible
off the substrate branch. -/
theorem im_e2_locus_is_nonempty :
    ∃ x y : ℝ, y ≠ 0 ∧ y * (2 * x - 1) = 0 :=
  ⟨1 / 2, 1, one_ne_zero, by norm_num⟩

/-- **The `1/2 < x` hypothesis is load-bearing for E1** too. The branch solves
to `y² = −x²(2x+3)/(2x−1)`, positive exactly on `−3/2 < x < 1/2`; at `x = −1/2`
that gives `y² = 1/4`, so `(x, y) = (−1/2, 1/2)` sits on it with `y ≠ 0`. Hence
neither theorem above may be restated without its hypothesis.

The first draft of this witness offered `(−1, 1)`, where the factor is `−2`, not
`0`. It is recorded because the failure mode is the point: an existence claim
whose witness does not satisfy the equation would have passed a reader and been
caught only by the kernel. -/
theorem im_e1_locus_is_nonempty :
    ∃ x y : ℝ, y ≠ 0 ∧ y * (2 * x ^ 3 + 3 * x ^ 2 + 2 * x * y ^ 2 - y ^ 2) = 0 :=
  ⟨-1 / 2, 1 / 2, by norm_num, by norm_num⟩

/-- **The two non-real branches are disjoint**, so the extensions disagree
about where imaginarity is admissible *everywhere except* on the substrate.
At E2's locus `x = 1/2` the E1 factor is `2(1/8) + 3(1/4) + y²(0) = 1`, never
zero — so no `q` off the real axis makes both readings real at once. -/
theorem branches_disjoint (y : ℝ) :
    2 * (1 / 2 : ℝ) ^ 3 + 3 * (1 / 2 : ℝ) ^ 2 + 2 * (1 / 2 : ℝ) * y ^ 2 - y ^ 2 = 1 := by
  norm_num

/-- **Candidate (ii)'s whole admissible set sits in the half-plane, not just
`q₀`.** The conjecture posits that CAL-2 alone leaves an Apollonius circle of
admissible complex `q`, with `Im q` as "the arc coordinate parametrizing the
other admissible q values". Reading CAL-2 with a modulus — which is what
produces a circle at all — gives `|q − 1| = √k·|q|` with
`k = Vol(4₁)/(m_μ/m_e)`, hence centre `1/(1−k)` and radius `√k/(1−k)`. The
probe derives **centre 1.0099145, radius 0.1000641** from the live CODATA-2022
ratio, reproducing the conjecture's own stated `≈1.010` / `≈0.100`.

Any circle with centre above `9/10` and radius below `2/5` lies strictly right
of `1/2`, with room to spare: the measured pair clears both bounds by an order
of magnitude. So `im_qbeta_zero_iff_e1` and `im_qbeta_zero_iff_e2` apply at
**every point of the arc**, and `Im Q_β = 0` leaves only its two real
intersections. That is candidate (ii)'s test answered on its entire admissible
set rather than at one point. -/
theorem cal2_circle_lies_in_substrate_half_plane {c r x y : ℝ}
    (hr0 : 0 ≤ r) (hc : (9 : ℝ) / 10 < c) (hr : r < (2 : ℝ) / 5)
    (hon : (x - c) ^ 2 + y ^ 2 = r ^ 2) : 1 / 2 < x := by
  nlinarith [sq_nonneg y, sq_nonneg (x - c), sq_nonneg (c - x - r)]

end QOU.QBeta
