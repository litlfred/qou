import QOU.Mass.KZTwoStrandHecke
import QOU.Mass.KZHolonomy.Continuity
import QOU.KZ.FuchsianConvergence
import QOU.KZ.KZHalfMonodromy
import Mathlib.Topology.Algebra.Module.Cardinality
import Mathlib.Analysis.Normed.Ring.Units

/-!
# Local monodromy: the `n`-strand KZ holonomy satisfies the Hecke quadratic
-/

namespace QOU.Mass.KZHolonomy.LocalMonodromy

open Set Complex Finset QOU.Mass.KZHolonomy QOU.MathlibExt.Braid QOU.Mass.BraidHeckeFactor
  QOU.Mass.KZTwoStrandHecke QOU.KZ.FuchsianFormal QOU.KZ.FuchsianAnalytic QOU.KZ.KZComplex

variable {A : Type*} [NormedRing A] [NormedAlgebra ℂ A]
variable {m : ℕ} (ρ : Equiv.Perm (Fin (m + 2)) →* A) (κ c : ℂ)

/-! ## The coefficients near the collision `z₀ = z₁` -/

/-- The spectator strand `k + 2`. -/
def spec (k : Fin m) : Fin (m + 2) := k.succ.succ

/-- `a_k = 2(k+2) − 1 = 2k + 3`: the spectator `k+2` meets `z₀`, `z₁` at `u = ∓ a_k`. -/
noncomputable def aSp (k : Fin m) : ℂ := 2 * (k : ℕ) + 3

lemma three_le_norm_aSp (k : Fin m) : 3 ≤ ‖aSp k‖ := by
  have : aSp k = (((2 * (k : ℕ) + 3 : ℕ) : ℝ) : ℂ) := by simp [aSp]
  rw [this, Complex.norm_real, Real.norm_of_nonneg (by positivity)]
  push_cast; have : (0 : ℝ) ≤ (k : ℕ) := by positivity
  linarith

lemma aSp_ne_zero (k : Fin m) : aSp k ≠ 0 := by
  intro h; have := three_le_norm_aSp k; rw [h, norm_zero] at this; norm_num at this

lemma norm_inv_aSp_le (k : Fin m) : ‖(aSp k)⁻¹‖ ≤ 1 / 3 := by
  rw [norm_inv]
  exact inv_anti₀ (by norm_num) (three_le_norm_aSp k) |>.trans_eq (by norm_num)

/-- The power-series coefficients of `M(u) = 2κ r₀₁ + 2κ Σ_k (u/(u+a_k) r₀ₖ + u/(u−a_k) r₁ₖ)`. -/
noncomputable def Mc : ℕ → A
  | 0 => (2 * κ) • resid ρ c 0 1
  | n + 1 => ∑ k : Fin m, (2 * κ) •
      (((-1) ^ n * (aSp k)⁻¹ ^ (n + 1)) • resid ρ c 0 (spec k) -
        ((aSp k)⁻¹ ^ (n + 1)) • resid ρ c 1 (spec k))

/-- The coefficient as a function. -/
noncomputable def Xf (u : ℂ) : A :=
  (2 * κ) • resid ρ c 0 1 + ∑ k : Fin m, (2 * κ) •
    ((u / (u + aSp k)) • resid ρ c 0 (spec k) + (u / (u - aSp k)) • resid ρ c 1 (spec k))

/-- The constant `C` of the geometric bound. -/
noncomputable def Cb : ℝ :=
  ∑ k : Fin m, ‖2 * κ‖ * (‖resid ρ c 0 (spec k)‖ + ‖resid ρ c 1 (spec k)‖)

lemma Cb_nonneg : 0 ≤ Cb ρ κ c := by unfold Cb; positivity

