import QOU.KZ.FuchsianConvergence
import Mathlib.Analysis.Calculus.SmoothSeries
import Mathlib.Analysis.SpecialFunctions.Exponential
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.Normed.Ring.InfiniteSum

/-!
# The analytic local solution `G(t) = H(t) · t^A`

Third brick of Step 1 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`. From the formal
solution of `QOU.KZ.FuchsianFormal` and the bound of `QOU.KZ.FuchsianConvergence` we build the
**actual solution** of the ODE on an interval `(0, r)`:

  `G(t) = H(t) · exp(log t · A)`,   `H(t) = ∑ t^k H_k`,

and prove `G'(t) = t⁻¹ M(t) G(t)` (`hasDerivAt_solution`), where `M(t) = ∑ t^k M_k`.

## How

* `H(t)` is differentiable termwise on `|t| < r` (`hasDerivAt_series`), by Mathlib's
  `hasDerivAt_tsum_of_isPreconnected` with the dominating series `∑ n s^{n-1} ‖H_n‖`.
* `t H'(t) + H(t) A = M(t) H(t)` (`gauge_series`) is the coefficient identity summed against
  `t^n`, using the Cauchy product in a complete normed algebra.
* `d/dt exp(log t · A) = t⁻¹ A exp(log t · A)`. Note that `A` lands on the **left** of the
  exponential, so `H · (A · E) = (H A) · E` needs no commutation, and the product rule closes.

For the three-point KZ system `M(t) = A − (t/(1−t)) B` (`series_kzM0`), so on `(0,1)`

  `G'(t) = (A/t + B/(t−1)) G(t)`   (`kz_hasDerivAt`),

with `G = H · t^A` normalised at `0`. By the symmetry `t ↦ 1 − t` (swap `A ↔ B`) the same theorem
gives the solution normalised at `1`. These two solutions are the input to the associator
`Φ_KZ = G₁(t)⁻¹ G₀(t)`.

## Not here

Invertibility of `G`, `t`-independence of `G₁⁻¹ G₀` (hence `Φ_KZ`), hexagon and pentagon.
Base: complete normed `ℝ`-algebra (archimedean by necessity: this is the analytic step). Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1, §5
-/

namespace QOU.KZ.FuchsianAnalytic

open Finset QOU.KZ.FuchsianFormal QOU.KZ.FuchsianConvergence

variable {R : Type*} [NormedRing R] [NormedAlgebra ℝ R] [CompleteSpace R]

/-- The sum `H(t) = ∑ t^k H_k`. -/
noncomputable def series (H : ℕ → R) (t : ℝ) : R := ∑' k, t ^ k • H k

/-- `H` has radius of convergence at least `r`, in the form produced by `bounded_weighted`. -/
def BoundedOn (H : ℕ → R) (r : ℝ) : Prop :=
  ∀ s, 0 < s → s < r → ∃ D, ∀ k, ‖H k‖ * s ^ k ≤ D

section Bounds

variable {H : ℕ → R} {r : ℝ}

omit [CompleteSpace R] in
theorem summable_norm_of_bounded (hb : BoundedOn H r) {t : ℝ} (ht : |t| < r) :
    Summable fun k => ‖t ^ k • H k‖ := by
  set s := (|t| + r) / 2
  have hs0 : 0 < s := by have := abs_nonneg t; simp only [s]; linarith
  obtain ⟨D, hD⟩ := hb s hs0 (by simp only [s]; linarith)
  have hq0 : 0 ≤ |t| / s := div_nonneg (abs_nonneg t) hs0.le
  have hq1 : |t| / s < 1 := (div_lt_one hs0).2 (by simp only [s]; linarith)
  clear_value s
  refine Summable.of_nonneg_of_le (fun k => norm_nonneg _) (fun k => ?_)
    ((summable_geometric_of_lt_one hq0 hq1).mul_left D)
  have hsk : 0 < s ^ k := pow_pos hs0 k
  calc ‖t ^ k • H k‖ = (‖H k‖ * s ^ k) * (|t| / s) ^ k := by
        rw [norm_smul, Real.norm_eq_abs, abs_pow, div_pow]; field_simp
    _ ≤ D * (|t| / s) ^ k := by gcongr; exact hD k

