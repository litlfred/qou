import Mathlib.Algebra.Polynomial.Eval.Defs

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
    rw [pow_succ, barPoly_mul, ih, barPoly_X]
    ring

/-- **`bar X^(2n) = X^(2n)`** — even powers of the indeterminate
    are bar-symmetric. Concrete polynomial realisation of the
    bar-grading "anti × anti × ... = sym" identity. -/
theorem barPoly_X_pow_even (n : ℕ) :
    barPoly ((X : R[X]) ^ (2 * n)) = X ^ (2 * n) := by
  rw [barPoly_X_pow]
  have h_neg_one_sq : ((-1 : R[X])) ^ (2 * n) = 1 := by
    rw [pow_mul, neg_one_sq, one_pow]
  rw [h_neg_one_sq, one_mul]

/-- **`bar X^(2n+1) = -X^(2n+1)`** — odd powers are bar-anti-symmetric. -/
theorem barPoly_X_pow_odd (n : ℕ) :
    barPoly ((X : R[X]) ^ (2 * n + 1)) = -(X ^ (2 * n + 1)) := by
  rw [barPoly_X_pow]
  have h_neg_one_odd : ((-1 : R[X])) ^ (2 * n + 1) = -1 := by
    rw [pow_succ, pow_mul, neg_one_sq, one_pow, one_mul]
  rw [h_neg_one_odd]
  ring

/-- **`bar` fixes every natural-number scalar in `R[X]`**. -/
theorem barPoly_natCast (n : ℕ) :
    barPoly ((n : R[X])) = (n : R[X]) := by
  induction n with
  | zero =>
    show barPoly (0 : R[X]) = 0
    exact barPoly_zero
  | succ k ih =>
    have hstep : ((k + 1 : ℕ) : R[X]) = (k : R[X]) + 1 := by push_cast; ring
    rw [hstep, barPoly_add, barPoly_one, ih]

/-- **`bar (4 + X²) = 4 + X²`** — the polynomial $h^2 + 4$ (the
    `c5` denominator in `c5_as_function_of_skein`) is bar-symmetric.
    Concrete polynomial realisation of "the c_5 denominator lives
    in the bar-symmetric subring $R[X^2]$". -/
theorem barPoly_c5_denominator :
    barPoly ((4 : R[X]) + X ^ 2) = 4 + X ^ 2 := by
  rw [barPoly_add]
  congr 1
  · -- bar 4 = 4
    show barPoly ((4 : R[X])) = 4
    have h4 : (4 : R[X]) = ((4 : ℕ) : R[X]) := by push_cast; ring
    rw [h4, barPoly_natCast]
  · exact barPoly_X_pow_two

/-- **`bar` distributes over subtraction**: `bar (p - q) = bar p - bar q`.
    Follows from `bar` being a ring homomorphism (`add` + `bar` of `-1`). -/
theorem barPoly_sub (p q : R[X]) :
    barPoly (p - q) = barPoly p - barPoly q := by
  have hsub : p - q = p + (-1) * q := by ring
  have hsub_rhs : barPoly p - barPoly q = barPoly p + (-1) * barPoly q := by ring
  rw [hsub, barPoly_add, barPoly_mul]
  -- bar (-1) = -1
  have h_neg_one : barPoly ((-1 : R[X])) = -1 := by
    have : (-1 : R[X]) = -((1 : R[X])) := by ring
    rw [this]
    -- bar (-1) = bar (- C 1) = ?
    -- Use barPoly p in terms of comp: bar (-1) = (-1).comp(-X) = -1
    unfold barPoly
    rw [neg_comp, one_comp]
  rw [h_neg_one, hsub_rhs]

/-- **`bar` distributes over negation**: `bar (-p) = -(bar p)`. -/
theorem barPoly_neg (p : R[X]) : barPoly (-p) = -(barPoly p) := by
  have : -p = 0 - p := by ring
  rw [this, barPoly_sub, barPoly_zero]
  ring

end QOU.BraidKnot.PolynomialBarInvolution
/-! ## Arbitrary-degree even-polynomial bar-symmetry

The bar-symmetry of `c5_taylor_6`, `cos_truncated_6`,
`cosh_truncated_6` are special cases of a generic theorem:
**any finite sum of bar-symmetric coefficients times even powers
of X is bar-symmetric**. This handles arbitrary truncation degree.
-/

