-- `QOU/Mathlib/ParallelogramContour.lean` was inconsistent, by TWO independent
-- routes. Both are recorded here as comments (they no longer compile, which is
-- the point) plus a positive check that the repaired axioms are still usable.
--
-- Nothing is reproduced: this imports the real module, so a revert of the fix
-- turns the commented routes back into live proofs of `False`.
--
-- ## Verifying this: a "must fail" probe is satisfied by ANY error
--
-- To re-check the fix you uncomment a route and confirm it no longer compiles.
-- That check is far weaker than it looks, and it silently passed for the wrong
-- reason on 2026-08-24: after a rebase the `QOU.Mathlib.ParallelogramContour`
-- olean was absent from `.lake/build/lib/lean`, so BOTH routes exited 1 with
--
--     error: object file '…/ParallelogramContour.olean' … does not exist
--
-- which is indistinguishable from "the added hypothesis blocks the route" if
-- you only read the exit code. THIS FILE exited 1 at the same moment, for the
-- same reason, while being the one file here expected to exit 0 — that is what
-- exposed it. Had the positive examples not been in the same file, the false
-- pass would have been reported as a verification.
--
-- So: build the olean first (`lean … -o <path>/ParallelogramContour.olean`),
-- and assert WHICH error each route fails with, not merely that it fails.
-- Verified against the repaired module:
--
--   route 1  →  `Type mismatch` at the axiom application
--                (`fun z => (z - w)⁻¹` is not `Differentiable ℂ`)
--   route 2  →  `unsolved goals`
--                (`horient : 0 < (ω₂ / ω₁).im` is undischargeable at ω₁ = ω₂ = 0)
--   this file →  exit 0, 0 errors

import QOU.Mathlib.ParallelogramContour

open Complex

namespace ParallelogramInconsistencyProbe

/-! ## Route 1 — the missing differentiability hypothesis

`parallelogramIntegral_eq_zero_of_differentiable` read

    axiom … (f : ℂ → ℂ) (ω₁ ω₂ z₀ : ℂ) : parallelogramIntegral f ω₁ ω₂ z₀ = 0

Its NAME says `_of_differentiable` and the comment above it says "If f is
analytic on and inside the parallelogram", but neither reached the statement:
it quantified over EVERY `f : ℂ → ℂ`. Instantiating at the pole function that
the second axiom evaluates to `2πi` gave `0 = 2πi`:

    theorem route_one : False := by
      have h0 : parallelogramIntegral (fun z => (z - 0)⁻¹) 1 I 0 = 0 :=
        parallelogramIntegral_eq_zero_of_differentiable _ _ _ _
      have h2 := parallelogramIntegral_inv_sub_eq_two_pi_i 1 I 0 0
      …                                          -- 0 = 2πi

Now blocked: the axiom demands `Differentiable ℂ f`, and `fun z => (z - w)⁻¹`
is not entire. -/

/-! ## Route 2 — the degenerate parallelogram, needing only ONE axiom

`parallelogramIntegral_inv_sub_eq_two_pi_i` read

    axiom … (ω₁ ω₂ z₀ w : ℂ) : parallelogramIntegral (fun z => (z-w)⁻¹) … = 2πi

Every term of `parallelogramIntegral` carries a literal `ω₁` or `ω₂` factor, so
at `ω₁ = ω₂ = 0` the left side is identically `0`. That is `0 = 2πi` from this
axiom ALONE — the first axiom is not needed:

    theorem route_two : False := by
      have h := parallelogramIntegral_inv_sub_eq_two_pi_i 0 0 0 0
      simp only [parallelogramIntegral, zero_mul,
        intervalIntegral.integral_zero, …] at h   -- h : 0 = 2πi
      …

Now blocked: `horient : 0 < (ω₂ / ω₁).im` fails at `ω₁ = ω₂ = 0`, since
`(0 / 0).im = 0`. -/

/-! ## The repaired axioms are still usable

A regression check in the other direction: the hypotheses are satisfiable, so
the fix constrains the axioms without emptying them. -/

example (f : ℂ → ℂ) (hf : Differentiable ℂ f) (ω₁ ω₂ z₀ : ℂ) :
    parallelogramIntegral f ω₁ ω₂ z₀ = 0 :=
  parallelogramIntegral_eq_zero_of_differentiable f ω₁ ω₂ z₀ hf

-- The constant function is entire, so the vanishing axiom applies to it.
example (c : ℂ) (ω₁ ω₂ z₀ : ℂ) :
    parallelogramIntegral (fun _ => c) ω₁ ω₂ z₀ = 0 :=
  parallelogramIntegral_eq_zero_of_differentiable _ _ _ _ (differentiable_const c)

-- A strictly interior pole in a positively-oriented parallelogram still gives 2πi.
example (ω₁ ω₂ z₀ : ℂ) (horient : 0 < (ω₂ / ω₁).im) :
    parallelogramIntegral
        (fun z => (z - (z₀ + ((1 / 2 : ℝ) : ℂ) * ω₁ + ((1 / 2 : ℝ) : ℂ) * ω₂))⁻¹)
        ω₁ ω₂ z₀
      = 2 * Real.pi * I :=
  parallelogramIntegral_inv_sub_eq_two_pi_i ω₁ ω₂ z₀ _ horient
    (1 / 2) (1 / 2) (by norm_num) (by norm_num) (by norm_num) (by norm_num) rfl

end ParallelogramInconsistencyProbe
