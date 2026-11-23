import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:gram-degeneracy-blocks-connes",
  title: "A Lipschitz seminorm with nonzero kernel has no finite Connes sup",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.lip_kernel_forces_unbounded",
    validation: "not_checked",
  },
  uses: ["prop:markov-gram-star-positive"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The consequence is packaged as\n[finite distance forces a trivial kernel](#cor:finite-connes-forces-trivial-kernel),\nand the quotient is shown to cost nothing by\n[the branching identity](#prop:branching-identity-isospin-weights)." },
  ],
  tags: [
    "connes-distance",
    "spectral-triple",
    "radical",
    "convention-d",
    "trace-convention",
  ],
});
