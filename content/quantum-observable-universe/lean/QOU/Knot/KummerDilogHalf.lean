/-
  The dilogarithm half of Kummer on the unit circle:
  `Im (cLiTwoExt (e^{iθ})) = Cl₂(θ)` for `θ ∈ (0, 2π)`.

  Bean `qou-kmmr`, second increment.  Companion to `QOU/Knot/KummerUnitCircle.lean`,
  which proved the Λ-side.

  ═══ WHY THIS CLOSES A GAP THAT WAS EXPLICITLY FLAGGED ═══

  `KummerUnitCircle.blochWigner_lob_exp` proves `BlochWigner_lob(e^{iθ}) = Cl₂(θ)`
  and stops there, stating its conclusion in terms of `Cl₂` alone.  Route 72's G3
  recorded precisely why: the *dilogarithm* half was numerically true to `1e-45`
  but unproved for the corpus's own `cLiTwoExt`, so nothing licensed identifying
  the corpus's `BlochWigner_lob` with the Bloch–Wigner dilogarithm.

  This file supplies that half.  Together with `blochWigner_lob_exp` it gives
  **Kummer's identity on the unit circle in full** (`kummer_unit_circle`).

  ═══ THE PROOF ═══

  The technique is the one the 5₂ sum-rule lane used throughout: **same
  derivative, then pin the constant.**

  Along `z = e^{iθ}`, `dz/dθ = i·z`, so by `hasDerivAt_cLiTwoExt'`

      d/dθ cLiTwoExt(e^{iθ}) = −(log(1−z)/z)·(i·z) = −i·log(1−z)

  whose imaginary part is `−Re log(1−z) = −log|1−z| = −log(2 sin(θ/2))` — which
  is *verbatim* `Cl₂′(θ)` (`hasDerivAt_Cl_2_series`).  So the difference is
  constant on `(0, 2π)`, and `θ = π` kills it: `cLiTwoExt(−1) = −π²/12` is
  **real**, so its imaginary part is `0`, and `Cl₂(π) = 0`.

  A pleasant accident of the domain: the **whole** punctured circle lies in
  `notCut = {w | w.im ≠ 0 ∨ w.re < 1}`.  Off `θ = π` the imaginary part
  `sin θ ≠ 0`; at `θ = π` the point is `−1`, whose real part is `< 1`.  So no
  case split on the upper/lower half is needed, and the interval `(0, 2π)` can be
  treated in one piece — which is also what makes `θ = π` available as the
  basepoint.

  ═══ WHAT IS STILL NOT PROVED ═══

  ~~Kummer for general `z`.~~  **Now proved** — `QOU/Knot/KummerRadial.lean`
  (`kummer`), by a *radial* reduction that uses this file's result as its
  basepoint, not by the two-variable argument this note anticipated.  This file
  still proves only the `|z| = 1` case; that is deliberate, since the radial
  argument needs exactly that as input.

  Still true: nothing here or in `KummerRadial` reaches `Vol(5₂)` — Kummer is the
  *analytic* factor of `Vol = D`; the geometric factor is `qou-m015`/`qou-krvm`.

  **The 5₂ sum rule is PROVED**
  (`FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`); the 5₂ **volume**
  conjecture is Ohtsuki's published theorem and is not formalised anywhere here.


  ═══ ⚠ NAMING: THIS IS NOT THE CORPUS'S OTHER KUMMER ═══

  "Kummer" appears in QOU in **two unrelated senses**, both after Ernst Kummer,
  and a grep for the name will mix them:

  1. **Kummer's identity** (Lewin, *Polylogarithms*, p. 121 eq. (5.5)) — the
     dilogarithm identity relating the Λ-sum to `Im Li₂(z) + log|z|·arg(1−z)`.
     That is this file, and the `QOU.Knot.Kummer` namespace.
  2. **The Kummer sequence / filtration / tower** — `1 → μₙ → 𝔾ₘ → 𝔾ₘ → 1` and
     the obstruction classes `κₙ ∈ H²(𝒮, ℬ)` of the Yekutieli lifting tower
     (`lifting-and-descent/`, `stochastic-mechanics/`, `conj:q-gl-kummer-filtration`,
     `prop:ns-kummer-specialisation`, `rem:hochschild-kummer-connection`). The
     "**central element**" language belongs to *that* story — the crossed-module
     boundary `∂ : 𝒪_M^× → SU_{qₙ}(2)` sending a unit to the central element
     `a·𝟙` — and has nothing to do with dilogarithms.

  They are mathematically unrelated. Do not let a search for one surface the
  other as if it were relevant.

  ═══ WHERE THE TWO STORIES DO TOUCH ═══

  Not through Kummer, but through `Vol(5₂)`. `predicted-spectra/yekutieli-transcendence-shadow.md`
  conjectures that `Vol(4₁)`, `Vol(5₂)`, `Vol(ℬ₃)` are **algebraically
  independent** — a polynomial relation among them over `ℚ[q,q^{-1}]` would force
  the obstruction tower to close up at finite height, which the corpus's
  perpetual-obstruction argument needs not to happen.

  Worth stating plainly, because it is the obvious worry: **the proved 5₂ sum
  rule does not threaten that conjecture.** The sum rule is a closed form for
  `A = Σ Li₂(yⱼ)` over the Galois orbit, and the Bloch–Wigner `D` — which is
  what carries the volume — **cancels identically on that orbit**. So the sum
  rule constrains a quantity from which `Vol(5₂)` has already dropped out, and
  says nothing about algebraic independence of volumes.

  -- Ref: [zagier1986], [milnor1982]
