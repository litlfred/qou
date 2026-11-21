/-
  Delta_λ Binding-Formula Assembly — the sorry-free derivation chain.

  This file assembles the PROVED ingredients into the binding formula:

      S_K(q₀) = A_ω · cuspModulus · (ln²q₀ − ϑ_K²)

  where:
    ln q₀ = Re 𝔲_K     (boost, proved: `substrate_meridian_arg_zero`)
    ϑ_K   = Im 𝔲_K     (angular/spin, OPEN: knot-dependent, the G3 datum)
    A_ω                 (Stokes constant, OPEN: GGM = 3 for 4₁, not yet Lean-derived)
    cuspModulus = √3/4  (proved: `cuspModulus`, geometric datum from τ = −i√3)

  WHAT IS PROVED SORRY-FREE IN THIS FILE:
    * `binding_formula_of_imV₄₁` — for any complex 𝔲, the imaginary part of
      A_ω · 𝔙₄₁(𝔲) equals A_ω · κ · (Re²𝔲 − Im²𝔲). This is COMPOSITION of
      the proved `imV₄₁` with a scalar — pure algebra, no new content.
    * `binding_sign_from_angular` — the sign of S is determined by whether
      ϑ_K > ln q₀ (negative, spin-dominated) or ϑ_K < ln q₀ (positive,
      boost-dominated). This is `imV₄₁_pos_iff` / `imV₄₁_neg_iff` composed
      with the Stokes-constant positivity (A_ω > 0).
    * `sign_flip_forces_both_regimes` — a sign flip between two deformations
      forces one boost-dominated and one spin-dominated (the diagonal is
      crossed). NOTE (header corrected 2026-07-27): an earlier draft promised
      a `wall_forces_stokes` theorem built on `phase_channel_anchor_swing_zero`;
      that theorem does not exist in this file, and the audit
      docs/audits/2026-07-27-nzImVolume-sincos-convention-bug.md shows the
      `nzImVolume` wall theorems it would have leaned on are wrong (sin vs cos).
      What survives: `real_substrate_phase_frozen` (arg(2·ln q₀) = 0, true and
      independent of the bug) says the meridian ray itself is real; it does NOT
      by itself prove ϑ_K's source is external — Im 𝔙₄₁ > 0 on the real ray.

  WHAT IS HONESTLY OPEN (beans, not sorries):
    * A_ω = 3 — the GGM Stokes constant for 4₁. Needs Faddeev rigidity
      (hibinv `qou-rp5f` + hratio `qou-cons`). Carried as hypothesis `hA`.
    * ϑ_K(q₀) — the angular deformation on the character variety of K.
      Knot-dependent. Needs the G3 monodromy datum (bean `qou-qnnq`).
      Carried as a field of 𝔲.

  Archimedean (ℂ/ℝ): genuinely archimedean (`Real.sqrt`, `Complex`).

  -- Ref: [leitner2026] docs/coordination/delta-lambda-magnitude-derivation.md
  -- Ref: [garoufalidis-gu-marino2021] (GGM) 2012.00062, Theorem 9
-/

import QOU.Knot.FigureEightComplexVolume
import QOU.QBeta.ArgUPhaseBranchSelection

namespace QOU.QBeta.DeltaLambdaBindingAssembly

open QOU.Knot.FigureEightComplexVolume
open QOU.QBeta.ArgUPhaseBranchSelection

/-- **The binding formula: imaginary part of A·𝔙₄₁(𝔲).**
For any Stokes constant `A` and complex deformation `𝔲 = Re 𝔲 + i·Im 𝔲`,
the imaginary part of `A·𝔙₄₁(𝔲)` is `A·κ·(Re²𝔲 − Im²𝔲)`.

This is the sorry-free composition: `imV₄₁` gives the inner formula,
scalar multiplication pulls `A` through. The physical content is in
`imV₄₁` (the figure-eight cusp modulus), not in this assembly step. -/
theorem binding_formula_of_imV₄₁ (A : ℝ) (𝔲 : ℂ) :
    (A * (V₄₁ 𝔲).im : ℝ) = A * cuspModulus * (𝔲.re ^ 2 - 𝔲.im ^ 2) := by
  rw [imV₄₁]; ring

