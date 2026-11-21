import QOU.Knot.WhiteheadInnerGaussianProof
import QOU.Knot.WhiteheadLemma4Reduction
import QOU.Knot.WhiteheadMajorantRate
import QOU.Knot.WhiteheadLemma1RootOfUnity

/-!
# The Whitehead-link volume conjecture, unconditional

`WhiteheadInnerGaussianProof` proves `WhiteheadInnerGaussianModel` (van der Veen
Lemma 2a/2b in weighted L¹ form). `WhiteheadOuterGaussianWindow` turns it into
`WhiteheadOuterGaussianModel`, and `vdVWhiteheadLemma4_of_gaussianModel` turns
that into `VdVWhiteheadLemma4` (van der Veen Lemma 4). With the majorant rate
(`tendsto_log_whiteheadLinkMajorant_vol`), `whiteheadLink_volume_of_lemma4`
gives the volume limit with no hypothesis left:

    (2π/N) · log ‖J_N(W)‖ → Vol(W) = 4·Cl₂(π/2).

Here `J_N(W)` is the Kashaev invariant `whiteheadLinkKashaev`, and the target is
`Vol_Borromean / 2`.

-- Ref: [manuscript] library/arxiv-math-0611181v2/0611181v2.pdf, Lemmas 2 and 4
-/

namespace QOU.Knot.FigureEightVolume

/-- **van der Veen's Lemma 4 for the Whitehead link, unconditional.** -/
instance vdVWhiteheadLemma4_holds : VdVWhiteheadLemma4 :=
  vdVWhiteheadLemma4_of_gaussianModel

/-- **The volume conjecture for the Whitehead link `5²₁`.** No hypotheses. -/
theorem whiteheadLink_volume_conjecture :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) * Real.log ‖whiteheadLinkKashaev N‖)
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) :=
  whiteheadLink_volume_of_lemma4

/-- The same limit stated on vdV's generic-`t` tangle formula, evaluated at
    `t = e^{2πi/N}`.  The root-of-unity evaluation is derived, not cited
    (`vdvWhiteheadLinkJones_at_kashaev_point`); what remains cited is the
    tangle formula itself (Zheng's tangle functions and multiplicativity). -/
theorem whiteheadLink_volume_conjecture_tangle :
    Filter.Tendsto
      (fun N : ℕ => (2 * Real.pi / N) *
        Real.log ‖vdvWhiteheadLinkJones (Complex.exp (((Real.pi / N : ℝ) : ℂ) * Complex.I)) N‖)
      Filter.atTop (nhds (QOU.Archimedean.Vol_Borromean / 2)) := by
  refine whiteheadLink_volume_conjecture.congr' ?_
  filter_upwards [Filter.eventually_ge_atTop 1] with N hN
  rw [vdvWhiteheadLinkJones_at_kashaev_point hN]

end QOU.Knot.FigureEightVolume
