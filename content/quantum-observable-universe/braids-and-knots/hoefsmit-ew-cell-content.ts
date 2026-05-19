import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hoefsmit-ew-cell-content",
  title:
    "Hoefsmit cell-content identification of the EW triplet inside $\\mathrm{End}_R(V^{\\otimes 6})$",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.HoefsmitEWCellContent",
    validation: "not_checked",
  },
  uses: [
    "conj:force-carrier-knot-vs-link-dichotomy",
    "conj:electroweak-higgs-torus-link-triplet",
    "conj:weak-spectral-completeness",
    "prop:knot-operator-lp-selection",
  ],
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
