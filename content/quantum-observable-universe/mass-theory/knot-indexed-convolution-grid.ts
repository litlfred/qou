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
    "def:hq-bi-filtration",
    "conj:joint-galois-braid-action",
    "thm:jones-markov-trace",
    "prop:hoefsmit-seminormal-form",
    "def:frobenius-hopf-substrate",
    "prop:vol-through-tau",
    "conj:bring-trilog-depth-3-witness",
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
