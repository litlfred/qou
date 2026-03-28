import { chapter, section } from "../../schema/builders";

/**
 * Chapter 6: The Descartes Universe.
 *
 * The concrete realisation with χ(A) = −6.  Four main sections after a
 * short preamble: (1) Bring's surface geometry and coordinates,
 * (2) spectral and gauge structures, (3) the Descartes condition,
 * particles, and the Descartes theorem, (4) topological mass and the
 * knot-particle spectrum.
 */
export default chapter({
  number: 6,
  title: "The Descartes Universe",
  label: "chap:descartes-universe",
  sections: [
    // ── Preamble (does not count as a numbered section) ──────────────
    section({
      title: "Why this universe",
      label: "sec:descartes-preamble",
      blocks: [
        "descartes-preamble",
      ],
    }),

    // ── §1. Bring's surface: geometry and coordinates ────────────────
    section({
      title: "Bring's surface: geometry and coordinates",
      label: "sec:brings-geometry",
      blocks: [
        // Bring's surface as a QOU
        "brings-surface",
        "brings-realisations",
        "brings-is-qou",
        "brings-is-qou-proof",
        "brings-qou-4tuple",
        "brings-qou-axiom-map",
        // Braid-group action (resolvents now in ch4 as categorical DFT)
        "braid-group-action",
        // Color tube coordinates
        "color-tube-coordinates",
        "aggregate-color-quantities",
        "color-tube-constraints",
        "color-tube-interpretation",
        "c5-color-tube",
        "intrinsic-color-cubic-pairing",
        // Chiral fibration and elliptic curves
        "chiral-elliptic",
        "chiral-elliptic-proof",
        "t-duality-elliptic",
        "color-tube-cubic",
        "color-tube-fibers",
        "observed-value",
        "t-duality-color-tube",
        "color-tube-subloci",
        // Bundle structures and smoothness
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

    // ── §2. Spectral resolvents and gauge structures ─────────────────
    section({
      title: "Spectral resolvents and gauge structures",
      label: "sec:spectral-gauge",
      blocks: [
        // Quaternionic spectral resolvents (minus SO(3) motivation → ch4)
        "quaternionic-spectral-resolvents",
        "omega-constraints",
        "spectral-dynamics",
        // Seiberg--Witten on Bring's
        "generation-dependent-sw",
        "mi-sw-abelianisation",
        "mi-sw-abelianisation-proof",
        // Categorical braid structure and colour sectors
        "chiral-sector-coords",
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "descartes-knot-eigenbasis",
        // The Descartes elliptic curve E_q
        "descartes-elliptic-curve",
      ],
    }),

    // ── §3. The Descartes condition, particles, and the theorem ──────
    section({
      title: "The Descartes condition, particles, and the Descartes theorem",
      label: "sec:descartes-particles",
      blocks: [
        // The Descartes condition
        "descent-to-zero",
        "descartes-condition",
        "descartes-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
        // Leptons, chirality, trefoil subgroups
        "descartes-leptons",
        "descartes-chirality",
        "light-cone-affine",
        "chirality-trefoil",
        "brings-curve",
        // Torus knot generators from χ = -6
        "torus-knot-generators",
        "embeddability-closure",
        "torus-embeddable-complete",
        "generation-completeness",
        // Fundamental fermions (Descartes-specific assignments)
        "up-quark",
        "down-quark",
        "electron-knot",
        "positron-knot",
        "neutrino-knot",
        "antineutrino-knot",
        // Building block reference tables
        "linking-relations-table",
        // q-deformed kinematics (definitions now in ch4)
        "q-value-transition",
        // Proton, neutron, stable nucleus
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
        // Integer stability and Diophantine valley
        "integer-stability",
        "diophantine-valley",
        "valley-stability",
        // Hadron half-life calculations relative to q
        // Beta decay as categorical Skein operation
        "beta-decay-skein",
        "lepton-number-categorical",
        "parity-violation-skein",
        "nuclear-spin-parity",
        // Half-life calculations
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
        // Elliptic stability conjecture
        "elliptic-stability-locus",
        "electron-shells-hopf",
        "helium-hopf-diagram",
        "noble-gas-characterization",
        "metallic-character-knot",
        "francium-extremal-metal",
        "hydrogen-shell-writhe",
        "hydrogen-orbitals",
        // The Descartes theorem
        "descartes",
        "descartes-proof",
        "universality-general",
        "descartes-yekutieli",
        "observation-brings",
      ],
    }),

    // ── §4. Topological mass and the knot-particle spectrum ──────────
    section({
      title: "Topological mass and the knot-particle spectrum",
      label: "sec:topological-mass-spectrum",
      blocks: [
        // Topological mass (Descartes-specific applications)
        "hyperbolic-volumes-prose",
        // Skein decomposition and hadronic mass
        "ch11-intro",
        "terminal-resolution",
        // Knot-to-particle mass spectrum
        "knot-formula-table",
        "mass-from-generators",
      ],
    }),
  ],
});
