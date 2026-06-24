import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:figure-eight-branching-rule",
  proofs: ["prf:figure-eight-branching-rule"],
  title:
    "Figure-eight character from Young's lattice branching multiplicities",
  lean: { ref: "qou:QOU.BraidKnot.figure_eight_branching_rule",
    validation: "not_checked",
  },
  uses: ["prop:hoefsmit-seminormal-form"],
  cites: ["hoefsmit1974"],
  tags: [
    "figure-eight",
    "branching-rule",
    "youngs-lattice",
    "skew-tableaux",
    "frobenius-character",
    "combinatorial",
  ],
});
