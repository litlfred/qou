import QOU.KZ.KZ4
import QOU.KZ.FuchsianParam
import QOU.KZ.Flat2D
import QOU.KZ.KZCorner
import QOU.KZ.KZHexagon

/-!
# Normalised solutions along a boundary divisor of the four-point KZ system

In an edge chart `(s, ε)` of `KZ4` the connection is `Ω_s = Ωs P Q B`, `Ω_ε = Ωe E A B`.
Write `ε Ω_ε = ∑_k ε^k M_k(s)` with `M₀ = E`, `M_k(s) = −A + (1−s)^k B` (`cseries_Mx`), and let
`hpar(s, ε) = ∑_k ε^k H_k(s)` be the parametric formal gauge of `FuchsianParam`. Then
`F(s, ε) = hpar(s, ε) ε^E` solves the `ε`-equation, and for every reference solution `N` of the
two-variable system, `F = N c(s)` with `c` independent of `ε`.  Comparing the `s`-derivatives and
using the asymptotic uniqueness `KZCorner.gauge_const` shows `c' = −c Ω⁰` with
`Ω⁰ = P/s + Q/(s−1)` the three-point KZ connection, so `c(s) G(s)` is constant for every
three-point KZ solution `G`.  Taking for `G` the solutions normalised at `s = 0` and `s = 1` gives
constants `a`, `b` with `N a = F G₀`, `N b = F G₁`, and `a = b Φ_KZ(P, Q)` (`edge`).

-- Ref: [drinfeld1990] Leningrad Math. J. 1 (1990) 1419–1457, §2
-- Ref: [leitner2026] docs/audits/2026-10-11-drinfeld-kohno-sl2-via-emvz.md §2 Step 1
-/

namespace QOU.KZ.KZEdge

open Set Filter Topology QOU.KZ.FuchsianFormal QOU.KZ.FuchsianAnalytic QOU.KZ.KZComplex
  QOU.KZ.FuchsianParam QOU.KZ.KZ4 QOU.KZ.KZCorner

variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

/-! ### The transverse coefficients -/

/-- `M_k(s) = −A + (1−s)^k B`, the `ε^k` coefficient of `ε Ω_ε` for `k ≥ 1`. -/
def Mt (A B : R) (k : ℕ) (s : ℂ) : R := -A + (1 - s) ^ k • B

/-- The parameter domain `U = B(1/2, 3/5) ⊃ [0, 1]`. -/
def U : Set ℂ := Metric.ball (1 / 2) (3 / 5)

theorem isOpen_U : IsOpen U := Metric.isOpen_ball

theorem norm_one_sub_le {s : ℂ} (hs : s ∈ U) : ‖1 - s‖ ≤ 11 / 10 := by
  have h : ‖1 - s‖ ≤ ‖(1 / 2 : ℂ)‖ + ‖1 / 2 - s‖ := by
    rw [show (1 : ℂ) - s = 1 / 2 + (1 / 2 - s) by ring]; exact norm_add_le _ _
  have h2 : ‖(1 / 2 : ℂ) - s‖ < 3 / 5 := by
    rw [norm_sub_rev]; simpa [U, dist_eq_norm] using hs
  have h3 : ‖(1 / 2 : ℂ)‖ = 1 / 2 := by norm_num
  linarith

theorem ofReal_mem_U {s : ℝ} (hs : s ∈ Icc (0 : ℝ) 1) : (s : ℂ) ∈ U := by
  have : dist (s : ℂ) (1 / 2) = |s - 1 / 2| := by
    rw [dist_eq_norm, show (s : ℂ) - 1 / 2 = ((s - 1 / 2 : ℝ) : ℂ) by push_cast; ring,
      Complex.norm_real, Real.norm_eq_abs]
  simp only [U, Metric.mem_ball, this, abs_lt]; constructor <;> linarith [hs.1, hs.2]

omit [CompleteSpace R] in
theorem differentiableOn_Mt (A B : R) (j : ℕ) : DifferentiableOn ℂ (Mt A B j) U := by
  intro s _
  exact ((differentiableAt_const _).add
    ((((differentiableAt_const _).sub differentiableAt_id).pow j).smul_const B)).differentiableWithinAt

