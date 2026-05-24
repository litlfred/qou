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
  label: "chap:archimedean-universe",
  sections: [
    // ── Preamble (does not count as a numbered section) ──────────────
    section({
      title: "Why this universe",
      label: "sec:archimedean-preamble",
      blocks: [
        "archimedean-preamble",
      ],
    }),

    // ── §0. Physical regimes and limiting context ────────────────────
    // R2: Imported from models-of-qous/ per the fit-section-chapter
    // audit on PR #882 (2026-05-22).  These blocks were previously
    // sitting in sec:archimedean-models but explicitly preview Bring's-
    // surface / χ = −6 / cosmological-limit material; they belong in
    // this chapter as physical-context framing before the formal
    // development begins.
    section({
      title: "Physical regimes and limiting context",
      label: "sec:physical-regimes",
      blocks: [
        "physical-regimes-intro",
        "brings-surface-unit-circle",
        "seiberg-witten",
        "primordial-vortex",
        "geometric-drag",
      ],
    }),

    // ── §0a. Algebraic substructure of Bring's surface ───────────────
    // Relocated from braids-and-knots/ per the PR #823 fit-section-
    // chapter audit. These blocks supply the algebraic infrastructure
    // (hyperelliptic quintic, Z_5 automorphism, Lagrange resolvent,
    // binary-dihedral SU(2) lifting, weight identification) that the
    // subsequent §1 Bring's-surface-as-QOU sections build on.
    section({
      title: "Bring's surface algebraic substructure",
      label: "sec:bring-algebraic-substructure",
      blocks: [
        "bring-algebraic-substructure-intro",
        "su2-generators",
        "hyperelliptic-quintic",
        "x5-z5-automorphism",
        "x5-bring-weight-identification",
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
    // Was: one 84-block section. Split R4 (navigability) reduced to
    // 28 blocks; further split R6/P13 (2026-05-22) below produces
    // 3 sub-sections each in the 3-18 band.
    section({
      title: "The Descartes condition $\\chi = -6$",
      label: "sec:archimedean-condition-statement",
      blocks: [
        "archimedean-condition-intro",
        // The Descartes condition (χ = −6)
        "descent-to-zero",
        "archimedean-condition",
        "chi-minus-six-chain",
        "archimedean-calabi-yau",
        "descent-one-dim",
        "genus-maximal-descent",
        "genus-maximal-descent-proof",
      ],
    }),
    section({
      title: "Descartes condition: leptons and chirality",
      label: "sec:archimedean-condition-leptons",
      blocks: [
        "archimedean-condition-leptons-intro",
        "archimedean-leptons",
        "archimedean-chirality",
        "light-cone-affine",
        "chirality-trefoil",
        "brings-curve",
      ],
    }),
    section({
      title: "Descartes condition: torus-knot generators and genus completeness",
      label: "sec:archimedean-condition-genus-completeness",
      blocks: [
        "archimedean-condition-genus-intro",
        "torus-knot-generators",
        // Detangler R3 (2026-05-23): 6-row admissible-torus-knot-
        // generators table extracted from torus-knot-generators.md.
        "torus-knot-generators-table-data",
        "embeddability-closure",
        "embeddability-closure-table-data",
        "genus-from-hecke-completeness",
        "genus-from-hecke-completeness-proof",
        "chebyshev-degree-genus",
        "chebyshev-degree-genus-proof",
        "genus-ideal-characterisation",
      ]),
    }),
    section({
      title: "Descartes condition: torus-knot generators and genus completeness : characterisation",
      label: "sec:archimedean-condition-genus-completeness-genus-ideal-characterisation",
      blocks: [
        "archimedean-condition-genus-completeness-genus-ideal-characterisation-intro",
        "genus-ideal-characterisation-proof",
        "yekutieli-leading-coefficient",
        "yekutieli-leading-coefficient-proof",
        "genus-filtration-ideal",
        "genus-filtration-ideal-table2-data",
        "genus-filtration-ideal-table1-data",
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

        "linking-relations-table-table1-data",
        "linking-relations-table-table2-data",
        "linking-relations-table-table3-data",
        "linking-relations-table-table4-data",
        "linking-relations-table-table5-data",
      ],
    }),

    // §B — Pair production and knot-operator selection
    section({
      title: "Pair production and knot-operator selection",
      label: "sec:pair-production-knot-operators",
      blocks: [
"intro-pair-production-knot-operators",
                // q-deformed kinematics (definitions in braids-and-knots; applied here)
        "q-value-transition",
        // Pair production and quark-antiquark creation
        "breit-wheeler-pair-production",
        "breit-wheeler-pair-production-table-data",
        "quark-antiquark-production",
        // Knot operator selection and Frobenius Gram matrix
        "knot-operator-selection",
        "frobenius-gram-matrix",

        "frobenius-gram-matrix-table1-data",
        "frobenius-gram-matrix-table2-data",
      ],
    }),

    // §C — Mesons and nucleons
    section({
      title: "Mesons and nucleons",
      label: "sec:mesons-nucleons",
      blocks: [
"intro-mesons-nucleons",
                // Meson, proton, neutron
        "categorical-meson",
        "meson-formation-chain",
        "categorical-proton",
        "categorical-proton-table3-data",
        "categorical-proton-table2-data",
        "categorical-proton-table1-data",
        "categorical-proton-exists",
        "categorical-proton-exists-proof",
        "categorical-proton-unique",
      ]),
    }),
    section({
      title: "Mesons and nucleons : characterisation",
      label: "sec:mesons-nucleons-categorical-proton-unique",
      blocks: [
        "mesons-nucleons-categorical-proton-unique-intro",
        "categorical-proton-unique-proof",
        "meson-to-proton-via-borromean",
        "categorical-neutron",
        "categorical-neutron-table-data",
        "categorical-neutron-table-data",
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
"intro-stable-nucleus-torus-knots",
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
"intro-em-completeness-gauge-coupling",
                "force-carrier-spectral-interpretation",
        "em-spectral-completeness",
        "gauge-coupling-uniqueness",
        "em-completeness-interpretation",
        "em-coupling-projection",
        "em-coupling-projection-table2-data",
        "em-coupling-projection-table1-data",
        "em-coupling-chern-simons",
        "gram-determinant-plancherel-ratio",
        "gram-kappa-spectral-interpretation",
        "chern-simons-as-knot-invariant",
        "alpha-em-derivation-open-problems",
        "em-coupling-bring-zero-mode",
        "alpha-em-derivation-exploration-options",
        // Detangler R3 (2026-05-23): 7-row ingredient-source map
        // extracted from alpha-em-derivation-exploration-options.md.
        "alpha-em-derivation-exploration-options-table-data",
      ]),
    }),
    section({
      title: "EM completeness and gauge coupling : characterisation",
      label: "sec:em-completeness-gauge-coupling-e-hartree-categorical",
      blocks: [
        "em-completeness-gauge-coupling-e-hartree-categorical-intro",
        "e-hartree-categorical-derivation",

        "e-hartree-categorical-derivation-table1-data",
        "e-hartree-categorical-derivation-table2-data",
        "e-hartree-categorical-derivation-table3-data",
        "e-hartree-categorical-derivation-table4-data",
        "e-hartree-categorical-derivation-table5-data",
        "e-hartree-categorical-derivation-table6-data",
        "e-hartree-categorical-derivation-table7-data",
        "e-hartree-categorical-derivation-table8-data",
        "e-hartree-categorical-derivation-table9-data",
        "e-hartree-categorical-derivation-table10-data",
        "e-hartree-categorical-derivation-table11-data",
        "e-hartree-categorical-derivation-table12-data",
        "e-hartree-categorical-derivation-table13-data",
        "bohr-radius-categorical",
      ],
    }),

    // §F — Archimedean Hartree, crystal basis, and Mathlib bridge
    section({
      title: "Archimedean Hartree, crystal basis, and Mathlib bridge",
      label: "sec:archimedean-hartree-crystal",
      blocks: [
"intro-archimedean-hartree-crystal",
                "archimedean-hartree-derivation",
        "archimedean-functor-uniqueness",
        "bring-hyperbolic-knot-bloch-decomposition",
        "mass-tower-open-problems-classes",
        "crystal-basis-resolves-mass-tower-open-problems",
        "type-b-folded-crystal-combinatorics",
        "type-b-folded-crystal-combinatorics-table-data",
        "clausen-function-mathlib-filler",
        "clausen-function-mathlib-filler-table2-data",
        "clausen-function-mathlib-filler-table1-data",
        "bloch-wigner-mathlib-filler",
        "bloch-wigner-mathlib-filler-table3-data",
        "bloch-wigner-mathlib-filler-table2-data",
        "bloch-wigner-mathlib-filler-table1-data",
      ]),
    }),
    section({
      title: "Archimedean Hartree, crystal basis, and Mathlib bridge : characterisation",
      label: "sec:archimedean-hartree-crystal-mass-tower-deeper",
      blocks: [
        "archimedean-hartree-crystal-mass-tower-deeper-intro",
        "mass-tower-deeper-fillers",
        "three-substantive-mathlib-fillers",
        "bloch-group-quotient-construction",
        "bloch-group-quotient-construction-table-data",
        "cl2-pentagon-and-faddeev-partial",
        "cl2-pentagon-and-faddeev-partial-table3-data",
        "cl2-pentagon-and-faddeev-partial-table2-data",
        "cl2-pentagon-and-faddeev-partial-table1-data",
        "upstream-mathlib-additions",
      ]),
    }),
    section({
      title: "Archimedean Hartree, crystal basis, and Mathlib bridge (continued) : characterisation",
      label: "sec:archimedean-hartree-crystal-alpha-em-categorical",
      blocks: [
        "archimedean-hartree-crystal-alpha-em-categorical-intro",
        "upstream-mathlib-additions-table2-data",
        "upstream-mathlib-additions-table1-data",
        "alpha-em-categorical-trace-ratio",
        // Detangler R3 (2026-05-23): 6-row numerical-verification
        // table extracted from alpha-em-categorical-trace-ratio.md.
        "alpha-em-categorical-trace-ratio-table-data",
        "alpha-em-shift-multiplicative-chain",
        "q-chromaticity",
        "schrodinger-color-falsifiability",
        "schrodinger-color-falsifiability-table4-data",
        "schrodinger-color-falsifiability-table3-data",
        "schrodinger-color-falsifiability-table2-data",
        "schrodinger-color-falsifiability-table1-data",
      ],
    }),

    // §G — Integer stability and Diophantine valley
    section({
      title: "Integer stability and the Diophantine valley",
      label: "sec:integer-stability-diophantine",
      blocks: [
"intro-integer-stability-diophantine",
                "integer-stability",
        "diophantine-valley",
        "diophantine-valley-table-data",
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
        "lepton-tower-witness-table-data",
        "tau-leptonic-universality",
        "tau-branching-ratio-witness",
        "tau-branching-ratio-witness-table2-data",
        "tau-branching-ratio-witness-table1-data",
        "parity-violation-skein",
        "nuclear-spin-parity",
        "nuclear-spin-parity-table-data",
        // Half-life calculations via Gröbner reductions
      ]),
    }),
    section({
      title: "Nuclear stability and decay : characterisation",
      label: "sec:nuclear-stability-decay-hadron-half-life",
      blocks: [
        "nuclear-stability-decay-hadron-half-life-intro",
        "hadron-half-life",
        "hadron-q-self-correction",
        "hadron-q-self-correction-table-data",
        "skein-coulomb-enhancement",
        "skein-coulomb-enhancement-table1-data",
        "skein-coulomb-enhancement-table2-data",
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
        "groebner-nf-computation-table3-data",
        "groebner-nf-computation-table2-data",
        "groebner-nf-computation-table1-data",
        "nf-computation-strategy",
        "kummer-shell-closure",
        "skein-shell-correction",
        "skein-shell-correction-table-data",
      ],
    }),

    // ── §3d. Atomic shells and the periodic table ─────────────────────
    // Detangler P14 split (2026-05-23): 22-block sec:atomic-shells
    // split into shell-construction foundations + per-element instances.
    section({
      title: "Atomic shells: construction foundations",
      label: "sec:atomic-shells-foundations",
      blocks: [
        "atomic-shells-intro",
        "shell-structure-eigenvalues",
        "shell-eigenvalue-properties",
        "quantum-dilogarithm-volume",
        "reidemeister-action-table",
        "topology-geometry-boundary",
        "topology-geometry-boundary-table-data",
        // Elliptic stability conjecture
        "elliptic-stability-locus",
        "shell-closure-normal-form",
        "shell-closure-normal-form-table5-data",
        "shell-closure-normal-form-table4-data",
        "shell-closure-normal-form-table3-data",
        "shell-closure-normal-form-table2-data",
        "shell-closure-normal-form-table1-data",
        "torus-knot-shell-binding",

      ]),
    }),
    section({
      title: "Atomic shells: construction foundations : characterisation",
      label: "sec:atomic-shells-foundations-skein-finiteness-bound",
      blocks: [
        "atomic-shells-foundations-skein-finiteness-bound-intro",
        "torus-knot-shell-binding-table1-data",
        "torus-knot-shell-binding-table2-data",
        "torus-knot-shell-binding-table3-data",
        "skein-finiteness-bound",
        "skein-finiteness-bound-table4-data",
        "skein-finiteness-bound-table3-data",
        "skein-finiteness-bound-table2-data",
        "skein-finiteness-bound-table1-data",
        "rj-canonical-inner-product",
        "rj-inner-product-interpretation",
        "spectral-decomposition-qvalue",
        "spectral-decomposition-qvalue-table3-data",
        "spectral-decomposition-qvalue-table2-data",
        "spectral-decomposition-qvalue-table1-data",
        "shell-construction-rules",
      ],
    }),
    section({
      title: "Atomic shells: per-element instances",
      label: "sec:atomic-shells-element-instances",
      blocks: [
        "atomic-shells-element-instances-intro",
        "electron-shells-hopf",
        "helium-hopf-diagram",
        "noble-gas-characterization",
        "noble-gas-characterization-table-data",
        "metallic-character-knot",
        "francium-extremal-metal",
        "francium-extremal-metal-table-data",
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
        "archimedean-yekutieli",
        "observation-brings",
      ],
    }),

    // ── §4. Topological mass and the knot-particle spectrum ──────────
    // Detangler P15 split (2026-05-22): the 32-block
    // sec:topological-mass-spectrum was split into 3 sub-sections,
    // each in the 3-18 block band: formula+transcendence (11),
    // Galois-baryon-periods (10), PL-SW-duality (11).
    section({
      title: "Topological mass and volume-tower transcendence",
      label: "sec:topological-mass-formula-transcendence",
      blocks: [
        // Topological mass (Descartes-specific applications)
        "topological-mass-formula-transcendence-intro",
        "hyperbolic-volumes-prose",
        // Skein decomposition and hadronic mass
        "intro",
        "terminal-resolution",
        // Knot-to-particle mass spectrum
        "knot-formula-table",

        "knot-formula-table-table1-data",
        "knot-formula-table-table2-data",
        "knot-formula-table-table3-data",
        "knot-formula-table-table4-data",
        "knot-formula-table-table5-data",
        "mass-from-generators",
        // Volume tower and Picard-Lefschetz decomposition (archimedean shadow only)
        "picard-lefschetz-thimble",
        "volume-tower-decomposition",
        "cs-evaluation-faithfulness",
        // Transcendence and algebraic independence
        "hyperbolic-volume-transcendence",
        "single-volume-irrationality",
        "borel-zagier-qou-volumes",
      ],
    }),
    section({
      title: "Topological mass: Galois orbit and baryon periods",
      label: "sec:topological-mass-galois-baryons",
      blocks: [
        "topological-mass-galois-baryons-intro",
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
        "golden-skew-dual-node-table-data",
      ],
    }),
    section({
      title: "Topological mass: PL-SW algebraic-geometric duality",
      label: "sec:topological-mass-pl-sw-duality",
      blocks: [
        "topological-mass-pl-sw-duality-intro",
        "bar-self-dual-confinement-band",
        "bar-t-duality-substrate",
        "bar-apply-transfer",
        "golden-quartet-galois",
        "moduli-symmetry-d4",
        "mobius-limit-from-thimble",
        "morse-wall-q-moduli",
        "delta-lambda-categorical-closure",
        // Categorical Markov-Frobenius ≡ algebraic residue (PL = archimedean shadow)
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
        "fivefold-symmetry-table2-data",
        "fivefold-symmetry-table1-data",
        "cohomological-embedding",

        "cohomological-embedding-table1-data",
        "cohomological-embedding-table2-data",
        "knot-basis-color-content",
        "trivial-knot-photon-interpretation",
        "trivial-knot-photon-interpretation-table5-data",
        "trivial-knot-photon-interpretation-table4-data",
        "trivial-knot-photon-interpretation-table3-data",
        "trivial-knot-photon-interpretation-table2-data",
        "trivial-knot-photon-interpretation-table1-data",
        "outro-archimedean-universe",
      ],
    }),
  ],
});
