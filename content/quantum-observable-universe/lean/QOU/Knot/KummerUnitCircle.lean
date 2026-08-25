/-
  Kummer's identity on the unit circle: `D(e^{iθ}) = Cl₂(θ)`.

  Bean `qou-kmmr`, first increment.

  ═══ CONTEXT ═══

  `QOU/Archimedean/BlochWignerLobachevsky.lean` *defines*

      BlochWigner_lob z := Λ(arg z) + Λ(arg(1/(1−z))) + Λ(arg(1 − 1/z))

  and correctly **forbids** transporting dilogarithm facts onto that symbol,
  because the identity relating it to `Im Li₂(z) + log|z|·arg(1−z)` — Kummer's
  identity — is a theorem the corpus has not proved.

  ═══ WHAT THIS FILE PROVES ═══

  Kummer **on the unit circle**, which is where it collapses to something
  elementary.  For `θ ∈ (0, π)` the three tetrahedron angles of `z = e^{iθ}` are

      (θ, (π−θ)/2, (π−θ)/2)

  — an *isosceles* ideal tetrahedron — so the Λ-sum is `Λ(θ) + 2Λ((π−θ)/2)`, and
  that equals `Cl₂(θ)` by the Clausen duplication formula the corpus already has
  (`Cl_2_duplication`).  Since `log|z| = 0` on the unit circle, the dilogarithm
  side of Kummer reduces to `Im Li₂(e^{iθ})`, classically `Cl₂(θ)`.

  So on `|z| = 1`, **Kummer's identity is exactly Clausen duplication**.  That is
  the content of this file, and it is why the unit circle is the cheap case.

  ═══ WHAT IS NOT PROVED ═══

  * **General `z`.**  Off the unit circle the angles are no longer isosceles and
    `log|z| ≠ 0`; the identity genuinely needs a two-variable argument
    (`dD = log|z| d arg(1−z) − log|1−z| d arg z` against
    `dΛ(θ) = −log|2 sin θ| dθ`).  Nothing here does that.  **The 5₂ shape
    `y₁` has `|y₁| = 1.5236 ≠ 1`, so this file does not reach `Vol(5₂)`.**
  * ~~`Im Li₂(e^{iθ}) = Cl₂(θ)` for the corpus's `cLiTwoExt`.~~  **Done** —
    `QOU/Knot/KummerDilogHalf.lean` (`im_cLiTwoExt_exp`), which combines with
    `blochWigner_lob_exp` below into `kummer_unit_circle`: the two halves of
    Kummer now meet on `|z| = 1`.  This file still proves only the Λ-side, and
    still states its own conclusion in terms of `Cl₂` alone — that separation is
    deliberate, not stale.

  So what is delivered is the **geometric** side on `|z| = 1`, stated in terms of
  `Cl₂` alone, with no dilogarithm claim.


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

  -- Ref: [zagier1986], [milnor1982], [thurston1978]
-/
import QOU.Archimedean.BlochWignerLobachevsky
import Mathlib.Analysis.SpecialFunctions.Complex.Arg

namespace QOU.Knot.Kummer

open Real Complex QOU.Archimedean

/-! ### The unit-circle geometry -/

/-- `arg (e^{iθ}) = θ` on `(−π, π]`. -/
theorem arg_exp_mul_I {θ : ℝ} (h : θ ∈ Set.Ioc (-π) π) :
    Complex.arg (Complex.exp ((θ : ℂ) * Complex.I)) = θ := by
  rw [Complex.exp_mul_I]
  simpa using Complex.arg_cos_add_sin_mul_I h

/-- **The half-angle factorisation.**  `1 − e^{iθ} = 2 sin(θ/2) · e^{i(θ−π)/2}`.

This is the whole geometric content: the modulus `2 sin(θ/2)` is positive on
`(0, 2π)` and the phase `(θ−π)/2` lands in `(−π/2, 0)`, so the argument of
`1 − e^{iθ}` is `(θ−π)/2` on the nose, with no branch ambiguity. -/
theorem one_sub_exp_mul_I (θ : ℝ) :
    1 - Complex.exp ((θ : ℂ) * Complex.I)
      = ((2 * Real.sin (θ / 2) : ℝ) : ℂ)
        * Complex.exp ((((θ - π) / 2 : ℝ) : ℂ) * Complex.I) := by
  have hc : Real.cos ((θ - π) / 2) = Real.sin (θ / 2) := by
    rw [show (θ - π) / 2 = θ / 2 - π / 2 by ring, Real.cos_sub_pi_div_two]
  have hs : Real.sin ((θ - π) / 2) = -Real.cos (θ / 2) := by
    rw [show (θ - π) / 2 = θ / 2 - π / 2 by ring, Real.sin_sub_pi_div_two]
  have hcos : Real.cos θ = 1 - 2 * Real.sin (θ / 2) ^ 2 := by
    have h2 := Real.cos_two_mul (θ / 2)
    rw [show 2 * (θ / 2) = θ by ring] at h2
    nlinarith [Real.sin_sq_add_cos_sq (θ / 2)]
  have hsin : Real.sin θ = 2 * Real.sin (θ / 2) * Real.cos (θ / 2) := by
    have h2 := Real.sin_two_mul (θ / 2)
    rw [show 2 * (θ / 2) = θ by ring] at h2
    exact h2
  rw [Complex.exp_mul_I, Complex.exp_mul_I, ← Complex.ofReal_cos, ← Complex.ofReal_sin,
    ← Complex.ofReal_cos, ← Complex.ofReal_sin, hc, hs, hcos, hsin]
  push_cast
  ring

