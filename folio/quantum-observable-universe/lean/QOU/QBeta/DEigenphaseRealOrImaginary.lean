/-
# Is the convention-D N=1 eigenphase real or imaginary?

Beans `qou-cds1` (the `c_k` ladder under convention D) and `qou-pdix` (the N=1
phase). Diagnostic companion:
`computations/qbeta/qbeta_d_eigenphase_real_or_imaginary_probe.py`.

## Why the question is live

On the owner-ruled base (`ε := tr_M` at `z_D = q³/(q²+1)`), the required
correction factor exceeds 1 in every scored cell. The ladder's N=1 factor is
`cos(α − u/2)`, which is `≤ 1` for every real `α`. So the one ladder-side lever
above 1 is an imaginary phase `α = i a`, where `cos(i a) = cosh a ≥ 1`
(`HolonomySpectrumSignObstruction.lean` proves the `cosh ≥ 1` half).

## What this file proves (all algebraic; no analysis beyond `cos`, `cosh`)

1. **Classification of a 2×2 block** (`factor_gt_one_imp_real_pos_spectrum`,
   `real_phase_of_disc_nonpos`, `imaginary_phase_of_factor_ge_one`). With
   trace `T`, determinant `D = s² > 0`, the N=1 factor `t = T/(2s)` is a real
   cosine iff `T² ≤ 4D` (complex-conjugate spectrum), and it exceeds 1 only if
   `T > 0` and `T² > 4D` (real positive spectrum), in which case `t = cosh a`
   for a real `a`, i.e. the eigenphase is `i a`.
2. **Bar-odd phases change type between the two real slices**
   (`bar_odd_real_coeff_real_on_axis`, `bar_odd_real_coeff_im_on_circle`,
   `cos_bar_odd_on_circle_is_cosh`). A phase `f` with real coefficients
   (`f (conj w) = conj (f w)`) that is bar-odd (`f w⁻¹ = −f w`) is real on the
   real axis and purely imaginary on `‖w‖ = 1`. So `cos ∘ f` is `≤ 1` on the
   real axis and is a `cosh` (`≥ 1`) on the unit circle.
3. **The D ladder phase is real at the substrate** (`alphaD_neg`,
   `alphaD_eq_zero_iff`, `alphaD_bar_sum`, `betaD_bar_odd`,
   `cube_lt_of_lt_six_fifths`). `α_D = (z_D − 1)·h/2` is a real rational
   function of `q`; for `1 < q` with `q³ < q² + 1` (true for `q < 6/5`, hence
   at `q₀ ≈ 1.10998`) it is strictly negative. It vanishes exactly at
   `q³ = q² + 1`. Its bar defect is `α_D(q) + α_D(q⁻¹) = h²/2`, so its bar-odd
   part `β_D = α_D − h²/4` is exactly bar-odd.

## What it does NOT say

It does not prove that no imaginary phase can be derived. It shows which
readings the corpus carries and what each gives: at real `q`, every phase built
from `q` by real rational operations is real, so the factor is a `cos`. An
imaginary phase needs either `q` off the real axis (item 2: the bar-odd part
turns imaginary on the unit circle) or a block with real positive spectrum
(item 1). The probe measures both for the scored elements. Scope (b) only for
"real phase ⇒ factor ≤ 1" (`Real.cos_le_one`) and for item 2; scope (a) for
everything numeric.
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Order.IntermediateValue
import Mathlib.Tactic.Positivity

namespace QOU.QBeta.DEigenphase

open Complex

/-! ## 1. The eigenphase of a 2×2 block -/

/-- A real eigenphase gives an N=1 factor at most 1. -/
theorem real_phase_factor_le_one (φ : ℝ) : Real.cos φ ≤ 1 :=
  Real.cos_le_one φ

/-- An imaginary eigenphase `φ = a·i` gives the factor `cosh a`. -/
theorem imaginary_phase_is_cosh (a : ℝ) :
    Complex.cos ((a : ℂ) * I) = ((Real.cosh a : ℝ) : ℂ) := by
  rw [Complex.cos_mul_I, Complex.ofReal_cosh]

/-- If the half-normalised trace `T/(2s)` of a block with `det = s² > 0`
exceeds 1, the spectrum is real and positive: `T > 0` and `T² > 4·det`. -/
theorem factor_gt_one_imp_real_pos_spectrum {T s : ℝ} (hs : 0 < s)
    (ht : 1 < T / (2 * s)) : 0 < T ∧ 4 * s ^ 2 < T ^ 2 := by
  have h2s : 0 < 2 * s := by linarith
  have hT : 2 * s < T := by
    have := (lt_div_iff₀ h2s).mp ht
    linarith
  refine ⟨by linarith, ?_⟩
  nlinarith