lemma norm_Mc_le (n : ℕ) (hn : 0 < n) : ‖Mc ρ κ c n‖ ≤ Cb ρ κ c * (1 / 3) ^ n := by
  obtain ⟨n, rfl⟩ : ∃ k, n = k + 1 := ⟨n - 1, by omega⟩
  simp only [Mc, Cb, Finset.sum_mul]
  refine (norm_sum_le _ _).trans (Finset.sum_le_sum fun k _ => ?_)
  have hi0 : ‖(aSp k)⁻¹‖ ^ (n + 1) ≤ (1 / 3) ^ (n + 1) :=
    pow_le_pow_left₀ (norm_nonneg _) (norm_inv_aSp_le k) _
  have hi : ‖(aSp k)⁻¹ ^ (n + 1)‖ ≤ (1 / 3) ^ (n + 1) := by rw [norm_pow]; exact hi0
  have hi' : ‖(-1 : ℂ) ^ n * (aSp k)⁻¹ ^ (n + 1)‖ ≤ (1 / 3) ^ (n + 1) := by
    rw [norm_mul, norm_pow, norm_neg, norm_one, one_pow, one_mul]; exact hi
  rw [norm_smul]
  have h2 := norm_sub_le (((-1) ^ n * (aSp k)⁻¹ ^ (n + 1)) • resid ρ c 0 (spec k))
    (((aSp k)⁻¹ ^ (n + 1)) • resid ρ c 1 (spec k))
  rw [norm_smul, norm_smul] at h2
  calc ‖2 * κ‖ * ‖((-1) ^ n * (aSp k)⁻¹ ^ (n + 1)) • resid ρ c 0 (spec k) -
        ((aSp k)⁻¹ ^ (n + 1)) • resid ρ c 1 (spec k)‖
      ≤ ‖2 * κ‖ * ((1 / 3) ^ (n + 1) * ‖resid ρ c 0 (spec k)‖ +
          (1 / 3) ^ (n + 1) * ‖resid ρ c 1 (spec k)‖) := by
        gcongr
        exact h2.trans (add_le_add (by gcongr) (by gcongr))
    _ = _ := by ring

lemma boundedOn_Mc (r : ℝ) (hr : r < 3) : BoundedOn (Mc ρ κ c) r := by
  intro s hs0 hs
  refine ⟨‖Mc ρ κ c 0‖ + Cb ρ κ c, fun k => ?_⟩
  rcases Nat.eq_zero_or_pos k with rfl | hk
  · simp only [pow_zero, mul_one]; linarith [Cb_nonneg ρ κ c]
  · have hq : s * (1 / 3) ≤ 1 := by nlinarith
    calc ‖Mc ρ κ c k‖ * s ^ k ≤ Cb ρ κ c * (1 / 3) ^ k * s ^ k := by
          gcongr; exact norm_Mc_le ρ κ c k hk
      _ = Cb ρ κ c * (s * (1 / 3)) ^ k := by rw [mul_pow]; ring
      _ ≤ Cb ρ κ c * 1 := by
          gcongr
          · exact Cb_nonneg ρ κ c
          · exact pow_le_one₀ (by positivity) hq
      _ ≤ _ := by linarith [norm_nonneg (Mc ρ κ c 0)]

/-! ## Summation: `M(u) = Σ Mₙ uⁿ` for `|u| < 3` -/

lemma hasSum_geom_plus (a u : ℂ) (ha : a ≠ 0) (hu : ‖u * a⁻¹‖ < 1) :
    HasSum (fun n : ℕ => u ^ (n + 1) * ((-1) ^ n * a⁻¹ ^ (n + 1))) (u / (u + a)) := by
  have hξ : ‖-(u * a⁻¹)‖ < 1 := by rwa [norm_neg]
  have h := (hasSum_geometric_of_norm_lt_one hξ).mul_left (u * a⁻¹)
  have hne : u + a ≠ 0 := by
    intro h0
    have : u * a⁻¹ = -1 := by rw [eq_neg_of_add_eq_zero_left h0, neg_mul, mul_inv_cancel₀ ha]
    rw [this] at hu; simp at hu
  convert h using 1
  · funext n; ring
  · field_simp
    rw [eq_div_iff (by rw [sub_neg_eq_add, add_comm]; exact hne)]; ring

lemma hasSum_geom_minus (a u : ℂ) (ha : a ≠ 0) (hu : ‖u * a⁻¹‖ < 1) :
    HasSum (fun n : ℕ => u ^ (n + 1) * (-(a⁻¹ ^ (n + 1)))) (u / (u - a)) := by
  have h := ((hasSum_geometric_of_norm_lt_one hu).mul_left (u * a⁻¹)).neg
  have hne : u - a ≠ 0 := by
    intro h0
    have : u * a⁻¹ = 1 := by rw [sub_eq_zero.1 h0, mul_inv_cancel₀ ha]
    rw [this] at hu; simp at hu
  have hne' : 1 - u * a⁻¹ ≠ 0 := by
    intro h0; rw [sub_eq_zero.1 h0 |>.symm] at hu; simp at hu
  convert h using 1
  · funext n; ring
  · have hau : a - u ≠ 0 := fun h0 => hne (by rw [sub_eq_zero.1 h0, sub_self])
    field_simp
    ring

