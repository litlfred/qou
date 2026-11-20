import QOU.Mathlib.CanonicalProductGrowth
import QOU.Mathlib.HadamardZeroFree
import Mathlib.Analysis.Complex.AbsMax
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Analysis.PSeries

/-!
# Minimum modulus of the canonical product, and the Hadamard degree bound

This file proves the analytic step of Hadamard's factorisation theorem that the rest of
`QOU.Mathlib` left open: if `f` is entire of order `≤ ρ` and `f = exp(g) · P`, where `P` is
the genus-`⌊ρ⌋₊` Weierstrass canonical product over a nonzero sequence `a` with
`∑ ‖aₙ‖^{-σ} < ∞` for every `σ > ρ`, and `g` is entire, then `g` is a polynomial of degree
`≤ ⌊ρ⌋₊`.

Route: the minimum-modulus route (R1) in the elementary form of Titchmarsh §8.22, with
the exclusion set chosen so that no Cartan/Boutroux lemma is needed.

## Proved here (sorry-free, no new axioms)

* **(A) one primary factor.**
  - `exp_neg_le_norm_weierstrassFactor_of_small`: `‖w‖ ≤ 1/2 → exp(-2‖w‖^{p+1}) ≤ ‖Eₚ(w)‖`,
    i.e. `log ‖Eₚ(w)‖ ≥ -2‖w‖^{p+1}`.
  - `norm_one_sub_mul_exp_le_norm_weierstrassFactor`: `‖w‖ ≥ 1/2 →
    ‖1 - w‖ · exp(-p·2^p·‖w‖^p) ≤ ‖Eₚ(w)‖`.
* **(B) the canonical product at a separated point.**
  `exp_neg_le_norm_canonicalProduct`: if `0 < σ`, `p ≤ σ ≤ p + 1`, `∑ ‖aₙ‖^{-σ} = S < ∞`,
  `‖z‖ ≥ 1/2` and `‖z - aₙ‖ ≥ ‖aₙ‖^{-σ}` for every `n`, then
  `‖∏' n, Eₚ(z/aₙ)‖ ≥ exp(-K(‖z‖) · S · ‖z‖^σ)` with
  `K(r) = 2 + p·2^{p+1} + (σ+1)·2^σ·log(2r)`. The zero count and the tail sum are both
  bounded through the single summability hypothesis, so no separate `n(r)` bound is used.
* **(C) separated circles.** `exists_separated_radius`: every window `[R, R + 2S + 1]`
  contains a radius `r` with `|r - ‖aₙ‖| > ‖aₙ‖^{-σ}` for all `n` (Lebesgue measure of the
  excluded set `≤ 2S`); `separated_of_norm_eq` puts every point of that circle at distance
  `≥ ‖aₙ‖^{-σ}` from every `aₙ`.
* **(D)/(E) the degree bound.** `norm_exp_le_of_eq_exp_mul_canonicalProduct`: on those
  circles `‖exp g‖ = ‖f‖/‖P‖` is bounded, the maximum modulus principle carries the bound
  inside, and the result is `‖exp(g z)‖ ≤ A' exp(C' ‖z‖^τ)` for every `τ > σ`.
  `exists_polynomial_of_eq_exp_mul_canonicalProduct` then applies the repository's
  Borel–Carathéodory transfer and generalised Liouville
  (`QOU.Mathlib.HadamardZeroFree.exists_norm_le_of_norm_exp_le`,
  `exists_polynomial_of_norm_le`) for every `τ > ρ`, and concludes `natDegree ≤ ⌊ρ⌋₊`
  by density. For integer `ρ` no finite-type hypothesis is needed: degree `≤ τ` for every
  `τ > ρ` already forces degree `≤ ρ`.
* A non-vacuity `example` (`aₙ = (n+1)²`, `ρ = 1`, `g = 0`, `f = P`).

## Not proved here

* That the zeros of `f` (with multiplicity) can be enumerated as such a sequence `a`, and
  that `f / P` is entire and zero-free, so that `g` exists. Those are the other halves of
  Hadamard's theorem; the theorem here takes the factorisation `f = exp(g) · P` and the
  summability of `‖aₙ‖^{-σ}` (`σ > ρ`) as hypotheses. The summability hypothesis is the
  conclusion of `QOU.Mathlib.ExponentOfConvergence` stated for a divisor, not yet for an
  enumeration; that bridge is not built here.
* Finitely many zeros (a polynomial factor) is not covered: `a` is an infinite sequence.
  A finite zero set can be padded only by changing `P`, which this file does not do.
* The class `HasHadamardFactorization` in `QOU.Mathlib.HadamardFactorization` is not
  discharged by this file.
  (Update 2026-11-20: `QOU.Mathlib.HadamardAssembly` generalises this argument to any
  countable index, finite or empty, and instantiates the class.)
* The constants are explicit and far from sharp; the classical `log ‖P‖ ≥ -K r^{ρ+ε}` off
  small discs (Cartan) is replaced by the weaker statement on a sequence of circles, which
  is all the degree bound needs.
-/

namespace QOU.Mathlib.HadamardMinimumModulus

open QOU.Mathlib.HadamardFactorization
open QOU.Mathlib.CanonicalProductGrowth
open QOU.Mathlib.WeierstrassFactorEstimate (expSum)

/-! ## (A) Lower bounds for one primary factor -/

