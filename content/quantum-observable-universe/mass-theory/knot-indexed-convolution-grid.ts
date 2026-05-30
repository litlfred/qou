import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-indexed-convolution-grid",
  title:
    "Placement of paper's existing knot-indexed convolutions in the bi-filtration grid",
  lean: {
    ref: "qou:QOU.BraidKnot.KnotIndexedConvolutionGrid.grid_placement",
    validation: "not_checked",
  },
  uses: [
    "conj:joint-galois-braid-action",
    "prop:vol-through-tau",
  ],
  cites: [],
  tags: [
    "bi-filtration",
    "knot-indexed-convolution",
    "placement-table",
    "categorical-linking",
    "EW-interface-knot",
    "graded-mikusinski",
  ],
});
