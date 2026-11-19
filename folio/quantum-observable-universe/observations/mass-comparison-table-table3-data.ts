import { table } from "../../schema/builders";
export default table({
  label: "tbl:mass-comparison-table-table3-data",
  title: "Constituent-sum baselines and empirical binding energies for light nuclei ($A = 2$ to $4$)",
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
