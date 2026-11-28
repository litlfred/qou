import QOU.MassTheory.EnergyReadingTangent
import Mathlib.RingTheory.PowerSeries.Derivative
import Mathlib.RingTheory.PowerSeries.Inverse

/-!
# The whole `(q − 1)`-adic jet of the energy reading is a homomorphism

`QOU.MassTheory.EnergyReadingTangent` works to first order, in `K[ε]/(ε²)`. Here the same map
is taken to all orders. The formal completion of `G_m` at `q = 1` is `K⟦t⟧` with `q = 1 + t`,
and the group law in this coordinate is `QOU.FormalGroups.multiplicative`. The invariant vector
field `q ∂_q` of `G_m` becomes `(1 + t) d/dt`. So the energy reading `q ∂_q log m`, expanded at
`q = 1`, is the power series

    energyTower m = (1 + t) · m̂′(t) · m̂(t)⁻¹,    m̂(t) = m(1 + t) ∈ K⟦t⟧.

Its `n`-th coefficient is the `n`-th Taylor coefficient in `q − 1` of `q ∂_q log m`. Every
statement is algebraic: no `ℝ`, no limits, no `exp` or `log` function, no measured value.

* `tangentSeries : K[q, q⁻¹] →+* K⟦t⟧`, `q ↦ 1 + t` (a unit, since its constant term is `1`).
* `invLogDeriv_mul`: `(1 + t) d/dt log` is a homomorphism from `×` to `+` on series with
  non-zero constant term. This is the invariant differential of `G_m`.
* `energyTower_mul`, `energyTower_T` (`qᵏ ↦ k`, a constant series),
  `binding_tower_eq_ratio`: **to every order in `q − 1`, binding is the energy series of the
  interaction factor**, `energyTower m_AB − energyTower m_A − energyTower m_B = energyTower r`.
* `binding_tower_integer_of_unit`: if `r = c qᵏ`, the binding series is the constant `k`.
* `constantCoeff_invLogDeriv`: the constant term is `m̂₁ / m̂₀ = m′(1)/m(1) = −U(1)`.

Building note: needs the Mathlib module `RingTheory.PowerSeries.Derivative` (and
`PowerSeries.Trunc`), which the `lake-cache/qou-v4-24-0` snapshot does not ship. They build from
source with `lean`-direct in under a minute, with `--root=.` and
`-DautoImplicit=false -DmaxSynthPendingDepth=3`, as for `FormalGroupLaw.lean`.
-/

namespace QOU.MassTheory.EnergyReadingTower

open LaurentPolynomial PowerSeries

noncomputable section

variable {K : Type*} [Field K]

/-- `1 + t` is a unit of `K⟦t⟧`. -/
theorem isUnit_one_add_X : IsUnit (1 + X : K⟦X⟧) := by
  rw [PowerSeries.isUnit_iff_constantCoeff]
  simp

/-- `q = 1 + t` as a unit. -/
def qUnit : (K⟦X⟧)ˣ := (isUnit_one_add_X (K := K)).unit

/-- **The formal-neighbourhood map of `G_m` at `q = 1`:** `m(q) ↦ m(1 + t)`. -/
def tangentSeries : K[T;T⁻¹] →+* K⟦X⟧ :=
  LaurentPolynomial.eval₂ (PowerSeries.C (R := K)) qUnit

/-- The invariant logarithmic derivative of `G_m` in the coordinate `t = q − 1`:
`f ↦ (1 + t) f′ / f`. -/
def invLogDeriv (f : K⟦X⟧) : K⟦X⟧ := (1 + X) * d⁄dX K f * f⁻¹

/-- **The invariant log-derivative is a homomorphism** from `×` to `+`. -/
theorem invLogDeriv_mul {f g : K⟦X⟧} (hf : constantCoeff f ≠ 0) (hg : constantCoeff g ≠ 0) :
    invLogDeriv (f * g) = invLogDeriv f + invLogDeriv g := by
  unfold invLogDeriv
  have hf' := PowerSeries.mul_inv_cancel f hf
  have hg' := PowerSeries.mul_inv_cancel g hg
  rw [Derivation.leibniz, PowerSeries.mul_inv_rev, smul_eq_mul, smul_eq_mul]
  linear_combination ((1 + X) * d⁄dX K g * g⁻¹) * hf' + ((1 + X) * d⁄dX K f * f⁻¹) * hg'

