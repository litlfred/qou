import { table } from "../../schema/builders";
export default table({
  label: "tbl:mass-table-z1-20-table-data",
  title: "Data table from rem:mass-table-z1-20",
  uses: ["rem:mass-table-z1-20"],
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/wedderburn_mass_table_z1_20.py",
    witness: [
      "computations/wedderburn-mass-table-z1-20.witness.json",
    ],
  },
  tags: ["extracted-table"],
});
