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
    "substrate parameter $q$.  We study quantum torsion, its lifting through " +
    "the Yekutieli brane tower, the resulting knot-theoretic particle spectrum " +
    "on the Descartes universe (Bring's surface, $\\chi = -6$), the fluid " +
    "dynamics of the brane including a categorical Navier--Stokes obstruction, " +
    "and physical predictions.  Experimental consequences are collected in the " +
    "final chapter.",
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
    // ── Part I: Foundations ─────────────────────────────────────────
    chapterRef({ dir: "ch0-introduction" }),
    chapterRef({ dir: "ch1-quantum-observable-universe" }),  // QU axioms
    chapterRef({ dir: "ch2-quantum-geometry" }),              // QOU axioms, q-operators
    chapterRef({ dir: "ch3-lifting-of-quantum-torsion" }),   // Yekutieli tower, brane tower

    // ── Part II: Structure ────────────────────────────────────────
    chapterRef({ dir: "ch4-path-integrals-and-braiding" }),  // Braids, knots, Hecke
    chapterRef({ dir: "ch6-descartes-universe" }),           // Models of QOUs (general)
    chapterRef({ dir: "ch8-algebraic-substrate" }),          // Frobenius substrate, defects

    // ── Part III: The Descartes Universe ──────────────────────────
    chapterRef({ dir: "ch5-brings-surface" }),               // Bring's surface, χ = -6
    chapterRef({ dir: "ch10-fluid-dynamics" }),              // Brane fluid, q-NS, NS obstruction
    chapterRef({ dir: "ch9-information-theory" }),           // Information, computation

    // ── Part IV: Observations ────────────────────────────────────
    chapterRef({ dir: "ch7-observations" }),                 // Physical predictions (last)

    // ── Back matter ──────────────────────────────────────────────
    chapterRef({ dir: "ch8-glossary" }),
    chapterRef({ dir: "appendix-knot-periodic-table" }),
    chapterRef({ dir: "appendix-transfer-matrices" }),
    chapterRef({ dir: "appendix-atomic-mass-calculations" }),
    chapterRef({ dir: "index-of-definitions" }),
  ],
});
