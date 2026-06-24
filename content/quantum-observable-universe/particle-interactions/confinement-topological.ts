import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-topological",
  proofs: ["prf:confinement-topological"],
  title: "Confinement is topological (LP proof)",
  tags: [
    "confinement",
    "topological",
    "linear-programming",
    "gram-matrix",
    "negative-eigenvalue",
    "borromean",
  ],
  lean: { ref: "qou:QOU.Interactions.gram_indefinite_witness",
    validation: "not_checked",
  },
  uses: ["prop:confinement-lp"],
});