/-- `arg (1 − e^{iθ}) = (θ − π)/2` for `θ ∈ (0, π)`. -/
theorem arg_one_sub_exp {θ : ℝ} (h0 : 0 < θ) (h1 : θ < π) :
    Complex.arg (1 - Complex.exp ((θ : ℂ) * Complex.I)) = (θ - π) / 2 := by
  have hpos : 0 < 2 * Real.sin (θ / 2) := by
    have : 0 < Real.sin (θ / 2) :=
      Real.sin_pos_of_pos_of_lt_pi (by linarith) (by linarith [Real.pi_pos])
    linarith
  rw [one_sub_exp_mul_I, Complex.arg_real_mul _ hpos]
  exact arg_exp_mul_I ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩

/-! ### The three tetrahedron angles on the unit circle -/

theorem tetAngle₁_exp {θ : ℝ} (h0 : 0 < θ) (h1 : θ < π) :
    tetAngle₁ (Complex.exp ((θ : ℂ) * Complex.I)) = θ :=
  arg_exp_mul_I ⟨by linarith [Real.pi_pos], le_of_lt h1⟩

theorem tetAngle₂_exp {θ : ℝ} (h0 : 0 < θ) (h1 : θ < π) :
    tetAngle₂ (Complex.exp ((θ : ℂ) * Complex.I)) = (π - θ) / 2 := by
  unfold tetAngle₂
  have harg := arg_one_sub_exp h0 h1
  have hne : Complex.arg (1 - Complex.exp ((θ : ℂ) * Complex.I)) ≠ π := by
    rw [harg]; intro h; linarith [Real.pi_pos]
  rw [one_div, Complex.arg_inv, if_neg hne, harg]
  ring

theorem tetAngle₃_exp {θ : ℝ} (h0 : 0 < θ) (h1 : θ < π) :
    tetAngle₃ (Complex.exp ((θ : ℂ) * Complex.I)) = (π - θ) / 2 := by
  unfold tetAngle₃
  have hz : Complex.exp ((θ : ℂ) * Complex.I) ≠ 0 := Complex.exp_ne_zero _
  have hinv : 1 - 1 / Complex.exp ((θ : ℂ) * Complex.I)
      = (starRingEnd ℂ) (1 - Complex.exp ((θ : ℂ) * Complex.I)) := by
    rw [map_sub, map_one, ← Complex.exp_conj]
    simp [Complex.conj_ofReal, Complex.exp_neg]
  have harg := arg_one_sub_exp h0 h1
  have hne : Complex.arg (1 - Complex.exp ((θ : ℂ) * Complex.I)) ≠ π := by
    rw [harg]; intro h; linarith [Real.pi_pos]
  rw [hinv, Complex.arg_conj, if_neg hne, harg]
  ring

/-! ### Kummer on the unit circle -/

/-- **The Λ-identity behind it**: `Λ(θ) + 2Λ((π−θ)/2) = Cl₂(θ)`.

Immediate from `Cl_2_duplication`, since `Λ(t) = Cl₂(2t)/2`:
`Cl₂(2θ)/2 + Cl₂(π−θ) = Cl₂(θ)` is the duplication formula halved. -/
theorem Lob_add_two_Lob (θ : ℝ) :
    Lob θ + 2 * Lob ((π - θ) / 2) = Cl_2 θ := by
  have hdup := Cl_2_duplication θ
  unfold Lob
  rw [show 2 * ((π - θ) / 2) = π - θ by ring]
  linarith

/-- **KUMMER'S IDENTITY ON THE UNIT CIRCLE.**

For `θ ∈ (0, π)`, the Bloch–Wigner Λ-sum at `z = e^{iθ}` is `Cl₂(θ)`.

The tetrahedron is *isosceles* — angles `(θ, (π−θ)/2, (π−θ)/2)` — and the
identity is exactly Clausen duplication.

⚠ This is the Λ-side only, and only on `|z| = 1`.  It makes no claim about
`Im Li₂` — for that, and for the two halves combined, see
`QOU/Knot/KummerDilogHalf.lean`.  Neither reaches the 5₂ shape, which has
`|y₁| = 1.52`. -/
theorem blochWigner_lob_exp {θ : ℝ} (h0 : 0 < θ) (h1 : θ < π) :
    BlochWigner_lob (Complex.exp ((θ : ℂ) * Complex.I)) = Cl_2 θ := by
  unfold BlochWigner_lob
  rw [tetAngle₁_exp h0 h1, tetAngle₂_exp h0 h1, tetAngle₃_exp h0 h1]
  have := Lob_add_two_Lob θ
  linarith

/-- The angles really do sum to `π`, as `tetAngles_sum_eq_pi` requires — recorded
as an independent check that the three computations above are mutually
consistent rather than three separate slips. -/
theorem tetAngles_exp_sum {θ : ℝ} (h0 : 0 < θ) (h1 : θ < π) :
    tetAngle₁ (Complex.exp ((θ : ℂ) * Complex.I))
      + tetAngle₂ (Complex.exp ((θ : ℂ) * Complex.I))
      + tetAngle₃ (Complex.exp ((θ : ℂ) * Complex.I)) = π := by
  rw [tetAngle₁_exp h0 h1, tetAngle₂_exp h0 h1, tetAngle₃_exp h0 h1]; ring

end QOU.Knot.Kummer