lemma hasSum_Mc (u : ℂ) (hu : ‖u‖ < 3) :
    HasSum (fun n => u ^ n • Mc ρ κ c n) (Xf ρ κ c u) := by
  rw [← hasSum_nat_add_iff' 1]
  simp only [Finset.range_one, Finset.sum_singleton, pow_zero, one_smul, Mc, Xf,
    add_sub_cancel_left]
  simp only [Finset.smul_sum]
  refine hasSum_sum fun k _ => ?_
  have hua : ‖u * (aSp k)⁻¹‖ < 1 := by
    rw [norm_mul]
    calc ‖u‖ * ‖(aSp k)⁻¹‖ ≤ ‖u‖ * (1 / 3) := by gcongr; exact norm_inv_aSp_le k
      _ < 1 := by linarith
  have h1 := (hasSum_geom_plus (aSp k) u (aSp_ne_zero k) hua).smul_const (resid ρ c 0 (spec k))
  have h2 := (hasSum_geom_minus (aSp k) u (aSp_ne_zero k) hua).smul_const (resid ρ c 1 (spec k))
  convert (h1.add h2).const_smul (2 * κ) using 1
  funext n
  simp only [smul_sub, smul_smul, smul_add]
  match_scalars <;> ring

lemma cseries_Mc [CompleteSpace A] (u : ℂ) (hu : ‖u‖ < 3) :
    cseries (Mc ρ κ c) u = Xf ρ κ c u :=
  (hasSum_Mc ρ κ c u hu).tsum_eq


/-! ## The exchange symmetry `u ↦ −u` -/

/-- `P = ρ(s₀₁)`. -/
noncomputable abbrev Pm : A := ρ (Equiv.swap 0 1)

omit [NormedAlgebra ℂ A] in
lemma Pm_sq : Pm ρ * Pm ρ = 1 := by
  rw [Pm, ← map_mul, Equiv.swap_mul_self, map_one]

lemma spec_ne_zero (k : Fin m) : spec k ≠ 0 := Fin.succ_ne_zero _

lemma spec_ne_one (k : Fin m) : spec k ≠ 1 := by
  intro h
  have : (k.succ.succ : Fin (m + 2)) = (0 : Fin (m + 1)).succ := by
    rw [Fin.succ_zero_eq_one]; exact h
  exact Fin.succ_ne_zero k (Fin.succ_injective _ this)

omit [NormedAlgebra ℂ A] in
lemma conj_swap (a b : Fin (m + 2)) :
    Pm ρ * ρ (Equiv.swap a b) * Pm ρ =
      ρ (Equiv.swap (Equiv.swap 0 1 a) (Equiv.swap 0 1 b)) := by
  rw [Equiv.swap_apply_apply, Pm, ← map_mul, ← map_mul, Equiv.swap_inv]

lemma conj_resid (a b : Fin (m + 2)) :
    Pm ρ * resid ρ c a b * Pm ρ = resid ρ c (Equiv.swap 0 1 a) (Equiv.swap 0 1 b) := by
  unfold resid
  rw [mul_sub, sub_mul, conj_swap, ← Algebra.commutes, mul_assoc, Pm_sq, mul_one]

lemma conj_resid01 : Pm ρ * resid ρ c 0 1 * Pm ρ = resid ρ c 0 1 := by
  rw [conj_resid, Equiv.swap_apply_left, Equiv.swap_apply_right]
  unfold resid; rw [Equiv.swap_comm]

lemma conj_resid0 (k : Fin m) :
    Pm ρ * resid ρ c 0 (spec k) * Pm ρ = resid ρ c 1 (spec k) := by
  rw [conj_resid, Equiv.swap_apply_left,
    Equiv.swap_apply_of_ne_of_ne (spec_ne_zero k) (spec_ne_one k)]

lemma conj_resid1 (k : Fin m) :
    Pm ρ * resid ρ c 1 (spec k) * Pm ρ = resid ρ c 0 (spec k) := by
  rw [conj_resid, Equiv.swap_apply_right,
    Equiv.swap_apply_of_ne_of_ne (spec_ne_zero k) (spec_ne_one k)]

lemma neg_one_pow_mul_self (n : ℕ) : ((-1 : ℂ) ^ n) * (-1) ^ n = 1 := by
  rw [← mul_pow]; norm_num

/-- **Exchange symmetry of the coefficients**: `Mₙ = (−1)ⁿ P Mₙ P`. -/
lemma Mc_sym (n : ℕ) : ((-1 : ℂ) ^ n) • (Pm ρ * Mc ρ κ c n * Pm ρ) = Mc ρ κ c n := by
  rcases n with _ | n
  · simp only [Mc, pow_zero, one_smul, mul_smul_comm, smul_mul_assoc, conj_resid01]
  · simp only [Mc, Finset.mul_sum, Finset.sum_mul, Finset.smul_sum, mul_smul_comm,
      smul_mul_assoc, mul_sub, sub_mul, conj_resid0, conj_resid1]
    refine Finset.sum_congr rfl fun k _ => ?_
    have h := neg_one_pow_mul_self n
    rw [pow_succ]
    generalize (-1 : ℂ) ^ n = σ at h ⊢
    simp only [smul_sub, smul_smul]
    match_scalars <;> first
      | ring1
      | linear_combination (-(2 * κ * (aSp k)⁻¹ ^ (n + 1))) * h


omit [NormedAlgebra ℂ A] in
lemma conj_mul (x y : A) : Pm ρ * (x * y) * Pm ρ = (Pm ρ * x * Pm ρ) * (Pm ρ * y * Pm ρ) := by
  have h := Pm_sq ρ
  calc Pm ρ * (x * y) * Pm ρ = Pm ρ * x * (Pm ρ * Pm ρ) * y * Pm ρ := by
        rw [h, mul_one]; noncomm_ring
    _ = _ := by noncomm_ring

/-- Non-resonance of the residue `2κ(P − c)`. -/
lemma nonResonant_Mc0 (hκ : ∀ k : ℕ, 0 < k → (k : ℂ) ^ 2 ≠ 4 * (2 * κ) ^ 2) :
    NonResonant (Mc ρ κ c 0) := by
  have e : ∀ k : ℕ, indicial (Mc ρ κ c 0) k = indicial ((2 * κ) • Pm ρ) k := by
    intro k; funext X
    simp only [indicial, ad, Mc, resid, Pm, smul_sub, sub_mul, mul_sub,
      Algebra.algebraMap_eq_smul_one, smul_mul_assoc, mul_smul_comm, one_mul, mul_one]
    abel
  intro k hk
  rw [e]
  exact nonResonant_smul_involution (Pm ρ) (Pm_sq ρ) (2 * κ) hκ k hk

/-- The normalised formal solution `H(u) = Σ Hₖ uᵏ`, `H₀ = 1`, of `u H' + H M₀ = M H`. -/
noncomputable def Hc (hNR : NonResonant (Mc ρ κ c 0)) : ℕ → A := formalSol (Mc ρ κ c) hNR

/-- **Exchange symmetry of the formal solution**: `Hₖ = (−1)ᵏ P Hₖ P`. -/
lemma Hc_sym (hNR : NonResonant (Mc ρ κ c 0)) (k : ℕ) :
    ((-1 : ℂ) ^ k) • (Pm ρ * Hc ρ κ c hNR k * Pm ρ) = Hc ρ κ c hNR k := by
  set H := Hc ρ κ c hNR
  set M := Mc ρ κ c
  have hH : IsFormalGauge M H := formalSol_isFormalGauge M hNR
  have hP := Pm_sq ρ
  set H' : ℕ → A := fun k => ((-1 : ℂ) ^ k) • (Pm ρ * H k * Pm ρ)
  have h0' : H' 0 = 1 := by
    simp only [H', pow_zero, one_smul, H, Hc, formalSol_zero, mul_one, hP]
  have hM0 : Pm ρ * M 0 * Pm ρ = M 0 := by simpa using Mc_sym ρ κ c 0
  have hcast : ∀ (k : ℕ) (x : A), Pm ρ * ((k : A) * x) * Pm ρ = (k : A) * (Pm ρ * x * Pm ρ) := by
    intro k x; rw [← mul_assoc, ← (Nat.cast_commute k (Pm ρ)).eq]; simp only [mul_assoc]
  have hG : IsFormalGauge M H' := by
    intro k
    have e := congrArg (fun x => ((-1 : ℂ) ^ k) • (Pm ρ * x * Pm ρ)) (hH k)
    simp only at e
    rw [mul_add, add_mul, hcast, conj_mul, hM0, Finset.mul_sum, Finset.sum_mul,
      Finset.smul_sum] at e
    simp only [H']
    rw [mul_smul_comm, smul_mul_assoc, ← smul_add, e]
    refine Finset.sum_congr rfl fun j hj => ?_
    have hjk : j ≤ k := Nat.lt_succ_iff.1 (Finset.mem_range.1 hj)
    rw [conj_mul, mul_smul_comm]
    conv_rhs => rw [show M (k - j) = _ from (Mc_sym ρ κ c (k - j)).symm]
    rw [smul_mul_assoc, smul_smul, ← pow_add, Nat.add_sub_cancel' hjk]
  have := formalGauge_unique M H' H (fun k hk => (hNR k hk).1) h0' (formalSol_zero M hNR) hG hH
  exact congrFun this k

end QOU.Mass.KZHolonomy.LocalMonodromy
