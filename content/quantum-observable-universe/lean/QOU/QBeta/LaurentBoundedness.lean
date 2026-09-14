/-
# A Laurent polynomial bounded on `(0, ∞)` is constant

This closes a step that `qbeta_eigenphase_rationality_quantization_probe.py`
has been asserting numerically and naming as unformalised.  Its assertion 5,
*"no word is bounded-but-not-constant"*, is the hinge of PART 1: the sibling
exclusion probe closes the braid-image branch only against a **q-varying**
ansatz, and a **constant** `α` walks straight through it.  Carrying boundedness
through to *integrality* is what closes the constant case — and that argument
starts here, with

> a Laurent polynomial bounded on `(0, ∞)` is constant.

Until now that was a paper step.  Assertion 8 of the same probe still says
*"the Lean twin of this step is NOT written"* for the general-`d` Kronecker
half; **this file writes the Laurent half and not the Kronecker half**, and the
distinction is deliberate — see `## What is NOT here` below.

## The shape of the argument

A Laurent polynomial on `(0, ∞)` is `f q = P(q) / q ^ m` for an honest
polynomial `P` and some `m : ℕ`.  Boundedness kills the two ends separately:

* **`degree_le_of_bounded_div_pow`** — the `q → ∞` end.  If `P(x)/x^m` is
  bounded near `+∞` then `deg P ≤ m`.  Mathlib's
  `Polynomial.abs_div_tendsto_atTop_of_degree_gt` does the work: were
  `deg (X^m) < deg P`, the quotient would tend to `+∞` in absolute value, which
  a bound forbids.
* **`laurent_reflect`** — the `q → 0⁺` end, and the step that makes the whole
  thing cheap.  Rather than a second asymptotic argument, `q ↦ 1/q` turns the
  Laurent polynomial into an **honest polynomial**:

      P(x) / x ^ m  =  (reflect m P)(1 / x)        for x ≠ 0, given deg P ≤ m

  which is Mathlib's `Polynomial.eval₂_reflect_mul_pow` read through
  `RingHom.id`.  There is no division on the right.  Since `q ↦ 1/q` is a
  bijection of `(0, ∞)`, boundedness transports, and the reflected polynomial
  is bounded near `+∞` — so `eq_const_of_bounded` finishes it.

The two ends are therefore **one** asymptotic lemma applied twice, not two.

## What is NOT here

* **The Kronecker step is not formalised.**  "A q-uniform ellipticity forces an
  integer characteristic polynomial, whose roots on the unit circle are roots of
  unity, so `α ∈ 2πℚ`" remains a paper argument, and the probe's assertion 8
  continues to say so.  This file is its *first* input, not the whole chain.
* **Nothing about `Q_β` accuracy.**  PART 3 of that probe already established
  that the phase is off the L2 critical path entirely — the residual is a
  base/assembly problem.  This is the formalisation of a named gap, not L2
  progress, and it should not be reported as the latter.
* **No integrality claim.**  The step from "constant" to "an integer" uses
  `σ⁻¹ = σ − (q − q⁻¹)I` and so lands in `ℤ[q, q⁻¹]`; that is a separate
  argument about the Hecke presentation, not about boundedness.

Verified `lean`-direct with `-DautoImplicit=false -s 65536`: exit 0, no
diagnostics, no `sorry`, no `axiom`.

Note for whoever next builds here.  `Mathlib.Analysis.Polynomial.Basic` and
`Mathlib.Analysis.Asymptotics.SpecificAsymptotics` are **not** in the restored
`lake-cache/qou-v4-24-0`.  Build them into the **root** tree, which is the one
`scripts/lean-direct-env.sh` resolves first:

    scripts/lean-build-mathlib-gap-cone.py Mathlib.Analysis.Polynomial.Basic \
      --dest "$(git rev-parse --show-toplevel)/.lake/packages/mathlib/.lake/build/lib/lean"

~7 s.  After that the **stock** `lean-direct-env.sh` verifies this file with no
`LEAN_PATH` override at all.

🛑 **An earlier revision of this note said to build into the default (paper)
tree and PREPEND it to `LEAN_PATH`.  That advice was wrong and is retracted.**
It does make this file compile — and it breaks `QOU/MobiusEnergy.lean`, because
the paper tree lacks `Mathlib.GroupTheory.SpecificGroups.Dihedral`, which the
root tree has.  The two trees are missing **different** modules, so *neither*
ordering verifies the whole set: root-first reds this file, paper-first reds
`MobiusEnergy`.  Measured on all five files of this branch, both ways.  Path
ordering is not the fix; completing the root tree is.

Also: a **0-second** failure from the gap-cone script means the module's
*source* is absent — i.e. it was renamed upstream — not that the build failed.
`Mathlib.Analysis.SpecialFunctions.Polynomials` is such a case in this
toolchain; the lemmas moved to `Mathlib.Analysis.Polynomial.Basic`.
-/