/-- For `‖w‖ ≤ 1/2`, `exp (-2‖w‖^{p+1}) ≤ ‖Eₚ(w)‖`; equivalently
`log ‖Eₚ(w)‖ ≥ -2‖w‖^{p+1}`. -/
theorem exp_neg_le_norm_weierstrassFactor_of_small (p : ℕ) {w : ℂ} (hw : ‖w‖ ≤ 1 / 2) :
    Real.exp (-(2 * ‖w‖ ^ (p + 1))) ≤ ‖weierstrassFactor p w‖ := by
  set x := ‖w‖ ^ (p + 1) with hx
  have hw1 : ‖w‖ ≤ 1 := by linarith
  have hx0 : 0 ≤ x := by positivity
  have hxw : x ≤ ‖w‖ := by
    rw [hx]
    calc ‖w‖ ^ (p + 1) ≤ ‖w‖ ^ 1 := pow_le_pow_of_le_one (norm_nonneg w) hw1 (by omega)
      _ = ‖w‖ := pow_one _
  have hx12 : x ≤ 1 / 2 := hxw.trans hw
  have h1 : ‖1 - weierstrassFactor p w‖ ≤ x := norm_one_sub_weierstrassFactor_le p hw1
  have h2 : 1 - x ≤ ‖weierstrassFactor p w‖ := by
    have := norm_sub_norm_le (1 : ℂ) (weierstrassFactor p w)
    simp only [norm_one] at this
    linarith
  have h3 : 1 + 2 * x ≤ Real.exp (2 * x) := by
    have := Real.add_one_le_exp (2 * x); linarith
  have h4 : Real.exp (-(2 * x)) * Real.exp (2 * x) = 1 := by
    rw [← Real.exp_add]; simp
  have h5 : Real.exp (-(2 * x)) * (1 + 2 * x) ≤ 1 := by
    calc Real.exp (-(2 * x)) * (1 + 2 * x) ≤ Real.exp (-(2 * x)) * Real.exp (2 * x) :=
          mul_le_mul_of_nonneg_left h3 (Real.exp_pos _).le
      _ = 1 := h4
  have h6 : 1 ≤ (1 - x) * (1 + 2 * x) := by nlinarith
  have hpos : 0 < 1 + 2 * x := by linarith
  have h7 : Real.exp (-(2 * x)) ≤ 1 - x := by
    by_contra hc
    push_neg at hc
    have := mul_lt_mul_of_pos_right hc hpos
    linarith
  linarith

/-- For `1/2 ≤ t` and `k + 1 ≤ p`, `t^{k+1} ≤ 2^p t^p`. -/
theorem pow_le_two_pow_mul_pow {t : ℝ} (ht : 1 / 2 ≤ t) {k p : ℕ} (hk : k + 1 ≤ p) :
    t ^ (k + 1) ≤ 2 ^ p * t ^ p := by
  have ht0 : 0 ≤ t := by linarith
  rcases le_or_gt 1 t with h1 | h1
  · calc t ^ (k + 1) ≤ t ^ p := pow_le_pow_right₀ h1 hk
      _ = 1 * t ^ p := (one_mul _).symm
      _ ≤ 2 ^ p * t ^ p :=
          mul_le_mul_of_nonneg_right (one_le_pow₀ (by norm_num)) (by positivity)
  · calc t ^ (k + 1) ≤ 1 := pow_le_one₀ ht0 h1.le
      _ ≤ (2 * t) ^ p := one_le_pow₀ (by linarith)
      _ = 2 ^ p * t ^ p := mul_pow _ _ _

/-- `‖Sₚ(w)‖ ≤ p · 2^p · ‖w‖^p` for `‖w‖ ≥ 1/2`. -/
theorem norm_expSum_le (p : ℕ) {w : ℂ} (hw : 1 / 2 ≤ ‖w‖) :
    ‖expSum p w‖ ≤ p * 2 ^ p * ‖w‖ ^ p := by
  unfold expSum
  refine (norm_sum_le _ _).trans ?_
  have hterm : ∀ k ∈ Finset.range p, ‖w ^ (k + 1) / ((k : ℂ) + 1)‖ ≤ 2 ^ p * ‖w‖ ^ p := by
    intro k hk
    have hk' : k + 1 ≤ p := Finset.mem_range.mp hk
    have hkc : ((k : ℂ) + 1) = ((k + 1 : ℕ) : ℂ) := by push_cast; ring
    rw [hkc, norm_div, Complex.norm_natCast, norm_pow]
    have hk1 : (1 : ℝ) ≤ ((k + 1 : ℕ) : ℝ) := by exact_mod_cast Nat.succ_pos k
    calc ‖w‖ ^ (k + 1) / ((k + 1 : ℕ) : ℝ) ≤ ‖w‖ ^ (k + 1) :=
          div_le_self (by positivity) hk1
      _ ≤ 2 ^ p * ‖w‖ ^ p := pow_le_two_pow_mul_pow hw hk'
  calc ∑ k ∈ Finset.range p, ‖w ^ (k + 1) / ((k : ℂ) + 1)‖
      ≤ ∑ _k ∈ Finset.range p, 2 ^ p * ‖w‖ ^ p := Finset.sum_le_sum hterm
    _ = p * 2 ^ p * ‖w‖ ^ p := by simp; ring

/-- For `‖w‖ ≥ 1/2`, `‖1 - w‖ · exp (-p·2^p·‖w‖^p) ≤ ‖Eₚ(w)‖`; equivalently
`log ‖Eₚ(w)‖ ≥ log ‖1 - w‖ - p·2^p·‖w‖^p`. -/
theorem norm_one_sub_mul_exp_le_norm_weierstrassFactor (p : ℕ) {w : ℂ} (hw : 1 / 2 ≤ ‖w‖) :
    ‖1 - w‖ * Real.exp (-(p * 2 ^ p * ‖w‖ ^ p)) ≤ ‖weierstrassFactor p w‖ := by
  have hdef : weierstrassFactor p w = (1 - w) * Complex.exp (expSum p w) := rfl
  rw [hdef, norm_mul, Complex.norm_exp]
  refine mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr ?_) (norm_nonneg _)
  have h1 := norm_expSum_le p hw
  have h2 : -‖expSum p w‖ ≤ (expSum p w).re :=
    (abs_le.mp (Complex.abs_re_le_norm (expSum p w))).1
  linarith

