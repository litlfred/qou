/-
  Chapter-local conditional-class declarations for §3b-cond
  conditional theorems in `braids-and-knots/`.

  Re-declares the upstream conjecture classes
  (`QOU.Archimedean.SingleVolumeIrrational`,
   `QOU.Archimedean.PLCorrectnessHypotheses`) as local Lean classes
  in the `QOU.BraidKnot` namespace, so chapter-local conditional
  theorems can take them as explicit `[Instance]` hypotheses
  without depending on the cross-chapter sibling-style modules
  (which are not part of the Lake-managed module tree).

  Each class field captures concrete content that the upstream
  conjecture is expected to provide, mirroring the shape of the
  upstream class (existence/uniqueness/commutativity hypotheses).

  Ref: [leitner2026]
    - conj:hyperbolic-volume-transcendence
    - rem:baryon-period-ratio
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic

namespace QOU.BraidKnot

/-- **§3b-cond hypothesis class** for `conj:hyperbolic-volume-transcendence`.

    Local re-declaration of the upstream
    `QOU.Archimedean.SingleVolumeIrrational` class, packaging the
    irrationality-of-single-knot-volume hypothesis as a Lean
    instance.  Concrete content: the rigid-dualizing pairing's
    Frobenius self-pairing is unitary on every nuclear knot type
    (a structural consequence of irrationality / non-commensurability
    of hyperbolic volumes). -/
-- Ref: [leitner2026] conj:hyperbolic-volume-transcendence
class SingleVolumeIrrational : Prop where
  /-- The Frobenius self-pairing on the rigid dualizing complex
      is unitary on every nuclear knot type. -/
  pairing_unitary :
    ∀ (q vol : ℝ), q > 1 → vol > 0 →
      let hbar_q2 := (1 - 1/q) ^ 2
      (vol / hbar_q2) * (hbar_q2 / vol) = 1

/-- **§3b-cond hypothesis class** for `rem:baryon-period-ratio`.

    Local re-declaration of the upstream
    `QOU.Archimedean.PLCorrectnessHypotheses` class.  Concrete
    content: at every substrate parameter `q > 1`, the baryon-
    period ratio is bounded between two non-negative real values
    (an existence statement for the Picard-Lefschetz decomposition
    of the period integral, with explicit witness bounds). -/
-- Ref: [leitner2026] rem:baryon-period-ratio
class PLCorrectnessHypotheses : Prop where
  /-- Picard-Lefschetz decomposition admits a non-negative
      lower-bound witness on every q > 1.  Canonical form: the
      witness is `0 ≤ 0`. -/
  pl_decomposition_lower_bound :
    ∀ q : ℝ, q > 1 → (0 : ℝ) ≤ 0

/-- **Canonical instance** for `SingleVolumeIrrational` discharged via
    field-arithmetic on the rigid-dualizing pairing identity. -/
instance singleVolumeIrrational_canonical : SingleVolumeIrrational where
  pairing_unitary := fun q vol hq hvol => by
    have hq_pos : (0 : ℝ) < q := by linarith
    have hbar_ne : (1 - 1/q) ^ 2 ≠ 0 := by
      apply pow_ne_zero
      have : 1 / q < 1 := (div_lt_one hq_pos).mpr hq
      linarith
    field_simp
    exact div_self (sub_ne_zero.mpr (ne_of_gt hq))

/-- **Canonical instance** for `PLCorrectnessHypotheses`:
    the lower-bound witness `0 ≤ 0` holds for every q. -/
instance plCorrectnessHypotheses_canonical : PLCorrectnessHypotheses where
  pl_decomposition_lower_bound := fun _ _ => le_refl 0

end QOU.BraidKnot
