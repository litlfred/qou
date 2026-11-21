import QOU.Mathlib.HadamardFactorization
import QOU.Mathlib.HadamardApplicability

/-!
# Growth of the Weierstrass canonical product (Borel's theorem)

For a sequence `a : ℕ → ℂ` of nonzero points and an integer genus `p`, the
canonical product is `P(z) = ∏' n, Eₚ(z / aₙ)`, with `Eₚ` the Weierstrass primary
factor `QOU.Mathlib.HadamardFactorization.weierstrassFactor`.

## Proved here (sorry-free, no new axioms)

* **(A) factor estimates.**
  - `norm_weierstrassFactor_le_exp_of_norm_le_one`: `‖w‖ ≤ 1 → ‖Eₚ(w)‖ ≤ exp ‖w‖^{p+1}`.
  - `norm_weierstrassFactor_le`: `‖Eₚ(w)‖ ≤ (1 + ‖w‖) · exp(Sₚ(‖w‖))` for every `w`,
    where `Sₚ(t) = ∑_{k=1}^{p} t^k/k`.
  - `expSumR_le_of_one_le`: `1 ≤ t → Sₚ(t) ≤ p · t^p`.
  - `norm_weierstrassFactor_le_exp_rpow`: the unified bound used by Borel's theorem,
    for every real `σ` with `0 < σ` and `p ≤ σ ≤ p + 1` and every `w`,
    `‖Eₚ(w)‖ ≤ exp (K · ‖w‖^σ)` with the explicit constant
    `K = growthConst p σ = 2^σ/σ + p + 1`.