-/
import QOU.Knot.KummerUnitCircle
import QOU.MathlibExt.ComplexDilogarithmDeriv
import QOU.MathlibExt.ComplexDilogarithmInversion
import QOU.Knot.Clausen

namespace QOU.Knot.Kummer

open Real Complex QOU.Archimedean

/-! ### A constancy helper on an open interval -/

/-- If a real function has derivative `0` throughout `Ioo a b`, it is constant
there.  `Ioo` is convex and open, so `fderivWithin` collapses to `fderiv`. -/
theorem eq_of_hasDerivAt_zero_Ioo {f : ℝ → ℝ} {a b : ℝ}
    (hf : ∀ x ∈ Set.Ioo a b, HasDerivAt f 0 x) {x y : ℝ}
    (hx : x ∈ Set.Ioo a b) (hy : y ∈ Set.Ioo a b) : f x = f y := by
  refine (convex_Ioo a b).is_const_of_fderivWithin_eq_zero
    (fun z hz => ((hf z hz).differentiableAt).differentiableWithinAt) ?_ hx hy
  intro z hz
  have hF : HasFDerivAt f (ContinuousLinearMap.smulRight (1 : ℝ →L[ℝ] ℝ) (0 : ℝ)) z :=
    hf z hz
  rw [fderivWithin_of_isOpen isOpen_Ioo hz, hF.fderiv]
  ext
  simp

/-! ### The unit circle sits inside `notCut` -/

