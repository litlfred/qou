import { remark } from "../../schema/builders";

/**
 * Moved out of prop:q-beta-cos-resummation on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:q-beta-cos-resummation-comparison",
  title: "$\\mathfrak{Q}_\\beta$ cos-resummation compared with measurement at the proton pin",
  interprets: "prop:q-beta-cos-resummation",
  uses: ["prop:q-beta-cos-resummation"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:q-beta-cos-resummation` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["q-beta", "cos-resummation", "comparison-with-measurement"],
});
