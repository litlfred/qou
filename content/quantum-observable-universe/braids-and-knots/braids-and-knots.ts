import { chapter, section } from "../../schema/builders";

/**
 * Chapter 3: Braids and Knots.
 *
 * Categorical origin of braiding, braid group representations,
 * SU(2)/SO(3) framework, knot groups, quantum groups, abstract hadron
 * composites and topological mass, Möbius energy, and varying Euler
 * characteristic.
 *
 * Hadron/knot/bundle blocks absorbed from lifting-and-descent §11-12 during
 * chapter restructuring (2026-03).  Proton/neutron definitions moved
 * to the Descartes chapter (Option A: nuclear binding references the
 * abstract hadron, not specific particles).
 * Fluid dynamics and information theory moved to their own chapters.
 */
export default chapter({
  title: "Braids and Knots",
  label: "chap:path-integrals-braiding",
  sections: [
    section({
      title: "Introduction",
      label: "sec:path-integrals-intro",
      blocks: [
        "intro",
      ],
    }),

    section({
      title: "Categorical origin of braiding",
      label: "sec:categorical-braiding",
      blocks: [
        "categorical-braiding-intro",
        "braid-action-tensor",
        "braid-action-tensor-proof",
        "why-b3",
        "categorical-boson-fermion",
        "symmetric-quotient-colour",
        "braid-base-field",
        "braid-lifting-compatibility",
        "jones-markov-trace",
        "hecke-algebra-from-braiding",
        "hecke-normal-form",
        "markov-moves-brane-tower",
        "knot-eigenbasis-complete",
        "knot-eigenbasis-complete-proof",
        "knot-exhaustiveness",
        "feynman-eigenbasis",
      ],
    }),

    section({
      title: "Braid group and symmetric group",
      label: "sec:braid-symmetric",
      blocks: [
        "braid-symmetric-intro",
        "braid-group",
        "braid-group-su2",
        "knot-notation-convention",
      ],
    }),

    section({
      title: "$\\mathrm{SU}(2)$ and $\\mathrm{SO}(3)$ framework",
      label: "sec:su2-so3",
      blocks: [
        "su2-so3-intro",
        "su2-basis",
        "first-order-taylor",
        "su2-generators",
        "so3-generators",
        "quaternion-so3-motivation",
      ],
    }),

    section({
      title: "Braid involutions and holonomy",
      label: "sec:braid-involutions",
      blocks: [
        "braid-involutions-intro",
        "braid-twist-flip",
        "holonomy-trefoil",
        "rho-s3-holonomy-exposition",
      ],
    }),

    section({
      title: "The trefoil knot",
      label: "sec:trefoil-knot",
      blocks: [
        "trefoil-knot-intro",
        "trefoil-knot-group",
        "trefoil-operator-algebra",
      ],
    }),

    section({
      title: "Knot fundamental groups",
      label: "sec:knot-fundamental-groups",
      blocks: [
        "knot-fundamental-groups-intro",
        "knot-complement-group",
        "kronheimer-mrowka",
        "reducible-reps",
      ],
    }),

    section({
      title: "Universal enveloping algebras and quantum groups",
      label: "sec:enveloping-algebras",
      blocks: [
        "enveloping-algebras-intro",
        "enveloping-algebra",
        "quantum-su2",
        "q-casimir",
        "q-casimir-exists",
        "q-casimir-exists-proof",
        "q-casimir-unique",
        "q-casimir-unique-proof",
        "r-matrix-braiding-structure",
        "r-matrix-braiding",
      ],
    }),

    section({
      title: "Categorical Möbius energy and self-avoidance",
      label: "sec:mobius-energy",
      blocks: [
        "mobius-energy",
        "mobius-energy-proof",
        "non-self-intersection",
        "non-self-intersection-proof",
      ],
    }),

    // ── Crossing energy and stability ───────────────────────────────────
    section({
      title: "Crossing energy and Coulomb charge",
      label: "sec:crossing-energy",
      blocks: [
        "crossing-energy",
        "crossing-energy-trefoil",
        "commutative-crossing-energy",
        "coulomb-charge",
        "skein-crossing-asymmetry-prop",
        "skein-crossing-asymmetry",
      ],
    }),

    // ── Lagrange resolvents (categorical DFT) ─────────────────────────
    section({
      title: "Lagrange Resolvents and $q$-Deformed Kinematics",
      label: "sec:lagrange-q-kinematics",
      blocks: [
        // DFT decomposition of cyclic representations
        "lagrange-resolvent-transform",
        "lagrange-resolvents",
        // q-deformed physical quantities (general QOU)
        "q-momentum",
        "q-angular-momentum",
        "q-angular-momentum-interpretation",
        "q-energy",
        "noether-theorem-callout",
      ],
    }),

    // ── Exceptional divisor, Reeb bundle, and vertex operators ────────
    // (P1 split: 19-block sec:vertex-operators-markov → 4 focused sections)
    section({
      title: "Exceptional Divisor and Vertex Operators",
      label: "sec:exceptional-divisor-reeb",
      blocks: [
        "exceptional-divisor",
        "reeb-bundle",
        "reeb-exceptional-divisor",
        "vertex-operator",
        "vertex-operator-dictionary",
      ],
    }),

    // ── Vertex factorisation through E_p ──────────────────────────────
    section({
      title: "Vertex Factorisation and the Markov Trace",
      label: "sec:vertex-factorisation",
      blocks: [
        "vertex-is-exceptional-divisor",
        "vertex-is-exceptional-divisor-proof",
        // Photon polarisation states as Hecke generators on the exceptional divisor
        "breit-wheeler-vertex",
        // Product factorization of the Markov trace
        "markov-trace-product",
        "markov-trace-product-interpretation",
        // Markov chain interpretation of the algebraic framework
        "hecke-markov-transition",
        "hecke-markov-interpretation",
        "markov-lambda-knot-operations",
        "markov-chain-fluctuations",
        // Feynman path integrals as categorical traces
        "feynman-categorical-trace",
        "feynman-categorical-trace-proof",
        "feynman-qou-dictionary",
        "feynman-classical-limit",
        "feynman-classical-limit-interpretation",
      ],
    }),

    // ── Transfer matrix and topological mass ──────────────────────────
    section({
      title: "Transfer Matrix and Topological Mass",
      label: "sec:transfer-matrix-mass",
      blocks: [
        "categorical-transfer-matrix",
        "transfer-matrix-level-independence",
        "transfer-matrix-level-independence-proof",
        "topological-mass-formula",
        "motivic-mass-measure",
        "hecke-mass-element",
        "hecke-mass-trace",
        "hecke-charge-mass-duality",
        "skein-decomposition",
        "topological-field-ansatz",
      ],
    }),

    // ── Braiding relations and the spectral filter ────────────────────
    section({
      title: "Braiding Relations and the Spectral Filter",
      label: "sec:braiding-relations",
      blocks: [
        "skein-archimedean-shadow",
        "vertex-algebra-relations",
        "vertex-algebra-jet-relations",
        "t211-ideal-annihilation",
      ],
    }),

    // ── Hadron algebra and knot factorisation ────────────────────────
    // (P2 split: 20-block sec:hadrons-knot-composites → 3 focused sections)
    section({
      title: "Hadron Algebra and Knot Factorisation",
      label: "sec:hadron-algebra",
      blocks: [
        "hadron",
        "hadron-exists",
        "hadron-exists-proof",
        "hadron-unique",
        "hadron-unique-proof",
        "hadron-interpretation",
        "hadron-operations-closure",
        "hadron-operations",
        "knot-factorization",
        "localized-hadron",
        "hadron-fibre-embedding",
      ],
    }),

    // ── Skein generation and particle correspondence ──────────────────
    section({
      title: "Skein Generation and Particle Correspondence",
      label: "sec:skein-particle-generation",
      blocks: [
        "skein-generation",
        "skein-generation-proof",
        "knot-particle-generation",
        "knot-particle-generation-interpretation",
        "knot-particle-correspondence",
        "knot-particle-dictionary",
      ],
    }),

    // ── Bundle structure and observation ───────────────────────────────
    section({
      title: "Bundle Structure and Observation",
      label: "sec:bundle-observation",
      blocks: [
        "quarks-borromean-picture",
        "bundle-initial-conditions",
        "observation-braid",
        "sorting-color-energy",
        "bundle-isotopy-equivalence",
        "torsion-knot-flow",
        "bundle-category",
      ],
    }),

    // ── Borromean baryons and fermion/boson classification ─────────────
    section({
      title: "Borromean Baryons and Reidemeister Invariance",
      label: "sec:borromean-reidemeister",
      blocks: [
        "borromean-baryon",
        "borromean-baryon-interpretation",
        "typed-crossing-operator",
        "nucleon-hecke-element",
        "hadron-proton-example",
        "fermion-boson-knot-link",
        "reidemeister-mass-invariance",
        "shell-transition-knot",
        "shell-transition-knot-interpretation",
      ],
    }),

    // ── Categorical mass foundations ────────────────────────────────────
    section({
      title: "Categorical Mass Foundations",
      label: "sec:categorical-mass-foundations",
      blocks: [
        "topological-mass",
        "topological-mass-categorical-proof",
        "categorical-mass-markov",
        "markov-z-reconciliation",
        "mass-endomorphism-conjecture",
      ],
    }),

    // ── Calibration and algebraic mass formula ──────────────────────────
    section({
      title: "Calibration and Algebraic Mass Formula",
      label: "sec:calibration-algebraic-mass",
      blocks: [
        "mass-element-nf",
        "calibration-inputs",
        "three-parameters-wedderburn",
        "wedderburn-trace-identity",
        "binding-scale-catalan",
        "wedderburn-mass-formula",
        "frobenius-s-classification",
        "commutative-chirality-vanishes",
        "derived-mass-formula-light-isotopes",
        "deuteron-binding-frobenius-codim",
        "hoefsmit-seminormal-form",
        "figure-eight-branching-rule",
        "figure-eight-bw-coefficients",
        "universal-braid-branching",
        "hoefsmit-scattering-pipeline",
        "hecke-convergence-bound",
        "algebraic-quantum-volume",
        "habiro-ring",
        "habiro-expansion-atomic",
        "algebraic-quantum-volume-specialization",
        "archimedean-realization-functor",
        "vol-through-tau",
        "kashaev-volume-density",
        "kashaev-as-archimedean-realization",
        "quantum-bloch-group",
        "degree-two-baryon-weight",
      ],
    }),

    // ── Atom, isotope, and confinement levels ──────────────────────────
    section({
      title: "Atom, Isotope, and Confinement Levels",
      label: "sec:atom-isotope-confinement",
      blocks: [
        "knot-operator-energy",
        "knot-operator-energy-exists",
        "knot-operator-energy-unique",
        "local-shadow-ordering",
        "confinement-level",
        "confinement-level-exists",
        "confinement-level-unique",
        "confined-particle",
        "confinement-category",
        "electron-shell",
        "dressed-particle",
        "shell-closure-stability",
        "shell-closure-stability-interprets",
        "level-sufficiency",
        "level-sufficiency-interprets",
        "confinement-phase-stratification",
        "phase-scoped-applicability",
        "atom-knot",
        "atom-knot-exists",
        "atom-knot-unique",
        "isotope-knot",
        "isotope-knot-equivalence",
        "stable-atom",
        "stable-atom-decidable",
        "unstable-atom",
        "unstable-atom-decay-channel",
        "ilp-solution-count-unwrap",
        "shell-schur-weyl-self-duality",
        "compound-beta-shell-calibration",
      ],
    }),

    // ── Nuclear binding and beta stability ──────────────────────────────
    section({
      title: "Nuclear Binding and Beta Stability",
      label: "sec:nuclear-binding-beta-stability",
      blocks: [
        "confined-knot-binding",
        "jet-filtered-knot-factor",
        "jet-convergence-classical-limit",
        "wigner-np-pairing",
        "unified-iterative-correction",
        "knot-factor-frobenius-pairing",
        "hook-weight-derivation",
        "wigner-coefficient-derivation",
        "bw-coefficient-shadow-price",
        "wigner-2-coefficient",
        "mass-endomorphism-tower",
        "mass-endomorphism-jet-tower",
        "schur-weyl-mass-decomposition",
        "gb-residue-spectral-sum",
        "residue-as-braid-holonomy",
        "graded-trace-residue-split",
        "full-pole-structure-mass-trace",
        "mn-classical-parity-blind",
        "q-character-closes-parity-gap",
        "frobenius-codim-universal",
        "frobenius-limits-substrate-cost",
        "knot-mass-formula-unified",
        "partition-sum-proton-residual",
        "np-discrepancy-resolution",
        "mass-formula-regime-switching",
        "jet-prefix-gb-filtration",
        "chirality-from-frobenius-self-pairing",
        "gb-spectral-sequence",
        "curvature-rank-gb-stratification",
        "spectral-sequence-collapse",
        "confinement-categorical",
        "exterior-square-borromean",
        "alpha-em-categorical-trace",
        "plancherel-term-7-formulation",
        "plancherel-weight-boundedness",
        "unified-curvature-rank-mass-formula",
        "b-over-a-spectral-decomposition",
        "chirality-residue-mass-term",
        "e-infinity-page-identifications",
        "spectral-sequence-h3-explicit",
        "chirality-writhe-ribbon-derivation",
        "gram-matrix-spectral-connection",
        "knot-factor-spectral-derivation",
        "knot-factor-amphicheiral",
        "knot-factor-borromean-composite",
        "knot-factor-shell-closed",
        "knot-factor-spectral-summary",
        "pauli-factor-wedderburn",
        "mass-formula-wedderburn-enumeration",
        "mass-tower-coefficient-stratification",
        "alpha-k-derivation-procedure",
        "explicit-alpha-k-h3",
        "y-lambda-sign-pattern",
        "terms-2-6-higher-operations",
        "six-term-mass-formula-complete",
        "shell-correction-term-seven",
        "chirality-dual-space-derivation",
        "frobenius-antipode-unifies-chirality-and-tower",
        "deuteron-first-principles",
        "markov-pair-z2",
        "pentagon-uv-commutation",
        "descended-level-zero",
        "jet-tower-convergence",
        "delta-max-uniform-bound",
        "mass-tower-syt-cells",
        "energy-scale-planck",
        "topological-mass-trefoil",
        "skein-binding-lagrangian",
        "beta-stability",
        "beta-stability-interpretation",
      ],
    }),

    // ── Varying Euler + mirror bundle (merged — 2+2 blocks + genus-2) ─
    section({
      title: "Varying Euler Characteristic and the Mirror Bundle",
      label: "sec:varying-euler-mirror",
      blocks: [
        "varying-euler-intro",
        "genus-2-intro",
        // ── Commutative-limit / genus-2 Track A ─────────────────────
        "commutative-qou",
        "hyperelliptic-quintic",
        "hyperelliptic-z5-classification",
        "x5-z5-automorphism",
        "bring-z5-descent",
        "x5-bring-weight-identification",
        "x5-bring-prym-jacobian",
        "weight-identification-consequences",
        "u1-equivariant-reduction",
        "u1-phase-tube",
        // ── Mirror bundle ───────────────────────────────────────────
        "descent-mirror-intro",
        "e-minus-one",
      ],
    }),
  ],
});
