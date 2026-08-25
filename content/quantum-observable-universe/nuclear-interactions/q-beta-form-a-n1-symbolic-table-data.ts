import { table } from "../../schema/builders";
export default table({
  label: "tbl:q-beta-form-a-n1-symbolic-table-data",
  title: "Symbolic form of $Q_\\beta$ at $A$, $N=1$",
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**This table has no source block.** It carried " +
        "`uses: [\"prop:q-beta-form-a-n1-symbolic\"]`, and no block with that " +
        "label exists in the corpus. Dropped rather than re-pointed, for the " +
        "same reason recorded on `tbl:hecke-log-decomposition-table-data`: " +
        "`uses[]` is editorial, and an invented parent is worse than none.\n\n" +
        "The title read `Data table from prop:q-beta-form-a-n1-symbolic`, " +
        "carrying the internal label into published prose; replaced with the " +
        "quantity it tabulates.",
    },
  ],
});
