import { paper, chapterRef } from "../schema/builders";
import { paperIdentity } from "./identity";

/**
 * Quantum Observable Universe — Paper manifest.
 *
 * This is the authoritative source for document structure.
 * Each chapter is referenced by directory name; the pipeline resolves
 * `<dir>/<dir>.ts` by convention (or uses `uri` override).
 *
 * Title, authors and date come from `./identity`, which the self-citation
 * `leitner2026` in `folio/schema/references.ts` also reads.
 */
export default paper({
  title: paperIdentity.title,
  authors: paperIdentity.authors,
  affiliations: [],
  date: paperIdentity.date,
  abstract:
    "This monograph develops the mathematical framework of the Quantum Observable " +
    "Universe (QOU): a rigid braided monoidal category equipped with a " +
    "Frobenius--Hopf object $A$, a fibre functor $\\tau$, and a unified two-term " +
    "categorical action ($\\mathrm{QCD} + \\mathrm{QED}$) governed by a single " +
    "proton-pinned substrate parameter $q$.  Every observable passes through a " +
    "five-step categorical trace pipeline: from the categorical action " +
    "$\\mathfrak{S}_q = \\mathrm{tr}(\\Phi)$, through the Iwahori--Hecke quotient " +
    "$H_n(q)$ and the Geer--Patureau-Mirand modified trace on negligible morphisms, " +
    "to torus-link and Borromean complements embedded in the genus-four Bring surface " +
    "$\\Sigma_4$ ($\\chi = -6$, selected by cohomological Seifert saturation and " +
    "minimal hyperbolic $\\mathbb{Z}/3$ Kummer descent), to Archimedean " +
    "Bring--Schwinger and Clausen period evaluations, yielding dimensionless mass " +
    "ratios, gauge couplings, weak $\\beta$-decay cumulants, and nuclear binding " +
    "across three-dimensional Wigner-$\\mathrm{SU}(4)$ $\\alpha$-simplex complexes.  " +
    "Part~I establishes the categorical axioms, the five-step framing arc across " +
    "Archimedean, $p$-adic, and surreal models, and the Yekutieli lifting and " +
    "descent tower.  Part~II develops the structural mechanics: braid and Hecke " +
    "representations, the geometry of Bring's surface, the knot--particle and " +
    "confinement hierarchy, the Eightfold Way flavour and octonionic colour " +
    "structure, the categorical mass endomorphism, $q$-hyperbolic volume and " +
    "kinematics, the elementary-particle and nuclear mass and binding pipelines, " +
    "and the emergence of contact-geometric gravity.  Part~III compares the " +
    "resulting spectra against experimental measurements and extends the braid " +
    "formalism to atomic, molecular, and organic chemistry.  Part~IV treats brane " +
    "fluid dynamics, Markov-trace stochastic mechanics, information-theoretic " +
    "complexity, internalised measurement, and the $q$-geometric Langlands " +
    "correspondence, accompanied throughout by machine-checked Lean~4 proofs and " +
    "arbitrary-precision certified numerical witnesses.",
  macros: {
    // NOTE: `\pp` is intentionally NOT defined here. The shared preamble
    // (latex/preamble.tex) defines `\pp` = `p` (the p-adic / finite-field
    // prime), and all content uses it that way ($\mathbb{F}_\pp$,
    // $\mathbb{Q}_\pp$, $v_\pp$). Re-emitting `\newcommand{\pp}{\mathfrak{p}}`
    // here both contradicts AGENTS.md §7aa (proton is `\mathfrak{p}`, never
    // `\pp`) and triggered a fatal "Command \pp already defined" in the
    // pdflatex compile. The proton is written `\mathfrak{p}` directly.
    nn:    { tex: "\\mathfrak{n}",  unicode: "$\\mathfrak{n}$" },
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
    // ── Front matter (intro only; notation register moved to appendix) ──
    chapterRef({ dir: "introduction" }),

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
    // The structural mechanism: algebra → geometry → particles & flavor →
    // mass endomorphism & q-hyperbolic geometry → mass analysis →
    // nuclear interactions → gravity.
    chapterRef({
      dir: "braids-and-knots",
      partTitle: "Structural Mechanics",
    }),                                                       // Braids, knots, Hecke quotient, Jones-Markov trace, quantum groups
    chapterRef({ dir: "brings-surface" }),                     // Bring's surface (deep): χ = −6, S_5/A_5 action, cohomological defect
    chapterRef({ dir: "knots-particles-confinement" }),         // Knots, Particles, and Confinement: particle definitions, hadron algebra, Borromean nucleons, electroweak torus-link triplet, confinement/shell hierarchy
    chapterRef({ dir: "eightfold-way" }),                      // The Eightfold Way and Flavor Structure: A₂ from 3-strand braiding, SU(3) flavor multiplets, U-spin, octonionic color algebra, q-deformation
    chapterRef({ dir: "mass-endomorphism" }),                   // The Mass Endomorphism: categorical mass identity, topological mass decomposition, complex volume, Markov-trace endomorphism, χ-character closed forms
    chapterRef({ dir: "climax-volume-mass" }),                 // q-Hyperbolic Geometry: Möbius energy, crossing energy & skein asymmetry, Lagrange resolvents, knot-operator energy, spectral filter
    chapterRef({ dir: "mass-theory" }),                        // Mass Analysis: geometric face, archimedean face, elementary particle, gauge, and nuclear mass pipeline
    chapterRef({ dir: "nuclear-interactions" }),                // Nuclear Interactions and Binding: Gröbner–Shirshov reduction, LP/SDP operator selection, beta decay, atomic braid mass, Q-values
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
    chapterRef({ dir: "appendix-mass-binding-algorithms" }),    // Bridge: canonical chain steps → propositions → Python API
    chapterRef({ dir: "appendix-standard-model" }),             // Toward the Standard Model: gauge action groupoid → Hecke realization → SM truncation, with honest open-problems ledger
    chapterRef({ dir: "appendix-nf-witnesses" }),               // Normal Form Witnesses: exact Pauli witnesses for light and medium nuclei via inductive Gröbner reduction
    chapterRef({ dir: "appendix-qvalues" }),
    chapterRef({ dir: "appendix-surreals" }),                  // Surreal-number lift (categorical lobe) + Millennium-problem surreal bounds
    chapterRef({ dir: "appendix-surreals-archimedean" }),      // Surreal-number lift (archimedean lobe) — substrate-q_0-pinned content split out per q-usage audit
    chapterRef({ dir: "index-of-definitions" }),
    chapterRef({ dir: "notation" }),                          // Symbol register — moved out of the front matter to its own appendix (too long for the front). Forward refs ignored by the detangler (preview chapter).

  ],
});
