import Mathlib.AlgebraicGeometry.EllipticCurve.Weierstrass
import Mathlib.RingTheory.PowerSeries.Basic
import Mathlib.NumberTheory.Divisors
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Tactic

/-!
# The Tate curve over `ℤ[[q]]` and its cusp (epic `08a2`, milestone M1)

The period map `Φ : q ↦ H¹(E_{τ(q)})` of epic `08a2` is the q-expansion of an elliptic family.
Its algebraic model is the Tate curve, a Weierstrass curve over the power-series ring `ℤ[[q]]`.
Nothing in this file uses `ℝ`, `ℂ`, `π` or `exp`: the coefficients are divisor sums.

  `E_q : y² + xy = x³ + a₄(q) x + a₆(q)`,
  `a₄ = −5 Σ σ₃(n) qⁿ`,   `a₆ = −Σ (5σ₃(n) + 7σ₅(n))/12 · qⁿ`.

Proved here, sorry-free:

* `twelve_dvd` — `12 ∣ 5d³ + 7d⁵` for every integer `d`, so `a₆ ∈ ℤ[[q]]`.
* `tate_c₄` — `c₄(E_q) = 1 + 240 Σ σ₃(n) qⁿ`, the Eisenstein series `E₄` as a divisor sum.
* `tate_c₆` — `c₆(E_q) = −(1 − 504 Σ σ₅(n) qⁿ)`, minus the divisor-sum `E₆`.
* `tate_Δ_factor`, `tate_Δ_coeff_zero`, `tate_Δ_coeff_one` — `Δ(E_q) = q·(1 + q·R)`. The nome `q`
  is a uniformizer of the discriminant: the family degenerates exactly to first order at `q = 0`.
* `cusp_fibre` — at `q = 0` the curve is the nodal cubic `y² + xy = x³`, with `Δ = 0`.
* `cusp_param`, `cusp_invariant_differential` — the nodal fibre is parametrized by the
  multiplicative group: `t ↦ (t/(1−t)², t²/(1−t)³)`, and the invariant differential
  `dx/(2y + x)` pulls back to `dt/t`, the invariant differential of `𝔾ₘ`.

**What this is for.** The last item is the algebraic half of the statement that the period of
`Φ` on the vanishing cycle is the period of `𝔾ₘ` (`∮ dt/t`). That period, `2πi`, is analytic and
belongs in `QOU/Transcendental/`; here only the algebraic identity `ω ↦ dt/t` is proved. The
link `𝔾ₘ` ↔ the formal-group law `QOU.FormalGroups.multiplicative` is milestone M3.

