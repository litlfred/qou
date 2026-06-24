import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:eigenvalue-product-expansion",
  proofs: ["prf:eigenvalue-product-expansion"],
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
