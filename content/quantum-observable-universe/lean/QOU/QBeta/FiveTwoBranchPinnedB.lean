import QOU.QBeta.FiveTwoEnvelopeWiring

/-!
# The *other* branch integer: `Σⱼ log(1 − yⱼ/x) = −log x`

Bean `qou-trns`. `sum_dVdx_of_pinned` takes **two** pinned log-sums, and only one
of them was proved. `FiveTwoBranchPinned` gave `Σⱼ log(1 − x·yⱼ) = log x`; this
file gives the companion. It became visible only once the first was written —
which is the point of writing joins out rather than calling them assembly.

## It is the same argument, mirrored

On `|x| = 1` we have `x⁻¹ = conj x`, so

    (y/x).im = y.im·x.re − y.re·x.im ,

and comparing with `(x·y).im = x.re·y.im + x.im·y.re` shows the two differ by
conjugating `y`. Since the extra roots are either both real or a conjugate pair,
**the same two facts** that gave `Im(x·y₃) < 0` and `Im(x·y₂) < 0` give
`Im(y₂/x) > 0` and `Im(y₃/x) > 0`. Nothing new is measured or assumed:
`im_div_otherRoots_fst_pos` re-runs the `sa_lt_cb` case split against the
mirrored quantity.

The window mirrors too. `Σⱼ arg(1 − yⱼ/x) = −φ + 2π·k₂`, and

| input | source |
|---|---|
| `arg(1 − t/x) ∈ (0, π/2)` | `(t/x).im = −t·x.im < 0` and `(t/x).re = t·x.re < 1` |
| `arg(1 − y₂/x) ≤ 0` | `Im(y₂/x) > 0` |
| when `φ > π/2`, also `arg(1 − y₃/x) ≤ 0` | `Im(y₃/x) > 0` once `c < 0` |

giving `Σ ∈ (−φ − 2π, −φ + 2π)` and `k₂ = 0`.

Route 27 G5 observed numerically that `k₂ = −k₁` because the two sums are
complex conjugates on the open arc. That is true and is why one expects this to
work — but it is *not* what is proved here. Formalising it would need the root
multiset to be conjugation-closed **as a permutation**; mirroring the sector
argument needs no such thing, so that is what is done.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Real Complex

/-! ### 1. Components of `y/x` on the unit circle -/

theorem normSq_eq_one {x : ℂ} (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) : Complex.normSq x = 1 := by
  simp only [Complex.normSq_apply]; nlinarith [hxnorm]

/-- On `|x| = 1`, `x⁻¹ = conj x`, so the imaginary part of `y/x` is this. -/
theorem div_im_of_normSq_one {x y : ℂ} (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) :
    (y / x).im = y.im * x.re - y.re * x.im := by
  rw [div_eq_mul_inv, Complex.mul_im, Complex.inv_re, Complex.inv_im, normSq_eq_one hxnorm]
  ring

theorem div_re_of_normSq_one {x y : ℂ} (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) :
    (y / x).re = y.re * x.re + y.im * x.im := by
  rw [div_eq_mul_inv, Complex.mul_re, Complex.inv_re, Complex.inv_im, normSq_eq_one hxnorm]
  ring

/-! ### 2. The mirrored sign facts -/

