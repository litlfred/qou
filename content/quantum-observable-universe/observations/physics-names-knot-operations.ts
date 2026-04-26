import { remark } from "../../schema/builders";

export default remark({
  label: "rem:physics-names-knot-operations",
  title: "Physics names $\\leftrightarrow$ categorical knot operations (table; depends on $q_0$)",
  uses: [
    "def:borromean-baryon",
    "prop:borromean-baryon-interpretation",
    "prop:chirality-residue-mass-term",
    "cor:gauge-coupling-uniqueness",
    "prop:force-carrier-bring-uniqueness",
    "def:electron-shell",
    "prop:pauli-factor-wedderburn",
    "prop:mass-tower-coefficient-stratification",
    "prop:confinement-categorical",
    "rem:confinement-curvature-rank",
    "prop:cp-violation-spectral-form",
    "prop:gravity-spectral-prefactor",
  ],
});
