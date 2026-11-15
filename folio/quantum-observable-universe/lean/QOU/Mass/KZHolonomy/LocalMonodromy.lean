import QOU.Mass.KZTwoStrandHecke
import QOU.Mass.KZHolonomy.Continuity
import QOU.KZ.FuchsianConvergence
import QOU.KZ.KZHalfMonodromy
import Mathlib.Topology.Algebra.Module.Cardinality
import Mathlib.Analysis.Normed.Ring.Units

/-!
# Local monodromy: the `n`-strand KZ holonomy satisfies the Hecke quadratic

Let `A` be a complete normed `ℂ`-algebra, `ρ : S_{m+2} →* A` any representation, `κ, c ∈ ℂ`,
and `θ = kzBraidRep ρ κ c : B_{m+2} →* Aˣ` the KZ holonomy representation
(`QOU.Mass.KZHolonomy.BraidRep`). With `ϑ = 2πiκ`, `q = e^{ϑ}`, `s = e^{ϑc}`, this file proves
that `β_j = s • θ(σ_j)` satisfies `β_j² = (q − q⁻¹)β_j + 1` for **every** strand count `≥ 2`,
every coupling `κ` and every generator (`kzBraidRep_sigma_isHeckeQuad`), so `θ` factors through
the Iwahori–Hecke algebra `H_{m+2}(q)` (`heckeOfKZ`, `heckeOfKZ_σ`).

## Proof (local monodromy at the collision divisor `z₀ = z₁`)

1. **The chart.** Along the half-turn `γ₀` the configuration is
   `z(u) = (½ − u/2, ½ + u/2, 2, 3, …)` at `u = e^{iπt}`, and the KZ coefficient is
   `ω(γ₀)(γ₀') = iπ · M(u)` with
   `M(u) = 2κ r₀₁ + 2κ Σ_k (u/(u + a_k) r₀ₖ + u/(u − a_k) r₁ₖ)`, `a_k = 2k + 3 ≥ 3`,
   `r_ab = ρ(s_ab) − c` (`kzForm_genPath_zero`). `M` is a power series `Σ Mₙ uⁿ` on `|u| < 3`
   (`hasSum_Mc`) with `‖Mₙ‖ ≤ C 3⁻ⁿ` (`norm_Mc_le`) and `M₀ = 2κ(P − c)`, `P = ρ(s₀₁)`.
2. **Fuchsian solution.** If `M₀` is non-resonant (`κ ∉ ±ℕ/4`, `nonResonant_Mc0`), the normalised
   formal solution `H` of `u H' + H M₀ = M H` (`QOU.KZ.FuchsianFormal`) converges on `|u| < 3`
   (`QOU.KZ.FuchsianConvergence`), and `F(t) = H(e^{iπt}) e^{iπ t M₀}` solves the transport
   equation along `γ₀` (`hasDerivWithinAt_Fsol`); so `T₀(1) H(1) = H(−1) e^{iπ M₀}`.
3. **Exchange symmetry.** `Mₙ = (−1)ⁿ P Mₙ P` (`Mc_sym`), hence by uniqueness of the formal
   solution `Hₖ = (−1)ᵏ P Hₖ P` (`Hc_sym`) and `H(−u) = P H(u) P` (`cseries_Hc_neg`). This gives
   the **monodromy relation** `θ(σ₀) H(1) = H(1) · P e^{iπ M₀}` (`monodromy_relation`).
4. **`H(1)` is a unit** (`isUnit_Hc_one`): `H(ε)` is a unit for small `ε`, and `H(u) u^{M₀}`
   solves a linear ODE along `[ε, 1]`, whose fundamental solution is a unit.
5. So `θ(σ₀)` is conjugate to `P e^{iπ M₀} = e^{ϑ(1−c)} e₊ − e^{−ϑ(1+c)} e₋`
   (`e± = (1 ± P)/2`), which satisfies the Hecke quadratic (`isHeckeQuad_P_usol`, as in `QOU.Mass.KZTwoStrandHecke`).
