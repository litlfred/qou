import { prose } from "../../schema/builders";

/**
 * Coverage of the Lean formalisation. Moved out of the author's note
 * (introduction/authors-note.md) on owner instruction 2026-11-20 (W14b,
 * qou-d4kh): the front matter keeps a plain pointer, this appendix keeps
 * the figures. The counts are carried over verbatim; they were not
 * re-measured in the move.
 */
export default prose({
  label: "prose:formalisation-coverage",
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body: "Counts (737/748, 87 primary conjectures, 75 class-axiomatised) moved verbatim from the author's note; not re-measured in the move. Re-measure with `folio/pipeline/lean-vacuity-axiom-audit.ts` before quoting them as current.",
    },
  ],
});
