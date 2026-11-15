import Mathlib.NumberTheory.Bernoulli
import Mathlib.Tactic

/-!
# The `q → 1` dilogarithm expansion as a formal Todd-operator identity

With `q = e^{−ħ}`, the coefficient of `xᵐ` in `log (x; q)_∞ = Σ_{m ≥ 1} xᵐ / (m (1 − qᵐ))` is
`1/(m(1 − e^{−mħ}))`. Multiplying by `ħ` and expanding with the Todd series
`t/(1 − e^{−t}) = Σ_n B'_n tⁿ/n!` (`B'_1 = +1/2`) gives, coefficient by coefficient,

  `ħ · log (x; e^{−ħ})_∞ = Σ_{n ≥ 0} (B'_n / n!) · ħⁿ · Li_{2−n}(x)`,

whose `n = 0` term is `Li₂(x)` (Part A of the dilogarithm limit) and whose `n = 1` term is
`−½ log(1 − x)`. Everything in this file is formal algebra over a characteristic-zero field
`A`: power series in `ħ`, and power series in `x` with power-series coefficients.

* `todd_mul_one_sub_exp_neg`: `Todd(t) · (1 − e^{−t}) = t`, from Mathlib's
  `bernoulli'PowerSeries_mul_exp_sub_one`.
* `hbarLogPochCoeff m`: the series `ħ/(m(1 − e^{−mħ}))`, defined as `m⁻² · Todd(mħ)`.
  `hbarLogPochCoeff_spec` checks the defining equation and `hbarLogPochCoeff_unique` shows
  it determines the series, so the definition is not a choice.
* `coeff_hbarLogPochCoeff`: the `ħⁿ xᵐ` coefficient is `(B'_n/n!) · m^{n−2}`.
* `hbarLogPoch_eq_todd_expansion`: the double-series identity above, with
  `polylogNeg n = Σ_m m^{n−2} xᵐ` the formal `Li_{2−n}`.

**What stays analytic.** That the real function `ħ · log (x; e^{−ħ})_∞` has this formal series
as its asymptotic expansion as `ħ → 0⁺` is not proved here, and no class asserting it is
introduced. The exact finite-`n` reduction to the `m`-series is
`partialProduct_log_eq_mseries` in `Archimedean/DilogarithmArchimedeanLimit`; its `n = 0`
limit is the Part-A theorem `partialProduct_to_LiTwo_Ioo`.

Audit: `/mnt/project-files/qou-categorify-audit/analytic-steps-ranked-2026-11-15.md`, item 11.
-/

namespace QOU.QBeta.ToddDilogExpansion

open PowerSeries

variable (A : Type*) [Field A] [CharZero A]

/-- The Todd series `t/(1 − e^{−t}) = Σ_n B'_n tⁿ/n!`. -/
noncomputable abbrev todd : PowerSeries A := bernoulli'PowerSeries A

