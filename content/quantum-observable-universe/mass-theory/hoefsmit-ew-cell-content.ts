import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-ew-cell-content",
  title:
    "Hoefsmit cell-content identification of the EW triplet inside $\\mathrm{End}_R(V^{\\otimes 6})$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.HoefsmitEWCellContent",
    validation: "not_checked",
  },
  uses: ["prop:knot-operator-lp-selection"],
  tags: [
    "hoefsmit",
    "cell-content",
    "seminormal-form",
    "wedderburn-decomposition",
    "electroweak",
    "ew-triplet",
    "disjoint-strand-pair",
    "non-uniform-plancherel",
    "n-six",
  ],
});
