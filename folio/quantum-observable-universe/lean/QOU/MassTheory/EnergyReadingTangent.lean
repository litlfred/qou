import QOU.LiftingDescent.MultiplicativeFormalGroup
import Mathlib.Algebra.DualNumber
import Mathlib.Algebra.Polynomial.Laurent

/-!
# The energy reading `U(1)` is the tangent map of `G_m`: algebraic, additive on composites

The energy reading `U = −q ∂_q log m` (def:mass-identity) is the logarithmic derivative along
`q ∂_q`, the invariant vector field of the multiplicative group `G_m`
(`QOU.FormalGroups.multiplicative`). At `q = 1` it needs no analysis. The **tangent map**

    tangent : R[q, q⁻¹] →+* R[ε]/(ε²),   q ↦ 1 + ε

is a ring map (`1 + ε` is a unit, with inverse `1 − ε`). It sends `m` to `m(1) + m′(1) ε`, so
`U(1) = −m′(1)/m(1) = −dlog(tangent m)`, where `dlog(a + bε) = b/a` is the first-order formal
logarithm of `G_m`: the group map from `G_m(K[ε])` to its Lie algebra `G_a(K)`.

Results (over a field `K`, no `ℝ`, no limits, no measured value):

* `dlog_mul`: `dlog` is a homomorphism, from `×` to `+`.
* `energyAtOne_mul`: `U(1)(m₁ m₂) = U(1)(m₁) + U(1)(m₂)` when `m₁(1), m₂(1) ≠ 0`.
* `binding_eq_energy_ratio`: if `m_AB = m_A · m_B · r`, then
  `U(1)(m_AB) − U(1)(m_A) − U(1)(m_B) = U(1)(r)`. **Binding in U-units is the energy reading of
  the interaction factor `r` alone.**
* `energyAtOne_C_mul_T`: a Laurent unit `c qᵏ` has `U(1) = −k`.
* `binding_integer_of_unit`: so if a composite factorises up to a Laurent unit, its binding is
  the **integer** `−k`.
* `energyAtOne_electron`: the electron's ring mass `[4]/q³ = 1 + q⁻² + q⁻⁴ + q⁻⁶` has
  `U(1) = 3`, the value `QOU.Transcendental.MassTheory.RingMassLinkingNumber.uAtOne_hopf`
  gets over `ℝ`. Here it is proved without `ℝ`.

What this does and does not say about the deuteron. It locates the binding exactly in the
interaction factor `r = m_d / (m_p m_n)`: binding is `U(1)(r) = −r′(1)/r(1)`, a first-order
coefficient of `r` in `q − 1`, not the value `r(q₀)`. It does not compute `r`.
-/

namespace QOU.MassTheory.EnergyReadingTangent

open LaurentPolynomial DualNumber TrivSqZeroExt

noncomputable section

variable {K : Type*} [Field K]

/-- `1 + ε` as a unit of the dual numbers, inverse `1 − ε`. -/
def onePlusEps : (DualNumber K)ˣ where
  val := 1 + ε
  inv := 1 - ε
  val_inv := by
    rw [show (1 + ε : DualNumber K) * (1 - ε) = 1 - ε * ε by ring, eps_mul_eps, sub_zero]
  inv_val := by
    rw [show (1 - ε : DualNumber K) * (1 + ε) = 1 - ε * ε by ring, eps_mul_eps, sub_zero]

/-- **The tangent map of `G_m` at `q = 1`:** `m(q) ↦ m(1 + ε) = m(1) + m′(1) ε`. -/
def tangent : K[T;T⁻¹] →+* DualNumber K :=
  LaurentPolynomial.eval₂ (algebraMap K (DualNumber K)) onePlusEps

/-- First-order formal logarithm of `G_m`: `a + bε ↦ b/a`. -/
def dlog (x : DualNumber K) : K := x.snd / x.fst

/-- **`dlog` is a homomorphism** from multiplication to addition. -/
theorem dlog_mul {x y : DualNumber K} (hx : x.fst ≠ 0) (hy : y.fst ≠ 0) :
    dlog (x * y) = dlog x + dlog y := by
  unfold dlog
  rw [TrivSqZeroExt.fst_mul, DualNumber.snd_mul]
  field_simp
  ring

/-- The energy reading at `q = 1`: `U(1)(m) = −m′(1)/m(1)`. -/
def energyAtOne (m : K[T;T⁻¹]) : K := -dlog (tangent m)

/-- The value `m(1)`. -/
def valueAtOne (m : K[T;T⁻¹]) : K := (tangent m).fst

/-- **The energy reading is additive on products.** -/
theorem energyAtOne_mul {m₁ m₂ : K[T;T⁻¹]} (h₁ : valueAtOne m₁ ≠ 0) (h₂ : valueAtOne m₂ ≠ 0) :
    energyAtOne (m₁ * m₂) = energyAtOne m₁ + energyAtOne m₂ := by
  unfold energyAtOne
  rw [map_mul, dlog_mul h₁ h₂, neg_add]