/-- **Defining equation of the Todd series:** `Todd(t) · (1 − e^{−t}) = t`. -/
theorem todd_mul_one_sub_exp_neg : todd A * (1 - evalNegHom (exp A)) = X := by
  have h := congrArg (· * evalNegHom (exp A)) (bernoulli'PowerSeries_mul_exp_sub_one A)
  simp only at h
  have hee : exp A * evalNegHom (exp A) = 1 := exp_mul_exp_neg_eq_one
  calc todd A * (1 - evalNegHom (exp A))
      = bernoulli'PowerSeries A * (exp A - 1) * evalNegHom (exp A) := by
        rw [mul_assoc, sub_mul, hee, one_mul]
    _ = X := by rw [h, mul_assoc, hee, mul_one]

/-- `1 − e^{−mħ}`, i.e. `1 − qᵐ` at `q = e^{−ħ}`. -/
noncomputable def oneSubQPow (m : ℕ) : PowerSeries A := 1 - rescale (m : A) (evalNegHom (exp A))

/-- **The `xᵐ` coefficient of `ħ · log (x; e^{−ħ})_∞`**, i.e. `ħ/(m(1 − e^{−mħ}))`, as
`m⁻² · Todd(mħ)`. -/
noncomputable def hbarLogPochCoeff (m : ℕ) : PowerSeries A :=
  C ((m : A)⁻¹ ^ 2) * rescale (m : A) (todd A)

omit [CharZero A] in
theorem rescale_X' (a : A) : rescale a (X : PowerSeries A) = C a * X := by
  ext n; rw [coeff_rescale, coeff_C_mul, coeff_X]; split_ifs with h <;> simp [h]

/-- `hbarLogPochCoeff m` satisfies `F · (1 − e^{−mħ}) = ħ/m`. -/
theorem hbarLogPochCoeff_spec (m : ℕ) (hm : m ≠ 0) :
    hbarLogPochCoeff A m * oneSubQPow A m = C (m : A)⁻¹ * X := by
  have hm' : (m : A) ≠ 0 := Nat.cast_ne_zero.mpr hm
  have h := congrArg (rescale (m : A)) (todd_mul_one_sub_exp_neg A)
  rw [map_mul, map_sub, map_one, rescale_X'] at h
  rw [hbarLogPochCoeff, oneSubQPow, mul_assoc, h, ← mul_assoc, ← map_mul]
  congr 2
  field_simp

theorem oneSubQPow_ne_zero (m : ℕ) (hm : m ≠ 0) : oneSubQPow A m ≠ 0 := by
  intro h
  have h1 := congrArg (coeff 1) h
  have hm' : (m : A) ≠ 0 := Nat.cast_ne_zero.mpr hm
  simp [oneSubQPow, evalNegHom, coeff_rescale, coeff_exp] at h1
  exact hm h1

/-- **Uniqueness:** the equation `F · (1 − e^{−mħ}) = ħ/m` determines `F`. -/
theorem hbarLogPochCoeff_unique (m : ℕ) (hm : m ≠ 0) {F : PowerSeries A}
    (hF : F * oneSubQPow A m = C (m : A)⁻¹ * X) : F = hbarLogPochCoeff A m := by
  have h := hF.trans (hbarLogPochCoeff_spec A m hm).symm
  exact mul_right_cancel₀ (oneSubQPow_ne_zero A m hm) h

/-- The formal polylogarithm `Li_{2−n}(x) = Σ_{m ≥ 1} m^{n−2} xᵐ`. -/
noncomputable def polylogNeg (n : ℕ) : PowerSeries A :=
  mk fun m => (m : A) ^ n / (m : A) ^ 2

/-- **The `ħⁿ xᵐ` coefficient** is `(B'_n/n!) · m^{n−2}`. -/
theorem coeff_hbarLogPochCoeff (m n : ℕ) :
    coeff n (hbarLogPochCoeff A m) =
      algebraMap ℚ A (bernoulli' n / n.factorial) * coeff m (polylogNeg A n) := by
  rw [hbarLogPochCoeff, coeff_C_mul, coeff_rescale, todd, bernoulli'PowerSeries, coeff_mk,
    polylogNeg, coeff_mk]
  rcases eq_or_ne (m : A) 0 with h | h
  · rw [h]; simp
  · field_simp

/-- `ħ · log (x; e^{−ħ})_∞` as a power series in `x` with coefficients in `A⟦ħ⟧`. -/
noncomputable def hbarLogPoch : PowerSeries (PowerSeries A) := mk (hbarLogPochCoeff A)

/-- **The Todd expansion**, coefficient by coefficient:
`ħ · log (x; e^{−ħ})_∞ = Σ_n (B'_n/n!) ħⁿ Li_{2−n}(x)`. -/
theorem hbarLogPoch_eq_todd_expansion :
    hbarLogPoch A = mk fun m => mk fun n =>
      algebraMap ℚ A (bernoulli' n / n.factorial) * coeff m (polylogNeg A n) := by
  ext m n
  rw [hbarLogPoch, coeff_mk, coeff_mk, coeff_mk, coeff_hbarLogPochCoeff]

/-- The leading term is `Li₂`: the `ħ⁰` coefficient of each `xᵐ` is `1/m²`. -/
theorem coeff_zero_hbarLogPochCoeff (m : ℕ) :
    coeff 0 (hbarLogPochCoeff A m) = 1 / (m : A) ^ 2 := by
  rw [coeff_hbarLogPochCoeff, polylogNeg, coeff_mk]; simp

/-- The first correction is `−½ log(1 − x)`: the `ħ¹` coefficient of each `xᵐ` is
`1/(2m)`. -/
theorem coeff_one_hbarLogPochCoeff (m : ℕ) :
    coeff 1 (hbarLogPochCoeff A m) = 1 / (2 * (m : A)) := by
  rw [coeff_hbarLogPochCoeff, polylogNeg, coeff_mk, bernoulli'_one]
  rcases eq_or_ne (m : A) 0 with h | h
  · rw [h]; simp
  · simp; field_simp

end QOU.QBeta.ToddDilogExpansion
