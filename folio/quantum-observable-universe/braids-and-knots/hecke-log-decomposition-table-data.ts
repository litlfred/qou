import { table } from "../../schema/builders";
export default table({
  label: "tbl:hecke-log-decomposition-table-data",
  title: "Hecke logarithmic decomposition",
  tags: ["extracted-table"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-08-08",
      body:
        "**This table has no source block.** It carried " +
        "`uses: [\"prop:hecke-log-decomposition\"]`, and no block with that " +
        "label exists anywhere in the corpus — the chapter manifest lists only " +
        "this extracted table. The reference was dropped rather than " +
        "re-pointed: `uses[]` is the editorial relation, so guessing a " +
        "plausible parent would fabricate the edge that ordering metrics are " +
        "computed from.\n\n" +
        "The title had the same defect, reading `Data table from " +
        "prop:hecke-log-decomposition` — an internal label in published prose. " +
        "Replaced with the subject it names.\n\n" +
        "What is actually missing is the proposition this table was extracted " +
        "from. Until it is written the table stands alone, which is what the " +
        "block now says rather than pointing at nothing.",
    },
  ],
});
