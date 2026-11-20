import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:topological-mass-formula",
  label: "rem:mass-comparison-table",
  title: "Mass predictions from knot formulas vs. CODATA/PDG values",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json", "computations/codata-masses.witness.json"],
    status: "verified",
  },
  tags: [
    "mass",
    "prediction",
    "CODATA",
    "PDG",
    "comparison",
    "knot",
    "experimental",
  ],
  uses: ["rem:mass-from-generators"],
});
