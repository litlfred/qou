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
  authors: ["Frederick Carl Leitner"],
  affiliations: ["World Health Organization"],
  date: "2026-03-21",
  macros: {
    pp:    { tex: "\\mathfrak{p}",  unicode: "𝔭" },
    frakr: { tex: "\\mathfrak{r}",  unicode: "𝔯" },
    frakg: { tex: "\\mathfrak{g}",  unicode: "𝔤" },
    frakb: { tex: "\\mathfrak{b}",  unicode: "𝔟" },
  },
  chapters: [
    chapterRef({ dir: "ch0-introduction" }),
    chapterRef({ dir: "ch1-quantum-observable-universe" }),
    chapterRef({ dir: "ch5-brings-surface" }),
    chapterRef({ dir: "ch3-lifting-of-quantum-torsion" }),
    chapterRef({ dir: "ch4-path-integrals-and-braiding" }),
    chapterRef({ dir: "ch6-descartes-universe" }),
    chapterRef({ dir: "ch11-experimental-evidence" }),
    chapterRef({ dir: "ch10-interpretations" }),
    chapterRef({ dir: "ch8-glossary" }),
  ],
});