/-- If the discriminant is non-positive (`T² ≤ 4s²`), the half-normalised trace
is a real cosine: the eigenphase is real. -/
theorem real_phase_of_disc_nonpos {T s : ℝ} (hs : 0 < s)
    (hdisc : T ^ 2 ≤ 4 * s ^ 2) : ∃ φ : ℝ, Real.cos φ = T / (2 * s) := by
  have h2s : 0 < 2 * s := by linarith
  have hsq : T ^ 2 ≤ (2 * s) ^ 2 := by nlinarith
  obtain ⟨hlo, hhi⟩ := abs_le_of_sq_le_sq' hsq h2s.le
  have h1 : -1 ≤ T / (2 * s) := by
    rw [le_div_iff₀ h2s]; linarith
  have h2 : T / (2 * s) ≤ 1 := by
    rw [div_le_iff₀ h2s]; linarith
  exact ⟨Real.arccos (T / (2 * s)), Real.cos_arccos h1 h2⟩

/-- `cosh (log (2t)) ≥ t` for `t ≥ 1` — the upper end for the intermediate
value step below. -/
theorem le_cosh_log_two_mul {t : ℝ} (ht : 1 ≤ t) : t ≤ Real.cosh (Real.log (2 * t)) := by
  have h2t : 0 < 2 * t := by linarith
  rw [Real.cosh_eq, Real.exp_neg, Real.exp_log h2t]
  have : 0 < (2 * t)⁻¹ := inv_pos.mpr h2t
  linarith

/-- A factor `t ≥ 1` is `cosh a` for a real `a ≥ 0`: the eigenphase is `i a`. -/
theorem imaginary_phase_of_factor_ge_one {t : ℝ} (ht : 1 ≤ t) :
    ∃ a : ℝ, 0 ≤ a ∧ Real.cosh a = t := by
  have hlog : 0 ≤ Real.log (2 * t) := Real.log_nonneg (by linarith)
  have hmem : t ∈ Set.Icc (Real.cosh 0) (Real.cosh (Real.log (2 * t))) :=
    ⟨by rw [Real.cosh_zero]; exact ht, le_cosh_log_two_mul ht⟩
  obtain ⟨a, ⟨ha0, _⟩, ha⟩ :=
    intermediate_value_Icc hlog Real.continuous_cosh.continuousOn hmem
  exact ⟨a, ha0, ha⟩

/-! ## 2. Bar-odd phases: real on the real axis, imaginary on the unit circle -/

/-- A phase with real coefficients is real on the real axis. -/
theorem bar_odd_real_coeff_real_on_axis (f : ℂ → ℂ)
    (hreal : ∀ w, f (starRingEnd ℂ w) = starRingEnd ℂ (f w)) (x : ℝ) :
    (f x).im = 0 := by
  have h := hreal (x : ℂ)
  rw [Complex.conj_ofReal] at h
  have him := congrArg Complex.im h
  rw [Complex.conj_im] at him
  linarith

/-- On the unit circle `conj w = w⁻¹`. -/
theorem conj_eq_inv_of_norm_one {w : ℂ} (hw : ‖w‖ = 1) : starRingEnd ℂ w = w⁻¹ := by
  rw [Complex.inv_def, Complex.normSq_eq_norm_sq, hw]
  simp

/-- **A bar-odd phase with real coefficients is purely imaginary on `‖w‖ = 1`.** -/
theorem bar_odd_real_coeff_im_on_circle (f : ℂ → ℂ)
    (hreal : ∀ w, f (starRingEnd ℂ w) = starRingEnd ℂ (f w))
    (hodd : ∀ w, w ≠ 0 → f w⁻¹ = -f w) {w : ℂ} (hw : ‖w‖ = 1) :
    (f w).re = 0 := by
  have hw0 : w ≠ 0 := by
    intro h; rw [h, norm_zero] at hw; exact zero_ne_one hw
  have h := hreal w
  rw [conj_eq_inv_of_norm_one hw, hodd w hw0] at h
  have hre := congrArg Complex.re h
  rw [Complex.conj_re, Complex.neg_re] at hre
  linarith

/-- Hence on the unit circle the factor `cos (f w)` is a `cosh` of a real number,
so it is real and at least 1. -/
theorem cos_bar_odd_on_circle_is_cosh (f : ℂ → ℂ)
    (hreal : ∀ w, f (starRingEnd ℂ w) = starRingEnd ℂ (f w))
    (hodd : ∀ w, w ≠ 0 → f w⁻¹ = -f w) {w : ℂ} (hw : ‖w‖ = 1) :
    Complex.cos (f w) = ((Real.cosh (f w).im : ℝ) : ℂ) := by
  have hre := bar_odd_real_coeff_im_on_circle f hreal hodd hw
  have hfw : f w = ((f w).im : ℂ) * I := by
    apply Complex.ext <;> simp [hre]
  rw [hfw, imaginary_phase_is_cosh]
  simp