/-! ## (B) Lower bound for the canonical product at separated points -/

/-- The constant of the minimum-modulus estimate at radius `r`:
`2 + p·2^{p+1} + (σ+1)·2^σ·log(2r)`. -/
noncomputable def minModConst (p : ℕ) (σ r : ℝ) : ℝ :=
  2 + p * 2 ^ (p + 1) + (σ + 1) * 2 ^ σ * Real.log (2 * r)

theorem two_le_minModConst (p : ℕ) {σ r : ℝ} (hσ : 0 ≤ σ) (hr : 1 / 2 ≤ r) :
    2 ≤ minModConst p σ r := by
  unfold minModConst
  have hlog : 0 ≤ Real.log (2 * r) := Real.log_nonneg (by linarith)
  have : 0 ≤ (σ + 1) * 2 ^ σ * Real.log (2 * r) := by positivity
  have : (0 : ℝ) ≤ p * 2 ^ (p + 1) := by positivity
  linarith

/-- For `0 < t`, `p ≤ σ ≤ p + 1` and `t ≥ 1/2`: `t^p ≤ 2 t^σ`. -/
theorem pow_le_two_mul_rpow {t σ : ℝ} {p : ℕ} (ht : 1 / 2 ≤ t) (hpσ : (p : ℝ) ≤ σ)
    (hσp : σ ≤ (p : ℝ) + 1) : t ^ p ≤ 2 * t ^ σ := by
  have ht0 : 0 ≤ t := by linarith
  have hσ0 : 0 ≤ σ := le_trans (Nat.cast_nonneg p) hpσ
  rcases le_or_gt 1 t with h1 | h1
  · have : t ^ p ≤ t ^ σ := by
      rw [← Real.rpow_natCast]
      exact Real.rpow_le_rpow_of_exponent_le h1 hpσ
    have : 0 ≤ t ^ σ := Real.rpow_nonneg ht0 σ
    linarith
  · have hs := pow_succ_le_rpow_of_le_one p ht0 h1.le hσ0 hσp
    rw [pow_succ] at hs
    have : 0 ≤ t ^ p := by positivity
    nlinarith

/-- **Per-factor minimum modulus.** If `b ≠ 0`, `‖z‖ ≥ 1/2`, `p ≤ σ ≤ p + 1`, `0 < σ`,
and `z` is separated from `b` by `‖z - b‖ ≥ ‖b‖^{-σ}`, then
`exp (-K · ‖z/b‖^σ) ≤ ‖Eₚ(z/b)‖` with `K = minModConst p σ ‖z‖`. -/
theorem exp_neg_le_norm_weierstrassFactor_div (p : ℕ) {σ : ℝ} (hσ0 : 0 < σ)
    (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1) {z b : ℂ} (hb : b ≠ 0)
    (hz : 1 / 2 ≤ ‖z‖) (hsep : ‖b‖ ^ (-σ) ≤ ‖z - b‖) :
    Real.exp (-(minModConst p σ ‖z‖ * ‖z / b‖ ^ σ)) ≤ ‖weierstrassFactor p (z / b)‖ := by
  set r := ‖z‖ with hr
  set t := ‖z / b‖ with ht
  set K := minModConst p σ r with hK
  have hbpos : 0 < ‖b‖ := norm_pos_iff.mpr hb
  have ht0 : 0 ≤ t := norm_nonneg _
  have hX : 0 ≤ t ^ σ := Real.rpow_nonneg ht0 σ
  have hK2 : 2 ≤ K := two_le_minModConst p hσ0.le hz
  have hlog : 0 ≤ Real.log (2 * r) := Real.log_nonneg (by linarith)
  rcases le_or_gt t (1 / 2) with hsmall | hlarge
  · -- small `t`: the Weierstrass estimate
    have h1 := exp_neg_le_norm_weierstrassFactor_of_small p hsmall
    have h2 : t ^ (p + 1) ≤ t ^ σ :=
      pow_succ_le_rpow_of_le_one p ht0 (by linarith) hσ0.le hσp
    refine le_trans (Real.exp_le_exp.mpr ?_) h1
    nlinarith
  · -- large `t`: the separation controls the linear factor
    have h1 := norm_one_sub_mul_exp_le_norm_weierstrassFactor p hlarge.le
    -- `‖1 - z/b‖ ≥ exp (-(σ+1) log (2r))`
    have hb2r : ‖b‖ ≤ 2 * r := by
      have : t = r / ‖b‖ := by rw [ht, hr, norm_div]
      rw [this, lt_div_iff₀ hbpos] at hlarge
      linarith
    have hlin : Real.exp (-((σ + 1) * Real.log (2 * r))) ≤ ‖1 - z / b‖ := by
      have heq : 1 - z / b = (b - z) / b := by field_simp
      rw [heq, norm_div, norm_sub_rev]
      have hrp : ‖b‖ ^ (-σ) / ‖b‖ = Real.exp (-((σ + 1) * Real.log ‖b‖)) := by
        rw [Real.rpow_def_of_pos hbpos]
        conv_lhs => rw [show ‖b‖ = Real.exp (Real.log ‖b‖) from (Real.exp_log hbpos).symm]
        rw [Real.log_exp, ← Real.exp_sub]
        congr 1; ring
      have hlogb : Real.log ‖b‖ ≤ Real.log (2 * r) := Real.log_le_log hbpos hb2r
      calc Real.exp (-((σ + 1) * Real.log (2 * r)))
          ≤ Real.exp (-((σ + 1) * Real.log ‖b‖)) := by
            apply Real.exp_le_exp.mpr
            have : 0 ≤ σ + 1 := by linarith
            nlinarith
        _ = ‖b‖ ^ (-σ) / ‖b‖ := hrp.symm
        _ ≤ ‖z - b‖ / ‖b‖ := div_le_div_of_nonneg_right hsep hbpos.le
    have hcomb : Real.exp (-((σ + 1) * Real.log (2 * r) + p * 2 ^ p * t ^ p))
        ≤ ‖weierstrassFactor p (z / b)‖ := by
      calc Real.exp (-((σ + 1) * Real.log (2 * r) + p * 2 ^ p * t ^ p))
          = Real.exp (-((σ + 1) * Real.log (2 * r))) * Real.exp (-(p * 2 ^ p * t ^ p)) := by
            rw [← Real.exp_add]; ring_nf
        _ ≤ ‖1 - z / b‖ * Real.exp (-(p * 2 ^ p * t ^ p)) :=
            mul_le_mul_of_nonneg_right hlin (Real.exp_pos _).le
        _ ≤ ‖weierstrassFactor p (z / b)‖ := h1
    refine le_trans (Real.exp_le_exp.mpr ?_) hcomb
    -- `(σ+1) log(2r) + p 2^p t^p ≤ K t^σ`
    have hA : t ^ p ≤ 2 * t ^ σ := pow_le_two_mul_rpow hlarge.le hpσ hσp
    have hB : 1 ≤ 2 ^ σ * t ^ σ := by
      rw [← Real.mul_rpow (by norm_num) ht0]
      exact Real.one_le_rpow (by linarith) hσ0.le
    have hc1 : 0 ≤ (σ + 1) * Real.log (2 * r) := by
      have : 0 ≤ σ + 1 := by linarith
      positivity
    have h1' : (σ + 1) * Real.log (2 * r) ≤ (σ + 1) * Real.log (2 * r) * (2 ^ σ * t ^ σ) := by
      have := mul_le_mul_of_nonneg_left hB hc1
      linarith
    have hc2 : (0 : ℝ) ≤ p * 2 ^ p := by positivity
    have h2' : p * 2 ^ p * t ^ p ≤ p * 2 ^ p * (2 * t ^ σ) := mul_le_mul_of_nonneg_left hA hc2
    have hKX : K * t ^ σ = 2 * t ^ σ + p * 2 ^ p * (2 * t ^ σ)
        + (σ + 1) * Real.log (2 * r) * (2 ^ σ * t ^ σ) := by
      rw [hK]; unfold minModConst; rw [pow_succ]; ring
    nlinarith