namespace QOU.BraidKnot.PolynomialBarInvolution.Arbitrary

open Polynomial QOU.BraidKnot.PolynomialBarInvolution

variable {R : Type*} [CommRing R]

/-- **Arbitrary even-power truncation is bar-symmetric**:

    For any natural-number coefficient sequence `c : ℕ → R` and
    any truncation degree `n`, the polynomial

    $$P_n(X) \;=\; \sum_{k=0}^{n-1} c_k \, X^{2k}$$

    is bar-symmetric.

    Proof: induction on `n`. Base case: empty sum = 0 is bar-sym.
    Inductive step: a new term `c_k · X^(2k)` is bar-sym (constant
    bar-fixed × even-power X bar-fixed), so adding to a bar-sym
    sum preserves bar-symmetry.

    This generalises all three concrete avatar polynomials
    (`c5_taylor_6`, `cos_truncated_6`, `cosh_truncated_6`) to
    truncations of arbitrary degree. -/
theorem barPoly_even_truncated_arbitrary
    (n : ℕ) (c : ℕ → R) :
    barPoly (∑ k ∈ Finset.range n, C (c k) * X ^ (2 * k))
      = ∑ k ∈ Finset.range n, C (c k) * X ^ (2 * k) := by
  induction n with
  | zero => simp [barPoly_zero]
  | succ m ih =>
    rw [Finset.sum_range_succ, barPoly_add, barPoly_mul,
        barPoly_C, barPoly_X_pow_even, ih]

/-- **Generic bar-symmetric finite even-power polynomial**:
    `bar (∑ c_k · X^(2k)) = ∑ c_k · X^(2k)` over any Finset index. -/
theorem barPoly_even_finset_sum
    {ι : Type*} (s : Finset ι) (c : ι → R) (k : ι → ℕ) :
    barPoly (∑ i ∈ s, C (c i) * X ^ (2 * k i))
      = ∑ i ∈ s, C (c i) * X ^ (2 * k i) := by
  induction s using Finset.induction with
  | empty => simp [barPoly_zero]
  | insert hi ih =>
    rw [Finset.sum_insert hi, barPoly_add, barPoly_mul,
        barPoly_C, barPoly_X_pow_even, ih]

/-- **Constant-plus-even-truncation is bar-symmetric**: a more
    convenient form for c_5-like polynomials where the constant
    term has its own coefficient. -/
theorem barPoly_constant_plus_even
    (c0 : R) (n : ℕ) (c : ℕ → R) :
    barPoly (C c0 + ∑ k ∈ Finset.range n, C (c k) * X ^ (2 * (k + 1)))
      = C c0 + ∑ k ∈ Finset.range n, C (c k) * X ^ (2 * (k + 1)) := by
  rw [barPoly_add, barPoly_C]
  congr 1
  induction n with
  | zero => simp [barPoly_zero]
  | succ m ih =>
    rw [Finset.sum_range_succ, barPoly_add, barPoly_mul,
        barPoly_C, barPoly_X_pow_even, ih]

end QOU.BraidKnot.PolynomialBarInvolution.Arbitrary

/-! ## Odd-power version (for completeness)

The bar-anti-symmetric analog: **any finite sum of bar-symmetric
coefficients times ODD powers of X is bar-anti-symmetric**.
-/

namespace QOU.BraidKnot.PolynomialBarInvolution.ArbitraryOdd

open Polynomial QOU.BraidKnot.PolynomialBarInvolution

variable {R : Type*} [CommRing R]

/-- **Arbitrary odd-power truncation is bar-anti-symmetric**:

    For any `c : ℕ → R` and truncation degree `n`,
    $\sum_{k=0}^{n-1} c_k \, X^{2k+1}$
    is bar-anti-symmetric (bar maps it to its negation). -/
theorem barPoly_odd_truncated_arbitrary
    (n : ℕ) (c : ℕ → R) :
    barPoly (∑ k ∈ Finset.range n, C (c k) * X ^ (2 * k + 1))
      = -(∑ k ∈ Finset.range n, C (c k) * X ^ (2 * k + 1)) := by
  induction n with
  | zero => simp [barPoly_zero]
  | succ m ih =>
    rw [Finset.sum_range_succ, barPoly_add, barPoly_mul,
        barPoly_C, barPoly_X_pow_odd, ih]
    ring

