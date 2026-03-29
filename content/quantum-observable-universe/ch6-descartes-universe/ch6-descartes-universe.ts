import { chapter, section } from "../../schema/builders";

/**
 * Chapter 5: Models of QOUs.
 *
 * Concrete realisations of the QOU axioms.  First half: general models
 * (Archimedean, p-adic, finite-field, Witt-vector, Jones, fluid).
 * Second half: the Descartes universe — the specific realisation with
 * χ(A) = −6 and Bring's surface as fibre geometry.
 *
 * Merged from former Ch 5 (Models of QOU) + Ch 6 (The Descartes Universe).
 */
export default chapter({
  number: 5,
  title: "Models of QOUs",
  label: "chap:models-qou",
  sections: [
    // ═══════════════════════════════════════════════════════════════════
    // PART A: GENERAL MODELS
    // ═══════════════════════════════════════════════════════════════════

    // ── Physical interpretation and main result ─────────────────────
    section({
      title: "Physical interpretation and the main result",
      label: "sec:physical-interpretation",
      blocks: [
        "q-yang-mills-levi",
        "gr-substrate-geometry",
        "main-commutative-diagram",
        "main-commutative-diagram-proof",
      ],
    }),

    // ── Archimedean realisations ────────────────────────────────────
    section({
      title: "Archimedean specialisations",
      label: "sec:archimedean-models",
      blocks: [
        "calabi-yau",
        "ale",
        "brings-surface-unit-circle",
        "cosmological-limits",
        "instanton",
        "irreducible-connection",
        "seiberg-witten",
        "primordial-vortex",
        "geometric-drag",
        "self-dual-curvature",
        "c-substrate-via-levi",
        "webster-inner-product",
        "heisenberg-commutator-prop",
        "heisenberg-commutator",
        "reeb-decomposition",
        "observation-archimedean",
        "spatial-realization-functor",
        "categorical-archimedean-bridge",
        "categorical-archimedean-bridge-proof",
      ],
    }),

    // ── Categorical reformulation ───────────────────────────────────
    section({
      title: "Key Results in Categorical Language",
      label: "sec:categorical-reformulation",
      blocks: ["categorical-reformulation"],
    }),

    // ── Non-Archimedean models ──────────────────────────────────────
    section({
      title: "Universal Enveloping Algebras and Quantum Groups",
      label: "sec:enveloping-algebras",
      blocks: ["enveloping-algebras"],
    }),
    section({
      title: "$\\pp$-Adic Number Fields and Universality",
      label: "sec:p-adic-fields",
      blocks: ["p-adic-fields"],
    }),
    section({
      title: "$\\mathbb{C}_\\pp$ Quantum Universe",
      label: "sec:cp-que",
      blocks: ["p-adic-realisation"],
    }),
    section({
      title: "Lifting via Formal Groups and Witt Vectors",
      label: "sec:witt-vector-lifting",
      blocks: [
        "witt-vector-lifting-intro",
        "witt-vector-lift",
        "skew-poisson-integration",
        "skew-poisson-integration-proof",
        "witt-lift-qou",
      ],
    }),

    // ── Finite-field models ─────────────────────────────────────────
    section({
      title: "Quotient to Finite Fields",
      label: "sec:finite-fields",
      blocks: [
        "finite-field-realisation",
        "finite-fields-outlook",
      ],
    }),

    // ── Jones polynomials ───────────────────────────────────────────
    section({
      title: "Jones Polynomials",
      label: "sec:jones-polynomials",
      blocks: ["jones-polynomials"],
    }),

    // ── Fluid dynamics ──────────────────────────────────────────────
    section({
      title: "Fluid Dynamics of the Brane",
      label: "sec:brane-fluid",
      blocks: [
        "brane-fluid",
        "geodesic-vortices",
        "braid-fluid",
        "planck-reynolds",
        "vortex-intensity-modes",
        "discrete-vortex-spectrum",
      ],
    }),

    // ═══════════════════════════════════════════════════════════════════
    // PART B: THE DESCARTES UNIVERSE  (χ(A) = −6)
    // ═══════════════════════════════════════════════════════════════════

    // ── Preamble ────────────────────────────────────────────────────
    section({
      title: "The Descartes Universe",
      label: "sec:descartes-preamble",
      blocks: [
        "descartes-preamble",
      ],
    }),

    // ── Bring's surface: geometry and coordinates ───────────────────
    section({
      title: "Bring's surface: geometry and coordinates",
      label: "sec:brings-geometry",
      contentDir: "ch5-brings-surface",
      blocks: [
        "brings-surface",
        "brings-surface-example",
        "brings-realisations",
        "brings-is-qou",
        "brings-is-qou-proof",
        "brings-qou-4tuple",
        "brings-qou-axiom-map",
        "braid-group-action",
        "color-tube-coordinates",
        "aggregate-color-quantities",
        "color-tube-constraints",
        "color-tube-interpretation",
        "c5-color-tube",
        "intrinsic-color-cubic-pairing",
        "chiral-elliptic",
        "chiral-elliptic-proof",
        "t-duality-elliptic",
        "color-tube-cubic",
        "color-tube-fibers",
        "t-duality-color-tube",
        "color-tube-subloci",
        "chiral-bundles",
        "brings-smoothness-resolution",
        "brings-smoothness",
        "briggs-klein-chart",
        "radial-projection",
        "four-colourability",
        "four-colour-theorem",
        "cyclotomic-reduction",
      ],
    }),

    // ── Spectral resolvents and gauge structures ───────────────────
    section({
      title: "Spectral resolvents and gauge structures",
      label: "sec:spectral-gauge",
      contentDir: "ch5-brings-surface",
      blocks: [
        "quaternionic-spectral-resolvents",
        "omega-constraints",
        "spectral-dynamics",
        "generation-dependent-sw",
        "mi-sw-abelianisation",
        "mi-sw-abelianisation-proof",
        "chiral-sector-coords",
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "descartes-knot-eigenbasis",
        "descartes-elliptic-curve",
      ],
    }),

    // ── The Descartes condition, particles, and the theorem ────────
    section({
      title: "The Descartes condition, particles, and the Descartes theorem",
      label: "sec:descartes-particles",
      contentDir: "ch5-brings-surface",
      blocks: [
        "descent-to-zero",
        "descartes-condition",
        "chi-minus-six-chain",
        "descartes-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
        "descartes-leptons",
        "descartes-chirality",
        "light-cone-affine",
        "chirality-trefoil",
        "brings-curve",
        "torus-knot-generators",
        "embeddability-closure",
        "torus-embeddable-complete",
        "generation-completeness",
        "up-quark",
        "down-quark",
        "electron-knot",
        "electron-knot-example",
        "positron-knot",
        "neutrino-knot",
        "antineutrino-knot",
        "linking-relations-table",
        "q-value-transition",
        "categorical-proton",
        "categorical-neutron",
        "antiparticle-crossing-reversal",
        "chirality-trefoil-electron-positron",
        "stable-nucleus",
        "torus-hopf-stability",
        "unmapped-torus-knots",
        "torus-knot-prime-powers",
        "force-knot-identification",
        "em-coupling-projection",
        "q-chromaticity",
        "integer-stability",
        "diophantine-valley",
        "valley-stability",
        "beta-decay-skein",
        "lepton-number-categorical",
        "parity-violation-skein",
        "nuclear-spin-parity",
        "hadron-half-life",
        "hadron-q-self-correction",
        "skein-coulomb-enhancement",
        "nuclear-groebner-reduction",
        "groebner-shirshov-energy",
        "box-braid-irreducibility",
        "generator-volume-decomposition",
        "markov-trace-factorization",
        "skein-polynomial-transfer-matrix",
        "transfer-matrix-operator",
        "beta-decay-transfer-matrix",
        "shell-structure-eigenvalues",
        "quantum-dilogarithm-volume",
        "reidemeister-action-table",
        "topology-geometry-boundary",
        "elliptic-stability-locus",
        "skein-shell-correction",
        "shell-closure-normal-form",
        "skein-finiteness-bound",
        "spectral-decomposition-qvalue",
        "shell-construction-rules",
        "electron-shells-hopf",
        "helium-hopf-diagram",
        "noble-gas-characterization",
        "metallic-character-knot",
        "francium-extremal-metal",
        "hydrogen-shell-writhe",
        "hydrogen-orbitals",
        "descartes",
        "descartes-proof",
        "universality-general",
        "descartes-yekutieli",
        "observation-brings",
      ],
    }),

    // ── Topological mass and the knot-particle spectrum ────────────
    section({
      title: "Topological mass and the knot-particle spectrum",
      label: "sec:topological-mass-spectrum",
      contentDir: "ch5-brings-surface",
      blocks: [
        "hyperbolic-volumes-prose",
        "ch11-intro",
        "terminal-resolution",
        "knot-formula-table",
        "mass-from-generators",
      ],
    }),
  ],
});