omit [CompleteSpace R] in
theorem norm_Mt_le (A B : R) (j : ℕ) {s : ℂ} (hs : s ∈ U) :
    ‖Mt A B j s‖ ≤ (‖A‖ + ‖B‖) * (11 / 10) ^ j := by
  have h1 : (1 : ℝ) ≤ (11 / 10) ^ j := one_le_pow₀ (by norm_num)
  have h2 : ‖(1 - s) ^ j‖ ≤ (11 / 10) ^ j := by
    rw [norm_pow]; exact pow_le_pow_left₀ (norm_nonneg _) (norm_one_sub_le hs) j
  calc ‖Mt A B j s‖ ≤ ‖A‖ + ‖(1 - s) ^ j‖ * ‖B‖ := by
        unfold Mt; refine (norm_add_le _ _).trans ?_
        rw [norm_neg]; gcongr; exact norm_smul_le _ _
    _ ≤ ‖A‖ * (11 / 10) ^ j + (11 / 10) ^ j * ‖B‖ := by
        gcongr
        · nlinarith [norm_nonneg A]
    _ = (‖A‖ + ‖B‖) * (11 / 10) ^ j := by ring

omit [CompleteSpace R] in
/-- `ε Ω_ε` as a power series in `ε`: its coefficients are `E, M₁(s), M₂(s), …`. -/
theorem smul_cseries_Mx (E A B : R) {s ε : ℂ} (hs : s ∈ U) (hε : ‖ε‖ < 9 / 10) (hε0 : ε ≠ 0) :
    ε⁻¹ • cseries (Mx E (Mt A B) s) ε = Ωe E A B s ε := by
  have h1 : ‖ε‖ < 1 := by linarith
  have h2 : ‖ε * (1 - s)‖ < 1 := by
    rw [norm_mul]
    nlinarith [norm_one_sub_le hs, norm_nonneg ε, norm_nonneg (1 - s)]
  have hA := (hasSum_geometric_of_norm_lt_one h1).smul_const (-A)
  have hB := (hasSum_geometric_of_norm_lt_one h2).smul_const B
  have hE := hasSum_single (f := fun k : ℕ => (Pi.single 0 (E + A - B) : ℕ → R) k) 0
    (fun k hk => by simp [hk])
  have hsum := (hA.add hB).add hE
  have hcs : cseries (Mx E (Mt A B) s) ε =
      ((1 - ε)⁻¹ • (-A) + (1 - ε * (1 - s))⁻¹ • B) + E + A - B := by
    unfold cseries
    rw [show ((1 - ε)⁻¹ • (-A) + (1 - ε * (1 - s))⁻¹ • B) + E + A - B =
      ((1 - ε)⁻¹ • (-A) + (1 - ε * (1 - s))⁻¹ • B) + (Pi.single 0 (E + A - B) : ℕ → R) 0 by
        simp; abel]
    refine (HasSum.tsum_eq ?_)
    convert hsum using 1
    funext k
    rcases k with _ | k
    · simp [Mx]
    · simp [Mx, Mt, mul_pow, mul_smul]
  rw [hcs]
  have hd1 : (1 : ℂ) - ε ≠ 0 := by
    intro h
    have : ε = 1 := (sub_eq_zero.mp h).symm
    rw [this] at h1; simp at h1
  have hd2 : (1 : ℂ) - ε * (1 - s) ≠ 0 := by
    intro h
    have : ε * (1 - s) = 1 := (sub_eq_zero.mp h).symm
    rw [this] at h2; simp at h2
  have hd3 : ε - 1 ≠ 0 := by rw [← neg_sub]; exact neg_ne_zero.mpr hd1
  unfold Ωe
  rw [show (1 - s) / (1 - ε * (1 - s)) = (1 - s) * (1 - ε * (1 - s))⁻¹ by rw [div_eq_mul_inv]]
  match_scalars <;> field_simp <;> ring

/-! ### The edge solution `F(s, ε) = hpar(s, ε) ε^E` -/

section Sol

variable (E A B : R) (hE : NonResonant E)

/-- The parametric gauge for the transverse coefficients `M_k = Mt A B k`. -/
noncomputable def H (s e : ℂ) : R := hpar E hE (Mt A B) s e

/-- The edge solution `F(s, ε) = H(s, ε) ε^E`. -/
noncomputable def F (s e : ℂ) : R := H E A B hE s e * cpowA E e

theorem hθ : (9 / 10 : ℝ) * (11 / 10) < 1 := by norm_num

