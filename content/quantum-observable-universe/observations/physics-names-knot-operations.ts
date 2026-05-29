import { remark } from "../../schema/builders";

export default remark({
  label: "rem:physics-names-knot-operations",
  title: "Physics names $\\leftrightarrow$ categorical knot operations (table; depends on $q_0$)",
  interprets: "prop:confinement-categorical",
  uses: [
    "rem:borromean-baryon-interpretation",
    "prop:chirality-residue-mass-term",
    "cor:gauge-coupling-uniqueness",
    "conj:cp-violation-spectral-form",
  ],
});
