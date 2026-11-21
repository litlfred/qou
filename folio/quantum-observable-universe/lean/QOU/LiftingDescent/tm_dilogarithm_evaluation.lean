import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

/-!
# QOU.LiftingDescent.tm_dilogarithm_evaluation

**Conjecture** ([`conj:topological-mass-dilogarithm`](../../../quantum-observable-universe/mass-endomorphism/topological-mass-dilogarithm.md)).

*Each exceptional-divisor summand evaluates to the symmetric q-dilogarithm:*

    ‖ MI∫_{E_i} (∇_A q, L ∧ F⁺) ‖ = ∫₀^{z_i} ln_q(1+t)/t dt = −Li₂^q(−z_i),

*in the spectral coordinates of the Briggs–Klein chart at `E_i`.*

## Structure (hypothesis vs. derivation)

The `.md` displays a chain of **two** equalities.

- The **second** equality — `∫₀^{z} ln_q(1+t)/t dt = −Li₂^q(−z)` — is
  termwise integration of the series for `ln_q` (proved in prose in the
  mass-endomorphism tower proof). Here `negLi2q` is **defined** as the
  Mathlib interval integral, recorded by `negLi2q_integral_representation`;
  the series form is not proved in Lean, since `ln_q` stays opaque.
- The **first** equality — the Briggs–Klein chart evaluation of the
  multiplicative-integral norm to that integral — is the genuine open
  analytic input (Yekutieli multiplicative integration evaluated in the
  Briggs–Klein chart). It is carried as the field
  `chart_eval` of the class `TmDivisorChartInputs`, and
  `tm_divisor_chart_evaluation` returns that field. There is no `sorry`;
  the input is a hypothesis.

The main theorem chains that hypothesis with the definitional integral
representation. Since the hypothesis is the first equality and the second
holds by definition, the theorem is the statement itself under a
hypothesis. For this reason the block is a conjecture (2026-11-21).

## Base ring (§7c)

`ℝ` throughout: the statement is about an archimedean norm and a real
interval integral (`∫ … dt` over the volume measure), which are
archimedean constructs.
-/

namespace QOU.LiftingDescent

/-! `MI` is `opaque`, deliberately.  An earlier revision *defined* it as the
very integral that `tm_divisor_chart_evaluation` claims it equals, which made
that "open analytic input" a `rfl` tautology — the Briggs-Klein chart
evaluation was assumed by definition rather than stated.  (It also created a
forward reference, since the definition mentioned `z`/`lnq` before either was
declared.)  Bean `qou-t4cv`.  `negLi2q` below is a *genuine* definition and its
integral representation is honestly definitional, as its docstring says. -/

/-- The norm of the divisor-`i` non-abelian multiplicative integral
    `‖MI∫_{E_i}(∇_A q, L ∧ F⁺)‖`. -/
opaque MI : ℕ → ℝ

/-- The q-logarithm `ln_q` (at the ambient deformation parameter `q`).
    Its q-series theory is not in Mathlib, so it stays opaque; the
    dilogarithm `negLi2q` below is a genuine integral of it. -/
opaque lnq : ℝ → ℝ

/-- The Briggs–Klein spectral coordinate `z_i` at the exceptional
    divisor `E_i`. -/
opaque z : ℕ → ℝ

/-- The integral `∫₀^{w} ln_q(1+t)/t dt` as a Mathlib interval integral.
    With the symmetric q-integer it equals `−Li₂^q(−w)`, the symmetric
    q-dilogarithm (termwise integration; not proved here). It is **not** the
    Faddeev–Kashaev product `Φ_q(w) = ∏(1 − q^{-k} w)⁻¹`: the corpus records
    that identification as false (`def:quantum-dilogarithm-disambiguation`),
    and a 40-digit check at the proton `q₀` gives 0.2802 for this integral at
    `w = 0.3` against `Φ_q(0.3) ≈ 19.13`. Until 2026-11-21 this was named
    `Phi_q`. -/
noncomputable def negLi2q (w : ℝ) : ℝ := ∫ t in (0 : ℝ)..w, lnq (1 + t) / t

/-- **Integral representation of `negLi2q`** — the .md's second equality,
    proved (definitionally) rather than assumed. -/
theorem negLi2q_integral_representation (w : ℝ) :
    negLi2q w = ∫ t in (0 : ℝ)..w, lnq (1 + t) / t := rfl

class TmDivisorChartInputs : Prop where
  /-- Open analytic input — Briggs–Klein chart evaluation. -/
  chart_eval : ∀ i : ℕ, MI i = ∫ t in (0 : ℝ)..(z i), lnq (1 + t) / t

/-- **Open analytic input — Briggs–Klein chart evaluation.**  In the
    spectral coordinates of the Briggs–Klein chart at `E_i`, the
    multiplicative-integral norm evaluates to the q-dilogarithm
    integral at `z_i`.  Needs Yekutieli multiplicative integration
    evaluated for a connection on `E_i`. The corpus has the discrete layer
    (`QOU.MathlibExt.YekutieliIntegration`), the continuum Stokes theorem
    only as the class `NonAbelianStokes`, and the abstract `∇_q`
    (`CategoricalQConnection.nabla_q`), but no explicit connection on `E_i`
    whose integral is computed. -/
-- Ref: [yekutieli2015] https://doi.org/10.1142/9537
theorem tm_divisor_chart_evaluation [ctx : TmDivisorChartInputs] :
    ∀ i : ℕ, MI i = ∫ t in (0 : ℝ)..(z i), lnq (1 + t) / t :=
  ctx.chart_eval

/-- **Exceptional-divisor summand = quantum dilogarithm**
    ([`conj:topological-mass-dilogarithm`]).

`‖MI∫_{E_i}‖ = negLi2q(z_i)` for every exceptional divisor `E_i`.
Conditional on `TmDivisorChartInputs`, which carries the first equality;
the second is the definition of `negLi2q`. -/
theorem tm_dilogarithm_evaluation [TmDivisorChartInputs] : ∀ i : ℕ, MI i = negLi2q (z i) :=
  fun i =>
    (tm_divisor_chart_evaluation i).trans
      (negLi2q_integral_representation (z i)).symm

end QOU.LiftingDescent
