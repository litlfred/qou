import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.Mathlib.ArchimedeanRealization — scalar evaluation `q ↦ q₀`

The Archimedean realisation functor `Real_q₀ : ModulesOver(ℚ(q))
→ ModulesOver(ℝ)` sends a `ℚ(q)`-valued categorical object to
its real-valued limit at `q = q₀`.  The full functor requires
Mathlib's `IwahoriHeckeAlgebra n q` formalisation (deferred
upstream).

This file supplies the **chain-independent scalar piece**: the
evaluation `Polynomial ℝ → ℝ` at a fixed point `q₀`, plus a
`ratPolyEvalAt` wrapper for rational-Laurent-polynomial
evaluation with denominator non-vanishing.

Once the full Hecke library lands, the functor `Real_q₀` is
defined by combining this scalar `evalAt` with the Hecke-module
structure.

**File status**: upstreamable scalar piece (~50 LoC); the full
functor requires `Mathlib.Algebra.IwahoriHecke` (deferred).

**References**:
- Mathlib `Polynomial.eval` — the underlying primitive.
- [manuscript] `prop:archimedean-realization-functor`.
-/

namespace QOU.Mathlib.ArchimedeanRealization

/-- The QOU substrate parameter `q₀`.  Bound here to the canonical
    50-digit decimal expansion from
    `computations/full-twist-delta-n2-verification.witness.json::q_0`
    (proton-anchor re-pin, 2026-05-28; see
    `tools/qou-substrate/python/qou_substrate/constants.py::Q_50_DIGIT_STR`).

    Bumped 2026-06-08 from the previous 5-dps literal `1.10998` to
    match the same canonical literal used in
    `QOU.HeckeAlgebra.QSubstrate.q_0` and
    `QOU.LiftingDescent.H3BraneTowerScaffold.q0` (both 50 dps, both
    landed in PR #1978). -/
-- Ref: full-twist-delta-n2-verification.witness.json::q_0 (the literal source — proton-anchor re-pin, 2026-05-28)
-- Ref: q-pinning-50-digit.witness.json (companion witness with the same q_0; canonical record of the pin)
-- Ref: [manuscript] def:m-mu-over-m-e-calibration
noncomputable def q_zero : ℝ :=
  1.10997858275138080759166909561076887987449912187357763605672

/-- `q_zero > 1`: the substrate is in the analytic-continuation
    regime where every `[k]_q` is positive and non-vanishing. -/
theorem q_zero_gt_one : q_zero > 1 := by
  unfold q_zero
  norm_num

/-- `q_zero > 0`: positivity of the substrate parameter. -/
theorem q_zero_pos : q_zero > 0 := by
  unfold q_zero
  norm_num

/-- `q_zero ≠ 0`: substrate parameter is non-zero. -/
theorem q_zero_ne_zero : q_zero ≠ 0 := ne_of_gt q_zero_pos

/-- **Scalar Archimedean evaluation**: a real polynomial
    `p ∈ ℝ[q]` evaluated at `q = q₀`.  Wraps Mathlib's
    `Polynomial.eval`. -/
noncomputable def evalAtQZero (p : Polynomial ℝ) : ℝ := p.eval q_zero

/-- The constant polynomial evaluates to its constant value. -/
theorem evalAtQZero_C (c : ℝ) : evalAtQZero (Polynomial.C c) = c := by
  unfold evalAtQZero
  exact Polynomial.eval_C

/-- The variable `X` evaluates to `q₀`. -/
theorem evalAtQZero_X : evalAtQZero (Polynomial.X) = q_zero := by
  unfold evalAtQZero
  exact Polynomial.eval_X

/-- Evaluation is a ring homomorphism (sends `+` to `+`). -/
theorem evalAtQZero_add (p q : Polynomial ℝ) :
    evalAtQZero (p + q) = evalAtQZero p + evalAtQZero q := by
  unfold evalAtQZero
  exact Polynomial.eval_add

/-- Evaluation is a ring homomorphism (sends `*` to `*`). -/
theorem evalAtQZero_mul (p q : Polynomial ℝ) :
    evalAtQZero (p * q) = evalAtQZero p * evalAtQZero q := by
  unfold evalAtQZero
  exact Polynomial.eval_mul

/-- **Rational-polynomial Archimedean evaluation**: evaluate
    a ratio of real polynomials at `q = q₀`, given the
    denominator's non-vanishing. -/
noncomputable def ratPolyEvalAtQZero
    (num den : Polynomial ℝ) (hden : den.eval q_zero ≠ 0) : ℝ :=
  evalAtQZero num / evalAtQZero den

/-- Substrate-q corollary: rational evaluation simplifies to
    `num.eval q₀ / den.eval q₀` directly. -/
theorem ratPolyEvalAtQZero_def
    (num den : Polynomial ℝ) (hden : den.eval q_zero ≠ 0) :
    ratPolyEvalAtQZero num den hden =
      num.eval q_zero / den.eval q_zero := rfl

/-- **§3b-cond class hypothesis**: the existence of a Hecke-
    compatible Archimedean realisation functor.  Once Mathlib's
    Iwahori–Hecke library lands, the class is discharged
    concretely.  For now, the class wraps the substrate-axiom
    that some such functor exists with the listed compatibility
    properties. -/
class ArchimedeanRealizationFunctor where
  /-- The substrate value `q₀` at which evaluation occurs. -/
  q0 : ℝ
  /-- `q₀ > 1` (analytic-continuation regime). -/
  q0_gt_one : q0 > 1
  /-- The substrate `q₀` matches the QOU canonical value. -/
  q0_canonical : q0 = q_zero

/-- Canonical instance: pin `q₀` to the QOU substrate value. -/
noncomputable instance canonical : ArchimedeanRealizationFunctor where
  q0 := q_zero
  q0_gt_one := q_zero_gt_one
  q0_canonical := rfl

end QOU.Mathlib.ArchimedeanRealization
