import { remark } from "../../schema/builders";

export default remark({
  label: "rem:habiro-precision-ladder-equivalence-context",
  title: "Verified proton coefficients, uniqueness, and scope of the Habiro precision-ladder evaluation",
  interprets: "prop:habiro-precision-ladder-equivalence",
  tags: ["habiro", "precision-ladder", "markov-trace", "archimedean"],
  uses: ["prop:habiro-precision-ladder-equivalence"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational witness: computations/habiro/habiro-coefficients-atomic.witness.json.",
    },
  ],
});
