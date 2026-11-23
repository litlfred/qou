import Mathlib.MeasureTheory.Function.Jacobian
import Mathlib.Analysis.Calculus.FDeriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import QOU.Archimedean.HyperbolicVolumeMeasure

/-!
# H2 (Möbius): `hypVolume` is invariant under inversion in the unit sphere

Bean `qou-h2mb`. `QOU.Archimedean.HyperbolicVolumeMeasure` proves that the measure
`dV = dx dy dz / z³` on upper half-space is invariant under dilation and horizontal
translation. This file proves the missing generator: inversion in the unit sphere

    σ(x) = x / ‖x‖²,      ‖x‖² = x₀² + x₁² + x₂²   (Euclidean, written out:
                                                     the `Fin 3 → ℝ` norm is the sup norm)

maps upper half-space to itself and preserves `hypVolume`.

The proof is a change of variables:

* `hasFDerivAt_inversion` — `Dσ(x) h = h/‖x‖² − 2⟨x,h⟩ x/‖x‖⁴`.
* `det_inversionDeriv` — `det Dσ(x) = −1/‖x‖⁶`. The bracket `I − 2xxᵀ/‖x‖²` is a
  Householder reflection; here the determinant is computed directly by
  `Matrix.det_fin_three`.
* `hypDensity_inversion_mul` — `|det Dσ(x)| · (1/(σx)₂³) = 1/x₂³`, since `(σx)₂ = x₂/‖x‖²`.
* `hypVolume_inversion_image` — `hypVolume (σ '' A) = hypVolume A` for every measurable
  `A ⊆ H³`, via `lintegral_image_eq_lintegral_abs_det_fderiv_mul`. Injectivity is `σ ∘ σ = id`
  off the origin.

* `hypVolume_linear_image` — the same for a linear map fixing the height with `|det| = 1`
  (rotations about the vertical axis, reflections in vertical planes).

With horizontal translation, dilation, vertical-axis rotation and this inversion,
`hypVolume` is invariant under a generating set of the isometry group of `H³`
(`PSL₂(ℂ)` together with the orientation-reversing elements). This file does NOT prove
that these maps generate the isometry group; that is a standard fact cited, not formalized.

Archimedean (ℝ): Lebesgue measure, ordering — §7c.

-- Ref: [thurston1978] Ch. 1 (the upper half-space model and its isometries)
-- Ref: [leitner2026] beans qou-5gai (H2), qou-h2mb
-/

namespace QOU.Archimedean.HyperbolicVolume

open MeasureTheory Set

/-- Euclidean squared norm on `Fin 3 → ℝ`. -/
def nsq (x : Fin 3 → ℝ) : ℝ := x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2

/-- Inversion in the unit sphere: `σ(x) = x / ‖x‖²`. -/
noncomputable def inversion (x : Fin 3 → ℝ) : Fin 3 → ℝ := (nsq x)⁻¹ • x

/-- The linear form `h ↦ ⟨x, h⟩`. -/
noncomputable def ip (x : Fin 3 → ℝ) : (Fin 3 → ℝ) →L[ℝ] ℝ :=
  x 0 • ContinuousLinearMap.proj 0 + x 1 • ContinuousLinearMap.proj 1 +
    x 2 • ContinuousLinearMap.proj 2

/-- The derivative of the inversion: `h ↦ h/‖x‖² − 2⟨x,h⟩ x/‖x‖⁴`. -/
noncomputable def inversionDeriv (x : Fin 3 → ℝ) : (Fin 3 → ℝ) →L[ℝ] (Fin 3 → ℝ) :=
  (nsq x)⁻¹ • ContinuousLinearMap.id ℝ (Fin 3 → ℝ) -
    (2 * (nsq x ^ 2)⁻¹) • (ip x).smulRight x

