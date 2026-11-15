/-
# Two lifts of the bar to √q, and they give the same object opposite parity

Beans `qou-ndt5` (is the negative branch `s = −√q` observable?) and `qou-fi93`.
Probe `computations/barparity/bar_lift_ambiguity_probe.py`.

## The collision, read off two existing corpus definitions

Two arcs define the *same expression* and do not cite each other:

* `QOU/Braiding/SkeinNormalisation.lean:74` — `sJ (u : K) : K := u - u⁻¹`
* `QOU/BringsSurface/ColourCurveBarVsBranch.lean:45` — `zOf (s : K) : K := s - s⁻¹`

`sJ` is the bar-odd generator of the half-power skein normalisation; `zOf` is
the colour curve's spacetime modulus.  They are byte-identical.

The two arcs then lift the substrate bar `q ↦ q⁻¹` to the square root
**differently**, and both lifts are legitimate — each squares to `q⁻¹`:

| arc | lift | this file |
|---|---|---|
| `SkeinNormalisation` (`sJ_bar_antiinvariant`) | `u ↦ u⁻¹` | `invLift` |
| `ColourCurveBarVsBranch` (`barLift`) | `u ↦ −u⁻¹` | `ndt5Lift` |

They differ by exactly the branch swap `u ↦ −u` (`lifts_differ_by_branch`) —
the very map `qou-ndt5` asks about.

## The consequence, which is not cosmetic

The same object has **opposite bar parity** under the two lifts:

* `z_invLift_odd`  — under `u ↦ u⁻¹`, `z ↦ −z`:  **bar-ODD**
* `z_ndt5Lift_even` — under `u ↦ −u⁻¹`, `z ↦ z`: **bar-EVEN**

and therefore so does the colour curve `r(z)`:

* `colourCurve27_ndt5Lift_invariant` — defect **exactly zero**
* `colourCurve27_invLift_defect` — defect `10·z·(4z² + 3)`, which is the
  *same formula* `qou-fi93` and `qou-ndt5` record as the "bar defect"
  (7.878 % at `q₀`).

So **"the bar parity of `z`" is not determined by the bar on `q`**
(`z_parity_not_determined`).  Fixing it requires choosing a lift, and the
corpus currently chooses differently in two places.

## What this does to two claims already in the corpus, one of them mine

Both were stated unconditionally and are **conditional on the lift**:

1. *"The name `bar_defect` is a misnomer; it is a branch defect"*
   (`qou-ndt5`, 2026-09-13).  True under `ndt5Lift`.  Under `invLift` the bar
   itself negates `z` and the original name was right.
2. *"The colour curve is the wrong parity to carry a matter/antimatter
   asymmetry — structurally"* (`qou-ndt5` consequence 3, a second route to
   `qou-fi93`'s exclusion).  True under `ndt5Lift`.  Under `invLift` the
   colour curve **does** have bar-odd content.

## Why `ndt5Lift` was chosen, and what that choice actually buys

