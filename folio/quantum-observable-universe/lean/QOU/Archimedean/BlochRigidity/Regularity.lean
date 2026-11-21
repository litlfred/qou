import Mathlib.MeasureTheory.Function.Jacobian
import Mathlib.RingTheory.Complex
import Mathlib.MeasureTheory.Measure.Lebesgue.Complex
import Mathlib.Analysis.Calculus.BumpFunction.Normed
import Mathlib.Analysis.Calculus.BumpFunction.InnerProduct
import Mathlib.Analysis.Convolution
import Mathlib.Analysis.Calculus.Deriv.Inv
import QOU.Archimedean.BlochRigidity.Algebra


/-!
# Bloch–Suslin rigidity: analytic proposition R (regularity)

**Proposition R.** A function `φ : ℂ → ℝ` that is continuous on `{0,1}ᶜ`, inversion-odd and
satisfies Suslin's five-term relation is `C^∞` on `{0,1}ᶜ` (`contDiffOn_of_fiveTerm`).

This is the first of the analytic steps, isolated from the algebra. The only algebraic input
is `five_term_rearranged` from `Algebra.lean`. Method: integrate that identity against a
normalized bump `ψ(y)`, change variables in each term so that `x` appears only in a smooth
kernel, and apply Mathlib's theorem on convolution with a parameter
(`contDiffOn_convolution_right_with_param_comp`).
-/

open MeasureTheory Complex

namespace QOU.Archimedean.BlochRigidity

/-- The real determinant of multiplication by `c` on `ℂ` is `‖c‖²`. -/
theorem det_mul_eq_normSq (c : ℂ) :
    LinearMap.det (((ContinuousLinearMap.smulRight (1 : ℂ →L[ℂ] ℂ) c).restrictScalars ℝ :
      ℂ →L[ℝ] ℂ) : ℂ →ₗ[ℝ] ℂ) = Complex.normSq c := by
  rw [← Algebra.norm_complex_apply, Algebra.norm_apply]
  congr 1
  ext v
  simp [mul_comm]

