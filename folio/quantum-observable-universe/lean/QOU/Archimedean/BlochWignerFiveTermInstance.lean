import QOU.MathlibExt.ComplexRogersDilog
import QOU.Knot.KummerRadial
import Mathlib.Analysis.NormedSpace.Connected
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.LinearAlgebra.Complex.FiniteDimensional

import QOU.Archimedean.BlochSuslinComplex

/-!
# Bloch–Wigner satisfies the five-term relation

This file proves that the Bloch–Wigner function satisfies Suslin's five-term
relation on `ℂ \ {0,1}`, and so gives an instance of
`QOU.Archimedean.BlochWignerFiveTerm` (bean `qou-o41q`, issue #7942).

The function is `blochD`, defined on all of `ℂ`:

* off the cut `(1, ∞)` it is the Neumann–Zagier formula
  `D(z) = Im Li₂(z) + log|z| · arg(1 − z)`;
* on the cut it is `−D(1/z)`.

The two pieces agree with each other on a neighbourhood of every point other than
`0` and `1` (inversion `D(1/w) = −D(w)`, proved here from the corpus's Rogers
inversion), so `blochD` has real derivative `v ↦ Im(c(z)·v)` there, with
`c(z) = −log|z|/(1−z) − log|1−z|/z`.

## Proof

1. Differentiate the five-term sum in `x`, then in `y`. In each case the five
   coefficients of `Im(· v)` add to `0`. This is the identity
   `Σ ±fᵢ ∧ (1 − fᵢ) = 0` written out in logarithms (`gradX_zero`, `gradY_zero`).
2. `ℂ` minus finitely many points is open and path connected, because the real
   dimension is `2 > 1`. So a function with zero derivative there is constant.
3. `blochD` is `0` on the real line. So the sum is `0` when both arguments are
   real. Hold a real `y` and vary `x`; then hold `x` and vary `y`.

The upper-half-plane values agree with `BlochWigner_lob` (Kummer's identity,
`QOU.Knot.KummerRadial.kummer`). `BlochWigner_lob` itself is `0` in the lower half
plane (a degenerate-tetrahedron convention), so it is **not** odd under
conjugation and is **not** the function this instance is for.

The rigidity class `BlochSuslinRigidity` is instantiated for `blochD` in
`BlochRigidity/Instance.lean`.

-- Ref: [zagier1991] Zagier, "Polylogarithms, Dedekind zeta functions and the algebraic K-theory of fields" (1991), §2.
-- Ref: [suslin1991] Suslin, K_3 of a field, and the Bloch group, Trudy Mat. Inst. Steklova 183 (1991) 217-239.
-/

open Complex QOU.MathlibExt

namespace QOU.Archimedean.FiveTermProof

/-- Neumann–Zagier formula. -/
noncomputable def DNZ (z : ℂ) : ℝ := (cLiTwoExt z).im + Real.log ‖z‖ * Complex.arg (1 - z)

/-- the coefficient of the derivative -/
noncomputable def cD (z : ℂ) : ℂ :=
  -((Real.log ‖z‖ : ℝ) : ℂ) / (1 - z) - ((Real.log ‖1 - z‖ : ℝ) : ℂ) / z

noncomputable def DLin (z : ℂ) : ℂ →L[ℝ] ℝ :=
  Complex.imCLM.comp ((ContinuousLinearMap.mul ℝ ℂ) (cD z))

@[simp] theorem DLin_apply (z v : ℂ) : DLin z v = (cD z * v).im := rfl

theorem hasFDerivAt_im_of_hasDerivAt {g : ℂ → ℂ} {d z : ℂ} (h : HasDerivAt g d z) :
    HasFDerivAt (fun w => (g w).im)
      (Complex.imCLM.comp ((ContinuousLinearMap.mul ℝ ℂ) d)) z := by
  have h1 := (h.hasFDerivAt.restrictScalars ℝ)
  have := Complex.imCLM.hasFDerivAt.comp z h1
  convert this using 1
  ext v
  simp [mul_comm]

theorem hasFDerivAt_re_of_hasDerivAt {g : ℂ → ℂ} {d z : ℂ} (h : HasDerivAt g d z) :
    HasFDerivAt (fun w => (g w).re)
      (Complex.reCLM.comp ((ContinuousLinearMap.mul ℝ ℂ) d)) z := by
  have h1 := (h.hasFDerivAt.restrictScalars ℝ)
  have := Complex.reCLM.hasFDerivAt.comp z h1
  convert this using 1
  ext v
  simp [mul_comm]

/-- `log ‖z‖` has derivative `v ↦ Re (v / z)` off `0`. -/
theorem hasFDerivAt_log_norm {z : ℂ} (hz : z ≠ 0) :
    HasFDerivAt (fun w : ℂ => Real.log ‖w‖)
      (Complex.reCLM.comp ((ContinuousLinearMap.mul ℝ ℂ) z⁻¹)) z := by
  by_cases hs : z ∈ slitPlane
  · have h := hasFDerivAt_re_of_hasDerivAt (Complex.hasStrictDerivAt_log hs).hasDerivAt
    convert h using 1
    funext w; simp [Complex.log_re]
  · have hs' : -z ∈ slitPlane := by
      rw [Complex.mem_slitPlane_iff] at hs ⊢
      push_neg at hs
      rcases hs with ⟨h1, h2⟩
      left; simp
      rcases lt_or_eq_of_le h1 with h | h
      · linarith
      · exfalso; exact hz (Complex.ext (by simpa using h) (by simpa using h2))
    have hl := (Complex.hasStrictDerivAt_log hs').hasDerivAt
    have hneg : HasDerivAt (fun w : ℂ => Complex.log (-w)) ((-z)⁻¹ * -1) z :=
      hl.comp z (hasDerivAt_neg z)
    have h := hasFDerivAt_re_of_hasDerivAt hneg
    convert h using 1
    · funext w; simp [Complex.log_re]
    · ext v; simp [inv_neg]

theorem hasFDerivAt_DNZ {z : ℂ} (hz : z ∈ notCut) (hz0 : z ≠ 0) :
    HasFDerivAt DNZ (DLin z) z := by
  have hs : (1 : ℂ) - z ∈ slitPlane := one_sub_mem_slitPlane_iff.2 hz
  have hLi := hasFDerivAt_im_of_hasDerivAt (hasDerivAt_cLiTwoExt' hz hz0)
  have hlog1 : HasDerivAt (fun w : ℂ => Complex.log (1 - w)) ((1 - z)⁻¹ * (-1)) z :=
    (Complex.hasStrictDerivAt_log hs).hasDerivAt.comp z ((hasDerivAt_id z).const_sub 1)
  have harg := hasFDerivAt_im_of_hasDerivAt hlog1
  have hn := hasFDerivAt_log_norm hz0
  have hprod := hn.mul harg
  have hsum := hLi.add hprod
  have hfun : DNZ = fun w => (cLiTwoExt w).im + Real.log ‖w‖ * (Complex.log (1 - w)).im := by
    funext w; simp [DNZ, Complex.log_im]
  rw [hfun]
  convert hsum using 1
  ext v
  have h1z : (1 : ℂ) - z ≠ 0 := Complex.slitPlane_ne_zero hs
  have hlog : Complex.log (1 - z) = ((Real.log ‖1 - z‖ : ℝ) : ℂ) + ((Complex.arg (1 - z) : ℝ) : ℂ) * I := by
    apply Complex.ext <;> simp [Complex.log_re, Complex.log_im]
  simp only [DLin_apply, cD, ContinuousLinearMap.add_apply, ContinuousLinearMap.coe_comp',
    Function.comp_apply, ContinuousLinearMap.mul_apply', Complex.imCLM_apply, Complex.reCLM_apply,
    ContinuousLinearMap.coe_smul', Pi.smul_apply, smul_eq_mul, hlog]
  set a := Real.log ‖z‖
  set b := Real.log ‖1 - z‖
  set t := Complex.arg (1 - z)
  simp only [div_eq_mul_inv]
  simp only [Complex.mul_im, Complex.mul_re, Complex.add_im, Complex.add_re, Complex.neg_im,
    Complex.neg_re, Complex.sub_im, Complex.sub_re, Complex.ofReal_re, Complex.ofReal_im,
    Complex.I_re, Complex.I_im, Complex.one_re, Complex.one_im]
  ring

/-- `Im Li₂(t) = 0` for real `t ≤ 1`: the integrand is real. -/
theorem im_cLiTwoExt_ofReal {t : ℝ} (ht : t ≤ 1) : (cLiTwoExt (t : ℂ)).im = 0 := by
  unfold cLiTwoExt
  have hcongr : Set.EqOn (fun z : ℝ => Complex.log (1 - (t : ℂ) * (z : ℂ)) / (z : ℂ))
      (fun z : ℝ => ((Real.log (1 - t * z) / z : ℝ) : ℂ)) (Set.uIcc 0 1) := by
    intro z hz
    rw [Set.uIcc_of_le zero_le_one] at hz
    have hpos : 0 ≤ 1 - t * z := by
      rcases le_total 0 t with h | h
      · nlinarith [hz.1, hz.2]
      · nlinarith [hz.1, hz.2]
    simp only
    rw [show (1 : ℂ) - (t : ℂ) * (z : ℂ) = ((1 - t * z : ℝ) : ℂ) by push_cast; ring,
      ← Complex.ofReal_log hpos]
    push_cast; ring
  rw [intervalIntegral.integral_congr hcongr, intervalIntegral.integral_ofReal]
  simp

theorem DNZ_ofReal {t : ℝ} (ht : t ≤ 1) : DNZ (t : ℂ) = 0 := by
  unfold DNZ
  rw [im_cLiTwoExt_ofReal ht,
    show (1 : ℂ) - (t : ℂ) = ((1 - t : ℝ) : ℂ) by push_cast; ring,
    Complex.arg_ofReal_of_nonneg (by linarith)]
  ring

/-- **Inversion.** `D(1/w) = −D(w)` off the real axis. -/
theorem DNZ_inv {w : ℂ} (hw : w.im ≠ 0) : DNZ w⁻¹ = -DNZ w := by
  have hinv : w ∈ invDomain := mem_invDomain_of_im_ne_zero hw
  have hlog1 := log_one_sub_inv_add_log_neg hinv
  have hloginv := Complex.log_inv w (arg_ne_pi_of_im_ne_zero hw)
  have hre : ∀ x : ℂ, Real.log ‖x‖ = (Complex.log x).re := fun x => by simp [Complex.log_re]
  have him : ∀ x : ℂ, Complex.arg x = (Complex.log x).im := fun x => by simp [Complex.log_im]
  unfold DNZ
  rw [hre, hre, him, him]
  have e1 : Complex.log (1 - w⁻¹) = Complex.log (1 - w) - Complex.log (-w) := by
    rw [← hlog1]; ring
  rw [e1, hloginv]
  rcases lt_or_gt_of_ne hw with h | h
  · have hR := cRogersL_add_inv_of_im_neg h
    rw [clog_neg_of_im_neg h] at *
    unfold cRogersL at hR
    try rw [hloginv, e1] at hR
    have := congrArg Complex.im hR
    simp only [Complex.add_im, Complex.sub_im, Complex.mul_im, Complex.mul_re, Complex.div_ofNat_im,
      Complex.div_ofNat_re, Complex.neg_im, Complex.neg_re, Complex.add_re, Complex.sub_re,
      Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im] at this ⊢
    nlinarith [this]
  · have hR := cRogersL_add_inv_of_im_pos h
    rw [clog_neg_of_im_pos h] at *
    unfold cRogersL at hR
    try rw [hloginv, e1] at hR
    have := congrArg Complex.im hR
    simp only [Complex.add_im, Complex.sub_im, Complex.mul_im, Complex.mul_re, Complex.div_ofNat_im,
      Complex.div_ofNat_re, Complex.neg_im, Complex.neg_re, Complex.sub_re,
      Complex.ofReal_re, Complex.ofReal_im, Complex.I_re, Complex.I_im] at this ⊢
    nlinarith [this]

/-- **The Bloch–Wigner function on all of `ℂ`.**  The Neumann–Zagier formula off
the cut `(1, ∞)`, and `−D(1/z)` on it. -/
noncomputable def blochD (z : ℂ) : ℝ :=
  if z.im = 0 ∧ 1 < z.re then -DNZ z⁻¹ else DNZ z

/-- Chain rule against a holomorphic map, for anything with derivative `DLin`. -/
theorem hasFDerivAt_comp_of_hasDerivAt {F : ℂ → ℝ} {g : ℂ → ℂ} {d z : ℂ}
    (hF : HasFDerivAt F (DLin (g z)) (g z)) (hg : HasDerivAt g d z) :
    HasFDerivAt (fun w => F (g w))
      (Complex.imCLM.comp ((ContinuousLinearMap.mul ℝ ℂ) (cD (g z) * d))) z := by
  have h := hF.comp z (hg.hasFDerivAt.restrictScalars ℝ)
  convert h using 1
  ext v
  simp [DLin_apply, mul_assoc, mul_comm d v]

theorem log_norm_inv (z : ℂ) : Real.log ‖z⁻¹‖ = -Real.log ‖z‖ := by
  rw [norm_inv, Real.log_inv]

theorem cD_inv {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    cD z⁻¹ * (-(z ^ 2)⁻¹) = -cD z := by
  have h1z : (1 : ℂ) - z ≠ 0 := sub_ne_zero.2 (Ne.symm hz1)
  have e : (1 : ℂ) - z⁻¹ = -(1 - z) / z := by field_simp; ring
  have hn : Real.log ‖(1 : ℂ) - z⁻¹‖ = Real.log ‖1 - z‖ - Real.log ‖z‖ := by
    rw [e, norm_div, norm_neg, Real.log_div (norm_ne_zero_iff.2 h1z) (norm_ne_zero_iff.2 hz0)]
  have h1z' : (1 : ℂ) - z⁻¹ ≠ 0 := by rw [e]; exact div_ne_zero (neg_ne_zero.2 h1z) hz0
  unfold cD
  rw [log_norm_inv, hn]
  have hz1' : z - 1 ≠ 0 := sub_ne_zero.2 hz1
  have hz1'' : -1 + z ≠ 0 := by rw [add_comm, ← sub_eq_add_neg]; exact hz1'
  push_cast
  field_simp
  ring

theorem hasFDerivAt_blochD {z : ℂ} (hz0 : z ≠ 0) (hz1 : z ≠ 1) :
    HasFDerivAt blochD (DLin z) z := by
  by_cases hc : z ∈ notCut
  · have hev : blochD =ᶠ[nhds z] DNZ := by
      filter_upwards [isOpen_notCut.mem_nhds hc] with w hw
      have : ¬ (w.im = 0 ∧ 1 < w.re) := by
        rintro ⟨h1, h2⟩
        rcases hw with h | h
        · exact h h1
        · linarith
      simp [blochD, this]
    exact (hasFDerivAt_DNZ hc hz0).congr_of_eventuallyEq hev
  · have him : z.im = 0 := by
      by_contra h; exact hc (Or.inl h)
    have hre1 : 1 ≤ z.re := by
      by_contra h; exact hc (Or.inr (lt_of_not_ge h))
    have hre : 1 < z.re := by
      rcases lt_or_eq_of_le hre1 with h | h
      · exact h
      · exfalso; apply hz1; apply Complex.ext <;> simp [him, ← h]
    have hev : blochD =ᶠ[nhds z] fun w => -DNZ w⁻¹ := by
      have hopen : IsOpen {w : ℂ | 1 < w.re} := isOpen_lt continuous_const Complex.continuous_re
      filter_upwards [hopen.mem_nhds hre] with w hw
      by_cases hwi : w.im = 0
      · simp [blochD, hwi, show 1 < w.re from hw]
      · have hnot : ¬ (w.im = 0 ∧ 1 < w.re) := fun h => hwi h.1
        simp only [blochD, hnot, if_false]
        rw [DNZ_inv hwi]; ring
    have hinvc : z⁻¹ ∈ notCut := by
      right
      rw [Complex.inv_re]
      have hns : Complex.normSq z = z.re ^ 2 := by simp [Complex.normSq_apply, him]; ring
      rw [hns, div_lt_one (by positivity)]
      nlinarith
    have hD := hasFDerivAt_DNZ hinvc (inv_ne_zero hz0)
    have hcomp := hasFDerivAt_comp_of_hasDerivAt (g := fun w : ℂ => w⁻¹) hD (hasDerivAt_inv hz0)
    have hneg := hcomp.neg
    refine HasFDerivAt.congr_of_eventuallyEq ?_ hev
    convert hneg using 1
    ext v
    simp only [DLin_apply, ContinuousLinearMap.neg_apply, ContinuousLinearMap.coe_comp',
      Function.comp_apply, ContinuousLinearMap.mul_apply', Complex.imCLM_apply]
    rw [cD_inv hz0 hz1]
    simp

/-! ### The five-term sum and its derivative -/

/-- Suslin's five-term combination. -/
noncomputable def fiveSum (x y : ℂ) : ℝ :=
  blochD x - blochD y + blochD (y / x) - blochD ((1 - x⁻¹) / (1 - y⁻¹))
    + blochD ((1 - x) / (1 - y))

theorem cD_eq {f g : ℂ} (hg : 1 - f = g) {a b : ℝ} (ha : Real.log ‖f‖ = a)
    (hb : Real.log ‖g‖ = b) : cD f = -(a : ℂ) / g - (b : ℂ) / f := by
  unfold cD; rw [hg, ha, hb]

theorem log_norm_mul {a b : ℂ} (ha : a ≠ 0) (hb : b ≠ 0) :
    Real.log ‖a * b‖ = Real.log ‖a‖ + Real.log ‖b‖ := by
  rw [norm_mul, Real.log_mul (norm_ne_zero_iff.2 ha) (norm_ne_zero_iff.2 hb)]

theorem log_norm_div {a b : ℂ} (ha : a ≠ 0) (hb : b ≠ 0) :
    Real.log ‖a / b‖ = Real.log ‖a‖ - Real.log ‖b‖ := by
  rw [norm_div, Real.log_div (norm_ne_zero_iff.2 ha) (norm_ne_zero_iff.2 hb)]

section Args
variable {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1) (hxy : x ≠ y)
include hx0 hx1 hy0 hy1 hxy

set_option linter.unusedSectionVars false in
theorem f4_eq : (1 - x⁻¹) / (1 - y⁻¹) = (1 - x) * y / ((1 - y) * x) := by
  have : (1 : ℂ) - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have : y - 1 ≠ 0 := sub_ne_zero.2 hy1
  field_simp; ring

set_option linter.unusedSectionVars false in
theorem one_sub_f4 : 1 - (1 - x) * y / ((1 - y) * x) = (x - y) / ((1 - y) * x) := by
  have : (1 : ℂ) - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  field_simp; ring

/-- The `x`-gradient coefficient of the five-term sum vanishes. -/
theorem gradX_zero :
    cD x * 1 + cD (y / x) * (y * -(x ^ 2)⁻¹)
      - cD ((1 - x) * y / ((1 - y) * x)) * (-(-(x ^ 2)⁻¹) / (1 - y⁻¹))
      + cD ((1 - x) / (1 - y)) * (-1 / (1 - y)) = 0 := by
  have hA : (1 : ℂ) - x ≠ 0 := sub_ne_zero.2 (Ne.symm hx1)
  have hB : (1 : ℂ) - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have hZ : x - y ≠ 0 := sub_ne_zero.2 hxy
  have hB' : y - 1 ≠ 0 := sub_ne_zero.2 hy1
  have hA' : x - 1 ≠ 0 := sub_ne_zero.2 hx1
  set LX := Real.log ‖x‖
  set LA := Real.log ‖1 - x‖
  set LY := Real.log ‖y‖
  set LB := Real.log ‖1 - y‖
  set LZ := Real.log ‖x - y‖
  rw [cD_eq (g := 1 - x) rfl rfl rfl,
    cD_eq (f := y / x) (g := (x - y) / x) (by field_simp) (log_norm_div hy0 hx0)
      (log_norm_div hZ hx0),
    cD_eq (g := (x - y) / ((1 - y) * x)) (one_sub_f4 hx0 hx1 hy0 hy1 hxy)
      (by rw [log_norm_div (mul_ne_zero hA hy0) (mul_ne_zero hB hx0), log_norm_mul hA hy0,
        log_norm_mul hB hx0])
      (by rw [log_norm_div hZ (mul_ne_zero hB hx0), log_norm_mul hB hx0]),
    cD_eq (g := (x - y) / (1 - y)) (by field_simp; ring) (log_norm_div hA hB)
      (log_norm_div hZ hB)]
  push_cast
  field_simp
  ring

/-- The `y`-gradient coefficient of the five-term sum vanishes. -/
theorem gradY_zero :
    -(cD y * 1) + cD (y / x) * (1 / x)
      - cD ((1 - x) * y / ((1 - y) * x)) * ((1 - x⁻¹) * (-((1 - y⁻¹) ^ 2)⁻¹ * (y ^ 2)⁻¹))
      + cD ((1 - x) / (1 - y)) * ((1 - x) * ((1 - y) ^ 2)⁻¹) = 0 := by
  have hA : (1 : ℂ) - x ≠ 0 := sub_ne_zero.2 (Ne.symm hx1)
  have hB : (1 : ℂ) - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have hZ : x - y ≠ 0 := sub_ne_zero.2 hxy
  have hB' : y - 1 ≠ 0 := sub_ne_zero.2 hy1
  have hA' : x - 1 ≠ 0 := sub_ne_zero.2 hx1
  set LX := Real.log ‖x‖
  set LA := Real.log ‖1 - x‖
  set LY := Real.log ‖y‖
  set LB := Real.log ‖1 - y‖
  set LZ := Real.log ‖x - y‖
  rw [cD_eq (g := 1 - y) rfl rfl rfl,
    cD_eq (f := y / x) (g := (x - y) / x) (by field_simp) (log_norm_div hy0 hx0)
      (log_norm_div hZ hx0),
    cD_eq (g := (x - y) / ((1 - y) * x)) (one_sub_f4 hx0 hx1 hy0 hy1 hxy)
      (by rw [log_norm_div (mul_ne_zero hA hy0) (mul_ne_zero hB hx0), log_norm_mul hA hy0,
        log_norm_mul hB hx0])
      (by rw [log_norm_div hZ (mul_ne_zero hB hx0), log_norm_mul hB hx0]),
    cD_eq (g := (x - y) / (1 - y)) (by field_simp; ring) (log_norm_div hA hB)
      (log_norm_div hZ hB)]
  push_cast
  field_simp
  ring

end Args

end QOU.Archimedean.FiveTermProof

namespace QOU.Archimedean.FiveTermProof

theorem im_comb {a b c e : ℂ} (h : a + b - c + e = 0) (v : ℂ) :
    (a * v).im - 0 + (b * v).im - (c * v).im + (e * v).im = 0 := by
  have h2 := congrArg (fun K => (K * v).im) h
  simp only [add_mul, sub_mul, Complex.add_im, Complex.sub_im, zero_mul, Complex.zero_im] at h2
  linarith

theorem im_comb2 {a b c e : ℂ} (h : -a + b - c + e = 0) (v : ℂ) :
    0 - (a * v).im + (b * v).im - (c * v).im + (e * v).im = 0 := by
  have h2 := congrArg (fun K => (K * v).im) h
  simp only [add_mul, sub_mul, neg_mul, Complex.add_im, Complex.sub_im, Complex.neg_im, zero_mul,
    Complex.zero_im] at h2
  linarith

section Deriv
variable {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1) (hxy : x ≠ y)
include hx0 hx1 hy0 hy1 hxy

theorem args_ok :
    (y / x ≠ 0 ∧ y / x ≠ 1) ∧
    ((1 - x⁻¹) / (1 - y⁻¹) ≠ 0 ∧ (1 - x⁻¹) / (1 - y⁻¹) ≠ 1) ∧
    ((1 - x) / (1 - y) ≠ 0 ∧ (1 - x) / (1 - y) ≠ 1) := by
  have hA : (1 : ℂ) - x ≠ 0 := sub_ne_zero.2 (Ne.symm hx1)
  have hB : (1 : ℂ) - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have hZ : x - y ≠ 0 := sub_ne_zero.2 hxy
  refine ⟨⟨div_ne_zero hy0 hx0, ?_⟩, ⟨?_, ?_⟩, ⟨div_ne_zero hA hB, ?_⟩⟩
  · intro h; rw [div_eq_one_iff_eq hx0] at h; exact hxy h.symm
  · rw [f4_eq hx0 hx1 hy0 hy1 hxy]; exact div_ne_zero (mul_ne_zero hA hy0) (mul_ne_zero hB hx0)
  · intro h
    have h2 := one_sub_f4 hx0 hx1 hy0 hy1 hxy
    rw [← f4_eq hx0 hx1 hy0 hy1 hxy, h, sub_self] at h2
    exact div_ne_zero hZ (mul_ne_zero hB hx0) h2.symm
  · intro h; rw [div_eq_one_iff_eq hB] at h; exact hxy (by linear_combination -h)

theorem hasFDerivAt_fiveSum_fst : HasFDerivAt (fun w => fiveSum w y) (0 : ℂ →L[ℝ] ℝ) x := by
  obtain ⟨⟨h30, h31⟩, ⟨h40, h41⟩, ⟨h50, h51⟩⟩ := args_ok hx0 hx1 hy0 hy1 hxy
  have hB : (1 : ℂ) - y⁻¹ ≠ 0 := by
    intro h; apply hy1; have := sub_eq_zero.1 h; exact (inv_eq_one.1 this.symm)
  have d1 := hasFDerivAt_blochD hx0 hx1
  have d3 := hasFDerivAt_comp_of_hasDerivAt (g := fun w => y * w⁻¹)
    (by simpa [div_eq_mul_inv] using hasFDerivAt_blochD h30 h31)
    ((hasDerivAt_inv hx0).const_mul y)
  have d4 := hasFDerivAt_comp_of_hasDerivAt (g := fun w => (1 - w⁻¹) / (1 - y⁻¹))
    (hasFDerivAt_blochD h40 h41) (((hasDerivAt_inv hx0).const_sub 1).div_const (1 - y⁻¹))
  have d5 := hasFDerivAt_comp_of_hasDerivAt (g := fun w => (1 - w) / (1 - y))
    (hasFDerivAt_blochD h50 h51) (((hasDerivAt_id' x).const_sub 1).div_const (1 - y))
  have h := (((d1.sub (hasFDerivAt_const (blochD y) x)).add d3).sub d4).add d5
  convert h using 1
  · ext v
    have g := gradX_zero hx0 hx1 hy0 hy1 hxy
    rw [← f4_eq hx0 hx1 hy0 hy1 hxy] at g
    simp only [ContinuousLinearMap.zero_apply, ContinuousLinearMap.add_apply,
      ContinuousLinearMap.sub_apply, DLin_apply, ContinuousLinearMap.coe_comp',
      Function.comp_apply, ContinuousLinearMap.mul_apply', Complex.imCLM_apply]
    have := im_comb g v
    simp only [mul_one, div_eq_mul_inv] at this ⊢
    linarith [this]

theorem hasFDerivAt_fiveSum_snd : HasFDerivAt (fun w => fiveSum x w) (0 : ℂ →L[ℝ] ℝ) y := by
  obtain ⟨⟨h30, h31⟩, ⟨h40, h41⟩, ⟨h50, h51⟩⟩ := args_ok hx0 hx1 hy0 hy1 hxy
  have hB : (1 : ℂ) - y⁻¹ ≠ 0 := by
    intro h; apply hy1; have := sub_eq_zero.1 h; exact (inv_eq_one.1 this.symm)
  have hB1 : (1 : ℂ) - y ≠ 0 := sub_ne_zero.2 (Ne.symm hy1)
  have d2 := hasFDerivAt_blochD hy0 hy1
  have d3 := hasFDerivAt_comp_of_hasDerivAt (g := fun w => w / x)
    (hasFDerivAt_blochD h30 h31) ((hasDerivAt_id' y).div_const x)
  have d4 := hasFDerivAt_comp_of_hasDerivAt (g := fun w => (1 - x⁻¹) * (1 - w⁻¹)⁻¹)
    (by simpa [div_eq_mul_inv] using hasFDerivAt_blochD h40 h41)
    ((((hasDerivAt_inv hy0).const_sub 1).inv hB).const_mul (1 - x⁻¹))
  have d5 := hasFDerivAt_comp_of_hasDerivAt (g := fun w => (1 - x) * (1 - w)⁻¹)
    (by simpa [div_eq_mul_inv] using hasFDerivAt_blochD h50 h51)
    ((((hasDerivAt_id' y).const_sub 1).inv hB1).const_mul (1 - x))
  have h := ((((hasFDerivAt_const (blochD x) y).sub d2).add d3).sub d4).add d5
  convert h using 1
  ext v
  have g := gradY_zero hx0 hx1 hy0 hy1 hxy
  simp only [ContinuousLinearMap.zero_apply, ContinuousLinearMap.add_apply,
    ContinuousLinearMap.sub_apply, DLin_apply, ContinuousLinearMap.coe_comp',
    Function.comp_apply, ContinuousLinearMap.mul_apply', Complex.imCLM_apply]
  rw [← div_eq_mul_inv (1 - x⁻¹), f4_eq hx0 hx1 hy0 hy1 hxy, ← div_eq_mul_inv (1 - x)]
  have e4 : (1 - x⁻¹) * (- - -(y ^ 2)⁻¹ / (1 - y⁻¹) ^ 2)
      = (1 - x⁻¹) * (-((1 - y⁻¹) ^ 2)⁻¹ * (y ^ 2)⁻¹) := by ring
  have e5 : (1 - x) * (- -1 / (1 - y) ^ 2) = (1 - x) * ((1 - y) ^ 2)⁻¹ := by ring
  rw [e4, e5]
  rw [mul_one] at g
  have h2 := im_comb2 g v
  linarith

end Deriv
end QOU.Archimedean.FiveTermProof

namespace QOU.Archimedean.FiveTermProof

theorem blochD_ofReal (r : ℝ) : blochD (r : ℂ) = 0 := by
  unfold blochD
  by_cases h : (1 : ℝ) < r
  · rw [if_pos ⟨by simp, by simpa using h⟩,
      show (r : ℂ)⁻¹ = ((r⁻¹ : ℝ) : ℂ) by push_cast; rfl,
      DNZ_ofReal (inv_le_one_of_one_le₀ h.le)]
    simp
  · rw [if_neg (fun h' => h (by simpa using h'.2)), DNZ_ofReal (not_lt.1 h)]

theorem fiveSum_ofReal (a b : ℝ) : fiveSum (a : ℂ) (b : ℂ) = 0 := by
  unfold fiveSum
  rw [show (b : ℂ) / (a : ℂ) = ((b / a : ℝ) : ℂ) by push_cast; rfl,
    show (1 - (a : ℂ)⁻¹) / (1 - (b : ℂ)⁻¹) = (((1 - a⁻¹) / (1 - b⁻¹) : ℝ) : ℂ) by push_cast; rfl,
    show (1 - (a : ℂ)) / (1 - (b : ℂ)) = (((1 - a) / (1 - b) : ℝ) : ℂ) by push_cast; rfl]
  simp only [blochD_ofReal]
  ring

theorem one_lt_rank_complex : 1 < Module.rank ℝ ℂ := by
  rw [Complex.rank_real_complex]; norm_num

/-- Step A: the five-term sum vanishes when the second argument is real. -/
theorem fiveSum_ofReal_snd {x : ℂ} {b : ℝ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hb0 : b ≠ 0)
    (hb1 : b ≠ 1) (hxb : x ≠ (b : ℂ)) : fiveSum x b = 0 := by
  set S : Set ℂ := ({0, 1, (b : ℂ)} : Set ℂ)ᶜ with hS
  have hfin : ({0, 1, (b : ℂ)} : Set ℂ).Finite := by simp
  have hpc : IsPathConnected S := hfin.countable.isPathConnected_compl_of_one_lt_rank
    one_lt_rank_complex
  have hopen : IsOpen S := hfin.isClosed.isOpen_compl
  have hmem : ∀ w, w ∈ S ↔ w ≠ 0 ∧ w ≠ 1 ∧ w ≠ (b : ℂ) := by intro w; simp [S]
  have hb0' : (b : ℂ) ≠ 0 := by exact_mod_cast hb0
  have hb1' : (b : ℂ) ≠ 1 := by exact_mod_cast hb1
  have hd : ∀ w ∈ S, HasFDerivAt (fun w => fiveSum w b) (0 : ℂ →L[ℝ] ℝ) w := by
    intro w hw
    obtain ⟨h0, h1, h2⟩ := (hmem w).1 hw
    exact hasFDerivAt_fiveSum_fst h0 h1 hb0' hb1' h2
  set x0 : ℝ := |b| + 2 with hx0def
  have hx0S : (x0 : ℂ) ∈ S := by
    rw [hmem]
    refine ⟨fun h => ?_, fun h => ?_, fun h => ?_⟩
    · have : x0 = 0 := by exact_mod_cast h
      linarith [abs_nonneg b]
    · have : x0 = 1 := by exact_mod_cast h
      linarith [abs_nonneg b]
    · have : x0 = b := by exact_mod_cast h
      linarith [le_abs_self b]
  have hc := hopen.is_const_of_fderiv_eq_zero (𝕜 := ℝ) hpc.isConnected.isPreconnected
    (fun w hw => (hd w hw).differentiableAt.differentiableWithinAt)
    (fun w hw => (hd w hw).fderiv) ((hmem x).2 ⟨hx0, hx1, hxb⟩) hx0S
  rw [hc, fiveSum_ofReal]

/-- **The five-term relation for Bloch–Wigner.** -/
theorem fiveSum_eq_zero {x y : ℂ} (hx0 : x ≠ 0) (hx1 : x ≠ 1) (hy0 : y ≠ 0) (hy1 : y ≠ 1)
    (hxy : x ≠ y) : fiveSum x y = 0 := by
  set S : Set ℂ := ({0, 1, x} : Set ℂ)ᶜ with hS
  have hfin : ({0, 1, x} : Set ℂ).Finite := by simp
  have hpc : IsPathConnected S := hfin.countable.isPathConnected_compl_of_one_lt_rank
    one_lt_rank_complex
  have hopen : IsOpen S := hfin.isClosed.isOpen_compl
  have hmem : ∀ w, w ∈ S ↔ w ≠ 0 ∧ w ≠ 1 ∧ w ≠ x := by intro w; simp [S]
  have hd : ∀ w ∈ S, HasFDerivAt (fun w => fiveSum x w) (0 : ℂ →L[ℝ] ℝ) w := by
    intro w hw
    obtain ⟨h0, h1, h2⟩ := (hmem w).1 hw
    exact hasFDerivAt_fiveSum_snd hx0 hx1 h0 h1 (Ne.symm h2)
  set y0 : ℝ := ‖x‖ + 2 with hy0def
  have hy00 : y0 ≠ 0 := by intro h; linarith [norm_nonneg x]
  have hy01 : y0 ≠ 1 := by intro h; linarith [norm_nonneg x]
  have hxy0 : x ≠ (y0 : ℂ) := by
    intro h
    have := congrArg (fun z : ℂ => ‖z‖) h
    simp only [Complex.norm_real, Real.norm_eq_abs, abs_of_nonneg (by positivity : (0:ℝ) ≤ y0)]
      at this
    linarith
  have hy0S : (y0 : ℂ) ∈ S := by
    rw [hmem]
    exact ⟨by exact_mod_cast hy00, by exact_mod_cast hy01, Ne.symm hxy0⟩
  have hc := hopen.is_const_of_fderiv_eq_zero (𝕜 := ℝ) hpc.isConnected.isPreconnected
    (fun w hw => (hd w hw).differentiableAt.differentiableWithinAt)
    (fun w hw => (hd w hw).fderiv) ((hmem y).2 ⟨hy0, hy1, Ne.symm hxy⟩) hy0S
  rw [hc, fiveSum_ofReal_snd hx0 hx1 hy00 hy01 hxy0]

end QOU.Archimedean.FiveTermProof


namespace QOU.Archimedean.FiveTermProof

/-- On the upper half plane `blochD` is the corpus's `BlochWigner_lob`. -/
theorem blochD_eq_lob {z : ℂ} (hz : 0 < z.im) : blochD z = BlochWigner_lob z := by
  have hnot : ¬ (z.im = 0 ∧ 1 < z.re) := fun h => (ne_of_gt hz) h.1
  rw [QOU.Knot.KummerRadial.kummer hz]
  simp only [blochD, hnot, if_false, DNZ]

end QOU.Archimedean.FiveTermProof

namespace QOU.Archimedean

/-- **Bloch–Wigner satisfies Suslin's five-term relation** — a proved instance
of `BlochWignerFiveTerm`, for the Bloch–Wigner function `blochD` on all of `ℂ`. -/
instance blochWignerFiveTerm_blochD : BlochWignerFiveTerm FiveTermProof.blochD :=
  ⟨fun _ _ hx0 hx1 hy0 hy1 hxy => FiveTermProof.fiveSum_eq_zero hx0 hx1 hy0 hy1 hxy⟩

end QOU.Archimedean
