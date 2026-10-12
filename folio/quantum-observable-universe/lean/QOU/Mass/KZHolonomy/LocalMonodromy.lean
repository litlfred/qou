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

end QOU.Mass.KZHolonomy.LocalMonodromy
