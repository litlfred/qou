import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import QOU.Archimedean.BringColorTubeGeomTruncation
import QOU.Archimedean.LinkingWeightSubstrateBounds

/-!
# Bring color-tube truncation error AT THE SUBSTRATE (PROVED)

Per user "try to prove it" — combines the closed-form geom-series
truncation identity from
[`BringColorTubeGeomTruncation.lean`](BringColorTubeGeomTruncation.lean)
with the substrate-q₀ rational bounds from
[`LinkingWeightSubstrateBounds.lean`](LinkingWeightSubstrateBounds.lean)
to PROVE a specific numerical truncation-error bound at q₀.

## The theorem

For the substrate q₀ ≈ 1.110 and the degree-8 truncation:

  `|bringColorTube q_0 − bringTrunc q_0 8| < 1/10`

i.e. the truncation error is bounded by 0.1 (10 % of the function
value). This is a coarse bound — the actual error at q₀ ≈ 0.024 ≈
2.4 % — but it is provable via `norm_num` on rational literals
without analytic-function infrastructure.

## Method

1. Apply `bringColorTube_truncation_abs_bound` (PROVED in
   `BringColorTubeGeomTruncation.lean`) to get the closed-form
   equality

     `|bringColorTube q_0 − bringTrunc q_0 8|
        = (heckeH q_0 · q_0^{10})^9 / (1 − heckeH q_0 · q_0^{10})`

2. Bound the RHS numerically: at q_0 = 1109978596/10⁹, the value
   z := h·q^{10} ≈ 0.594 is in (0, 1); z^9 ≈ 0.0096; (1-z) ≈
   0.406; ratio ≈ 0.024.

3. `norm_num` closes `0.024 < 1/10`.

## Status

PROVED sorry-free. Closes a SPECIFIC NUMERICAL truncation-error
bound at the substrate, complementing the abstract bound in
[`BringColorTubeGeomTruncation.lean`](BringColorTubeGeomTruncation.lean).
-/

namespace QOU.Archimedean

open Real

/-! ## §1  Substrate-specific premise verifications

The geom-series truncation identity requires `z := heckeH q · q^{10}`
to satisfy `z > 0` and `z < 1` for absolute-value bound to apply.
Both follow from `q_0_substrate > 1`. -/

/-- At q_0_substrate, `heckeH q_0 = q_0 − q_0⁻¹` is positive (since
    q_0 > 1). -/
theorem heckeH_at_q_0_pos : heckeH q_0_substrate > 0 := by
  unfold heckeH q_0_substrate
  norm_num

/-- `heckeH q_0 · q_0^{10} > 0`. -/
theorem heckeH_q10_at_q_0_pos :
    heckeH q_0_substrate * q_0_substrate ^ 10 > 0 := by
  have h1 : heckeH q_0_substrate > 0 := heckeH_at_q_0_pos
  have h2 : q_0_substrate ^ 10 > 0 := by
    have : q_0_substrate > 0 := by
      have := q_0_substrate_gt_one; linarith
    positivity
  positivity

/-- `heckeH q_0 · q_0^{10} < 1` (substrate value ≈ 0.594 < 1). -/
theorem heckeH_q10_at_q_0_lt_one :
    heckeH q_0_substrate * q_0_substrate ^ 10 < 1 := by
  unfold heckeH q_0_substrate
  norm_num

/-! ## §2  Numerical truncation bound at q_0 (PROVED) -/

/-- The geom-series tail `bringTail q_0 8` lies in (0, 1/10).

    Numerical value: `(0.594)^9 / (1 - 0.594) ≈ 0.0096 / 0.406 ≈ 0.024`.

    PROVED via `norm_num` on the rational q₀ literal.

    This is a COARSE bound — the actual tail is ≈ 0.024 — but
    sufficient to demonstrate that the truncation is well-defined
    and bounded. -/
theorem bringTail_at_q_0_lt_one_tenth :
    bringTail q_0_substrate 8 < 1 / 10 := by
  unfold bringTail heckeH q_0_substrate
  -- Numerically: ((1.110-0.901) * 1.110^10)^9 / (1 - (1.110-0.901)*1.110^10)
  --         = (0.209 * 2.840)^9 / (1 - 0.594)
  --         = 0.594^9 / 0.406
  --         ≈ 0.0096 / 0.406
  --         ≈ 0.024
  -- 0.024 < 0.1 = 1/10 ✓
  --
  -- Note: norm_num needs to evaluate (1109978596/10^9 - 10^9/1109978596) * (1109978596/10^9)^10
  -- raised to the 9th power.  This is heavy but tractable.
  have hden_pos :
      (1 : ℝ) - (1109978596 / 1000000000 - 1000000000 / 1109978596)
                * (1109978596 / 1000000000) ^ 10 > 0 := by norm_num
  rw [div_lt_iff hden_pos]
  norm_num

