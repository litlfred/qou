import Mathlib.NumberTheory.LSeries.RiemannZeta

/-!
# QOU.BraidKnot.ClassicalRiemannHypothesis — conjectural class (§3b)

**§3b class axiomatisation** for content block
[`conj:classical-riemann-hypothesis`](../../../quantum-observable-universe/stochastic-mechanics/classical-riemann-hypothesis.md): *The Riemann hypothesis*.

This is a **conjecture**: the class `ClassicalRiemannHypothesis` carries the
conjecture's actual content — every non-trivial zero of `riemannZeta` lies on
the critical line `Re s = 1/2`. The `noncomputable instance` is the conjectural
witness whose `sorry` represents the open conjecture itself (per AGENTS.md §3b),
NOT a missing proof. Downstream theorems may take
`[ClassicalRiemannHypothesis]` as an explicit `[Instance]` hypothesis to derive
rigorous-conditional results (per §3b-cond).

Matured 2026-06-25 from a degenerate `residual : ℝ := 0` placeholder to the
faithful statement over Mathlib's `riemannZeta`. The trivial zeros of
`riemannZeta` are the negative even integers `s = -2(n+1)` (`n : ℕ`); RH
constrains the remaining (non-trivial) zeros. Statement shape typechecked
against `opaque riemannZeta : ℂ → ℂ`; full compile is CI-gated (the
`Mathlib.NumberTheory.LSeries.RiemannZeta` olean is absent from the partial
sandbox cache, and Mathlib search was network-blocked).

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

-- The conjecture itself.  The `sorry` represents the **open conjecture**
-- per §3b — not a missing proof.
-- Ref: [leitner2026] quantum-observable-universe/stochastic-mechanics/classical-riemann-hypothesis.ts

-- **No instance is provided — that is the honest open state** (AGENTS.md §3b-tax).
-- History: this file previously carried
--     axiom classicalRiemannHypothesis_conjecture : ClassicalRiemannHypothesis
--     noncomputable instance : ClassicalRiemannHypothesis := classicalRiemannHypothesis_conjecture
-- i.e. the conjecture was asserted by `axiom` and installed as a global instance, so
-- every downstream `[ClassicalRiemannHypothesis]` resolved for free.  Removed, not completed — downstream
-- results must take `[ClassicalRiemannHypothesis]` as an explicit hypothesis.

end QOU.BraidKnot
