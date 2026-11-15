import { remark } from "../../schema/builders";

/**
 * Moved out of prop:isospin-singlet-binds-more on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:isospin-singlet-binds-more-two-nucleon-reading",
  title: "Which two-nucleon channel the singlet ordering selects",
  interprets: "prop:isospin-singlet-binds-more",
  uses: ["prop:isospin-singlet-binds-more"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:isospin-singlet-binds-more` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["isospin", "two-nucleon", "comparison-with-measurement"],
});
