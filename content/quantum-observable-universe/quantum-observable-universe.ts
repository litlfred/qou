import { paper, chapterRef } from "../schema/builders";

/**
 * Quantum Observable Universe — Paper manifest.
 *
 * This is the authoritative source for document structure.
 * Each chapter is referenced by directory name; the pipeline resolves
 * `<dir>/<dir>.ts` by convention (or uses `uri` override).
 */
export default paper({
  title: "Quantum Observable Universe",
  authors: ["litlfred"],
  date: "2026-03-21",
  chapters: [
    chapterRef({ dir: "ch1-quantum-observable-universe" }),
    // chapterRef({ dir: "ch2-brings-surface" }),
    // chapterRef({ dir: "ch3-descartes-universe", uri: "https://..." }), // remote
  ],
});
