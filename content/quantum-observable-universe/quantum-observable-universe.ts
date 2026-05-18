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
    "This paper develops the mathematical framework of the Quantum Observable " +
    "Universe (QOU): a rigid braided monoidal category equipped with a " +
    "Frobenius--Hopf object whose differential geometry is controlled by a " +
    "substrate parameter $q$.  Part~I (Chapters 1--3) establishes the " +
    "categorical foundations and the Yekutieli brane tower.  Part~II " +
    "(Chapters 4--8) develops the structural consequences: braiding and " +
    "knot theory, models over various ground fields, the algebraic " +
    "substrate, fluid dynamics, and information-theoretic " +
    "perspectives.  Part~III (Chapters 9--10) specialises to the Descartes " +
    "universe on Bring's surface ($\\chi = -6$) and collects physical " +
    "predictions.  Chapter~11 develops the $q$-geometric Langlands " +
    "correspondence.",
  macros: {
    pp:    { tex: "\\mathfrak{p}",  unicode: "𝔭" },
    nn:    { tex: "\\mathfrak{n}",  unicode: "𝔫" },
    frakr: { tex: "\\mathfrak{r}",  unicode: "𝔯" },
    frakg: { tex: "\\mathfrak{g}",  unicode: "𝔤" },
    frakb: { tex: "\\mathfrak{b}",  unicode: "𝔟" },
    frakI: { tex: "\\mathfrak{I}",  unicode: "ℑ" },
    frakK: { tex: "\\mathfrak{K}",  unicode: "𝔎" },
    frakP: { tex: "\\mathfrak{P}",  unicode: "𝔓" },
    // ω-adic order (leading exponent in Conway normal form).
    // Direct analogue of p-adic ord_p; used in the surreal-numbers
    // appendix as the surreal replacement for classical Big-O.
    // See: app:surreals/rem:conway-normal-form.
    ordw:  { tex: "\\mathrm{ord}_{\\omega}",  unicode: "ord_ω" },
  },
  chapters: [
    // ── Front matter (intro first, then notation register) ──────────
    chapterRef({ dir: "introduction" }),
    chapterRef({ dir: "notation" }),                          // Symbol register; forward refs from notation are ignored by the detangler (preview chapter).

    // ── Part I: Foundations ──────────────────────────────────────────
    chapterRef({ dir: "quantum-universes" }),                 // QU axioms
    chapterRef({ dir: "quantum-observable-universes" }),       // QOU axioms, q-operators, substrate parameter, Reeb derivation
    chapterRef({ dir: "lifting-and-descent" }),                // Yekutieli tower

    // ── Part II: Structure (physics narrative — bk, particles, obs) ──
    chapterRef({ dir: "braids-and-knots" }),                  // Braids, knots, Hecke, classical-limit machinery
    chapterRef({ dir: "models-of-qous" }),                    // Models of QOUs — the archimedean wall (Calabi-Yau, ALE, SW)
    chapterRef({ dir: "descartes-universe" }),                // Bring's surface, χ = −6, fundamental particles (incl. cohomological defect)
    chapterRef({ dir: "particle-interactions" }),              // GB, LP, nuclear structure, SDP-as-thimble
    chapterRef({ dir: "observations" }),                      // Physical observations / CODATA
    chapterRef({ dir: "molecular-construction" }),             // Molecular braids: H₂ → benzene
    chapterRef({ dir: "organic-chemistry" }),                  // Organic chemistry (covalent / Hopf-ring)

    // ── Part III: Further machinery (deeper algebraic / dynamical) ───
    chapterRef({ dir: "fluid-dynamics" }),                     // Fluid dynamics of the brane
    chapterRef({ dir: "information-theory" }),                 // Information-theoretic perspectives
    chapterRef({ dir: "q-geometric-langlands" }),              // q-Geometric Langlands (incl. Tannaka–Krein, Hasse–Weil)

    // ── Back matter ─────────────────────────────────────────────────
    chapterRef({ dir: "glossary" }),
    chapterRef({ dir: "appendix-knot-periodic-table" }),
    chapterRef({ dir: "appendix-knot-operations" }),
    chapterRef({ dir: "appendix-transfer-matrices" }),
    chapterRef({ dir: "appendix-atomic-mass-calculations" }),
    chapterRef({ dir: "appendix-qvalues" }),
    chapterRef({ dir: "appendix-surreals" }),                  // Surreal-number lift + Millennium-problem surreal bounds
    chapterRef({ dir: "index-of-definitions" }),
  ],
});
