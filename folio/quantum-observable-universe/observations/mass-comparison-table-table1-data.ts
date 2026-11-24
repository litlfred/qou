import { table } from "../../schema/builders";
export default table({
  label: "tbl:mass-comparison-table-table1-data",
  title: "Table 1 from rem:mass-comparison-table",
  uses: ["rem:mass-comparison-table"],
  tags: ["extracted-table"],
  computation: {
    engine: "mpmath",
    script: "computations/master_atlas_jacobian_80dps.py",
    witness: "computations/master-atlas-80dps.witness.json",
    status: "verified",
  },
});
