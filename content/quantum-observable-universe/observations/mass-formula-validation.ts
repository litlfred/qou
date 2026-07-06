import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:mass-comparison-table",
  label: "rem:mass-formula-validation",
  title: "Mass formula validation: source classification and isotope coverage",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: ["computations/q-pinning-50-digit.witness.json", "computations/codata-masses.witness.json"],
    status: "verified",
  },
  tags: [
    "mass",
    "validation",
    "isotope",
    "CODATA",
    "AME2020",
    "certificate",
    "hecke-engine",
  ],
  uses: [
    "rem:mass-comparison-table",
  ],
  cites: [
    "kerov1996",
  ],
});
