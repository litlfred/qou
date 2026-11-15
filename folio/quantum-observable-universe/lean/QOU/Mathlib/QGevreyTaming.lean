/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Gevrey taming: the q-native counterpart of the Gevrey-2 taming lemma

[`AlienDerivation.lean`](AlienDerivation.lean) proves the CLASSICAL taming step —
`abs_doubleBorelCoeff_le_of_gevrey2`: if `|aₙ| ≤ C·Aⁿ·(n!)²` then dividing by
`(n!)²` leaves geometrically bounded coefficients. That is the Gevrey-`s` world,
where divergence is measured by factorials.

**q-difference equations diverge differently.** Their formal solutions grow like
`q^{(quadratic in n)}`, not like a power of `n!`. Concretely, the C1 module's
`∞`-side coefficients satisfy `deg_q(cₙ) = n²` — proved for all `n` in
[`QOU/QBeta/C1InfDegreeLaw.lean`](../QBeta/C1InfDegreeLaw.lean) — so the divisor
that tames them is a power of `q`, not a factorial. The existing lemma does not
apply, and no q-native version existed.

This file supplies it, in two forms:

* `abs_qBorel_le_of_qGevrey` — the concrete `q^{n²}` case, matching `deg_q(cₙ) = n²`;
* `abs_qBorelCoeff_le_of_growth` — the general form, dividing by `q^{e n}` for an
  arbitrary exponent sequence `e`, so it composes with the level-`d` kernel
  exponents of [`QBorelKernelLevel.lean`](QBorelKernelLevel.lean) (`qBorelExp d`)
  or with any other q-Borel kernel.

**Scope.** This is the *formal-coefficient* taming step only: it says the divided
coefficients are geometrically bounded, which is what makes the transformed series
converge. It does **not** construct a q-Borel/Laplace summation, does not produce
an alien derivative, and computes no Stokes constant.

**No level is asserted for C1 here.** An earlier reading of RSZ §3.3 attached a
"level `d = 2`" to C1's `∞`; that reading is withdrawn — §3.3 is restricted to
integral slopes and its `d` is a slope *difference*, and C1 is pure isoclinic at
`∞`. See [`2026-08-08-rsz-c1-infinity-route-closed.md`](../../../../../docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md).
The general lemma below is deliberately parameterised by the exponent sequence so
that it carries no such claim.

§7c: `ℝ`-valued (an ordered field is needed for the absolute-value estimate).
Sorry-free.

-- Ref: [ecalle1981] Fonctions résurgentes, tome I
-- Ref: [sauzin2014] https://arxiv.org/abs/1405.0356
-- Ref: [leitner2026] docs/audits/2026-08-08-rsz-c1-infinity-route-closed.md
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Algebra.Order.Field.Basic

namespace QOU.Mathlib.QGevreyTaming

/-- The q-Borel coefficient for a general exponent sequence `e`: `aₙ / q^{e n}`.

Taking `e n = n²` gives the divisor matching `deg_q(cₙ) = n²`; taking
`e = qBorelExp d` gives the RSZ level-`d` kernel. -/
noncomputable def qBorelCoeff (q : ℝ) (e : ℕ → ℕ) (a : ℕ → ℝ) (n : ℕ) : ℝ :=
  a n / q ^ (e n)

/-- **q-Gevrey taming, general exponent.** If the coefficients are dominated by
`C·Aⁿ·q^{e n}`, then dividing by `q^{e n}` leaves them geometrically bounded.

This is the q-native counterpart of `abs_doubleBorelCoeff_le_of_gevrey2`: there the
divisor is `(n!)²`, here it is a power of `q`. -/
theorem abs_qBorelCoeff_le_of_growth {q : ℝ} (hq : 0 < q) {e : ℕ → ℕ}
    {a : ℕ → ℝ} {C A : ℝ}
    (h : ∀ n, |a n| ≤ C * A ^ n * q ^ (e n)) (n : ℕ) :
    |qBorelCoeff q e a n| ≤ C * A ^ n := by
  have hpow : (0 : ℝ) < q ^ (e n) := by positivity
  unfold qBorelCoeff
  rw [abs_div, abs_of_pos hpow, div_le_iff₀ hpow]
  exact h n

/-- **q-Gevrey taming at the `n²` order** — the case matching the proved
`deg_q(cₙ) = n²` growth of the C1 `∞`-side coefficients. -/
theorem abs_qBorel_le_of_qGevrey {q : ℝ} (hq : 0 < q) {a : ℕ → ℝ} {C A : ℝ}
    (h : ∀ n, |a n| ≤ C * A ^ n * q ^ (n * n)) (n : ℕ) :
    |qBorelCoeff q (fun k => k * k) a n| ≤ C * A ^ n :=
  abs_qBorelCoeff_le_of_growth hq h n

/-- The q-Borel coefficient is additive, like its classical counterpart. -/
theorem qBorelCoeff_add (q : ℝ) (e : ℕ → ℕ) (a b : ℕ → ℝ) (n : ℕ) :
    qBorelCoeff q e (fun k => a k + b k) n
      = qBorelCoeff q e a n + qBorelCoeff q e b n := by
  unfold qBorelCoeff; rw [add_div]

/-- Composing two q-Borel divisions adds their exponents — the q-analogue of
`borelCoeff_compose` (there, applying the single-Borel divisor twice gives the
double-Borel divisor; here the exponents add rather than the factorials squaring).
This is the formal-series face of q-acceleration transitivity. -/
theorem qBorelCoeff_compose (q : ℝ) (e f : ℕ → ℕ) (a : ℕ → ℝ) (n : ℕ) :
    qBorelCoeff q f (qBorelCoeff q e a) n = qBorelCoeff q (fun k => e k + f k) a n := by
  unfold qBorelCoeff
  rw [pow_add, div_div]

/-- **The q-Borel transform intertwines the two dilations.**  Dilating the
    argument by `q` multiplies the `n`-th coefficient by `qⁿ`; the transform
    divides by a kernel that does not depend on the coefficients, so the
    transformed sequence is dilated in exactly the same way:

    `B(qⁿ·aₙ) = qⁿ · B(aₙ)`.

    This is the reason the dilation on `x` induces a dilation on the **Borel**
    variable, hence why a Borel-plane singularity at `ω` moves to `qω` — the
    `shift` field of `QAlienBridge.TwistedQBridgeSystem`, and in turn why the
    index set of the q-bridge has to be the spiral quotient `E_q = ℂ*/q^ℤ` rather
    than `ℂ*`.  Recorded here as a lemma rather than left as prose in that file:
    it is the one step of that argument that is a computation. -/
theorem qBorelCoeff_dilate (q : ℝ) (e : ℕ → ℕ) (a : ℕ → ℝ) (n : ℕ) :
    qBorelCoeff q e (fun k => q ^ k * a k) n = q ^ n * qBorelCoeff q e a n := by
  unfold qBorelCoeff
  rw [mul_div_assoc]

/-- **Why the classical lemma does not cover this.** The two divisors are genuinely
different functions of `n`: at `n = 3` the Gevrey-2 divisor `(n!)²` is `36`, while
the q-Gevrey divisor `q^{n²}` at `q = 2` is `2⁹ = 512`. Recorded as a concrete
witness that `QGevreyTaming` is not a restatement of `abs_doubleBorelCoeff_le_of_gevrey2`. -/
example : (3 : ℕ).factorial * (3 : ℕ).factorial = 36 := by decide

example : (2 : ℕ) ^ (3 * 3) = 512 := by decide

end QOU.Mathlib.QGevreyTaming
