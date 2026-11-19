import { table } from "../../schema/builders";
export default table({
  label: "tbl:b1-current-status-table2-data",
  title: "High-precision numerical verifications of depth-2 and depth-3 polylogarithm and hyperbolic-volume identities",
  uses: ["rem:b1-current-status"],
  authorNotes: [
    {
      kind: "note",
      body: "50-dps witness files: `computations/gb-depth-period-bring-fig8.witness.json`, `computations/bring-trilog-zeta5-depth-3.witness.json`, `computations/kummer-reflection-zeta5.witness.json`, and `computations/cl3-zeta5-orbit-sum.witness.json`.",
    },
  ],
  tags: ["extracted-table"],
});