end QOU.BraidKnot.PolynomialBarInvolution.ArbitraryOdd

/-! ## Pre-archimedean generic versions (over `CommRing R`)

Per AGENTS.md §7c (Base ring convention), the bar-symmetry of
even-power polynomial truncations is **algebraic**, not analytic
— it holds over any commutative ring `R`, no `Field`/`ℝ` needed.
This section provides the **pre-archimedean generic** versions of
`c5_taylor_6`, `cos_truncated_6`, `cosh_truncated_6` parameterized
by arbitrary coefficients in `R`. The archimedean specialisations
(over `ℝ` with specific numerical coefficients) become instances.
-/

namespace QOU.BraidKnot.PolynomialBarInvolution.Generic

open Polynomial QOU.BraidKnot.PolynomialBarInvolution

variable {R : Type*} [CommRing R]

/-- **Generic degree-6 even-polynomial** in `R[X]`:
    $P(X) = c_0 + c_1 X^2 + c_2 X^4 + c_3 X^6$
    for arbitrary coefficients $c_0, c_1, c_2, c_3 \in R$. -/
noncomputable def evenPoly_6 (c0 c1 c2 c3 : R) : R[X] :=
  C c0 + C c1 * X ^ 2 + C c2 * X ^ 4 + C c3 * X ^ 6

/-- **Generic `evenPoly_6` is bar-symmetric** over any `CommRing R`,
    no field structure needed. -/
theorem barPoly_evenPoly_6 (c0 c1 c2 c3 : R) :
    barPoly (evenPoly_6 c0 c1 c2 c3) = evenPoly_6 c0 c1 c2 c3 := by
  unfold evenPoly_6
  rw [barPoly_add, barPoly_add, barPoly_add,
      barPoly_C, barPoly_mul, barPoly_C, barPoly_mul,
      barPoly_C, barPoly_mul, barPoly_C, barPoly_X_pow_two]
  have hX4 : barPoly ((X : R[X]) ^ 4) = X ^ 4 := by
    have : (4 : ℕ) = 2 * 2 := by decide
    rw [this]; exact barPoly_X_pow_even 2
  have hX6 : barPoly ((X : R[X]) ^ 6) = X ^ 6 := by
    have : (6 : ℕ) = 2 * 3 := by decide
    rw [this]; exact barPoly_X_pow_even 3
  rw [hX4, hX6]

/-- **Generic degree-8 even-polynomial** in `R[X]`. -/
noncomputable def evenPoly_8 (c0 c1 c2 c3 c4 : R) : R[X] :=
  evenPoly_6 c0 c1 c2 c3 + C c4 * X ^ 8

theorem barPoly_evenPoly_8 (c0 c1 c2 c3 c4 : R) :
    barPoly (evenPoly_8 c0 c1 c2 c3 c4) = evenPoly_8 c0 c1 c2 c3 c4 := by
  unfold evenPoly_8
  rw [barPoly_add, barPoly_mul, barPoly_C, barPoly_evenPoly_6]
  have hX8 : barPoly ((X : R[X]) ^ 8) = X ^ 8 := by
    have : (8 : ℕ) = 2 * 4 := by decide
    rw [this]; exact barPoly_X_pow_even 4
  rw [hX8]

/-- **Generic arbitrary-degree even-polynomial truncation is bar-symmetric**
    — over any `CommRing R`. Combines `Arbitrary.barPoly_even_truncated_arbitrary`
    with the pre-archimedean naming convention. The same theorem, restated
    here for the §7c discipline: nothing about this requires `ℝ`. -/
theorem barPoly_even_truncated_pre_archimedean
    (n : ℕ) (c : ℕ → R) :
    barPoly (∑ k ∈ Finset.range n, C (c k) * X ^ (2 * k))
      = ∑ k ∈ Finset.range n, C (c k) * X ^ (2 * k) :=
  Arbitrary.barPoly_even_truncated_arbitrary n c

end QOU.BraidKnot.PolynomialBarInvolution.Generic
