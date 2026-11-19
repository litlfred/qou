import { table } from "../../schema/builders";
export default table({
  label: "tbl:bar-involution-table8-data",
  title: "Data table 8 from def:bar-involution",
  uses: ["def:bar-involution"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "Lean predicates: `IsBarSymmetric x` and `IsBarAntiSymmetric x`.",
    },
  ],
});
