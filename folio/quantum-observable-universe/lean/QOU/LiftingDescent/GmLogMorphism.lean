import QOU.LiftingDescent.GmFormalLog
import QOU.LiftingDescent.MultiplicativeFormalGroup
import Mathlib.RingTheory.PowerSeries.Substitution
import Mathlib.RingTheory.PowerSeries.Trunc

/-!
# The logarithm series of `Ĝ_m` carries the group law `X + Y + XY` to `+`

`GmFormalLog.lean` defines `formalLog f = ∫ f′/f` and proves `log (fg) = log f + log g`.
This file turns that into a statement about **one fixed power series** `L(t) = log(1 + t)`,
composed with other series by Mathlib's substitution `PowerSeries.subst`, over a field `K` of
characteristic `0`.

* `derivative_subst`: the **chain rule** `d/dt (f ∘ h) = (f′ ∘ h) · h′` for `h(0) = 0`. Not in
  Mathlib. Proved by splitting `f` into its truncation (a polynomial, where it is
  `Derivation.map_aeval`) and a tail `X^{N+1} g`, whose contribution is divisible by `h^{N+1}`.
* `logSeries K := formalLog (1 + X)`, the series `Σ_{k ≥ 1} (−1)^{k+1} tᵏ / k`.
* `logSeries_subst`: `L ∘ h = formalLog (1 + h)`.
* `logSeries_subst_mulLaw`: for any two points `h₁, h₂ ∈ t K⟦t⟧`,
  `L(h₁ + h₂ + h₁h₂) = L(h₁) + L(h₂)`.
* `logSeries_subst2_multiplicative`: the same, written with the group law
  `QOU.FormalGroups.multiplicative` and its substitution `subst2`: on `K⟦t⟧`-points, `L` carries
  `Ĝ_m` to `Ĝ_a`.

**Scope.** This is the morphism property on the `K⟦t⟧`-points of `Ĝ_m`. The universal statement,
the identity `L(X + Y + XY) = L(X) + L(Y)` in the two-variable ring `K⟦X, Y⟧`, is not proved
here: it needs a two-variable chain rule, which Mathlib does not have.

Pure algebra: power series over `K`, no analysis, no measured values.
-/

namespace QOU.FormalGroups.GmLog

open PowerSeries

noncomputable section

variable {K : Type*} [Field K] [CharZero K]

/-! ### The chain rule for substitution -/

/-- The defect of the chain rule at `f`. -/
def chainDefect (h f : K⟦X⟧) : K⟦X⟧ :=
  d⁄dX K (f.subst h) - (d⁄dX K f).subst h * d⁄dX K h

omit [CharZero K] in
theorem chainDefect_add {h : K⟦X⟧} (hh : HasSubst h) (f g : K⟦X⟧) :
    chainDefect h (f + g) = chainDefect h f + chainDefect h g := by
  simp only [chainDefect, map_add, subst_add hh]
  ring

omit [CharZero K] in
theorem chainDefect_coe {h : K⟦X⟧} (hh : HasSubst h) (p : Polynomial K) :
    chainDefect h (p : K⟦X⟧) = 0 := by
  rw [chainDefect, derivative_coe, subst_coe hh, subst_coe hh, Derivation.map_aeval,
    smul_eq_mul, sub_self]

omit [CharZero K] in
theorem chainDefect_X_pow_mul {h : K⟦X⟧} (hh : HasSubst h) (N : ℕ) (g : K⟦X⟧) :
    chainDefect h (X ^ (N + 1) * g) = h ^ (N + 1) * chainDefect h g := by
  have hone : (1 : K⟦X⟧).subst h = 1 := by rw [← coe_substAlgHom hh, map_one]
  have hn : ((N + 1 : ℕ) : K⟦X⟧).subst h = ((N + 1 : ℕ) : K⟦X⟧) := by
    rw [← coe_substAlgHom hh, map_natCast]
  simp only [chainDefect, subst_mul hh, subst_pow hh, subst_X hh, Derivation.leibniz,
    Derivation.leibniz_pow, derivative_X, smul_eq_mul, nsmul_eq_mul, subst_add hh, hone, hn,
    Nat.add_sub_cancel]
  ring

omit [CharZero K] in
theorem chainDefect_eq_zero {h : K⟦X⟧} (h0 : constantCoeff h = 0) (f : K⟦X⟧) :
    chainDefect h f = 0 := by
  have hh : HasSubst h := HasSubst.of_constantCoeff_zero' h0
  have hXh : (X : K⟦X⟧) ∣ h := X_dvd_iff.mpr h0
  refine PowerSeries.ext fun m => ?_
  rw [map_zero]
  -- split `f = trunc (m+1) f + X^{m+1} g`
  obtain ⟨g, hg⟩ : X ^ (m + 1) ∣ f - (trunc (m + 1) f : K⟦X⟧) := by
    rw [X_pow_dvd_iff]
    intro i hi
    rw [map_sub, Polynomial.coeff_coe, coeff_trunc, if_pos hi, sub_self]
  have hf : f = (trunc (m + 1) f : K⟦X⟧) + X ^ (m + 1) * g := by rw [← hg]; ring
  rw [hf, chainDefect_add hh, chainDefect_coe hh, zero_add, chainDefect_X_pow_mul hh]
  have : X ^ (m + 1) ∣ h ^ (m + 1) * chainDefect h g :=
    (pow_dvd_pow_of_dvd hXh _).mul_right _
  exact (X_pow_dvd_iff.mp this) m (Nat.lt_succ_self m)

