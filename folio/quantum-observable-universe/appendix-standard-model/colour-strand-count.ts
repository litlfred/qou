import { proposition } from "../../schema/builders";

/**
 * With five strands, a complex non-abelian colour block and a non-abelian weak block
 * force the split 3 + 2.
 */
export default proposition({
  label: "prop:colour-strand-count",
  title: "Three colour strands from complex colour and a weak doublet",
  uses: ["prop:strand-count-from-bring", "prop:hypercharge-sign-is-bring-orientation"],
  lean: {
    ref: "qou:QOU.StandardModel.ColourCount.colour_weak_split",
  },
  tags: ["appendix", "standard-model"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-28",
      body:
        "Sorry-free (`ColourStrandCount.lean`), conditional on two labelled inputs: colour " +
        "is non-abelian and complex type, and the weak block carries a doublet. Neither " +
        "input is derived from the braid or Bring structure yet. Bean qou-h0zz.",
    },
  ],
});