/-- **Minimum modulus of the canonical product at a separated point.** Let all `aₙ ≠ 0`,
`0 < σ`, `p ≤ σ ≤ p + 1`, `∑ ‖aₙ‖^{-σ} = S < ∞`. If `‖z‖ ≥ 1/2` and `z` is separated from
every zero, `‖z - aₙ‖ ≥ ‖aₙ‖^{-σ}`, then
`exp (-K · S · ‖z‖^σ) ≤ ‖∏' n, Eₚ(z/aₙ)‖`, `K = minModConst p σ ‖z‖`. -/
theorem exp_neg_le_norm_canonicalProduct {a : ℕ → ℂ} (p : ℕ) {σ : ℝ}
    (ha : ∀ n, a n ≠ 0) (hσ0 : 0 < σ) (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable (fun n => ‖a n‖ ^ (-σ))) {z : ℂ} (hz : 1 / 2 ≤ ‖z‖)
    (hsep : ∀ n, ‖a n‖ ^ (-σ) ≤ ‖z - a n‖) :
    Real.exp (-(minModConst p σ ‖z‖ * (∑' n, ‖a n‖ ^ (-σ)) * ‖z‖ ^ σ))
      ≤ ‖∏' n, weierstrassFactor p (z / a n)‖ := by
  set K := minModConst p σ ‖z‖
  have hK : 0 ≤ K := le_trans (by norm_num) (two_le_minModConst p hσ0.le hz)
  have hmult := multipliable_canonicalProduct_rpow p ha hσ0 hσp hs z
  have htend := (hmult.hasProd.tendsto_prod_nat).norm
  refine ge_of_tendsto' htend fun N => ?_
  have hnn : ∀ n, 0 ≤ ‖a n‖ ^ (-σ) := fun n => Real.rpow_nonneg (norm_nonneg _) _
  have hpart : ∑ i ∈ Finset.range N, ‖a i‖ ^ (-σ) ≤ ∑' n, ‖a n‖ ^ (-σ) :=
    hs.sum_le_tsum _ (fun n _ => hnn n)
  have hrw : ∑ i ∈ Finset.range N, K * ‖z / a i‖ ^ σ
      = K * ‖z‖ ^ σ * ∑ i ∈ Finset.range N, ‖a i‖ ^ (-σ) := by
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [norm_div_rpow]; ring
  have hc : 0 ≤ K * ‖z‖ ^ σ := mul_nonneg hK (Real.rpow_nonneg (norm_nonneg _) _)
  calc Real.exp (-(K * (∑' n, ‖a n‖ ^ (-σ)) * ‖z‖ ^ σ))
      ≤ Real.exp (∑ i ∈ Finset.range N, -(K * ‖z / a i‖ ^ σ)) := by
        apply Real.exp_le_exp.mpr
        rw [Finset.sum_neg_distrib, hrw]
        have := mul_le_mul_of_nonneg_left hpart hc
        linarith
    _ = ∏ i ∈ Finset.range N, Real.exp (-(K * ‖z / a i‖ ^ σ)) := Real.exp_sum _ _
    _ ≤ ∏ i ∈ Finset.range N, ‖weierstrassFactor p (z / a i)‖ :=
        Finset.prod_le_prod (fun i _ => (Real.exp_pos _).le)
          (fun i _ => exp_neg_le_norm_weierstrassFactor_div p hσ0 hpσ hσp (ha i) hz (hsep i))
    _ = ‖∏ i ∈ Finset.range N, weierstrassFactor p (z / a i)‖ := (norm_prod _ _).symm

/-! ## (C) Existence of separated circles -/

/-- **Separated radii exist in every window.** If `∑ ‖aₙ‖^{-σ} = S < ∞`, every interval
`[R, R + 2S + 1]` contains a radius `r` with `|r - ‖aₙ‖| > ‖aₙ‖^{-σ}` for every `n`: the
excluded radii form a union of intervals of total length `≤ 2S`. -/
theorem exists_separated_radius {a : ℕ → ℂ} {σ : ℝ} (hs : Summable (fun n => ‖a n‖ ^ (-σ)))
    (R : ℝ) :
    ∃ r ∈ Set.Icc R (R + 2 * (∑' n, ‖a n‖ ^ (-σ)) + 1),
      ∀ n, ‖a n‖ ^ (-σ) < |r - ‖a n‖| := by
  set δ : ℕ → ℝ := fun n => ‖a n‖ ^ (-σ) with hδ
  set S := ∑' n, δ n with hS
  have hδ0 : ∀ n, 0 ≤ δ n := fun n => Real.rpow_nonneg (norm_nonneg _) _
  have hS0 : 0 ≤ S := tsum_nonneg hδ0
  by_contra hcon
  push_neg at hcon
  have hsub : Set.Icc R (R + 2 * S + 1) ⊆ ⋃ n, Set.Icc (‖a n‖ - δ n) (‖a n‖ + δ n) := by
    intro r hr
    obtain ⟨n, hn⟩ := hcon r hr
    refine Set.mem_iUnion.mpr ⟨n, ?_⟩
    have := abs_le.mp hn
    constructor <;> linarith [this.1, this.2]
  have hvol := MeasureTheory.measure_mono (μ := MeasureTheory.volume) hsub
  have hU : MeasureTheory.volume (⋃ n, Set.Icc (‖a n‖ - δ n) (‖a n‖ + δ n))
      ≤ ENNReal.ofReal (2 * S) := by
    refine (MeasureTheory.measure_iUnion_le _).trans ?_
    simp only [Real.volume_Icc]
    have h2 : ∀ n, ‖a n‖ + δ n - (‖a n‖ - δ n) = 2 * δ n := fun n => by ring
    simp only [h2]
    rw [← ENNReal.ofReal_tsum_of_nonneg (fun n => by linarith [hδ0 n]) (hs.mul_left 2),
      tsum_mul_left]
  rw [Real.volume_Icc] at hvol
  have hlt : ENNReal.ofReal (2 * S) < ENNReal.ofReal (R + 2 * S + 1 - R) :=
    (ENNReal.ofReal_lt_ofReal_iff (by linarith)).mpr (by linarith)
  exact absurd (hvol.trans hU) (not_le.mpr hlt)

/-- On a separated circle, every point is separated from every zero. -/
theorem separated_of_norm_eq {a : ℕ → ℂ} {σ r : ℝ}
    (hr : ∀ n, ‖a n‖ ^ (-σ) < |r - ‖a n‖|) {z : ℂ} (hz : ‖z‖ = r) (n : ℕ) :
    ‖a n‖ ^ (-σ) ≤ ‖z - a n‖ := by
  have := abs_norm_sub_norm_le z (a n)
  rw [hz] at this
  linarith [hr n]

/-! ## (D) Real-variable bookkeeping -/

/-- For `v ≥ 1`, `0 ≤ σ < τ`, `ρ ≤ τ`, `0 ≤ C`, `0 ≤ S`:
`C v^ρ + K(v) · S · v^σ ≤ D · v^τ`, `K(v) = minModConst p σ v`, with the explicit `D`
below (the `log(2v)` in `K(v)` is absorbed by the gap `τ - σ`). -/
noncomputable def growthD (p : ℕ) (σ τ C S : ℝ) : ℝ :=
  C + (2 + p * 2 ^ (p + 1)) * S + (σ + 1) * 2 ^ σ * S * (2 ^ (τ - σ) / (τ - σ))

theorem growthD_nonneg (p : ℕ) {σ τ C S : ℝ} (hσ : 0 ≤ σ) (hστ : σ < τ) (hC : 0 ≤ C)
    (hS : 0 ≤ S) : 0 ≤ growthD p σ τ C S := by
  unfold growthD
  have hε : 0 < τ - σ := by linarith
  have : 0 ≤ (σ + 1) * 2 ^ σ * S * (2 ^ (τ - σ) / (τ - σ)) := by
    have : 0 ≤ σ + 1 := by linarith
    positivity
  have : 0 ≤ (2 + p * 2 ^ (p + 1)) * S := by positivity
  linarith

theorem exponent_le_growthD (p : ℕ) {ρ σ τ C S v : ℝ} (hv : 1 ≤ v) (hσ : 0 ≤ σ)
    (hστ : σ < τ) (hρτ : ρ ≤ τ) (hC : 0 ≤ C) (hS : 0 ≤ S) :
    C * v ^ ρ + minModConst p σ v * S * v ^ σ ≤ growthD p σ τ C S * v ^ τ := by
  have hv0 : 0 < v := by linarith
  set ε := τ - σ with hε
  have hεpos : 0 < ε := by linarith
  have h1 : v ^ ρ ≤ v ^ τ := Real.rpow_le_rpow_of_exponent_le hv hρτ
  have h2 : v ^ σ ≤ v ^ τ := Real.rpow_le_rpow_of_exponent_le hv hστ.le
  have h3 : Real.log (2 * v) * v ^ σ ≤ 2 ^ ε / ε * v ^ τ := by
    have hl := Real.log_le_rpow_div (by linarith : (0 : ℝ) ≤ 2 * v) hεpos
    rw [Real.mul_rpow (by norm_num) hv0.le] at hl
    have hvσ : 0 ≤ v ^ σ := Real.rpow_nonneg hv0.le σ
    have hτ : v ^ ε * v ^ σ = v ^ τ := by
      rw [← Real.rpow_add hv0]; congr 1; rw [hε]; ring
    calc Real.log (2 * v) * v ^ σ ≤ 2 ^ ε * v ^ ε / ε * v ^ σ :=
          mul_le_mul_of_nonneg_right hl hvσ
      _ = 2 ^ ε / ε * (v ^ ε * v ^ σ) := by ring
      _ = 2 ^ ε / ε * v ^ τ := by rw [hτ]
  have hsplit : minModConst p σ v * S * v ^ σ
      = (2 + p * 2 ^ (p + 1)) * S * v ^ σ
        + (σ + 1) * 2 ^ σ * S * (Real.log (2 * v) * v ^ σ) := by
    unfold minModConst; ring
  have hD : growthD p σ τ C S * v ^ τ
      = C * v ^ τ + (2 + p * 2 ^ (p + 1)) * S * v ^ τ
        + (σ + 1) * 2 ^ σ * S * (2 ^ ε / ε * v ^ τ) := by
    unfold growthD; rw [← hε]; ring
  rw [hsplit, hD]
  have hc1 : 0 ≤ (2 + p * 2 ^ (p + 1)) * S := by positivity
  have hc2 : 0 ≤ (σ + 1) * 2 ^ σ * S := by
    have : 0 ≤ σ + 1 := by linarith
    positivity
  have e1 := mul_le_mul_of_nonneg_left h1 hC
  have e2 := mul_le_mul_of_nonneg_left h2 hc1
  have e3 := mul_le_mul_of_nonneg_left h3 hc2
  nlinarith

/-- `(u + M)^τ ≤ 2^τ (u^τ + M^τ)` for `u, M, τ ≥ 0`. -/
theorem add_rpow_le_two_rpow_mul {u M τ : ℝ} (hu : 0 ≤ u) (hM : 0 ≤ M) (hτ : 0 ≤ τ) :
    (u + M) ^ τ ≤ 2 ^ τ * (u ^ τ + M ^ τ) := by
  have huτ : 0 ≤ u ^ τ := Real.rpow_nonneg hu τ
  have hMτ : 0 ≤ M ^ τ := Real.rpow_nonneg hM τ
  have h2 : (0 : ℝ) ≤ 2 ^ τ := Real.rpow_nonneg (by norm_num) τ
  rcases le_total u M with h | h
  · calc (u + M) ^ τ ≤ (2 * M) ^ τ := Real.rpow_le_rpow (by linarith) (by linarith) hτ
      _ = 2 ^ τ * M ^ τ := Real.mul_rpow (by norm_num) hM
      _ ≤ 2 ^ τ * (u ^ τ + M ^ τ) := mul_le_mul_of_nonneg_left (by linarith) h2
  · calc (u + M) ^ τ ≤ (2 * u) ^ τ := Real.rpow_le_rpow (by linarith) (by linarith) hτ
      _ = 2 ^ τ * u ^ τ := Real.mul_rpow (by norm_num) hu
      _ ≤ 2 ^ τ * (u ^ τ + M ^ τ) := mul_le_mul_of_nonneg_left (by linarith) h2

/-! ## (E) Growth of `exp g`, and the Hadamard degree bound -/

/-- **Growth transfer through the canonical product.** If `f = exp(g) · P` with `P` the
genus-`p` canonical product over `a` (`∑ ‖aₙ‖^{-σ} < ∞`, `0 < σ`, `p ≤ σ ≤ p + 1`), `g`
entire, and `‖f z‖ ≤ A exp (C ‖z‖^ρ)`, then for every `τ > σ` with `τ ≥ ρ`, `exp ∘ g` obeys
`‖exp (g z)‖ ≤ A' exp (C' ‖z‖^τ)`. No lower bound on `P` or `Re g` is assumed: it is
produced by `exp_neg_le_norm_canonicalProduct` on the separated circles of
`exists_separated_radius`, and propagated inside by the maximum modulus principle. -/
theorem norm_exp_le_of_eq_exp_mul_canonicalProduct {f g : ℂ → ℂ} {a : ℕ → ℂ} (p : ℕ)
    {ρ σ τ A C : ℝ} (hg : Differentiable ℂ g) (ha : ∀ n, a n ≠ 0) (hσ0 : 0 < σ)
    (hpσ : (p : ℝ) ≤ σ) (hσp : σ ≤ (p : ℝ) + 1) (hs : Summable (fun n => ‖a n‖ ^ (-σ)))
    (hρτ : ρ ≤ τ) (hστ : σ < τ) (hC : 0 < C)
    (hbound : ∀ z, ‖f z‖ ≤ A * Real.exp (C * ‖z‖ ^ ρ))
    (hfac : ∀ z, f z = Complex.exp (g z) * ∏' n, weierstrassFactor p (z / a n)) :
    ∃ A' C' : ℝ, 0 < A' ∧ 0 < C' ∧
      ∀ z, ‖Complex.exp (g z)‖ ≤ A' * Real.exp (C' * ‖z‖ ^ τ) := by
  set S := ∑' n, ‖a n‖ ^ (-σ) with hSdef
  have hS : 0 ≤ S := tsum_nonneg fun n => Real.rpow_nonneg (norm_nonneg _) _
  set M : ℝ := 2 * S + 2 with hM
  have hM0 : 0 ≤ M := by linarith
  set A1 := max A 1 with hA1
  have hA1pos : 0 < A1 := lt_of_lt_of_le one_pos (le_max_right _ _)
  set D := growthD p σ τ C S with hDdef
  have hD : 0 ≤ D := growthD_nonneg p hσ0.le hστ hC.le hS
  have hτ0 : 0 ≤ τ := by linarith
  have h2τ : (0 : ℝ) ≤ 2 ^ τ := Real.rpow_nonneg (by norm_num) τ
  refine ⟨A1 * Real.exp (D * 2 ^ τ * M ^ τ), D * 2 ^ τ + 1,
    mul_pos hA1pos (Real.exp_pos _), by positivity, fun z => ?_⟩
  obtain ⟨r, ⟨hr1, hr2⟩, hsep⟩ := exists_separated_radius hs (max ‖z‖ 1)
  have hrge : 1 ≤ r := le_trans (le_max_right _ _) hr1
  have hzr : ‖z‖ ≤ r := le_trans (le_max_left _ _) hr1
  have hrM : r ≤ ‖z‖ + M := by
    have : max ‖z‖ 1 ≤ ‖z‖ + 1 := max_le (by linarith) (by linarith [norm_nonneg z])
    rw [hM]; linarith
  have hr0 : 0 < r := by linarith
  -- the bound on the separated circle
  set B := C * r ^ ρ + minModConst p σ r * S * r ^ σ with hB
  have hcircle : ∀ w ∈ frontier (Metric.ball (0 : ℂ) r),
      ‖Complex.exp (g w)‖ ≤ A1 * Real.exp B := by
    intro w hw
    rw [frontier_ball _ hr0.ne', mem_sphere_zero_iff_norm] at hw
    have hP := exp_neg_le_norm_canonicalProduct p ha hσ0 hpσ hσp hs
      (by rw [hw]; norm_num; linarith) (separated_of_norm_eq hsep hw)
    rw [hw] at hP
    set P := ∏' n, weierstrassFactor p (w / a n)
    set e := ‖Complex.exp (g w)‖
    have he : 0 ≤ e := norm_nonneg _
    have hfw : e * ‖P‖ ≤ A1 * Real.exp (C * r ^ ρ) := by
      have h1 := hbound w
      rw [hfac w, norm_mul, hw] at h1
      exact h1.trans (mul_le_mul_of_nonneg_right (le_max_left _ _) (Real.exp_pos _).le)
    set E := minModConst p σ r * S * r ^ σ
    have hmul : e * Real.exp (-E) ≤ A1 * Real.exp (C * r ^ ρ) :=
      le_trans (mul_le_mul_of_nonneg_left hP he) hfw
    have hEE : Real.exp (-E) * Real.exp E = 1 := by rw [← Real.exp_add]; simp
    calc e = e * Real.exp (-E) * Real.exp E := by rw [mul_assoc, hEE, mul_one]
      _ ≤ A1 * Real.exp (C * r ^ ρ) * Real.exp E :=
          mul_le_mul_of_nonneg_right hmul (Real.exp_pos _).le
      _ = A1 * Real.exp B := by rw [mul_assoc, ← Real.exp_add]
  have hzmem : z ∈ closure (Metric.ball (0 : ℂ) r) := by
    rw [closure_ball _ hr0.ne']; simpa using hzr
  have hmax := Complex.norm_le_of_forall_mem_frontier_norm_le Metric.isBounded_ball
    (hg.cexp.diffContOnCl) hcircle hzmem
  refine hmax.trans ?_
  -- real bookkeeping
  have hBD : B ≤ D * r ^ τ := exponent_le_growthD p hrge hσ0.le hστ hρτ hC.le hS
  have hrτ : r ^ τ ≤ (‖z‖ + M) ^ τ := Real.rpow_le_rpow hr0.le hrM hτ0
  have hsum := add_rpow_le_two_rpow_mul (norm_nonneg z) hM0 hτ0
  have hzτ : 0 ≤ ‖z‖ ^ τ := Real.rpow_nonneg (norm_nonneg _) τ
  have hfin : B ≤ D * 2 ^ τ * M ^ τ + (D * 2 ^ τ + 1) * ‖z‖ ^ τ := by
    have e1 := mul_le_mul_of_nonneg_left hrτ hD
    have e2 := mul_le_mul_of_nonneg_left hsum hD
    nlinarith
  calc A1 * Real.exp B ≤ A1 * Real.exp (D * 2 ^ τ * M ^ τ + (D * 2 ^ τ + 1) * ‖z‖ ^ τ) :=
        mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr hfin) hA1pos.le
    _ = A1 * Real.exp (D * 2 ^ τ * M ^ τ) * Real.exp ((D * 2 ^ τ + 1) * ‖z‖ ^ τ) := by
        rw [Real.exp_add]; ring

/-- **The Hadamard degree bound (the step `qou-n4pv` / `qou-kp89` was missing).**
Let `0 ≤ ρ`, `p = ⌊ρ⌋₊`, `a : ℕ → ℂ` nonzero with `∑ ‖aₙ‖^{-σ} < ∞` for every `σ > ρ`, and
`P(z) = ∏' n, Eₚ(z/aₙ)`. If `f` is entire of order `≤ ρ` and `f = exp(g) · P` with `g`
entire, then `g` is a polynomial of degree `≤ ⌊ρ⌋₊` (equivalently `≤ ρ`).

Nothing is assumed about the zeros of `f` beyond the factorisation itself, and no lower
bound on `‖P‖` or `Re g` is assumed. -/
theorem exists_polynomial_of_eq_exp_mul_canonicalProduct {f g : ℂ → ℂ} {a : ℕ → ℂ} {ρ : ℝ}
    (hρ : 0 ≤ ρ) (hf : IsEntireOfOrderLE f ρ) (hg : Differentiable ℂ g) (ha : ∀ n, a n ≠ 0)
    (hs : ∀ σ, ρ < σ → Summable (fun n => ‖a n‖ ^ (-σ)))
    (hfac : ∀ z, f z = Complex.exp (g z) * ∏' n, weierstrassFactor ⌊ρ⌋₊ (z / a n)) :
    ∃ Q : Polynomial ℂ, Q.natDegree ≤ ⌊ρ⌋₊ ∧ ∀ z, g z = Q.eval z := by
  obtain ⟨_, A, C, hC, hbound⟩ := hf
  set p := ⌊ρ⌋₊ with hp
  have hpρ : (p : ℝ) ≤ ρ := Nat.floor_le hρ
  have hρp : ρ < (p : ℝ) + 1 := Nat.lt_floor_add_one ρ
  -- for every `τ > ρ`, `g` is a polynomial of degree `≤ τ`
  have key : ∀ τ, ρ < τ → ∃ Q : Polynomial ℂ, (Q.natDegree : ℝ) ≤ τ ∧ ∀ z, g z = Q.eval z := by
    intro τ hτ
    set σ := min (ρ + (τ - ρ) / 2) ((p : ℝ) + 1) with hσ
    have hσρ : ρ < σ := lt_min (by linarith) hρp
    have hστ : σ < τ := lt_of_le_of_lt (min_le_left _ _) (by linarith)
    have hσp : σ ≤ (p : ℝ) + 1 := min_le_right _ _
    have hσ0 : 0 < σ := lt_of_le_of_lt hρ hσρ
    obtain ⟨A', C', hA', hC', hb⟩ := norm_exp_le_of_eq_exp_mul_canonicalProduct p hg ha hσ0
      (le_trans hpρ hσρ.le) hσp (hs σ hσρ) hτ.le hστ hC hbound hfac
    have hτ0 : 0 ≤ τ := by linarith
    obtain ⟨K, hK⟩ := QOU.Mathlib.HadamardZeroFree.exists_norm_le_of_norm_exp_le hg hτ0 hC' hA' hb
    exact QOU.Mathlib.HadamardZeroFree.exists_polynomial_of_norm_le hg hτ0 hK
  obtain ⟨Q, -, hQ⟩ := key (ρ + 1) (by linarith)
  refine ⟨Q, ?_, hQ⟩
  have hdeg : (Q.natDegree : ℝ) ≤ ρ := by
    refine le_of_forall_gt_imp_ge_of_dense fun τ hτ => ?_
    obtain ⟨Q', hQ'deg, hQ'⟩ := key τ hτ
    have heq : Q' = Q := Polynomial.funext fun z => by rw [← hQ' z, hQ z]
    rw [← heq]; exact hQ'deg
  exact Nat.le_floor hdeg

/-! ## Non-vacuity -/

/-- The zero sequence `aₙ = (n+1)²` has `∑ ‖aₙ‖^{-σ} < ∞` for every `σ ≥ 1`. -/
theorem summable_sq_rpow_neg {σ : ℝ} (hσ : 1 ≤ σ) :
    Summable (fun n : ℕ => ‖(((n : ℂ) + 1) ^ 2)‖ ^ (-σ)) := by
  have hbase : Summable (fun n : ℕ => 1 / ((n : ℝ) + 1) ^ 2) := by
    have := (summable_nat_add_iff 1).mpr ((Real.summable_one_div_nat_pow (p := 2)).mpr (by norm_num))
    simpa using this
  refine hbase.of_nonneg_of_le (fun n => Real.rpow_nonneg (norm_nonneg _) _) fun n => ?_
  have hn : (1 : ℝ) ≤ (n : ℝ) + 1 := by have := Nat.cast_nonneg (α := ℝ) n; linarith
  have hnorm : ‖(((n : ℂ) + 1) ^ 2)‖ = ((n : ℝ) + 1) ^ 2 := by
    rw [norm_pow]; congr 1
    rw [show ((n : ℂ) + 1) = (((n : ℝ) + 1 : ℝ) : ℂ) by push_cast; ring, Complex.norm_real,
      Real.norm_of_nonneg (by linarith)]
  rw [hnorm]
  have h1 : (1 : ℝ) ≤ ((n : ℝ) + 1) ^ 2 := one_le_pow₀ hn
  calc (((n : ℝ) + 1) ^ 2) ^ (-σ) ≤ (((n : ℝ) + 1) ^ 2) ^ (-1 : ℝ) :=
        Real.rpow_le_rpow_of_exponent_le h1 (by linarith)
    _ = 1 / ((n : ℝ) + 1) ^ 2 := by rw [Real.rpow_neg_one, one_div]

/-- **Non-vacuity of `exists_polynomial_of_eq_exp_mul_canonicalProduct`.** With
`aₙ = (n+1)²`, `ρ = 1`, `g = 0` and `f = P` (Borel's theorem supplies the order bound),
every hypothesis holds, and the theorem returns a polynomial of degree `≤ 1`. -/
example : ∃ Q : Polynomial ℂ, Q.natDegree ≤ ⌊(1 : ℝ)⌋₊ ∧ ∀ z : ℂ, (0 : ℂ) = Q.eval z := by
  have hfl : ⌊(1 : ℝ)⌋₊ = 1 := by simp
  have ha : ∀ n : ℕ, ((n : ℂ) + 1) ^ 2 ≠ 0 := fun n =>
    pow_ne_zero 2 (by exact_mod_cast Nat.succ_ne_zero n)
  have hP : IsEntireOfOrderLE
      (fun z => ∏' n : ℕ, weierstrassFactor 1 (z / ((n : ℂ) + 1) ^ 2)) 1 :=
    isEntireOfOrderLE_canonicalProduct (a := fun n : ℕ => ((n : ℂ) + 1) ^ 2) 1 ha one_pos
      (by norm_num) (by norm_num) (summable_sq_rpow_neg le_rfl)
  exact exists_polynomial_of_eq_exp_mul_canonicalProduct (g := fun _ => 0) zero_le_one hP
    (differentiable_const _) ha (fun σ hσ => summable_sq_rpow_neg hσ.le)
    (fun z => by simp [hfl])

-- Ref: [leitner2026] standard: Titchmarsh, The Theory of Functions, §8.22–8.24; Conway, Functions of One Complex Variable I, XI §3

end QOU.Mathlib.HadamardMinimumModulus