/-- `bringTail q_0 8 > 0` (truncation tail is strictly positive
    when the geom-series argument z ∈ (0, 1)). -/
theorem bringTail_at_q_0_pos : bringTail q_0_substrate 8 > 0 :=
  bringTail_pos q_0_substrate q_0_substrate_ne_zero
    heckeH_q10_at_q_0_pos heckeH_q10_at_q_0_lt_one 8

/-- **Main theorem: truncation-error bound at q_0** (PROVED).

    The degree-8 geom-series truncation of `bringColorTube q_0` has
    absolute error strictly less than 0.1:

      `|bringColorTube q_0 − bringTrunc q_0 8| < 1/10`.

    Combines:
    - `bringColorTube_truncation_abs_bound`: closed-form equality
      with bringTail
    - `bringTail_at_q_0_lt_one_tenth`: numerical bound on the tail -/
theorem bringColorTube_truncation_at_q_0_bound :
    |bringColorTube q_0_substrate - bringTrunc q_0_substrate 8| < 1 / 10 := by
  rw [bringColorTube_truncation_abs_bound q_0_substrate q_0_substrate_ne_zero
        heckeH_q10_at_q_0_pos heckeH_q10_at_q_0_lt_one 8]
  -- The bound now reads:
  --   (heckeH q_0 · q_0^10)^9 / (1 - heckeH q_0 · q_0^10) < 1/10
  -- which is exactly `bringTail q_0 8 < 1/10`.
  have h := bringTail_at_q_0_lt_one_tenth
  unfold bringTail at h
  exact h

/-! ## §3  Tighter substrate-specific bound

A tighter bound — `< 1/30` — follows directly from `norm_num` with
no additional infrastructure. The actual numerical value is ≈ 0.024
= 1/41.7, so we can pick any denominator < 41 for a provable bound. -/

/-- The tail at q_0 is < 1/30 (tightening of the previous theorem). -/
theorem bringTail_at_q_0_lt_one_thirtieth :
    bringTail q_0_substrate 8 < 1 / 30 := by
  unfold bringTail heckeH q_0_substrate
  have hden_pos :
      (1 : ℝ) - (1109978596 / 1000000000 - 1000000000 / 1109978596)
                * (1109978596 / 1000000000) ^ 10 > 0 := by norm_num
  rw [div_lt_iff hden_pos]
  norm_num

/-- **Sharper truncation bound at q_0 (PROVED)**: error < 1/30 ≈ 0.033. -/
theorem bringColorTube_truncation_at_q_0_sharper :
    |bringColorTube q_0_substrate - bringTrunc q_0_substrate 8| < 1 / 30 := by
  rw [bringColorTube_truncation_abs_bound q_0_substrate q_0_substrate_ne_zero
        heckeH_q10_at_q_0_pos heckeH_q10_at_q_0_lt_one 8]
  have h := bringTail_at_q_0_lt_one_thirtieth
  unfold bringTail at h
  exact h

/-! ## §4  Numerical-corroboration table

| n  | bringTrunc q_0 n (approx) | bringTail q_0 n (approx) |
|----|---------------------------|--------------------------|
| 0  | 1                         | 1.460  |
| 1  | 1.594                     | 0.866  |
| 2  | 1.947                     | 0.513  |
| 4  | 2.272                     | 0.188  |
| 6  | 2.385                     | 0.0746 |
| 8  | 2.436                     | 0.0241 |
| 12 | 2.456                     | 0.00388 |

At n=8, the truncation error is ≈ 0.0241, well within the (1/30 ≈
0.0333) bound proved above. The actual error decays as
z^{n+1}/(1-z) with z ≈ 0.594.

## §5  Status

PROVED sorry-free:
  ✓ heckeH_at_q_0_pos
  ✓ heckeH_q10_at_q_0_pos, heckeH_q10_at_q_0_lt_one
  ✓ bringTail_at_q_0_lt_one_tenth, bringTail_at_q_0_lt_one_thirtieth
  ✓ bringColorTube_truncation_at_q_0_bound (< 1/10)
  ✓ bringColorTube_truncation_at_q_0_sharper (< 1/30)
  ✓ bringTail_at_q_0_pos

This file CLOSES a concrete substrate-specific instance of the
Taylor-form truncation error theorem in
[`TruncationErrorBound.lean`](TruncationErrorBound.lean) which
remains sorry'd at the abstract-q-interval level (gated on
Mathlib's Taylor.Lagrange).

The substrate-specific bound is achievable WITHOUT Mathlib's
analytic-function infrastructure because we use:
  1. The PROVED closed-form geom-series identity from
     `BringColorTubeGeomTruncation.lean`
  2. `norm_num` on the rational q₀ literal.
-/

end QOU.Archimedean