/-- The mirror of `im_mul_otherRoots_snd_neg`: `Im(y₂/x) > 0`. Same case split,
same two inputs. -/
theorem im_div_otherRoots_fst_pos {c t : ℝ} (hc : c ≤ 1) (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0) {x : ℂ} (hxre : x.re = c) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) :
    0 < ((otherRoots (t - 2 * c) (t ^ 2 - 2 * c * t + 2 * c + 1)).1 / x).im := by
  set β := t - 2 * c with hβdef
  set γ := t ^ 2 - 2 * c * t + 2 * c + 1 with hγdef
  have hconst := gamma_rel hp
  have hγpos : 0 < γ := by rw [hγdef]; nlinarith
  rw [div_im_of_normSq_one hxnorm]
  unfold otherRoots
  split_ifs with h
  · -- real pair: the root is negative, so `−r·x.im > 0`
    have hW := W_nonneg_of_disc_nonneg hc ht0 ht1 hp h
    have hb := beta_rel hp
    have ht1t : 0 < t * (1 - t) := by nlinarith
    have hβ0 : 0 < β := by
      rcases lt_or_eq_of_le (by nlinarith : (0:ℝ) ≤ β) with hlt | heq
      · exact hlt
      · exfalso; rw [← heq] at h; nlinarith
    have hlt : Real.sqrt (β ^ 2 - 4 * γ) < β := (Real.sqrt_lt' hβ0).mpr (by nlinarith)
    have hroot : (-β + Real.sqrt (β ^ 2 - 4 * γ)) / 2 < 0 := by linarith
    simp only [Complex.ofReal_re, Complex.ofReal_im, zero_mul, zero_sub, neg_pos]
    exact mul_neg_of_neg_of_pos hroot hxim
  · -- conjugate pair: `b·c − a·s = −(s·a − c·b) > 0` by `sa_lt_cb`
    have h' : (0 : ℝ) ≤ 4 * γ - β ^ 2 := by linarith
    set b := Real.sqrt (4 * γ - β ^ 2) / 2 with hbdef
    have hb0 : 0 < b := by
      rw [hbdef]
      have : 0 < 4 * γ - β ^ 2 := by linarith
      positivity
    have hbsq : b ^ 2 = (4 * γ - β ^ 2) / 4 := by
      rw [hbdef, div_pow, Real.sq_sqrt h']; norm_num
    have hR : γ = (-β / 2) ^ 2 + b ^ 2 := by rw [hbsq]; ring
    have h1 : 2 * c * γ = 1 + 2 * (-β / 2) * γ := by rw [hβdef]; linear_combination hconst
    have h2 : 2 * (-β / 2) * (γ - 1) = γ ^ 2 - γ - 1 := by
      have hb' := beta_rel hp
      rw [hβdef, hγdef] at *
      nlinarith [hconst, hb', sq_nonneg t]
    have hkey := sa_lt_cb hb0 hxim hR (hxre ▸ h1) h2 hxnorm
    simp only [Complex.add_re, Complex.add_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.mul_re, Complex.mul_im, Complex.I_re, Complex.I_im]
    rw [hxre]
    nlinarith [hkey]

/-- The mirror of `im_mul_otherRoots_fst_neg`: `Im(y₃/x) > 0` once `c < 0`. -/
theorem im_div_otherRoots_snd_pos {c t : ℝ} (hc : c ≤ 1) (hcneg : c < 0)
    (ht0 : 0 < t) (ht1 : t < 1)
    (hp : unitCubic c t = 0) {x : ℂ} (hxre : x.re = c) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) :
    0 < ((otherRoots (t - 2 * c) (t ^ 2 - 2 * c * t + 2 * c + 1)).2 / x).im := by
  set β := t - 2 * c with hβdef
  set γ := t ^ 2 - 2 * c * t + 2 * c + 1 with hγdef
  have hconst := gamma_rel hp
  have hγpos : 0 < γ := by rw [hγdef]; nlinarith
  rw [div_im_of_normSq_one hxnorm]
  unfold otherRoots
  split_ifs with h
  · have hW := W_nonneg_of_disc_nonneg hc ht0 ht1 hp h
    have hb := beta_rel hp
    have ht1t : 0 < t * (1 - t) := by nlinarith
    have hβ0 : 0 < β := by
      rcases lt_or_eq_of_le (by nlinarith : (0:ℝ) ≤ β) with hlt | heq
      · exact hlt
      · exfalso; rw [← heq] at h; nlinarith
    have hsnn : 0 ≤ Real.sqrt (β ^ 2 - 4 * γ) := Real.sqrt_nonneg _
    have hroot : (-β - Real.sqrt (β ^ 2 - 4 * γ)) / 2 < 0 := by linarith
    simp only [Complex.ofReal_re, Complex.ofReal_im, zero_mul, zero_sub, neg_pos]
    exact mul_neg_of_neg_of_pos hroot hxim
  · have h' : (0 : ℝ) ≤ 4 * γ - β ^ 2 := by linarith
    set b := Real.sqrt (4 * γ - β ^ 2) / 2 with hbdef
    have hb0 : 0 < b := by
      rw [hbdef]
      have : 0 < 4 * γ - β ^ 2 := by linarith
      positivity
    have hbsq : b ^ 2 = (4 * γ - β ^ 2) / 4 := by
      rw [hbdef, div_pow, Real.sq_sqrt h']; norm_num
    have hR : γ = (-β / 2) ^ 2 + b ^ 2 := by rw [hbsq]; ring
    have h1 : 2 * c * γ = 1 + 2 * (-β / 2) * γ := by rw [hβdef]; linear_combination hconst
    have h2 : 2 * (-β / 2) * (γ - 1) = γ ^ 2 - γ - 1 := by
      have hb' := beta_rel hp
      rw [hβdef, hγdef] at *
      nlinarith [hconst, hb', sq_nonneg t]
    have hkey := sa_lt_cb hb0 hxim hR (hxre ▸ h1) h2 hxnorm
    have hcb : c * b < 0 := mul_neg_of_neg_of_pos hcneg hb0
    simp only [Complex.sub_re, Complex.sub_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.mul_re, Complex.mul_im, Complex.I_re, Complex.I_im]
    rw [hxre]
    nlinarith [hkey, hcb]

/-! ### 3. The mirrored window -/

/-- `arg(1 − t/x) ∈ (0, π/2)` for the positive real root. -/
theorem arg_pos_real_root_div {x : ℂ} {t : ℝ}
    (hxim : 0 < x.im) (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) (ht0 : 0 < t) (ht1 : t < 1) :
    0 < (1 - (t : ℂ) / x).arg ∧ (1 - (t : ℂ) / x).arg < π / 2 := by
  have hxre : x.re ≤ 1 := by nlinarith
  have him : 0 < (1 - (t : ℂ) / x).im := by
    rw [Complex.sub_im, Complex.one_im, div_im_of_normSq_one hxnorm]
    simp only [Complex.ofReal_re, Complex.ofReal_im, zero_mul, zero_sub, sub_neg_eq_add,
      zero_add]
    nlinarith
  have hre : 0 < (1 - (t : ℂ) / x).re := by
    rw [Complex.sub_re, Complex.one_re, div_re_of_normSq_one hxnorm]
    simp only [Complex.ofReal_re, Complex.ofReal_im, zero_mul, add_zero, sub_pos]
    nlinarith
  refine ⟨?_, ?_⟩
  · exact lt_of_le_of_ne (Complex.arg_nonneg_iff.mpr him.le)
      (fun hz => absurd (Complex.arg_eq_zero_iff.mp hz.symm).2 (by simpa using him.ne'))
  · exact (abs_lt.mp (Complex.abs_arg_lt_pi_div_two_iff.mpr (Or.inl hre))).2

/-- **The mirrored window.** -/
theorem sum_window_B {a₁ a₂ a₃ φ : ℝ} (hφ0 : 0 ≤ φ) (hφπ : φ < π)
    (h1lo : 0 < a₁) (h1hi : a₁ < π / 2)
    (h2lo : -π < a₂) (h2hi : a₂ ≤ 0)
    (h3lo : -π < a₃) (h3hi : a₃ ≤ π)
    (hbig : π / 2 < φ → a₃ ≤ 0) :
    -φ - 2 * π < a₁ + a₂ + a₃ ∧ a₁ + a₂ + a₃ < -φ + 2 * π := by
  refine ⟨by linarith, ?_⟩
  rcases le_or_gt φ (π / 2) with h | h
  · linarith
  · have := hbig h; linarith

/-- **The second branch integer vanishes.** -/
theorem branchInt_eq_zero_of_roots_B {x : ℂ} {t : ℝ} {y₂ y₃ : ℂ} {φ : ℝ} {k : ℤ}
    (hxim : 0 < x.im) (hxnorm : x.re ^ 2 + x.im ^ 2 = 1)
    (ht0 : 0 < t) (ht1 : t < 1)
    (h2 : 0 < (y₂ / x).im)
    (hbig : π / 2 < φ → 0 < (y₃ / x).im)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π)
    (h : (1 - (t : ℂ) / x).arg + (1 - y₂ / x).arg + (1 - y₃ / x).arg = -φ + 2 * π * k) :
    k = 0 := by
  obtain ⟨h1lo, h1hi⟩ := arg_pos_real_root_div hxim hxnorm ht0 ht1
  have hneg : ∀ z : ℂ, 0 < z.im → (1 - z).arg ≤ 0 := fun z hz =>
    (Complex.arg_neg_iff.mpr (by simpa using hz)).le
  obtain ⟨hlo, hhi⟩ := sum_window_B hφ0 hφπ h1lo h1hi
    (Complex.neg_pi_lt_arg _) (hneg _ h2)
    (Complex.neg_pi_lt_arg _) (Complex.arg_le_pi _)
    (fun hb => hneg _ (hbig hb))
  exact branchInt_eq_zero_of_window (φ := -φ) hlo hhi h

/-! ### 4. The pinning -/

/-- `exp(A + log x) = 1` pins `Im A` to `−arg x` modulo `2π`. -/
theorem exists_int_im_eq_add {A x : ℂ} (h : Complex.exp (A + Complex.log x) = 1) :
    ∃ k : ℤ, A + Complex.log x = k * (2 * π * Complex.I) ∧ A.im = -x.arg + 2 * π * k := by
  obtain ⟨n, hn⟩ := Complex.exp_eq_one_iff.mp h
  refine ⟨n, hn, ?_⟩
  have hrw : (n : ℂ) * (2 * (π : ℂ) * Complex.I) = ((2 * π * n : ℝ) : ℂ) * Complex.I := by
    push_cast; ring
  rw [hrw] at hn
  have him := congrArg Complex.im hn
  simp only [Complex.add_im, Complex.log_im, Complex.mul_im,
    Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im] at him
  linarith

theorem eq_neg_log_of_branchInt_eq_zero {A x : ℂ} (h : Complex.exp (A + Complex.log x) = 1)
    (hk : ∀ k : ℤ, A.im = -x.arg + 2 * π * k → k = 0) : A = -Complex.log x := by
  obtain ⟨n, hn, him⟩ := exists_int_im_eq_add h
  rw [hk n him] at hn
  have hz : A + Complex.log x = 0 := by simpa using hn
  linear_combination hz

/-- **`Σⱼ log(1 − yⱼ/x) = −log x`** — the second input to `sum_dVdx_of_pinned`. -/
theorem logSumB_eq_neg_log {x : ℂ} {t : ℝ} {y₂ y₃ : ℂ} {φ : ℝ}
    (hx : x ≠ 0)
    (hc₁ : (1 : ℂ) - (t : ℂ) / x ≠ 0) (hc₂ : (1 : ℂ) - y₂ / x ≠ 0)
    (hc₃ : (1 : ℂ) - y₃ / x ≠ 0)
    (hv₁ : x * ((t : ℂ) + y₂ + y₃) = x ^ 2 + 1)
    (hv₂ : x * ((t : ℂ) * y₂ + (t : ℂ) * y₃ + y₂ * y₃) = x ^ 2 + x + 1)
    (hv₃ : (t : ℂ) * y₂ * y₃ = 1)
    (hxim : 0 < x.im) (hxnorm : x.re ^ 2 + x.im ^ 2 = 1)
    (ht0 : 0 < t) (ht1 : t < 1)
    (h2 : 0 < (y₂ / x).im) (hbig : π / 2 < φ → 0 < (y₃ / x).im)
    (hφ0 : 0 ≤ φ) (hφπ : φ < π) (hxarg : x.arg = φ) :
    Complex.log (1 - (t : ℂ) / x) + Complex.log (1 - y₂ / x) + Complex.log (1 - y₃ / x)
      = -Complex.log x := by
  refine eq_neg_log_of_branchInt_eq_zero
    (exp_logSumB_add_log_eq_one hx hc₁ hc₂ hc₃ hv₁ hv₂ hv₃) ?_
  intro k hk
  rw [im_logSum, hxarg] at hk
  exact branchInt_eq_zero_of_roots_B (t := t) (y₂ := y₂) (y₃ := y₃)
    hxim hxnorm ht0 ht1 h2 hbig hφ0 hφπ hk

end QOU.QBeta.FiveTwoDeformedSaddle