omit [CharZero K] in
/-- **The chain rule** `d/dt (f ∘ h) = (f′ ∘ h) · h′` when `h(0) = 0`. -/
theorem derivative_subst {h : K⟦X⟧} (h0 : constantCoeff h = 0) (f : K⟦X⟧) :
    d⁄dX K (f.subst h) = (d⁄dX K f).subst h * d⁄dX K h :=
  sub_eq_zero.mp (chainDefect_eq_zero h0 f)

/-! ### The logarithm series -/

variable (K) in
/-- **The logarithm series of `Ĝ_m`**, `L(t) = log(1 + t) = Σ_{k ≥ 1} (−1)^{k+1} tᵏ / k`. -/
def logSeries : K⟦X⟧ := formalLog (1 + X)

theorem constantCoeff_one_add {h : K⟦X⟧} (h0 : constantCoeff h = 0) :
    constantCoeff (1 + h) ≠ 0 := by
  rw [map_add, map_one, h0, add_zero]; exact one_ne_zero

theorem subst_inv_one_add_X {h : K⟦X⟧} (h0 : constantCoeff h = 0) :
    ((1 + X : K⟦X⟧)⁻¹).subst h = (1 + h)⁻¹ := by
  have hh : HasSubst h := HasSubst.of_constantCoeff_zero' h0
  rw [PowerSeries.eq_inv_iff_mul_eq_one (constantCoeff_one_add h0)]
  have h1 : (1 + h : K⟦X⟧) = (1 + X : K⟦X⟧).subst h := by
    rw [subst_add hh, subst_X hh, ← coe_substAlgHom hh, map_one]
  have hX : constantCoeff (1 + X : K⟦X⟧) ≠ 0 := constantCoeff_one_add (constantCoeff_X)
  rw [h1, ← subst_mul hh, PowerSeries.inv_mul_cancel _ hX, ← coe_substAlgHom hh, map_one]

omit [CharZero K] in
theorem constantCoeff_subst_of_zero {h : K⟦X⟧} (h0 : constantCoeff h = 0) {f : K⟦X⟧}
    (hf : constantCoeff f = 0) : constantCoeff (f.subst h) = 0 := by
  have hh : HasSubst h := HasSubst.of_constantCoeff_zero' h0
  rw [← coeff_zero_eq_constantCoeff_apply, coeff_subst' hh]
  apply finsum_eq_zero_of_forall_eq_zero
  intro d
  rcases Nat.eq_zero_or_pos d with rfl | hd
  · rw [coeff_zero_eq_constantCoeff_apply, hf, zero_smul]
  · rw [coeff_zero_eq_constantCoeff_apply, map_pow, h0, zero_pow hd.ne', smul_zero]

/-- **`L ∘ h = log (1 + h)`.** -/
theorem logSeries_subst {h : K⟦X⟧} (h0 : constantCoeff h = 0) :
    (logSeries K).subst h = formalLog (1 + h) := by
  apply derivative.ext
  · rw [derivative_subst h0, logSeries, derivative_formalLog, derivative_formalLog, map_add,
      Derivation.map_one_eq_zero, zero_add, derivative_X, one_mul, subst_inv_one_add_X h0,
      map_add, Derivation.map_one_eq_zero, zero_add, mul_comm]
  · rw [logSeries, constantCoeff_subst_of_zero h0 (constantCoeff_formalLog _),
      constantCoeff_formalLog]

/-- **On points, `L` carries `X + Y + XY` to `+`.** -/
theorem logSeries_subst_mulLaw {h₁ h₂ : K⟦X⟧} (h₁0 : constantCoeff h₁ = 0)
    (h₂0 : constantCoeff h₂ = 0) :
    (logSeries K).subst (h₁ + h₂ + h₁ * h₂) =
      (logSeries K).subst h₁ + (logSeries K).subst h₂ := by
  have h0 : constantCoeff (h₁ + h₂ + h₁ * h₂) = 0 := by
    rw [map_add, map_add, map_mul, h₁0, h₂0]; ring
  rw [logSeries_subst h0, logSeries_subst h₁0, logSeries_subst h₂0,
    show (1 + (h₁ + h₂ + h₁ * h₂) : K⟦X⟧) = (1 + h₁) * (1 + h₂) by ring,
    formalLog_mul (constantCoeff_one_add h₁0) (constantCoeff_one_add h₂0)]

/-- **`L` is a morphism `Ĝ_m → Ĝ_a` on `K⟦t⟧`-points**, written with the group law
`QOU.FormalGroups.multiplicative` and its substitution `subst2`. -/
theorem logSeries_subst2_multiplicative {h₁ h₂ : K⟦X⟧} (h₁0 : constantCoeff h₁ = 0)
    (h₂0 : constantCoeff h₂ = 0) :
    (logSeries K).subst (subst2 (fun _ : Unit => h₁) (fun _ => h₂)
        ((multiplicative (R := K)).F ())) =
      (logSeries K).subst h₁ + (logSeries K).subst h₂ := by
  have ha : NoConst (fun _ : Unit => (h₁ : MvPowerSeries Unit K)) := fun _ => h₁0
  have hb : NoConst (fun _ : Unit => (h₂ : MvPowerSeries Unit K)) := fun _ => h₂0
  show (logSeries K).subst (subst2 _ _ (multiplicativeF ())) = _
  rw [subst2_multiplicativeF ha hb]
  exact logSeries_subst_mulLaw h₁0 h₂0

end

end QOU.FormalGroups.GmLog
