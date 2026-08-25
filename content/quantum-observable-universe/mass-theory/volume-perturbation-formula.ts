import { proposition } from "../../schema/builders";
export default proposition({
  label: "prop:volume-perturbation-formula",
  title: "Volume perturbation: $\\delta\\Phi_k = z^2 \\cdot \\mathrm{Vol}(4_1) \\cdot [k{-}3]_q$",
  lean: { ref: "qou:QOU.BraidKnot.volume_perturbation", validation: "not_checked" },
  uses: ["prop:hecke-convergence-bound"],
  tags: ["volume-perturbation", "figure-eight", "markov-parameter", "jet-level"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/BraidKnot/volume_perturbation.lean` " +
        "uses `Real.sqrt`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
