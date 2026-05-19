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

    // ── §1a. Bring's surface as a QOU ────────────────────────────────
    // (P5 split: 31-block sec:brings-geometry → 4 focused sections)
    section({
      title: "Bring's surface as a QOU",
      label: "sec:brings-surface-qou",
      blocks: [
        "brings-surface-qou-intro",
        "brings-surface",
        "brings-surface-example",
        "brings-realisations",
        "brings-physics-interpretations",
        "brings-is-qou",
        "brings-euler-characteristic",
        "brings-euler-characteristic-proof",
        "brings-riemann-hurwitz",
        "brings-riemann-hurwitz-proof",
        "brings-is-qou-proof",
        "brings-qou-4tuple",
        "brings-qou-axiom-map",
        "braid-group-action",
      ],
    }),

    // ── §1b. Color tube coordinates ───────────────────────────────────
    section({
      title: "Color tube coordinates",
      label: "sec:color-tube-coords",
      blocks: [
        "color-tube-coords-intro",
        "color-tube-coordinates",
        "aggregate-color-quantities",
        "color-tube-constraints",
        "color-tube-interpretation",
        "c5-color-tube",
        "intrinsic-color-cubic-pairing",
      ],
    }),

    // ── §1c. Coral fibration and elliptic curves ──────────────────────
    section({
      title: "Coral fibration and elliptic curves",
      label: "sec:coral-fibration-elliptic",
      blocks: [
        "coral-fibration-elliptic-intro",
        "coral-elliptic",
        "coral-elliptic-proof",
        "t-duality-elliptic",
        "color-tube-cubic",
        "color-tube-fibers",
        "t-duality-color-tube",
        "color-tube-subloci",
        "pure-colour-sublocus",
      ],
    }),

    // ── §1d. Bundle structures and smoothness ─────────────────────────
    section({
      title: "Bundle structures and smoothness",
      label: "sec:brings-smoothness",
      blocks: [
        "brings-smoothness-intro",
        "coral-bundles",
        "brings-smoothness-resolution",
        "brings-smoothness",
        // Absorbed from former Ch `encounter` (now dissolved): the
        // base-M↔fibre-S_p exposition and the Thurston / hyperbolic
        // relaxation narrative live here, adjacent to the descartes
        // geometric machinery they bridge.
        "approach-to-exceptional-divisor",
        "thurston-relaxation",
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
        "spectral-gauge-intro",
        // Quaternionic spectral resolvents (minus SO(3) motivation → braids-and-knots)
        "quaternionic-spectral-resolvents",
        "omega-constraints",
        "spectral-dynamics",
        // Seiberg--Witten on Bring's
        "generation-dependent-sw",
        "lepton-mass-integrals",
        "mi-sw-abelianisation",
        "mi-sw-abelianisation-cartan",
        "mi-sw-abelianisation-cartan-proof",
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
        "descartes-condition-intro",
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
        "genus-from-hecke-completeness",
        "genus-from-hecke-completeness-proof",
        "chebyshev-degree-genus",
        "chebyshev-degree-genus-proof",
        "genus-ideal-characterisation",
        "genus-ideal-characterisation-proof",
        "yekutieli-leading-coefficient",
        "yekutieli-leading-coefficient-proof",
        "genus-filtration-ideal",
        "genus-filtration-ideal-proof",
        "genus-filtration-interpretation",
        "torus-embeddable-complete",
        "generation-completeness",
      ],
    }),

    // ── §3b. Fundamental particles ────────────────────────────────────
    // ── Unit particle as a cohomological defect ─────────────────────
    // Absorbed from former `algebraic-substrate / sec:cohomological-defect`
    // (now dissolved). The unit particle IS a particle; defects belong
    // adjacent to the fundamental-particles section below.
    section({
      title: "The unit particle as a cohomological defect",
      label: "sec:cohomological-defect",
      blocks: [
        "cohomological-defect-intro",
        "levi-form-defect",
        "maximal-ideal-defect",
        "local-cohomology-group",
        "unit-particle-state",
        "topological-charge-quantization",
        "defect-legendrian-knot",
      ],
    }),

    // ── Fundamental particles (P3 split 2026-05-19): the 71-block
    //    sec:fundamental-particles is split into 7 topical sub-sections
    //    matching the ascending pedagogy: fermions → operations →
    //    mesons/nucleons → stability → EM coupling → archimedean
    //    Hartree/crystal → integer Diophantine endgame. The existing
    //    fundamental-particles-intro stays at the top of A as the
    //    umbrella narrative.

    // §A — Fundamental fermions
    section({
      title: "Fundamental fermions",
      label: "sec:fundamental-fermions",
      blocks: [
        "fundamental-particles-intro",
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
      ],
    }),

    // §B — Pair production and knot-operator selection
    section({
      title: "Pair production and knot-operator selection",
      label: "sec:pair-production-knot-operators",
      blocks: [
        // q-deformed kinematics (definitions in braids-and-knots; applied here)
        "q-value-transition",
        // Pair production and quark-antiquark creation
        "breit-wheeler-pair-production",
        "quark-antiquark-production",
        // Knot operator selection and Frobenius Gram matrix
        "knot-operator-selection",
        "frobenius-gram-matrix",
      ],
    }),

    // §C — Mesons and nucleons
    section({
      title: "Mesons and nucleons",
      label: "sec:mesons-nucleons",
      blocks: [
        // Meson, proton, neutron
        "categorical-meson",
        "meson-formation-chain",
        "categorical-proton",
        "categorical-proton-exists",
        "categorical-proton-exists-proof",
        "categorical-proton-unique",
        "categorical-proton-unique-proof",
        "meson-to-proton-via-borromean",
        "categorical-neutron",
        "categorical-neutron-exists",
        "categorical-neutron-exists-proof",
        "categorical-neutron-unique",
        "categorical-neutron-unique-proof",
        "antiparticle-crossing-reversal",
        "chirality-trefoil-electron-positron",
      ],
    }),

    // §D — Stable nucleus and torus knots
    section({
      title: "Stable nucleus and torus knots",
      label: "sec:stable-nucleus-torus-knots",
      blocks: [
        "stable-nucleus",
        "torus-hopf-stability",
        "unmapped-torus-knots",
        "torus-knot-prime-powers",
        "force-knot-identification",
        "torus-knot-genus-four-unique",
        "force-carrier-bring-uniqueness",
      ],
    }),

    // §E — EM completeness and gauge coupling
    section({
      title: "EM completeness and gauge coupling",
      label: "sec:em-completeness-gauge-coupling",
      blocks: [
        "force-carrier-spectral-interpretation",
        "em-spectral-completeness",
        "gauge-coupling-uniqueness",
        "em-completeness-interpretation",
        "em-coupling-projection",
        "em-coupling-chern-simons",
        "gram-determinant-plancherel-ratio",
        "gram-kappa-spectral-interpretation",
        "chern-simons-as-knot-invariant",
        "alpha-em-derivation-open-problems",
        "em-coupling-bring-zero-mode",
        "alpha-em-derivation-exploration-options",
        "e-hartree-categorical-derivation",
        "bohr-radius-categorical",
      ],
    }),

    // §F — Archimedean Hartree, crystal basis, and Mathlib bridge
    section({
      title: "Archimedean Hartree, crystal basis, and Mathlib bridge",
      label: "sec:archimedean-hartree-crystal",
      blocks: [
        "archimedean-hartree-derivation",
        "archimedean-functor-uniqueness",
        "bring-hyperbolic-knot-bloch-decomposition",
        "mass-tower-open-problems-classes",
        "crystal-basis-resolves-mass-tower-open-problems",
        "type-b-folded-crystal-combinatorics",
        "clausen-function-mathlib-filler",
        "bloch-wigner-mathlib-filler",
        "mass-tower-deeper-fillers",
        "three-substantive-mathlib-fillers",
        "bloch-group-quotient-construction",
        "cl2-pentagon-and-faddeev-partial",
        "upstream-mathlib-additions",
        "alpha-em-categorical-trace-ratio",
        "alpha-em-shift-multiplicative-chain",
        "q-chromaticity",
        "schrodinger-color-falsifiability",
      ],
    }),

    // §G — Integer stability and Diophantine valley
    section({
      title: "Integer stability and the Diophantine valley",
      label: "sec:integer-stability-diophantine",
      blocks: [
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
        "nuclear-stability-decay-intro",
        // Beta decay as categorical Skein operation
        "beta-decay-skein",
        "lepton-number-categorical",
        // Lepton tower NF and tau decay universality
        "lepton-continuant-recurrence",
        "lepton-tower-witness",
        "tau-leptonic-universality",
        "tau-branching-ratio-witness",
        "parity-violation-skein",
        "nuclear-spin-parity",
        // Half-life calculations via Gröbner reductions
        "hadron-half-life",
        "hadron-q-self-correction",
        "skein-coulomb-enhancement",
        // NOTE: nuclear-groebner-reduction, groebner-shirshov-energy,
        // box-braid-irreducibility, generator-volume-decomposition,
        // markov-trace-factorization, skein-polynomial-transfer-matrix,
        // transfer-matrix-operator, beta-decay-transfer-matrix,
        // beta-decay-interpretation, nucleon-nf-observability,
        // beta-decay-energy-scale, beta-decay-braid-visualizer
        // are referenced from particle-interactions.ts (their canonical
        // home). Listing them here too caused multiply-defined LaTeX
        // labels.
        // NF computation and shell corrections
        "groebner-nf-computation",
        "nf-computation-strategy",
        "kummer-shell-closure",
        "skein-shell-correction",
      ],
    }),

    // ── §3d. Atomic shells and the periodic table ─────────────────────
    section({
      title: "Atomic shells and the periodic table",
      label: "sec:atomic-shells",
      blocks: [
        "atomic-shells-intro",
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
        "rj-canonical-inner-product",
        "rj-inner-product-interpretation",
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
        "descartes-theorem-intro",
        "descartes",
        "descartes-proof",
        "terminal-morphism-brings",
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
        // Volume tower and Picard-Lefschetz decomposition (archimedean shadow only)
        "picard-lefschetz-thimble",
        "volume-tower-decomposition",
        "cs-evaluation-faithfulness",
        // Transcendence and algebraic independence
        "hyperbolic-volume-transcendence",
        "single-volume-irrationality",
        "borel-zagier-qou-volumes",
        "formal-chain-transcendence-remark",
        "yekutieli-transcendence-shadow",
        "implications-algebraic-independence",
        "implications-algebraic-dependence",
        // Baryon periods and integration limits
        "baryon-product-from-alt",
        "baryon-period-conjecture",
        "baryon-integration-limit",
        "mobius-golden-fixed-points",
        "golden-skew-dual-node",
        "bar-self-dual-confinement-band",
        "bar-t-duality-substrate",
        "bar-apply-transfer",
        "golden-quartet-galois",
        "moduli-symmetry-d4",
        "mobius-limit-from-thimble",
        "morse-wall-q-moduli",
        "delta-lambda-categorical-closure",
        // Categorical Markov-Frobenius ≡ algebraic residue (PL = archimedean shadow)
        "sw-period-thimble-equivalence",
        "jet-gb-pl-correspondence",
        // Algebraic-geometric duality with SW theory
        "gb-reduction-pl-thimble-bijection",
        "denominator-zeros-as-sw-critical-points",
        "abelianisation-at-algebraic-poles",
      ],
    }),
    // ── §5. Orbital symmetry and cohomological embedding ────────────
    // Merged (P9): sec:orbital-space (2 blocks) + sec:fivefold-symmetry (2 blocks).
    // Originally moved from quantum-observable-universes (R1) to avoid
    // forward refs to braids-and-knots.
    section({
      title: "Orbital Symmetry and Cohomological Embedding",
      label: "sec:orbital-symmetry-embedding",
      blocks: [
        "orbital-symmetry-embedding-intro",
        "orbital-space-normal-bundle",
        "orbital-fourier-decomposition",
        "fivefold-symmetry",
        "cohomological-embedding",
        "knot-basis-color-content",
        "trivial-knot-photon-interpretation",
      ],
    }),
  ],
});
