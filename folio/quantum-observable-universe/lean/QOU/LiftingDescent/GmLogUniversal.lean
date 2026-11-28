import QOU.LiftingDescent.GmDistPrimitive

/-!
# `log(1 + t)` is a homomorphism of formal group laws `Ĝ_m → Ĝ_a`

Let `L(t) = log(1 + t) = Σ_{k ≥ 1} (−1)^{k+1} tᵏ / k` (`formalLog (1 + X)`), over a field `K` of
characteristic `0`. This file proves the **universal** identity in two variables

    L(X + Y + XY) = L(X) + L(Y)      in K⟦X, Y⟧,

so `L` is a morphism from the multiplicative formal group law to the additive one.

The proof goes through the distribution algebra `Dist(Ĝ_m)`, not through a two-variable chain
rule. Write `δ_a` for the distribution `⟨δ_a, f⟩ = coeff_a f`.

* `deltaOne_conv_delta`: `δ₁ * δ_a = (a + 1) δ_{a+1} + a δ_a` (from `pair_conv_deltaOne`,
  `⟨δ₁ * μ, f⟩ = ⟨μ, (1 + t) f′⟩`). So `δ₁` generates, and every `δ_a` is reached by induction.
* `pair_conv_delta_log`: `⟨δ_a * δ_b, L⟩ = [b = 0] L_a + [a = 0] L_b`, i.e. `L` is a primitive
  functional on `Dist(Ĝ_m)`. Induction on `a`: `conv_assoc` turns `δ₁ * (δ_a * δ_b)` into the
  left-hand side, and `⟨δ₁ * μ, L⟩ = μ(0)` (`pair_conv_deltaOne_log`).
* `logOnePlus_subst_mulLaw`: reading the coefficients of both sides, the universal identity.

Pure algebra, proved without placeholders. No measured values.

-- Ref: [fred2005]
-/

namespace QOU.FormalGroups

open MvPowerSeries

noncomputable section

section Ring

variable {R : Type*} [CommRing R]

/-- The distribution `δ_a` on one coordinate: `⟨δ_a, f⟩ = coeff_a f`. -/
def delta (a : ℕ) : Dist R Unit := Finsupp.single (Finsupp.single () a) 1

theorem pair_delta (a : ℕ) (f : PowerSeries R) : pair (delta a) f = PowerSeries.coeff a f := by
  rw [delta, pair_single, one_mul]; rfl

