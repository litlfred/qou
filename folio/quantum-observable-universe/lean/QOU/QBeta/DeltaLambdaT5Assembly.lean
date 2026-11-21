import QOU.QBeta.DeltaLambdaBindingAssembly
import QOU.QBeta.PhiBSArgumentIdentification

/-!
# T5 partial assembly: S_K = A_ω · κ · (ln²q₀ − ϑ_K²)

Composes the proved binding formula with the channel identity to get the
fully-expanded S-leak as a function of the two open inputs (A_ω, ϑ_K):

    S_K(q₀) = A_ω · cuspModulus · (ln²q₀ − ϑ_K(q₀)²)

where `cuspModulus = √3/4` is the proved geometric datum and
`ϑ_K(q₀) = Im 𝔲_K(q₀)` is the open angular deformation (bean `qou-qnnq`).

## What is proved here (sorry-free)

* `s_channel_expanded` — for any `SDeformedVolumeChannel` whose deformed
  volume is V₄₁ (the figure-eight complex volume), the channel identity
  expands to S(q₀) = A_ω · κ · (Re²u − Im²u). This is pure composition:
  `S_eq` (channel) + `imV₄₁` (cusp geometry).

* `s_channel_at_substrate` — specializes to the substrate meridian: if
  `Re(u(q₀)) = ln q₀`, then S(q₀) = A_ω · κ · (ln²q₀ − ϑ_K²) where
  `ϑ_K = Im(u(q₀))`.

  **`hRe` is an UNDISCHARGED HYPOTHESIS, not a proved fact.** Earlier revisions
  of this docstring attributed it to a lemma `meridian_holonomy_boost`; no such
  declaration exists anywhere in the corpus, and the attribution propagated into
  a bean and a probe docstring before it was caught (PR #4513, bean `qou-5nze`).
  Nothing below establishes `hRe`; it is assumed wherever it appears.

  The one corpus object that could discharge it does not: the substrate-matched
  Murakami meridian (`Knot.DeformedMeridianWinding`) has real part `N·ln q₀`,
  so `hRe` would force the degenerate colour `N = 1`, and the resulting
  quantization `Im u = −2πk` is refuted by the measured anchor signs. Proved
  sorry-free in `QOU.QBeta.ChannelMeridianIdentification`; that file also proves
  the channel class constrains `u` not at all.

## What is honestly open (beans, not sorries)

* **A_ω** — the Stokes constant. Carried as a class field in
  `SDeformedVolumeChannel`. For 4₁, GGM gives A_ω = 3.
  Uniqueness: conditional on `FaddeevPhiPhysical` class axioms (merged).

* **ϑ_K(q₀)** — the angular deformation. Carried as `Im(u(q₀))`.
  Source: G3 monodromy datum on the SL₂(ℂ) character variety of K.
  Bean `qou-qnnq`.

* **V = V₄₁** — the channel uses the figure-eight complex volume.
  Carried as the hypothesis `hV`.

-- Ref: [leitner2026] docs/coordination/delta-lambda-magnitude-derivation.md — T5
-- Ref: [garoufalidis-gu-marino2021] GGM 2012.00062
-/

open QOU.Knot.FigureEightComplexVolume
open QOU.QBeta.DeltaLambdaBindingAssembly
open QOU.QBeta.PhiBSArgumentIdentification

namespace QOU.QBeta.DeltaLambdaT5Assembly

/-- **T5 expanded channel formula.** For any `SDeformedVolumeChannel` whose
complex volume is V₄₁, the S-leak expands to `A_ω · κ · (Re²u − Im²u)`.
This is the composition of the channel identity with the cusp geometry. -/
theorem s_channel_expanded {S : ℝ → ℝ} [ch : SDeformedVolumeChannel S]
    (hV : ch.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀) :
    S q₀ = ch.A_ω * cuspModulus * ((ch.u q₀).re ^ 2 - (ch.u q₀).im ^ 2) := by
  have h1 := ch.S_eq q₀ hq
  rw [h1, hV]
  exact binding_formula_of_imV₄₁ ch.A_ω (ch.u q₀)

/-- **T5 at substrate: S = A_ω · κ · (ln²q₀ − ϑ²).** For a channel whose
deformation map `u` has `Re(u(q₀)) = ln q₀` (`hRe` — an ASSUMPTION on the
channel, not a proved fact; see the module docstring) and `Im(u(q₀)) = ϑ` (the
open angular deformation), the S-leak becomes the explicit two-parameter
formula.

This is the **derive-then-check target**: everything except A_ω and ϑ_K is
derived from geometry. The T4 crux probe verified that A_ω = 3 + this formula
reproduces both anchor S values with real ϑ_K. -/
theorem s_channel_at_substrate {S : ℝ → ℝ} [ch : SDeformedVolumeChannel S]
    (hV : ch.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀)
    (hRe : (ch.u q₀).re = Real.log q₀)
    {ϑ : ℝ} (hIm : (ch.u q₀).im = ϑ) :
    S q₀ = ch.A_ω * cuspModulus * (Real.log q₀ ^ 2 - ϑ ^ 2) := by
  rw [s_channel_expanded hV hq, hRe, hIm]

/-- **T5 sign characterization.** Under the substrate specialization: S > 0
iff |ϑ_K| < |ln q₀| (boost-dominated, muon-type), S < 0 iff |ϑ_K| > |ln q₀|
(spin-dominated, proton-type). Conditional on A_ω > 0. -/
theorem s_channel_sign_pos {S : ℝ → ℝ} [ch : SDeformedVolumeChannel S]
    (hV : ch.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀)
    (hA : 0 < ch.A_ω)
    (hRe : (ch.u q₀).re = Real.log q₀)
    {ϑ : ℝ} (hIm : (ch.u q₀).im = ϑ)
    (hboost : ϑ ^ 2 < Real.log q₀ ^ 2) :
    0 < S q₀ := by
  rw [s_channel_at_substrate hV hq hRe hIm]
  apply mul_pos (mul_pos hA cuspModulus_pos)
  linarith

theorem s_channel_sign_neg {S : ℝ → ℝ} [ch : SDeformedVolumeChannel S]
    (hV : ch.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀)
    (hA : 0 < ch.A_ω)
    (hRe : (ch.u q₀).re = Real.log q₀)
    {ϑ : ℝ} (hIm : (ch.u q₀).im = ϑ)
    (hspin : Real.log q₀ ^ 2 < ϑ ^ 2) :
    S q₀ < 0 := by
  rw [s_channel_at_substrate hV hq hRe hIm]
  apply mul_neg_of_pos_of_neg (mul_pos hA cuspModulus_pos)
  linarith

/-- **T5 boost-spin critical balance (`qou-w49j`).** At the critical angular
threshold `ϑ² = (ln q₀)²`, the substrate S-channel vanishes identically (`S q₀ = 0`). -/
theorem s_channel_eq_zero_of_sq_eq {S : ℝ → ℝ} [ch : SDeformedVolumeChannel S]
    (hV : ch.V = V₄₁) {q₀ : ℝ} (hq : 1 < q₀)
    (hRe : (ch.u q₀).re = Real.log q₀)
    {ϑ : ℝ} (hIm : (ch.u q₀).im = ϑ)
    (hcrit : ϑ ^ 2 = Real.log q₀ ^ 2) :
    S q₀ = 0 := by
  rw [s_channel_at_substrate hV hq hRe hIm, hcrit, sub_self, mul_zero]

end QOU.QBeta.DeltaLambdaT5Assembly
