import Mathlib.NumberTheory.LSeries.RiemannZeta

/-!
# QOU.BraidKnot.ClassicalRiemannHypothesis — conjectural class (§3b)

**§3b class axiomatisation** for content block
[`conj:classical-riemann-hypothesis`](../../../quantum-observable-universe/stochastic-mechanics/classical-riemann-hypothesis.md): *The Riemann hypothesis*.

This is a **conjecture**: the class `ClassicalRiemannHypothesis` carries the
conjecture's actual content — every non-trivial zero of `riemannZeta` lies on
the critical line `Re s = 1/2`. No global instance is provided (per AGENTS.md
§3b-tax), representing the honest open state. Downstream theorems may take
`[ClassicalRiemannHypothesis]` as an explicit `[Instance]` hypothesis to derive
rigorous-conditional results (per §3b-cond).

Matured 2026-06-25 from a degenerate `residual : ℝ := 0` placeholder to the
faithful statement over Mathlib's `riemannZeta`. The trivial zeros of
`riemannZeta` are the negative even integers `s = -2(n+1)` (`n : ℕ`); RH
constrains the remaining (non-trivial) zeros.

Ref: [leitner2026] quantum-observable-universe/stochastic-mechanics/classical-riemann-hypothesis.md
-/

namespace QOU.BraidKnot

/-- **Conjecture (Riemann, 1859).** Every non-trivial zero `s` of the Riemann
zeta function lies on the critical line `Re s = 1/2`. "Non-trivial" excludes the
trivial zeros at the negative even integers `s = -2(n+1)`, `n : ℕ`.

    Conjectural class — see
    [`conj:classical-riemann-hypothesis`](../../../quantum-observable-universe/stochastic-mechanics/classical-riemann-hypothesis.md). -/
class ClassicalRiemannHypothesis : Prop where
  /-- All non-trivial zeros of `ζ` satisfy `Re s = 1/2`. -/
  rh : ∀ s : ℂ, riemannZeta s = 0 → (∀ n : ℕ, s ≠ -2 * ((n : ℂ) + 1)) → s.re = 1 / 2

-- Ref: [leitner2026] quantum-observable-universe/stochastic-mechanics/classical-riemann-hypothesis.ts
-- **No instance is provided — that is the honest open state** (AGENTS.md §3b-tax).

namespace ClassicalRiemannHypothesis

/-- Conditional on `ClassicalRiemannHypothesis`, every non-trivial zero `s`
    satisfies `2 * s.re = 1`. -/
theorem two_mul_re_eq_one [h : ClassicalRiemannHypothesis] {s : ℂ}
    (hz : riemannZeta s = 0) (htriv : ∀ n : ℕ, s ≠ -2 * ((n : ℂ) + 1)) :
    2 * s.re = 1 := by
  have hre := h.rh s hz htriv
  linarith

/-- Conditional on `ClassicalRiemannHypothesis`, every non-trivial zero `s`
    lies strictly in the right half-plane `0 < s.re`. -/
theorem re_pos_of_nontrivial_zero [h : ClassicalRiemannHypothesis] {s : ℂ}
    (hz : riemannZeta s = 0) (htriv : ∀ n : ℕ, s ≠ -2 * ((n : ℂ) + 1)) :
    0 < s.re := by
  have hre := h.rh s hz htriv
  linarith

/-- Conditional on `ClassicalRiemannHypothesis`, every non-trivial zero `s`
    satisfies `s.re < 1`. -/
theorem re_lt_one_of_nontrivial_zero [h : ClassicalRiemannHypothesis] {s : ℂ}
    (hz : riemannZeta s = 0) (htriv : ∀ n : ℕ, s ≠ -2 * ((n : ℂ) + 1)) :
    s.re < 1 := by
  have hre := h.rh s hz htriv
  linarith

/-- Conditional on `ClassicalRiemannHypothesis`, every non-trivial zero `s`
    has real part invariant under the functional-equation reflection `s ↦ 1 - s`. -/
theorem one_sub_re_eq_re_of_nontrivial_zero [h : ClassicalRiemannHypothesis] {s : ℂ}
    (hz : riemannZeta s = 0) (htriv : ∀ n : ℕ, s ≠ -2 * ((n : ℂ) + 1)) :
    (1 - s).re = s.re := by
  have hre := h.rh s hz htriv
  simp only [Complex.sub_re, Complex.one_re]
  linarith

end ClassicalRiemannHypothesis

end QOU.BraidKnot
