import QOU.KZ.AssociatorKZ
import Mathlib.Analysis.SpecialFunctions.Complex.LogDeriv

/-!
# The three-point KZ equation in the complex domain

First brick of the hexagon for `Φ_KZ` (Step 1 of
`docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`). The hexagon compares solutions of

  `G'(z) = Ω(z) G(z)`,   `Ω(z) = A/z + B/(z − 1)`,

continued into the upper half-plane, so the real-variable theory of `QOU.KZ.FuchsianAnalytic` and
`QOU.KZ.AssociatorKZ` is redone here with a **complex** variable, in a complete normed
`ℂ`-algebra `R`.

* `cseries H z = ∑ z^k H_k` is complex-differentiable inside its radius (`hasDerivAt_cseries`);
  the convergence estimates of `QOU.KZ.FuchsianConvergence` are reused unchanged.
* `cpowA A z = exp(log z · A)` with the principal logarithm, `d/dz z^A = z⁻¹ A z^A` on the slit
  plane (`hasDerivAt_cpowA`).
* `G₀(z) = H₀(z) z^A` solves KZ on the slit unit disc `D₀`, and `G₁(z) = H₁(1 − z)(1 − z)^B` on
  the slit disc `D₁` about `1` (`isKZSolOn_G₀`, `isKZSolOn_G₁`).
* **Uniqueness on convex sets** (`eqOn_of_convex`): for any `Ω` continuous on a convex `U`, two
  solutions agreeing at a point agree on `U`. Restrict to the real segment from that point and
  apply Mathlib's Gronwall uniqueness `ODE_solution_unique_of_mem_Icc_right`. With one invertible
  value this gives the connection constant (`eqOn_mul_of_isUnit`).

Base: complete normed `ℂ`-algebra (archimedean by necessity). Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1, §5
-/

namespace QOU.KZ.KZComplex

open Set Finset QOU.KZ.FuchsianFormal QOU.KZ.FuchsianConvergence QOU.KZ.FuchsianAnalytic

variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

/-- The sum `H(z) = ∑ z^k H_k` for complex `z`. -/
noncomputable def cseries (H : ℕ → R) (z : ℂ) : R := ∑' k, z ^ k • H k

section Bounds

variable {H : ℕ → R} {r : ℝ}

omit [CompleteSpace R] in
theorem summable_norm_cseries (hb : BoundedOn H r) {z : ℂ} (hz : ‖z‖ < r) :
    Summable fun k => ‖z ^ k • H k‖ := by
  set s := (‖z‖ + r) / 2
  have hs0 : 0 < s := by have := norm_nonneg z; simp only [s]; linarith
  obtain ⟨D, hD⟩ := hb s hs0 (by simp only [s]; linarith)
  have hq0 : 0 ≤ ‖z‖ / s := div_nonneg (norm_nonneg z) hs0.le
  have hq1 : ‖z‖ / s < 1 := (div_lt_one hs0).2 (by simp only [s]; linarith)
  clear_value s
  refine Summable.of_nonneg_of_le (fun k => norm_nonneg _) (fun k => ?_)
    ((summable_geometric_of_lt_one hq0 hq1).mul_left D)
  have hsk : 0 < s ^ k := pow_pos hs0 k
  calc ‖z ^ k • H k‖ = (‖H k‖ * s ^ k) * (‖z‖ / s) ^ k := by
        rw [norm_smul, norm_pow, div_pow]; field_simp
    _ ≤ D * (‖z‖ / s) ^ k := by gcongr; exact hD k

