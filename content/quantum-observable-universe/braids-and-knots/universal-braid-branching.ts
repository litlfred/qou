import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:universal-braid-branching",
  title:
    "Universal braid character formula via Young's lattice branching",
  lean: {
    decl: "QOU.BraidKnot.universal_braid_branching",
    validation: "not_checked",
  },
  uses: [
    "prop:hoefsmit-seminormal-form",
    "prop:figure-eight-branching-rule",
    "def:hecke-algebra",
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
