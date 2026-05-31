import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hoefsmit-ew-cell-content",
  title:
    "Hoefsmit cell-content identification of the EW triplet inside $\\mathrm{End}_R(V^{\\otimes 6})$ (categorical existence)",
  lean: {
    ref: "qou:QOU.IwahoriHecke.Hoefsmit.HoefsmitSeminormalBasis",
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
    "closure-tier-b",
    "phase-2-sprint-5-discharge",
  ],
});
