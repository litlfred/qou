import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:toffoli-lp-stability",
  title:
    "LP-dual stability of the $q$-Toffoli braid and the golden-ratio threshold",
  tags: [
    "toffoli",
    "lp-duality",
    "stability",
    "gram-matrix",
    "golden-ratio",
    "substrate-q",
    "hecke-algebra",
    "q-AND",
  ],
  lean: { ref: "qou:QOU.Information.toffoli_lp_stable",
    validation: "not_checked",
  },
  uses: [
    "prop:toffoli-transfer-matrix",
    "prop:lp-dual-stability",
    "def:hecke-mass-element",
  ],
});
