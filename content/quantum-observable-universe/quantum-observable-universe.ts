import { paper, chapterRef } from "../schema/builders";

/**
 * Quantum Observable Universe — Paper manifest.
 *
 * This is the authoritative source for document structure.
 * Each chapter is referenced by directory name; the pipeline resolves
 * `<dir>/<dir>.ts` by convention (or uses `uri` override).
 */
export default paper({
  title: "On the Mechanics of Quantum Observable Universes",
  authors: ["Frederick Carl Leitner"],
  affiliations: [],
  date: "2026-03-21",
  abstract:
    "This paper presents a mathematical framework for the Quantum Observable " +
    "Universe (QOU).  We introduce the notion of quantum torsion in this setting, " +
    "study its lifting to higher categorical structures, and examine the resulting " +
    "interpretational and experimental consequences.  Speculative extensions are " +
    "discussed in the final chapter.",
  macros: {
    pp:    { tex: "\\mathfrak{p}",  unicode: "𝔭" },
    nn:    { tex: "\\mathfrak{n}",  unicode: "𝔫" },
    frakr: { tex: "\\mathfrak{r}",  unicode: "𝔯" },
    frakg: { tex: "\\mathfrak{g}",  unicode: "𝔤" },
    frakb: { tex: "\\mathfrak{b}",  unicode: "𝔟" },
    frakI: { tex: "\\mathfrak{I}",  unicode: "ℑ" },
    frakK: { tex: "\\mathfrak{K}",  unicode: "𝔎" },
    frakP: { tex: "\\mathfrak{P}",  unicode: "𝔓" },
  },
  chapters: [
    chapterRef({ dir: "ch0-introduction" }),
    chapterRef({ dir: "ch1-quantum-observable-universe" }),
    chapterRef({ dir: "ch2-quantum-geometry" }),
    chapterRef({ dir: "ch3-lifting-of-quantum-torsion" }),
    chapterRef({ dir: "ch4-path-integrals-and-braiding" }),
    chapterRef({ dir: "ch6-descartes-universe" }),
    chapterRef({ dir: "ch7-observations" }),
    chapterRef({ dir: "ch9-information-theory" }),
    chapterRef({ dir: "ch8-glossary" }),
    chapterRef({ dir: "appendix-knot-periodic-table" }),
    chapterRef({ dir: "index-of-definitions" }),
  ],
});
