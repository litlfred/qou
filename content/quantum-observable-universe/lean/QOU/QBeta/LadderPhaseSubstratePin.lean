/-
Copyright (c) 2026 litlfred. All rights reserved.

# The ladder-phase exclusion is non-vacuous at the substrate pin

Bean `qou-q2oa`. The archimedean half of `QOU.QBeta.LadderPhaseFromWeights`,
split out per §7c: that file is generic `[Field F]` throughout, and this one
carries the single statement that needs an ordering.

## What it is for

`LadderPhaseFromWeights.no_weight_function_gives_phase` — no function of the
Wedderburn weight vector reproduces the ladder phase — carries the
non-degeneracy hypothesis `2z - h ≠ 2`. Without it the exclusion would be
vacuous: when `2z - h = 2` the phase IS bar-fixed and a constant function
would do.

Under convention D, `LadderPhaseFromWeights.zD_loopMean_sub_two_num` shows
that hypothesis is exactly the non-vanishing of

    q⁴ - 2q³ - 2q + 1.

This file proves that quartic is strictly negative on `[1, 2]`, an interval
containing the substrate pin `q₀ ≈ 1.1099785827513808` (proton / experimental
anchor, 2026-08-07 owner directive). So the exclusion's hypothesis genuinely
holds where the physics is evaluated, and the exclusion has content there.

Endpoints for orientation: the quartic is `-2` at `q = 1` and `-3` at `q = 2`;
`computations/qbeta/qbeta_ladder_phase_from_wedderburn_weights.py` reports
`-2.4371…` at `q₀`. The interval `[1, 2]` is deliberately generous — nothing
downstream needs it tight, and a wide interval is a stronger statement than a
neighbourhood of the pin.

No experimental Q_β is inverted here and no value is wired; this is a
statement about a polynomial.

Sorry-free.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import QOU.QBeta.LadderPhaseFromWeights

namespace QOU.QBeta

/-- **The quartic `q⁴ - 2q³ - 2q + 1` is strictly negative on `[1, 2]`**,
    an interval containing the substrate pin `q₀ ≈ 1.10998`.

    Combined with `zD_loopMean_sub_two_num`, this says `2·z_D - h ≠ 2` at the
    pin, so `no_weight_function_gives_phase` applies there and its exclusion
    is not vacuous. -/
theorem quartic_neg_on_Icc_one_two (q : ℝ) (h1 : 1 ≤ q) (h2 : q ≤ 2) :
    q ^ 4 - 2 * q ^ 3 - 2 * q + 1 < 0 := by
  nlinarith [sq_nonneg (q - 1), sq_nonneg (q - 2), sq_nonneg q,
    mul_nonneg (sub_nonneg.mpr h1) (sub_nonneg.mpr h2),
    sq_nonneg (q * q - 2)]

/-- **Hence the D-frame loop mean is never `2` on `[1, 2]`.**

    The exclusion hypothesis, delivered in the form
    `no_weight_function_gives_phase` consumes it. `q ≠ 0` and `q² + 1 ≠ 0`
    are automatic over `ℝ` on this interval and are discharged here rather
    than pushed onto the caller. -/
theorem zD_loopMean_ne_two_on_Icc (q : ℝ) (h1 : 1 ≤ q) (h2 : q ≤ 2) :
    2 * zD q - (q - q⁻¹) ≠ 2 := by
  have hq : q ≠ 0 := by positivity
  have hd : q ^ 2 + 1 ≠ 0 := by positivity
  intro hEq
  have hnum := zD_loopMean_sub_two_num q hq hd
  rw [hEq] at hnum
  simp only [sub_self, zero_mul] at hnum
  exact absurd hnum.symm (ne_of_lt (quartic_neg_on_Icc_one_two q h1 h2))

end QOU.QBeta