/-! ## 3. The convention-D ladder phase is real at the substrate -/

/-- `z_D = q³/(q²+1)`, the convention-D Markov parameter. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- `α_D = (z_D − 1)·h/2`, `h = q − q⁻¹`. -/
noncomputable def alphaD (q : ℝ) : ℝ := (zD q - 1) * (q - q⁻¹) / 2

/-- `β_D = α_D − h²/4`, the bar-odd part. -/
noncomputable def betaD (q : ℝ) : ℝ := alphaD q - (q - q⁻¹) ^ 2 / 4

theorem zD_sub_one (q : ℝ) : zD q - 1 = (q ^ 3 - q ^ 2 - 1) / (q ^ 2 + 1) := by
  have : q ^ 2 + 1 ≠ 0 := by positivity
  unfold zD; field_simp; ring

/-- **At the substrate window the D phase is real and strictly negative.** -/
theorem alphaD_neg {q : ℝ} (h1 : 1 < q) (h2 : q ^ 3 < q ^ 2 + 1) : alphaD q < 0 := by
  have hq0 : 0 < q := by linarith
  have hz : zD q - 1 < 0 := by
    rw [zD_sub_one]; exact div_neg_of_neg_of_pos (by linarith) (by positivity)
  have hh : 0 < q - q⁻¹ := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ h1
    linarith
  unfold alphaD
  have : (zD q - 1) * (q - q⁻¹) < 0 := mul_neg_of_neg_of_pos hz hh
  linarith

/-- `α_D` vanishes, for `q > 1`, exactly on `q³ = q² + 1`. -/
theorem alphaD_eq_zero_iff {q : ℝ} (h1 : 1 < q) : alphaD q = 0 ↔ q ^ 3 = q ^ 2 + 1 := by
  have hh : q - q⁻¹ ≠ 0 := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ h1
    linarith
  have hd : q ^ 2 + 1 ≠ 0 := by positivity
  unfold alphaD
  rw [zD_sub_one]
  constructor
  · intro h
    have h' : (q ^ 3 - q ^ 2 - 1) / (q ^ 2 + 1) * (q - q⁻¹) = 0 := by linarith
    rcases mul_eq_zero.mp h' with h3 | h3
    · rcases div_eq_zero_iff.mp h3 with h4 | h4
      · linarith
      · exact absurd h4 hd
    · exact absurd h3 hh
  · intro h
    have : q ^ 3 - q ^ 2 - 1 = 0 := by linarith
    rw [this]; simp

/-- The substrate window: every `q ∈ (1, 6/5)` has `q³ < q² + 1`. -/
theorem cube_lt_of_lt_six_fifths {q : ℝ} (h1 : 1 < q) (h2 : q < 6 / 5) :
    q ^ 3 < q ^ 2 + 1 := by
  nlinarith [sq_nonneg q, mul_pos (by linarith : (0:ℝ) < q) (by linarith : (0:ℝ) < q)]

/-- **The D bar defect.** `α_D(q) + α_D(q⁻¹) = h²/2`, so `α_D` is not bar-odd. -/
theorem alphaD_bar_sum {q : ℝ} (hq : q ≠ 0) :
    alphaD q + alphaD q⁻¹ = (q - q⁻¹) ^ 2 / 2 := by
  have h1 : q ^ 2 + 1 ≠ 0 := by positivity
  have h2 : (q⁻¹) ^ 2 + 1 ≠ 0 := by positivity
  unfold alphaD zD
  field_simp
  ring

/-- **`β_D = α_D − h²/4` is exactly bar-odd.** -/
theorem betaD_bar_odd {q : ℝ} (hq : q ≠ 0) : betaD q + betaD q⁻¹ = 0 := by
  have hs := alphaD_bar_sum hq
  unfold betaD
  rw [inv_inv]
  have : (q⁻¹ - q) ^ 2 = (q - q⁻¹) ^ 2 := by ring
  rw [this]
  linarith

/-- **Hence at the substrate the D ladder factor is a cosine, at most 1**, for
either reading of the phase (`α_D` or its bar-odd part `β_D`), and for every
real shift `δ`. -/
theorem d_ladder_factor_le_one (q δ : ℝ) :
    Real.cos (alphaD q - δ) ≤ 1 ∧ Real.cos (betaD q - δ) ≤ 1 :=
  ⟨Real.cos_le_one _, Real.cos_le_one _⟩

end QOU.QBeta.DEigenphase