/-- Change of variables along a holomorphic map, injective on `S`. -/
theorem integral_image_holo {g g' : ℂ → ℂ} {S : Set ℂ} (hS : MeasurableSet S)
    (hd : ∀ y ∈ S, HasDerivAt g (g' y) y) (hinj : Set.InjOn g S) (F : ℂ → ℝ) :
    ∫ t in g '' S, F t = ∫ y in S, Complex.normSq (g' y) * F (g y) := by
  have := integral_image_eq_integral_abs_det_fderiv_smul (μ := volume) hS
    (f' := fun y => (ContinuousLinearMap.smulRight (1 : ℂ →L[ℂ] ℂ) (g' y)).restrictScalars ℝ)
    (fun y hy => ((hd y hy).hasFDerivAt.restrictScalars ℝ).hasFDerivWithinAt) hinj F
  rw [this]
  congr 1
  ext y
  rw [ContinuousLinearMap.det, det_mul_eq_normSq, abs_of_nonneg (Complex.normSq_nonneg _),
    smul_eq_mul]

theorem integral_eq_compl_singleton (a : ℂ) (F : ℂ → ℝ) :
    ∫ y in ({a}ᶜ : Set ℂ), F y = ∫ y, F y := by
  rw [Measure.restrict_eq_self_of_ae_mem]
  rw [ae_iff]; simp

/-- `∫ F(y) dy = ‖x‖² ∫ F(x t) dt`. -/
theorem integral_comp_mul {x : ℂ} (hx : x ≠ 0) (F : ℂ → ℝ) :
    ∫ y, F y = ∫ t, Complex.normSq x * F (x * t) := by
  have h := integral_image_holo (g := fun t => x * t) (g' := fun _ => x) MeasurableSet.univ
    (fun y _ => by simpa using (hasDerivAt_id y).const_mul x)
    (fun a _ b _ hab => mul_left_cancel₀ hx hab) F
  have himg : (fun t => x * t) '' Set.univ = Set.univ := by
    apply Set.eq_univ_of_forall; intro y; exact ⟨y / x, trivial, by field_simp⟩
  rw [himg, setIntegral_univ, setIntegral_univ] at h
  exact h

/-- `∫ F(y) dy = ‖c‖² ∫ F(1 − c t) dt`. -/
theorem integral_comp_one_sub_mul {c : ℂ} (hc : c ≠ 0) (F : ℂ → ℝ) :
    ∫ y, F y = ∫ t, Complex.normSq c * F (1 - c * t) := by
  have h := integral_image_holo (g := fun t => 1 - c * t) (g' := fun _ => -c) MeasurableSet.univ
    (fun y _ => by simpa using ((hasDerivAt_id y).const_mul c).const_sub 1)
    (fun a _ b _ hab => mul_left_cancel₀ hc (by simpa using hab)) F
  have himg : (fun t => 1 - c * t) '' Set.univ = Set.univ := by
    apply Set.eq_univ_of_forall; intro y; exact ⟨(1 - y) / c, trivial, by field_simp; ring⟩
  rw [himg, setIntegral_univ, setIntegral_univ] at h
  simpa [Complex.normSq_neg] using h

/-- `∫ F(y) dy = ∫ ‖c/(1−ct)²‖² F((1 − c t)⁻¹) dt`. -/
theorem integral_comp_inv_one_sub_mul {c : ℂ} (hc : c ≠ 0) (F : ℂ → ℝ) :
    ∫ y, F y = ∫ t, Complex.normSq (c / (1 - c * t) ^ 2) * F ((1 - c * t)⁻¹) := by
  set S : Set ℂ := {c⁻¹}ᶜ
  have hS1 : ∀ t ∈ S, 1 - c * t ≠ 0 := by
    intro t ht h
    apply ht
    show t = c⁻¹
    field_simp
    linear_combination -h
  have h := integral_image_holo (g := fun t => (1 - c * t)⁻¹) (g' := fun t => c / (1 - c * t) ^ 2)
    (S := S) (measurableSet_singleton _).compl
    (fun y hy => by
      have h0 : HasDerivAt (fun t => 1 - c * t) (-c) y := by
        simpa using ((hasDerivAt_id y).const_mul c).const_sub 1
      have h1 := h0.inv (hS1 y hy)
      convert h1 using 1; field_simp)
    (fun a ha b hb hab => by
      have := inv_inj.1 hab
      exact mul_left_cancel₀ hc (by linear_combination -this)) F
  have himg : (fun t => (1 - c * t)⁻¹) '' S = ({0}ᶜ : Set ℂ) := by
    ext y; constructor
    · rintro ⟨t, ht, rfl⟩; exact inv_ne_zero (hS1 t ht)
    · intro hy
      have hy' : y ≠ 0 := hy
      refine ⟨(1 - y⁻¹) / c, ?_, ?_⟩
      · intro h
        have h' : (1 - y⁻¹) / c = c⁻¹ := h
        field_simp at h'
        have : (1:ℂ) = 0 := by linear_combination -h'
        exact one_ne_zero this
      · simp only; field_simp; ring
  rw [himg, integral_eq_compl_singleton, integral_eq_compl_singleton] at h
  exact h

/-- An integral against a smooth, parameter-dependent kernel with fixed compact support
`k` is smooth in the parameter, for any `φ` continuous on a neighbourhood of `k`.
(Mathlib's convolution-with-parameter theorem, evaluated at `0`.) -/
theorem contDiffOn_integral_kernel {φ : ℂ → ℝ} {U k s : Set ℂ} (hk : IsCompact k)
    (hkU : k ⊆ U) (hφ : ContinuousOn φ U) (hs : IsOpen s) {K : ℂ → ℂ → ℝ}
    (hK : ContDiffOn ℝ (⊤ : ℕ∞) (Function.uncurry K) (s ×ˢ Set.univ))
    (hKs : ∀ p ∈ s, ∀ t ∉ k, K p t = 0) :
    ContDiffOn ℝ (⊤ : ℕ∞) (fun p => ∫ t, K p t * φ t) s := by
  classical
  set f : ℂ → ℝ := k.indicator φ
  set g : ℂ → ℂ → ℝ := fun p u => K p (-u)
  have hf : LocallyIntegrable f volume := by
    have : IntegrableOn φ k volume := (hφ.mono hkU).integrableOn_compact hk
    exact ((integrable_indicator_iff hk.measurableSet).2 this).locallyIntegrable
  have hgs : ∀ p, ∀ x, p ∈ s → x ∉ -k → g p x = 0 := by
    intro p x hp hx
    exact hKs p hp (-x) (by simpa [Set.mem_neg] using hx)
  have hg : ContDiffOn ℝ (⊤ : ℕ∞) (Function.uncurry g) (s ×ˢ Set.univ) := by
    have : Function.uncurry g = Function.uncurry K ∘ (fun q : ℂ × ℂ => (q.1, -q.2)) := rfl
    rw [this]
    refine hK.comp (contDiff_fst.prodMk contDiff_snd.neg).contDiffOn ?_
    intro q hq; exact ⟨hq.1, Set.mem_univ _⟩
  have main := contDiffOn_convolution_right_with_param_comp (μ := volume)
    (ContinuousLinearMap.lsmul ℝ ℝ) (v := fun _ : ℂ => (0 : ℂ)) contDiffOn_const hs
    hk.neg hgs hf hg
  refine main.congr ?_
  intro p hp
  rw [convolution_def]
  refine integral_congr_ae (Filter.Eventually.of_forall fun t => ?_)
  simp only [ContinuousLinearMap.lsmul_apply, smul_eq_mul, zero_sub, neg_neg, g, f]
  by_cases ht : t ∈ k
  · simp [Set.indicator_of_mem ht, mul_comm]
  · simp [Set.indicator_of_notMem ht, hKs p hp t ht]

theorem contDiff_normSq {n : ℕ∞} : ContDiff ℝ n (fun z : ℂ => Complex.normSq z) := by
  have hr : ContDiff ℝ n (fun z : ℂ => z.re) := Complex.reCLM.contDiff
  have hi : ContDiff ℝ n (fun z : ℂ => z.im) := Complex.imCLM.contDiff
  simpa [Complex.normSq_apply] using (hr.mul hr).add (hi.mul hi)

/-- A continuous-on-`Y` integrand that vanishes off a compact `Y` is integrable. -/
theorem integrable_of_vanish {F : ℂ → ℝ} {Y : Set ℂ} (hY : IsCompact Y)
    (hF : ContinuousOn F Y) (h0 : ∀ y ∉ Y, F y = 0) : Integrable F := by
  have hi : Integrable (Y.indicator F) :=
    (integrable_indicator_iff hY.measurableSet).2 (hF.integrableOn_compact hY)
  refine hi.congr (Filter.Eventually.of_forall fun y => ?_)
  by_cases hy : y ∈ Y
  · simp [Set.indicator_of_mem hy]
  · simp [Set.indicator_of_notMem hy, h0 y hy]

/-- `Ψ(w) = ‖w⁻¹‖⁴ ψ(w⁻¹)` is smooth on all of `ℂ` when `ψ` is smooth and vanishes
outside a bounded set avoiding `0`: near `w = 0` it is identically zero. -/
theorem contDiff_invKernel {ψ : ℂ → ℝ} {M : ℝ} (hM : 0 < M) (hψ : ContDiff ℝ (⊤ : ℕ∞) ψ)
    (hψ0 : ∀ y, M < ‖y‖ → ψ y = 0) (hψz : ψ 0 = 0) :
    ContDiff ℝ (⊤ : ℕ∞) (fun w : ℂ => Complex.normSq w⁻¹ ^ 2 * ψ w⁻¹) := by
  rw [contDiff_iff_contDiffAt]
  intro w
  by_cases hw : w = 0
  · subst hw
    refine (contDiffAt_const (c := (0 : ℝ))).congr_of_eventuallyEq ?_
    have : Metric.ball (0 : ℂ) M⁻¹ ∈ nhds (0 : ℂ) := Metric.ball_mem_nhds _ (inv_pos.2 hM)
    filter_upwards [this] with v hv
    by_cases hv0 : v = 0
    · simp [hv0, hψz]
    · have : M < ‖v⁻¹‖ := by
        rw [norm_inv]
        rw [Metric.mem_ball, dist_zero_right] at hv
        exact (lt_inv_comm₀ hM (norm_pos_iff.2 hv0)).2 hv
      simp [hψ0 _ this]
  · have hi : ContDiffAt ℝ (⊤ : ℕ∞) (fun w : ℂ => w⁻¹) w := contDiffAt_inv ℝ hw
    exact ((contDiff_normSq.contDiffAt.comp w hi).pow 2).mul (hψ.contDiffAt.comp w hi)

/-- Membership in `{0,1}ᶜ`. -/
theorem mem_U {z : ℂ} : z ∈ ({0, 1}ᶜ : Set ℂ) ↔ z ≠ 0 ∧ z ≠ 1 := by
  simp [Set.mem_compl_iff, Set.mem_insert_iff, not_or]

/-- **Regularity core.** Let `φ` be continuous on `{0,1}ᶜ`, inversion-odd and satisfying
the five-term relation.  Let `X, Y` be compact, with `X, Y ⊆ {0,1}ᶜ` and `X ∩ Y = ∅`, let
`ψ` be smooth with `∫ ψ = 1`, vanishing off `Y` and off `‖y‖ ≤ M`.  Then `φ` is smooth on any
open `s ⊆ X`. -/
theorem contDiffOn_of_fiveTerm_core {φ : ℂ → ℝ} (hφ : ContinuousOn φ {0, 1}ᶜ)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {X Y s : Set ℂ} (hX : IsCompact X) (hY : IsCompact Y) (hs : IsOpen s) (hsX : s ⊆ X)
    (hX0 : ∀ x ∈ X, x ≠ 0) (hX1 : ∀ x ∈ X, x ≠ 1)
    (hY0 : ∀ y ∈ Y, y ≠ 0) (hY1 : ∀ y ∈ Y, y ≠ 1) (hXY : ∀ x ∈ X, ∀ y ∈ Y, x ≠ y)
    {ψ : ℂ → ℝ} (hψ : ContDiff ℝ (⊤ : ℕ∞) ψ) (hψ1 : ∫ y, ψ y = 1)
    (hψY : ∀ y ∉ Y, ψ y = 0) {M : ℝ} (hM : 0 < M) (hYM : ∀ y ∈ Y, ‖y‖ ≤ M) :
    ContDiffOn ℝ (⊤ : ℕ∞) φ s := by
  classical
  set U : Set ℂ := {0, 1}ᶜ
  set Ψ : ℂ → ℝ := fun w => Complex.normSq w⁻¹ ^ 2 * ψ w⁻¹
  have hψc : Continuous ψ := hψ.continuous
  have hΨ : ContDiff ℝ (⊤ : ℕ∞) Ψ := by
    refine contDiff_invKernel hM hψ (fun y hy => hψY y fun hyY => ?_) (hψY 0 fun h0 => hY0 0 h0 rfl)
    exact absurd (hYM y hyY) (not_le.2 hy)
  -- kernels
  set KA : ℂ → ℂ → ℝ := fun x t => Complex.normSq x * ψ (x * t)
  set KB : ℂ → ℂ → ℝ := fun x t => Complex.normSq (1 - x⁻¹) * Ψ (1 - (1 - x⁻¹) * t)
  set KC : ℂ → ℂ → ℝ := fun x t => Complex.normSq (1 - x) * ψ (1 - (1 - x) * t)
  -- compact supports in the parameter-free variable
  set kA : Set ℂ := (fun p : ℂ × ℂ => p.2 / p.1) '' (X ×ˢ Y)
  set kB : Set ℂ := (fun p : ℂ × ℂ => (1 - p.2⁻¹) / (1 - p.1⁻¹)) '' (X ×ˢ Y)
  set kC : Set ℂ := (fun p : ℂ × ℂ => (1 - p.2) / (1 - p.1)) '' (X ×ˢ Y)
  have hXY' := hX.prod hY
  have hkA : IsCompact kA := hXY'.image_of_continuousOn
    (continuousOn_snd.div continuousOn_fst fun p hp => hX0 p.1 hp.1)
  have hkB : IsCompact kB := by
    refine hXY'.image_of_continuousOn (ContinuousOn.div ?_ ?_ ?_)
    · exact continuousOn_const.sub (continuousOn_snd.inv₀ fun p hp => hY0 p.2 hp.2)
    · exact continuousOn_const.sub (continuousOn_fst.inv₀ fun p hp => hX0 p.1 hp.1)
    · exact fun p hp => one_sub_inv_ne_zero (hX1 p.1 hp.1)
  have hkC : IsCompact kC := by
    refine hXY'.image_of_continuousOn (ContinuousOn.div ?_ ?_ ?_)
    · exact continuousOn_const.sub continuousOn_snd
    · exact continuousOn_const.sub continuousOn_fst
    · exact fun p hp => sub_ne_zero.2 (Ne.symm (hX1 p.1 hp.1))
  have hkAU : kA ⊆ U := by
    rintro _ ⟨⟨x, y⟩, ⟨hx, hy⟩, rfl⟩
    refine mem_U.2 ⟨div_ne_zero (hY0 y hy) (hX0 x hx), ?_⟩
    rw [Ne, div_eq_one_iff_eq (hX0 x hx)]; exact Ne.symm (hXY x hx y hy)
  have hkBU : kB ⊆ U := by
    rintro _ ⟨⟨x, y⟩, ⟨hx, hy⟩, rfl⟩
    exact mem_U.2 (flip_args (hX1 x hx) (hY1 y hy) (hXY x hx y hy)).1
  have hkCU : kC ⊆ U := by
    rintro _ ⟨⟨x, y⟩, ⟨hx, hy⟩, rfl⟩
    exact mem_U.2 (flip_args (hX1 x hx) (hY1 y hy) (hXY x hx y hy)).2
  -- the kernels vanish off the compact supports
  have hψmem : ∀ y, ψ y ≠ 0 → y ∈ Y := fun y h => by_contra fun hn => h (hψY y hn)
  have hKA0 : ∀ p ∈ s, ∀ t ∉ kA, KA p t = 0 := by
    intro x hx t ht
    have hx0 := hX0 x (hsX hx)
    have : ψ (x * t) = 0 := by
      by_contra h
      exact ht ⟨(x, x * t), ⟨hsX hx, hψmem _ h⟩, by simp [mul_div_cancel_left₀ _ hx0]⟩
    simp [KA, this]
  have hKB0 : ∀ p ∈ s, ∀ t ∉ kB, KB p t = 0 := by
    intro x hx t ht
    have hc := one_sub_inv_ne_zero (hX1 x (hsX hx))
    have : ψ (1 - (1 - x⁻¹) * t)⁻¹ = 0 := by
      by_contra h
      refine ht ⟨(x, (1 - (1 - x⁻¹) * t)⁻¹), ⟨hsX hx, hψmem _ h⟩, ?_⟩
      simp only [inv_inv, sub_sub_cancel]
      exact mul_div_cancel_left₀ _ hc
    simp [KB, Ψ, this]
  have hKC0 : ∀ p ∈ s, ∀ t ∉ kC, KC p t = 0 := by
    intro x hx t ht
    have hc : 1 - x ≠ 0 := sub_ne_zero.2 (Ne.symm (hX1 x (hsX hx)))
    have : ψ (1 - (1 - x) * t) = 0 := by
      by_contra h
      refine ht ⟨(x, 1 - (1 - x) * t), ⟨hsX hx, hψmem _ h⟩, ?_⟩
      simp only [sub_sub_cancel]
      exact mul_div_cancel_left₀ _ hc
    simp [KC, this]
  -- the kernels are smooth on `s × ℂ`
  have hsU : ∀ p ∈ s ×ˢ (Set.univ : Set ℂ), p.1 ≠ 0 := fun p hp => hX0 p.1 (hsX hp.1)
  have hcB : ContDiffOn ℝ (⊤ : ℕ∞) (fun p : ℂ × ℂ => 1 - p.1⁻¹) (s ×ˢ Set.univ) :=
    contDiffOn_const.sub ((contDiffOn_inv ℝ).comp contDiff_fst.contDiffOn
      fun p hp => hsU p hp)
  have hKAs : ContDiffOn ℝ (⊤ : ℕ∞) (Function.uncurry KA) (s ×ˢ Set.univ) :=
    ((contDiff_normSq.comp contDiff_fst).mul
      (hψ.comp (contDiff_fst.mul contDiff_snd))).contDiffOn
  have hKBs : ContDiffOn ℝ (⊤ : ℕ∞) (Function.uncurry KB) (s ×ˢ Set.univ) :=
    (contDiff_normSq.comp_contDiffOn hcB).mul
      (hΨ.comp_contDiffOn (contDiffOn_const.sub (hcB.mul contDiff_snd.contDiffOn)))
  have hKCs : ContDiffOn ℝ (⊤ : ℕ∞) (Function.uncurry KC) (s ×ˢ Set.univ) :=
    ((contDiff_normSq.comp (contDiff_const.sub contDiff_fst)).mul
      (hψ.comp (contDiff_const.sub ((contDiff_const.sub contDiff_fst).mul contDiff_snd)))).contDiffOn
  have hA := contDiffOn_integral_kernel hkA hkAU hφ hs hKAs hKA0
  have hB := contDiffOn_integral_kernel hkB hkBU hφ hs hKBs hKB0
  have hC := contDiffOn_integral_kernel hkC hkCU hφ hs hKCs hKC0
  -- the integral identity on `s`
  refine ((contDiffOn_const (c := ∫ y, ψ y * φ y)).sub hA |>.sub hB |>.add hC).congr ?_
  intro x hx
  have hxX := hsX hx
  have hx0 := hX0 x hxX
  have hx1 := hX1 x hxX
  have hcx : 1 - x⁻¹ ≠ 0 := one_sub_inv_ne_zero hx1
  have hcx' : 1 - x ≠ 0 := sub_ne_zero.2 (Ne.symm hx1)
  -- integrability of the four terms
  have hint : ∀ g : ℂ → ℂ, ContinuousOn g Y → (∀ y ∈ Y, g y ∈ U) →
      Integrable (fun y => ψ y * φ (g y)) := by
    intro g hg hgU
    refine integrable_of_vanish hY (hψc.continuousOn.mul (hφ.comp hg hgU)) ?_
    intro y hy; simp [hψY y hy]
  have i1 := hint id continuousOn_id fun y hy => mem_U.2 ⟨hY0 y hy, hY1 y hy⟩
  have i2 := hint (fun y => y / x) (continuousOn_id.div_const x) fun y hy => by
    refine mem_U.2 ⟨div_ne_zero (hY0 y hy) hx0, ?_⟩
    rw [Ne, div_eq_one_iff_eq hx0]; exact Ne.symm (hXY x hxX y hy)
  have i3 := hint (fun y => (1 - y⁻¹) / (1 - x⁻¹))
    ((continuousOn_const.sub (continuousOn_id.inv₀ fun y hy => hY0 y hy)).div_const _)
    fun y hy => mem_U.2 (flip_args hx1 (hY1 y hy) (hXY x hxX y hy)).1
  have i4 := hint (fun y => (1 - y) / (1 - x))
    ((continuousOn_const.sub continuousOn_id).div_const _)
    fun y hy => mem_U.2 (flip_args hx1 (hY1 y hy) (hXY x hxX y hy)).2
  have hpt : ∀ y, ψ y * φ x = ψ y * φ (id y) - ψ y * φ (y / x)
      - ψ y * φ ((1 - y⁻¹) / (1 - x⁻¹)) + ψ y * φ ((1 - y) / (1 - x)) := by
    intro y
    by_cases hy : y ∈ Y
    · rw [five_term_rearranged hinv h5 hx0 hx1 (hY0 y hy) (hY1 y hy) (hXY x hxX y hy)]
      simp only [id]; ring
    · simp [hψY y hy]
  have hφx : φ x = ∫ y, ψ y * φ x := by rw [integral_mul_const, hψ1, one_mul]
  have e1 : (∫ y, (ψ y * φ (id y) - ψ y * φ (y / x) - ψ y * φ ((1 - y⁻¹) / (1 - x⁻¹))
      + ψ y * φ ((1 - y) / (1 - x)))) = (∫ y, (ψ y * φ (id y) - ψ y * φ (y / x)
      - ψ y * φ ((1 - y⁻¹) / (1 - x⁻¹)))) + (∫ y, ψ y * φ ((1 - y) / (1 - x))) :=
    integral_add ((i1.sub i2).sub i3) i4
  have e2 : (∫ y, (ψ y * φ (id y) - ψ y * φ (y / x) - ψ y * φ ((1 - y⁻¹) / (1 - x⁻¹))))
      = (∫ y, (ψ y * φ (id y) - ψ y * φ (y / x)))
        - (∫ y, ψ y * φ ((1 - y⁻¹) / (1 - x⁻¹))) := integral_sub (i1.sub i2) i3
  have e3 : (∫ y, (ψ y * φ (id y) - ψ y * φ (y / x)))
      = (∫ y, ψ y * φ (id y)) - (∫ y, ψ y * φ (y / x)) := integral_sub i1 i2
  rw [hφx, integral_congr_ae (Filter.Eventually.of_forall hpt), e1, e2, e3]
  -- change of variables in each term
  have cA : ∫ y, ψ y * φ (y / x) = ∫ t, KA x t * φ t := by
    rw [integral_comp_mul hx0]
    refine integral_congr_ae (Filter.Eventually.of_forall fun t => ?_)
    simp only [KA, mul_div_cancel_left₀ _ hx0]; ring
  have cB : ∫ y, ψ y * φ ((1 - y⁻¹) / (1 - x⁻¹)) = ∫ t, KB x t * φ t := by
    rw [integral_comp_inv_one_sub_mul hcx]
    refine integral_congr_ae (Filter.Eventually.of_forall fun t => ?_)
    simp only [KB, Ψ, inv_inv, sub_sub_cancel, mul_div_cancel_left₀ _ hcx]
    rw [map_div₀, map_pow, map_inv₀]
    ring
  have cC : ∫ y, ψ y * φ ((1 - y) / (1 - x)) = ∫ t, KC x t * φ t := by
    rw [integral_comp_one_sub_mul hcx']
    refine integral_congr_ae (Filter.Eventually.of_forall fun t => ?_)
    simp only [KC, sub_sub_cancel, mul_div_cancel_left₀ _ hcx']; ring
  rw [cA, cB, cC]
  rfl

/-- **Stage R.** A solution of the five-term relation that is continuous on `{0,1}ᶜ` and
inversion-odd is `C^∞` on `{0,1}ᶜ`. -/
theorem contDiffOn_of_fiveTerm {φ : ℂ → ℝ} (hφ : ContinuousOn φ {0, 1}ᶜ)
    (hinv : ∀ z : ℂ, z ≠ 0 → z ≠ 1 → φ z⁻¹ = -φ z)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0) :
    ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ := by
  intro x₀ hx₀
  obtain ⟨h00, h01⟩ := mem_U.1 hx₀
  set δ : ℝ := min (min ‖x₀‖ ‖x₀ - 1‖) 1 with hδ
  have hδpos : 0 < δ := lt_min (lt_min (norm_pos_iff.2 h00)
    (norm_pos_iff.2 (sub_ne_zero.2 h01))) one_pos
  have hδ0 : δ ≤ ‖x₀‖ := (min_le_left _ _).trans (min_le_left _ _)
  have hδ1 : δ ≤ ‖x₀ - 1‖ := (min_le_left _ _).trans (min_le_right _ _)
  have hδ2 : δ ≤ 1 := min_le_right _ _
  set y₀ : ℂ := ((‖x₀‖ + 3 : ℝ) : ℂ)
  have hy₀ : ‖y₀‖ = ‖x₀‖ + 3 := by
    simp only [y₀, Complex.norm_real, Real.norm_eq_abs]
    exact abs_of_pos (by positivity)
  set X : Set ℂ := Metric.closedBall x₀ (δ / 2)
  set Y : Set ℂ := Metric.closedBall y₀ 1
  have hXn : ∀ x ∈ X, ‖x - x₀‖ ≤ δ / 2 := fun x hx => by
    simpa [X, Metric.mem_closedBall, dist_eq_norm] using hx
  have hYn : ∀ y ∈ Y, ‖y - y₀‖ ≤ 1 := fun y hy => by
    simpa [Y, Metric.mem_closedBall, dist_eq_norm] using hy
  have hYlow : ∀ y ∈ Y, ‖x₀‖ + 2 ≤ ‖y‖ := fun y hy => by
    have := norm_sub_norm_le y₀ y
    rw [← norm_neg (y₀ - y), neg_sub] at this
    linarith [hYn y hy]
  have hYup : ∀ y ∈ Y, ‖y‖ ≤ ‖x₀‖ + 4 := fun y hy => by
    have h2 : ‖y‖ ≤ ‖y₀‖ + ‖y - y₀‖ := by
      calc ‖y‖ = ‖y₀ + (y - y₀)‖ := by ring_nf
        _ ≤ _ := norm_add_le _ _
    linarith [hYn y hy]
  have hXup : ∀ x ∈ X, ‖x‖ ≤ ‖x₀‖ + 1 := fun x hx => by
    have h2 : ‖x‖ ≤ ‖x₀‖ + ‖x - x₀‖ := by
      calc ‖x‖ = ‖x₀ + (x - x₀)‖ := by ring_nf
        _ ≤ _ := norm_add_le _ _
    linarith [hXn x hx]
  have hX0 : ∀ x ∈ X, x ≠ 0 := by
    rintro x hx rfl
    have := hXn 0 hx
    rw [zero_sub, norm_neg] at this
    linarith
  have hX1 : ∀ x ∈ X, x ≠ 1 := by
    rintro x hx rfl
    have := hXn 1 hx
    rw [← norm_neg, neg_sub] at this
    linarith
  have hY0 : ∀ y ∈ Y, y ≠ 0 := by
    rintro y hy rfl
    have := hYlow 0 hy
    rw [norm_zero] at this
    linarith [norm_nonneg x₀]
  have hY1 : ∀ y ∈ Y, y ≠ 1 := by
    rintro y hy rfl
    have := hYlow 1 hy
    rw [norm_one] at this
    linarith [norm_nonneg x₀]
  have hXY : ∀ x ∈ X, ∀ y ∈ Y, x ≠ y := by
    rintro x hx y hy rfl
    linarith [hXup x hx, hYlow x hy]
  let f : ContDiffBump y₀ := ⟨1 / 2, 1, by norm_num, by norm_num⟩
  set ψ : ℂ → ℝ := f.normed volume
  have hψY : ∀ y ∉ Y, ψ y = 0 := by
    intro y hy
    have : y ∉ Function.support ψ := by
      rw [f.support_normed_eq]
      exact fun h => hy (Metric.ball_subset_closedBall h)
    simpa using this
  have core := contDiffOn_of_fiveTerm_core hφ hinv h5 (isCompact_closedBall x₀ (δ / 2))
    (isCompact_closedBall y₀ 1) Metric.isOpen_ball Metric.ball_subset_closedBall
    hX0 hX1 hY0 hY1 hXY f.contDiff_normed f.integral_normed hψY
    (by positivity : (0 : ℝ) < ‖x₀‖ + 4) hYup
  exact (core.contDiffAt (Metric.isOpen_ball.mem_nhds
    (Metric.mem_ball_self (half_pos hδpos)))).contDiffWithinAt

end QOU.Archimedean.BlochRigidity