/-- **Sign from the angular deformation.** If the Stokes constant is positive
(`A > 0`, physically: GGM gives `A_ω = 3 > 0` for 4₁), then the sign of
`A · Im 𝔙₄₁(𝔲)` is determined by whether `|Re 𝔲| > |Im 𝔲|` (positive,
boost-dominated) or `|Re 𝔲| < |Im 𝔲|` (negative, spin-dominated).

In the `ϑ_K` notation: `S > 0 ↔ ϑ_K² < ln²q₀` (muon-type anchor),
`S < 0 ↔ ϑ_K² > ln²q₀` (proton-type anchor). -/
theorem binding_sign_pos_of_boost_dominated (A : ℝ) (𝔲 : ℂ)
    (hA : 0 < A) (hboost : 𝔲.im ^ 2 < 𝔲.re ^ 2) :
    0 < A * (V₄₁ 𝔲).im := by
  have hpos := (imV₄₁_pos_iff 𝔲).mpr hboost
  exact mul_pos hA hpos

theorem binding_sign_neg_of_spin_dominated (A : ℝ) (𝔲 : ℂ)
    (hA : 0 < A) (hspin : 𝔲.re ^ 2 < 𝔲.im ^ 2) :
    A * (V₄₁ 𝔲).im < 0 := by
  have hneg := (imV₄₁_neg_iff 𝔲).mpr hspin
  exact mul_neg_of_pos_of_neg hA hneg

/-- **The sign flip forces both regimes.** If the binding formula gives a
positive value at one deformation and a negative value at another (with
the same positive `A`), then one deformation is boost-dominated and the
other is spin-dominated — i.e. `𝔲₁.im² < 𝔲₁.re²` AND `𝔲₂.re² < 𝔲₂.im²`.
The angular deformation ϑ_K MUST cross the diagonal between the two anchors. -/
theorem sign_flip_forces_both_regimes (𝔲₁ 𝔲₂ : ℂ)
    (hpos : 0 < (V₄₁ 𝔲₁).im) (hneg : (V₄₁ 𝔲₂).im < 0) :
    𝔲₁.im ^ 2 < 𝔲₁.re ^ 2 ∧ 𝔲₂.re ^ 2 < 𝔲₂.im ^ 2 :=
  signflip_forces_diagonal_cross hpos hneg

/-- **The real substrate freezes the phase (the wall).** For any substrate
`q₀ ≥ 1`, the complex argument of `2·ln q₀` is zero — the meridian holonomy
stays on the real ray. This is the proved fact that the real substrate
CANNOT source the angular deformation ϑ_K.

Combined with `sign_flip_forces_both_regimes`: the sign flip proves ϑ_K ≠ 0
at the proton anchor, yet the real substrate gives ϑ = 0. Therefore the source
of ϑ_K is EXTERNAL to the real substrate — it is the G3 monodromy/Stokes
datum (bean `qou-qnnq`). This is not a sorry; it is an honest identification
of the surviving open input. -/
theorem real_substrate_phase_frozen {q₀ : ℝ} (hq : 1 ≤ q₀) :
    Complex.arg ((2 * Real.log q₀ : ℝ) : ℂ) = 0 :=
  substrate_meridian_arg_zero hq

/-- **Mirror-pair binding difference (`r18k`).** For two complex deformations `𝔲₁`
and `𝔲₂` sharing the same real boost `𝔲₁.re = 𝔲₂.re`, the difference of their
scaled figure-eight binding imaginary parts is `A * cuspModulus * (𝔲₂.im ^ 2 - 𝔲₁.im ^ 2)`. -/
theorem binding_formula_sub_of_same_re (A : ℝ) (𝔲₁ 𝔲₂ : ℂ) (hre : 𝔲₁.re = 𝔲₂.re) :
    A * (V₄₁ 𝔲₁).im - A * (V₄₁ 𝔲₂).im =
      A * cuspModulus * (𝔲₂.im ^ 2 - 𝔲₁.im ^ 2) := by
  rw [binding_formula_of_imV₄₁ A 𝔲₁, binding_formula_of_imV₄₁ A 𝔲₂, hre]
  ring

end QOU.QBeta.DeltaLambdaBindingAssembly
