import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:eigenvalue-product-expansion",
  title:
    "Eigenvalue product expansion of the nuclear braid Markov trace",
  lean: { ref: "qou:QOU.BraidKnot.eigenvalue_product_expansion",
    validation: "not_checked",
  },
  uses: ["prop:universal-braid-branching"],
  tags: [
    "eigenvalue-product",
    "markov-trace",
    "symmetric-channel",
    "isospin",
    "crossing-number",
    "q-integer",
  ],
});
