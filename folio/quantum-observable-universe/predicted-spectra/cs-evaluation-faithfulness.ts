import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). Faithfulness is a statement *across* the wall, " +
        "which is why the $\\mathbb{R}$ cannot be removed from it. " +
        "`QOU.Archimedean.CSEvaluationFaithful.faithful` reads " +
        "`Nonempty (ylc.obstructionClass n) → vtd.levelContribution n ≠ 0`: " +
        "the hypothesis is categorical and already generic — " +
        "`QOU.Torsion.YekutieliLiftingCondition` and its obstruction classes " +
        "carry no ring at all — while the conclusion is the non-vanishing of " +
        "a real Chern–Simons period. The proposition's content *is* that " +
        "pairing: a substrate-side obstruction is detected by an archimedean " +
        "evaluation. Restating it over a `CommRing` would erase the half that " +
        "makes it a faithfulness claim rather than a tautology about " +
        "obstruction classes.\n\n" +
        "The real side is inherited, not introduced here: it arrives through " +
        "`VolumeTowerDecomposition` (`prop:volume-tower-decomposition`), whose " +
        "`levelContribution : ℕ → ℝ` is constrained by `Summable` and " +
        "`HasSum` against a positive real `totalVolume`. The shared file " +
        "`QOU/Archimedean/HyperbolicVolumeTranscendence.lean` supplies those " +
        "volumes as analytic constants — `vol_4_1` " +
        "$= 2\\,\\mathrm{Cl}_2(\\pi/3)$, `vol_B3` $= 8G$ with $G$ Catalan's " +
        "constant as a `tsum` — so the non-vanishing asserted by `faithful` " +
        "is non-vanishing of a real number, not of a ring element. " +
        "`infinitely_many_nonzero`, the one theorem proved from the " +
        "structure, is pure logic over that data and inherits the same " +
        "placement.",
      see: "folio/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicVolumeTranscendence.lean",
    },
  ],
  label: "prop:cs-evaluation-faithfulness",
  title:
    "Faithfulness of the Chern--Simons evaluation on the brane tower",
  tags: [
    "chern-simons",
    "yekutieli",
    "faithfulness",
    "obstruction",
    "brane-tower",
  ],
  uses: [
    "prop:volume-tower-decomposition",
    "prop:yekutieli-lifting",
  ],
  lean: { ref: "qou:QOU.Archimedean.CSEvaluationFaithful",
    validation: "not_checked",
  },
});
