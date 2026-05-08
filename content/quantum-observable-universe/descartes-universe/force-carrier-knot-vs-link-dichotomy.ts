import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:force-carrier-knot-vs-link-dichotomy",
  title:
    "Knot/link dichotomy of force-carriers — categorical (path-α-Bring)",
  lean: {
    ref: "qou:QOU.Descartes.force_carrier_knot_vs_link_dichotomy",
    validation: "not_checked",
  },
  uses: [
    "prop:force-carrier-bring-uniqueness",
    "prop:torus-embeddable-complete",
    "def:rigid-monoidal-category",
    "def:frobenius-hopf-substrate",
    "rem:hecke-algebra-from-braiding",
  ],
  tags: [
    "force-carrier",
    "matter-vs-force",
    "knot-vs-link",
    "categorical-type",
    "wedderburn-decomposition",
    "hoefsmit-cell-content",
    "higgs-as-linking",
    "open-problem",
  ],
});
