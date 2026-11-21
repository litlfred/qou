import Mathlib.Analysis.Calculus.FDeriv.Symmetric
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Complex.RealDeriv
import QOU.Archimedean.BlochRigidity.ComplexAlgebra

/-!
# Bloch–Suslin rigidity: analytic proposition D1 (chain rule)

For `φ : ℂ → ℝ` smooth on `{0,1}ᶜ` (Proposition R) write `dφ_z(w) = Re(ω(z) w)` and
`dω_z(w) = α(z) w + γ(z) w̄`. `γ` is real by symmetry of the second derivative
(`gamma_im`).

* `first_identity`: differentiating the five-term relation in `y` gives a complex identity
  in `ω` at the three non-trivial arguments.
* `mixed_identity`: differentiating that in `x` and keeping the antilinear part gives
  the three-term identity in `γ` that `mixed_eq_mul_im` (pure algebra) needs.
* `gamma_normSq_eq_mul_im`: hence `Re γ(z) · |z|² |1-z|² = k · Im z`.

The only analytic inputs are Mathlib's chain, product and quotient rules, uniqueness of the
derivative, and `ContDiffAt.isSymmSndFDerivAt`. All the algebra lives in `Algebra.lean` and
`ComplexAlgebra.lean`.
-/

open Complex

namespace QOU.Archimedean.BlochRigidity

/-- The complex form of the differential: `dφ_z(w) = Re(ω_φ(z) w)`. -/
noncomputable def omega (φ : ℂ → ℝ) (z : ℂ) : ℂ :=
  (fderiv ℝ φ z 1 : ℂ) - I * (fderiv ℝ φ z I : ℂ)

theorem fderiv_eq_re (φ : ℂ → ℝ) (z w : ℂ) : fderiv ℝ φ z w = (omega φ z * w).re :=
  rlinear_functional_eq_re (fderiv ℝ φ z).toLinearMap w

/-- Antilinear part of a real-linear map `ℂ → ℂ`, evaluated through `c` and `I c`. -/
theorem anti_eval (M : ℂ →ₗ[ℝ] ℂ) (c : ℂ) :
    M c + I * M (I * c) = (M 1 + I * M I) * (starRingEnd ℂ) c := by
  rw [rlinear_eq_add_conj M c, rlinear_eq_add_conj M (I * c)]
  simp only [map_mul, conj_I]
  have h3 : I ^ 3 = -I := by rw [pow_succ, I_sq]; ring
  ring_nf
  rw [h3]
  ring_nf
  rw [I_sq]
  ring

