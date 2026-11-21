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

**Nothing in this file is that functor** (2026-08-24, bean
`qou-7nbx`).  There is no source category, no target category, no
action on morphisms and no Hecke-compatibility square anywhere
below — only the scalar evaluation and the point it evaluates at.
The class at the end of the file was called
`ArchimedeanRealizationFunctor` and advertised "the existence of a
Hecke-compatible Archimedean realisation functor … with the listed
compatibility properties"; its fields were a real number, its
positivity, and an equation pinning it to `q_zero`, and the listed
properties were not listed.  It is now `ArchimedeanEvaluationPoint`,
which is what it always was.

**File status**: upstreamable scalar piece (~50 LoC); the full
functor requires `Mathlib.Algebra.IwahoriHecke`, which this
checkout's Mathlib does not contain in any form (deferred).

**References**:
- Mathlib `Polynomial.eval` — the underlying primitive.
- [leitner2026] `prop:archimedean-realization-functor`.
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
-- Ref: [leitner2026] def:m-mu-over-m-e-calibration
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

/-! ### The evaluation point — a pinned constant, not a functor

**Restated 2026-08-24 (bean `qou-7nbx`).**  This was
`class ArchimedeanRealizationFunctor` with fields `q0 : ℝ`,
`q0_gt_one : q0 > 1`, `q0_canonical : q0 = q_zero`, and a global
`instance canonical` setting `q0 := q_zero` so that `q0_canonical`
closed by `rfl`.  Two things were wrong with it and one of them was
load-bearing:

1. **The name and docstring promised a functor and the class contained
   a real number.**  Fixed by saying what it is.
2. **`q0_canonical` pinned the class's only datum to a constant**, so
   the class had exactly one model, the global instance supplied it,
   and `[ArchimedeanRealizationFunctor]` was equivalent to no
   hypothesis at all.  Fixed by moving the point out of the class and
   taking it as a *parameter*, the remedy worked in
   `QOU/Archimedean/JetOrderIndependence.lean`: `[ArchimedeanEvaluationPoint q0]`
   is now a falsifiable constraint on a named `q0` — satisfied at
   `q_zero` (`instCanonical`) and refuted anywhere else
   (`not_evaluationPoint_of_ne`, and concretely
   `not_evaluationPoint_two`).

**Why the class was not given the functor instead.**  That is the
paper's actual claim and it cannot be written here: this checkout's
Mathlib has no Iwahori–Hecke algebra at all, so a "functor" declared
now would have to invent both its source category and its
compatibility square — which reproduces exactly the defect above, one
level up, with more prose covering it.  Until
`Mathlib.Algebra.IwahoriHecke` exists, the honest content of this file
is the scalar evaluation (`evalAtQZero`, proved a ring map, and proved
*unique* as one in `UpstreamSubstrateBridge.archimedean_eval_well_defined`)
plus the point below.  A discharge of `S-Archimedean-realisation`
would owe: the two categories, the action on morphisms, and the square
`Real_q₀ ∘ (Hecke action) = (real action) ∘ Real_q₀`.  None of the
three is here, and `UpstreamSubstrateBridge` no longer says otherwise. -/

/-- **The Archimedean evaluation point.**  `q0` is the substrate value
    at which `evalAtQZero` evaluates; the class asserts of a *given*
    `q0` that it is the QOU canonical one.

    Only the pin is a field.  `q0 > 1` (the analytic-continuation
    regime) was a second field and is derivable from the pin, so it is
    a theorem below rather than an assumption a model gets to restate. -/
class ArchimedeanEvaluationPoint (q0 : ℝ) : Prop where
  /-- The evaluation point is the QOU canonical substrate value. -/
  is_substrate : q0 = q_zero

/-- **Analytic-continuation regime — PROVED (derived).**  Any
    Archimedean evaluation point is `> 1`, from the pin and
    `q_zero_gt_one`. -/
theorem ArchimedeanEvaluationPoint.gt_one (q0 : ℝ)
    [h : ArchimedeanEvaluationPoint q0] : q0 > 1 := by
  rw [h.is_substrate]; exact q_zero_gt_one

/-- **The hypothesis is satisfiable, at `q_zero` (PROVED).**  So
    `[ArchimedeanEvaluationPoint q0]` for an *unspecified* `q0` asserts
    nothing beyond that some point exists; a downstream result must say
    which point. -/
instance instCanonical : ArchimedeanEvaluationPoint q_zero :=
  ⟨rfl⟩

/-- **…and it fails at every other real (PROVED).**  This is the content
    the parameterisation buys: the hypothesis is a real constraint on the
    supplied point, not a restatement of `q_zero`'s definition. -/
theorem not_evaluationPoint_of_ne {q0 : ℝ} (h : q0 ≠ q_zero) :
    ¬ ArchimedeanEvaluationPoint q0 :=
  fun hp => h hp.is_substrate

/-- **A concrete non-model (PROVED).**  `2` is not the QOU evaluation
    point, so the class is not satisfied by every real. -/
theorem not_evaluationPoint_two : ¬ ArchimedeanEvaluationPoint 2 :=
  not_evaluationPoint_of_ne (by unfold q_zero; norm_num)

end QOU.Mathlib.ArchimedeanRealization
