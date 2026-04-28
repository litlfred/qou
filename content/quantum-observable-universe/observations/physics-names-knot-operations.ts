import { remark } from "../../schema/builders";

export default remark({
  label: "rem:physics-names-knot-operations",
  title: "Physics names $\\leftrightarrow$ categorical knot operations (table; depends on $q_0$)",
  interprets: "prop:confinement-categorical",
  uses: [
    "prop:borromean-baryon-interpretation",
    "prop:chirality-residue-mass-term",
    "cor:gauge-coupling-uniqueness",
    "prop:force-carrier-bring-uniqueness",
    "def:electron-shell",
    "prop:cp-violation-spectral-form",
  ],
});