6. **All couplings.** The Hecke defect is continuous in `κ` (`continuous_kzBraidRep_σ`) and
   vanishes off the countable resonant set, whose complement is dense; so it vanishes everywhere
   (`kzBraidRep_sigma_zero_isHeckeQuad`). All generators are conjugate
   (`QOU.Mass.BraidHeckeFactor.isHeckeQuad_all_of_zero`).

No numerical input; sorry-free; axioms `propext`, `Classical.choice`, `Quot.sound`.

-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §5.1 gap 1
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


/-! ## The KZ coefficient along the half-turn `γ₀` -/

section Path

variable (t : ℝ)

lemma norm_eArc : ‖eArc t‖ = 1 := by
  rw [Complex.norm_def, Complex.normSq_apply, ← sq, ← sq, eArc_re, eArc_im,
    Real.cos_sq_add_sin_sq, Real.sqrt_one]

lemma eArc_add_aSp_ne (k : Fin m) : eArc t + aSp k ≠ 0 := by
  intro h
  have h1 : ‖aSp k‖ = ‖eArc t‖ := by rw [eq_neg_of_add_eq_zero_right h, norm_neg]
  have := three_le_norm_aSp k; rw [h1, norm_eArc] at this; norm_num at this

lemma eArc_sub_aSp_ne (k : Fin m) : eArc t - aSp k ≠ 0 := by
  intro h
  have h1 : ‖aSp k‖ = ‖eArc t‖ := by rw [sub_eq_zero.1 h]
  have := three_le_norm_aSp k; rw [h1, norm_eArc] at this; norm_num at this

lemma one_ne_zero' : (1 : Fin (m + 2)) ≠ 0 := by simp

lemma gp_zero : genPath (0 : Fin (m + 1)) t 0 = 1 / 2 - eArc t / 2 := by
  simp [genPath]

lemma gp_one : genPath (0 : Fin (m + 1)) t 1 = 1 / 2 + eArc t / 2 := by
  simp [genPath]

lemma gp_spec (k : Fin m) : genPath (0 : Fin (m + 1)) t (spec k) = (k : ℕ) + 2 := by
  have h0 := spec_ne_zero k
  have h1 := spec_ne_one k
  simp only [genPath, Fin.castSucc_zero, Fin.succ_zero_eq_one, h0, h1, if_false]
  simp [spec]; ring