omit [NormedAlgebra ℝ R] [CompleteSpace R] in
theorem summable_deriv_bound (hb : BoundedOn H r) {s : ℝ} (hs0 : 0 < s) (hs : s < r) :
    Summable fun n : ℕ => (n : ℝ) * s ^ (n - 1) * ‖H n‖ := by
  set s' := (s + r) / 2
  have hs'0 : 0 < s' := by simp only [s']; linarith
  obtain ⟨D, hD⟩ := hb s' hs'0 (by simp only [s']; linarith)
  have hq0 : 0 ≤ s / s' := div_nonneg hs0.le hs'0.le
  have hq1 : s / s' < 1 := (div_lt_one hs'0).2 (by simp only [s']; linarith)
  clear_value s'
  have hsum := (summable_pow_mul_geometric_of_norm_lt_one 1
    (r := s / s') (by rw [Real.norm_eq_abs, abs_of_nonneg hq0]; exact hq1)).mul_left (D / s)
  refine Summable.of_nonneg_of_le (fun n => by positivity) (fun n => ?_) hsum
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · simp only [CharP.cast_eq_zero, zero_mul, pow_one, mul_zero]; rfl
  have hDn : ‖H n‖ ≤ D / s' ^ n := by
    rw [le_div_iff₀ (pow_pos hs'0 n)]; exact hD n
  have hD0 : 0 ≤ D := le_trans (by positivity) (hD 0)
  have e : s ^ (n - 1) = s ^ n / s := by
    rw [eq_div_iff hs0.ne', ← pow_succ]; congr 1; omega
  calc (n : ℝ) * s ^ (n - 1) * ‖H n‖ ≤ (n : ℝ) * s ^ (n - 1) * (D / s' ^ n) := by gcongr
    _ = D / s * ((n : ℝ) ^ 1 * (s / s') ^ n) := by rw [e, div_pow]; field_simp

end Bounds

/-- **Termwise differentiation** of `H(t) = ∑ t^k H_k` inside the radius of convergence. -/
theorem hasDerivAt_series {H : ℕ → R} {r : ℝ} (hb : BoundedOn H r) {t : ℝ} (ht : |t| < r) :
    HasDerivAt (series H) (∑' n : ℕ, ((n : ℝ) * t ^ (n - 1)) • H n) t := by
  set s := (|t| + r) / 2
  have hs0 : 0 < s := by have := abs_nonneg t; simp only [s]; linarith
  have hsr : s < r := by simp only [s]; linarith
  have hts : t ∈ Metric.ball (0 : ℝ) s := by
    rw [Metric.mem_ball, dist_zero_right, Real.norm_eq_abs]; simp only [s]; linarith
  unfold series
  refine hasDerivAt_tsum_of_isPreconnected (g := fun n y => y ^ n • H n)
    (g' := fun n y => ((n : ℝ) * y ^ (n - 1)) • H n) (summable_deriv_bound hb hs0 hsr) Metric.isOpen_ball
    (convex_ball _ _).isPreconnected (fun n y _ => (hasDerivAt_pow n y).smul_const (H n))
    (fun n y hy => ?_) (Metric.mem_ball_self hs0) ?_ hts
  · rw [Metric.mem_ball, dist_zero_right, Real.norm_eq_abs] at hy
    rw [norm_smul, Real.norm_eq_abs, abs_mul, Nat.abs_cast, abs_pow]
    gcongr
  · simpa using (summable_norm_of_bounded hb (t := 0) (by rw [abs_zero]; linarith)).of_norm

omit [CompleteSpace R] in
/-- `t · ∑ n t^{n-1} H_n = ∑ n t^n H_n`. -/
theorem smul_deriv_series (H : ℕ → R) (t : ℝ) :
    t • ∑' n : ℕ, ((n : ℝ) * t ^ (n - 1)) • H n = ∑' n : ℕ, ((n : ℝ) * t ^ n) • H n := by
  rw [← tsum_const_smul'']
  refine tsum_congr fun n => ?_
  rw [smul_smul]
  rcases n with _ | n
  · simp
  · congr 1; simp only [Nat.add_sub_cancel]; push_cast; ring

omit [CompleteSpace R] in
theorem summable_norm_n_series {H : ℕ → R} {r : ℝ} (hb : BoundedOn H r) {t : ℝ}
    (ht : |t| < r) : Summable fun n : ℕ => ‖((n : ℝ) * t ^ n) • H n‖ := by
  set s := (|t| + r) / 2
  have hs0 : 0 < s := by have := abs_nonneg t; simp only [s]; linarith
  have hsr : s < r := by simp only [s]; linarith
  have hts : |t| ≤ s := by simp only [s]; linarith
  refine Summable.of_nonneg_of_le (fun n => norm_nonneg _) (fun n => ?_)
    ((summable_deriv_bound hb hs0 hsr).mul_left |t|)
  rw [norm_smul, Real.norm_eq_abs, abs_mul, Nat.abs_cast, abs_pow]
  rcases n with _ | n
  · simp
  · have : |t| ^ (n + 1) ≤ |t| * s ^ n := by
      rw [pow_succ']; gcongr
    simp only [Nat.add_sub_cancel]
    calc ((n + 1 : ℕ) : ℝ) * |t| ^ (n + 1) * ‖H (n + 1)‖
        ≤ ((n + 1 : ℕ) : ℝ) * (|t| * s ^ n) * ‖H (n + 1)‖ := by gcongr
      _ = |t| * (((n + 1 : ℕ) : ℝ) * s ^ n * ‖H (n + 1)‖) := by ring

/-- **The gauge equation for the sums**: `t H'(t) + H(t) A = M(t) H(t)`. -/
theorem gauge_series {M H : ℕ → R} {r : ℝ} (hbM : BoundedOn M r) (hbH : BoundedOn H r)
    (hH : IsFormalGauge M H) {t : ℝ} (ht : |t| < r) :
    (∑' n : ℕ, ((n : ℝ) * t ^ n) • H n) + series H t * M 0 = series M t * series H t := by
  have sH := summable_norm_of_bounded hbH ht
  have sM := summable_norm_of_bounded hbM ht
  have sN := summable_norm_n_series hbH ht
  have sHA : Summable fun n => ‖t ^ n • (H n * M 0)‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
      (fun n => by rw [← smul_mul_assoc]; exact norm_mul_le _ _) (sH.mul_right ‖M 0‖)
  unfold series
  rw [tsum_mul_tsum_eq_tsum_sum_range_of_summable_norm sM sH, ← sH.of_norm.tsum_mul_right,
    ← sN.of_norm.tsum_add (sH.of_norm.mul_right (M 0))]
  refine tsum_congr fun n => ?_
  have hsum : ∑ k ∈ range (n + 1), t ^ k • M k * t ^ (n - k) • H (n - k)
      = t ^ n • ∑ j ∈ range (n + 1), M (n - j) * H j := by
    rw [smul_sum, ← sum_range_reflect (fun j => t ^ n • (M (n - j) * H j)) (n + 1)]
    refine sum_congr rfl fun k hk => ?_
    have hk := mem_range.1 hk
    have e1 : n + 1 - 1 - k = n - k := by omega
    have e2 : n - (n - k) = k := by omega
    have e3 : k + (n - k) = n := by omega
    simp only [e1, e2]
    rw [smul_mul_smul_comm, ← pow_add, e3]
  rw [hsum, ← hH n, smul_add, smul_mul_assoc]
  congr 1
  rw [natCast_mul_eq_smul (R := R) n (H n), smul_smul, mul_comm]

/-- `exp(log t · A)`, i.e. `t^A` for `t > 0`. -/
noncomputable def tpow (A : R) (t : ℝ) : R := NormedSpace.exp ℝ (Real.log t • A)

theorem hasDerivAt_tpow (A : R) {t : ℝ} (ht : 0 < t) :
    HasDerivAt (tpow A) (t⁻¹ • (A * tpow A t)) t :=
  (hasDerivAt_exp_smul_const' (𝕂 := ℝ) A (Real.log t)).scomp t (Real.hasDerivAt_log ht.ne')

/-- **The local solution at a regular singular point.** If `H` is the normalised formal solution
and both `M` and `H` converge on `|t| < r`, then `G(t) = H(t) t^A` satisfies
`G'(t) = t⁻¹ M(t) G(t)` on `(0, r)`. -/
theorem hasDerivAt_solution {M H : ℕ → R} {r : ℝ} (hbM : BoundedOn M r) (hbH : BoundedOn H r)
    (hH : IsFormalGauge M H) {t : ℝ} (ht0 : 0 < t) (ht : t < r) :
    HasDerivAt (fun u => series H u * tpow (M 0) u)
      (t⁻¹ • (series M t * (series H t * tpow (M 0) t))) t := by
  have hta : |t| < r := by rwa [abs_of_pos ht0]
  have hd := (hasDerivAt_series hbH hta).mul (hasDerivAt_tpow (M 0) ht0)
  convert hd using 1
  have hg := gauge_series hbM hbH hH hta
  rw [← smul_deriv_series] at hg
  rw [← mul_assoc, ← hg, add_mul, smul_add, smul_mul_assoc, smul_smul, inv_mul_cancel₀ ht0.ne',
    one_smul, mul_smul_comm, mul_assoc]

section KZ

omit [NormedAlgebra ℝ R] [CompleteSpace R] in
/-- The coefficient sequence of the three-point KZ system has bounded coefficients. -/
theorem boundedOn_kzM0 (A B : R) : BoundedOn (kzM0 A B) 1 := by
  intro s hs0 hs1
  refine ⟨max ‖A‖ ‖B‖, fun k => ?_⟩
  have hsk : s ^ k ≤ 1 := pow_le_one₀ hs0.le hs1.le
  have hk : ‖kzM0 A B k‖ ≤ max ‖A‖ ‖B‖ := by
    rcases k with _ | k
    · exact le_max_left _ _
    · simp only [kzM0, norm_neg]; exact le_max_right _ _
  calc ‖kzM0 A B k‖ * s ^ k ≤ max ‖A‖ ‖B‖ * 1 := by gcongr
    _ = _ := mul_one _

omit [CompleteSpace R] in
/-- The normalised formal solution of the three-point KZ system converges on `|t| < 1`. -/
theorem boundedOn_kz_solution (A B : R) (H : ℕ → R) (h0 : H 0 = 1)
    (hH : IsFormalGauge (kzM0 A B) H) : BoundedOn H 1 := by
  intro s hs0 hs1
  refine bounded_weighted (kzM0 A B) H h0 hH ‖B‖ 1 s (norm_nonneg _) zero_le_one hs0
    (by linarith) fun m hm => ?_
  obtain ⟨m, rfl⟩ : ∃ n, m = n + 1 := ⟨m - 1, by omega⟩
  simp [kzM0]

/-- `M(t) = A − (t/(1−t)) B` for the KZ coefficients. -/
theorem series_kzM0 (A B : R) {t : ℝ} (ht : |t| < 1) :
    series (kzM0 A B) t = A - (t / (1 - t)) • B := by
  have hs := (summable_norm_of_bounded (boundedOn_kzM0 A B) ht).of_norm
  unfold series
  rw [hs.tsum_eq_zero_add]
  have hg : HasSum (fun k : ℕ => t ^ (k + 1)) (t / (1 - t)) := by
    have := (hasSum_geometric_of_abs_lt_one ht).mul_left t
    simpa [pow_succ', div_eq_mul_inv] using this
  have : ∑' k : ℕ, t ^ (k + 1) • kzM0 A B (k + 1) = -((t / (1 - t)) • B) := by
    simp only [kzM0, smul_neg]
    rw [tsum_neg, (hg.smul_const B).tsum_eq]
  rw [this]; simp [kzM0, sub_eq_add_neg]

/-- **The KZ solution normalised at `0`.** For any residues `A, B` and the normalised formal
solution `H` (unique under non-resonance, `QOU.KZ.FuchsianFormal.kz_formal_solutions`),
`G(t) = H(t) t^A` solves `G' = (A/t + B/(t−1)) G` on `(0, 1)`. -/
theorem kz_hasDerivAt (A B : R) (H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge (kzM0 A B) H)
    {t : ℝ} (ht0 : 0 < t) (ht1 : t < 1) :
    HasDerivAt (fun u => series H u * tpow A u)
      ((t⁻¹ • A + (t - 1)⁻¹ • B) * (series H t * tpow A t)) t := by
  have h := hasDerivAt_solution (boundedOn_kzM0 A B) (boundedOn_kz_solution A B H h0 hH) hH
    ht0 ht1
  convert h using 1
  rw [series_kzM0 A B (by rw [abs_of_pos ht0]; exact ht1), ← smul_mul_assoc]
  congr 1
  have h1 : (1 - t) ≠ 0 := by linarith
  have h2 : (t - 1) ≠ 0 := by linarith
  rw [smul_sub, smul_smul, sub_eq_add_neg (t⁻¹ • A), ← neg_smul]
  congr 2
  field_simp
  ring

end KZ

end QOU.KZ.FuchsianAnalytic
