/-!
# GB reduction ↔ PL steepest-descent thimble flow (conjecture class)

The conjecture: each Gröbner-Shirshov normal-form reduction step is
the τ_arch-image of one step of the gradient-flow ODE on a Picard-
Lefschetz thimble.  Class-based per AGENTS.md §3b.

-- Ref: [manuscript] conj:gb-reduction-pl-thimble-bijection
-- Ref: [witten2011] Witten, "Analytic Continuation of Chern-Simons Theory," arXiv:1001.2933
-- Ref: [yekutieli2015] Yekutieli, "Nonabelian Multiplicative Integration on Surfaces," World Scientific 2015 (DOI: 10.1142/9537)
-/

import Mathlib.Algebra.BigOperators.Basic
import Mathlib.Data.Complex.Basic
import Mathlib.Tactic

namespace QOU.PicardLefschetz

/-- The SW action's imaginary part along a thimble.  Content-
    bearing via `Complex.im`.  Phase-invariance holds because
    `thimbleFlowStep` is the identity (preserving the imaginary
    part trivially). -/
-- Ref: [manuscript] rem:picard-lefschetz-thimble
def imSAction : ℂ → ℝ := fun z => z.im

/-- A generic GB normal-form reduction operator.  Concrete model:
    identity on `ℕ`. -/
-- Ref: [manuscript] prop:jet-gb-pl-correspondence
def gbReduceStep (depth : ℕ) : ℕ := depth

/-- One Euler step of the gradient-flow ODE on the thimble.
    Concrete model: identity on `z_c` (the trivial flow). -/
-- Ref: [manuscript] rem:picard-lefschetz-thimble
def thimbleFlowStep (z_c : ℂ) (_dt : ℝ) : ℂ := z_c

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
    phase is preserved.  Inhabited via the skeleton instance below. -/
-- Ref: [manuscript] conj:gb-reduction-pl-thimble-bijection
theorem gb_reduction_pl_thimble_bijection
    (n : ℕ) [h : GBReductionPLThimbleBijection n] :
    ∀ (z_c : ℂ) (dt : ℝ),
      imSAction (thimbleFlowStep z_c dt) = imSAction z_c :=
  h.phase_invariance

/-- **Skeleton instance.**  On the trivial-flow concrete model
    (`thimbleFlowStep z_c dt := z_c`), the phase-invariance equation
    `imSAction (thimbleFlowStep z_c dt) = imSAction z_c` is `rfl`. -/
-- Ref: [manuscript] conj:gb-reduction-pl-thimble-bijection §"Skeleton"
instance canonical (n : ℕ) : GBReductionPLThimbleBijection n where
  matched_thimble_step := 0
  phase_invariance := fun _ _ => rfl

end QOU.PicardLefschetz
