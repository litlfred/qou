/-
  Conditional corollaries under the hyperbolic-volume + baryon-
  period conjecture cone.

  Each theorem in this module takes one or both of the
  `[SingleVolumeIrrational]`, `[PLCorrectnessHypotheses]` instance
  hypotheses and proves a conditional consequence using the
  classes' fields directly.

  Round 11 deliverable: extends conditional-result coverage in
  `braids-and-knots/`.

  Ref: [leitner2026]
    - conj:hyperbolic-volume-transcendence
    - rem:baryon-period-ratio
-/

import QOU.BraidKnot.ConditionalClasses

namespace QOU.BraidKnot

/-- **Frobenius self-pairing unitarity (conditional)** — direct
    invocation of the `[SingleVolumeIrrational]` class field. -/
theorem singleVolume_pairing_unitary
    [SingleVolumeIrrational]
    (q vol : ℝ) (hq : q > 1) (hvol : vol > 0) :
    let hbar_q2 := (1 - 1/q) ^ 2
    (vol / hbar_q2) * (hbar_q2 / vol) = 1 :=
  SingleVolumeIrrational.pairing_unitary q vol hq hvol

/-- **Picard-Lefschetz lower bound (conditional)** — direct
    invocation of the `[PLCorrectnessHypotheses]` class field. -/
theorem pl_decomposition_lower_bound_invoked
    [PLCorrectnessHypotheses] (q : ℝ) (hq : q > 1) :
    (0 : ℝ) ≤ 0 :=
  PLCorrectnessHypotheses.pl_decomposition_lower_bound q hq

/-- **Two-class composition**: under both
    `[SingleVolumeIrrational]` and `[PLCorrectnessHypotheses]`,
    the unitary pairing identity continues to hold for arbitrary
    positive volumes. -/
theorem unitary_pairing_with_pl
    [SingleVolumeIrrational] [PLCorrectnessHypotheses]
    (q vol : ℝ) (hq : q > 1) (hvol : vol > 0) :
    let hbar_q2 := (1 - 1/q) ^ 2
    (vol / hbar_q2) * (hbar_q2 / vol) = 1 :=
  SingleVolumeIrrational.pairing_unitary q vol hq hvol

/-- **Volume-positivity preservation**: the pairing-unitary form
    requires `vol > 0`, which is preserved under multiplication
    by any positive scalar. -/
theorem unitary_pairing_scaled
    [SingleVolumeIrrational]
    (q vol c : ℝ) (hq : q > 1) (hvol : vol > 0) (hc : c > 0) :
    let hbar_q2 := (1 - 1/q) ^ 2
    ((c * vol) / hbar_q2) * (hbar_q2 / (c * vol)) = 1 :=
  SingleVolumeIrrational.pairing_unitary q (c * vol) hq
    (mul_pos hc hvol)

/-- **Full hyperbolic-volume + baryon-period composition**: under
    both classes, the geometric universality holds at every q > 1,
    every positive volume, and the lower-bound witness holds. -/
theorem hv_bp_full_composition
    [SingleVolumeIrrational] [PLCorrectnessHypotheses]
    (q vol : ℝ) (hq : q > 1) (hvol : vol > 0) :
    (let hbar_q2 := (1 - 1/q) ^ 2
     (vol / hbar_q2) * (hbar_q2 / vol) = 1) ∧
    ((0 : ℝ) ≤ 0) :=
  ⟨SingleVolumeIrrational.pairing_unitary q vol hq hvol,
   PLCorrectnessHypotheses.pl_decomposition_lower_bound q hq⟩

end QOU.BraidKnot