theorem pair_conv_add_left (G : FormalGroupLaw R Unit) (μ μ' ν : Dist R Unit)
    (f : MvPowerSeries Unit R) :
    pair (conv G (μ + μ') ν) f = pair (conv G μ ν) f + pair (conv G μ' ν) f := by
  simp only [pair_conv, tensor2, pair_tensor]
  rw [Finsupp.sum_add_index']
  · intro m; simp
  · intro m a b; rw [← Finsupp.sum_add]; congr 1; funext n c; ring

theorem pair_conv_smul_left (G : FormalGroupLaw R Unit) (r : R) (μ ν : Dist R Unit)
    (f : MvPowerSeries Unit R) :
    pair (conv G (r • μ) ν) f = r * pair (conv G μ ν) f := by
  simp only [pair_conv, tensor2, pair_tensor]
  rw [Finsupp.sum_smul_index']
  · rw [Finsupp.mul_sum]; congr 1; funext m a
    rw [Finsupp.mul_sum]; congr 1; funext n c; rw [smul_eq_mul]; ring
  · intro m; simp

/-- **`δ₁ * δ_a = (a + 1) δ_{a+1} + a δ_a`.** -/
theorem deltaOne_conv_delta (a : ℕ) :
    conv (multiplicative (R := R)) deltaOne (delta a) =
      ((a + 1 : ℕ) : R) • delta (a + 1) + (a : R) • delta a := by
  apply ext_pair
  intro f
  rw [pair_conv_deltaOne, pair_add, pair_smul, pair_smul, pair_delta, pair_delta, pair_delta]
  rw [mul_comm, mul_add, mul_one, map_add, PowerSeries.coeff_derivative]
  rcases a with _ | m
  · simp
  · rw [mul_comm (PowerSeries.derivative R f) PowerSeries.X, PowerSeries.coeff_succ_X_mul,
      PowerSeries.coeff_derivative]
    push_cast; ring

/-- `⟨δ_a * δ_b, 1⟩ = [a = 0][b = 0]`: the counit of `δ_a * δ_b`. -/
theorem conv_delta_delta_zero (a b : ℕ) :
    conv (multiplicative (R := R)) (delta a) (delta b) 0 = if a = 0 ∧ b = 0 then 1 else 0 := by
  rw [← pair_monomial, pair_conv, tensor2, pair_tensor, delta, delta,
    Finsupp.sum_single_index (by simp), Finsupp.sum_single_index (by simp), one_mul, one_mul,
    Finsupp.mapDomain_single, Finsupp.mapDomain_single]
  have hs : HasSubst (multiplicative (R := R)).F := (multiplicative (R := R)).hasSubst_F
  rw [show (monomial 0 1 : MvPowerSeries Unit R) = 1 from monomial_zero_one, ← coe_substAlgHom hs,
    map_one, coeff_one]
  by_cases h : a = 0 ∧ b = 0
  · obtain ⟨rfl, rfl⟩ := h; simp
  · rw [if_neg h, if_neg]
    intro h0
    apply h
    have h1 := congrArg (fun d => d (blk 0 ())) h0
    have h2 := congrArg (fun d => d (blk 1 ())) h0
    simp [blk] at h1 h2
    exact ⟨h1, h2⟩

end Ring

section Field

variable {K : Type*} [Field K] [CharZero K]

open GmLog

/-- `L(t) = log(1 + t)`. -/
abbrev logOnePlus : PowerSeries K := formalLog (1 + PowerSeries.X)

omit [CharZero K] in
theorem coeff_logOnePlus_zero : PowerSeries.coeff 0 (logOnePlus (K := K)) = 0 := by
  rw [PowerSeries.coeff_zero_eq_constantCoeff_apply, constantCoeff_formalLog]

/-- `L_{a+2} = −(a+1)/(a+2) · L_{a+1}`, and `L_1 = 1`. -/
theorem coeff_logOnePlus_succ_succ (a : ℕ) :
    ((a + 2 : ℕ) : K) * PowerSeries.coeff (a + 1 + 1) (logOnePlus (K := K)) =
      -((a + 1 : ℕ) : K) * PowerSeries.coeff (a + 1) logOnePlus := by
  rw [coeff_formalLog_one_add_X _ (by omega), coeff_formalLog_one_add_X _ (by omega)]
  have h1 : ((a + 1 : ℕ) : K) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have h2 : ((a + 2 : ℕ) : K) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  field_simp
  rw [pow_succ]; ring

theorem coeff_logOnePlus_one : PowerSeries.coeff 1 (logOnePlus (K := K)) = 1 := by
  rw [coeff_formalLog_one_add_X _ one_ne_zero]; norm_num

/-- **`L` is primitive on `Dist(Ĝ_m)`:** `⟨δ_a * δ_b, L⟩ = [b = 0] L_a + [a = 0] L_b`. -/
theorem pair_conv_delta_log (a b : ℕ) :
    pair (conv (multiplicative (R := K)) (delta a) (delta b)) logOnePlus =
      (if b = 0 then PowerSeries.coeff a (logOnePlus (K := K)) else 0) +
        (if a = 0 then PowerSeries.coeff b (logOnePlus (K := K)) else 0) := by
  induction a with
  | zero =>
    rw [show (delta 0 : Dist K Unit) = one by simp [delta, one], one_conv, pair_delta,
      coeff_logOnePlus_zero]
    simp
  | succ a ih =>
    -- `⟨δ₁ * (δ_a * δ_b), L⟩` computed two ways
    have hL := pair_conv_deltaOne_log (K := K) (conv multiplicative (delta a) (delta b))
    rw [← conv_assoc, deltaOne_conv_delta, pair_conv_add_left, pair_conv_smul_left,
      pair_conv_smul_left, ih, conv_delta_delta_zero] at hL
    have hpos : ((a + 1 : ℕ) : K) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
    rw [if_neg (Nat.succ_ne_zero a), add_zero]
    apply mul_left_cancel₀ hpos
    rcases a with _ | a
    · -- a = 0
      by_cases hb : b = 0
      · subst hb; simp at hL ⊢; rw [coeff_logOnePlus_one]; linear_combination hL
      · simp [hb] at hL ⊢; linear_combination hL
    · by_cases hb : b = 0
      · subst hb
        simp only [if_true, Nat.succ_ne_zero, if_false, add_zero, false_and] at hL ⊢
        have hrec := coeff_logOnePlus_succ_succ (K := K) a
        push_cast at hL hrec ⊢
        linear_combination hL - hrec
      · simp only [hb, if_false, Nat.succ_ne_zero, and_false, add_zero, mul_zero] at hL ⊢
        linear_combination hL

local notation "S" => MvPowerSeries (Fin 2 × Unit) K

omit [CharZero K] in
theorem eq_dOne_split (D : Fin 2 × Unit →₀ ℕ) :
    D = Finsupp.single (0, ()) (D (0, ())) + Finsupp.single (1, ()) (D (1, ())) := by
  ext ⟨i, u⟩
  fin_cases i <;> simp

omit [CharZero K] in
theorem coeff_subst_X_logOnePlus (k : Fin 2) (D : Fin 2 × Unit →₀ ℕ) :
    coeff D (PowerSeries.subst (X (k, ()) : S) (logOnePlus (K := K))) =
      if D = Finsupp.single (k, ()) (D (k, ())) then
        PowerSeries.coeff (D (k, ())) (logOnePlus (K := K)) else 0 := by
  have hs : PowerSeries.HasSubst (X (k, ()) : S) := PowerSeries.HasSubst.X _
  rw [PowerSeries.coeff_subst hs]
  simp only [X_pow_eq, coeff_monomial, smul_eq_mul, mul_ite, mul_one, mul_zero]
  split_ifs with h
  · rw [finsum_eq_single _ (D (k, ()))]
    · rw [if_pos h]
    · intro j hj; rw [if_neg]; intro h'; apply hj
      have := congrArg (fun d => d (k, ())) h'; simpa using this.symm
  · apply finsum_eq_zero_of_forall_eq_zero
    intro j; rw [if_neg]; intro h'; apply h
    rw [h']; simp

/-- **`L(X + Y + XY) = L(X) + L(Y)` in `K⟦X, Y⟧`: `log(1+t)` is a homomorphism of formal group
laws from `Ĝ_m` to `Ĝ_a`.** -/
theorem logOnePlus_subst_mulLaw :
    PowerSeries.subst (xx + yy + xx * yy : S) (logOnePlus (K := K)) =
      PowerSeries.subst (xx : S) (logOnePlus (K := K)) +
        PowerSeries.subst (yy : S) (logOnePlus (K := K)) := by
  refine MvPowerSeries.ext fun D => ?_
  rw [map_add, coeff_subst_X_logOnePlus, coeff_subst_X_logOnePlus]
  set a := D (0, ())
  set b := D (1, ())
  have hD : D = Finsupp.single (0, ()) a + Finsupp.single (1, ()) b := eq_dOne_split D
  -- the left side is `⟨δ_a * δ_b, L⟩`
  have hl : coeff D (PowerSeries.subst (xx + yy + xx * yy : S) (logOnePlus (K := K))) =
      pair (conv (multiplicative (R := K)) (delta a) (delta b)) logOnePlus := by
    rw [pair_conv, tensor2, pair_tensor, delta, delta, Finsupp.sum_single_index (by simp),
      Finsupp.sum_single_index (by simp), one_mul, one_mul, Finsupp.mapDomain_single,
      Finsupp.mapDomain_single]
    rw [hD]; rfl
  rw [hl, pair_conv_delta_log]
  congr 1
  · by_cases hb : b = 0
    · rw [if_pos hb, if_pos]; rw [hD, hb]; simp
    · rw [if_neg hb, if_neg]
      intro h; apply hb
      have := congrArg (fun d => d (1, ())) h; simpa using this
  · by_cases ha : a = 0
    · rw [if_pos ha, if_pos]; rw [hD, ha]; simp
    · rw [if_neg ha, if_neg]
      intro h; apply ha
      have := congrArg (fun d => d (0, ())) h; simpa using this

end Field

end

end QOU.FormalGroups