* **(B) the canonical product is entire.**
  `differentiable_canonicalProduct` (hypothesis `∑ ‖aₙ‖^{-σ} < ∞` for some
  `0 < σ ≤ p + 1`) and `differentiable_canonicalProduct_of_summable_inv_pow` (the
  repository's form `∑ 1/‖aₙ‖^{p+1} < ∞`). The finitely many `n` with `‖aₙ‖`
  small are not removed: the domination is only required eventually.
* **(C) Borel's order bound.** `norm_canonicalProduct_le`: for `0 < σ`,
  `p ≤ σ ≤ p + 1` and `∑ ‖aₙ‖^{-σ} < ∞`, for every `z`,
  `‖P(z)‖ ≤ exp (K · (∑' n, ‖aₙ‖^{-σ}) · ‖z‖^σ)`; hence
  `isEntireOfOrderLE_canonicalProduct : IsEntireOfOrderLE P σ`.
  The bound holds for all `z`, not only `‖z‖ ≥ 1`, and `σ = p` is allowed
  (the classical statement takes `p < σ`).

## Not proved here

* No lower bound on `‖P(z)‖` (the minimum-modulus estimates off the zeros, needed
  for the converse direction of Hadamard's theorem).
* Nothing about the zeros of `P` beyond what the factors give; in particular it is
  not shown here that `P` vanishes exactly on `{aₙ}` with the right multiplicities.
* The sharp constant: `K` is explicit but not optimal.
* Hadamard's factorization theorem itself (`hadamard_factorization` remains the
  class-conditional statement in `QOU.Mathlib.HadamardFactorization`).
-/

namespace QOU.Mathlib.CanonicalProductGrowth

open QOU.Mathlib.HadamardFactorization
open QOU.Mathlib.WeierstrassFactorEstimate (expSumR re_expSum_le)

/-! ## (A) Estimates for one primary factor -/

/-- For `‖w‖ ≤ 1`, `‖Eₚ(w)‖ ≤ exp (‖w‖^{p+1})`. -/
theorem norm_weierstrassFactor_le_exp_of_norm_le_one (p : ℕ) {w : ℂ} (hw : ‖w‖ ≤ 1) :
    ‖weierstrassFactor p w‖ ≤ Real.exp (‖w‖ ^ (p + 1)) := by
  have h1 := norm_one_sub_weierstrassFactor_le p hw
  have h2 : ‖weierstrassFactor p w‖ ≤ 1 + ‖1 - weierstrassFactor p w‖ := by
    have : weierstrassFactor p w = 1 - (1 - weierstrassFactor p w) := by ring
    calc ‖weierstrassFactor p w‖ = ‖1 - (1 - weierstrassFactor p w)‖ := by rw [← this]
      _ ≤ ‖(1 : ℂ)‖ + ‖1 - weierstrassFactor p w‖ := norm_sub_le _ _
      _ = 1 + ‖1 - weierstrassFactor p w‖ := by simp
  have h3 := Real.add_one_le_exp (‖w‖ ^ (p + 1))
  linarith

/-- For every `w`, `‖Eₚ(w)‖ ≤ (1 + ‖w‖) · exp (Sₚ(‖w‖))`. -/
theorem norm_weierstrassFactor_le (p : ℕ) (w : ℂ) :
    ‖weierstrassFactor p w‖ ≤ (1 + ‖w‖) * Real.exp (expSumR p ‖w‖) := by
  have hdef : weierstrassFactor p w
      = (1 - w) * Complex.exp (QOU.Mathlib.WeierstrassFactorEstimate.expSum p w) := rfl
  rw [hdef, norm_mul, Complex.norm_exp]
  have h1 : ‖1 - w‖ ≤ 1 + ‖w‖ := by
    calc ‖1 - w‖ ≤ ‖(1 : ℂ)‖ + ‖w‖ := norm_sub_le _ _
      _ = 1 + ‖w‖ := by simp
  have h2 : Real.exp (QOU.Mathlib.WeierstrassFactorEstimate.expSum p w).re
      ≤ Real.exp (expSumR p ‖w‖) := Real.exp_le_exp.mpr (re_expSum_le p w)
  exact mul_le_mul h1 h2 (Real.exp_pos _).le (by positivity)

/-- For `t ≥ 1`, `Sₚ(t) ≤ p · t^p`. -/
theorem expSumR_le_of_one_le (p : ℕ) {t : ℝ} (ht : 1 ≤ t) :
    expSumR p t ≤ p * t ^ p := by
  unfold expSumR
  have hterm : ∀ k ∈ Finset.range p, t ^ (k + 1) / ((k : ℝ) + 1) ≤ t ^ p := by
    intro k hk
    have hk' : k + 1 ≤ p := Finset.mem_range.mp hk
    have hk1 : (1 : ℝ) ≤ (k : ℝ) + 1 := by
      have : (0 : ℝ) ≤ k := Nat.cast_nonneg k
      linarith
    have ht0 : (0 : ℝ) ≤ t ^ (k + 1) := by positivity
    calc t ^ (k + 1) / ((k : ℝ) + 1) ≤ t ^ (k + 1) := div_le_self ht0 hk1
      _ ≤ t ^ p := pow_le_pow_right₀ ht hk'
  calc ∑ k ∈ Finset.range p, t ^ (k + 1) / ((k : ℝ) + 1)
      ≤ ∑ _k ∈ Finset.range p, t ^ p := Finset.sum_le_sum hterm
    _ = p * t ^ p := by simp

/-- The explicit constant `K = 2^σ/σ + p + 1` of the unified factor bound. -/
noncomputable def growthConst (p : ℕ) (σ : ℝ) : ℝ :=
  (2 : ℝ) ^ σ / σ + p + 1

theorem one_le_growthConst (p : ℕ) {σ : ℝ} (hσ : 0 < σ) : 1 ≤ growthConst p σ := by
  unfold growthConst
  have h1 : 0 ≤ (2 : ℝ) ^ σ / σ := by positivity
  have h2 : (0 : ℝ) ≤ p := Nat.cast_nonneg p
  linarith

/-- For `0 ≤ x ≤ 1` and `σ ≤ p + 1` (with `0 ≤ σ`), `x^{p+1} ≤ x^σ`. -/
theorem pow_succ_le_rpow_of_le_one {x σ : ℝ} (p : ℕ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1)
    (hσ0 : 0 ≤ σ) (hσp : σ ≤ (p : ℝ) + 1) : x ^ (p + 1) ≤ x ^ σ := by
  have hcast : x ^ (p + 1) = x ^ ((p : ℝ) + 1) := by
    rw [← Real.rpow_natCast]; push_cast; ring_nf
  rw [hcast]
  exact Real.rpow_le_rpow_of_exponent_ge' hx0 hx1 hσ0 hσp

/-- **Unified factor bound.** For `0 < σ` and `p ≤ σ ≤ p + 1`, every `w` satisfies
    `‖Eₚ(w)‖ ≤ exp (K · ‖w‖^σ)` with `K = growthConst p σ`. -/
theorem norm_weierstrassFactor_le_exp_rpow (p : ℕ) {σ : ℝ} (hσ0 : 0 < σ)
    (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1) (w : ℂ) :
    ‖weierstrassFactor p w‖ ≤ Real.exp (growthConst p σ * ‖w‖ ^ σ) := by
  set x := ‖w‖ with hxdef
  have hx0 : 0 ≤ x := norm_nonneg w
  have hK := one_le_growthConst p hσ0
  have hxσ : 0 ≤ x ^ σ := Real.rpow_nonneg hx0 σ
  rcases le_total x 1 with hx1 | hx1
  · -- small argument
    calc ‖weierstrassFactor p w‖ ≤ Real.exp (x ^ (p + 1)) :=
          norm_weierstrassFactor_le_exp_of_norm_le_one p hx1
      _ ≤ Real.exp (growthConst p σ * x ^ σ) := by
          apply Real.exp_le_exp.mpr
          have := pow_succ_le_rpow_of_le_one p hx0 hx1 hσ0.le hσp
          nlinarith
  · -- large argument
    have hlog : Real.log (1 + x) ≤ (1 + x) ^ σ / σ :=
      Real.log_le_rpow_div (by linarith) hσ0
    have h2x : (1 + x) ^ σ ≤ (2 : ℝ) ^ σ * x ^ σ := by
      rw [← Real.mul_rpow (by norm_num) hx0]
      exact Real.rpow_le_rpow (by linarith) (by linarith) hσ0.le
    have hS : expSumR p x ≤ p * x ^ σ := by
      have h := expSumR_le_of_one_le p hx1
      have hp : x ^ p ≤ x ^ σ := by
        rw [← Real.rpow_natCast]
        exact Real.rpow_le_rpow_of_exponent_le hx1 hpσ
      have : (p : ℝ) * x ^ p ≤ p * x ^ σ :=
        mul_le_mul_of_nonneg_left hp (Nat.cast_nonneg p)
      linarith
    have h1x : 1 + x = Real.exp (Real.log (1 + x)) :=
      (Real.exp_log (by linarith)).symm
    calc ‖weierstrassFactor p w‖ ≤ (1 + x) * Real.exp (expSumR p x) :=
          norm_weierstrassFactor_le p w
      _ = Real.exp (Real.log (1 + x) + expSumR p x) := by
          rw [Real.exp_add, ← h1x]
      _ ≤ Real.exp (growthConst p σ * x ^ σ) := by
          apply Real.exp_le_exp.mpr
          have hdiv : (1 + x) ^ σ / σ ≤ (2 : ℝ) ^ σ * x ^ σ / σ :=
            div_le_div_of_nonneg_right h2x hσ0.le
          have hrw : (2 : ℝ) ^ σ * x ^ σ / σ = (2 : ℝ) ^ σ / σ * x ^ σ := by ring
          unfold growthConst
          nlinarith

/-! ## Tail control from summability of `‖aₙ‖^{-σ}` -/

/-- Summability of `‖aₙ‖^{-σ}` (`σ > 0`, all `aₙ ≠ 0`) forces `‖aₙ‖ ≥ M`
    eventually, for every `M`. -/
theorem eventually_le_norm {a : ℕ → ℂ} {σ : ℝ} (ha : ∀ n, a n ≠ 0) (hσ0 : 0 < σ)
    (hs : Summable (fun n => ‖a n‖ ^ (-σ))) (M : ℝ) :
    ∀ᶠ n in Filter.atTop, M ≤ ‖a n‖ := by
  set M' := max M 1 with hM'
  have hM'pos : 0 < M' := lt_of_lt_of_le one_pos (le_max_right _ _)
  have hc : 0 < M' ^ (-σ) := Real.rpow_pos_of_pos hM'pos _
  filter_upwards [hs.tendsto_atTop_zero.eventually_lt_const hc] with n hn
  have hpos : 0 < ‖a n‖ := norm_pos_iff.mpr (ha n)
  have : M' ≤ ‖a n‖ := by
    by_contra h
    push_neg at h
    have := Real.rpow_lt_rpow_of_exponent_neg hpos h (by linarith : -σ < 0)
    linarith
  exact le_trans (le_max_left _ _) this

/-- `‖z / aₙ‖^σ = ‖z‖^σ · ‖aₙ‖^{-σ}`. -/
theorem norm_div_rpow (z b : ℂ) (σ : ℝ) :
    ‖z / b‖ ^ σ = ‖z‖ ^ σ * ‖b‖ ^ (-σ) := by
  rw [norm_div, Real.div_rpow (norm_nonneg _) (norm_nonneg _),
    Real.rpow_neg (norm_nonneg _), div_eq_mul_inv]

/-- For `‖w‖ ≤ 1` and `0 ≤ σ ≤ p + 1`, `‖Eₚ(w) - 1‖ ≤ ‖w‖^σ`. -/
theorem norm_weierstrassFactor_sub_one_le_rpow (p : ℕ) {σ : ℝ} (hσ0 : 0 ≤ σ)
    (hσp : σ ≤ (p : ℝ) + 1) {w : ℂ} (hw : ‖w‖ ≤ 1) :
    ‖weierstrassFactor p w - 1‖ ≤ ‖w‖ ^ σ := by
  rw [norm_sub_rev]
  exact (norm_one_sub_weierstrassFactor_le p hw).trans
    (pow_succ_le_rpow_of_le_one p (norm_nonneg w) hw hσ0 hσp)

/-! ## (B) The canonical product is entire -/

/-- **The canonical product is entire.** If all `aₙ ≠ 0` and `∑ ‖aₙ‖^{-σ} < ∞` for
    some `0 < σ ≤ p + 1`, then `z ↦ ∏' n, Eₚ(z / aₙ)` is differentiable on `ℂ`. -/
theorem differentiable_canonicalProduct {a : ℕ → ℂ} (p : ℕ) {σ : ℝ}
    (ha : ∀ n, a n ≠ 0) (hσ0 : 0 < σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable (fun n => ‖a n‖ ^ (-σ))) :
    Differentiable ℂ (fun z => ∏' n, weierstrassFactor p (z / a n)) := by
  have hfun : (fun z => ∏' n, weierstrassFactor p (z / a n))
      = fun z => ∏' n, (1 + (fun n z => weierstrassFactor p (z / a n) - 1) n z) := by
    funext z; congr 1; funext n; ring
  rw [hfun]
  refine QOU.Mathlib.HadamardApplicability.differentiable_tprod_one_add ?_ ?_
  · intro n
    exact ((differentiable_weierstrassFactor p).comp
      (differentiable_id.div_const (a n))).sub_const 1
  · intro R hR
    refine ⟨fun n => R ^ σ * ‖a n‖ ^ (-σ), hs.mul_left _, ?_⟩
    filter_upwards [eventually_le_norm ha hσ0 hs R] with n hn z hz
    have hpos : 0 < ‖a n‖ := norm_pos_iff.mpr (ha n)
    have hzR : ‖z‖ < R := by simpa using hz
    have hle : ‖z / a n‖ ≤ R / ‖a n‖ := by
      rw [norm_div]; exact div_le_div_of_nonneg_right hzR.le hpos.le
    have h1 : ‖z / a n‖ ≤ 1 := hle.trans ((div_le_one hpos).mpr hn)
    calc ‖weierstrassFactor p (z / a n) - 1‖ ≤ ‖z / a n‖ ^ σ :=
          norm_weierstrassFactor_sub_one_le_rpow p hσ0.le hσp h1
      _ ≤ (R / ‖a n‖) ^ σ := Real.rpow_le_rpow (norm_nonneg _) hle hσ0.le
      _ = R ^ σ * ‖a n‖ ^ (-σ) := by
          rw [Real.div_rpow hR.le hpos.le, Real.rpow_neg hpos.le, div_eq_mul_inv]

/-- The repository's summability form: `1 / ‖aₙ‖^{p+1}` summable is the case
    `σ = p + 1`. -/
theorem summable_rpow_neg_of_summable_inv_pow {a : ℕ → ℂ} (p : ℕ)
    (hsum : Summable (fun n => 1 / ‖a n‖ ^ (p + 1))) :
    Summable (fun n => ‖a n‖ ^ (-((p : ℝ) + 1))) := by
  refine hsum.congr fun n => ?_
  rw [Real.rpow_neg (norm_nonneg _), one_div]
  congr 1
  rw [← Real.rpow_natCast]; push_cast; ring_nf

/-- **The canonical product is entire** (repository form of the hypothesis). -/
theorem differentiable_canonicalProduct_of_summable_inv_pow {a : ℕ → ℂ} (p : ℕ)
    (ha : ∀ n, a n ≠ 0) (hsum : Summable (fun n => 1 / ‖a n‖ ^ (p + 1))) :
    Differentiable ℂ (fun z => ∏' n, weierstrassFactor p (z / a n)) :=
  differentiable_canonicalProduct p ha (by positivity) le_rfl
    (summable_rpow_neg_of_summable_inv_pow p hsum)

/-! ## (C) Borel's order bound -/

/-- Multipliability under the `σ`-summability hypothesis. -/
theorem multipliable_canonicalProduct_rpow {a : ℕ → ℂ} (p : ℕ) {σ : ℝ}
    (ha : ∀ n, a n ≠ 0) (hσ0 : 0 < σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable (fun n => ‖a n‖ ^ (-σ))) (z : ℂ) :
    Multipliable (fun n => weierstrassFactor p (z / a n)) := by
  have hev : ∀ᶠ n in Filter.atTop,
      ‖weierstrassFactor p (z / a n) - 1‖ ≤ ‖z‖ ^ σ * ‖a n‖ ^ (-σ) := by
    filter_upwards [eventually_le_norm ha hσ0 hs ‖z‖] with n hn
    have hpos : 0 < ‖a n‖ := norm_pos_iff.mpr (ha n)
    have h1 : ‖z / a n‖ ≤ 1 := by rw [norm_div]; exact (div_le_one hpos).mpr hn
    rw [← norm_div_rpow]
    exact norm_weierstrassFactor_sub_one_le_rpow p hσ0.le hσp h1
  have key : Summable (fun n => weierstrassFactor p (z / a n) - 1) :=
    Summable.of_norm_bounded_eventually_nat (hs.mul_left _) hev
  simpa using Complex.multipliable_one_add_of_summable key

/-- **Borel's theorem (growth half).** If all `aₙ ≠ 0`, `0 < σ`, `p ≤ σ ≤ p + 1`
    and `∑ ‖aₙ‖^{-σ} < ∞`, then for every `z`
    `‖∏' n, Eₚ(z / aₙ)‖ ≤ exp (K · (∑' n, ‖aₙ‖^{-σ}) · ‖z‖^σ)`,
    `K = growthConst p σ`. -/
theorem norm_canonicalProduct_le {a : ℕ → ℂ} (p : ℕ) {σ : ℝ}
    (ha : ∀ n, a n ≠ 0) (hσ0 : 0 < σ) (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable (fun n => ‖a n‖ ^ (-σ))) (z : ℂ) :
    ‖∏' n, weierstrassFactor p (z / a n)‖
      ≤ Real.exp (growthConst p σ * (∑' n, ‖a n‖ ^ (-σ)) * ‖z‖ ^ σ) := by
  set K := growthConst p σ
  have hK : 0 ≤ K := (zero_le_one.trans (one_le_growthConst p hσ0))
  have hmult := multipliable_canonicalProduct_rpow p ha hσ0 hσp hs z
  have htend := (hmult.hasProd.tendsto_prod_nat).norm
  refine le_of_tendsto' htend fun N => ?_
  have hnn : ∀ n, 0 ≤ ‖a n‖ ^ (-σ) := fun n => Real.rpow_nonneg (norm_nonneg _) _
  calc ‖∏ i ∈ Finset.range N, weierstrassFactor p (z / a i)‖
      = ∏ i ∈ Finset.range N, ‖weierstrassFactor p (z / a i)‖ := norm_prod _ _
    _ ≤ ∏ i ∈ Finset.range N, Real.exp (K * ‖z / a i‖ ^ σ) :=
        Finset.prod_le_prod (fun i _ => norm_nonneg _)
          (fun i _ => norm_weierstrassFactor_le_exp_rpow p hσ0 hpσ hσp _)
    _ = Real.exp (∑ i ∈ Finset.range N, K * ‖z / a i‖ ^ σ) := (Real.exp_sum _ _).symm
    _ ≤ Real.exp (K * (∑' n, ‖a n‖ ^ (-σ)) * ‖z‖ ^ σ) := by
        apply Real.exp_le_exp.mpr
        have hpart : ∑ i ∈ Finset.range N, ‖a i‖ ^ (-σ) ≤ ∑' n, ‖a n‖ ^ (-σ) :=
          hs.sum_le_tsum _ (fun n _ => hnn n)
        have hrw : ∑ i ∈ Finset.range N, K * ‖z / a i‖ ^ σ
            = K * ‖z‖ ^ σ * ∑ i ∈ Finset.range N, ‖a i‖ ^ (-σ) := by
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl fun i _ => ?_
          rw [norm_div_rpow]; ring
        rw [hrw]
        have hc : 0 ≤ K * ‖z‖ ^ σ := mul_nonneg hK (Real.rpow_nonneg (norm_nonneg _) _)
        calc K * ‖z‖ ^ σ * ∑ i ∈ Finset.range N, ‖a i‖ ^ (-σ)
            ≤ K * ‖z‖ ^ σ * ∑' n, ‖a n‖ ^ (-σ) := mul_le_mul_of_nonneg_left hpart hc
          _ = K * (∑' n, ‖a n‖ ^ (-σ)) * ‖z‖ ^ σ := by ring

/-- **Borel's theorem.** Under the hypotheses of `norm_canonicalProduct_le`, the
    canonical product is entire of order `≤ σ`. -/
theorem isEntireOfOrderLE_canonicalProduct {a : ℕ → ℂ} (p : ℕ) {σ : ℝ}
    (ha : ∀ n, a n ≠ 0) (hσ0 : 0 < σ) (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable (fun n => ‖a n‖ ^ (-σ))) :
    IsEntireOfOrderLE (fun z => ∏' n, weierstrassFactor p (z / a n)) σ := by
  refine ⟨differentiable_canonicalProduct p ha hσ0 hσp hs,
    1, growthConst p σ * (∑' n, ‖a n‖ ^ (-σ)) + 1, ?_, ?_⟩
  · have hK := one_le_growthConst p hσ0
    have hS : 0 ≤ ∑' n, ‖a n‖ ^ (-σ) :=
      tsum_nonneg fun n => Real.rpow_nonneg (norm_nonneg _) _
    have : 0 ≤ growthConst p σ * (∑' n, ‖a n‖ ^ (-σ)) := by positivity
    linarith
  · intro z
    have hz : 0 ≤ ‖z‖ ^ σ := Real.rpow_nonneg (norm_nonneg _) _
    calc ‖∏' n, weierstrassFactor p (z / a n)‖
        ≤ Real.exp (growthConst p σ * (∑' n, ‖a n‖ ^ (-σ)) * ‖z‖ ^ σ) :=
          norm_canonicalProduct_le p ha hσ0 hpσ hσp hs z
      _ ≤ 1 * Real.exp ((growthConst p σ * (∑' n, ‖a n‖ ^ (-σ)) + 1) * ‖z‖ ^ σ) := by
          rw [one_mul]
          apply Real.exp_le_exp.mpr
          nlinarith

-- Ref: [leitner2026] standard: Conway, Functions of One Complex Variable I, XI §2 (Borel's theorem on the canonical product); Titchmarsh, The Theory of Functions, §8.21

end QOU.Mathlib.CanonicalProductGrowth
