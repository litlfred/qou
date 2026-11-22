import { table } from "../../schema/builders";
export default table({
  label: "tbl:observability-independent-motivation-table-data",
  title: "Data table from rem:observability-independent-motivation",
  uses: ["rem:observability-independent-motivation"],
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-10-13",
      body:
        "Row removed: \"Contact structure | Non-degenerate | May degenerate\". It " +
        "restated item 2 of `rem:observability-independent-motivation`, the " +
        "identification of observability with Levi non-degeneracy, which is " +
        "withdrawn after owner ruling Q1 ($\\varTheta = f\\,\\xi^\\flat$, " +
        "2026-10-13). Bean `qou-fm7s`.",
    },
  ],
});