theorem nsq_pos_of_mem {x : Fin 3 → ℝ} (hx : x ∈ upperHalfSpace) : 0 < nsq x := by
  have h2 : 0 < x 2 := hx
  unfold nsq; positivity

theorem inversion_apply_two (x : Fin 3 → ℝ) : inversion x 2 = x 2 / nsq x := by
  simp [inversion, div_eq_inv_mul]

theorem nsq_inversion {x : Fin 3 → ℝ} (hx : nsq x ≠ 0) : nsq (inversion x) = (nsq x)⁻¹ := by
  simp only [nsq, inversion, Pi.smul_apply, smul_eq_mul] at hx ⊢
  field_simp

/-- `σ ∘ σ = id` off the origin. -/
theorem inversion_inversion {x : Fin 3 → ℝ} (hx : nsq x ≠ 0) : inversion (inversion x) = x := by
  rw [inversion, nsq_inversion hx, inv_inv, inversion, smul_smul, mul_inv_cancel₀ hx, one_smul]

/-- Inversion maps upper half-space into itself. -/
theorem inversion_mem {x : Fin 3 → ℝ} (hx : x ∈ upperHalfSpace) : inversion x ∈ upperHalfSpace := by
  show 0 < inversion x 2
  rw [inversion_apply_two]
  exact div_pos hx (nsq_pos_of_mem hx)

theorem hasFDerivAt_nsq (x : Fin 3 → ℝ) : HasFDerivAt nsq ((2 : ℝ) • ip x) x := by
  have h : ∀ i : Fin 3, HasFDerivAt (fun y : Fin 3 → ℝ => y i ^ 2)
      ((2 * x i) • ContinuousLinearMap.proj (R := ℝ) (φ := fun _ : Fin 3 => ℝ) i) x := by
    intro i
    have := (hasFDerivAt_apply (𝕜 := ℝ) i x).pow 2
    refine this.congr_fderiv ?_
    ext h; simp
  have hs := ((h 0).add (h 1)).add (h 2)
  refine hs.congr_fderiv ?_
  ext h; simp [ip]; ring

theorem hasFDerivAt_inversion {x : Fin 3 → ℝ} (hx : nsq x ≠ 0) :
    HasFDerivAt inversion (inversionDeriv x) x := by
  have hinv : HasFDerivAt (fun y => (nsq y)⁻¹)
      ((ContinuousLinearMap.smulRight (1 : ℝ →L[ℝ] ℝ) (-(nsq x ^ 2)⁻¹)).comp
        ((2 : ℝ) • ip x)) x :=
    (hasFDerivAt_inv hx).comp x (hasFDerivAt_nsq x)
  have hs := hinv.fun_smul (hasFDerivAt_id x)
  refine hs.congr_fderiv ?_
  ext h i
  simp [inversionDeriv, ip]
  ring

