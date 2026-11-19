import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:confinement-grading-correspondence-conditional",
  label: "rem:confinement-grading-correspondence-conditional-witness",
  title: "Upstream-conjecture status, empirical witness, and engine corollary",
  uses: ["thm:confinement-grading-correspondence-conditional"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witnesses: lp-confinement-nf-forcing.witness.json, confined-knot-binding.witness.json, confinement-operator-selection.witness.json.",
    },
  ],
});
