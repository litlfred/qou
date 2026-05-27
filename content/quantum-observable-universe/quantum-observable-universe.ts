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
    // The `partTitle` field renders as a \part{...} banner before this
    // chapter; LaTeX supplies the "Part N" prefix automatically, so
    // the value here is the bare title (no "Part I:" repetition).
    // Subsequent chapters belong to the same Part until the next
    // `partTitle` is set. Per chapter-reorg proposal §6 (E3 banner
    // approach).
    chapterRef({
      dir: "quantum-universes",
      partTitle: "Foundations",
    }),                                                       // QU axioms
    chapterRef({ dir: "quantum-observable-universes" }),       // QOU axioms, q-operators, substrate parameter, Reeb derivation
    chapterRef({ dir: "models-of-qous" }),                    // Models of QOUs — FRAMING CHAPTER: 5-step arc (Cat→Alg→Geom→Arch→Phys); also model gallery + Bring's basics. Forward refs allowed (preview chapter — see docs/chapter-restructure-2026-05-25.md). Moved from Part II 2026-05-25.
    chapterRef({ dir: "lifting-and-descent" }),                // Yekutieli tower / brane tower (descent, jets, Gröbner-Shirshov filtration)

    // ── Part II: Structural Mechanics ─────────────────────────────────
    // The structural mechanism: algebra → geometry → particles → mass →
    // gravity. Closes with the non-abelian Stokes mass identity and its
    // long-range gravitational consequence.
    //
    // Phase 6 (2026-05-25): inserted scaffolds for Statistics &
    // Symmetrisation (Pauli, spin-statistics) between Bring's content
    // and Particles; Gravity & Spacetime Emergence after Particle
    // Interactions. Phase 4+5 (TBD) will split braids-and-knots and
    // archimedean-universe into focused destination chapters.
    chapterRef({
      dir: "braids-and-knots",
      partTitle: "Structural Mechanics",
    }),                                                       // Braids, knots, Hecke, mass machinery (further split per remaining Phase 4 chunks)
    chapterRef({ dir: "climax-volume-mass" }),                 // [NEW Ch 6 — Phase 4] q-Hyperbolic, Vol, tangle energies, vertex factorisation, Kashaev — climax of Part II's first half
    chapterRef({ dir: "brings-surface" }),                     // [NEW Ch 7 — Phase 5] Bring's surface (deep): χ = −6, S_5/A_5 action, cohomological defect — split from archimedean-universe
    // statistics-symmetrisation dissolved (2026-05-27): 7-block scaffold
    // never populated; 5 orphan blocks redistributed to braids-and-knots
    // (pontryagin-dual-coxeter-character) and particle-interactions
    // (spin-from-so3-fiber, type-b-folding-cpt, weinberg-angle-categorical,
    // wigner-su4-from-spin-isospin). Pauli/spin-stats content remains a
    // future authoring goal — will create a new chapter when content exists.
    chapterRef({ dir: "particle-interactions" }),              // Ch 9 Particles: GB, LP, nuclear structure, SDP-as-thimble + skein/hadron/atom-shell content migrated from braids-and-knots
    chapterRef({ dir: "mass-theory" }),                        // [NEW Ch 10 — Phase 4] Mass — Theory (light): Wedderburn, Frobenius pairing, transfer matrix, categorical mass foundations
    chapterRef({ dir: "mass-application" }),                   // [NEW Ch 11 — Phase 4] Mass — Application (heavy): Hoefsmit construction, Wenzl, Markov-peel, GS reductions, LP/SDP, φ_q convergence
    chapterRef({ dir: "gravity-spacetime" }),                  // [NEW Ch 12 — Phase 6 scaffold] Gravity emergence: contact geometry + geodesic Madelung

    // ── Part III: Physical Realization ────────────────────────────────
    // Predictions, comparisons to CODATA, and extension to atomic /
    // molecular / organic chemistry. New Part introduced 2026-05-25 per
    // chapter-restructure plan.
    chapterRef({
      dir: "predicted-spectra",
      partTitle: "Physical Realization",
    }),                                                       // [NEW Ch 13 — Phase 5] Predicted spectra: fundamental fermions, mesons/nucleons, atomic shells, EM coupling — split from archimedean-universe
    chapterRef({ dir: "observations" }),                       // Ch 14 Physical observations / CODATA
    chapterRef({ dir: "molecular-construction" }),             // Molecular braids: H₂ → benzene
    chapterRef({ dir: "organic-chemistry" }),                  // Organic chemistry (covalent / Hopf-ring)

    // ── Part IV: Dynamics, Information, Emergence ─────────────────────
    // Dynamical and information-theoretic deepenings of the framework.
    // Renamed 2026-05-25 from "Further Machinery". Adds Stochastic
    // Mechanics + Measurement & Observation chapters as scaffolds.
    chapterRef({
      dir: "fluid-dynamics",
      partTitle: "Dynamics, Information, Emergence",
    }),                                                       // Fluid dynamics of the brane
    chapterRef({ dir: "stochastic-mechanics" }),               // [NEW Ch 18 — Phase 6 scaffold] Markov-trace stochastic dynamics, Nelson, Itô
    chapterRef({ dir: "information-theory" }),                 // Information-theoretic perspectives
    chapterRef({ dir: "measurement-observation" }),            // [NEW Ch 20 — Phase 6 scaffold] Quantum measurement as fibre-functor behaviour
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
