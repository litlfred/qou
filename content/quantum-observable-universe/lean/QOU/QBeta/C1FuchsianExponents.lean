/-
Copyright (c) 2026 litlfred. All rights reserved.

# C1's weights at the Fuchsian point `0` are computable — pure algebra, no analysis

The `∞`-side weight needs the analytic q-Borel/Laplace construction and is open
(bean `qou-vkg5`).  The **`0`-side** does not: `L1` is Fuchsian at `0`, and at a
Fuchsian point the multiplicative weights are the roots of the **indicial
equation**, which is read straight off the coefficients.

`L1 = (q²x−1)σ² − (q−1)σ − (q−1)`.  A local solution behaves like `x^α`, and
`σ(x^α) = q^α x^α`, so writing `t = q^α` and evaluating the coefficients at
`x = 0`:

    a₂(0)·t² + a₁(0)·t + a₀(0) = 0
    (−1)·t²  + (−(q−1))·t + (−(q−1)) = 0
    t² + (q−1)·t + (q−1) = 0

**Cross-checked against the recurrence, not just read off.**  Substituting
`y = Σ bₙ xⁿ` into `L1` and using `σ(xⁿ) = qⁿ xⁿ`, the coefficient of `xⁿ` is

    bₙ·[ q^{2n} + (q−1)qⁿ + (q−1) ]  =  q^{2n}·b_{n−1},

so the recurrence degenerates exactly when the bracket vanishes — i.e. at
`t = qⁿ` satisfying the same `t² + (q−1)t + (q−1) = 0`.  The indicial equation
above is therefore the resonance condition of the actual recurrence, derived two
independent ways.

The roots `t` **are** the multiplicative weights at `0`, in exactly the sense of
`QOU.Mathlib.QAlienBridge`: `t` is the `σ`-eigenvalue of the local solution.  So
C1's `0`-side weights are

    t = ( −(q−1) ± √((q−1)(q−5)) ) / 2 ,     discriminant  (q−1)² − 4(q−1) = q² − 6q + 5.

**Provenance.**  The indicial polynomial, its Vieta relations, and the
factorisation `(q−1)² − 4(q−1) = (q−1)(q−5)` are **not** introduced here — they
predate this file in [`C1ZeroSideExponents.lean`](C1ZeroSideExponents.lean)
(bean `qou-wgnx`), over a generic `CommRing` rather than the `ℚ[X]` used here,
and that file additionally proves the exponents are a **conjugate pair** for
`1 < q < 5` (so the substrate `q₀ ≈ 1.11` is inside) and that `|t|² = q−1`.
Neither is reproved here.  What is genuinely new below is only the
**non-square** proof.

This file proves the one structural fact that makes them interesting: **the
discriminant is not a square in `ℚ[q]`**, so the two weights at `0` are *not*
rational functions of `q` — they generate a quadratic extension, just as the `∞`
side does (`not_isSquare_newtonEdgeConstant`, `not_isSquare_dilationFactor`).

The proof is a multiplicity argument rather than the degree parity used for the
`∞`-side constants, because `q² − 6q + 5` has even degree and degree parity says
nothing: it factors as `(q−1)(q−5)` with **simple** roots, while a square has all
roots of even multiplicity.  Concretely, `f² = p` forces `f(1) = 0`, hence
`p'(1) = 2·f(1)·f'(1) = 0`; but `p'(1) = −4`.

**Scope.**  This computes the weights at `0` and shows they are irrational over
`ℚ(q)`.  It says nothing about the `∞`-side weight, which is the open item — the
two ends are genuinely different: `0` is Fuchsian (weights from an indicial
equation, pure algebra) and `∞` is irregular of slope `½` (weights from Stokes
data, needing the analytic construction).  No fit, nothing wired, no Stokes
multiplier.

§7c: `ℚ[X]` throughout — pure algebra over a domain, no ordering, nothing
archimedean.  Sorry-free.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853
-- Ref: [manuscript] docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md
-/
import Mathlib.Algebra.Polynomial.Degree.Lemmas
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Tactic
import QOU.QBeta.C1NewtonRamification

namespace QOU.QBeta

open Polynomial

/-- The discriminant of C1's indicial equation at the Fuchsian point `0`:
`(q−1)² − 4(q−1) = q² − 6q + 5`. -/
noncomputable def indicialDiscriminant : Polynomial ℚ := X ^ 2 - 6 * X + 5

/-- The discriminant factors with **simple** roots `1` and `5`.  This is why the
degree-parity argument used on the `∞` side does not apply here: the degree is
even. -/
theorem indicialDiscriminant_eq : indicialDiscriminant = (X - 1) * (X - 5) := by
  unfold indicialDiscriminant; ring

@[simp] theorem indicialDiscriminant_eval_one : indicialDiscriminant.eval 1 = 0 := by
  simp [indicialDiscriminant]; norm_num

@[simp] theorem indicialDiscriminant_derivative :
    derivative indicialDiscriminant = 2 * X - 6 := by
  unfold indicialDiscriminant
  simp
  ring

theorem indicialDiscriminant_derivative_eval_one :
    (derivative indicialDiscriminant).eval 1 = -4 := by
  rw [indicialDiscriminant_derivative]
  simp
  norm_num

/-- **C1's two weights at `0` are irrational over `ℚ(q)`.**  The indicial
discriminant `q² − 6q + 5` is not a square in `ℚ[q]`, so the roots
`t = (−(q−1) ± √(q²−6q+5))/2` of the indicial equation are not rational functions
of `q`.

Proof by multiplicity, not degree parity (the degree is even, so parity is
silent): `f·f = p` forces `f(1)² = p(1) = 0`, hence `f(1) = 0`; differentiating,
`p' = f'·f + f·f'`, so `p'(1) = 0`.  But `p'(1) = −4`. -/
theorem not_isSquare_indicialDiscriminant :
    ¬ ∃ f : Polynomial ℚ, f * f = indicialDiscriminant := by
  rintro ⟨f, hf⟩
  -- `f` vanishes at `1`, because `p` does and `ℚ` is a domain.
  have hf1 : f.eval 1 = 0 := by
    have h : f.eval 1 * f.eval 1 = 0 := by
      rw [← eval_mul, hf, indicialDiscriminant_eval_one]
    exact mul_self_eq_zero.mp h
  -- Differentiating a square makes `p'(1)` vanish too.
  have hderiv : (derivative indicialDiscriminant).eval 1 = 0 := by
    rw [← hf, derivative_mul, eval_add, eval_mul, eval_mul, hf1]
    ring
  rw [indicialDiscriminant_derivative_eval_one] at hderiv
  norm_num at hderiv

/-- Restated in Mathlib's `IsSquare` form. -/
theorem not_isSquare_indicialDiscriminant' : ¬ IsSquare indicialDiscriminant := by
  rintro ⟨f, hf⟩
  exact not_isSquare_indicialDiscriminant ⟨f, hf.symm⟩

/-- **Both ends of C1 are quadratically irrational, for different reasons.**
Recorded together because the *contrast* is the point: at `0` the weights come
from an indicial equation and are computable by pure algebra; at `∞` they come
from Stokes data and are not.  That the two ends need different arguments
(multiplicity here, degree parity there) reflects that difference rather than
being an accident of the proofs. -/
theorem both_ends_irrational :
    ¬ IsSquare indicialDiscriminant ∧ ¬ IsSquare newtonEdgeConstant :=
  ⟨not_isSquare_indicialDiscriminant', not_isSquare_X_sub_one⟩

end QOU.QBeta