/-- The whole punctured unit circle is off both cuts: for `θ ∈ (0, 2π)`, either
`sin θ ≠ 0`, or `θ = π` and the point is `−1` with real part `< 1`. -/
theorem exp_mem_notCut {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    Complex.exp ((θ : ℂ) * Complex.I) ∈ QOU.MathlibExt.notCut := by
  rw [QOU.MathlibExt.mem_notCut_iff]
  right
  have hs : 0 < Real.sin (θ / 2) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hcos : Real.cos θ = 1 - 2 * Real.sin (θ / 2) ^ 2 := by
    have hd := Real.cos_two_mul (θ / 2)
    rw [show 2 * (θ / 2) = θ by ring] at hd
    nlinarith [Real.sin_sq_add_cos_sq (θ / 2)]
  rw [Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin]
  simp only [Complex.add_re, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
    Complex.I_re, Complex.I_im, mul_zero, sub_zero, zero_mul, add_zero]
  nlinarith [hcos, hs]

/-! ### The derivative along the circle -/

/-- `d/dθ cLiTwoExt(e^{iθ}) = −i·log(1 − e^{iθ})`. -/
theorem hasDerivAt_cLiTwoExt_exp {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt (fun s : ℝ => QOU.MathlibExt.cLiTwoExt (Complex.exp ((s : ℂ) * Complex.I)))
      (-(Complex.I * Complex.log (1 - Complex.exp ((θ : ℂ) * Complex.I)))) θ := by
  have hz : Complex.exp ((θ : ℂ) * Complex.I) ≠ 0 := Complex.exp_ne_zero _
  have hmem := exp_mem_notCut h0 h2
  -- inner: `θ ↦ e^{iθ}` as a map `ℝ → ℂ`
  have hinner : HasDerivAt (fun s : ℝ => Complex.exp ((s : ℂ) * Complex.I))
      (Complex.I * Complex.exp ((θ : ℂ) * Complex.I)) θ := by
    have hlin : HasDerivAt (fun s : ℝ => ((s : ℂ) * Complex.I)) Complex.I θ := by
      simpa using (Complex.ofRealCLM.hasDerivAt (x := θ)).mul_const Complex.I
    simpa [mul_comm] using (Complex.hasDerivAt_exp _).scomp θ hlin
  have hout := QOU.MathlibExt.hasDerivAt_cLiTwoExt' hmem hz
  have := hout.scomp θ hinner
  -- `-(log(1-z)/z) * (I*z) = -(I * log(1-z))`
  convert this using 1
  rw [smul_eq_mul]
  field_simp

/-- Its imaginary part has derivative `−log(2 sin(θ/2))` — verbatim `Cl₂′`. -/
theorem hasDerivAt_im_cLiTwoExt_exp {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    HasDerivAt
      (fun s : ℝ => (QOU.MathlibExt.cLiTwoExt (Complex.exp ((s : ℂ) * Complex.I))).im)
      (-Real.log (2 * Real.sin (θ / 2))) θ := by
  have h : HasDerivAt
      (fun s : ℝ => (QOU.MathlibExt.cLiTwoExt (Complex.exp ((s : ℂ) * Complex.I))).im)
      ((-(Complex.I * Complex.log (1 - Complex.exp ((θ : ℂ) * Complex.I)))).im) θ := by
    simpa [Function.comp] using
      Complex.imCLM.hasFDerivAt.comp_hasDerivAt θ (hasDerivAt_cLiTwoExt_exp h0 h2)
  -- `Im (-(I * log w)) = -Re (log w) = -log ‖w‖`
  have hre : (-(Complex.I * Complex.log (1 - Complex.exp ((θ : ℂ) * Complex.I)))).im
      = -Real.log ‖1 - Complex.exp ((θ : ℂ) * Complex.I)‖ := by
    simp [Complex.mul_im, Complex.log_re]
  rw [hre] at h
  -- `‖1 - e^{iθ}‖ = 2 sin(θ/2)` on `(0, 2π)`
  have hsin : 0 < Real.sin (θ / 2) :=
    Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith)
  have hnorm : ‖1 - Complex.exp ((θ : ℂ) * Complex.I)‖ = 2 * Real.sin (θ / 2) := by
    have hone : ‖Complex.exp ((((θ - π) / 2 : ℝ) : ℂ) * Complex.I)‖ = 1 := by
      simp [Complex.norm_exp]
    rw [one_sub_exp_mul_I, norm_mul, hone, mul_one, Complex.norm_real, Real.norm_eq_abs,
      abs_of_pos (by linarith : (0:ℝ) < 2 * Real.sin (θ / 2))]
  rwa [hnorm] at h

/-! ### The dilogarithm half of Kummer -/

/-- **`Im cLiTwoExt(e^{iθ}) = Cl₂(θ)` on `(0, 2π)`.**

Same derivative (`−log(2 sin(θ/2))` on both sides) and the same value at `θ = π`,
where `cLiTwoExt(−1) = −π²/12` is real and `Cl₂(π) = 0`. -/
theorem im_cLiTwoExt_exp {θ : ℝ} (h0 : 0 < θ) (h2 : θ < 2 * π) :
    (QOU.MathlibExt.cLiTwoExt (Complex.exp ((θ : ℂ) * Complex.I))).im = Cl_2 θ := by
  set g : ℝ → ℝ := fun s =>
    (QOU.MathlibExt.cLiTwoExt (Complex.exp ((s : ℂ) * Complex.I))).im - Cl_2 s with hg
  have hzero : ∀ s ∈ Set.Ioo (0 : ℝ) (2 * π), HasDerivAt g 0 s := by
    intro s hs
    have h1 := hasDerivAt_im_cLiTwoExt_exp hs.1 hs.2
    have h2' := QOU.Knot.hasDerivAt_Cl_2_series hs.1 hs.2
    simpa using h1.sub h2'
  have hpi : (π : ℝ) ∈ Set.Ioo (0 : ℝ) (2 * π) :=
    ⟨Real.pi_pos, by linarith [Real.pi_pos]⟩
  have hθ : θ ∈ Set.Ioo (0 : ℝ) (2 * π) := ⟨h0, h2⟩
  have hconst := eq_of_hasDerivAt_zero_Ioo hzero hθ hpi
  -- at `θ = π` the point is `-1`
  have hval : g π = 0 := by
    have hneg : Complex.exp (((π : ℝ) : ℂ) * Complex.I) = -1 :=
      Complex.exp_pi_mul_I
    simp only [hg]
    rw [hneg, QOU.Archimedean.cLiTwoExt_neg_one, Cl_2_pi]
    simp [← Complex.ofReal_pow]
  have hzero' : g θ = 0 := by rw [hconst, hval]
  simp only [hg, sub_eq_zero] at hzero'
  exact hzero'

/-- **KUMMER'S IDENTITY ON THE UNIT CIRCLE, both halves.**

For `θ ∈ (0, π)`,

    `BlochWigner_lob(e^{iθ}) = Im cLiTwoExt(e^{iθ}) + log‖e^{iθ}‖ · arg(1 − e^{iθ})`

— the second term vanishing because `‖e^{iθ}‖ = 1`.  This is Route 72's G3
discharged: the corpus's angle-built `BlochWigner_lob` **is** the Bloch–Wigner
dilogarithm on the unit circle.

⚠ Still only on `|z| = 1`.  `|y₁| = 1.5236`, so this does not reach `Vol(5₂)`. -/
theorem kummer_unit_circle {θ : ℝ} (h0 : 0 < θ) (h1 : θ < π) :
    BlochWigner_lob (Complex.exp ((θ : ℂ) * Complex.I))
      = (QOU.MathlibExt.cLiTwoExt (Complex.exp ((θ : ℂ) * Complex.I))).im
        + Real.log ‖Complex.exp ((θ : ℂ) * Complex.I)‖
          * Complex.arg (1 - Complex.exp ((θ : ℂ) * Complex.I)) := by
  have hnorm : ‖Complex.exp ((θ : ℂ) * Complex.I)‖ = 1 := by
    simp [Complex.norm_exp]
  rw [hnorm, Real.log_one, zero_mul, add_zero,
    im_cLiTwoExt_exp h0 (by linarith [Real.pi_pos])]
  exact blochWigner_lob_exp h0 h1

end QOU.Knot.Kummer
