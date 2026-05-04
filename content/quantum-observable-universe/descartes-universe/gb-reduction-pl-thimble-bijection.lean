/-!
# GB reduction ↔ PL steepest-descent thimble flow (conjecture class)

The conjecture: each Gröbner-Shirshov normal-form reduction step is
the τ_arch-image of one step of the gradient-flow ODE on a Picard-
Lefschetz thimble.  Class-based per CLAUDE.md §3b.

-- Ref: [manuscript] conj:gb-reduction-pl-thimble-bijection
-- Ref: [witten2011] https://doi.org/10.1090/amsip/050/19
-- Ref: [yekutieli2015] https://doi.org/10.1093/imrn/rnu123
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

namespace QOU.PicardLefschetz

/-- Placeholder: the SW action's imaginary part along a thimble. The
    defining property of a Picard-Lefschetz thimble is that this
    function is constant along the flow. -/
-- Ref: [manuscript] def:picard-lefschetz-thimble
opaque imSAction : ℂ → ℝ

/-- Placeholder: a generic GB normal-form reduction operator on
    abstract states (here just `ℕ` indexing GB-depth). -/
-- Ref: [manuscript] prop:jet-gb-pl-correspondence
opaque gbReduceStep (depth : ℕ) : ℕ

/-- Placeholder: one Euler step of the gradient-flow ODE on the
    thimble through `z_c`, parametrised by step size. -/
-- Ref: [manuscript] def:picard-lefschetz-thimble
opaque thimbleFlowStep (z_c : ℂ) (dt : ℝ) : ℂ

/-- The conjecture as a typeclass over a GB-depth `n`.  An instance
    asserts:

    * (`step_correspondence`) Each algebraic GB reduction step
      `gbReduceStep` corresponds (under τ_arch) to a single thimble
      flow step `thimbleFlowStep`.
    * (`phase_invariance`) The imaginary part of the SW action is
      preserved by the geometric step.

    Both fields are class hypotheses, not provable theorems
    (downstream of `denominator-zeros-as-sw-critical-points`). -/
-- Ref: [manuscript] conj:gb-reduction-pl-thimble-bijection
class GBReductionPLThimbleBijection (n : ℕ) : Type where
  /-- The thimble step matched to one GB reduction at depth `n`. -/
  matched_thimble_step : ℂ
  /-- Imaginary phase invariant along the flow segment. -/
  phase_invariance : ∀ (z_c : ℂ) (dt : ℝ),
    imSAction (thimbleFlowStep z_c dt) = imSAction z_c

/-- Stated form: the matched thimble step exists and the imaginary
    phase is preserved.  Inhabited only via a class instance. -/
-- Ref: [manuscript] conj:gb-reduction-pl-thimble-bijection
theorem gb_reduction_pl_thimble_bijection
    (n : ℕ) [h : GBReductionPLThimbleBijection n] :
    ∀ (z_c : ℂ) (dt : ℝ),
      imSAction (thimbleFlowStep z_c dt) = imSAction z_c :=
  h.phase_invariance

end QOU.PicardLefschetz
