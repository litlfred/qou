/-
  Kummer's identity for general `z`, by radial reduction.

  Bean `qou-kmmr`, fourth increment — the assembly.

  ═══ THE ARGUMENT ═══

  Fix `φ = arg z ∈ (0, π)` and move along the ray `r ↦ r·e^{iφ}`.  Then:

  * `θ₁ = arg z = φ` is **constant**, so `Λ(θ₁)` contributes nothing;
  * `θ₁+θ₂+θ₃ = π` (`tetAngles_sum_eq_pi`) gives `θ₃ = π − φ − θ₂`, so `θ₃` moves
    exactly opposite to `θ₂`;
  * hence `d/dr (Λ(θ₂)+Λ(θ₃)) = (log(2 sin θ₃) − log(2 sin θ₂))·θ₂′`, which the
    **law of sines** (`IdealTetLawOfSines.log_sin_sub_log_sin`) turns into
    `−log r · θ₂′`;
  * on the dilogarithm side `d/dr Im cLiTwoExt = θ₂/r` and
    `d/dr (log r · arg(1−z)) = −θ₂/r − log r · θ₂′`, so that side also moves at
    `−log r · θ₂′`.

  The difference is therefore constant on `(0, ∞)`, and `r = 1` kills it by
  `KummerDilogHalf.kummer_unit_circle`.  Two variables collapsed to one, with the
  unit-circle case as the basepoint.

  ═══ WHAT THIS GIVES ═══

  `kummer` — for every `z` with `Im z > 0`,

      `BlochWigner_lob z = Im cLiTwoExt z + log‖z‖ · arg(1−z)`

  i.e. the corpus's angle-built Bloch–Wigner function **is** the dilogarithm one.
  This lifts, in full, the prohibition `BlochWignerLobachevsky.lean` records
  against transporting dilogarithm facts onto `BlochWigner_lob`.

  ⚠ It is still **not** `Vol(5₂)`.  That needs the *geometric* factor — that a
  particular triangulation's Λ-sum is the hyperbolic volume of a particular knot
  complement — which is `qou-m015`/`qou-krvm` territory and untouched here.

  -- Ref: [zagier1986], [milnor1982], [neumann-zagier1985]
-/
import QOU.Knot.KummerDilogHalf
import QOU.Knot.IdealTetLawOfSines
import QOU.Knot.RivinConcavity

namespace QOU.Knot.KummerRadial

open Real Complex QOU.Archimedean QOU.Knot.IdealTet

/-- The ray through `e^{iφ}`. -/
noncomputable def ray (φ r : ℝ) : ℂ := (r : ℂ) * Complex.exp ((φ : ℂ) * Complex.I)

variable {φ r : ℝ}

theorem ray_norm (hr : 0 < r) : ‖ray φ r‖ = r := by
  unfold ray
  rw [norm_mul, Complex.norm_real, Real.norm_eq_abs, abs_of_pos hr]
  simp [Complex.norm_exp]

theorem ray_im (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) : 0 < (ray φ r).im := by
  unfold ray
  rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]
  simp only [Complex.mul_im, Complex.add_re, Complex.add_im, Complex.ofReal_re,
    Complex.ofReal_im, Complex.I_re, Complex.I_im, mul_zero, zero_mul,
    add_zero, zero_add, mul_one]
  exact mul_pos hr (Real.sin_pos_of_pos_of_lt_pi hφ0 hφ1)

