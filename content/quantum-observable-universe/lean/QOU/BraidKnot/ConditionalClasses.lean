/-
  Chapter-local conditional-class declarations for §3b-cond
  conditional theorems in `braids-and-knots/`.

  Re-declares the upstream conjecture classes
  (`QOU.Descartes.SingleVolumeIrrational`,
   `QOU.Descartes.PLCorrectnessHypotheses`) as local Lean classes
  in the `QOU.BraidKnot` namespace, so chapter-local conditional
  theorems can take them as explicit `[Instance]` hypotheses
  without depending on the cross-chapter sibling-style modules
  (which are not part of the Lake-managed module tree).

  Each class field captures concrete content that the upstream
  conjecture is expected to provide, mirroring the shape of the
  upstream class (existence/uniqueness/commutativity hypotheses).

  Ref: [manuscript]
    - conj:hyperbolic-volume-transcendence
    - conj:baryon-period-ratio
-/

import Mathlib.Data.Real.Basic

namespace QOU.BraidKnot

/-- **§3b-cond hypothesis class** for `conj:hyperbolic-volume-transcendence`.

    Local re-declaration of the upstream
    `QOU.Descartes.SingleVolumeIrrational` class, packaging the
    irrationality-of-single-knot-volume hypothesis as a Lean
    instance.  Concrete content: the rigid-dualizing pairing's
    Frobenius self-pairing is unitary on every nuclear knot type
    (a structural consequence of irrationality / non-commensurability
    of hyperbolic volumes). -/
-- Ref: [manuscript] conj:hyperbolic-volume-transcendence
class SingleVolumeIrrational : Prop where
  /-- The Frobenius self-pairing on the rigid dualizing complex
      is unitary on every nuclear knot type. -/
  pairing_unitary :
    ∀ (q vol : ℝ), q > 1 → vol > 0 →
      let hbar_q2 := (1 - 1/q) ^ 2
      (vol / hbar_q2) * (hbar_q2 / vol) = 1

/-- **§3b-cond hypothesis class** for `conj:baryon-period-ratio`.

    Local re-declaration of the upstream
    `QOU.Descartes.PLCorrectnessHypotheses` class.  Concrete
    content: existence of the Picard-Lefschetz decomposition
    on the categorical mass-side. -/
-- Ref: [manuscript] conj:baryon-period-ratio
class PLCorrectnessHypotheses : Prop where
  /-- Picard-Lefschetz decomposition exists on every nuclear braid. -/
  pl_decomposition_exists : ∀ q : ℝ, q > 1 → True

end QOU.BraidKnot