open Matrix in
/-- **The Jacobian determinant of the inversion is `−1/‖x‖⁶`.** -/
theorem det_inversionDeriv {x : Fin 3 → ℝ} (hx : nsq x ≠ 0) :
    (inversionDeriv x).det = -((nsq x)⁻¹) ^ 3 := by
  rw [ContinuousLinearMap.det, ← LinearMap.det_toMatrix', Matrix.det_fin_three]
  simp only [LinearMap.toMatrix'_apply, ContinuousLinearMap.coe_coe, inversionDeriv, ip,
    ContinuousLinearMap.coe_sub', ContinuousLinearMap.coe_smul', Pi.sub_apply, Pi.smul_apply,
    ContinuousLinearMap.coe_id', id_eq, ContinuousLinearMap.smulRight_apply,
    ContinuousLinearMap.add_apply, ContinuousLinearMap.coe_smul', ContinuousLinearMap.proj_apply,
    smul_eq_mul]
  simp only [Fin.isValue, Fin.reduceEq, if_true, if_false, mul_one, mul_zero, add_zero, zero_add]
  have hn : nsq x = x 0 ^ 2 + x 1 ^ 2 + x 2 ^ 2 := rfl
  field_simp
  rw [hn]
  ring

/-- The density times the Jacobian is the density: `|det Dσ(x)| · 1/((σx)₂)³ = 1/x₂³`. -/
theorem hypDensity_inversion_mul {x : Fin 3 → ℝ} (hx : x ∈ upperHalfSpace) :
    ENNReal.ofReal |(inversionDeriv x).det| * hypDensity (inversion x) = hypDensity x := by
  have hn := nsq_pos_of_mem hx
  have h2 : 0 < x 2 := hx
  rw [det_inversionDeriv hn.ne', hypDensity, hypDensity, inversion_apply_two,
    ← ENNReal.ofReal_mul (abs_nonneg _)]
  congr 1
  rw [abs_neg, abs_of_pos (by positivity)]
  field_simp

/-- **H2 (Möbius) — `hypVolume` is invariant under inversion in the unit sphere.**
For every measurable `A` in upper half-space, `hypVolume (σ '' A) = hypVolume A`. -/
theorem hypVolume_inversion_image {A : Set (Fin 3 → ℝ)} (hA : MeasurableSet A)
    (hAH : A ⊆ upperHalfSpace) : hypVolume (inversion '' A) = hypVolume A := by
  have hder : ∀ x ∈ A, HasFDerivWithinAt inversion (inversionDeriv x) A x := fun x hx =>
    (hasFDerivAt_inversion (nsq_pos_of_mem (hAH hx)).ne').hasFDerivWithinAt
  have hinj : InjOn inversion A := by
    intro x hx y hy hxy
    rw [← inversion_inversion (nsq_pos_of_mem (hAH hx)).ne',
      ← inversion_inversion (nsq_pos_of_mem (hAH hy)).ne', hxy]
  rw [hypVolume, withDensity_apply' _ _, withDensity_apply' _ _,
    lintegral_image_eq_lintegral_abs_det_fderiv_mul volume hA hder hinj]
  refine setLIntegral_congr_fun hA fun x hx => ?_
  exact hypDensity_inversion_mul (hAH hx)

/-- Inversion maps upper half-space onto itself. -/
theorem inversion_image_upperHalfSpace : inversion '' upperHalfSpace = upperHalfSpace := by
  ext y
  constructor
  · rintro ⟨x, hx, rfl⟩; exact inversion_mem hx
  · intro hy
    exact ⟨inversion y, inversion_mem hy, inversion_inversion (nsq_pos_of_mem hy).ne'⟩

/-! ### Linear maps fixing the height: rotations about the vertical axis

A linear map that fixes the height coordinate and has `|det| = 1` (a rotation about the
vertical axis, or a reflection in a vertical plane) preserves `hypVolume`. -/

/-- **H2 (vertical-axis rotations and vertical reflections).** If `L` is an injective
continuous linear map with `|det L| = 1` and `(L x)₂ = x₂` for all `x`, then
`hypVolume (L '' A) = hypVolume A` for every measurable `A`. -/
theorem hypVolume_linear_image {L : (Fin 3 → ℝ) →L[ℝ] (Fin 3 → ℝ)}
    (hdet : |L.det| = 1) (hL2 : ∀ x, L x 2 = x 2) (hinj : Function.Injective L)
    {A : Set (Fin 3 → ℝ)} (hA : MeasurableSet A) : hypVolume (L '' A) = hypVolume A := by
  rw [hypVolume, withDensity_apply' _ _, withDensity_apply' _ _,
    lintegral_image_eq_lintegral_abs_det_fderiv_mul volume hA
      (fun x _ => L.hasFDerivAt.hasFDerivWithinAt) hinj.injOn]
  refine setLIntegral_congr_fun hA fun x _ => ?_
  rw [hdet, ENNReal.ofReal_one, one_mul, hypDensity, hypDensity, hL2]

end QOU.Archimedean.HyperbolicVolume
