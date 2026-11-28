import QOU.MassTheory.EnergyReadingTower

/-!
# The formal logarithm of `G_m`: a homomorphism `(1 + t K⟦t⟧, ×) → (t K⟦t⟧, +)`

Over a field `K` of characteristic `0` the formal group `Ĝ_m` is isomorphic to `Ĝ_a` by the
logarithm. This file builds the logarithm from the invariant differential and proves it is a
group homomorphism on the `K⟦t⟧`-points of `Ĝ_m`, i.e. on series with constant term `1`.

* `integ`: formal integration, `t ↦ tⁿ⁺¹/(n+1)`, with `d/dt ∘ integ = id` (`derivative_integ`).
* `formalLog f := integ (f′ / f)`, constant term `0`.
* `formalLog_mul`: **`log(fg) = log f + log g`** for `f, g` with non-zero constant term. This is
  the formal-group statement that `log` is a homomorphism `G_m → G_a`.
* `formalLog_one`, `formalLog_pow`: `log 1 = 0`, `log(fⁿ) = n log f`.
* `invLogDeriv_eq`: `(1 + t) d/dt log f = invLogDeriv f`, so the energy series of
  `QOU.MassTheory.EnergyReadingTower` is the invariant derivative of the formal logarithm.
* `coeff_formalLog_one_add_X`: `log(1 + t) = Σ_{k ≥ 1} (−1)^{k+1} tᵏ / k`.

Pure algebra: `log` here is a power series, not the analytic function. No measured values.
-/

namespace QOU.FormalGroups.GmLog

open PowerSeries

noncomputable section

variable {K : Type*} [Field K] [CharZero K]

/-- Formal integration with zero constant term. -/
def integ (f : K⟦X⟧) : K⟦X⟧ := mk fun n => if n = 0 then 0 else coeff (n - 1) f / n

omit [CharZero K] in
theorem constantCoeff_integ (f : K⟦X⟧) : constantCoeff (integ f) = 0 := by
  rw [← coeff_zero_eq_constantCoeff_apply, integ, coeff_mk, if_pos rfl]

theorem derivative_integ (f : K⟦X⟧) : d⁄dX K (integ f) = f := by
  ext n
  rw [coeff_derivative, integ, coeff_mk, if_neg (Nat.succ_ne_zero n), Nat.add_sub_cancel]
  have : ((n + 1 : ℕ) : K) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.succ_ne_zero n)
  push_cast at this ⊢
  field_simp

/-- **The formal logarithm** `log f = ∫ f′/f`. -/
def formalLog (f : K⟦X⟧) : K⟦X⟧ := integ (d⁄dX K f * f⁻¹)

omit [CharZero K] in
theorem constantCoeff_formalLog (f : K⟦X⟧) : constantCoeff (formalLog f) = 0 :=
  constantCoeff_integ _

theorem derivative_formalLog (f : K⟦X⟧) : d⁄dX K (formalLog f) = d⁄dX K f * f⁻¹ :=
  derivative_integ _

/-- **`log` is a homomorphism `G_m → G_a`.** -/
theorem formalLog_mul {f g : K⟦X⟧} (hf : constantCoeff f ≠ 0) (hg : constantCoeff g ≠ 0) :
    formalLog (f * g) = formalLog f + formalLog g := by
  apply derivative.ext
  · rw [map_add, derivative_formalLog, derivative_formalLog, derivative_formalLog,
      Derivation.leibniz, PowerSeries.mul_inv_rev, smul_eq_mul, smul_eq_mul]
    have hf' := PowerSeries.mul_inv_cancel f hf
    have hg' := PowerSeries.mul_inv_cancel g hg
    linear_combination (d⁄dX K g * g⁻¹) * hf' + (d⁄dX K f * f⁻¹) * hg'
  · rw [map_add, constantCoeff_formalLog, constantCoeff_formalLog, constantCoeff_formalLog,
      add_zero]

theorem formalLog_one : formalLog (1 : K⟦X⟧) = 0 := by
  apply derivative.ext
  · rw [derivative_formalLog, Derivation.map_one_eq_zero, zero_mul, map_zero]
  · rw [constantCoeff_formalLog, map_zero]

theorem formalLog_pow {f : K⟦X⟧} (hf : constantCoeff f ≠ 0) (n : ℕ) :
    formalLog (f ^ n) = (n : K⟦X⟧) * formalLog f := by
  induction n with
  | zero => simp [formalLog_one]
  | succ n ih =>
    have hfn : constantCoeff (f ^ n) ≠ 0 := by rw [map_pow]; exact pow_ne_zero n hf
    rw [pow_succ, formalLog_mul hfn hf, ih]
    push_cast; ring

/-- **The energy series is the invariant derivative of the formal logarithm.** -/
theorem invLogDeriv_eq (f : K⟦X⟧) :
    QOU.MassTheory.EnergyReadingTower.invLogDeriv f = (1 + X) * d⁄dX K (formalLog f) := by
  rw [derivative_formalLog, QOU.MassTheory.EnergyReadingTower.invLogDeriv, mul_assoc]

/-- **`log(1 + t) = Σ_{k≥1} (−1)^{k+1} tᵏ/k`.** -/
theorem coeff_formalLog_one_add_X (k : ℕ) (hk : k ≠ 0) :
    coeff k (formalLog (1 + X : K⟦X⟧)) = (-1) ^ (k + 1) / k := by
  have h1 : constantCoeff (1 + X : K⟦X⟧) ≠ 0 := by simp
  have hinv : (1 + X : K⟦X⟧)⁻¹ = mk fun n => (-1 : K) ^ n := by
    rw [PowerSeries.inv_eq_iff_mul_eq_one h1]
    ext n
    rcases n with _ | n
    · simp
    · rw [mul_add, mul_one, mul_comm, map_add, coeff_succ_X_mul, coeff_mk, coeff_mk, coeff_one,
        if_neg (Nat.succ_ne_zero n), pow_succ]
      ring
  obtain ⟨m, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hk
  rw [formalLog, integ, coeff_mk, if_neg hk, Nat.succ_sub_one, map_add,
    Derivation.map_one_eq_zero, PowerSeries.derivative_X, zero_add, one_mul, hinv, coeff_mk]
  push_cast
  rw [pow_succ, pow_succ]
  ring

end

end QOU.FormalGroups.GmLog
