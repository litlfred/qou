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
    "This book develops the mathematical framework of the Quantum Observable " +
    "Universe (QOU): a rigid braided monoidal category equipped with a " +
    "Frobenius--Hopf object whose differential geometry is controlled by a " +
    "substrate parameter $q$.  Part I (Chapters 0--3) establishes the " +
    "categorical foundations and the Yekutieli brane tower.  Part II " +
    "(Chapters 4--8) develops the structural consequences: braiding and " +
    "knot theory, models over various ground fields, the algebraic " +
    "substrate, the fluid dynamics of the brane, and information-theoretic " +
    "perspectives.  Part III (Chapters 9--10) specialises to the Descartes " +
    "universe on Bring's surface ($\\chi = -6$) and collects physical " +
    "predictions.",
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
    // ── Part I: Foundations (Ch 0–3) ─────────────────────────────────
    chapterRef({ dir: "ch0-introduction" }),                  // Ch 0
    chapterRef({ dir: "ch1-quantum-observable-universe" }),   // Ch 1: QU axioms
    chapterRef({ dir: "ch2-quantum-geometry" }),              // Ch 2: QOU axioms, q-operators
    chapterRef({ dir: "ch3-lifting-of-quantum-torsion" }),   // Ch 3: Yekutieli tower

    // ── Part II: Structure (Ch 4–8) ──────────────────────────────
    chapterRef({ dir: "ch4-path-integrals-and-braiding" }),  // Ch 4: Braids, knots, Hecke
    chapterRef({ dir: "ch6-descartes-universe" }),           // Ch 5: Models of QOUs
    chapterRef({ dir: "ch8-algebraic-substrate" }),          // Ch 6: Algebraic substrate
    chapterRef({ dir: "ch10-fluid-dynamics" }),              // Ch 7: Fluid dynamics
    chapterRef({ dir: "ch9-information-theory" }),           // Ch 8: Information theory

    // ── Part III: The Descartes Universe and Observations (Ch 9–10)
    chapterRef({ dir: "ch5-brings-surface" }),               // Ch 9:  Bring's surface, χ = -6
    chapterRef({ dir: "ch7-observations" }),                 // Ch 10: Physical observations

    // ── Back matter ──────────────────────────────────────────────
    chapterRef({ dir: "ch8-glossary" }),
    chapterRef({ dir: "appendix-knot-periodic-table" }),
    chapterRef({ dir: "appendix-transfer-matrices" }),
    chapterRef({ dir: "appendix-atomic-mass-calculations" }),
    chapterRef({ dir: "index-of-definitions" }),
  ],
});
