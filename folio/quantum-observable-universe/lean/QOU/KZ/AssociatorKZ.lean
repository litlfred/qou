import QOU.KZ.FuchsianAnalytic
import Mathlib.Analysis.ODE.Gronwall

/-!
# The KZ associator `Φ_KZ` as a renormalised connection matrix

Fourth brick of Step 1 of `docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md`. On `(0, 1)` the
three-point KZ equation

  `G'(t) = Ω(t) G(t)`,   `Ω(t) = A/t + B/(t − 1)`,

has two distinguished solutions (`QOU.KZ.FuchsianAnalytic`):

* `G₀(t) = H₀(t) · t^A`, with `H₀(0) = 1` (normalised at `0`),
* `G₁(t) = H₁(1 − t) · (1 − t)^B`, with `H₁(0) = 1` (normalised at `1`).

We prove that there is a **unique** `Φ` with `G₀(t) = G₁(t) Φ` for every `t ∈ (0, 1)`, and that
`Φ` is **invertible** (`kz_associator`). This `Φ` is the KZ associator `Φ_KZ = G₁(t)⁻¹ G₀(t)`
(Drinfeld's renormalised monodromy from `0` to `1`); `phiKZ` names it.

## How

* `G₁` solves the same equation: compose the solution at `0` of the system with `A ↔ B` swapped
  with `t ↦ 1 − t` (`isKZSol_G₁`).
* **Uniqueness on `(0, 1)`** (`eqOn_of_isKZSol`): `X ↦ Ω(t) X` is Lipschitz with constant
  `‖A‖/a + ‖B‖/(1 − b)` on any `[a, b] ⊂ (0, 1)`, so Mathlib's Gronwall uniqueness
  `ODE_solution_unique_of_mem_Icc` applies. Two solutions agreeing at one point agree on `(0, 1)`.
* Right multiplication by a constant preserves solutions. So `G₁ · (G₁(t*)⁻¹ G₀(t*))` is a solution
  agreeing with `G₀` at `t*`, hence everywhere: we only need `G₁` **invertible at one point**.
  Near `t = 1`, `H₁(1 − t)` is within `1` of `1` (continuity, `H₁(0) = 1`) and `(1 − t)^B` is an
  exponential, so `G₁(t*)` is a unit. Symmetrically `G₀` is a unit near `0`.
* Invertibility of `Φ`: with `G₁ = G₀ Ψ` from the symmetric argument, `G₀ = G₀ Ψ Φ` and
  `G₁ = G₁ Φ Ψ`; cancelling the units `G₀(s*)`, `G₁(t*)` gives `ΨΦ = ΦΨ = 1`. No derivative of the
  inverse is needed.

* **Inversion** `Φ(B, A) Φ(A, B) = Φ(A, B) Φ(B, A) = 1` (`phiKZ_swap_mul`, Drinfeld (2.12)):
  `G₁` for `(A, B)` is literally `G₀` for `(B, A)` evaluated at `1 − t`, so the two connection
  matrices compose to the identity after cancelling one unit value.

## Not here

The asymptotic `Φ_KZ = lim_{ε→0} ε^{-B} G(1−ε)…` normalisation is not restated (it is built into
`G₀`, `G₁`); hexagon and pentagon are later bricks. Base: complete normed `ℝ`-algebra. Sorry-free.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1, §5
-/

namespace QOU.KZ.AssociatorKZ

open Set QOU.KZ.FuchsianFormal QOU.KZ.FuchsianAnalytic

variable {R : Type*} [NormedRing R] [NormedAlgebra ℝ R] [CompleteSpace R]

/-- The KZ connection coefficient `Ω(t) = t⁻¹ A + (t − 1)⁻¹ B`. -/
noncomputable def kzΩ (A B : R) (t : ℝ) : R := t⁻¹ • A + (t - 1)⁻¹ • B

/-- `G` solves the three-point KZ equation `G' = Ω G` on `(0, 1)`. -/
def IsKZSol (A B : R) (G : ℝ → R) : Prop :=
  ∀ t ∈ Ioo (0 : ℝ) 1, HasDerivAt G (kzΩ A B t * G t) t

/-- The solution normalised at `0`: `G₀(t) = H₀(t) t^A`. -/
noncomputable def G₀ (A : R) (H₀ : ℕ → R) (t : ℝ) : R := series H₀ t * tpow A t

/-- The solution normalised at `1`: `G₁(t) = H₁(1 − t) (1 − t)^B`. -/
noncomputable def G₁ (B : R) (H₁ : ℕ → R) (t : ℝ) : R := series H₁ (1 - t) * tpow B (1 - t)

theorem isKZSol_G₀ (A B : R) (H₀ : ℕ → R) (h0 : H₀ 0 = 1)
    (hH : IsFormalGauge (kzM0 A B) H₀) : IsKZSol A B (G₀ A H₀) :=
  fun _ ht => kz_hasDerivAt A B H₀ h0 hH ht.1 ht.2

theorem isKZSol_G₁ (A B : R) (H₁ : ℕ → R) (h0 : H₁ 0 = 1)
    (hH : IsFormalGauge (kzM0 B A) H₁) : IsKZSol A B (G₁ B H₁) := by
  intro t ht
  have hw := kz_hasDerivAt B A H₁ h0 hH (t := 1 - t) (by linarith [ht.2]) (by linarith [ht.1])
  have hc : HasDerivAt (fun u : ℝ => 1 - u) (-1) t := by
    simpa using (hasDerivAt_id t).const_sub (1 : ℝ)
  have h := hw.scomp t hc
  unfold G₁
  convert h using 1
  rw [neg_one_smul, ← neg_mul]
  congr 1
  unfold kzΩ
  have h1 : (1 - t - 1) = -t := by ring
  have h2 : (1 - t) = -(t - 1) := by ring
  rw [h1, h2, inv_neg, inv_neg, neg_smul, neg_smul, neg_add, neg_neg, neg_neg, add_comm]

omit [CompleteSpace R] in
theorem IsKZSol.mul_const {A B : R} {G : ℝ → R} (hG : IsKZSol A B G) (c : R) :
    IsKZSol A B (fun t => G t * c) :=
  fun t ht => by simpa [mul_assoc] using (hG t ht).mul_const c

omit [CompleteSpace R] in
/-- `‖Ω(s)‖ ≤ ‖A‖/a + ‖B‖/(1 − b)` for `0 < a < s < b < 1`. -/
theorem norm_kzΩ_le (A B : R) {a b s : ℝ} (ha : 0 < a) (hb : b < 1) (hs : s ∈ Ioo a b) :
    ‖kzΩ A B s‖ ≤ ‖A‖ / a + ‖B‖ / (1 - b) := by
  have hs0 : 0 < s := ha.trans hs.1
  have hs1 : s - 1 < 0 := by linarith [hs.2]
  unfold kzΩ
  refine (norm_add_le _ _).trans ?_
  rw [norm_smul, norm_smul, Real.norm_eq_abs, Real.norm_eq_abs, abs_inv, abs_inv,
    abs_of_pos hs0, abs_of_neg hs1, div_eq_inv_mul, div_eq_inv_mul]
  gcongr
  all_goals linarith [hs.1, hs.2]

omit [CompleteSpace R] in
/-- **Uniqueness for the KZ equation on `(0, 1)`.** Two solutions agreeing at one point of
`(0, 1)` agree on all of `(0, 1)` (Gronwall). -/
theorem eqOn_of_isKZSol {A B : R} {f g : ℝ → R} (hf : IsKZSol A B f) (hg : IsKZSol A B g)
    {t₀ : ℝ} (ht₀ : t₀ ∈ Ioo (0 : ℝ) 1) (h : f t₀ = g t₀) : EqOn f g (Ioo 0 1) := by
  intro t ht
  set a := min t t₀ / 2 with ha_def
  set b := (max t t₀ + 1) / 2 with hb_def
  have hmin : 0 < min t t₀ := lt_min ht.1 ht₀.1
  have hmax : max t t₀ < 1 := max_lt ht.2 ht₀.2
  have ha : 0 < a := by positivity
  have hb : b < 1 := by rw [hb_def]; linarith
  have hsub : Icc a b ⊆ Ioo (0 : ℝ) 1 := fun s hs => ⟨ha.trans_le hs.1, hs.2.trans_lt hb⟩
  have hcont : ∀ {F : ℝ → R}, IsKZSol A B F → ContinuousOn F (Icc a b) :=
    fun hF s hs => (hF s (hsub hs)).continuousAt.continuousWithinAt
  set K : NNReal := Real.toNNReal (‖A‖ / a + ‖B‖ / (1 - b))
  have hK : ∀ s ∈ Ioo a b, LipschitzOnWith K (fun X => kzΩ A B s * X) univ := by
    intro s hs
    refine (LipschitzWith.of_dist_le_mul fun x y => ?_).lipschitzOnWith
    rw [dist_eq_norm, dist_eq_norm, ← mul_sub]
    refine (norm_mul_le _ _).trans ?_
    gcongr
    rw [Real.coe_toNNReal _ (add_nonneg (div_nonneg (norm_nonneg _) ha.le)
      (div_nonneg (norm_nonneg _) (by linarith)))]
    exact norm_kzΩ_le A B ha hb hs
  have hmin_le : min t t₀ ≤ t₀ := min_le_right _ _
  have hle_max : t₀ ≤ max t t₀ := le_max_right _ _
  have ht₀ab : t₀ ∈ Ioo a b := ⟨by rw [ha_def]; linarith, by rw [hb_def]; linarith⟩
  have htab : t ∈ Icc a b :=
    ⟨by rw [ha_def]; linarith [min_le_left t t₀], by rw [hb_def]; linarith [le_max_left t t₀]⟩
  exact ODE_solution_unique_of_mem_Icc (v := fun s X => kzΩ A B s * X) (s := fun _ => univ)
    hK ht₀ab (hcont hf) (fun s hs => hf s (hsub (Ioo_subset_Icc_self hs)))
    (fun _ _ => mem_univ _) (hcont hg) (fun s hs => hg s (hsub (Ioo_subset_Icc_self hs)))
    (fun _ _ => mem_univ _) h htab

omit [CompleteSpace R] in
/-- **Connection matrix from one invertible value.** If `G` and `X` solve KZ on `(0, 1)` and
`G(t*)` is a unit, then `X = G · (G(t*)⁻¹ X(t*))` on `(0, 1)`. -/
theorem eqOn_mul_of_isUnit {A B : R} {G X : ℝ → R} (hG : IsKZSol A B G) (hX : IsKZSol A B X)
    {t : ℝ} (ht : t ∈ Ioo (0 : ℝ) 1) (hu : IsUnit (G t)) :
    EqOn X (fun s => G s * (Ring.inverse (G t) * X t)) (Ioo 0 1) :=
  eqOn_of_isKZSol hX (hG.mul_const _) ht (by rw [Ring.mul_inverse_cancel_left _ _ hu])

omit [CompleteSpace R] in
theorem series_zero (H : ℕ → R) : series H 0 = H 0 := by
  unfold series
  rw [tsum_eq_single 0 fun k hk => by rw [zero_pow hk, zero_smul]]
  simp

/-- A convergent series with `H 0 = 1` is a unit for small positive `w`. -/
theorem exists_isUnit_series {H : ℕ → R} (hb : BoundedOn H 1) (h0 : H 0 = 1) :
    ∃ δ, 0 < δ ∧ δ < 1 ∧ ∀ w ∈ Ioo (0 : ℝ) δ, IsUnit (series H w) := by
  have hc := (hasDerivAt_series hb (t := 0) (by simp)).continuousAt
  obtain ⟨δ, hδ, hδ'⟩ := Metric.continuousAt_iff.mp hc 1 one_pos
  refine ⟨min δ (1 / 2), lt_min hδ (by norm_num), by
    linarith [min_le_right δ (1 / 2 : ℝ)], fun w hw => ?_⟩
  have hd : dist w 0 < δ := by
    rw [Real.dist_eq, sub_zero, abs_of_pos hw.1]; exact hw.2.trans_le (min_le_left _ _)
  have h1 := hδ' hd
  rw [series_zero, h0, dist_eq_norm, ← norm_neg, neg_sub] at h1
  have : series H w = 1 - (1 - series H w) := by abel
  rw [this]
  exact (Units.oneSub _ h1).isUnit

theorem isUnit_tpow (A : R) (t : ℝ) : IsUnit (tpow A t) := NormedSpace.isUnit_exp ℝ _

/-- **The KZ associator.** For residues `A, B` and the normalised formal solutions `H₀` (at `0`,
coefficients `kzM0 A B`) and `H₁` (at `1`, coefficients `kzM0 B A`), there is a unique `Φ` with
`G₀(t) = G₁(t) Φ` on `(0, 1)`, and it is a unit. -/
theorem kz_associator (A B : R) (H₀ H₁ : ℕ → R) (h₀ : H₀ 0 = 1)
    (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁) :
    ∃! Φ : R, IsUnit Φ ∧ ∀ t ∈ Ioo (0 : ℝ) 1, G₀ A H₀ t = G₁ B H₁ t * Φ := by
  have hS₀ := isKZSol_G₀ A B H₀ h₀ hH₀
  have hS₁ := isKZSol_G₁ A B H₁ h₁ hH₁
  obtain ⟨δ₀, hδ₀, hδ₀1, hu₀⟩ := exists_isUnit_series (boundedOn_kz_solution A B H₀ h₀ hH₀) h₀
  obtain ⟨δ₁, hδ₁, hδ₁1, hu₁⟩ := exists_isUnit_series (boundedOn_kz_solution B A H₁ h₁ hH₁) h₁
  -- the two base points
  set s := δ₀ / 2
  set t := 1 - δ₁ / 2
  have hs : s ∈ Ioo (0 : ℝ) 1 := ⟨by positivity, by simp only [s]; linarith⟩
  have ht : t ∈ Ioo (0 : ℝ) 1 := ⟨by simp only [t]; linarith, by simp only [t]; linarith⟩
  have hU₀ : IsUnit (G₀ A H₀ s) :=
    (hu₀ s ⟨hs.1, by simp only [s]; linarith⟩).mul (isUnit_tpow A s)
  have hU₁ : IsUnit (G₁ B H₁ t) :=
    (hu₁ (1 - t) ⟨by simp only [t]; linarith, by simp only [t]; linarith⟩).mul
      (isUnit_tpow B (1 - t))
  set Φ := Ring.inverse (G₁ B H₁ t) * G₀ A H₀ t
  set Ψ := Ring.inverse (G₀ A H₀ s) * G₁ B H₁ s
  have hΦ : EqOn (G₀ A H₀) (fun u => G₁ B H₁ u * Φ) (Ioo 0 1) := eqOn_mul_of_isUnit hS₁ hS₀ ht hU₁
  have hΨ : EqOn (G₁ B H₁) (fun u => G₀ A H₀ u * Ψ) (Ioo 0 1) := eqOn_mul_of_isUnit hS₀ hS₁ hs hU₀
  have hΨΦ : Ψ * Φ = 1 := by
    have e1 : G₀ A H₀ s = G₁ B H₁ s * Φ := hΦ hs
    have e2 : G₁ B H₁ s = G₀ A H₀ s * Ψ := hΨ hs
    have e : G₀ A H₀ s * 1 = G₀ A H₀ s * (Ψ * Φ) := by
      rw [mul_one, ← mul_assoc, ← e2, ← e1]
    exact (hU₀.mul_left_cancel e).symm
  have hΦΨ : Φ * Ψ = 1 := by
    have e1 : G₀ A H₀ t = G₁ B H₁ t * Φ := hΦ ht
    have e2 : G₁ B H₁ t = G₀ A H₀ t * Ψ := hΨ ht
    have e : G₁ B H₁ t * 1 = G₁ B H₁ t * (Φ * Ψ) := by
      rw [mul_one, ← mul_assoc, ← e1, ← e2]
    exact (hU₁.mul_left_cancel e).symm
  refine ⟨Φ, ⟨⟨⟨Φ, Ψ, hΦΨ, hΨΦ⟩, rfl⟩, fun u hu => hΦ hu⟩, fun Φ' ⟨_, hΦ'⟩ => ?_⟩
  exact hU₁.mul_left_cancel ((hΦ' t ht).symm.trans (hΦ ht))

/-- `Φ_KZ`, the associator of `kz_associator`. -/
noncomputable def phiKZ (A B : R) (H₀ H₁ : ℕ → R) (h₀ : H₀ 0 = 1)
    (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁) : R :=
  (kz_associator A B H₀ H₁ h₀ hH₀ h₁ hH₁).exists.choose


theorem phiKZ_spec (A B : R) (H₀ H₁ : ℕ → R) (h₀ : H₀ 0 = 1)
    (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁) :
    IsUnit (phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁) ∧
      ∀ t ∈ Ioo (0 : ℝ) 1, G₀ A H₀ t = G₁ B H₁ t * phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁ :=
  (kz_associator A B H₀ H₁ h₀ hH₀ h₁ hH₁).exists.choose_spec

omit [CompleteSpace R] in
theorem G₁_eq_G₀ (B : R) (H : ℕ → R) (t : ℝ) : G₁ B H t = G₀ B H (1 - t) := rfl

/-- **Inversion**: `Φ(B, A) · Φ(A, B) = 1` (Drinfeld (2.12), `Φ(B,A) = Φ(A,B)⁻¹`). The solution
normalised at `1` for `(A, B)` is the solution normalised at `0` for `(B, A)` read in `1 − t`. -/
theorem phiKZ_swap_mul (A B : R) (H₀ H₁ : ℕ → R) (h₀ : H₀ 0 = 1)
    (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1) (hH₁ : IsFormalGauge (kzM0 B A) H₁) :
    phiKZ B A H₁ H₀ h₁ hH₁ h₀ hH₀ * phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁ = 1 ∧
      phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁ * phiKZ B A H₁ H₀ h₁ hH₁ h₀ hH₀ = 1 := by
  obtain ⟨hu, hΦ⟩ := phiKZ_spec A B H₀ H₁ h₀ hH₀ h₁ hH₁
  obtain ⟨-, hΦ'⟩ := phiKZ_spec B A H₁ H₀ h₁ hH₁ h₀ hH₀
  set Φ := phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁
  set Φ' := phiKZ B A H₁ H₀ h₁ hH₁ h₀ hH₀
  obtain ⟨δ, hδ, hδ1, hu₁⟩ := exists_isUnit_series (boundedOn_kz_solution B A H₁ h₁ hH₁) h₁
  set t := 1 - δ / 2
  have ht : t ∈ Ioo (0 : ℝ) 1 := ⟨by simp only [t]; linarith, by simp only [t]; linarith⟩
  have hU : IsUnit (G₁ B H₁ t) :=
    (hu₁ (1 - t) ⟨by simp only [t]; linarith, by simp only [t]; linarith⟩).mul
      (isUnit_tpow B (1 - t))
  have e1 : G₀ A H₀ t = G₁ B H₁ t * Φ := hΦ t ht
  have e2 : G₀ B H₁ (1 - t) = G₁ A H₀ (1 - t) * Φ' :=
    hΦ' (1 - t) ⟨by linarith [ht.2], by linarith [ht.1]⟩
  have e3 : G₁ A H₀ (1 - t) = G₀ A H₀ t := by rw [G₁_eq_G₀, sub_sub_cancel]
  rw [← G₁_eq_G₀, e3, e1, mul_assoc] at e2
  have hΦΦ' : Φ * Φ' = 1 := (hU.mul_left_cancel ((mul_one _).trans e2)).symm
  refine ⟨?_, hΦΦ'⟩
  obtain ⟨u, hu⟩ := hu
  rw [← hu] at hΦΦ' ⊢
  calc Φ' * ↑u = (↑u⁻¹ * (↑u * Φ')) * ↑u := by rw [← mul_assoc, Units.inv_mul, one_mul]
    _ = 1 := by rw [hΦΦ', mul_one, Units.inv_mul]

end QOU.KZ.AssociatorKZ
