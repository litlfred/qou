import { chapter, section } from "../../schema/builders";

/**
 * Chapter 6: The Descartes Universe.
 *
 * The concrete realisation with χ(A) = −6.  Sections:
 * (1) Bring's surface geometry and coordinates,
 * (2) spectral and gauge structures, (3) the Descartes condition,
 * particles, and the Descartes theorem, (4) topological mass and the
 * knot-particle spectrum.
 */
export default chapter({
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
        "brings-surface-example",
        "brings-realisations",
        "brings-physics-interpretations",
        "brings-is-qou",
        "brings-is-qou-proof",
        "brings-qou-4tuple",
        "brings-qou-axiom-map",
        // Braid-group action (resolvents in braids-and-knots as categorical DFT)
        "braid-group-action",
        // Color tube coordinates
        "color-tube-coordinates",
        "aggregate-color-quantities",
        "color-tube-constraints",
        "color-tube-interpretation",
        "c5-color-tube",
        "intrinsic-color-cubic-pairing",
        // Coral fibration and elliptic curves
        "coral-elliptic",
        "coral-elliptic-proof",
        "t-duality-elliptic",
        "color-tube-cubic",
        "color-tube-fibers",
        "t-duality-color-tube",
        "color-tube-subloci",
        "pure-colour-sublocus",
        // Bundle structures and smoothness
        "coral-bundles",
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
        // Quaternionic spectral resolvents (minus SO(3) motivation → braids-and-knots)
        "quaternionic-spectral-resolvents",
        "omega-constraints",
        "spectral-dynamics",
        // Seiberg--Witten on Bring's
        "generation-dependent-sw",
        "lepton-mass-integrals",
        "mi-sw-abelianisation",
        "mi-sw-abelianisation-proof",
        // Categorical braid structure and colour sectors
        "coral-sector-coords",
        "descartes-braid-structure",
        "descartes-braid-structure-proof",
        "descartes-knot-eigenbasis",
        // The Descartes elliptic curve E_q
        "descartes-elliptic-curve",
      ],
    }),

    // ── §3a. The Descartes condition and lepton spectrum ─────────────
    // Was: one 84-block section.  Split (R4) for navigability.
    section({
      title: "The Descartes condition and lepton spectrum",
      label: "sec:descartes-condition",
      blocks: [
        // The Descartes condition (χ = −6)
        "descent-to-zero",
        "descartes-condition",
        "chi-minus-six-chain",
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
        "genus-filtration-ideal",
        "genus-filtration-interpretation",
        "torus-embeddable-complete",
        "generation-completeness",
      ],
    }),

    // ── §3b. Fundamental particles ────────────────────────────────────
    section({
      title: "Fundamental particles",
      label: "sec:fundamental-particles",
      blocks: [
        // Fundamental fermions (Descartes-specific assignments)
        "up-quark",
        "up-quark-properties",
        "down-quark",
        "down-quark-properties",
        "electron-knot",
        "electron-knot-example",
        "positron-knot",
        "neutrino-knot",
        "antineutrino-knot",
        // Building block reference table
        "linking-relations-table",
        // q-deformed kinematics (definitions in braids-and-knots; applied here)
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
      ],
    }),

    // ── §3c. Nuclear stability and decay ─────────────────────────────
    section({
      title: "Nuclear stability and decay",
      label: "sec:nuclear-stability-decay",
      blocks: [
        // Beta decay as categorical Skein operation
        "beta-decay-skein",
        "lepton-number-categorical",
        "parity-violation-skein",
        "nuclear-spin-parity",
        // Half-life calculations via Gröbner reductions
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
        "beta-decay-interpretation",
        "beta-decay-braid-visualizer",
      ],
    }),

    // ── §3d. Atomic shells and the periodic table ─────────────────────
    section({
      title: "Atomic shells and the periodic table",
      label: "sec:atomic-shells",
      blocks: [
        "shell-structure-eigenvalues",
        "shell-eigenvalue-properties",
        "quantum-dilogarithm-volume",
        "reidemeister-action-table",
        "topology-geometry-boundary",
        // Elliptic stability conjecture
        "elliptic-stability-locus",
        "shell-closure-normal-form",
        "torus-knot-shell-binding",
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
        "hydrogen-orbital-tables",
      ],
    }),

    // ── §3e. The Descartes theorem ────────────────────────────────────
    section({
      title: "The Descartes theorem",
      label: "sec:descartes-theorem",
      blocks: [
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
        "intro",
        "terminal-resolution",
        // Knot-to-particle mass spectrum
        "knot-formula-table",
        "mass-from-generators",
      ],
    }),
    // ── §5. Orbital space and resonance modes ────────────────────────
    // Moved here from quantum-observable-universes (R1): uses
    // prop:reidemeister-mass-invariance (braids-and-knots) which would
    // otherwise be a forward ref from quantum-observable-universes.
    section({
      title: "Orbital space and resonance modes",
      label: "sec:orbital-space",
      blocks: [
        "orbital-space-normal-bundle",
        "orbital-fourier-decomposition",
      ],
    }),

    // ── §6. Five-fold symmetry and cohomological embedding ───────────
    // Moved here from quantum-observable-universes (R1): uses
    // prop:skein-finiteness-bound, prop:shell-closure-normal-form,
    // rem:force-knot-identification — all in this chapter — which would
    // otherwise be span-7 forward refs.
    section({
      title: "Five-fold symmetry and cohomological embedding",
      label: "sec:fivefold-symmetry",
      blocks: [
        "fivefold-symmetry",
        "cohomological-embedding",
      ],
    }),
  ],
});
