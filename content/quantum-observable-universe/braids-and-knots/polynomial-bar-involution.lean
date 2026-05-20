/-!
# QOU.BraidKnot.PolynomialBarInvolution

**Non-trivial bar-involution on `Polynomial R`**: the bar map
sends `X ↦ -X` and fixes constants. Under this map:
- `X` is bar-anti-symmetric (`bar X = -X`)
- `X²` is bar-symmetric (`bar X² = X²`)
- Every even-degree monomial is bar-symmetric
- Every odd-degree monomial is bar-anti-symmetric

The bar-symmetric subring of `R[X]` is exactly `R[X²]`.

This file provides a **standalone non-trivial bar-involution
example** on the polynomial ring. The categorical content: under
this bar, the polynomial indeterminate `X` plays the role of the
Hecke skein `h = q - q⁻¹` with the correct bar-action `h ↔ -h`.

What's proved (all theorems below, no `sorry`):
- `barPoly_X`: `bar X = -X` (definitional)
- `barPoly_neg_X`: `bar (-X) = X` (involution closes)
- `barPoly_C`: `bar (C c) = C c` (bar fixes constants)
- `barPoly_add`: `bar (p + q) = bar p + bar q`
- `barPoly_mul`: `bar (p · q) = bar p · bar q`
- `barPoly_one`: `bar 1 = 1`
- `barPoly_zero`: `bar 0 = 0`
- `barPoly_involutive`: `bar (bar p) = p`
- `barPoly_X_pow_two`: `bar (X²) = X²` (concrete bar-symmetry on the
  squared indeterminate — the analogue of "h² is bar-symmetric")
-/

import Mathlib.Algebra.Polynomial.Eval.Defs
-- Ref: [manuscript] prop:bar-symmetric-three-layer-synthesis
-- Ref: [manuscript] def:bar-involution
-- Ref: [wenzl1988] doi:10.1007/BF01404457

namespace QOU.BraidKnot.PolynomialBarInvolution

open Polynomial

variable {R : Type*} [CommRing R]

/-- The bar map on `R[X]` sending `X ↦ -X`. Implemented as
    `p.comp (-X)` — substitute `-X` for the indeterminate. -/
noncomputable def barPoly (p : R[X]) : R[X] := p.comp (-X)

/-- `bar X = -X` by definition. -/
theorem barPoly_X : barPoly (X : R[X]) = -X := by
  unfold barPoly
  exact X_comp

/-- `bar (-X) = X`: the involution closes on the indeterminate. -/
theorem barPoly_neg_X : barPoly (-X : R[X]) = X := by
  unfold barPoly
  rw [neg_comp, X_comp, neg_neg]

/-- `bar` fixes constants `C c`. -/
theorem barPoly_C (c : R) : barPoly (C c) = C c := by
  unfold barPoly
  exact C_comp

/-- `bar` is **additive**: `bar (p + q) = bar p + bar q`. -/
theorem barPoly_add (p q : R[X]) : barPoly (p + q) = barPoly p + barPoly q := by
  unfold barPoly
  exact add_comp

/-- `bar` is **multiplicative**: `bar (p · q) = bar p · bar q`. -/
theorem barPoly_mul (p q : R[X]) : barPoly (p * q) = barPoly p * barPoly q := by
  unfold barPoly
  exact mul_comp

/-- `bar 1 = 1`. -/
theorem barPoly_one : barPoly (1 : R[X]) = 1 := by
  unfold barPoly
  exact one_comp

/-- `bar 0 = 0`. -/
theorem barPoly_zero : barPoly (0 : R[X]) = 0 := by
  unfold barPoly
  exact zero_comp

/-- **`bar` is involutive**: `bar (bar p) = p`.
    Proof: substituting `-X` for `X` and then again gives
    `-(-X) = X`, so we recover the identity composition. -/
theorem barPoly_involutive (p : R[X]) : barPoly (barPoly p) = p := by
  unfold barPoly
  rw [comp_assoc]
  congr 1
  rw [neg_comp, X_comp, neg_neg]

/-- **`bar X² = X²`** — the squared indeterminate is bar-symmetric.
    Concrete polynomial realisation of "anti × anti = sym". -/
theorem barPoly_X_pow_two : barPoly ((X : R[X]) ^ 2) = X ^ 2 := by
  rw [sq, barPoly_mul, barPoly_X]
  ring

/-- **`bar X^n = (-1)^n · X^n`** — natural-power bar action.
    Follows by induction on `n`: at the inductive step,
    `bar (X^(n+1)) = bar X · bar (X^n) = (-X) · (-1)^n · X^n = (-1)^(n+1) X^(n+1)`. -/
theorem barPoly_X_pow (n : ℕ) :
    barPoly ((X : R[X]) ^ n) = (-1 : R[X]) ^ n * X ^ n := by
  induction n with
  | zero => simp [barPoly_one]
  | succ k ih =>
    have hstep : (X : R[X]) ^ (k + 1) = X * X ^ k := by ring
    rw [hstep, barPoly_mul, barPoly_X, ih]
    ring

end QOU.BraidKnot.PolynomialBarInvolution