theorem invLogDeriv_one : invLogDeriv (1 : K⟦X⟧) = 0 := by
  simp [invLogDeriv]

/-- **The constant term is `f₁ / f₀`**, i.e. `m′(1)/m(1) = −U(1)` for `f = m̂`. -/
theorem constantCoeff_invLogDeriv (f : K⟦X⟧) :
    constantCoeff (invLogDeriv f) = coeff 1 f / constantCoeff f := by
  unfold invLogDeriv
  rw [map_mul, map_mul, PowerSeries.constantCoeff_inv]
  have h1 : constantCoeff (d⁄dX K f) = coeff 1 f := by
    rw [← PowerSeries.coeff_zero_eq_constantCoeff_apply, PowerSeries.coeff_derivative]
    simp
  rw [h1]
  simp [div_eq_mul_inv]

/-- The energy series: `q ∂_q log m` expanded at `q = 1 + t`. -/
def energyTower (m : K[T;T⁻¹]) : K⟦X⟧ := invLogDeriv (tangentSeries m)

/-- The value `m(1)`. -/
def valueAtOne (m : K[T;T⁻¹]) : K := constantCoeff (tangentSeries m)

theorem valueAtOne_mul (m₁ m₂ : K[T;T⁻¹]) :
    valueAtOne (m₁ * m₂) = valueAtOne m₁ * valueAtOne m₂ := by
  unfold valueAtOne; rw [map_mul, map_mul]

theorem energyTower_mul {m₁ m₂ : K[T;T⁻¹]} (h₁ : valueAtOne m₁ ≠ 0) (h₂ : valueAtOne m₂ ≠ 0) :
    energyTower (m₁ * m₂) = energyTower m₁ + energyTower m₂ := by
  unfold energyTower; rw [map_mul]; exact invLogDeriv_mul h₁ h₂

theorem valueAtOne_T (k : ℤ) : valueAtOne (T k : K[T;T⁻¹]) = 1 := by
  unfold valueAtOne tangentSeries
  rw [eval₂_T]
  have hu : constantCoeff (qUnit (K := K) : K⟦X⟧) = 1 := by
    simp [qUnit]
  have : ∀ u : (K⟦X⟧)ˣ, constantCoeff (u : K⟦X⟧) = 1 → constantCoeff ((u ^ k : (K⟦X⟧)ˣ) : K⟦X⟧) = 1 := by
    intro u hu1
    rcases Int.eq_nat_or_neg k with ⟨n, rfl | rfl⟩
    · rw [zpow_natCast, Units.val_pow_eq_pow_val, map_pow, hu1, one_pow]
    · rw [zpow_neg, zpow_natCast]
      have e : ((u ^ n)⁻¹ : (K⟦X⟧)ˣ) * u ^ n = 1 := inv_mul_cancel _
      have e' := congrArg (fun v : (K⟦X⟧)ˣ => constantCoeff (v : K⟦X⟧)) e
      simp only [Units.val_mul, map_mul, Units.val_pow_eq_pow_val, map_pow, hu1, one_pow,
        mul_one, Units.val_one, map_one] at e'
      exact e'
  exact this _ hu

/-- `(1 + t) d/dt` of `(1 + t)ⁿ` over `(1 + t)ⁿ` is `n`. -/
theorem invLogDeriv_one_add_X_pow (n : ℕ) :
    invLogDeriv ((1 + X : K⟦X⟧) ^ n) = PowerSeries.C (n : K) := by
  induction n with
  | zero => simp [invLogDeriv_one]
  | succ n ih =>
    have h0 : constantCoeff ((1 + X : K⟦X⟧) ^ n) ≠ 0 := by simp
    have h1 : constantCoeff (1 + X : K⟦X⟧) ≠ 0 := by simp
    rw [pow_succ, invLogDeriv_mul h0 h1, ih]
    have : invLogDeriv (1 + X : K⟦X⟧) = 1 := by
      unfold invLogDeriv
      rw [map_add, Derivation.map_one_eq_zero, PowerSeries.derivative_X, zero_add, mul_one]
      exact PowerSeries.mul_inv_cancel _ h1
    rw [this]
    push_cast
    rw [map_add, map_one]