**What this is not.** It does not construct `Φ` from the categorical side. It does not identify
the Hecke parameter with the Tate nome (that identification is milestone M4 and needs the
owner's ruling: it is a core definition). It proves nothing about `μ₁`.
The product formula `Δ = q ∏ (1 − qⁿ)²⁴` is not proved here.

-- Ref: [leitner2026] Ch. mass-theory, per-loop measure (R2 / Φ, epic 08a2)
-/

set_option autoImplicit false

namespace QOU.GaussManin
namespace TateCurveCusp

open PowerSeries

noncomputable section

/-- Coefficients of an integer multiple. -/
theorem coeff_intCast_mul (k : ℤ) (f : PowerSeries ℤ) (n : ℕ) :
    coeff n ((k : PowerSeries ℤ) * f) = k * coeff n f := by
  rw [← map_intCast (PowerSeries.C (R := ℤ)) k, PowerSeries.coeff_C_mul]; simp

/-! ## Integrality of `a₆` -/

/-- `12 ∣ 5d³ + 7d⁵` for every integer `d`. -/
theorem twelve_dvd (d : ℤ) : (12 : ℤ) ∣ 5 * d ^ 3 + 7 * d ^ 5 := by
  have h3 : (3 : ℤ) ∣ 5 * d ^ 3 + 7 * d ^ 5 := by
    have : d % 3 = 0 ∨ d % 3 = 1 ∨ d % 3 = 2 := by omega
    rcases this with h | h | h <;>
      simp [Int.dvd_iff_emod_eq_zero, Int.add_emod, Int.mul_emod, pow_succ, h]
  have h4 : (4 : ℤ) ∣ 5 * d ^ 3 + 7 * d ^ 5 := by
    have : d % 4 = 0 ∨ d % 4 = 1 ∨ d % 4 = 2 ∨ d % 4 = 3 := by omega
    rcases this with h | h | h | h <;>
      simp [Int.dvd_iff_emod_eq_zero, Int.add_emod, Int.mul_emod, pow_succ, h]
  have : IsCoprime (3 : ℤ) 4 := by
    rw [Int.isCoprime_iff_gcd_eq_one]; rfl
  simpa using this.mul_dvd h3 h4

/-! ## The coefficients -/

/-- `σ₃(n)` as an integer (`0` at `n = 0`). -/
def s3 (n : ℕ) : ℤ := ∑ d ∈ n.divisors, (d : ℤ) ^ 3

/-- `σ₅(n)` as an integer (`0` at `n = 0`). -/
def s5 (n : ℕ) : ℤ := ∑ d ∈ n.divisors, (d : ℤ) ^ 5

/-- The `qⁿ` coefficient of `a₆`: `−Σ_{d ∣ n} (5d³ + 7d⁵)/12`, each term an integer. -/
def c6coeff (n : ℕ) : ℤ := -∑ d ∈ n.divisors, (5 * (d : ℤ) ^ 3 + 7 * (d : ℤ) ^ 5) / 12

theorem twelve_mul_c6coeff (n : ℕ) : 12 * c6coeff n = -(5 * s3 n + 7 * s5 n) := by
  unfold c6coeff s3 s5
  rw [mul_neg, Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib]
  congr 1
  refine Finset.sum_congr rfl fun d _ => ?_
  rw [Int.mul_ediv_cancel' (twelve_dvd d)]

@[simp] theorem s3_zero : s3 0 = 0 := by simp [s3]
@[simp] theorem s5_zero : s5 0 = 0 := by simp [s5]
@[simp] theorem c6coeff_zero : c6coeff 0 = 0 := by simp [c6coeff]
theorem c6coeff_one : c6coeff 1 = -1 := by simp [c6coeff]
theorem s3_one : s3 1 = 1 := by simp [s3]

/-- `a₄(q) = −5 Σ σ₃(n) qⁿ`. -/
def a4 : PowerSeries ℤ := PowerSeries.mk fun n => -5 * s3 n

/-- `a₆(q) = −Σ (5σ₃(n) + 7σ₅(n))/12 · qⁿ`. -/
def a6 : PowerSeries ℤ := PowerSeries.mk c6coeff

/-- The Tate curve `y² + xy = x³ + a₄ x + a₆` over `ℤ[[q]]`. -/
def tateCurve : WeierstrassCurve (PowerSeries ℤ) where
  a₁ := 1
  a₂ := 0
  a₃ := 0
  a₄ := a4
  a₆ := a6

/-- The divisor-sum Eisenstein series `E₄ = 1 + 240 Σ σ₃(n) qⁿ`. -/
def E4 : PowerSeries ℤ := PowerSeries.mk fun n => if n = 0 then 1 else 240 * s3 n

/-- The divisor-sum Eisenstein series `E₆ = 1 − 504 Σ σ₅(n) qⁿ`. -/
def E6 : PowerSeries ℤ := PowerSeries.mk fun n => if n = 0 then 1 else -504 * s5 n

/-! ## `c₄ = E₄`, `c₆ = −E₆` -/

theorem tate_c₄ : tateCurve.c₄ = E4 := by
  have h : tateCurve.c₄ = 1 - ((48 : ℤ) : PowerSeries ℤ) * a4 := by
    simp only [WeierstrassCurve.c₄, WeierstrassCurve.b₂, WeierstrassCurve.b₄, tateCurve]
    push_cast; ring
  rw [h]
  ext n
  rw [map_sub, coeff_intCast_mul]
  rcases n with _ | n
  · simp [E4, a4]
  · simp [E4, a4, PowerSeries.coeff_one]
    ring

theorem tate_c₆ : tateCurve.c₆ = -E6 := by
  have h : tateCurve.c₆ =
      -1 + ((72 : ℤ) : PowerSeries ℤ) * a4 - ((864 : ℤ) : PowerSeries ℤ) * a6 := by
    simp only [WeierstrassCurve.c₆, WeierstrassCurve.b₂, WeierstrassCurve.b₄,
      WeierstrassCurve.b₆, tateCurve]
    push_cast; ring
  rw [h]
  ext n
  rw [map_sub, map_add, coeff_intCast_mul, coeff_intCast_mul]
  rcases n with _ | n
  · simp [E6, a4, a6]
  · have key := twelve_mul_c6coeff (n + 1)
    simp [E6, a4, a6, PowerSeries.coeff_one]
    linear_combination (-72 : ℤ) * key

/-! ## The discriminant: `Δ = q·(1 + q·R)` -/

/-- `a₄ = q·A` with `A = Σ −5σ₃(n+1) qⁿ`. -/
def A4 : PowerSeries ℤ := PowerSeries.mk fun n => -5 * s3 (n + 1)

/-- `a₆ = q·B` with `B = Σ c₆(n+1) qⁿ`. -/
def B6 : PowerSeries ℤ := PowerSeries.mk fun n => c6coeff (n + 1)

theorem a4_eq : a4 = X * A4 := by
  ext n
  rcases n with _ | n
  · simp [a4, A4]
  · rw [PowerSeries.coeff_succ_X_mul]; simp [a4, A4]

theorem a6_eq : a6 = X * B6 := by
  ext n
  rcases n with _ | n
  · simp [a6, B6]
  · rw [PowerSeries.coeff_succ_X_mul]; simp [a6, B6]

/-- The higher part of the discriminant. -/
def deltaRest : PowerSeries ℤ :=
  A4 ^ 2 - 64 * X * A4 ^ 3 - 432 * B6 ^ 2 + 72 * A4 * B6

/-- `Δ(E_q) = q·(−B + q·R)`. -/
theorem tate_Δ_factor : tateCurve.Δ = X * (-B6 + X * deltaRest) := by
  have h : tateCurve.Δ = -(a6 - a4 ^ 2) - 64 * a4 ^ 3 - 432 * a6 ^ 2 + 72 * a4 * a6 := by
    simp only [WeierstrassCurve.Δ, WeierstrassCurve.b₂, WeierstrassCurve.b₄,
      WeierstrassCurve.b₆, WeierstrassCurve.b₈, tateCurve]
    ring
  rw [h, a4_eq, a6_eq, deltaRest]
  ring

theorem tate_Δ_coeff_zero : coeff 0 tateCurve.Δ = 0 := by
  rw [tate_Δ_factor]; simp

/-- The `q¹` coefficient of the discriminant is `1`: `q` is a uniformizer of `Δ`. -/
theorem tate_Δ_coeff_one : coeff 1 tateCurve.Δ = 1 := by
  rw [tate_Δ_factor, PowerSeries.coeff_succ_X_mul]
  simp [B6, c6coeff_one]

/-! ## The cusp `q = 0`: the nodal cubic and `𝔾ₘ` -/

/-- The fibre at `q = 0`. -/
def cusp : WeierstrassCurve ℤ := tateCurve.map (PowerSeries.constantCoeff (R := ℤ))

theorem cusp_fibre : cusp.a₁ = 1 ∧ cusp.a₂ = 0 ∧ cusp.a₃ = 0 ∧ cusp.a₄ = 0 ∧ cusp.a₆ = 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩ <;> simp [cusp, tateCurve, a4, a6]

theorem cusp_Δ : cusp.Δ = 0 := by
  rw [cusp, WeierstrassCurve.map_Δ, ← PowerSeries.coeff_zero_eq_constantCoeff_apply]
  exact tate_Δ_coeff_zero

variable {K : Type*} [Field K]

/-- The `𝔾ₘ` parametrization of the nodal cubic: `x = t/(1−t)²`. -/
def cuspX (t : K) : K := t / (1 - t) ^ 2

/-- The `𝔾ₘ` parametrization of the nodal cubic: `y = t²/(1−t)³`. -/
def cuspY (t : K) : K := t ^ 2 / (1 - t) ^ 3

/-- `t ↦ (t/(1−t)², t²/(1−t)³)` lands on `y² + xy = x³`. -/
theorem cusp_param (t : K) (ht : t ≠ 1) :
    cuspY t ^ 2 + cuspX t * cuspY t = cuspX t ^ 3 := by
  have h : (1 - t) ≠ 0 := sub_ne_zero.mpr (Ne.symm ht)
  unfold cuspX cuspY
  field_simp
  ring

/-- The formal derivative of `x(t) = t/(1−t)²`, by the quotient rule on the polynomials
`N = t`, `D = (1−t)²`: `x' = (N'D − ND')/D²`. -/
def cuspXDeriv (t : K) : K :=
  ((Polynomial.derivative (Polynomial.X : Polynomial K)).eval t * ((1 - t) ^ 2)
    - t * (Polynomial.derivative ((1 - Polynomial.X) ^ 2 : Polynomial K)).eval t) / ((1 - t) ^ 2) ^ 2

/-- **The invariant differential pulls back to `dt/t`.** On the nodal fibre,
`t · x'(t) = 2y + x` (with `a₁ = 1`, `a₃ = 0`, the invariant differential is `dx/(2y + x)`), so
`dx/(2y + x) = dt/t`, the invariant differential of `𝔾ₘ`. -/
theorem cusp_invariant_differential (t : K) (ht : t ≠ 1) :
    t * cuspXDeriv t = 2 * cuspY t + cuspX t := by
  have h : (1 - t) ≠ 0 := sub_ne_zero.mpr (Ne.symm ht)
  unfold cuspXDeriv cuspX cuspY
  simp only [Polynomial.derivative_X, Polynomial.eval_one, Polynomial.derivative_pow,
    Polynomial.derivative_sub, Polynomial.derivative_one, Polynomial.eval_mul,
    Polynomial.eval_pow, Polynomial.eval_sub, Polynomial.eval_X, Polynomial.eval_C,
    zero_sub, Polynomial.eval_neg]
  field_simp
  ring

end

end TateCurveCusp
end QOU.GaussManin
