import { remark } from "../../schema/builders";

export default remark({
  label: "rem:Q-value-transition-properties",
  interprets: "def:Q-value-transition",
  title:
    "Crossing-level decomposition, the $q$-anomaly, and non-conservation of $\\mathcal{Q}_q$",
  tags: [
    "q-value",
    "transition-energy",
    "beta-decay",
    "crossing-change",
    "recoil",
    "kinetic-energy",
    "skein",
    "q-anomaly",
  ],
  uses: [
    "def:Q-value-transition",
    "conj:q-integer-mass-formula",
    "prop:nuclear-groebner-reduction",
    "prop:hadron-q-self-correction",
    "def:q-momentum",
  ],
});