/-- Chain rule through a holomorphic map, real-valued outer function. -/
theorem hasFDerivAt_comp_holo {φ : ℂ → ℝ} {f : ℂ → ℂ} {f' y : ℂ}
    (hφ : DifferentiableAt ℝ φ (f y)) (hf : HasDerivAt f f' y) :
    HasFDerivAt (fun y => φ (f y))
      ((fderiv ℝ φ (f y)).comp
        ((ContinuousLinearMap.smulRight (1 : ℂ →L[ℂ] ℂ) f').restrictScalars ℝ)) y :=
  hφ.hasFDerivAt.comp y (hf.hasFDerivAt.restrictScalars ℝ)


/-- The punctured plane is open. -/
theorem isOpen_U : IsOpen ({0, 1}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl

theorem mem_U' {z : ℂ} : z ∈ ({0, 1}ᶜ : Set ℂ) ↔ z ≠ 0 ∧ z ≠ 1 := by simp

/-- The five arguments of the five-term relation stay in `{0,1}ᶜ`. -/
theorem args_ne {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1)
    (hxy : x ≠ y) :
    y / x ≠ 0 ∧ y / x ≠ 1 ∧ y / x * ((1 - x) / (1 - y)) ≠ 0 ∧
      y / x * ((1 - x) / (1 - y)) ≠ 1 ∧ (1 - x) / (1 - y) ≠ 0 ∧ (1 - x) / (1 - y) ≠ 1 := by
  have h1x : 1 - x ≠ 0 := sub_ne_zero.2 (Ne.symm hx1)
  have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  refine ⟨div_ne_zero hy0 hx0, ?_, mul_ne_zero (div_ne_zero hy0 hx0) (div_ne_zero h1x h1y),
    ?_, div_ne_zero h1x h1y, ?_⟩
  · intro h; rw [div_eq_one_iff_eq hx0] at h; exact hxy h.symm
  · intro h
    have : y * (1 - x) = x * (1 - y) := by
      field_simp at h; linear_combination h
    exact hxy (by linear_combination -this)
  · intro h; rw [div_eq_one_iff_eq h1y] at h; exact hxy (by linear_combination -h)

/-- The middle argument in the form used below. -/
theorem flip_eq {x y : ℂ} (hx0 : x ≠ 0) (hy0 : y ≠ 0) (hy1 : y ≠ 1) :
    (1 - x⁻¹) / (1 - y⁻¹) = y / x * ((1 - x) / (1 - y)) := by
  have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have h1y' : y - 1 ≠ 0 := sub_ne_zero.2 hy1
  field_simp
  ring

theorem differentiableAt_of_U {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) : DifferentiableAt ℝ φ z :=
  (hφ.differentiableOn (by simp)).differentiableAt (isOpen_U.mem_nhds (mem_U'.2 ⟨h0, h1⟩))

/-- **Proposition D1a (chain rule, first derivative in `y`).** -/
theorem first_identity {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1) (hxy : x ≠ y) :
    -omega φ y + omega φ (y / x) * (1 / x)
      - omega φ (y / x * ((1 - x) / (1 - y))) * ((1 - x) / (x * (1 - y) ^ 2))
      + omega φ ((1 - x) / (1 - y)) * ((1 - x) / (1 - y) ^ 2) = 0 := by
  have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  obtain ⟨a0, a1, b0, b1, c0, c1⟩ := args_ne hx0 hx1 hy0 hy1 hxy
  -- holomorphic derivatives in `y`
  have d1 : HasDerivAt (fun y => y / x) (1 / x) y := (hasDerivAt_id y).div_const x
  have d5 : HasDerivAt (fun y => (1 - x) / (1 - y)) ((1 - x) / (1 - y) ^ 2) y := by
    have := (hasDerivAt_const y (1 - x)).div ((hasDerivAt_const y (1 : ℂ)).sub (hasDerivAt_id y))
      h1y
    convert this using 1
    simp
  have d4 : HasDerivAt (fun y => y / x * ((1 - x) / (1 - y)))
      ((1 - x) / (x * (1 - y) ^ 2)) y := by
    convert d1.mul d5 using 1
    field_simp
    ring
  -- the five-term function of `y` vanishes near `y`
  set G : ℂ → ℝ := fun y' => φ x - φ y' + φ (y' / x) - φ (y' / x * ((1 - x) / (1 - y')))
    + φ ((1 - x) / (1 - y')) with hG
  have hev : G =ᶠ[nhds y] fun _ => (0 : ℝ) := by
    have hV : IsOpen ({0, 1, x}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl
    filter_upwards [hV.mem_nhds (by simp [hy0, hy1, Ne.symm hxy])] with y' hy'
    simp only [Set.mem_compl_iff, Set.mem_insert_iff, Set.mem_singleton_iff, not_or] at hy'
    obtain ⟨h0, h1, h2⟩ := hy'
    have := h5 x y' hx0 hx1 h0 h1 (Ne.symm h2)
    rw [flip_eq hx0 h0 h1] at this
    simpa [hG] using this
  have hL := (((((hasFDerivAt_const (φ x) y).sub
      (differentiableAt_of_U hφ hy0 hy1).hasFDerivAt).add
      (hasFDerivAt_comp_holo (differentiableAt_of_U hφ a0 a1) d1)).sub
      (hasFDerivAt_comp_holo (differentiableAt_of_U hφ b0 b1) d4)).add
      (hasFDerivAt_comp_holo (differentiableAt_of_U hφ c0 c1) d5))
  have h0 := hL.unique ((hasFDerivAt_const (0 : ℝ) y).congr_of_eventuallyEq hev)
  set E := -omega φ y + omega φ (y / x) * (1 / x)
      - omega φ (y / x * ((1 - x) / (1 - y))) * ((1 - x) / (x * (1 - y) ^ 2))
      + omega φ ((1 - x) / (1 - y)) * ((1 - x) / (1 - y) ^ 2) with hE
  have key : ∀ v : ℂ, (E * v).re = 0 := by
    intro v
    have := congrArg (fun L => L v) h0
    simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.sub_apply,
      ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_restrictScalars',
      ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.one_apply, smul_eq_mul,
      ContinuousLinearMap.zero_apply, fderiv_eq_re] at this
    rw [← this, hE]
    simp only [add_mul, sub_mul, neg_mul, add_re, sub_re, neg_re]
    ring_nf
  apply Complex.ext
  · simpa using key 1
  · simpa using key I

/-- The second-derivative coefficient: `dω_z(w) = α w + γ_φ(z) w̄`. -/
noncomputable def gamma (φ : ℂ → ℝ) (z : ℂ) : ℂ :=
  (fderiv ℝ (omega φ) z 1 + I * fderiv ℝ (omega φ) z I) / 2

theorem hasFDerivAt_fderiv_apply {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) (v : ℂ) :
    HasFDerivAt (fun z => fderiv ℝ φ z v) ((fderiv ℝ (fderiv ℝ φ) z).flip v) z := by
  have hD : ContDiffOn ℝ (⊤ : ℕ∞) (fderiv ℝ φ) {0, 1}ᶜ :=
    hφ.fderiv_of_isOpen isOpen_U (by simp)
  have hDz : DifferentiableAt ℝ (fderiv ℝ φ) z :=
    (hD.differentiableOn (by simp)).differentiableAt (isOpen_U.mem_nhds (mem_U'.2 ⟨h0, h1⟩))
  have := hDz.hasFDerivAt.clm_apply (hasFDerivAt_const v z)
  simpa using this

theorem hasFDerivAt_omega {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) :
    HasFDerivAt (omega φ)
      (ofRealCLM.comp ((fderiv ℝ (fderiv ℝ φ) z).flip 1)
        - I • ofRealCLM.comp ((fderiv ℝ (fderiv ℝ φ) z).flip I)) z := by
  have e1 := ofRealCLM.hasFDerivAt.comp z (hasFDerivAt_fderiv_apply hφ h0 h1 1)
  have e2 := (ofRealCLM.hasFDerivAt.comp z (hasFDerivAt_fderiv_apply hφ h0 h1 I)).const_mul I
  exact e1.sub e2

/-- **`γ` is real** (symmetry of the second derivative). -/
theorem gamma_im {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) : (gamma φ z).im = 0 := by
  have hs : IsSymmSndFDerivAt ℝ φ z :=
    (hφ.contDiffAt (isOpen_U.mem_nhds (mem_U'.2 ⟨h0, h1⟩))).isSymmSndFDerivAt
      (by simp; exact WithTop.coe_le_coe.2 (le_top : ((2 : ℕ∞)) ≤ ⊤))
  have := hs I 1
  rw [gamma, (hasFDerivAt_omega hφ h0 h1).fderiv]
  simp [this]

theorem differentiableAt_omega {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) : DifferentiableAt ℝ (omega φ) z :=
  (hasFDerivAt_omega hφ h0 h1).differentiableAt

/-- Derivative of `x ↦ ω(g x) · c x` and its antilinear part. -/
theorem anti_comp_mul {ω g c : ℂ → ℂ} {g' c' x : ℂ} (hω : DifferentiableAt ℝ ω (g x))
    (hg : HasDerivAt g g' x) (hc : HasDerivAt c c' x) :
    ∃ L : ℂ →L[ℝ] ℂ, HasFDerivAt (fun x => ω (g x) * c x) L x ∧
      L 1 + I * L I = c x * (fderiv ℝ ω (g x) 1 + I * fderiv ℝ ω (g x) I)
        * (starRingEnd ℂ) g' := by
  have h1 := hω.hasFDerivAt.comp x (hg.hasFDerivAt.restrictScalars ℝ)
  have h2 := hc.hasFDerivAt.restrictScalars ℝ
  refine ⟨_, h1.mul h2, ?_⟩
  have ha := anti_eval (fderiv ℝ ω (g x)).toLinearMap g'
  simp only [ContinuousLinearMap.coe_coe] at ha
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.smul_apply,
    ContinuousLinearMap.comp_apply, ContinuousLinearMap.coe_restrictScalars',
    ContinuousLinearMap.smulRight_apply, ContinuousLinearMap.one_apply, smul_eq_mul,
    Function.comp_apply, one_mul]
  have hI2 : I * (ω (g x) * (I * c')) = -(ω (g x) * c') := by
    ring_nf; rw [I_sq]; ring
  rw [show c x * fderiv ℝ ω (g x) (I * g') = c x * (fderiv ℝ ω (g x) (I * g')) from rfl]
  linear_combination c x * ha + hI2

/-- **Proposition D1 (chain rule, mixed derivative).** Differentiating `first_identity` in `x`
and keeping the antilinear part gives the three-term identity in `γ`. -/
theorem mixed_identity {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0)
    {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1) (hxy : x ≠ y) :
    gamma φ (y / x) * (starRingEnd ℂ) (-y / x ^ 2) * (1 / x)
      - gamma φ (y / x * ((1 - x) / (1 - y))) * (starRingEnd ℂ) (-y / (x ^ 2 * (1 - y)))
          * ((1 - x) / (x * (1 - y) ^ 2))
      + gamma φ ((1 - x) / (1 - y)) * (starRingEnd ℂ) (-1 / (1 - y))
          * ((1 - x) / (1 - y) ^ 2) = 0 := by
  have h1y : 1 - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have hxy2 : x * (1 - y) ^ 2 ≠ 0 := mul_ne_zero hx0 (pow_ne_zero 2 h1y)
  obtain ⟨a0, a1, b0, b1, c0, c1⟩ := args_ne hx0 hx1 hy0 hy1 hxy
  -- holomorphic derivatives in `x`
  have g1 : HasDerivAt (fun x => y / x) (-y / x ^ 2) x := by
    convert (hasDerivAt_const x y).div (hasDerivAt_id x) hx0 using 1
    simp
  have g5 : HasDerivAt (fun x => (1 - x) / (1 - y)) (-1 / (1 - y)) x := by
    convert ((hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_id x)).div_const (1 - y) using 1
    simp
  have g4 : HasDerivAt (fun x => y / x * ((1 - x) / (1 - y))) (-y / (x ^ 2 * (1 - y))) x := by
    convert g1.mul g5 using 1
    field_simp
    ring
  have k1 : HasDerivAt (fun x : ℂ => 1 / x) _ x := (hasDerivAt_const x (1 : ℂ)).div
    (hasDerivAt_id x) hx0
  have k4 : HasDerivAt (fun x : ℂ => (1 - x) / (x * (1 - y) ^ 2)) _ x :=
    ((hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_id x)).div
      ((hasDerivAt_id x).mul_const ((1 - y) ^ 2)) hxy2
  have k5 : HasDerivAt (fun x : ℂ => (1 - x) / (1 - y) ^ 2) _ x :=
    ((hasDerivAt_const x (1 : ℂ)).sub (hasDerivAt_id x)).div_const ((1 - y) ^ 2)
  obtain ⟨L1, hL1, e1⟩ := anti_comp_mul (g := fun x => y / x) (differentiableAt_omega hφ a0 a1) g1 k1
  obtain ⟨L4, hL4, e4⟩ := anti_comp_mul (g := fun x => y / x * ((1 - x) / (1 - y)))
    (differentiableAt_omega hφ b0 b1) g4 k4
  obtain ⟨L5, hL5, e5⟩ := anti_comp_mul (g := fun x => (1 - x) / (1 - y))
    (differentiableAt_omega hφ c0 c1) g5 k5
  have hH := (((hasFDerivAt_const (-omega φ y) x).add hL1).sub hL4).add hL5
  -- `first_identity` holds for all `x'` near `x`
  have hev : (fun x' => -omega φ y + omega φ (y / x') * (1 / x')
      - omega φ (y / x' * ((1 - x') / (1 - y))) * ((1 - x') / (x' * (1 - y) ^ 2))
      + omega φ ((1 - x') / (1 - y)) * ((1 - x') / (1 - y) ^ 2)) =ᶠ[nhds x]
      fun _ => (0 : ℂ) := by
    have hV : IsOpen ({0, 1, y}ᶜ : Set ℂ) := (Set.toFinite _).isClosed.isOpen_compl
    filter_upwards [hV.mem_nhds (by simp [hx0, hx1, hxy])] with x' hx'
    simp only [Set.mem_compl_iff, Set.mem_insert_iff, Set.mem_singleton_iff, not_or] at hx'
    obtain ⟨h0, h1, h2⟩ := hx'
    exact first_identity hφ h5 h0 h1 hy0 hy1 h2
  have h0 := hH.unique ((hasFDerivAt_const (0 : ℂ) x).congr_of_eventuallyEq hev)
  have hz : (0 + L1 - L4 + L5) 1 + I * (0 + L1 - L4 + L5) I = 0 := by
    rw [h0]; simp
  simp only [ContinuousLinearMap.add_apply, ContinuousLinearMap.sub_apply,
    zero_add] at hz
  have : (L1 1 + I * L1 I) - (L4 1 + I * L4 I) + (L5 1 + I * L5 I) = 0 := by
    linear_combination hz
  rw [e1, e4, e5] at this
  simp only [gamma]
  linear_combination this / 2

theorem gamma_eq_re {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ) {z : ℂ}
    (h0 : z ≠ 0) (h1 : z ≠ 1) : (((gamma φ z).re : ℝ) : ℂ) = gamma φ z :=
  Complex.ext (by simp) (by simp [gamma_im hφ h0 h1])

/-- **D1 + algebra.** For a smooth five-term solution, the real coefficient
`β = Re γ` (by construction `2γ = Δφ`, the Laplacian) satisfies `β(z)·|z|²·|1-z|² = k · Im z` on `ℂ ∖ {0,1}`. -/
theorem gamma_normSq_eq_mul_im {φ : ℂ → ℝ} (hφ : ContDiffOn ℝ (⊤ : ℕ∞) φ {0, 1}ᶜ)
    (h5 : ∀ x y : ℂ, x ≠ 0 → x ≠ 1 → y ≠ 0 → y ≠ 1 → x ≠ y →
      φ x - φ y + φ (y / x) - φ ((1 - x⁻¹) / (1 - y⁻¹)) + φ ((1 - x) / (1 - y)) = 0) :
    ∃ k : ℝ, ∀ z : ℂ, z ≠ 0 → z ≠ 1 →
      (gamma φ z).re * normSq z * normSq (1 - z) = k * z.im := by
  apply mixed_eq_mul_im
  intro x y hx0 hx1 hy0 hy1 hxy
  obtain ⟨a0, a1, b0, b1, c0, c1⟩ := args_ne hx0 hx1 hy0 hy1 hxy
  rw [gamma_eq_re hφ a0 a1, gamma_eq_re hφ b0 b1, gamma_eq_re hφ c0 c1]
  exact mixed_identity hφ h5 hx0 hx1 hy0 hy1 hxy

end QOU.Archimedean.BlochRigidity
