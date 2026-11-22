import Mathlib.RingTheory.PowerSeries.Inverse
import Mathlib.Tactic

/-!
# Compact quantum dilogarithm — the genuine infinite object (bi-formal `R[[q]][[x]]`)

The analytic layer deferred by `QOU.MathlibExt.QuantumDilogarithm` (finite
`q`-Pochhammer backbone).  Target **T1**: treat both `q` and `x` as *formal*
variables, so the reciprocal quantum dilogarithm
$$\Phi_q(x)^{-1} \;=\; \prod_{n=0}^{\infty}\bigl(1 + q^{2n+1} x\bigr)$$
is an element of `R[[q]][[x]]` — a power series in `x` whose coefficients are
power series in `q`.  This is well-defined with **no analytic convergence**:
the `x^k` coefficient is the elementary symmetric series `e_k(q, q³, q⁵, …)`,
whose lowest `q`-term is `q^{k²}` and whose every `q`-power has finite
multiplicity.  (The naive analytic product *diverges* at the physical
`q₀ ≈ 1.11 > 1`; see `docs/workplans/2026-07-11-q-dilog-infinite-product.md`.)

We do **not** formalise the product via an infinite-`Multipliable` argument.
Instead we take the equivalent **`q`-difference characterisation**: Euler's
identity gives the coefficient recurrence
$$(1 - q^{2k})\,a_k \;=\; -\,q\,a_{k-1}, \qquad a_0 = 1,$$
each `1 - q^{2k}` being a *unit* in `R[[q]]` (constant term `1`).  We define
`Φ_q^{-1}` by this recurrence ([`qDilogInv`](#QOU.MathlibExt.QuantumDilogarithmInfinite.qDilogInv))
and prove the defining functional equation
`Φ_q(q²x)^{-1} = (1 + q x)·Φ_q(x)^{-1}` coefficient-wise
([`qDilogInv_functional`](#QOU.MathlibExt.QuantumDilogarithmInfinite.qDilogInv_functional)).

TODO upstream: `Mathlib.RingTheory.PowerSeries` — the `q`-Pochhammer /
`q`-exponential as a `PowerSeries` with its `q`-difference equation.
-- Ref: [faddeev1994] https://doi.org/10.1007/BF02101594 — Faddeev, the quantum dilogarithm.
-- Ref: [leitner2026] QOU.MathlibExt.QuantumDilogarithm (finite backbone; PR #3500)
-/

namespace QOU.MathlibExt.QuantumDilogarithmInfinite

open PowerSeries

variable {R : Type*} [CommRing R]

/-- The coefficient ring `R[[q]]`, with `q := X`. -/
abbrev QSeries (R : Type*) [CommRing R] := PowerSeries R

/-- `1 - q^{2k}` as an element of `R[[q]]`; a unit, since its constant term
is `1` (the `q^{2k}` term has no constant part for `k ≥ 1`). -/
noncomputable def oneSubQPow (k : ℕ) : QSeries R := 1 - X ^ (2 * k)

theorem constantCoeff_oneSubQPow_succ (k : ℕ) :
    constantCoeff (oneSubQPow (k + 1) : QSeries R) = 1 := by
  have h : 2 * (k + 1) ≠ 0 := by omega
  simp [oneSubQPow, map_sub, map_pow, constantCoeff_X, zero_pow h]

/-- The `x^k` coefficient of `Φ_q^{-1}`, an element of `R[[q]]`, defined by the
`q`-difference recurrence `a_{k+1} = -q · a_k · (1 - q^{2(k+1)})⁻¹`, `a_0 = 1`. -/
noncomputable def coeffSeq : ℕ → QSeries R
  | 0 => 1
  | (k + 1) => (-X) * coeffSeq k * invOfUnit (oneSubQPow (k + 1)) 1

@[simp] theorem coeffSeq_zero : (coeffSeq 0 : QSeries R) = 1 := rfl

/-- The genuine infinite reciprocal quantum dilogarithm `Φ_q^{-1} ∈ R[[q]][[x]]`. -/
noncomputable def qDilogInv : PowerSeries (QSeries R) := mk coeffSeq

@[simp] theorem coeff_qDilogInv (k : ℕ) :
    (coeff k) (qDilogInv : PowerSeries (QSeries R)) = coeffSeq k :=
  coeff_mk k coeffSeq

/-- **`q`-difference recurrence** (the defining relation), cleared of the
inverse: `(1 - q^{2(k+1)}) · a_{k+1} = -q · a_k`. -/
theorem oneSubQPow_mul_coeffSeq_succ (k : ℕ) :
    (oneSubQPow (k + 1) : QSeries R) * coeffSeq (k + 1) = (-X) * coeffSeq k := by
  have hu : constantCoeff (oneSubQPow (k + 1) : QSeries R) = ((1 : Rˣ) : R) := by
    simpa using constantCoeff_oneSubQPow_succ (R := R) k
  have hmul : (oneSubQPow (k + 1) : QSeries R) * invOfUnit (oneSubQPow (k + 1)) 1 = 1 :=
    mul_invOfUnit _ 1 hu
  rw [coeffSeq]
  calc (oneSubQPow (k + 1) : QSeries R)
          * ((-X) * coeffSeq k * invOfUnit (oneSubQPow (k + 1)) 1)
      = ((-X) * coeffSeq k)
          * ((oneSubQPow (k + 1) : QSeries R) * invOfUnit (oneSubQPow (k + 1)) 1) := by ring
    _ = (-X) * coeffSeq k := by rw [hmul, mul_one]

/-- **Functional equation** (the defining `q`-difference equation of the
compact quantum dilogarithm):
$$\Phi_q(q^2 x)^{-1} \;=\; (1 + q\,x)\,\Phi_q(x)^{-1},$$
here as `rescale (q²) Φ_q^{-1} = (1 + C q · X) · Φ_q^{-1}` in `R[[q]][[x]]`
(`q := (X : R[[q]])`, `x := (X : R[[q]][[x]])`). -/
theorem qDilogInv_functional :
    rescale (X ^ 2 : QSeries R) qDilogInv
      = (1 + C (X : QSeries R) * X) * qDilogInv := by
  ext1 k
  rw [coeff_rescale, coeff_qDilogInv, add_mul, one_mul, map_add, mul_assoc,
      coeff_C_mul, coeff_qDilogInv]
  cases k with
  | zero =>
      rw [coeff_zero_X_mul]
      simp [coeffSeq]
  | succ n =>
      rw [coeff_succ_X_mul, coeff_qDilogInv, ← pow_mul]
      have hrec := oneSubQPow_mul_coeffSeq_succ (R := R) n
      simp only [oneSubQPow, sub_mul, one_mul] at hrec
      linear_combination -hrec

end QOU.MathlibExt.QuantumDilogarithmInfinite
