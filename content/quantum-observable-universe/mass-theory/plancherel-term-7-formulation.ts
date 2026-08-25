import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:plancherel-term-7-formulation",
  title:
    "Universal residue at curvature-rank $k \\geq 4$ (q-deformed Wedderburn-weighted log functional)",
  lean: {
    ref: "qou:QOU.WedderburnMass.plancherel_term_7",
    validation: "not_checked",
  },
  uses: [
    "prop:spectral-sequence-collapse",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `mass-theory/plancherel-term-7-formulation.lean` " +
        "uses `Real.exp`, `Real.log`. These are real-analytic constructs " +
        "with no generic-`CommRing` counterpart, so the `ℝ` " +
        "specialisation is forced by the statement itself rather than " +
        "chosen. The block therefore sits on the archimedean side of the " +
        "§7c wall by construction.",
    },
  ],
});