theorem ray_arg (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    tetAngle₁ (ray φ r) = φ := by
  unfold tetAngle₁ ray
  rw [Complex.arg_real_mul _ hr]
  exact QOU.Knot.Kummer.arg_exp_mul_I ⟨by linarith [Real.pi_pos], le_of_lt hφ1⟩

/-! ### `θ₂` along the ray -/

/-- `θ₂ = −arg(1−z) = −Im log(1−z)` on the upper half plane. -/
theorem tetAngle₂_eq {z : ℂ} (hz : 0 < z.im) :
    tetAngle₂ z = -(Complex.log (1 - z)).im := by
  have h1z : (1 : ℂ) - z ≠ 0 := IdealTet.one_sub_ne_zero hz
  have hne : Complex.arg (1 - z) ≠ π := by
    intro h
    have := Complex.arg_eq_pi_iff.mp h
    have him : ((1 : ℂ) - z).im = 0 := this.2
    simp only [Complex.sub_im, Complex.one_im, zero_sub, neg_eq_zero] at him
    exact absurd him (ne_of_gt hz)
  unfold tetAngle₂
  rw [one_div, Complex.arg_inv, if_neg hne, Complex.log_im]

/-- `1 − z` is off the slit whenever `Im z ≠ 0`. -/
theorem one_sub_mem_slit {z : ℂ} (hz : 0 < z.im) :
    (1 : ℂ) - z ∈ Complex.slitPlane := by
  refine Or.inr ?_
  simp only [Complex.sub_im, Complex.one_im, zero_sub, ne_eq, neg_eq_zero]
  exact ne_of_gt hz

/-- The derivative of `θ₂` along the ray.  Its **value** is never used — only
that it exists, and that both sides of Kummer move at `−log r` times it. -/
theorem hasDerivAt_tetAngle₂_ray (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    HasDerivAt (fun s : ℝ => tetAngle₂ (ray φ s))
      (((1 - ray φ r)⁻¹ * Complex.exp ((φ : ℂ) * Complex.I)).im) r := by
  have hz := ray_im hφ0 hφ1 hr
  have hslit := one_sub_mem_slit hz
  -- `s ↦ 1 - ray φ s` has derivative `-e^{iφ}`
  have hinner : HasDerivAt (fun s : ℝ => 1 - ray φ s)
      (-Complex.exp ((φ : ℂ) * Complex.I)) r := by
    have hlin : HasDerivAt (fun s : ℝ => ray φ s) (Complex.exp ((φ : ℂ) * Complex.I)) r := by
      unfold ray
      simpa using (Complex.ofRealCLM.hasDerivAt (x := r)).mul_const
        (Complex.exp ((φ : ℂ) * Complex.I))
    simpa using hlin.const_sub 1
  have hlog := (Complex.hasDerivAt_log hslit).scomp r hinner
  -- take `-Im`
  have him : HasDerivAt (fun s : ℝ => (Complex.log (1 - ray φ s)).im)
      ((-Complex.exp ((φ : ℂ) * Complex.I) * (1 - ray φ r)⁻¹).im) r := by
    simpa [Function.comp, mul_comm] using
      Complex.imCLM.hasFDerivAt.comp_hasDerivAt r hlog
  -- the two descriptions of `θ₂` agree on a NEIGHBOURHOOD of `r` (namely `Ioi 0`),
  -- which is all `HasDerivAt` needs — they do not agree globally
  have hev : (fun s : ℝ => tetAngle₂ (ray φ s))
      =ᶠ[nhds r] fun s : ℝ => -(Complex.log (1 - ray φ s)).im := by
    filter_upwards [Ioi_mem_nhds hr] with s hs
    exact tetAngle₂_eq (ray_im hφ0 hφ1 hs)
  have hneg := him.neg
  have hval : -(-Complex.exp ((φ : ℂ) * Complex.I) * (1 - ray φ r)⁻¹).im
      = ((1 - ray φ r)⁻¹ * Complex.exp ((φ : ℂ) * Complex.I)).im := by
    rw [neg_mul, Complex.neg_im, neg_neg, mul_comm]
  rw [hval] at hneg
  exact hneg.congr_of_eventuallyEq hev



/-! ### Angle ranges along the ray -/

theorem tetAngle₂_mem (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    0 < tetAngle₂ (ray φ r) ∧ tetAngle₂ (ray φ r) < π :=
  arg_mem_Ioo_of_im_pos _ (tet_im_pos _ (ray_im hφ0 hφ1 hr)).1

theorem tetAngle₃_mem (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    0 < tetAngle₃ (ray φ r) ∧ tetAngle₃ (ray φ r) < π :=
  arg_mem_Ioo_of_im_pos _ (tet_im_pos _ (ray_im hφ0 hφ1 hr)).2

/-- `θ₃ = π − φ − θ₂` along the ray: the angle sum with `θ₁ = φ` frozen. -/
theorem tetAngle₃_eq (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    tetAngle₃ (ray φ r) = π - φ - tetAngle₂ (ray φ r) := by
  have h := tetAngles_sum_eq_pi _ (ray_im hφ0 hφ1 hr)
  rw [ray_arg hφ0 hφ1 hr] at h
  linarith

/-! ### The two sides move together -/

/-- `d/dr Im cLiTwoExt(r e^{iφ}) = θ₂ / r`. -/
theorem hasDerivAt_im_cLiTwoExt_ray (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    HasDerivAt (fun s : ℝ => (QOU.MathlibExt.cLiTwoExt (ray φ s)).im)
      (tetAngle₂ (ray φ r) / r) r := by
  have hz := ray_im hφ0 hφ1 hr
  have hz0 : ray φ r ≠ 0 := IdealTet.ne_zero_of_im_pos hz
  have hmem : ray φ r ∈ QOU.MathlibExt.notCut :=
    QOU.MathlibExt.mem_notCut_iff.mpr (Or.inl (ne_of_gt hz))
  have hinner : HasDerivAt (fun s : ℝ => ray φ s) (Complex.exp ((φ : ℂ) * Complex.I)) r := by
    unfold ray
    simpa using (Complex.ofRealCLM.hasDerivAt (x := r)).mul_const
      (Complex.exp ((φ : ℂ) * Complex.I))
  have hcomp := (QOU.MathlibExt.hasDerivAt_cLiTwoExt' hmem hz0).scomp r hinner
  -- `e^{iφ}/z = 1/r`, so the derivative is `-log(1-z)/r`
  have hval : (Complex.exp ((φ : ℂ) * Complex.I)) •
      (-(Complex.log (1 - ray φ r) / ray φ r))
      = -(Complex.log (1 - ray φ r)) / (r : ℂ) := by
    rw [smul_eq_mul]
    unfold ray
    have hrc : ((r : ℝ) : ℂ) ≠ 0 := by
      simpa using ne_of_gt hr
    field_simp
  rw [hval] at hcomp
  have him : HasDerivAt (fun s : ℝ => (QOU.MathlibExt.cLiTwoExt (ray φ s)).im)
      ((-(Complex.log (1 - ray φ r)) / (r : ℂ)).im) r := by
    simpa [Function.comp] using Complex.imCLM.hasFDerivAt.comp_hasDerivAt r hcomp
  have hfin : (-(Complex.log (1 - ray φ r)) / (r : ℂ)).im = tetAngle₂ (ray φ r) / r := by
    rw [tetAngle₂_eq hz, Complex.div_ofReal_im, Complex.neg_im]
  rwa [hfin] at him

/-- `d/dr (Λ(θ₁) + Λ(θ₂) + Λ(θ₃)) = −log r · θ₂′` — the law of sines is what
turns the two `Λ′` terms into `−log r`. -/
theorem hasDerivAt_lobSide (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    HasDerivAt (fun s : ℝ => BlochWigner_lob (ray φ s))
      (-Real.log r * ((1 - ray φ r)⁻¹ * Complex.exp ((φ : ℂ) * Complex.I)).im) r := by
  have hz := ray_im hφ0 hφ1 hr
  have h2 := tetAngle₂_mem hφ0 hφ1 hr
  have h3 := tetAngle₃_mem hφ0 hφ1 hr
  have hu := hasDerivAt_tetAngle₂_ray hφ0 hφ1 hr
  set u := ((1 - ray φ r)⁻¹ * Complex.exp ((φ : ℂ) * Complex.I)).im with hu_def
  -- `Λ(θ₁)` is constant, `Λ(θ₂)` and `Λ(θ₃)` move oppositely
  have hA : HasDerivAt (fun s : ℝ => Lob (tetAngle₁ (ray φ s))) 0 r := by
    have hev : (fun s : ℝ => Lob (tetAngle₁ (ray φ s))) =ᶠ[nhds r] fun _ : ℝ => Lob φ := by
      filter_upwards [Ioi_mem_nhds hr] with s hs
      rw [ray_arg hφ0 hφ1 hs]
    exact (hasDerivAt_const r (Lob φ)).congr_of_eventuallyEq hev
  -- `HasDerivAt.comp` yields `?f ∘ g`, which will not unify against a lambda:
  -- bind the composed form first, then coerce.
  have hB0 : HasDerivAt (Lob ∘ fun s : ℝ => tetAngle₂ (ray φ s))
      (-Real.log (2 * Real.sin (tetAngle₂ (ray φ r))) * u) r :=
    (QOU.Knot.Rivin.hasDerivAt_Lob h2.1 h2.2).comp r hu
  have hB : HasDerivAt (fun s : ℝ => Lob (tetAngle₂ (ray φ s)))
      (-Real.log (2 * Real.sin (tetAngle₂ (ray φ r))) * u) r := hB0
  have hC : HasDerivAt (fun s : ℝ => Lob (tetAngle₃ (ray φ s)))
      (-Real.log (2 * Real.sin (tetAngle₃ (ray φ r))) * -u) r := by
    have hev : (fun s : ℝ => tetAngle₃ (ray φ s))
        =ᶠ[nhds r] fun s : ℝ => π - φ - tetAngle₂ (ray φ s) := by
      filter_upwards [Ioi_mem_nhds hr] with s hs
      exact tetAngle₃_eq hφ0 hφ1 hs
    have hd : HasDerivAt (fun s : ℝ => tetAngle₃ (ray φ s)) (-u) r := by
      have := (hasDerivAt_const r (π - φ)).sub hu
      simpa using this.congr_of_eventuallyEq hev
    have hC0 : HasDerivAt (Lob ∘ fun s : ℝ => tetAngle₃ (ray φ s))
        (-Real.log (2 * Real.sin (tetAngle₃ (ray φ r))) * -u) r :=
      (QOU.Knot.Rivin.hasDerivAt_Lob h3.1 h3.2).comp r hd
    exact hC0
  have hsum := (hA.add hB).add hC
  -- the law of sines collapses the two `Λ′` terms
  have hlos := IdealTet.log_sin_sub_log_sin hz
  rw [ray_norm hr] at hlos
  have hval : (0 : ℝ) + -Real.log (2 * Real.sin (tetAngle₂ (ray φ r))) * u
      + -Real.log (2 * Real.sin (tetAngle₃ (ray φ r))) * -u
      = -Real.log r * u := by
    have hl : Real.log (2 * Real.sin (tetAngle₃ (ray φ r)))
        - Real.log (2 * Real.sin (tetAngle₂ (ray φ r))) = -Real.log r := hlos
    linear_combination u * hl
  rw [hval] at hsum
  exact hsum

/-! ### Constancy along the ray, and the basepoint -/

/-- `arg(1 − z) = −θ₂`. -/
theorem arg_one_sub_eq {z : ℂ} (hz : 0 < z.im) :
    Complex.arg (1 - z) = -tetAngle₂ z := by
  rw [tetAngle₂_eq hz, Complex.log_im, neg_neg]

/-- Constancy from a vanishing derivative on `Ioi`. -/
theorem eq_of_hasDerivAt_zero_Ioi {f : ℝ → ℝ} {a : ℝ}
    (hf : ∀ x ∈ Set.Ioi a, HasDerivAt f 0 x) {x y : ℝ}
    (hx : x ∈ Set.Ioi a) (hy : y ∈ Set.Ioi a) : f x = f y := by
  refine (convex_Ioi a).is_const_of_fderivWithin_eq_zero
    (fun z hz => ((hf z hz).differentiableAt).differentiableWithinAt) ?_ hx hy
  intro z hz
  have hF : HasFDerivAt f (ContinuousLinearMap.smulRight (1 : ℝ →L[ℝ] ℝ) (0 : ℝ)) z :=
    hf z hz
  rw [fderivWithin_of_isOpen isOpen_Ioi hz, hF.fderiv]
  ext
  simp

/-- **The Kummer defect is constant along every ray**, because both sides move at
`−log r · θ₂′`. -/
theorem hasDerivAt_defect_zero (hφ0 : 0 < φ) (hφ1 : φ < π) (hr : 0 < r) :
    HasDerivAt (fun s : ℝ => BlochWigner_lob (ray φ s)
      - ((QOU.MathlibExt.cLiTwoExt (ray φ s)).im
        + Real.log s * Complex.arg (1 - ray φ s))) 0 r := by
  set u := ((1 - ray φ r)⁻¹ * Complex.exp ((φ : ℂ) * Complex.I)).im with hu_def
  have hu := hasDerivAt_tetAngle₂_ray hφ0 hφ1 hr
  have hlob := hasDerivAt_lobSide hφ0 hφ1 hr
  have hdil := hasDerivAt_im_cLiTwoExt_ray hφ0 hφ1 hr
  rw [← hu_def] at hlob hu
  -- the `log r · arg(1−z)` term
  have hG : HasDerivAt (fun s : ℝ => Real.log s * Complex.arg (1 - ray φ s))
      (r⁻¹ * -tetAngle₂ (ray φ r) + Real.log r * -u) r := by
    have hev : (fun s : ℝ => Real.log s * Complex.arg (1 - ray φ s))
        =ᶠ[nhds r] fun s : ℝ => Real.log s * -tetAngle₂ (ray φ s) := by
      filter_upwards [Ioi_mem_nhds hr] with s hs
      rw [arg_one_sub_eq (ray_im hφ0 hφ1 hs)]
    have hmul := (Real.hasDerivAt_log (ne_of_gt hr)).mul hu.neg
    exact hmul.congr_of_eventuallyEq hev
  have hsum := hlob.sub (hdil.add hG)
  convert hsum using 1
  have hrne : r ≠ 0 := ne_of_gt hr
  field_simp
  ring

/-- **KUMMER'S IDENTITY, general `z`.**

For every `z` with `Im z > 0`,

    `BlochWigner_lob z = Im cLiTwoExt z + log‖z‖ · arg(1 − z)`

— the corpus's angle-built Bloch–Wigner function **is** the dilogarithm one.

Proof: along the ray through `z`, the defect has vanishing derivative
(`hasDerivAt_defect_zero`, which is the law of sines in disguise), so it is
constant; at `r = 1` it vanishes by `KummerDilogHalf.kummer_unit_circle`. -/
theorem kummer {z : ℂ} (hz : 0 < z.im) :
    BlochWigner_lob z
      = (QOU.MathlibExt.cLiTwoExt z).im + Real.log ‖z‖ * Complex.arg (1 - z) := by
  have hz0 : z ≠ 0 := IdealTet.ne_zero_of_im_pos hz
  have harg := arg_mem_Ioo_of_im_pos z hz
  set φ := Complex.arg z with hφ
  have hn : (0 : ℝ) < ‖z‖ := norm_pos_iff.mpr hz0
  have hray : ray φ ‖z‖ = z := by
    unfold ray; exact Complex.norm_mul_exp_arg_mul_I z
  have hconst := eq_of_hasDerivAt_zero_Ioi
    (fun s hs => hasDerivAt_defect_zero harg.1 harg.2 hs)
    (x := ‖z‖) (y := 1) (Set.mem_Ioi.mpr hn) (Set.mem_Ioi.mpr one_pos)
  -- at `r = 1` the defect vanishes: this is the unit-circle case
  have hr1 : ray φ 1 = Complex.exp ((φ : ℂ) * Complex.I) := by
    unfold ray; simp
  have huc := QOU.Knot.Kummer.kummer_unit_circle harg.1 harg.2
  rw [show ‖Complex.exp ((φ : ℂ) * Complex.I)‖ = 1 by simp [Complex.norm_exp],
    Real.log_one, zero_mul, add_zero] at huc
  rw [hr1, Real.log_one, zero_mul, add_zero, huc] at hconst
  rw [hray] at hconst
  linarith [hconst]

end QOU.Knot.KummerRadial