lemma gp'_zero : genPath' (0 : Fin (m + 1)) t 0 = -(eArc' t / 2) := by
  simp [genPath']

lemma gp'_one : genPath' (0 : Fin (m + 1)) t 1 = eArc' t / 2 := by
  simp [genPath']

lemma gp'_spec (k : Fin m) : genPath' (0 : Fin (m + 1)) t (spec k) = 0 := by
  have h0 := spec_ne_zero k
  have h1 := spec_ne_one k
  simp only [genPath', Fin.castSucc_zero, Fin.succ_zero_eq_one, h0, h1, if_false]

local notation "Z" => genPath (0 : Fin (m + 1)) t
local notation "Z'" => genPath' (0 : Fin (m + 1)) t

lemma d01 : dlogPair Z Z' 0 1 = Real.pi * I := by
  rw [dlogPair, gp_zero, gp_one, gp'_zero, gp'_one, eArc'_eq]
  have he := eArc_ne_zero t
  rw [div_eq_iff (by intro h; apply he; linear_combination -h)]
  ring

lemma d0k (k : Fin m) :
    dlogPair Z Z' 0 (spec k) = Real.pi * I * (eArc t / (eArc t + aSp k)) := by
  rw [dlogPair, gp_zero, gp_spec, gp'_zero, gp'_spec, eArc'_eq]
  have he := eArc_add_aSp_ne t k
  rw [div_eq_iff (by intro h; apply he; unfold aSp; linear_combination -2 * h),
    mul_div_assoc', div_mul_eq_mul_div, eq_div_iff he]
  unfold aSp; ring

lemma d1k (k : Fin m) :
    dlogPair Z Z' 1 (spec k) = Real.pi * I * (eArc t / (eArc t - aSp k)) := by
  rw [dlogPair, gp_one, gp_spec, gp'_one, gp'_spec, eArc'_eq]
  have he := eArc_sub_aSp_ne t k
  rw [div_eq_iff (by intro h; apply he; unfold aSp; linear_combination 2 * h),
    mul_div_assoc', div_mul_eq_mul_div, eq_div_iff he]
  unfold aSp; ring

lemma dkl (k l : Fin m) : dlogPair Z Z' (spec k) (spec l) = 0 := by
  rw [dlogPair, gp'_spec, gp'_spec, sub_self, zero_div]

lemma resid_comm (a b : Fin (m + 2)) : resid ρ c a b = resid ρ c b a := by
  unfold resid; rw [Equiv.swap_comm]

/-- **The KZ coefficient along `γ₀`**: `ω(γ₀(t))(γ₀'(t)) = iπ · M(e^{iπt})`. -/
theorem kzForm_genPath_zero :
    kzForm ρ κ c (genPath (0 : Fin (m + 1)) t) (genPath' (0 : Fin (m + 1)) t) =
      ((Real.pi : ℂ) * I) • Xf ρ κ c (eArc t) := by
  rw [kzForm_apply]
  have hop : kzOp ρ c Z Z' = ∑ a, ∑ b, dlogPair Z Z' a b • resid ρ c a b := rfl
  rw [hop]
  simp only [Fin.sum_univ_succ, Fin.succ_zero_eq_one, dlogPair_self, zero_smul, zero_add]
  have hs : ∀ k : Fin m, (k.succ.succ : Fin (m + 2)) = spec k := fun _ => rfl
  simp only [hs, dkl, zero_smul, Finset.sum_const_zero, add_zero]
  rw [dlogPair_comm Z Z' 1 0, resid_comm ρ c 1 0, d01]
  simp only [fun k => dlogPair_comm Z Z' (spec k) 0, fun k => dlogPair_comm Z Z' (spec k) 1,
    fun k => resid_comm ρ c (spec k) 0, fun k => resid_comm ρ c (spec k) 1, d0k, d1k,
    Finset.sum_add_distrib]
  set U0 := ∑ k : Fin m, (eArc t / (eArc t + aSp k)) • resid ρ c 0 (spec k)
  set U1 := ∑ k : Fin m, (eArc t / (eArc t - aSp k)) • resid ρ c 1 (spec k)
  have e0 : ∑ k : Fin m, (Real.pi * I * (eArc t / (eArc t + aSp k))) • resid ρ c 0 (spec k) =
      ((Real.pi : ℂ) * I) • U0 := by
    simp only [U0, Finset.smul_sum, smul_smul]
  have e1 : ∑ k : Fin m, (Real.pi * I * (eArc t / (eArc t - aSp k))) • resid ρ c 1 (spec k) =
      ((Real.pi : ℂ) * I) • U1 := by
    simp only [U1, Finset.smul_sum, smul_smul]
  have eX : Xf ρ κ c (eArc t) = (2 * κ) • resid ρ c 0 1 + (2 * κ) • U0 + (2 * κ) • U1 := by
    simp only [Xf, U0, U1, smul_add, Finset.smul_sum, Finset.sum_add_distrib, add_assoc]
  rw [e0, e1, eX]
  module

end Path


/-! ## The local solution `H(u) u^{M₀}` and the monodromy relation -/

section Analytic

variable [CompleteSpace A]

omit [CompleteSpace A] in
open QOU.KZ.FuchsianConvergence in
lemma boundedOn_Hc (hNR : NonResonant (Mc ρ κ c 0)) : BoundedOn (Hc ρ κ c hNR) 2 := by
  intro s hs0 hs
  exact bounded_weighted (Mc ρ κ c) _ (formalSol_zero _ hNR) (formalSol_isFormalGauge _ hNR)
    (Cb ρ κ c) (1 / 3) s (Cb_nonneg ρ κ c) (by norm_num) hs0 (by linarith) (norm_Mc_le ρ κ c)

lemma cseries_Hc_neg (hNR : NonResonant (Mc ρ κ c 0)) (u : ℂ) (hu : ‖u‖ < 2) :
    cseries (Hc ρ κ c hNR) (-u) = Pm ρ * cseries (Hc ρ κ c hNR) u * Pm ρ := by
  have hs := (summable_norm_cseries (boundedOn_Hc ρ κ c hNR) hu).of_norm
  unfold cseries
  rw [← hs.tsum_mul_left, ← (hs.mul_left _).tsum_mul_right]
  refine tsum_congr fun k => ?_
  conv_lhs => rw [← Hc_sym ρ κ c hNR k]
  have e : (-u) ^ k * (-1) ^ k = u ^ k := by
    rw [neg_pow, mul_comm ((-1 : ℂ) ^ k), mul_assoc, neg_one_pow_mul_self, mul_one]
  rw [smul_smul, e, mul_smul_comm, smul_mul_assoc]

/-- `θ = 2πiκ`. -/
noncomputable abbrev θk : ℂ := 2 * κ * (Real.pi * I)

/-- The candidate transport `F(t) = H(e^{iπt}) · e^{iπ t M₀}` along `γ₀`. -/
noncomputable def Fsol (hNR : NonResonant (Mc ρ κ c 0)) (t : ℝ) : A :=
  cseries (Hc ρ κ c hNR) (eArc t) * Usol (Pm ρ) (θk κ) c t

omit [CompleteSpace A] in
lemma resid01_eq : resid ρ c 0 1 = Pm ρ - algebraMap ℂ A c := rfl

lemma hasDerivWithinAt_Fsol (hNR : NonResonant (Mc ρ κ c 0)) (t : ℝ) (ht : t ∈ Icc (0 : ℝ) 1) :
    HasDerivWithinAt (Fsol ρ κ c hNR)
      (kzForm ρ κ c (genPath (0 : Fin (m + 1)) t) (genPath' (0 : Fin (m + 1)) t) *
        Fsol ρ κ c hNR t) (Icc 0 1) t := by
  have hbH := boundedOn_Hc ρ κ c hNR
  have hbM := boundedOn_Mc ρ κ c 2 (by norm_num)
  have he2 : ‖eArc t‖ < 2 := by rw [norm_eArc]; norm_num
  have he3 : ‖eArc t‖ < 3 := by rw [norm_eArc]; norm_num
  have hH := (hasDerivAt_cseries hbH he2).scomp t (hasDerivAt_eArc t)
  have hU := (usol_isFundSol (θk κ) c (Pm_sq ρ)).2 t ht
  have hprod := hH.hasDerivWithinAt.mul hU
  unfold Fsol
  convert hprod using 1
  have hg := gauge_cseries hbM hbH (formalSol_isFormalGauge (Mc ρ κ c) hNR) he2
  rw [← smul_deriv_cseries] at hg
  have hD : eArc' t • ∑' n : ℕ, ((n : ℂ) * eArc t ^ (n - 1)) • Hc ρ κ c hNR n =
      ((Real.pi : ℂ) * I) • (cseries (Mc ρ κ c) (eArc t) * cseries (Hc ρ κ c hNR) (eArc t) -
        cseries (Hc ρ κ c hNR) (eArc t) * Mc ρ κ c 0) := by
    rw [eArc'_eq, mul_smul, eq_sub_of_add_eq hg]
  have hR : θk κ • (Pm ρ - algebraMap ℂ A c) = ((Real.pi : ℂ) * I) • Mc ρ κ c 0 := by
    simp only [θk, Mc, ← resid01_eq, smul_smul]; congr 1; ring
  rw [kzForm_genPath_zero, ← cseries_Mc ρ κ c _ he3, Function.comp_apply, hD, hR]
  simp only [sub_mul, smul_mul_assoc, mul_smul_comm, mul_assoc]
  module

lemma genFund_mul_eq (hNR : NonResonant (Mc ρ κ c 0)) :
    EqOn (fun t => genFund ρ κ c (0 : Fin (m + 1)) t * cseries (Hc ρ κ c hNR) 1)
      (Fsol ρ κ c hNR) (Icc 0 1) := by
  have hspec := genFund_spec ρ κ c (0 : Fin (m + 1))
  refine linear_eqOn_of_hasDerivWithinAt (continuousOn_genCoeff ρ κ c 0)
    (fun t ht => ?_) (hasDerivWithinAt_Fsol ρ κ c hNR) ?_
  · simpa only [mul_assoc] using (hspec.2 t ht).mul_const (cseries (Hc ρ κ c hNR) 1)
  · simp only [Fsol, hspec.1, one_mul, eArc_zero, (usol_isFundSol (θk κ) c (Pm_sq ρ)).1,
      mul_one]

lemma kz_sigma_zero_eq :
    ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A) =
      Pm ρ * genFund ρ κ c (0 : Fin (m + 1)) 1 := by
  rw [kzBraidRep_σ]; rfl

/-- **The monodromy relation** `θ(σ₀) H(1) = H(1) · P e^{iπ M₀}`. -/
theorem monodromy_relation (hNR : NonResonant (Mc ρ κ c 0)) :
    ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A) * cseries (Hc ρ κ c hNR) 1 =
      cseries (Hc ρ κ c hNR) 1 * (Pm ρ * Usol (Pm ρ) (θk κ) c 1) := by
  have h1 := genFund_mul_eq ρ κ c hNR ⟨zero_le_one, le_rfl⟩
  simp only at h1
  rw [kz_sigma_zero_eq, mul_assoc, h1, Fsol, eArc_one,
    cseries_Hc_neg ρ κ c hNR 1 (by norm_num)]
  have hP := Pm_sq ρ
  calc Pm ρ * (Pm ρ * cseries (Hc ρ κ c hNR) 1 * Pm ρ * Usol (Pm ρ) (θk κ) c 1)
      = (Pm ρ * Pm ρ) * cseries (Hc ρ κ c hNR) 1 * (Pm ρ * Usol (Pm ρ) (θk κ) c 1) := by
        simp only [mul_assoc]
    _ = _ := by rw [hP, one_mul]


/-! ### `H(1)` is invertible -/

lemma exists_isUnit_near_zero (hNR : NonResonant (Mc ρ κ c 0)) :
    ∃ ε : ℝ, 0 < ε ∧ ε < 1 ∧ IsUnit (cseries (Hc ρ κ c hNR) (ε : ℂ)) := by
  have hc := (hasDerivAt_cseries (boundedOn_Hc ρ κ c hNR) (z := 0) (by simp)).continuousAt
  obtain ⟨δ, hδ, h⟩ := Metric.continuousAt_iff.1 hc 1 one_pos
  refine ⟨min (δ / 2) (1 / 2), by positivity, by
    have := min_le_right (δ / 2) (1 / 2); linarith, ?_⟩
  have hx := h (x := ((min (δ / 2) (1 / 2) : ℝ) : ℂ)) (by
    rw [dist_zero_right, Complex.norm_real, Real.norm_of_nonneg (by positivity)]
    have := min_le_left (δ / 2) (1 / 2); linarith)
  rw [QOU.KZ.KZHalfMonodromy.cseries_zero, Hc, formalSol_zero, dist_eq_norm, ← norm_neg,
    neg_sub] at hx
  set x := cseries (Hc ρ κ c hNR) ((min (δ / 2) (1 / 2) : ℝ) : ℂ)
  have := (Units.oneSub (1 - x) hx).isUnit
  rwa [Units.val_oneSub, sub_sub_cancel] at this

lemma isUnit_Hc_one (hNR : NonResonant (Mc ρ κ c 0)) : IsUnit (cseries (Hc ρ κ c hNR) 1) := by
  obtain ⟨ε, hε0, hε1, hεu⟩ := exists_isUnit_near_zero ρ κ c hNR
  have hbH := boundedOn_Hc ρ κ c hNR
  have hbM := boundedOn_Mc ρ κ c 2 (by norm_num)
  set Y : ℂ → A := fun z => cseries (Hc ρ κ c hNR) z * cpowA (Mc ρ κ c 0) z
  set s : ℝ → ℝ := fun τ => ε + τ * (1 - ε)
  have hs_pos : ∀ τ ∈ Icc (0 : ℝ) 1, 0 < s τ := fun τ hτ => by
    have : 0 ≤ τ * (1 - ε) := mul_nonneg hτ.1 (by linarith)
    simp only [s]; linarith
  have hs_le : ∀ τ ∈ Icc (0 : ℝ) 1, s τ ≤ 1 := fun τ hτ => by
    have : τ * (1 - ε) ≤ 1 * (1 - ε) := mul_le_mul_of_nonneg_right hτ.2 (by linarith)
    simp only [s]; linarith
  have hnorm : ∀ τ ∈ Icc (0 : ℝ) 1, ‖((s τ : ℝ) : ℂ)‖ < 2 := fun τ hτ => by
    rw [Complex.norm_real, Real.norm_of_nonneg (hs_pos τ hτ).le]; linarith [hs_le τ hτ]
  set X : ℝ → A := fun τ =>
    ((((1 - ε : ℝ) : ℂ)) * ((s τ : ℝ) : ℂ)⁻¹) • cseries (Mc ρ κ c) ((s τ : ℝ) : ℂ)
  have hsd : ∀ τ : ℝ, HasDerivAt (fun τ => ((s τ : ℝ) : ℂ)) (((1 - ε : ℝ) : ℂ)) τ := by
    intro τ
    have := (((hasDerivAt_id τ).mul_const (1 - ε)).const_add ε).ofReal_comp
    simpa [s] using this
  have hW : ∀ τ ∈ Icc (0 : ℝ) 1,
      HasDerivWithinAt (fun τ => Y ((s τ : ℝ) : ℂ)) (X τ * Y ((s τ : ℝ) : ℂ)) (Icc 0 1) τ := by
    intro τ hτ
    have hY := hasDerivAt_csolution hbM hbH (formalSol_isFormalGauge (Mc ρ κ c) hNR)
      (Complex.ofReal_mem_slitPlane.2 (hs_pos τ hτ)) (hnorm τ hτ)
    have := (hY.scomp τ (hsd τ)).hasDerivWithinAt (s := Icc 0 1)
    convert this using 1
    simp only [X, smul_mul_assoc, smul_smul, Y]
  have hX : ContinuousOn X (Icc 0 1) := by
    intro τ hτ
    have h1 : ContinuousAt (fun τ => ((s τ : ℝ) : ℂ)) τ := (hsd τ).continuousAt
    have h2 : ContinuousAt (fun τ => cseries (Mc ρ κ c) ((s τ : ℝ) : ℂ)) τ :=
      ContinuousAt.comp (g := cseries (Mc ρ κ c))
        (hasDerivAt_cseries hbM (hnorm τ hτ)).continuousAt h1
    have h3 : ContinuousAt (fun τ => ((s τ : ℝ) : ℂ)⁻¹) τ :=
      h1.inv₀ (by exact_mod_cast (hs_pos τ hτ).ne')
    exact ((continuousAt_const.mul h3).smul h2).continuousWithinAt
  obtain ⟨Φ, hΦ⟩ := exists_isFundSol hX
  have heq := linear_eqOn_of_hasDerivWithinAt hX hW
    (W' := fun τ => Φ τ * Y ((s 0 : ℝ) : ℂ))
    (fun τ hτ => by simpa only [mul_assoc] using (hΦ.2 τ hτ).mul_const _)
    (by simp only [hΦ.1, one_mul]) ⟨zero_le_one, le_rfl⟩
  simp only at heq
  have hs0 : s 0 = ε := by simp [s]
  have hs1 : s 1 = 1 := by simp [s]
  rw [hs1, hs0] at heq
  have hcp : cpowA (Mc ρ κ c 0) 1 = 1 := by
    simp [cpowA]
  have hY1 : Y (((1 : ℝ) : ℂ)) = cseries (Hc ρ κ c hNR) 1 := by
    simp only [Y, Complex.ofReal_one]; rw [hcp, mul_one]
  rw [hY1] at heq
  rw [heq]
  exact (hΦ.isUnit hX 1 ⟨zero_le_one, le_rfl⟩).mul (hεu.mul (isUnit_cpowA _ _))

/-! ### The Hecke quadratic -/

omit [CompleteSpace A] in
/-- `P e^{θ(P − c)}` satisfies the Hecke quadratic for any involution `P`. -/
theorem isHeckeQuad_P_usol {P : A} (hP : P * P = 1) (θ : ℂ) :
    IsHeckeQuad (Complex.exp (θ * c)) (Complex.exp θ) (Complex.exp θ)⁻¹ (P * Usol P θ c 1) := by
  have hβ : Complex.exp (θ * c) • (P * Usol P θ c 1) =
      Complex.exp θ • eP P - (Complex.exp θ)⁻¹ • eM P := by
    rw [Usol, mul_add, mul_smul_comm, mul_smul_comm, P_mul_eP hP, P_mul_eM hP, smul_neg,
      ← sub_eq_add_neg, smul_sub, smul_smul, smul_smul, ← Complex.exp_add, ← Complex.exp_add,
      ← Complex.exp_neg]
    simp only [Complex.ofReal_one, one_mul]
    congr 3 <;> ring
  unfold IsHeckeQuad
  rw [hβ]
  exact split_hecke hP (Complex.exp_ne_zero θ)

/-- **The Hecke quadratic for the first generator, `n` strands** (non-resonant coupling). -/
theorem kzBraidRep_sigma_zero_isHeckeQuad_of_nonResonant (hNR : NonResonant (Mc ρ κ c 0)) :
    IsHeckeQuad (Complex.exp (θk κ * c)) (Complex.exp (θk κ)) (Complex.exp (θk κ))⁻¹
      ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A) := by
  obtain ⟨u, hu⟩ := isUnit_Hc_one ρ κ c hNR
  have hrel := monodromy_relation ρ κ c hNR
  rw [← hu] at hrel
  have hg : ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A) =
      (u : A) * (Pm ρ * Usol (Pm ρ) (θk κ) c 1) * ((u⁻¹ : Aˣ) : A) := by
    rw [← hrel, mul_assoc, Units.mul_inv, mul_one]
  rw [hg]
  exact isHeckeQuad_conj u (isHeckeQuad_P_usol c (Pm_sq ρ) (θk κ))

end Analytic


/-! ## All couplings, all generators -/

section Main

variable [CompleteSpace A]

/-- The resonant couplings `κ ∈ ±ℕ/4`. -/
def resonantSet : Set ℂ := {κ | ∃ k : ℕ, 0 < k ∧ (k : ℂ) ^ 2 = 4 * (2 * κ) ^ 2}

lemma countable_resonantSet : resonantSet.Countable := by
  refine (Set.countable_range (fun p : ℕ × Bool =>
    if p.2 then (p.1 : ℂ) / 4 else -((p.1 : ℂ) / 4))).mono ?_
  rintro κ ⟨k, -, hk⟩
  have : ((k : ℂ) - 4 * κ) * ((k : ℂ) + 4 * κ) = 0 := by linear_combination hk
  rcases mul_eq_zero.1 this with h | h
  · exact ⟨(k, true), by simp only [if_true]; linear_combination h / 4⟩
  · exact ⟨(k, false), by simp only [Bool.false_eq_true, if_false]; linear_combination -h / 4⟩

/-- The Hecke defect `β² − (q − q⁻¹)β − q q⁻¹` of `β = s • θ(σ₀)`, as a function of `κ`. -/
noncomputable def heckeDefect (κ : ℂ) : A :=
  (Complex.exp (θk κ * c) • ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A)) *
      (Complex.exp (θk κ * c) • ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A)) -
    ((Complex.exp (θk κ) - (Complex.exp (θk κ))⁻¹) •
        (Complex.exp (θk κ * c) • ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A)) +
      (Complex.exp (θk κ) * (Complex.exp (θk κ))⁻¹) • (1 : A))

lemma continuous_heckeDefect : Continuous (heckeDefect ρ c) := by
  have hg := continuous_kzBraidRep_σ ρ c (0 : Fin (m + 1))
  have hs : Continuous fun κ : ℂ => Complex.exp (θk κ * c) := by unfold θk; fun_prop
  have hq : Continuous fun κ : ℂ => Complex.exp (θk κ) := by unfold θk; fun_prop
  have hqi : Continuous fun κ : ℂ => (Complex.exp (θk κ))⁻¹ :=
    hq.inv₀ fun _ => Complex.exp_ne_zero _
  have hb := hs.smul hg
  unfold heckeDefect
  exact (hb.mul hb).sub (((hq.sub hqi).smul hb).add ((hq.mul hqi).smul continuous_const))

/-- **The Hecke quadratic for the first generator, `n ≥ 2` strands, every coupling.** -/
theorem kzBraidRep_sigma_zero_isHeckeQuad :
    IsHeckeQuad (Complex.exp (θk κ * c)) (Complex.exp (θk κ)) (Complex.exp (θk κ))⁻¹
      ((kzBraidRep ρ κ c (σ (0 : Fin (m + 1))) : Aˣ) : A) := by
  have hzero : ∀ κ' ∈ resonantSetᶜ, heckeDefect ρ c κ' = 0 := by
    intro κ' hκ'
    have hNR : NonResonant (Mc ρ κ' c 0) :=
      nonResonant_Mc0 ρ κ' c fun k hk h => hκ' ⟨k, hk, h⟩
    have := kzBraidRep_sigma_zero_isHeckeQuad_of_nonResonant ρ κ' c hNR
    unfold IsHeckeQuad at this
    unfold heckeDefect
    rw [this, sub_self]
  have hclosed : IsClosed {κ' : ℂ | heckeDefect ρ c κ' = 0} :=
    isClosed_eq (continuous_heckeDefect ρ c) continuous_const
  have hdense : Dense resonantSetᶜ := countable_resonantSet.dense_compl ℂ
  have hall : heckeDefect ρ c κ = 0 := by
    have hsub : closure resonantSetᶜ ⊆ {κ' : ℂ | heckeDefect ρ c κ' = 0} :=
      closure_minimal (fun κ' h => hzero κ' h) hclosed
    exact hsub (hdense.closure_eq ▸ Set.mem_univ κ)
  unfold heckeDefect at hall
  unfold IsHeckeQuad
  exact sub_eq_zero.1 hall

/-- **Every generator** satisfies the Hecke quadratic (the generators are conjugate). -/
theorem kzBraidRep_sigma_isHeckeQuad (j : Fin (m + 1)) :
    IsHeckeQuad (Complex.exp (θk κ * c)) (Complex.exp (θk κ)) (Complex.exp (θk κ))⁻¹
      ((kzBraidRep ρ κ c (σ j) : Aˣ) : A) :=
  isHeckeQuad_all_of_zero (kzBraidRep ρ κ c)
    (fun _ => kzBraidRep_sigma_zero_isHeckeQuad ρ κ c) j

/-- **The KZ holonomy representation factors through `H_{m+2}(q)`**, `q = e^{2πiκ}`:
`σ_j ↦ e^{2πiκc} • θ(σ_j)`. -/
noncomputable def heckeOfKZ :
    QOU.SchurWeyl.Hecke ℂ (Complex.exp (θk κ)) (Complex.exp (θk κ))⁻¹ (m + 1) →ₐ[ℂ] A :=
  heckeOfBraidRepOfZero (s := Complex.exp (θk κ * c)) (kzBraidRep ρ κ c)
    (fun _ => kzBraidRep_sigma_zero_isHeckeQuad ρ κ c)

theorem heckeOfKZ_σ (j : Fin (m + 1)) :
    heckeOfKZ ρ κ c (QOU.SchurWeyl.Hecke.σ ℂ _ _ (m + 1) j) =
      Complex.exp (θk κ * c) • ((kzBraidRep ρ κ c (σ j) : Aˣ) : A) :=
  heckeOfBraidRep_σ _ (isHeckeQuad_all_of_zero _ fun _ => kzBraidRep_sigma_zero_isHeckeQuad ρ κ c) j

end Main

end QOU.Mass.KZHolonomy.LocalMonodromy
