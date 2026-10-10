/-
# The colour curve is bar-INVARIANT; its 7.878 % defect is a BRANCH defect

Beans `qou-ndt5` and `qou-fi93`; probe
`computations/barparity/colour_curve_bar_vs_branch_probe.py`.

`qou-ndt5` settles the algebra: the colour-curve modulus is `z = s − 1/s` with
`s² = q`, `r` is a polynomial in `z`, and `s ↦ −1/s` is the unique lift of the
substrate bar `q ↦ 1/q` preserving the degeneration locus `s² + s − 1`.
`qou-fi93` measures a 7.878 % asymmetry as `r(z) − r(−z)` and reads it as a
candidate matter/antimatter defect.

**Two different involutions are in play.**

    the BAR      `q ↦ 1/q`, lifted as `s ↦ −1/s`   — FIXES `z`
    the BRANCH   `s ↦ −s`   (same `q`, other root) — NEGATES `z`

Since `r` is a polynomial in `z`, it is *exactly* bar-invariant, and
`r(z) − r(−z)` is a difference between the two square roots of one and the
same `q`.

Matter and antimatter are related by the bar in this framework
(`prop:antiparticle-crossing-reversal` sends `q ↔ q⁻¹`), so a bar-invariant
quantity cannot distinguish them — which is a second, structural route to
`qou-fi93`'s exclusion, independent of its survey of the counting measures.

This says nothing about whether the negative branch is physically observable;
`qou-ndt5` records the owner's standing ruling that it stays open. It says
only which involution the defect belongs to.

Generic over a `Field`; no anchor, no `ℝ`, per §7c.

-- Ref: [manuscript] beans `qou-ndt5` / `qou-fi93`,
--      `prop:antiparticle-crossing-reversal`
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

namespace QOU.BringsSurface.ColourCurveBarVsBranch

variable {K : Type*} [Field K]

/-- The colour-curve modulus `z = s − 1/s`, with `s² = q`. -/
def zOf (s : K) : K := s - s⁻¹

/-- The substrate bar `q ↦ 1/q`, lifted to `s`.  `qou-ndt5`: this is the
unique lift preserving the degeneration locus `s² + s − 1`. -/
def barLift (s : K) : K := -s⁻¹

/-- The branch swap: the *other* square root of the same `q`. -/
def branchSwap (s : K) : K := -s

/-- `barLift` really does invert `q = s²`. -/
theorem barLift_sq (s : K) (hs : s ≠ 0) : (barLift s) ^ 2 = (s ^ 2)⁻¹ := by
  unfold barLift
  field_simp

/-- `branchSwap` fixes `q = s²` — it is the other root of the SAME `q`. -/
theorem branchSwap_sq (s : K) : (branchSwap s) ^ 2 = s ^ 2 := by
  unfold branchSwap
  ring

/-- **The bar FIXES `z`.**  This is the load-bearing fact.

No `s ≠ 0` hypothesis is needed: in a field `0⁻¹ = 0`, so both sides are `0`
at `s = 0` and the identity is unconditional.  Stated that way deliberately —
carrying a hypothesis the proof does not use would invite a reader to think
the bar-invariance is conditional on something. -/
theorem zOf_barLift (s : K) : zOf (barLift s) = zOf s := by
  unfold zOf barLift
  rw [inv_neg, inv_inv]
  ring

/-- **The branch NEGATES `z`.** -/
theorem zOf_branchSwap (s : K) : zOf (branchSwap s) = -zOf s := by
  unfold zOf branchSwap
  rw [inv_neg]
  ring

/-- Any function of `z` is therefore bar-invariant — stated for an arbitrary
`f`, so it covers `r` and every other quantity built from the modulus. -/
theorem bar_invariant_of_zOf (f : K → K) (s : K) :
    f (zOf (barLift s)) = f (zOf s) := by
  rw [zOf_barLift s]

/-- The colour curve `r(z) = (5/27)(4z³ + 3z² + 3z + 4)` (`qou-ndt5`; the same
`q_W(z)` as `t-duality-elliptic.md`). -/
def colourCurve (z : K) : K := (5 / 27) * (4 * z ^ 3 + 3 * z ^ 2 + 3 * z + 4)

/-- **`r` is exactly bar-invariant.** -/
theorem colourCurve_bar_invariant (s : K) :
    colourCurve (zOf (barLift s)) = colourCurve (zOf s) :=
  bar_invariant_of_zOf colourCurve s

/-- **The branch defect is `qou-fi93`'s `(10/27)·z·(4z² + 3)`** — so that
quantity is a difference between the two square roots of one `q`, not between
`q` and `1/q`. -/
theorem colourCurve_branch_defect (z : K) :
    colourCurve z - colourCurve (-z) = (10 / 27) * z * (4 * z ^ 2 + 3) := by
  unfold colourCurve
  ring

end QOU.BringsSurface.ColourCurveBarVsBranch
