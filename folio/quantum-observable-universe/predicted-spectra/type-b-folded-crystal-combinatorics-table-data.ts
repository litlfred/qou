import { table } from "../../schema/builders";
export default table({
  label: "tbl:type-b-folded-crystal-combinatorics-table-data",
  title: "Cell-transpose involution and summand-by-summand content cancellation $c(\\lambda) + c(\\lambda^T) = 0$",
  uses: ["prop:type-b-folded-crystal-combinatorics"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean declarations in `QOU.Archimedean.TypeBCrystal` (`TypeBFoldedCrystalCombinatorics.lean`): `Cell`, `Cell.content`, `Cell.transpose`, `Cell.transpose_transpose`, `Cell.content_plus_transpose_content_eq_zero`, `PartitionWithCells`, `PartitionWithCells.content_sum`, `PartitionWithCells.transpose`, `PartitionWithCells.content_sum_plus_transpose_content_sum_eq_zero`, `PartitionWithCells.self_transpose_content_sum_zero`.",
    },
  ],
});
