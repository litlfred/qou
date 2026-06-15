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
    // NOTE: `\pp` is intentionally NOT defined here. The shared preamble
    // (latex/preamble.tex) defines `\pp` = `p` (the p-adic / finite-field
    // prime), and all content uses it that way ($\mathbb{F}_\pp$,
    // $\mathbb{Q}_\pp$, $v_\pp$). Re-emitting `\newcommand{\pp}{\mathfrak{p}}`
    // here both contradicts CLAUDE.md §7aa (proton is `\mathfrak{p}`, never
    // `\pp`) and triggered a fatal "Command \pp already defined" in the
    // pdflatex compile. The proton is written `\mathfrak{p}` directly.
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
    // Braced so a place-subscript composes: `\ordw_v` / `\ordw_{\mathbb{A}}`
    // would otherwise be `\mathrm{ord}_{\omega}_v` → "! Double subscript".
    ordw:  { tex: "{\\mathrm{ord}_{\\omega}}",  unicode: "ord_ω" },
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
    chapterRef({ dir: "brings-surface" }),                     // Bring's surface (deep): χ = −6, S_5/A_5 action, cohomological defect
    // statistics-symmetrisation dissolved (2026-05-27): 7-block scaffold
    // never populated; 5 orphan blocks redistributed to braids-and-knots
    // (pontryagin-dual-coxeter-character) and particle-interactions
    // (spin-from-so3-fiber, type-b-folding-cpt, weinberg-angle-categorical,
    // wigner-su4-from-spin-isospin). Pauli/spin-stats content remains a
    // future authoring goal — will create a new chapter when content exists.
    chapterRef({ dir: "mass-endomorphism" }),                   // The Mass Endomorphism: categorical opener + algebraic core (~80 blocks). Generic Yekutieli path — before particles.
    chapterRef({ dir: "particle-interactions" }),              // Particles: GB, LP, nuclear structure, SDP-as-thimble + skein/hadron/atom-shell
    chapterRef({ dir: "climax-volume-mass" }),                 // q-Hyperbolic Geometry: Möbius energy, crossing energy, Lagrange resolvents, braiding relations (42 blocks)
    chapterRef({ dir: "mass-theory" }),                        // Mass Analysis: geometric face, archimedean face, physical predictions, compute (~470 blocks). Consumes particles + q-hyperbolic geometry.
    // mass-application merged into mass-theory (2026-05-27)
    chapterRef({ dir: "gravity-spacetime" }),                  // Gravity emergence: contact geometry + geodesic Madelung

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
    chapterRef({ dir: "appendix-knot-operations-archimedean" }),  // Archimedean lobe (particle NF + gluon-model) — split per q-usage Policy A
    chapterRef({ dir: "appendix-transfer-matrices" }),
    chapterRef({ dir: "appendix-atomic-mass-calculations" }),
    chapterRef({ dir: "appendix-mass-binding-algorithms" }),    // Bridge: canonical chain steps → propositions → Python API
    chapterRef({ dir: "appendix-qvalues" }),
    chapterRef({ dir: "appendix-surreals" }),                  // Surreal-number lift (categorical lobe) + Millennium-problem surreal bounds
    chapterRef({ dir: "appendix-surreals-archimedean" }),      // Surreal-number lift (archimedean lobe) — substrate-q_0-pinned content split out per q-usage audit
    chapterRef({ dir: "index-of-definitions" }),
  ],
});
