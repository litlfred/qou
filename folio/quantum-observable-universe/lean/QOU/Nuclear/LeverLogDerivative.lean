import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Pow

/-!
# The lever derivative decomposition (machine-checked calculus for the m(q₀) gate)

The Q_β precision-ladder relation `S(q) − Vol(4₁) = A(q)/u(q)³` differentiates
(quotient rule) into

$$\frac{dS}{dq} \;=\; \frac{A'}{u^3} \;-\; 3\,\frac{u'}{u}\,\bigl(S - \mathrm{Vol}(4_1)\bigr),$$

which underlies the **one-anchor derivative gate** on any meridian-holonomy
assignment `m(q₀)` for the c₃ bar-odd S
(`computations/qbeta/qbeta_c3_phib_mq_logderivative_constraint.py`: the static
term `A′/u³` carries > 99.99 % of the 3.84×10⁶ slope, `A′ ≈ +2.37`; the
log-derivative term is only ~10²).  This file machine-checks the *algebraic
form* of that decomposition so the gate is not re-derived by hand.  No
numerical value is used or wired; the statement is generic real calculus.

-- Ref: [leitner2026] computations/qbeta/qbeta-c3-phib-mq-logderivative-constraint.witness.json
-/

namespace QOU.QBeta.LeverLogDerivative

/-- **Quotient-rule decomposition for a cube-lever ratio.**  If `f` and `u`
are differentiable at `q` with `u q ≠ 0`, then `f/u³` is differentiable at
`q` with derivative `f′/u³ − 3(u′/u)(f/u³)` — the exact algebraic shape of
the c₃ S-slope decomposition (`f = A`, `S − Vol(4₁) = A/u³`). -/
theorem hasDerivAt_div_pow_three {f u : ℝ → ℝ} {f' u' q : ℝ}
    (hf : HasDerivAt f f' q) (hu : HasDerivAt u u' q) (hu0 : u q ≠ 0) :
    HasDerivAt (fun x => f x / u x ^ 3)
      (f' / u q ^ 3 - 3 * (u' / u q) * (f q / u q ^ 3)) q := by
  have h := hf.div (hu.pow 3) (pow_ne_zero 3 hu0)
  convert h using 1
  simp only [Pi.pow_apply]
  field_simp
  ring

/-- The decomposition rewritten in gate form: the *un-levered* derivative of
the ratio recovers `f′` up to the log-derivative correction —
`u³·(d/dq)(f/u³) = f′ − 3(u′/u)·f`.  This is the identity behind
"`u³·d[Im 𝔙(m(q))]/dq ≈ A′` at an anchor". -/
theorem cube_lever_gate_form {f u : ℝ → ℝ} (f' u' q : ℝ) (hu0 : u q ≠ 0) :
    u q ^ 3 * (f' / u q ^ 3 - 3 * (u' / u q) * (f q / u q ^ 3))
      = f' - 3 * (u' / u q) * f q := by
  field_simp

/-- **Static derivative recovery from the cube-lever slope (`thb7`).**
Adding the logarithmic-derivative correction `3 * (u' / u q) * f q` to the
rescaled cube-lever slope `u q ^ 3 * (f' / u q ^ 3 - 3 * (u' / u q) * (f q / u q ^ 3))`
recovers the bare numerator derivative `f'` whenever `u q ≠ 0`. -/
theorem cube_lever_static_recovery {f u : ℝ → ℝ} (f' u' q : ℝ) (hu0 : u q ≠ 0) :
    u q ^ 3 * (f' / u q ^ 3 - 3 * (u' / u q) * (f q / u q ^ 3)) + 3 * (u' / u q) * f q
      = f' := by
  rw [cube_lever_gate_form f' u' q hu0, sub_add_cancel]

end QOU.QBeta.LeverLogDerivative
