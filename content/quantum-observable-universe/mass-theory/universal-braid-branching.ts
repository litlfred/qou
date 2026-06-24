import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:universal-braid-branching",
  proofs: ["prf:universal-braid-branching"],
  title:
    "Universal braid character formula via Young's lattice branching",
  lean: { ref: "qou:QOU.BraidKnot.universal_braid_branching",
    validation: "not_checked",
  },
  uses: [
    "prop:figure-eight-branching-rule",
    "rem:body-asymptotics-catalog",
  ],
  cites: ["hoefsmit1974", "wenzl1988"],
  tags: [
    "branching-rule",
    "youngs-lattice",
    "universal",
    "borromean",
    "figure-eight",
    "chebyshev",
    "convergence",
  ],
});