`qou-ndt5` selects `s ↦ −s⁻¹` as *"the unique lift of `q ↦ 1/q` preserving the
degeneration locus `s² + s − 1`"*, and that uniqueness is correct — but it is
uniqueness **subject to preserving that polynomial**, not uniqueness among
lifts of the bar.  `invLift` is an equally valid lift that preserves something
else (the skein normalisation's parity grading).  So the corpus has two
defensible conventions and no ruling between them.

This file does not choose.  It makes the choice visible and prices it.

Generic over a `Field`; no anchor, no `ℝ`, per §7c.  `colourCurve27` carries
the factor 27 rather than dividing by it, so nothing here needs `27 ≠ 0`.

-- Ref: [leitner2026] beans `qou-ndt5` / `qou-fi93`;
--      `QOU/Braiding/SkeinNormalisation.lean`,
--      `QOU/BringsSurface/ColourCurveBarVsBranch.lean`
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination

namespace QOU.BringsSurface.BarLiftAmbiguity

variable {K : Type*} [Field K]

/-- The shared object.  `= SkeinNormalisation.sJ = ColourCurveBarVsBranch.zOf`. -/
def z (u : K) : K := u - u⁻¹

/-- The skein arc's lift of the bar: `u ↦ u⁻¹`. -/
def invLift (u : K) : K := u⁻¹

/-- The colour-curve arc's lift (`ColourCurveBarVsBranch.barLift`): `u ↦ −u⁻¹`. -/
def ndt5Lift (u : K) : K := -u⁻¹

/-- The branch swap: the other square root of the same `q`. -/
def branchSwap (u : K) : K := -u

/-! ### Both lifts are lifts -/

theorem invLift_sq (u : K) : (invLift u) ^ 2 = (u ^ 2)⁻¹ := by
  simp only [invLift, inv_pow]

theorem ndt5Lift_sq (u : K) : (ndt5Lift u) ^ 2 = (u ^ 2)⁻¹ := by
  simp only [ndt5Lift, neg_sq, inv_pow]

/-- **The two lifts differ by exactly the branch swap** — the map `qou-ndt5`
asks about.  So the ambiguity in the lift *is* the branch ambiguity. -/
theorem lifts_differ_by_branch (u : K) : ndt5Lift u = branchSwap (invLift u) := by
  simp only [ndt5Lift, branchSwap, invLift]

/-! ### The same object, opposite parity -/

/-- Under the skein lift `u ↦ u⁻¹`, the shared object is **bar-ODD**. -/
theorem z_invLift_odd (u : K) : z (invLift u) = -z u := by
  simp only [z, invLift, inv_inv]
  ring

/-- Under the colour-curve lift `u ↦ −u⁻¹`, the same object is **bar-EVEN**. -/
theorem z_ndt5Lift_even (u : K) : z (ndt5Lift u) = z u := by
  simp only [z, ndt5Lift, inv_neg, inv_inv]
  ring

/-- **The parity of `z` is not determined by the bar on `q`.**  Both lifts
square to `q⁻¹`, and they disagree wherever `z u ≠ 0`. -/
theorem z_parity_not_determined (h2 : (2 : K) ≠ 0) {u : K} (hz : z u ≠ 0) :
    z (invLift u) ≠ z (ndt5Lift u) := by
  rw [z_invLift_odd, z_ndt5Lift_even]
  intro h
  have : (2 : K) * z u = 0 := by linear_combination -h
  rcases mul_eq_zero.mp this with h' | h'
  · exact h2 h'
  · exact hz h'

/-! ### The colour curve inherits it -/

/-- The colour curve, carrying its 27 rather than dividing by it, so that
nothing below needs `27 ≠ 0`.  `27·r(x)` in the corpus's normalisation. -/
def colourCurve27 (x : K) : K := 5 * (4 * x ^ 3 + 3 * x ^ 2 + 3 * x + 4)

/-- Under the colour-curve arc's lift, `r` is **exactly** bar-invariant —
zero defect, not a small one.  (This is `ColourCurveBarVsBranch`'s result,
restated here so the two lifts stand side by side.) -/
theorem colourCurve27_ndt5Lift_invariant (u : K) :
    colourCurve27 (z (ndt5Lift u)) = colourCurve27 (z u) := by
  rw [z_ndt5Lift_even]

/-- Under the skein arc's lift, `r` has defect `10·z·(4z² + 3)` — the *same*
formula `qou-fi93` and `qou-ndt5` record as the "bar defect". -/
theorem colourCurve27_invLift_defect (u : K) :
    colourCurve27 (z u) - colourCurve27 (z (invLift u))
      = 10 * z u * (4 * (z u) ^ 2 + 3) := by
  rw [z_invLift_odd]
  simp only [colourCurve27]
  ring

/-- The defect vanishes exactly where the shared object does, so the two lifts
agree only on the fixed locus `z = 0` (`u² = 1`). -/
theorem invLift_defect_ne_zero (h2 : (2 : K) ≠ 0) (h5 : (5 : K) ≠ 0)
    {u : K} (hz : z u ≠ 0) (h3 : 4 * (z u) ^ 2 + 3 ≠ 0) :
    colourCurve27 (z u) - colourCurve27 (z (invLift u)) ≠ 0 := by
  rw [colourCurve27_invLift_defect]
  have h10 : (10 : K) ≠ 0 := by
    have h : (10 : K) = 2 * 5 := by norm_num
    rw [h]
    exact mul_ne_zero h2 h5
  exact mul_ne_zero (mul_ne_zero h10 hz) h3

end QOU.BringsSurface.BarLiftAmbiguity