/-- **`qᵏ` has energy series the constant `k`.** -/
theorem energyTower_T (k : ℤ) : energyTower (T k : K[T;T⁻¹]) = PowerSeries.C (k : K) := by
  rcases Int.eq_nat_or_neg k with ⟨n, rfl | rfl⟩
  · unfold energyTower tangentSeries
    rw [eval₂_T, zpow_natCast, Units.val_pow_eq_pow_val]
    simpa [qUnit] using invLogDeriv_one_add_X_pow (K := K) n
  · have hmul : (T (-(n : ℤ)) : K[T;T⁻¹]) * T n = 1 := by
      rw [← T_add, neg_add_cancel, T_zero]
    have h := energyTower_mul (valueAtOne_T (K := K) (-(n : ℤ)) ▸ one_ne_zero)
      (valueAtOne_T (K := K) (n : ℤ) ▸ one_ne_zero)
    rw [hmul] at h
    have h1 : energyTower (1 : K[T;T⁻¹]) = 0 := by
      unfold energyTower; rw [map_one]; exact invLogDeriv_one
    have hn : energyTower (T (n : ℤ) : K[T;T⁻¹]) = PowerSeries.C (n : K) := by
      unfold energyTower tangentSeries
      rw [eval₂_T, zpow_natCast, Units.val_pow_eq_pow_val]
      simpa [qUnit] using invLogDeriv_one_add_X_pow (K := K) n
    rw [h1, hn] at h
    push_cast
    rw [map_neg]
    linear_combination -h

/-- **Binding to every order in `q − 1` is the energy series of the interaction factor.** -/
theorem binding_tower_eq_ratio {mA mB r mAB : K[T;T⁻¹]} (h : mAB = mA * mB * r)
    (hA : valueAtOne mA ≠ 0) (hB : valueAtOne mB ≠ 0) (hr : valueAtOne r ≠ 0) :
    energyTower mAB - energyTower mA - energyTower mB = energyTower r := by
  have hAB : valueAtOne (mA * mB) ≠ 0 := by rw [valueAtOne_mul]; exact mul_ne_zero hA hB
  rw [h, energyTower_mul hAB hr, energyTower_mul hA hB]
  ring

theorem energyTower_C_mul_T (c : K) (hc : c ≠ 0) (k : ℤ) :
    energyTower (LaurentPolynomial.C c * T k : K[T;T⁻¹]) = PowerSeries.C (k : K) := by
  have hC : valueAtOne (LaurentPolynomial.C c : K[T;T⁻¹]) ≠ 0 := by
    simp [valueAtOne, tangentSeries, eval₂_C, hc]
  rw [energyTower_mul hC (by rw [valueAtOne_T]; exact one_ne_zero), energyTower_T]
  have : energyTower (LaurentPolynomial.C c : K[T;T⁻¹]) = 0 := by
    simp [energyTower, invLogDeriv, tangentSeries, eval₂_C]
  rw [this, zero_add]

/-- **Integer binding to all orders.** If `m_AB = m_A · m_B · c qᵏ`, the binding series is the
constant `k` (in the sign convention of `q ∂_q log`; `U = −` this). -/
theorem binding_tower_integer_of_unit {mA mB mAB : K[T;T⁻¹]} (c : K) (hc : c ≠ 0) (k : ℤ)
    (h : mAB = mA * mB * (LaurentPolynomial.C c * T k)) (hA : valueAtOne mA ≠ 0)
    (hB : valueAtOne mB ≠ 0) :
    energyTower mAB - energyTower mA - energyTower mB = PowerSeries.C (k : K) := by
  have hr : valueAtOne (LaurentPolynomial.C c * T k : K[T;T⁻¹]) ≠ 0 := by
    rw [valueAtOne_mul, valueAtOne_T, mul_one]
    simpa [valueAtOne, tangentSeries, eval₂_C] using hc
  rw [binding_tower_eq_ratio h hA hB hr, energyTower_C_mul_T c hc]

end

end QOU.MassTheory.EnergyReadingTower
