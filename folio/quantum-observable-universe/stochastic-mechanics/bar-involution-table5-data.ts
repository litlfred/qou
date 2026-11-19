import { table } from "../../schema/builders";
export default table({
  label: "tbl:bar-involution-table5-data",
  title: "Data table 5 from def:bar-involution",
  uses: ["def:bar-involution"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      body: "Lean theorems: `IsBarSymmetric.add`, `IsBarSymmetric.mul`, `IsBarAntiSymmetric.add`, `IsBarSymmetric.of_mul_antisym`, `IsBarAntiSymmetric.of_sym_mul`, `IsBarSymmetric.neg`, `IsBarAntiSymmetric.neg`, `IsBarAntiSymmetric.pow_two_mul`, `IsBarAntiSymmetric.pow_two_mul_add_one`, `bar_neg`.",
    },
  ],
});
