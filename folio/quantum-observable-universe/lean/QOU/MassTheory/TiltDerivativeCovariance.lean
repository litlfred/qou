/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Polynomial.Derivative
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic

/-!
# The tilt derivative IS the covariance, and the vanishing mean is what makes it so

Bean `qou-k5r5` (gap: `M₁ = Cov_Planch(Σ□h, ω₃) > 0` for all `n`), epic `qou-x631`.

## What this file proves, and why it is not bookkeeping

The probe `wlambda_covariance_epic_M1_sigmah_tilt_path.py` reformulates `M₁` by tilting
Plancherel measure with the statistic `Σ□h` itself: with `x` a formal tilt variable,

    N(x) = ∑ᵢ wᵢ · fᵢ · x^{hᵢ},   D(x) = ∑ᵢ wᵢ · x^{hᵢ},   R(x) = N(x)/D(x)

and `R'(1) = M₁`. That identity was checked numerically at every `n ≤ 22`. Here it is
proved, for an arbitrary finite family over an arbitrary field — so it is a fact about
the construction, not about the range that was sampled.

The mathematical content is **not** the quotient rule. It is that the derivative of the
tilted mean at `x = 1` is a *covariance* rather than merely a weighted moment, and that
this holds precisely because the tilted statistic has **vanishing weighted mean**
(`wMean s w f = 0`). In the application `f = ω₃` and that hypothesis is the exact fact
`E_Planch[ω₃] = 0` — the same fact that `qou-ujil` uses to eliminate limit-shape
arguments. So the hypothesis of `tilt_deriv_eq_wCov` is the obstruction, re-used as
an asset rather than suffered as one.

## Anti-vacuity

`hf` is load-bearing, not decorative: `tilt_deriv_ne_wCov_of_mean_ne_zero` exhibits a
two-point family with `wMean ≠ 0` where the conclusion **fails**. Without that, a reader
could not tell whether the hypothesis was doing any work.

## Scope

This proves the *reformulation*, not the gap. `M₁ > 0` remains OPEN — nothing here
bounds `R'(1)` below, and the file makes no claim about the sign.
-/

namespace QOU.MassTheory

open Polynomial Finset

variable {R : Type*} {ι : Type*}

section CommRing

variable [CommRing R] (s : Finset ι) (w f : ι → R) (h : ι → ℕ)

/-- The tilted numerator `N(x) = ∑ᵢ wᵢ fᵢ x^{hᵢ}`. -/
noncomputable def tiltNum : R[X] := ∑ i ∈ s, C (w i * f i) * X ^ (h i)

/-- The tilted partition function `D(x) = ∑ᵢ wᵢ x^{hᵢ}`. -/
noncomputable def tiltDen : R[X] := ∑ i ∈ s, C (w i) * X ^ (h i)

@[simp]
theorem tiltNum_eval_one : (tiltNum s w f h).eval 1 = ∑ i ∈ s, w i * f i := by
  simp [tiltNum, eval_finset_sum]

@[simp]
theorem tiltDen_eval_one : (tiltDen s w h).eval 1 = ∑ i ∈ s, w i := by
  simp [tiltDen, eval_finset_sum]

/-- The derivative of the tilted numerator at `x = 1` is the `h`-weighted first moment
of `f`. This is the algebraic core: differentiating in the tilt brings down `hᵢ`. -/
theorem tiltNum_derivative_eval_one :
    (derivative (tiltNum s w f h)).eval 1 = ∑ i ∈ s, w i * f i * (h i : R) := by
  simp [tiltNum, eval_finset_sum, derivative_X_pow, mul_assoc]

end CommRing

section Field

variable [Field R] (s : Finset ι) (w f : ι → R) (h : ι → ℕ)

/-- The `w`-weighted mean of `g`. -/
noncomputable def wMean (s : Finset ι) (w g : ι → R) : R :=
  (∑ i ∈ s, w i * g i) / (∑ i ∈ s, w i)

/-- The `w`-weighted covariance of `g` and `k`. -/
noncomputable def wCov (s : Finset ι) (w g k : ι → R) : R :=
  wMean s w (fun i => g i * k i) - wMean s w g * wMean s w k

/-- **The tilt derivative is the covariance.**

`R'(1) = Cov_w(h, f)`, given only that `f` has vanishing `w`-weighted mean. In the
application `f = ω₃`, `h = Σ□h` and `w` is the Plancherel weight `(f^λ)²`, so this says
`M₁` is the slope at `x = 1` of the `Σ□h`-tilted mean of `ω₃` — a function that
*vanishes* at `x = 1`, which is exactly why the limit-shape evaluation there is
uninformative and the derivative is not. -/
theorem tilt_deriv_eq_wCov (hf : wMean s w f = 0) :
    (derivative (tiltNum s w f h)).eval 1 / (tiltDen s w h).eval 1
      = wCov s w (fun i => (h i : R)) f := by
  rw [tiltNum_derivative_eval_one, tiltDen_eval_one, wCov, hf, mul_zero, sub_zero, wMean]
  congr 1
  exact Finset.sum_congr rfl fun i _ => by ring

/-- The tilted mean vanishes at `x = 1` exactly when `f` has vanishing weighted mean —
so `R(1) = 0` is not an extra assumption, it is the same hypothesis. -/
theorem tiltNum_eval_one_eq_zero_iff (hw : ∑ i ∈ s, w i ≠ 0) :
    (tiltNum s w f h).eval 1 = 0 ↔ wMean s w f = 0 := by
  rw [tiltNum_eval_one, wMean, div_eq_zero_iff]
  exact ⟨fun hz => Or.inl hz, fun hz => hz.resolve_right hw⟩

end Field

section AntiVacuity

/-- **The vanishing-mean hypothesis is load-bearing.** A two-point family with
`wMean ≠ 0` on which `tilt_deriv_eq_wCov`'s conclusion is FALSE. Without this, the
hypothesis `hf` could be inert and the theorem above would be weaker than it reads. -/
theorem tilt_deriv_ne_wCov_of_mean_ne_zero :
    ∃ (s : Finset (Fin 2)) (w f : Fin 2 → ℚ) (h : Fin 2 → ℕ),
      (∑ i ∈ s, w i) ≠ 0 ∧ wMean s w f ≠ 0 ∧
      (derivative (tiltNum s w f h)).eval 1 / (tiltDen s w h).eval 1
        ≠ wCov s w (fun i => (h i : ℚ)) f := by
  refine ⟨Finset.univ, fun _ => 1, fun _ => 1, fun i => if i = 0 then 0 else 1, ?_, ?_, ?_⟩
  · norm_num [Fin.sum_univ_two]
  · norm_num [wMean, Fin.sum_univ_two]
  · norm_num [wMean, wCov, tiltNum_derivative_eval_one, tiltDen_eval_one, Fin.sum_univ_two]

end AntiVacuity

end QOU.MassTheory
