import { prose } from "../../schema/builders";

/**
 * Coverage of the Lean formalisation. Moved out of the author's note
 * (introduction/authors-note.md) on owner instruction 2026-11-20 (W14b,
 * qou-d4kh): the front matter keeps a plain pointer, this appendix keeps
 * the figures. The counts were re-measured on 2026-11-21 (see the
 * authorNote below); they move with the corpus.
 */
export default prose({
  label: "prose:formalisation-coverage",
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body: "Counts re-measured 2026-11-21 with `bun scripts/refresh-authors-note.ts` (PR #8888): 705/720 provable blocks sorry-free (97.9 %), 97 primary conjectures, 72 (74.2 %) class-axiomatised. They move with the corpus; re-run that script before quoting them.",
    },
  ],
});
