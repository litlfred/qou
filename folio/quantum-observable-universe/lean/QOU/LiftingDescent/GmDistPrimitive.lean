import QOU.LiftingDescent.Distributions
import QOU.LiftingDescent.MultiplicativeFormalGroup
import QOU.LiftingDescent.GmFormalLog
import Mathlib.RingTheory.PowerSeries.Substitution

/-!
# The primitive distribution `δ₁` of `Ĝ_m` acts as `(1 + t) d/dt`, and is dual to `log`

`Distributions.lean` builds the distribution algebra `Dist(G)` of a formal group law, with
convolution `⟨μ * ν, f⟩ = ⟨μ ⊠ ν, f(F(X, Y))⟩`. For the multiplicative law
`F(X, Y) = X + Y + XY` (`MultiplicativeFormalGroup.lean`) let `δ₁` be the distribution
`⟨δ₁, f⟩ = f′(0)`, the tangent vector at the origin (the primitive element of `Dist(Ĝ_m)`).

* `mulLaw_pow`: `F^k = Y^k + k X (Y^{k−1} + Y^k) + X² (⋯)`, i.e. `∂_X F^k |_{X=0} = (1 + Y) k Y^{k−1}`.
* `coeff_subst_mulLaw`: the `X¹ Yⁿ` coefficient of `f(F(X, Y))` is the `tⁿ` coefficient of
  `(1 + t) f′(t)`.
* `pair_conv_deltaOne`: **`⟨δ₁ * μ, f⟩ = ⟨μ, (1 + t) f′⟩`** for every distribution `μ`. So left
  convolution by `δ₁` is the invariant derivation `(1 + t) d/dt` of `Ĝ_m`. Over any commutative
  ring.
* `pair_conv_deltaOne_formalLog`: over a field of characteristic `0`,
  `⟨δ₁ * μ, log f⟩ = ⟨μ, invLogDeriv f⟩`: the energy series of `EnergyReadingTower` is what
  `δ₁` reads off the formal logarithm.
* `pair_conv_deltaOne_log`: `⟨δ₁ * μ, log(1 + t)⟩ = μ(0)` (the counit). The coordinate `log(1+t)`
  is the one whose invariant derivative is `1`: it is dual to the primitive `δ₁`.

Pure algebra, sorry-free. No measured values.

-- Ref: [fred2005]
-/

namespace QOU.FormalGroups

open MvPowerSeries

noncomputable section

section Ring

variable {R : Type*} [CommRing R]

local notation "S" => MvPowerSeries (Fin 2 × Unit) R

/-- The coordinate `X` of the first block. -/
abbrev xx : S := X (0, ())
/-- The coordinate `Y` of the second block. -/
abbrev yy : S := X (1, ())

theorem natCast_mul_pow_pred_mul (k : ℕ) (y : S) :
    (k : S) * (y ^ (k - 1) * y) = (k : S) * y ^ k := by
  rcases k with _ | k
  · simp
  · rw [Nat.add_sub_cancel, ← pow_succ]

/-- **First-order expansion of `F^k` in `X`.** -/
theorem mulLaw_pow (k : ℕ) : ∃ G : S,
    (xx + yy + xx * yy : S) ^ k = yy ^ k + xx * ((k : S) * (yy ^ (k - 1) + yy ^ k)) + xx ^ 2 * G := by
  induction k with
  | zero => exact ⟨0, by simp⟩
  | succ k ih =>
    obtain ⟨G, hG⟩ := ih
    refine ⟨(k : S) * (yy ^ (k - 1) + yy ^ k) * (1 + yy) + G * (xx + yy + xx * yy), ?_⟩
    rw [pow_succ, hG, Nat.add_sub_cancel]
    push_cast
    linear_combination (xx : S) * natCast_mul_pow_pred_mul k (yy : S)

/-- The multi-index `X¹ Yⁿ`. -/
def dOne (n : ℕ) : Fin 2 × Unit →₀ ℕ := Finsupp.single (0, ()) 1 + Finsupp.single (1, ()) n

theorem single_zero_le_dOne (n : ℕ) : Finsupp.single (0, ()) 1 ≤ dOne n := by
  simp [dOne]

theorem coeff_dOne_yy_pow (n j : ℕ) : coeff (dOne n) (yy ^ j : S) = 0 := by
  rw [X_pow_eq, coeff_monomial, if_neg]
  intro h
  have := congrArg (fun d => d (0, ())) h
  simp [dOne] at this

theorem coeff_dOne_xx_mul (n : ℕ) (Z : S) :
    coeff (dOne n) (xx * Z) = coeff (Finsupp.single (1, ()) n) Z := by
  rw [show (xx : S) = monomial (Finsupp.single (0, ()) 1) 1 from (X_pow_eq _ 1).symm.trans
    (pow_one _), coeff_monomial_mul, if_pos (single_zero_le_dOne n), one_mul, dOne,
    add_tsub_cancel_left]

theorem coeff_dOne_xx_sq_mul (n : ℕ) (G : S) : coeff (dOne n) (xx ^ 2 * G) = 0 := by
  rw [X_pow_eq, coeff_monomial_mul, if_neg]
  intro h
  have := h (0, ())
  simp [dOne] at this

