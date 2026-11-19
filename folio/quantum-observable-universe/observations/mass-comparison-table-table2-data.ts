import { table } from "../../schema/builders";
export default table({
  label: "tbl:mass-comparison-table-table2-data",
  title: "Leading-order knot mass evaluations and two-term nucleon mass splitting against CODATA 2022 and PDG 2024",
  uses: ["rem:mass-comparison-table"],
  tags: ["extracted-table"],
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/m-p-substrate-identity-50dps.witness.json",
      "computations/codata-2022-validation-masses.witness.json",
    ],
    status: "verified",
  },
});
