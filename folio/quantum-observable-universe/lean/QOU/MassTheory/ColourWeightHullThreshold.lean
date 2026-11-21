/-
ColourWeightHullThreshold.lean — the p–n colour weight is inside the convex
hull exactly when |δ| ≤ 2, and a target above the ceiling forces it outside.

CONTEXT.  The atom word's proton–neutron letter is the Hecke element
`σ − h(½ − δ/4)·1` with `δ = flavor_split_leading(q)`
(`conj:flavor-split-substrate-mass`).  Using `σ⁻¹ = σ − h` it is the AFFINE
combination

    (½ + δ/4)·σ  +  (½ − δ/4)·σ⁻¹,

whose coefficients sum to 1 for every δ.  `convex_comb_le_bound`
(`BranchConvexityBound.lean`) bounds such a combination by the branch maximum
ONLY when the coefficients are non-negative, and `bound_fails_without_nonneg`
there shows that hypothesis is load-bearing.  So the whole magnitude question
at this letter reduces to a threshold on δ, and that threshold is what this
file establishes.

WHAT IS PROVED.
  * `colourWeights_sum_one`  — the two weights sum to 1, for ANY δ.  This is
    why the letter is affine rather than arbitrary: it is `σ⁻¹ = σ − h` in
    coordinates, not an assumption.
  * `colourWeights_nonneg_iff` — both weights are non-negative **iff** |δ| ≤ 2.
    An iff, so it says both that the substrate value is admissible and what
    would have to change for it not to be.
  * `affine_le_max_of_nonneg` — inside the hull, the two-point bound.
  * `target_above_max_forces_outside_hull` — the converse that carries the
    physics: if an affine combination attains a value strictly above both
    endpoints, its weight is outside [0,1].  Reaching a target the endpoints
    do not reach is not a matter of choosing δ well; no admissible δ does it.
  * `hull_bound_fails_beyond_threshold` — non-vacuity: an explicit δ = 4 with
    a combination exceeding both endpoints, so the threshold is sharp rather
    than a sufficient condition stated loosely.

MEASURED COMPANION.  `computations/meson/delta_freedom_buys_no_magnitude_probe.py`
supplies the numbers this file's hypotheses are about: δ(q₀) = 0.001375710807,
weights 0.50034 / 0.49966 (inside), and the target `√B_AME` requiring
δ = 15.493 — 11262× the substrate value and far past the 2 proved here.

`ℝ` is genuine (§7c): every statement is an inequality between real
magnitudes.  Nothing here is q-symbolic and nothing needs to be.

@module QOU.MassTheory.ColourWeightHullThreshold
-/

import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

set_option autoImplicit false

namespace QOU.MassTheory

/-- Weight on `σ` in the colour-weighted p–n letter. -/
noncomputable def wPos (d : ℝ) : ℝ := 1 / 2 + d / 4

/-- Weight on `σ⁻¹` in the colour-weighted p–n letter. -/
noncomputable def wNeg (d : ℝ) : ℝ := 1 / 2 - d / 4

/-- The letter is an AFFINE combination for every `δ` — a consequence of
`σ⁻¹ = σ − h`, not an assumption about the colour weighting. -/
theorem colourWeights_sum_one (d : ℝ) : wPos d + wNeg d = 1 := by
  unfold wPos wNeg; ring

/-- **The threshold.**  Both weights are non-negative exactly when `|δ| ≤ 2`.
Below it the letter lies in the convex hull of `{σ, σ⁻¹}` and
`convex_comb_le_bound` applies; above it one weight is negative and the bound
has no force. -/
theorem colourWeights_nonneg_iff (d : ℝ) :
    (0 ≤ wPos d ∧ 0 ≤ wNeg d) ↔ |d| ≤ 2 := by
  unfold wPos wNeg
  constructor
  · rintro ⟨h1, h2⟩
    rw [abs_le]
    constructor <;> linarith
  · intro h
    rw [abs_le] at h
    exact ⟨by linarith [h.1], by linarith [h.2]⟩

/-- Inside the hull, an affine combination of two values is at most their
maximum.  The two-point case of `convex_comb_le_bound`. -/
theorem affine_le_max_of_nonneg {w x y M : ℝ} (hw : 0 ≤ w) (hw' : w ≤ 1)
    (hx : x ≤ M) (hy : y ≤ M) : w * x + (1 - w) * y ≤ M := by
  nlinarith [mul_nonneg hw (sub_nonneg.mpr hx), mul_nonneg (sub_nonneg.mpr hw') (sub_nonneg.mpr hy)]

/-- **The converse that carries the physics.**  If an affine combination
attains a value strictly greater than both endpoints, its weight lies outside
`[0,1]`.  So a target above the branch ceiling cannot be reached by any
admissible colour weight — it is not a matter of choosing `δ` well. -/
theorem target_above_max_forces_outside_hull {w x y T : ℝ}
    (hx : x < T) (hy : y < T) (heq : w * x + (1 - w) * y = T) :
    w < 0 ∨ 1 < w := by
  by_contra hcon
  push_neg at hcon
  obtain ⟨hw, hw'⟩ := hcon
  have : w * x + (1 - w) * y ≤ max x y := by
    exact affine_le_max_of_nonneg hw hw' (le_max_left x y) (le_max_right x y)
  rw [heq] at this
  rcases max_cases x y with ⟨he, _⟩ | ⟨he, _⟩ <;> rw [he] at this <;> linarith

/-- Non-vacuity: the threshold is sharp.  At `δ = 4` the weight on `σ⁻¹` is
`−1/2`, and the combination `(3/2)·1 + (−1/2)·0 = 3/2` exceeds both endpoints —
so beyond `|δ| = 2` the bound genuinely fails rather than merely losing its
proof. -/
theorem hull_bound_fails_beyond_threshold :
    ¬ (0 ≤ wNeg 4) ∧ wPos 4 * 1 + wNeg 4 * 0 > (1 : ℝ) := by
  refine ⟨by norm_num [wNeg], by norm_num [wPos, wNeg]⟩

end QOU.MassTheory