theorem coeff_single_yy_pow (n j : ℕ) :
    coeff (Finsupp.single (1, ()) n) (yy ^ j : S) = if j = n then 1 else 0 := by
  rw [X_pow_eq, coeff_monomial]
  by_cases h : j = n
  · subst h; simp
  · rw [if_neg, if_neg h]
    intro h'
    exact h (Finsupp.single_injective _ h').symm

/-- **`∂_X F^k |_{X=0}`, coefficientwise.** -/
theorem coeff_dOne_mulLaw_pow (n k : ℕ) :
    coeff (dOne n) ((xx + yy + xx * yy : S) ^ k) =
      (k : R) * ((if k - 1 = n then 1 else 0) + (if k = n then 1 else 0)) := by
  obtain ⟨G, hG⟩ := mulLaw_pow (R := R) k
  rw [hG, map_add, map_add, coeff_dOne_yy_pow, coeff_dOne_xx_sq_mul, coeff_dOne_xx_mul,
    ← map_natCast (C (σ := Fin 2 × Unit) (R := R)), coeff_C_mul, map_add,
    coeff_single_yy_pow, coeff_single_yy_pow, zero_add, add_zero]

/-- **The `X¹ Yⁿ` coefficient of `f(X + Y + XY)` is the `tⁿ` coefficient of `(1 + t) f′`.** -/
theorem coeff_subst_mulLaw (f : PowerSeries R) (n : ℕ) :
    coeff (dOne n) (PowerSeries.subst (xx + yy + xx * yy : S) f) =
      PowerSeries.coeff n ((1 + PowerSeries.X) * PowerSeries.derivative R f) := by
  have hs : PowerSeries.HasSubst (xx + yy + xx * yy : S) :=
    PowerSeries.HasSubst.of_constantCoeff_zero (by simp)
  rw [PowerSeries.coeff_subst hs]
  simp only [coeff_dOne_mulLaw_pow, smul_eq_mul]
  have hsupp : (Function.support fun k : ℕ => PowerSeries.coeff k f *
      ((k : R) * ((if k - 1 = n then 1 else 0) + (if k = n then 1 else 0)))) ⊆
      (({n, n + 1} : Finset ℕ) : Set ℕ) := by
    intro k hk
    simp only [Function.mem_support] at hk
    simp only [Finset.coe_insert, Finset.coe_singleton, Set.mem_insert_iff,
      Set.mem_singleton_iff]
    by_contra hne
    push_neg at hne
    apply hk
    rcases Nat.eq_zero_or_pos k with rfl | hpos
    · simp
    · rw [if_neg (by omega), if_neg hne.1]; simp
  rw [finsum_eq_sum_of_support_subset _ hsupp, Finset.sum_pair (by omega), add_mul,
    one_mul, map_add]
  rcases n with _ | m
  · simp [PowerSeries.coeff_derivative]
  · rw [PowerSeries.coeff_succ_X_mul, PowerSeries.coeff_derivative,
      PowerSeries.coeff_derivative]
    simp only [show m + 1 - 1 ≠ m + 1 by omega, show m + 1 + 1 - 1 = m + 1 by omega,
      show m + 1 + 1 ≠ m + 1 by omega, if_true, if_false]
    push_cast
    ring

/-- The primitive distribution `δ₁`: `⟨δ₁, f⟩ = f′(0)`. -/
def deltaOne : Dist R Unit := Finsupp.single (Finsupp.single () 1) 1

/-- **Left convolution by `δ₁` is the invariant derivation `(1 + t) d/dt` of `Ĝ_m`.** -/
theorem pair_conv_deltaOne (μ : Dist R Unit) (f : PowerSeries R) :
    pair (conv (multiplicative (R := R)) deltaOne μ) f =
      pair μ ((1 + PowerSeries.X) * PowerSeries.derivative R f) := by
  rw [pair_conv, tensor2, pair_tensor, deltaOne, Finsupp.sum_single_index (by simp), pair]
  refine Finsupp.sum_congr fun d _ => ?_
  rw [one_mul, Finsupp.mapDomain_single, Finsupp.unique_single d, Finsupp.mapDomain_single]
  congr 1
  exact coeff_subst_mulLaw f (d ())

end Ring

section Field

variable {K : Type*} [Field K] [CharZero K]

open GmLog in
/-- **`δ₁` reads the energy series off the formal logarithm:**
`⟨δ₁ * μ, log f⟩ = ⟨μ, invLogDeriv f⟩`. -/
theorem pair_conv_deltaOne_formalLog (μ : Dist K Unit) (f : PowerSeries K) :
    pair (conv (multiplicative (R := K)) deltaOne μ) (formalLog f) =
      pair μ (QOU.MassTheory.EnergyReadingTower.invLogDeriv f) := by
  rw [pair_conv_deltaOne, invLogDeriv_eq]

open GmLog in
/-- **`log(1 + t)` is dual to the primitive `δ₁`:** `⟨δ₁ * μ, log(1 + t)⟩ = μ(0)`. -/
theorem pair_conv_deltaOne_log (μ : Dist K Unit) :
    pair (conv (multiplicative (R := K)) deltaOne μ) (formalLog (1 + PowerSeries.X)) = μ 0 := by
  have h1 : PowerSeries.constantCoeff (1 + PowerSeries.X : PowerSeries K) ≠ 0 := by simp
  rw [pair_conv_deltaOne, derivative_formalLog, map_add, Derivation.map_one_eq_zero, zero_add,
    PowerSeries.derivative_X, one_mul, PowerSeries.mul_inv_cancel _ h1]
  rw [show (1 : PowerSeries K) = MvPowerSeries.monomial 0 1 from (monomial_zero_one).symm,
    pair_monomial]

end Field

end

end QOU.FormalGroups