omit [CompleteSpace R] in
theorem hMb : ∀ j, 0 < j → ∀ s ∈ U, ‖Mt A B j s‖ ≤ (‖A‖ + ‖B‖) * (11 / 10) ^ j :=
  fun j _ _ hs => norm_Mt_le A B j hs

omit [NormedAlgebra ℂ R] [CompleteSpace R] in
theorem hC : (0 : ℝ) ≤ ‖A‖ + ‖B‖ := by positivity

/-- **The `ε`-equation along the real square.** -/
theorem hasDerivAt_F_e {s ε : ℝ} (hs : s ∈ Icc (0 : ℝ) 1) (hε0 : 0 < ε) (hε : ε < 9 / 10) :
    HasDerivAt (fun e : ℝ => F E A B hE s e) (Ωe E A B s ε * F E A B hE s ε) ε := by
  have hεn : ‖(ε : ℂ)‖ < 9 / 10 := by rwa [Complex.norm_real, Real.norm_of_nonneg hε0.le]
  have h := hasDerivAt_hpar_cpowA E hE (Mt A B) (hC A B) (by norm_num) (by norm_num) hθ
    (hMb A B) (ofReal_mem_U hs) (Complex.ofReal_mem_slitPlane.2 hε0) hεn
  have h' := hasDerivAt_comp_ofReal h
  rw [← smul_mul_assoc, smul_cseries_Mx E A B (ofReal_mem_U hs) hεn
    (Complex.ofReal_ne_zero.2 hε0.ne')] at h'
  exact h'

/-- **The `s`-derivative along the real square.** -/
theorem hasDerivAt_F_s {s ε : ℝ} (hs : s ∈ Icc (0 : ℝ) 1) (hε : |ε| < 9 / 10) :
    HasDerivAt (fun w : ℝ => F E A B hE w ε)
      (cseries (fun k => deriv (coeff E hE (Mt A B) k) s) ε * cpowA E ε) s := by
  have hεn : ‖(ε : ℂ)‖ < 9 / 10 := by rwa [Complex.norm_real, Real.norm_eq_abs]
  have h := (hasDerivAt_hpar_param E hE (Mt A B) isOpen_U (fun j _ => differentiableOn_Mt A B j)
    (hC A B) (by norm_num) (by norm_num) hθ (hMb A B) hεn).2 _ (ofReal_mem_U hs)
  exact hasDerivAt_comp_ofReal (h.mul_const (cpowA E ε))

end Sol

/-! ### The gauge argument -/

/-- The three-point KZ connection `Ω⁰(s) = P/s + Q/(s − 1)`, i.e. `Ω_s` on the divisor `ε = 0`. -/
noncomputable def Ω0 (P Q : R) (s : ℂ) : R := s⁻¹ • P + (s - 1)⁻¹ • Q

omit [CompleteSpace R] in
theorem Ωs_zero (P Q B : R) (s : ℂ) : Ωs P Q B s 0 = Ω0 P Q s := by simp [Ωs, Ω0]

omit [CompleteSpace R] in
theorem commute_Ω0 {E P Q : R} (hEP : Commute E P) (hEQ : Commute E Q) (s : ℂ) :
    Commute E (Ω0 P Q s) :=
  ((hEP.smul_right _).add_right (hEQ.smul_right _))

theorem closedBall_subset_U {s : ℝ} (hs : s ∈ Ioo (0 : ℝ) 1) :
    Metric.closedBall (s : ℂ) (1 / 10) ⊆ U := by
  intro z hz
  have h1 : dist (s : ℂ) (1 / 2) < 1 / 2 := by
    rw [dist_eq_norm, show (s : ℂ) - 1 / 2 = ((s - 1 / 2 : ℝ) : ℂ) by push_cast; ring,
      Complex.norm_real, Real.norm_eq_abs, abs_lt]
    constructor <;> linarith [hs.1, hs.2]
  have h2 := dist_triangle z (s : ℂ) (1 / 2)
  simp only [U, Metric.mem_ball]
  rw [Metric.mem_closedBall] at hz
  linarith

omit [CompleteSpace R] in
theorem analyticAt_Ωs (P Q B : R) (s : ℂ) : AnalyticAt ℂ (fun z => Ωs P Q B s z) 0 := by
  unfold Ωs
  refine analyticAt_const.sub ?_
  have h : AnalyticAt ℂ (fun z : ℂ => z / (1 - z * (1 - (s : ℂ)))) 0 :=
    analyticAt_id.div (analyticAt_const.sub (analyticAt_id.mul analyticAt_const)) (by simp)
  exact h.smul (analyticAt_const (v := B))

/-- **The gauge step.** If `c` is a unit and, along `(0, δ)`, the `s`-derivative of
`F = H ε^E` satisfies `∂_s F = Ω_s F + F c⁻¹ c'`, then `c' = −c Ω⁰`. -/
theorem gauge_zero (P Q E A B : R) (hE : NonResonant E) (hEP : Commute E P)
    (hEQ : Commute E Q) {s : ℝ} (hs : s ∈ Ioo (0 : ℝ) 1) {c c' : R} (hc : IsUnit c)
    {δ : ℝ} (hδ : 0 < δ)
    (h : ∀ t : ℝ, 0 < t → t < δ →
      cseries (fun k => deriv (coeff E hE (Mt A B) k) s) t * cpowA E t =
        Ωs P Q B s t * F E A B hE s t + F E A B hE s t * (Ring.inverse c * c')) :
    c' = -(c * Ω0 P Q s) := by
  have hsU : (s : ℂ) ∈ U := ofReal_mem_U (Ioo_subset_Icc_self hs)
  obtain ⟨δH, hδH, hHu⟩ := exists_isUnit_hpar E hE (Mt A B) (hC A B) (by norm_num)
    (by norm_num) hθ (hMb A B)
  set D : ℕ → R := fun k => deriv (coeff E hE (Mt A B) k) s with hD
  set W : ℂ → R := fun z => cseries D z + H E A B hE s z * Ω0 P Q s -
    Ωs P Q B s z * H E A B hE s z with hW
  set Uf : ℂ → R := fun z => Ring.inverse (H E A B hE s z) * W z with hUf
  set κ : R := Ring.inverse c * c' + Ω0 P Q s with hκ
  have hH0 : H E A B hE s 0 = 1 := hpar_zero E hE (Mt A B) s
  have hUan : AnalyticAt ℂ Uf 0 := by
    refine analyticAt_inverse_mul (analyticAt_hpar E hE (Mt A B) (hC A B) (by norm_num)
      (by norm_num) hθ (hMb A B) hsU) ?_ (by rw [hH0]; exact isUnit_one)
    exact ((boundedOn_deriv_coeff E hE (Mt A B) (fun j _ => differentiableOn_Mt A B j) (hC A B)
      (by norm_num) (r := 9 / 10) (by norm_num) hθ (hMb A B) (by norm_num : (0 : ℝ) < 1 / 10)
      (closedBall_subset_U hs)).2.add ((analyticAt_hpar E hE (Mt A B) (hC A B) (by norm_num)
      (by norm_num) hθ (hMb A B) hsU).mul analyticAt_const)).sub
      ((analyticAt_Ωs P Q B s).mul (analyticAt_hpar E hE (Mt A B) (hC A B) (by norm_num)
      (by norm_num) hθ (hMb A B) hsU))
  have hconj : ∀ t : ℝ, 0 < t → t < min δ δH →
      Uf t = cpowA E t * κ * cpowA (-E) t := by
    intro t ht htδ
    have htδ1 : t < δ := htδ.trans_le (min_le_left _ _)
    have hHu' : IsUnit (H E A B hE s t) := hHu _ hsU _ (by
      rw [Complex.norm_real, Real.norm_of_nonneg ht.le]; exact htδ.trans_le (min_le_right _ _))
    have hcm : Commute (cpowA E t) (Ω0 P Q s) := commute_cpowA (commute_Ω0 hEP hEQ s) t
    have h1 := h t ht htδ1
    have hWt : W t * cpowA E t = H E A B hE s t * (cpowA E t * κ) := by
      simp only [hW, hκ, F] at h1 ⊢
      rw [sub_mul, add_mul, h1, mul_assoc (H E A B hE s t) (Ω0 P Q s), ← hcm.eq]
      noncomm_ring
    have hWt' : W t = H E A B hE s t * (cpowA E t * κ * cpowA (-E) t) := by
      calc W t = W t * cpowA E t * cpowA (-E) t := by
            rw [mul_assoc, cpowA_mul_cpowA_neg, mul_one]
        _ = _ := by rw [hWt]; simp only [mul_assoc]
    simp only [hUf]
    rw [hWt', ← mul_assoc, Ring.inverse_mul_cancel _ hHu', one_mul]
  have hg := (gauge_const (fun k hk => (hE k hk).1) hUan (lt_min hδ hδH) hconj).1
  have hU0 : Uf 0 = 0 := by
    have hD0 : cseries D 0 = 0 := by
      rw [KZHalfMonodromy.cseries_zero, hD]
      dsimp only
      have : coeff E hE (Mt A B) 0 = fun _ => 1 := funext (coeff_zero E hE (Mt A B))
      rw [this, deriv_const]
    simp only [hUf, hW, hH0, Ωs_zero, hD0, Ring.inverse_one, one_mul, mul_one, zero_add, sub_self]
  rw [hU0] at hg
  have e : Ring.inverse c * c' = -Ω0 P Q s := eq_neg_of_add_eq_zero_left hg
  calc c' = c * (Ring.inverse c * c') := by rw [← mul_assoc, Ring.mul_inverse_cancel _ hc, one_mul]
    _ = -(c * Ω0 P Q s) := by rw [e, mul_neg]

/-! ### The edge theorem -/

omit [CompleteSpace R] in
theorem Ω0_ofReal (P Q : R) (s : ℝ) : Ω0 P Q s = AssociatorKZ.kzΩ P Q s := by
  simp only [Ω0, AssociatorKZ.kzΩ, ← Complex.coe_smul]; push_cast; rfl

theorem exists_hasDerivAt_ringInverse {f : ℝ → R} {f' : R} {x : ℝ} (hf : HasDerivAt f f' x)
    (hu : IsUnit (f x)) : ∃ d, HasDerivAt (fun t => Ring.inverse (f t)) d x := by
  obtain ⟨u, hu⟩ := hu
  have hI : HasFDerivAt Ring.inverse (-ContinuousLinearMap.mulLeftRight ℝ R ↑u⁻¹ ↑u⁻¹) (f x) := by
    rw [← hu]; exact hasFDerivAt_ringInverse u
  exact ⟨_, hI.comp_hasDerivAt x hf⟩

/-- **The edge theorem.** Let `N` solve the two-variable system on the square in an edge chart,
with unit values. Then there are `δ > 0` and units `c(s)` with `F(s, ε) = N(s, ε) c(s)` on
`(0, 1) × (0, δ)`, and `c(s) G(s)` is constant for every three-point KZ solution `G`. -/
theorem edge (P Q E A B : R) (hE : NonResonant E) (hEP : Commute E P) (hEQ : Commute E Q)
    {N : ℝ × ℝ → R}
    (hN : Flat2D.IsSol2 (fun q => Ωs P Q B q.1 q.2) (fun q => Ωe E A B q.1 q.2) N sq)
    (hNu : ∀ q ∈ sq, IsUnit (N q)) :
    ∃ δ > 0, δ < 1 ∧ ∃ c : ℝ → R, (∀ s ∈ Ioo (0 : ℝ) 1, IsUnit (c s)) ∧
      (∀ s ∈ Ioo (0 : ℝ) 1, ∀ ε ∈ Ioo (0 : ℝ) δ, F E A B hE s ε = N (s, ε) * c s) ∧
      ∀ G : ℝ → R, AssociatorKZ.IsKZSol P Q G → ∃ a, ∀ s ∈ Ioo (0 : ℝ) 1, c s * G s = a := by
  obtain ⟨δH, hδH, hHu⟩ := exists_isUnit_hpar E hE (Mt A B) (hC A B) (by norm_num)
    (by norm_num) hθ (hMb A B)
  set δ : ℝ := min (1 / 2) δH with hδdef
  have hδ : 0 < δ := lt_min (by norm_num) hδH
  have hδ1 : δ ≤ 1 / 2 := min_le_left _ _
  have hδ2 : δ ≤ δH := min_le_right _ _
  set ε0 : ℝ := δ / 2 with hε0def
  have hε0 : ε0 ∈ Ioo (0 : ℝ) δ := ⟨by positivity, by linarith⟩
  set c : ℝ → R := fun s => Ring.inverse (N (s, ε0)) * F E A B hE s ε0 with hcdef
  have hsq : ∀ {s e : ℝ}, s ∈ Ioo (0 : ℝ) 1 → e ∈ Ioo (0 : ℝ) (9 / 10) → (s, e) ∈ sq :=
    fun hs he => ⟨hs, he.1, by linarith [he.2]⟩
  have hIoo : ∀ {e : ℝ}, e ∈ Ioo (0 : ℝ) δ → e ∈ Ioo (0 : ℝ) (9 / 10) :=
    fun he => ⟨he.1, by linarith [he.2]⟩
  -- `F = N c`
  have hFN : ∀ s ∈ Ioo (0 : ℝ) 1, ∀ ε ∈ Ioo (0 : ℝ) δ, F E A B hE s ε = N (s, ε) * c s := by
    intro s hs ε hε
    have hv : Ring.inverse (N (s, ε)) * F E A B hE s ε = c s :=
      Flat2D.eq_of_hasDerivAt_zero_Ioo (h := fun e => Ring.inverse (N (s, e)) * F E A B hE s e)
        (fun e he => Flat2D.hasDerivAt_inverse_mul (hN (s, e) (hsq hs he)).2
          (hasDerivAt_F_e E A B hE (Ioo_subset_Icc_self hs) he.1 he.2) (hNu _ (hsq hs he)))
        (hIoo hε) (hIoo hε0)
    rw [← hv, ← mul_assoc, Ring.mul_inverse_cancel _ (hNu _ (hsq hs (hIoo hε))), one_mul]
  -- `c` is a unit
  have hcu : ∀ s ∈ Ioo (0 : ℝ) 1, IsUnit (c s) := by
    intro s hs
    have hFu : IsUnit (F E A B hE s ε0) := by
      refine IsUnit.mul (hHu _ (ofReal_mem_U (Ioo_subset_Icc_self hs)) _ ?_) (isUnit_cpowA E _)
      rw [Complex.norm_real, Real.norm_of_nonneg hε0.1.le]; linarith [hε0.2]
    exact (hNu _ (hsq hs (hIoo hε0))).ringInverse.mul hFu
  -- `c` is differentiable
  have hcd : ∀ s ∈ Ioo (0 : ℝ) 1, ∃ c', HasDerivAt c c' s := by
    intro s hs
    obtain ⟨d, hd⟩ := exists_hasDerivAt_ringInverse (hN (s, ε0) (hsq hs (hIoo hε0))).1
      (hNu _ (hsq hs (hIoo hε0)))
    have hF := hasDerivAt_F_s E A B hE (Ioo_subset_Icc_self hs)
      (ε := ε0) (by rw [abs_of_pos hε0.1]; linarith [hε0.2])
    exact ⟨_, hd.mul hF⟩
  -- `c' = −c Ω⁰`
  have hc' : ∀ s ∈ Ioo (0 : ℝ) 1, HasDerivAt c (-(c s * Ω0 P Q s)) s := by
    intro s hs
    obtain ⟨c', hc'⟩ := hcd s hs
    suffices e : c' = -(c s * Ω0 P Q s) by rw [← e]; exact hc'
    refine gauge_zero P Q E A B hE hEP hEQ hs (hcu s hs) hδ fun t ht htδ => ?_
    have htI : t ∈ Ioo (0 : ℝ) δ := ⟨ht, htδ⟩
    have hNc := (hN (s, t) (hsq hs (hIoo htI))).1.mul hc'
    have hev : (fun w : ℝ => F E A B hE w t) =ᶠ[𝓝 s] fun w => N (w, t) * c w := by
      filter_upwards [Ioo_mem_nhds hs.1 hs.2] with w hw
      exact hFN w hw t htI
    have hF := hasDerivAt_F_s E A B hE (Ioo_subset_Icc_self hs)
      (ε := t) (by rw [abs_of_pos ht]; linarith [hδ1])
    rw [hF.unique (hNc.congr_of_eventuallyEq hev), hFN s hs t htI]
    simp only
    rw [mul_assoc (N (s, t)) (c s), ← mul_assoc (c s), Ring.mul_inverse_cancel _ (hcu s hs),
      one_mul, mul_assoc]
  refine ⟨δ, hδ, by linarith, c, hcu, hFN, fun G hG => ?_⟩
  have hz : ∀ s ∈ Ioo (0 : ℝ) 1, HasDerivAt (fun s => c s * G s) 0 s := by
    intro s hs
    have h := (hc' s hs).mul (hG s hs)
    rw [← Ω0_ofReal] at h
    convert h using 1
    noncomm_ring
  refine ⟨c (1 / 2) * G (1 / 2), fun s hs => ?_⟩
  exact Flat2D.eq_of_hasDerivAt_zero_Ioo hz hs ⟨by norm_num, by norm_num⟩

end QOU.KZ.KZEdge
