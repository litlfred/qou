import { table } from "../../schema/builders";
export default table({
  label: "tbl:bar-involution-table8-data",
  title: "Summary of bar-involution operators, projections, and averaged crossing notation",
  uses: ["def:bar-involution"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "Lean predicates: `IsBarSymmetric x` and `IsBarAntiSymmetric x`.",
    },
  ],
});
