import { table } from "../../schema/builders";
export default table({
  label: "tbl:mass-comparison-table-table1-data",
  title: "Topological knot formulas and mass evaluations for leptons against CODATA 2022 and KATRIN bounds",
  uses: ["rem:mass-comparison-table"],
  tags: ["extracted-table"],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/codata-2022-validation-masses.witness.json",
      "computations/two-term-qed-isotope-and-nucleon-compute.witness.json",
    ],
    status: "verified",
  },
});