omit [CompleteSpace R] in
theorem summable_norm_n_cseries (hb : BoundedOn H r) {z : ℂ}
    (hz : ‖z‖ < r) : Summable fun n : ℕ => ‖((n : ℂ) * z ^ n) • H n‖ := by
  set s := (‖z‖ + r) / 2
  have hs0 : 0 < s := by have := norm_nonneg z; simp only [s]; linarith
  have hsr : s < r := by simp only [s]; linarith
  have hzs : ‖z‖ ≤ s := by simp only [s]; linarith
  refine Summable.of_nonneg_of_le (fun n => norm_nonneg _) (fun n => ?_)
    ((summable_deriv_bound hb hs0 hsr).mul_left ‖z‖)
  rw [norm_smul, norm_mul, Complex.norm_natCast, norm_pow]
  rcases n with _ | n
  · simp
  · have : ‖z‖ ^ (n + 1) ≤ ‖z‖ * s ^ n := by
      rw [pow_succ']; gcongr
    simp only [Nat.add_sub_cancel]
    calc ((n + 1 : ℕ) : ℝ) * ‖z‖ ^ (n + 1) * ‖H (n + 1)‖
        ≤ ((n + 1 : ℕ) : ℝ) * (‖z‖ * s ^ n) * ‖H (n + 1)‖ := by gcongr
      _ = ‖z‖ * (((n + 1 : ℕ) : ℝ) * s ^ n * ‖H (n + 1)‖) := by ring

end Bounds

/-- **Termwise complex differentiation** of `H(z) = ∑ z^k H_k` inside the radius. -/
theorem hasDerivAt_cseries {H : ℕ → R} {r : ℝ} (hb : BoundedOn H r) {z : ℂ} (hz : ‖z‖ < r) :
    HasDerivAt (cseries H) (∑' n : ℕ, ((n : ℂ) * z ^ (n - 1)) • H n) z := by
  set s := (‖z‖ + r) / 2
  have hs0 : 0 < s := by have := norm_nonneg z; simp only [s]; linarith
  have hsr : s < r := by simp only [s]; linarith
  have hzs : z ∈ Metric.ball (0 : ℂ) s := by
    rw [Metric.mem_ball, dist_zero_right]; simp only [s]; linarith
  unfold cseries
  refine hasDerivAt_tsum_of_isPreconnected (g := fun n y => y ^ n • H n)
    (g' := fun n y => ((n : ℂ) * y ^ (n - 1)) • H n) (summable_deriv_bound hb hs0 hsr)
    Metric.isOpen_ball (convex_ball _ _).isPreconnected
    (fun n y _ => (hasDerivAt_pow n y).smul_const (H n)) (fun n y hy => ?_)
    (Metric.mem_ball_self hs0) ?_ hzs
  · rw [Metric.mem_ball, dist_zero_right] at hy
    rw [norm_smul, norm_mul, Complex.norm_natCast, norm_pow]
    gcongr
  · simpa using (summable_norm_cseries hb (z := 0) (by rw [norm_zero]; linarith)).of_norm

omit [CompleteSpace R] in
theorem smul_deriv_cseries (H : ℕ → R) (z : ℂ) :
    z • ∑' n : ℕ, ((n : ℂ) * z ^ (n - 1)) • H n = ∑' n : ℕ, ((n : ℂ) * z ^ n) • H n := by
  rw [← tsum_const_smul'']
  refine tsum_congr fun n => ?_
  rw [smul_smul]
  rcases n with _ | n
  · simp
  · congr 1; simp only [Nat.add_sub_cancel]; push_cast; ring

omit [CompleteSpace R] in
theorem natCast_mul_eq_csmul (k : ℕ) (X : R) : (k : R) * X = (k : ℂ) • X := by
  rw [Nat.cast_smul_eq_nsmul, nsmul_eq_mul]

/-- `z H'(z) + H(z) A = M(z) H(z)` for complex `z`. -/
theorem gauge_cseries {M H : ℕ → R} {r : ℝ} (hbM : BoundedOn M r) (hbH : BoundedOn H r)
    (hH : IsFormalGauge M H) {z : ℂ} (hz : ‖z‖ < r) :
    (∑' n : ℕ, ((n : ℂ) * z ^ n) • H n) + cseries H z * M 0 = cseries M z * cseries H z := by
  have sH := summable_norm_cseries hbH hz
  have sM := summable_norm_cseries hbM hz
  have sN := summable_norm_n_cseries hbH hz
  have sHA : Summable fun n => ‖z ^ n • (H n * M 0)‖ :=
    Summable.of_nonneg_of_le (fun _ => norm_nonneg _)
      (fun n => by rw [← smul_mul_assoc]; exact norm_mul_le _ _) (sH.mul_right ‖M 0‖)
  unfold cseries
  rw [tsum_mul_tsum_eq_tsum_sum_range_of_summable_norm sM sH, ← sH.of_norm.tsum_mul_right,
    ← sN.of_norm.tsum_add (sH.of_norm.mul_right (M 0))]
  refine tsum_congr fun n => ?_
  have hsum : ∑ k ∈ range (n + 1), z ^ k • M k * z ^ (n - k) • H (n - k)
      = z ^ n • ∑ j ∈ range (n + 1), M (n - j) * H j := by
    rw [smul_sum, ← sum_range_reflect (fun j => z ^ n • (M (n - j) * H j)) (n + 1)]
    refine sum_congr rfl fun k hk => ?_
    have hk := mem_range.1 hk
    have e1 : n + 1 - 1 - k = n - k := by omega
    have e2 : n - (n - k) = k := by omega
    have e3 : k + (n - k) = n := by omega
    simp only [e1, e2]
    rw [smul_mul_smul_comm, ← pow_add, e3]
  rw [hsum, ← hH n, smul_add, smul_mul_assoc]
  congr 1
  rw [natCast_mul_eq_csmul n (H n), smul_smul, mul_comm]

/-- `z^A = exp(log z · A)` with the principal logarithm. -/
noncomputable def cpowA (A : R) (z : ℂ) : R := NormedSpace.exp ℂ (Complex.log z • A)

theorem hasDerivAt_cpowA (A : R) {z : ℂ} (hz : z ∈ Complex.slitPlane) :
    HasDerivAt (cpowA A) (z⁻¹ • (A * cpowA A z)) z :=
  (hasDerivAt_exp_smul_const' (𝕂 := ℂ) A (Complex.log z)).scomp z (Complex.hasDerivAt_log hz)

theorem isUnit_cpowA (A : R) (z : ℂ) : IsUnit (cpowA A z) := NormedSpace.isUnit_exp ℂ _

/-- **The complex local solution** `G(z) = H(z) z^A` on the slit disc. -/
theorem hasDerivAt_csolution {M H : ℕ → R} {r : ℝ} (hbM : BoundedOn M r) (hbH : BoundedOn H r)
    (hH : IsFormalGauge M H) {z : ℂ} (hz0 : z ∈ Complex.slitPlane) (hz : ‖z‖ < r) :
    HasDerivAt (fun u => cseries H u * cpowA (M 0) u)
      (z⁻¹ • (cseries M z * (cseries H z * cpowA (M 0) z))) z := by
  have hd := (hasDerivAt_cseries hbH hz).mul (hasDerivAt_cpowA (M 0) hz0)
  convert hd using 1
  have hg := gauge_cseries hbM hbH hH hz
  rw [← smul_deriv_cseries] at hg
  rw [← mul_assoc, ← hg, add_mul, smul_add, smul_mul_assoc, smul_smul,
    inv_mul_cancel₀ (Complex.slitPlane_ne_zero hz0), one_smul, mul_smul_comm, mul_assoc]

section KZ

/-- `M(z) = A − (z/(1−z)) B` for the KZ coefficients, `‖z‖ < 1`. -/
theorem cseries_kzM0 (A B : R) {z : ℂ} (hz : ‖z‖ < 1) :
    cseries (kzM0 A B) z = A - (z / (1 - z)) • B := by
  have hs := (summable_norm_cseries (boundedOn_kzM0 A B) hz).of_norm
  unfold cseries
  rw [hs.tsum_eq_zero_add]
  have hg : HasSum (fun k : ℕ => z ^ (k + 1)) (z / (1 - z)) := by
    have := (hasSum_geometric_of_norm_lt_one hz).mul_left z
    simpa [pow_succ', div_eq_mul_inv] using this
  have : ∑' k : ℕ, z ^ (k + 1) • kzM0 A B (k + 1) = -((z / (1 - z)) • B) := by
    simp only [kzM0, smul_neg]
    rw [tsum_neg, (hg.smul_const B).tsum_eq]
  rw [this]; simp [kzM0, sub_eq_add_neg]

/-- The complex KZ coefficient `Ω(z) = z⁻¹ A + (z − 1)⁻¹ B`. -/
noncomputable def kzΩ (A B : R) (z : ℂ) : R := z⁻¹ • A + (z - 1)⁻¹ • B

/-- `G` solves `G' = Ω G` (complex derivative) at every point of `U`. -/
def IsKZSolOn (A B : R) (G : ℂ → R) (U : Set ℂ) : Prop :=
  ∀ z ∈ U, HasDerivAt G (kzΩ A B z * G z) z

/-- The solution normalised at `0`: `G₀(z) = H₀(z) z^A`. -/
noncomputable def G₀ (A : R) (H : ℕ → R) (z : ℂ) : R := cseries H z * cpowA A z

/-- The solution normalised at `1`: `G₁(z) = H₁(1 − z) (1 − z)^B`. -/
noncomputable def G₁ (B : R) (H : ℕ → R) (z : ℂ) : R := cseries H (1 - z) * cpowA B (1 - z)

/-- Domain of `G₀`: the unit disc minus `(−1, 0]`. -/
def D₀ : Set ℂ := {z | ‖z‖ < 1} ∩ Complex.slitPlane

/-- Domain of `G₁`: the unit disc about `1` minus `[1, 2)`. -/
def D₁ : Set ℂ := {z | ‖1 - z‖ < 1} ∩ {z | 1 - z ∈ Complex.slitPlane}

theorem isKZSolOn_G₀ (A B : R) (H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge (kzM0 A B) H) :
    IsKZSolOn A B (G₀ A H) D₀ := by
  rintro z ⟨hz1, hz0⟩
  have hz1 : ‖z‖ < 1 := hz1
  have h := hasDerivAt_csolution (boundedOn_kzM0 A B) (boundedOn_kz_solution A B H h0 hH) hH
    hz0 hz1
  have hzne : z ≠ 0 := Complex.slitPlane_ne_zero hz0
  have h1 : (1 - z) ≠ 0 := by
    intro h; rw [sub_eq_zero] at h; rw [← h, norm_one] at hz1; exact lt_irrefl _ hz1
  have h2 : (z - 1) ≠ 0 := by rw [← neg_sub]; exact neg_ne_zero.2 h1
  unfold G₀
  convert h using 1
  rw [cseries_kzM0 A B hz1, ← smul_mul_assoc]
  congr 1
  unfold kzΩ
  rw [smul_sub, smul_smul, sub_eq_add_neg (z⁻¹ • A), ← neg_smul]
  congr 2
  field_simp
  ring

theorem isKZSolOn_G₁ (A B : R) (H : ℕ → R) (h0 : H 0 = 1) (hH : IsFormalGauge (kzM0 B A) H) :
    IsKZSolOn A B (G₁ B H) D₁ := by
  rintro z ⟨hz1, hz0⟩
  have hw := isKZSolOn_G₀ B A H h0 hH (1 - z) ⟨hz1, hz0⟩
  have hc : HasDerivAt (fun u : ℂ => 1 - u) (-1) z := by
    simpa using (hasDerivAt_id z).const_sub (1 : ℂ)
  have h := hw.scomp z hc
  unfold G₁
  convert h using 1
  rw [neg_one_smul, ← neg_mul]
  congr 1
  unfold kzΩ
  have h1 : (1 - z - 1) = -z := by ring
  have h2 : (1 - z) = -(z - 1) := by ring
  rw [h1, h2, inv_neg, inv_neg, neg_smul, neg_smul, neg_add, neg_neg, neg_neg, add_comm]

omit [CompleteSpace R] in
theorem IsKZSolOn.mul_const {A B : R} {G : ℂ → R} {U : Set ℂ} (hG : IsKZSolOn A B G U) (c : R) :
    IsKZSolOn A B (fun z => G z * c) U :=
  fun z hz => by simpa [mul_assoc] using (hG z hz).mul_const c

end KZ

section Uniqueness

omit [CompleteSpace R] in
/-- **Uniqueness on a convex set.** Two solutions of a linear holomorphic equation `X' = Ω X` on a
convex set `U` (with `Ω` continuous on `U`) that agree at one point agree on `U`: restrict to the
segment from that point and apply Gronwall. -/
theorem eqOn_of_convex {Ω : ℂ → R} {U : Set ℂ} (hU : Convex ℝ U) (hΩ : ContinuousOn Ω U)
    {X Y : ℂ → R} (hX : ∀ z ∈ U, HasDerivAt X (Ω z * X z) z)
    (hY : ∀ z ∈ U, HasDerivAt Y (Ω z * Y z) z) {c : ℂ} (hc : c ∈ U) (h : X c = Y c) :
    EqOn X Y U := by
  intro z hz
  set γ : ℝ → ℂ := fun s => c + (s : ℂ) * (z - c) with hγ
  have hγU : ∀ s ∈ Icc (0 : ℝ) 1, γ s ∈ U := by
    intro s hs
    have := hU.add_smul_sub_mem hc hz hs
    simpa [γ, Complex.real_smul] using this
  have hγ' : ∀ s : ℝ, HasDerivAt γ (z - c) s := by
    intro s
    have := (((hasDerivAt_id s).ofReal_comp).mul_const (z - c)).const_add c
    simpa [γ] using this
  have hγc : Continuous γ := by simp only [γ]; fun_prop
  have hcpt : IsCompact (γ '' Icc 0 1) := isCompact_Icc.image hγc
  obtain ⟨M, hM⟩ := hcpt.exists_bound_of_continuousOn
    (hΩ.mono (by rintro _ ⟨s, hs, rfl⟩; exact hγU s hs))
  have hM0 : 0 ≤ M := (norm_nonneg _).trans (hM _ ⟨0, left_mem_Icc.2 zero_le_one, rfl⟩)
  set K : NNReal := Real.toNNReal (‖z - c‖ * M)
  have hv : ∀ s ∈ Ico (0 : ℝ) 1,
      LipschitzOnWith K (fun W : R => (z - c) • (Ω (γ s) * W)) univ := by
    intro s hs
    refine (LipschitzWith.of_dist_le_mul fun x y => ?_).lipschitzOnWith
    rw [dist_eq_norm, dist_eq_norm, ← smul_sub, ← mul_sub, norm_smul,
      Real.coe_toNNReal _ (mul_nonneg (norm_nonneg _) hM0), mul_assoc]
    gcongr
    refine (norm_mul_le _ _).trans ?_
    gcongr
    exact hM _ ⟨s, Ico_subset_Icc_self hs, rfl⟩
  have hd : ∀ {F : ℂ → R}, (∀ w ∈ U, HasDerivAt F (Ω w * F w) w) → ∀ s ∈ Icc (0 : ℝ) 1,
      HasDerivAt (F ∘ γ) ((z - c) • (Ω (γ s) * F (γ s))) s :=
    fun hF s hs => (hF _ (hγU s hs)).scomp s (hγ' s)
  have key := ODE_solution_unique_of_mem_Icc_right
    (v := fun s W => (z - c) • (Ω (γ s) * W)) (s := fun _ => univ) (K := K)
    (f := X ∘ γ) (g := Y ∘ γ) (a := 0) (b := 1) hv
    (fun s hs => (hd hX s hs).continuousAt.continuousWithinAt)
    (fun s hs => (hd hX s (Ico_subset_Icc_self hs)).hasDerivWithinAt)
    (fun _ _ => mem_univ _)
    (fun s hs => (hd hY s hs).continuousAt.continuousWithinAt)
    (fun s hs => (hd hY s (Ico_subset_Icc_self hs)).hasDerivWithinAt)
    (fun _ _ => mem_univ _)
    (by simpa [γ] using h)
  simpa [γ] using key (right_mem_Icc.2 zero_le_one)

omit [CompleteSpace R] in
/-- **Connection constant from one invertible value.** If `G`, `X` solve on a convex `U` and `G(c)`
is a unit, then `X = G · (G(c)⁻¹ X(c))` on `U`. -/
theorem eqOn_mul_of_isUnit {Ω : ℂ → R} {U : Set ℂ} (hU : Convex ℝ U) (hΩ : ContinuousOn Ω U)
    {G X : ℂ → R} (hG : ∀ z ∈ U, HasDerivAt G (Ω z * G z) z)
    (hX : ∀ z ∈ U, HasDerivAt X (Ω z * X z) z) {c : ℂ} (hc : c ∈ U) (hu : IsUnit (G c)) :
    EqOn X (fun z => G z * (Ring.inverse (G c) * X c)) U :=
  eqOn_of_convex hU hΩ hX (fun z hz => by simpa [mul_assoc] using (hG z hz).mul_const _) hc
    (by rw [Ring.mul_inverse_cancel_left _ _ hu])

end Uniqueness

end QOU.KZ.KZComplex