theorem valueAtOne_mul (m₁ m₂ : K[T;T⁻¹]) :
    valueAtOne (m₁ * m₂) = valueAtOne m₁ * valueAtOne m₂ := by
  unfold valueAtOne; rw [map_mul, TrivSqZeroExt.fst_mul]

/-- **Binding is the energy reading of the interaction factor.** If `m_AB = m_A · m_B · r` and
all three values at `1` are non-zero, the binding in U-units is `U(1)(r)`. -/
theorem binding_eq_energy_ratio {mA mB r mAB : K[T;T⁻¹]} (h : mAB = mA * mB * r)
    (hA : valueAtOne mA ≠ 0) (hB : valueAtOne mB ≠ 0) (hr : valueAtOne r ≠ 0) :
    energyAtOne mAB - energyAtOne mA - energyAtOne mB = energyAtOne r := by
  have hAB : valueAtOne (mA * mB) ≠ 0 := by rw [valueAtOne_mul]; exact mul_ne_zero hA hB
  rw [h, energyAtOne_mul hAB hr, energyAtOne_mul hA hB]
  ring

/-- `(1 + ε)ⁿ = 1 + n ε`. -/
theorem one_add_eps_pow (n : ℕ) :
    ((1 : DualNumber K) + ε) ^ n = 1 + (n : K) • ε := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ih]
    ext
    · simp [TrivSqZeroExt.fst_mul]
    · simp; ring

/-- `(1 − ε)ⁿ = 1 − n ε`. -/
theorem one_sub_eps_pow (n : ℕ) :
    ((1 : DualNumber K) - ε) ^ n = 1 - (n : K) • ε := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ih]
    ext <;> simp [TrivSqZeroExt.fst_mul]

/-- **`tangent (qᵏ) = 1 + k ε`.** -/
theorem tangent_T (k : ℤ) : tangent (T k : K[T;T⁻¹]) = 1 + (k : K) • ε := by
  unfold tangent
  rw [eval₂_T]
  rcases Int.eq_nat_or_neg k with ⟨n, rfl | rfl⟩
  · rw [zpow_natCast, Units.val_pow_eq_pow_val]
    simpa using one_add_eps_pow (K := K) n
  · rw [zpow_neg, zpow_natCast, ← inv_pow, Units.val_pow_eq_pow_val]
    have : ((onePlusEps (K := K))⁻¹ : (DualNumber K)ˣ).val = 1 - ε := rfl
    rw [this, one_sub_eps_pow]
    push_cast
    rw [neg_smul, sub_eq_add_neg]

theorem tangent_C (c : K) : tangent (C c : K[T;T⁻¹]) = algebraMap K (DualNumber K) c := by
  unfold tangent; rw [eval₂_C]

/-- **A Laurent unit `c qᵏ` has `U(1) = −k`.** -/
theorem energyAtOne_C_mul_T (c : K) (hc : c ≠ 0) (k : ℤ) :
    energyAtOne (C c * T k : K[T;T⁻¹]) = -(k : K) := by
  unfold energyAtOne dlog
  rw [map_mul, tangent_C, tangent_T, TrivSqZeroExt.fst_mul, DualNumber.snd_mul]
  simp [algebraMap_eq_inl, hc]

theorem valueAtOne_C_mul_T (c : K) (k : ℤ) :
    valueAtOne (C c * T k : K[T;T⁻¹]) = c := by
  unfold valueAtOne
  rw [map_mul, tangent_C, tangent_T, TrivSqZeroExt.fst_mul]
  simp [algebraMap_eq_inl]

/-- **Integer binding.** If a composite factorises as `m_AB = m_A · m_B · c qᵏ`, its binding in
U-units is the integer `−k`. -/
theorem binding_integer_of_unit {mA mB mAB : K[T;T⁻¹]} (c : K) (hc : c ≠ 0) (k : ℤ)
    (h : mAB = mA * mB * (C c * T k)) (hA : valueAtOne mA ≠ 0) (hB : valueAtOne mB ≠ 0) :
    energyAtOne mAB - energyAtOne mA - energyAtOne mB = -(k : K) := by
  rw [binding_eq_energy_ratio h hA hB (by rw [valueAtOne_C_mul_T]; exact hc),
    energyAtOne_C_mul_T c hc]

/-- The electron's ring mass `[4]/q³ = (q³ + q + q⁻¹ + q⁻³)/q³ = 1 + q⁻² + q⁻⁴ + q⁻⁶`. -/
def electronMass : K[T;T⁻¹] := T 0 + T (-2) + T (-4) + T (-6)

/-- **`U(1) = 3` for the electron, without `ℝ`.** -/
theorem energyAtOne_electron [CharZero K] : energyAtOne (electronMass : K[T;T⁻¹]) = 3 := by
  unfold energyAtOne dlog electronMass
  simp only [map_add, tangent_T, fst_add, snd_add, fst_one, snd_one, fst_smul, snd_smul,
    fst_eps, snd_eps, smul_eq_mul, mul_zero, mul_one]
  push_cast
  norm_num

end

end QOU.MassTheory.EnergyReadingTangent
