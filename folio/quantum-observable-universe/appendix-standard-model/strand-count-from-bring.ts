import { proposition } from "../../schema/builders";

/**
 * Conditional: if strand relabellings are Bring's symmetries (S5), there are five
 * strands; with three colour strands, two are isospin. Agrees with oddness.
 */
export default proposition({
  label: "prop:strand-count-from-bring",
  title: "Five strands if strand relabellings are Bring's symmetries",
  uses: ["prop:odd-strands-force-chirality", "def:color-tube-coordinates"],
  lean: {
    ref: "qou:QOU.StandardModel.StrandCount.strandCount_eq_five",
  },
  tags: ["appendix", "standard-model", "brings-surface"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`StrandCountFromBring.lean`), conditional on the hypothesis " +
        "that strand relabellings are Bring's S5 symmetries; that hypothesis and the " +
        "three colour strands are not derived. Bean qou-h0zz.",
    },
  ],
});
