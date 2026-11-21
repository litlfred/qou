import { remark } from "../../schema/builders";

/**
 * Moved out of prop:cyclotomic-strand-doubling on 2026-11-15 under the owner's ruling that data,
 * fits and comparisons with measurement go in remarks, not statements.
 */
export default remark({
  label: "rem:cyclotomic-strand-doubling-habiro-observation",
  title: "The $\\Phi_8^2$ prefactor observed in atomic-step Habiro elements",
  interprets: "prop:cyclotomic-strand-doubling",
  uses: ["prop:cyclotomic-strand-doubling"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-15",
      body: "Moved verbatim from `prop:cyclotomic-strand-doubling` (owner ruling 2026-11-15: data, fits and comparisons with measurement go in remarks, not statements).",
    },
  ],
  tags: ["cyclotomic", "habiro", "computed-observation"],
});