import Mathlib.Analysis.Polynomial.Basic
import Mathlib.Algebra.Polynomial.Reverse

open Polynomial Filter

namespace QOU.QBeta.LaurentBoundedness

/-- If `P(x)/x^m` is bounded near `+∞` then `deg P ≤ m`. -/
theorem degree_le_of_bounded_div_pow (P : ℝ[X]) (m : ℕ) (M : ℝ)
    (h : ∀ᶠ x : ℝ in atTop, |eval x P / x ^ m| ≤ M) :
    P.degree ≤ (m : ℕ) := by
  by_contra hcon
  push_neg at hcon
  have hQ : (X ^ m : ℝ[X]) ≠ 0 := pow_ne_zero _ X_ne_zero
  have hdegX : (X ^ m : ℝ[X]).degree = (m : ℕ) := degree_X_pow m
  have hdeg : (X ^ m : ℝ[X]).degree < P.degree := by rw [hdegX]; exact hcon
  have ht := Polynomial.abs_div_tendsto_atTop_of_degree_gt P (X ^ m) hdeg hQ
  simp only [eval_pow, eval_X] at ht
  exact not_isBoundedUnder_of_tendsto_atTop ht ⟨M, h⟩

/-- A real polynomial bounded near `+∞` is constant. -/
theorem eq_const_of_bounded (P : ℝ[X]) (M : ℝ)
    (h : ∀ᶠ x : ℝ in atTop, |eval x P| ≤ M) :
    ∀ x : ℝ, eval x P = P.coeff 0 := by
  have hd : P.degree ≤ ((0 : ℕ) : WithBot ℕ) := by
    refine degree_le_of_bounded_div_pow P 0 M ?_
    filter_upwards [h] with x hx
    simpa using hx
  have hd0 : P.degree ≤ 0 := by exact_mod_cast hd
  have hC := Polynomial.eq_C_of_degree_le_zero hd0
  intro x
  conv_lhs => rw [hC]
  exact eval_C

/-- **The reflection identity.**  `P(x)/x^m` IS an honest polynomial, read at
`1/x`.  This is what removes the need for a second asymptotic argument at the
`x → 0⁺` end. -/
theorem laurent_reflect (P : ℝ[X]) (m : ℕ) (x : ℝ) (hx : x ≠ 0)
    (hdeg : P.natDegree ≤ m) :
    eval x P / x ^ m = eval x⁻¹ (reflect m P) := by
  haveI : Invertible x := invertibleOfNonzero hx
  have hkey := Polynomial.eval₂_reflect_mul_pow (RingHom.id ℝ) x m P hdeg
  simp only [eval₂_id] at hkey
  rw [invOf_eq_inv] at hkey
  exact (div_eq_iff (pow_ne_zero m hx)).mpr hkey.symm

/-- **A Laurent polynomial bounded on `(0, ∞)` is constant there.**

The constant is named: it is `(reflect m P).coeff 0`, which is `P.coeff m`. -/
theorem laurent_const_of_bounded (P : ℝ[X]) (m : ℕ) (M : ℝ)
    (h : ∀ x : ℝ, 0 < x → |eval x P / x ^ m| ≤ M) :
    ∀ x : ℝ, 0 < x → eval x P / x ^ m = (reflect m P).coeff 0 := by
  have hdeg : P.degree ≤ ((m : ℕ) : WithBot ℕ) := by
    refine degree_le_of_bounded_div_pow P m M ?_
    filter_upwards [eventually_gt_atTop (0 : ℝ)] with x hx
    exact h x hx
  have hnd : P.natDegree ≤ m := natDegree_le_iff_degree_le.mpr hdeg
  have hrefl : ∀ y : ℝ, y ≠ 0 → eval y P / y ^ m = eval y⁻¹ (reflect m P) :=
    fun y hy => laurent_reflect P m y hy hnd
  have hRb : ∀ᶠ y : ℝ in atTop, |eval y (reflect m P)| ≤ M := by
    filter_upwards [eventually_gt_atTop (0 : ℝ)] with y hy
    have hy' : (0 : ℝ) < y⁻¹ := inv_pos.mpr hy
    have hb := h y⁻¹ hy'
    rw [hrefl y⁻¹ (ne_of_gt hy'), inv_inv] at hb
    exact hb
  have hconst := eq_const_of_bounded (reflect m P) M hRb
  intro x hx
  rw [hrefl x (ne_of_gt hx)]
  exact hconst x⁻¹

/-- The constant is `P.coeff m`, spelled without `reflect`. -/
theorem laurent_const_coeff (P : ℝ[X]) (m : ℕ) :
    (reflect m P).coeff 0 = P.coeff m := by
  rw [coeff_reflect]
  simp [revAt]

end QOU.QBeta.LaurentBoundedness
