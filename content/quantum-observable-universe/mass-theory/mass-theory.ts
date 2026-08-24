import { chapter, section } from "../../schema/builders";

/**
 * Mass Analysis.
 *
 * The detailed geometric, archimedean, and physical faces of the
 * mass endomorphism. Consumes the algebraic core (stated in "The
 * Mass Endomorphism" chapter, before Particles) and applies it to
 * specific knots, isotopes, and observables.
 *
 * Sections:
 *   - Algebraic: transfer matrices, mass-formula derivation,
 *     Hoefsmit construction, GS axiomatic backing
 *   - Geometric: vertex factorisation, Kashiwara-Jones, quantum
 *     dilogarithm, archimedean realization, Kashaev volume,
 *     mass-volume factorisation, crossing expansion
 *   - Archimedean: substrate binding, LP-dual, spectral sequence,
 *     Plancherel, α_k derivation, Wenzl bridge
 *   - Physical: parity classification, six-term formula,
 *     mass predictions, binding energy
 *   - Open problems: crystal basis, mass-tower directions
 */
export default chapter({
  title: "Mass Analysis",
  label: "chap:mass-theory",
  sections: [


    // ═══ ALGEBRAIC FACE ═════════════════════════════════════════
    // Wedderburn, Frobenius pairing, transfer matrices, Hecke
    // characters, Hoefsmit construction, GS axiomatic backing.
    // ── §2 Algebraic face: Transfer Matrix and Topological Mass ────
    section({
      title: "Transfer Matrix and Topological Mass",
      label: "sec:transfer-matrix-mass",
      blocks: [
        "transfer-matrix-mass-intro",
        "categorical-transfer-matrix",
        "categorical-transfer-matrix-properties",
        "transfer-matrix-level-independence",
        "tmli-constituent-composite-agreement",
        "tmli-constituent-composite-agreement-proof",
        "transfer-matrix-level-independence-proof",
        "topological-mass-formula",
        "topological-mass-formula-context",
        "motivic-mass-measure",
        "motivic-mass-rationale",
        "hecke-mass-element",
        "hecke-mass-trace",
        "hecke-mass-trace-proof",
        "hecke-generator-poly-reduction",
        "hecke-generator-poly-reduction-proof",
        "hecke-charge-mass-duality",
        "skein-decomposition",
        "topological-field-ansatz",
        "topological-field-ansatz-table-data",
      ],
    }),

    section({
      title: "Mass-formula derivation",
      label: "sec:mass-formula-derivation",
      blocks: [
        "calibration-algebraic-mass-intro",
        "mass-element-nf",
        "calibration-inputs",
        "three-calibration-inputs",
        "three-calibration-inputs-proof",
        "three-calibration-inputs-context",
        "two-tier-scaling-pq",
        "three-parameters-wedderburn",
        "three-parameters-wedderburn-context",
        "wedderburn-trace-identity",
        "wedderburn-trace-identity-context",
        "wedderburn-trace-identity-proof",
        "binding-scale-catalan",
        "binding-scale-catalan-proof",
        "binding-error-amplification",
        "binding-error-amplification-proof",
        "deuteron-fusion-frame",
        "frakD-energy-decomposition",
        "wedderburn-mass-formula",
        "wedderburn-mass-formula-proof",
        "frobenius-s-classification",
        "frobenius-s-classification-proof",
        "frobenius-s-classification-table3-data",
      ],
    }),

    section({
      title: "Mass-formula derivation (generation)",
      label: "sec:mass-formula-derivation-commutative-chirality-vanishes",
      blocks: [
        "mass-formula-derivation-commutative-chirality-vanishes-intro",
        "frobenius-s-classification-table2-data",
        "frobenius-s-classification-table1-data",
        "commutative-chirality-vanishes",
        "commutative-chirality-vanishes-proof",
        "commutative-chirality-vanishes-interpretation",
        "derived-mass-formula-light-isotopes",
        "derived-mass-formula-light-isotopes-proof",
        "derived-mass-formula-light-isotopes-context",
        "derived-mass-formula-light-isotopes-table1-data",
        "derived-mass-formula-light-isotopes-table2-data",
        "hoefsmit-seminormal-form",
        "hoefsmit-seminormal-form-proof",
        "figure-eight-branching-rule",
        "figure-eight-branching-rule-proof",
        "figure-eight-branching-rule-table2-data",
        "figure-eight-branching-rule-table1-data",
      ],
    }),

    // §algebraic: transfer matrix, Skein mass, Markov trace corrections
    section({
      title: "Algebraic face: transfer matrices, Skein mass, and Markov corrections",
      label: "sec:mass-algebraic-consolidated",
      blocks: [
        "mass-algebraic-consolidated-intro",
      ],
      // Over-weight split (P4): 30-block algebraic-face section into 4
      // reading-order sub-arcs (the compound title's three themes plus
      // the Q_beta and filtration tails). Order preserved; parent keeps
      // the intro.
      subsections: [
        section({
          title: "Transfer matrices and Skein mass",
          label: "sec:mass-algebraic-transfer-skein",
          blocks: [
            "transfer-matrix-operator",
            "transfer-matrix-operator-properties",
            "skein-polynomial-transfer-matrix",
            "skein-polynomial-transfer-matrix-proof",
            "beta-decay-transfer-matrix",
            "beta-decay-transfer-matrix-proof",
            "transfer-matrix-identities",
            "transfer-matrix-identities-context",
            "transfer-matrix-identities-proof",
            "ground-state-ordering",
            "ground-state-ordering-derivation",
            "skein-generation",
            "skein-generation-proof",
            "skein-mass-from-linking",
            "skein-mass-from-linking-proof",
          ],
        }),
        section({
          title: "Markov corrections and the Gram matrix",
          label: "sec:mass-algebraic-markov-gram",
          blocks: [
            "corrected-markov-trace",
            "corrected-markov-trace-proof",
            "mass-ordering-corrected",
            "frobenius-gram-matrix",
            "frobenius-gram-matrix-context",
            "frobenius-gram-matrix-proof",
            "frobenius-dual-h3",
            "gram-determinant-plancherel-ratio",
            "gram-determinant-plancherel-ratio-proof",
            "archimedean-functor-uniqueness",
            "archimedean-functor-uniqueness-proof",
            "archimedean-functor-uniqueness-context",
            "em-spectral-completeness",
            "em-spectral-completeness-proof",
            "reidemeister-mass-invariance",
            // Re-homed from the trace/operator collection: the Borromean
            // Markov-trace closed form belongs with the Markov corrections.
            "borromean-markov-trace-closed-form",
            "borromean-markov-trace-closed-form-proof",
            // Re-homed orphan: H_3 Jones/Temperley–Lieb Markov–Wenzl weights
            // feed the Borromean trace; sit with the Markov corrections.
            "h3-markov-wenzl-weights",
            "h3-markov-wenzl-weights-proof",
            "h3-markov-wenzl-weights-context",
            // Re-homed orphan (moved braids→mass-theory + thm:→prop: fix):
            // unit-modulus eigenvalues on V_(2,1) and the Borromean −1
            // fixed point; consumes the Borromean Markov-trace closed form.
            "unit-modulus-eigenvalue",
            "unit-modulus-eigenvalue-proof",
            // Decision 7: convention D IS Temperley–Lieb. The characterisation
            // comes first, then the metric consequence it explains — a reader
            // who meets "the radical blocks the Connes sup" before "the radical
            // is the TL ideal" reads the quotient as an ad-hoc amputation.
            "convention-d-kills-antisymmetriser",
            "convention-d-kills-antisymmetriser-proof",
            "markov-branching-three-term",
            "hecke-radical-is-temperley-lieb",
            "markov-gram-star-positive",
            "markov-gram-bilinear-vs-star",
            "gram-degeneracy-blocks-connes",
            "finite-connes-forces-trivial-kernel",
          ],
        }),
        section({
          title:
            "Complex-volume precision ladder: $\\operatorname{Re}(\\mathfrak{V})$ \\& $\\operatorname{Im}(\\mathfrak{V})$",
          label: "sec:mass-algebraic-complex-volume-ladder",
          blocks: [
            "complex-volume-ladder-intro",
            "phi-b-bar-parity-decomposition",
            "phi-b-bar-parity-interpretation",
            "phi-b-unitary-bar-odd",
            "q-beta-categorical-precision-ladder",
            "q-beta-categorical-precision-ladder-context",
            "q-beta-c3-hopf-three-fold-markov",
            "q-beta-c3-hopf-three-fold-markov-context",
            "q-beta-c3-continuum-geometry",
            "ck-extraction-from-algebraic-rules",
            "typed-b3-sub-braid-extraction",
            "cl3-zeta5-geometric-realization",
          ],
        }),
        section({
          title: "Bi-filtration and the adelic substrate",
          label: "sec:mass-algebraic-bifiltration-adelic",
          blocks: [
            "lusztig-vs-hermitian-bar",
            "lusztig-vs-hermitian-bar-proof",
            "q-zero-complex-extension",
            "q-zero-complex-extension-proof",
            "two-filtration-bridge-general",
            "two-filtration-bridge-general-proof",
            "two-filtration-bridge",
            "hq-bi-filtration",
            "joint-galois-braid-action",
            "adelic-substrate",
            "archimedean-realization-functor",
            "archimedean-realization-functor-interpretation",
            "adelic-substrate-integration",
            "q-clt-jsj-mass-scaling",
          ],
        }),
      ],
    }),

    section({
      title: "Hoefsmit convergence: construction",
      label: "sec:hoefsmit-convergence-construction",
      blocks: [
        "intro-hoefsmit-convergence-atomic",
        "operator-selection-lp",
        "operator-selection-lp-proof",
        "operator-selection-lp-interpretation",
        "confinement-sdp",
        "confinement-sdp-proof",
        "sdp-degeneracy-at-metallic-coincidence",
        "universal-braid-branching",
        "universal-braid-branching-proof",
        "hecke-convergence-bound",
        "algebraic-quantum-volume",
        "algebraic-quantum-volume-structure",
        "habiro-ring",
        "habiro-expansion-atomic",
        "habiro-expansion-atomic-proof",
        "z-habiro-ring",
        "quantum-dilog-convergence",
        "quantum-dilog-convergence-proof",
        "brane-tower-z-habiro",
        "brane-tower-z-habiro-table1-data",
        // Re-homed from the trace/operator collection: the Hoefsmit extended-
        // Wedderburn cell content belongs with the construction.
        "hoefsmit-ew-cell-content",
        "hoefsmit-ew-cell-content-context",
        "hoefsmit-ew-cell-content-table1-data",
        "hoefsmit-ew-cell-content-table2-data",
      ],
    }),

    section({
      title: "Per-partition brane-tower convergence",
      label: "sec:hoefsmit-convergence-construction-per-partition-k",
      blocks: [
        "hoefsmit-convergence-construction-per-partition-k-intro",
        "brane-tower-z-habiro-table2-data",
        "brane-tower-z-habiro-table7-data",
        "brane-tower-z-habiro-table8-data",
      ],
    }),

    section({
      title: "Hoefsmit convergence: magic-shell consequences",
      label: "sec:hoefsmit-convergence-magic-shells",
      blocks: [
        "hoefsmit-convergence-magic-shells-intro",
      ],
      // Over-weight split (P4): 33-block magic-shell section into 4
      // reading-order sub-arcs. Order preserved; parent keeps the intro.
      subsections: [
        section({
          title: "He-4 channel and magic-A binding",
          label: "sec:hoefsmit-he4-magic-a-binding",
          blocks: [
            "two-row-stratum",
            "two-row-projection",
            "he4-channel-active-set",
            "he4-two-row-dominance",
            // Ledger §5 orphan integration (2026-07-12): LR-fusion support
            // bound conjecture explaining which Wedderburn blocks vanish.
            "active-set-trace-concentration",
            "markov-trace-frobenius-selection",
            "markov-trace-frobenius-selection-proof",
            // Re-homed orphans: the min-Frobenius-norm collapse T_β = S·1
            // (and its general unital-R-algebra lift) that selects the
            // Markov-trace direction the Hoefsmit He-4 channel uses.
            "t-beta-markov-frobenius-collapse",
            "t-beta-markov-frobenius-collapse-proof",
            "t-beta-markov-frobenius-collapse-general",
            "t-beta-markov-frobenius-collapse-general-proof",
            "pn-averaging-uniqueness",
            "averaging-resonance-rule",
            "meson-color-tube-uniqueness",
            "bring-residue-resolvent",
            "bring-residue-resolvent-context",
            "binding-alpha-shift-extension",
            "binding-alpha-shift-extension-context",
            "magic-A-binding-formula",
            "magic-A-binding-formula-context",
          ],
        }),
        section({
          title: "Binding generating function and closure",
          label: "sec:hoefsmit-binding-genfun-closure",
          blocks: [
            "bond-order-eq-jet-degree",
            "bond-order-eq-jet-degree-context",
            "bond-order-eq-jet-degree-proof",
            "binding-manybody-jet-filtration",
            "cyclotomic-boundary-at-keystone",
            "bk-coordination-multiplicity",
            "jet-filtration-binding-extensive",
            "tower-geometric-lower-bound",
            "level-selection-not-linear",
            "linear-chain-bond-count",
            "alpha-cluster-activation-gate",
            "alpha-cluster-model-g-closure",
            "binding-genfun-qdifference",
            "binding-genfun-qdifference-proof",
            "binding-period-involution-statistic",
            "binding-period-involution-statistic-proof",
            "binding-period-statistic-reading",
            "content-genfun-palindromic",
            "content-genfun-palindromic-proof",
            "binding-closure-conditional",
            "binding-closure-conditional-proof",
            "universal-binding-architecture",
          ],
        }),
        section({
          title: "q-difference prolongation and periods",
          label: "sec:hoefsmit-qdifference-prolongation",
          blocks: [
            "qdifference-kernel-prolongation-symbol",
            "c1-ggm-bar-parity-faces",
            "c1-theta-zero-locus-and-pole-divisor",
            "prolonged-periods-fixed-depth",
            "prolonged-periods-fixed-depth-proof",
            "sl2-prolongation-recurrence",
            "sl2-prolongation-recurrence-proof",
            "sl2-period-conserved-quantity",
            "sl2-period-conserved-quantity-proof",
          ],
        }),
        section({
          title: "Substrate cohomology calibration",
          label: "sec:hoefsmit-substrate-cohomology-calibration",
          blocks: [
            "substrate-cohomology-calibration-story",
            "electron-period-base",
            "electron-period-base-proof",
            "electron-period-base-cohomology",
            "calibration-cohomology-alignment",
            "calibration-cohomology-alignment-proof",
            "bar-parity-split",
            "bar-parity-split-proof",
            "deuteron-binding-dressing-proton-net",
            "lr-coefficient-hecke",
            "hecke-1d-irrep-closed-form-character",
            "hecke-1d-irrep-closed-form-character-proof",
            "hoefsmit-V21-cos-symmetrization",
          ],
        }),
      ],
    }),

    section({
      title:
        "$\\mathfrak{Q}_\\beta$ precision ladder: formalize-first gates and the $c_k$ recursion",
      label: "sec:mass-algebraic-qbeta-formalize-first-gates",
      blocks: [
        "qbeta-formalize-first-gates-intro",
        "toroidal-harmonics-delta-lambda",
        "q-beta-over-e0-classical-vanishing",
        "q-beta-over-e0-classical-vanishing-proof",
        "qbeta-c8-c10-silver-rationals",
        "q-beta-c-k-recursion-from-habiro-q-difference",
        "q-beta-c-k-recursion-from-habiro-q-difference-interpretation",
        "q-bessel-c-k-recurrence-cfinite",
        "q-bessel-second-order-qdifference",
        "jackson-q-bessel-contiguity-recurrence",
        "jackson-q-bessel-contiguity",
        "qbeta-c4-from-c3-c8-product-identity",
        "qbeta-z-recursion-to-ck-recursion-bridge",
        "qbeta-z-recursion-to-ck-recursion-bridge-proof",
        "qbeta-odd-carrier-hopf-cubic",
        "faddeev-phib-uniqueness",
        "q-beta-c-2-eq-neg-one-structural",
        "q-beta-c-2-eq-neg-one-structural-proof",
        "q-beta-bar-even-kernel-invariant",
        "q-beta-bar-even-kernel-invariant-proof",
        "q-beta-radius-of-convergence-gate",
        "q-beta-radius-of-convergence-gate-proof",
        "q-beta-q-eq-one-shadow-gate",
        "q-beta-q-eq-one-shadow-gate-proof",
        "q-beta-direction-sanity-gate",
        "q-beta-direction-sanity-gate-proof",
        "q-beta-c-k-leading-bias-correction-identity",
        "q-beta-c-k-leading-bias-correction-identity-proof",
        "q-beta-bar-even-kernel-typeclass",
        "mass-side-kernel-formalize-first-gates",
      ],
    }),

    section({
      title: "Gröbner-Shirshov axiomatic backing",
      label: "sec:gs-axiomatic-backing",
      blocks: [
        "intro-gs-axiomatic-backing",
        "gs-graded-markov-trace-existence",
        "gs-residue-at-root-existence",
        "gs-spectral-decomposition-existence",
        "gs-spectral-sum-finite",
        "gs-archimedean-agreement-trace",
        "gs-archimedean-agreement-residue",
      ],
    }),


    // ═══ GEOMETRIC FACE ═════════════════════════════════════════
    // Mass-volume factorisation, Bloch group, φ_q resummation,
    // cyclotomic depth-3, Habiro identifications.
    // Sections below consolidated from climax-volume-mass (2026-05-27):
    // the mass-derivation chain (vertex factorisation → Feynman →
    // Kashiwara-Jones → quantum dilogarithm → archimedean realization).

    section({
      title: "Exceptional divisor, Reeb bundle, and vertex operators",
      label: "sec:exceptional-divisor-reeb",
      blocks: [
        "exceptional-divisor-reeb-intro",
        "reeb-bundle",
        "reeb-exceptional-divisor",
        "vertex-operator",
        "vertex-operator-affine-coordinate",
        "vertex-operator-dictionary",
        "vertex-operator-dictionary-table-data",
        "q-reeb-flow-on-color-coords",
        "six-canonical-knot-operators",
        "six-canonical-knot-operators-context",
        "six-canonical-knot-operators-table-data",
        "garside-as-compound-flow",
        "garside-flow-explicit-closed-form",
        "ramified-disc-fusion",
        "ramified-disc-fusion-interpretation",
        "reeb-bundle-complement-equals-volume",
        "torus-knot-zero-volume-via-reeb",
        "hyperbolic-knot-positive-volume-via-reeb",
      ],
    }),
    section({
      title: "Vertex factorisation: Markov trace",
      label: "sec:vertex-factorisation-markov",
      blocks: [
        "vertex-factorisation-intro",
        "vertex-is-exceptional-divisor",
        "vertex-is-exceptional-divisor-proof",
        "six-operators-via-vertex-factorisation",
        "six-operators-via-vertex-factorisation-table-data",
        "breit-wheeler-vertex",
        "breit-wheeler-vertex-literature",
        "markov-trace-product",
        "markov-trace-product-proof",
        "markov-trace-product-interpretation",
        "hecke-markov-transition",
        "hecke-markov-transition-proof",
        "hecke-markov-interpretation",
        "hecke-markov-interpretation-table-data",
        "markov-lambda-knot-operations",
        "q-gaussian-obstruction-at-q0",
        "q-gaussian-obstruction-at-q0-proof",
        "markov-chain-fluctuations",
      ],
    }),
    section({
      title: "Vertex factorisation: Feynman identifications",
      label: "sec:vertex-factorisation-feynman",
      blocks: [
        "vertex-factorisation-feynman-intro",
        "feynman-eigenbasis-decomposition",
        "feynman-eigenbasis-decomposition-proof",
        "feynman-trace-collapse",
        "feynman-trace-collapse-proof",
        "feynman-markov-identification",
        "feynman-markov-identification-proof",
        "feynman-categorical-trace",
        "feynman-categorical-trace-proof",
        "feynman-qou-dictionary",
        "feynman-qou-dictionary-table-data",
        "feynman-classical-limit",
        "feynman-classical-limit-interpretation",
      ],
    }),
    section({
      title: "Kashiwara-Jones interpretations and quantum dilogarithm",
      label: "sec:kashiwara-jones-quantum-dilog",
      blocks: [
        "intro-kashiwara-jones-quantum-dilog",
        "kashiwara-jones-alternation-interpretation",
        "canonical-braid-interface-composition",
        "canonical-braid-interface-composition-table3-data",
        "canonical-braid-interface-composition-table2-data",
        "canonical-braid-interface-composition-table1-data",
        "prop-rigid-monoidal-structural-gap-invariance",
        "prop-rigid-monoidal-structural-gap-invariance-proof",
        "quantum-dilogarithm-stratified",
        "quantum-dilogarithm-stratified-proof",
        "qz-bicompletion",
        "qz-bicompletion-properties",
        "q-pochhammer-partial-product",
        "phi-q-categorical-truncation",
        "phi-q-categorical-truncation-interpretation",
        "phi-q-categorical-truncation-proof",
        // Re-homed from the geometric-bridges collection: the pentagon
        // identities belong with the quantum dilogarithm.
        "quantum-bloch-group",
        "quantum-bloch-group-framework-connection",
        "q-rogers-pentagon-archimedean",
        "q-rogers-pentagon-archimedean-proof",
        "pachner-pentagon-borromean",
      ],
    }),
    section({
      title: "Archimedean realization and Kashaev volume",
      label: "sec:archimedean-realization-kashaev",
      blocks: [
        "intro-archimedean-realization-kashaev",
        "archimedean-image-table",
        "archimedean-image-table-table2-data",
        "archimedean-image-table-table1-data",
        "pre-tau-vs-post-tau",
        "vol-through-tau",
        "vol-as-motivic-period",
        "kashaev-volume-density",
        "kashaev-as-archimedean-realization",
        "phi-q-piece",
        "phi-q-tower-algebraic-stratification",
        "phi-q-tower-algebraic-stratification-proof",
        "kashaev-volume-conjecture",
        "dilog-saddle-regime",
        "figure-8-archimedean-illustration",
        "gb-depth-period-correspondence",
        "vc-as-depth-2-instance",
        "bring-figure-eight-depth-2-witness",
        // Re-homed from the geometric-bridges collection: Kashaev density =
        // SDP multiplicity belongs with the Kashaev-volume realization.
        "kashaev-density-equals-sdp-multiplicity",
      ],
    }),
    section({
      title: "Geometric face: pentagon and volume bridges",
      label: "sec:mass-bridge-orphan-reconnect",
      blocks: [
        "mass-bridge-orphan-reconnect-intro",
        "categorical-linking-operation",
        "categorical-linking-operation-interpretation",
        "crossed-module-euler-characteristic",
        "crossed-module-euler-characteristic-proof",
        "geom-bridge-status",
        "tau-all-orders-bridge",
        "dim-master-pentagon",
        "nuclear-knot-classification",
        "nuclear-knot-classification-proof",
        "geometric-invariant-piecewise",
        "geom-yekutieli-alignment",
        "hoefsmit-scattering-pipeline",
        "hopf-link-non-magic",
        "p-from-braid-mirror",
        "poincare-lefschetz-borromean",
        "volume-perturbation-formula",
        // Re-homed (high-confidence): kashaev-density-equals-sdp-multiplicity
        // -> sec:archimedean-realization-kashaev; pachner-pentagon-borromean +
        // q-rogers-pentagon-archimedean -> sec:kashiwara-jones-quantum-dilog.
      ],
    }),

    // Existing geometric-face sections (from particle-interactions consolidation)
    section({
      title: "Geometric face: mass-volume factorisation and crossing expansion",
      label: "sec:mass-geometric-face",
      blocks: [
                "mass-geometric-face-intro",
"thurston-volume-additivity",
        "flat-tetrahedron-zero-volume",
        "gluing-equations-do-not-detect-hyperbolicity",
        "gluing-certification-mechanical-reach",
        "hyperbolic-knot-shape-fields",
        "five-two-saddle-sum-rule",
        "kummer-bloch-wigner-identity",
        "rivin-concavity-one-tetrahedron",
        "ideal-tetrahedron-relabelling-invariance",
        "mass-volume-factorization",
        "frobenius-packing-density",
        "crossing-graded-mass-expansion",
        "crossing-graded-mass-expansion-table-data",
        "lifted-crossing-locality",
        "mass-categorical-descent",
        "mass-categorical-descent-proof",
        "descended-level-zero",
        "jet-tower-convergence",
        "jet-tower-convergence-proof",
        "jet-tower-convergence-context",
        "vhat-pair-commutation-trace",
        "vhat-pair-commutation-trace-proof",
        "pentagon-uv-commutation",
        "delta-max-uniform-bound",
        "delta-max-uniform-bound-context",
        "mass-tower-syt-cells",
        "markov-pair-z2",
        "markov-pair-z2-proof",
      ],
    }),

    section({
      title: "Mutant Jones falsifiability and Bloch group closure",
      label: "sec:mutant-jones-bloch-group",
      blocks: [
        "intro-mutant-jones-bloch-group",
        "knot-indexed-convolution-grid",
        "knot-indexed-convolution-grid-context",
        "knot-indexed-convolution-grid-table2-data",
        "knot-indexed-convolution-grid-table1-data",
        "conway-kt-vol-injectivity-test",
        "jones-faithfulness-crossing-8",
        "wedderburn-as-noncomm-fourier",
        "wedderburn-as-noncomm-fourier-context",
        "degree-one-braid-trivial-volume",
        "degree-one-braid-trivial-volume-proof",
        "pieri-photon-shift",
        "pieri-photon-shift-proof",
        "pieri-photon-shift-interpretation",
        "phi-q-tower-jsj-bridge",
        "dilogarithm-archimedean-limit",
        "algebraic-geometric-dilog-equivalence",
        "phi-q-wkb-greens-function",
        "shared-denominator-cusp-holonomy",
        "degree-two-baryon-weight",
        "degree-two-baryon-weight-proof",
        // Re-homed from the weak-spectral/isospin collection: the Borromean
        // Bloch-group (K3) element belongs with the Bloch group closure.
        "borromean-bloch-group-element",
      ],
    }),

    section({
      title: "$\\\\varphi_q$ resummation, Markov trace, Schur-Weyl: foundations",
      label: "sec:phi-q-markov-schur-weyl-foundations",
      blocks: [
        "intro-phi-q-markov-schur-weyl-tower",
      ],
      // Over-weight split (P4): 24-block foundations section into 3
      // reading-order sub-arcs (matching the compound title). Order
      // preserved; parent keeps the intro.
      subsections: [
        section({
          title: "Markov trace resummation",
          label: "sec:phi-q-markov-resummation",
          blocks: [
            "markov-trace-factorization",
            "markov-trace-factorization-proof",
            // Algebraic shortcut of KS Thm 8 (multiplicative invariant) via the Markov property.
            "ks-multiplicativity-via-markov",
            "markov-trace-ratio-exact",
            "markov-trace-ratio-exact-proof",
            "vassiliev-filtration-mass-tower",
            "hecke-quandle",
            "knot-operator-bring-action",
            "phi-q-resums-trace-series",
            "phi-q-resums-trace-series-table-data",
            "markov-axiom-recursive-ascent",
            "per-braid-mass-tower",
          ],
        }),
        section({
          title: "The lepton mass tower",
          label: "sec:phi-q-lepton-mass-tower",
          blocks: [
            "lepton-mass-tower-canonical",
            "lepton-bring-surface-h3-3channel",
            "conj-lepton-tower-h-n-plus-1-branching",
            "conj-atom-braid-exterior-algebra",
            "conj-psd-trace-orthogonality",
            "three-halves-structural-factor",
            "rem-im-q-vs-p-skew",
            "conj-im-q-physical-role",
            "rem-c3-s-imq-decay-projection",
            "rem-qstar-decay-sector-q0",
            "rem-ohtsuki-tower-bar-parity",
            // Provenance of the 1-loop prefactor law c_sigma = k |tau|^p: the
            // FORM is DGLZ eq (2.3) for a general M, the exponent -1/2 is
            // normalisation-invariant and was already measured by the k_c
            // checks, and the constant k -- which cannot be lifted out of
            // DGLZ's conventions -- is instead DERIVED on the link side from
            // van der Veen's colored-Jones asymptotic (bean qou-vdvS).
            "one-loop-prefactor-provenance",
            // A_ω=3 closed-sector conditional adoption (bean qou-ujmw): the
            // resurgent-Stokes = DT/BPS bridge (GGM Conj 3(d) + GPPV) and the
            // conditional theorem deriving A_ω(4₁)=3 as a BPS/DT count.
            "stokes-dt-bps-bridge",
            "aomega-fourone-dt-count",
            "dt-spectrum-bar-eigenspace",
          ],
        }),
        section({
          title: "Schur-Weyl decomposition and positivity",
          label: "sec:phi-q-schur-weyl-positivity",
          blocks: [
            "schur-weyl-mass-decomposition",
            "categorical-mass-positivity",
            "mass-spectrum-generating-function",
            "graded-markov-trace-from-gs-filtration",
            "graded-markov-trace-from-gs-filtration-proof",
            "residue-at-root",
            "residue-at-root-proof",
            "gb-residue-spectral-sum",
          ],
        }),
      ],
    }),

    section({
      title: "$\\\\varphi_q$ resummation: residue and Habiro identifications",
      label: "sec:phi-q-markov-residue-habiro",
      blocks: [
        "phi-q-markov-residue-habiro-intro",
        "tower-pair-equality-fixed-level",
        "tower-pair-equality-fixed-level-proof",
        "jet-tower-uniform-delta-max",
        "topological-mass-formula-algebraic",
        "topological-mass-formula-algebraic-proof",
        "residue-as-braid-holonomy",
        "graded-trace-residue-split",
        "graded-trace-strutinsky-interpretation",
        "term6-binding-density",
        "term6-binding-density-table2-data",
        "term6-binding-density-table1-data",
        "full-pole-structure-mass-trace",
        "full-pole-structure-mass-trace-proof",
        "full-pole-structure-mass-trace-interpretation",
        "habiro-residue-sum-equivalence",
        "habiro-residue-sum-equivalence-interpretation",
        // Re-homed orphan: the Borromean h^4 = -3/4 categorical derivation
        // (R-matrix character × Markov normalisation via Schur–Weyl)
        // consumes the Habiro residue sum + the H_3 Markov–Wenzl weights.
        "borromean-h4-categorical-derivation",
        "borromean-h4-categorical-derivation-proof",
        "borromean-h4-categorical-derivation-context",
        // Re-homed orphans (2026-06-28): the Habiro precision-ladder
        // integrality statement + the Pochhammer normalisation bridge,
        // authored 2026-06-26 but never wired into a manifest. The
        // bridge consumes the precision-ladder equivalence.
        "habiro-precision-ladder-equivalence",
        "habiro-precision-ladder-equivalence-context",
        "habiro-pochhammer-bridge",
        "habiro-pochhammer-bridge-proof",
      ],
    }),

    section({
      title: "Cyclotomic depth-3 trilog identities",
      label: "sec:cyclotomic-depth-3-trilog",
      blocks: [
        "intro-cyclotomic-depth-3-trilog",
        "bring-trilog-depth-3-witness",
        "bring-trilog-imaginary-tate-rational",
        "bring-trilog-imaginary-tate-rational-proof",
        "cl3-zeta5-orbit-sum-identity",
        "cl3-zeta5-orbit-sum-identity-proof",
        "cl3-zeta5-pslq-independence",
        "cyclotomic-trilog-imaginary-closed-form",
        "cyclotomic-trilog-imaginary-closed-form-proof",
        "cyclotomic-trilog-imaginary-closed-form-table-data",
        "cyclotomic-cl3-orbit-sum-general",
        "cyclotomic-cl3-orbit-sum-general-proof",
        "cyclotomic-cl3-orbit-sum-general-table-data",
        "cyclotomic-depth3-dimension-synthesis",
        "cyclotomic-depth3-dimension-synthesis-proof",
        "cyclotomic-depth3-dimension-synthesis-table2-data",
        "cyclotomic-depth3-dimension-synthesis-table1-data",
        "jonquiere-cyclotomic-tate-rationality",
        "jonquiere-cyclotomic-tate-rationality-proof",
        "cyclotomic-orbit-sum-all-depths",
        "cyclotomic-orbit-sum-all-depths-proof",
        "cyclotomic-orbit-sum-all-depths-table2-data",
        "cyclotomic-orbit-sum-all-depths-table1-data",
        "cyclotomic-dimension-synthesis-all-depths",
        "cyclotomic-dimension-synthesis-all-depths-proof",
        // Re-homed orphans (2026-06-28): the cyclotomic doubling
        // identity Φ₈(X)=Φ₄(X²) + the a₈ partition-function identity +
        // the ζ₈ level-2 SU(2) Verlinde witness, authored 2026-06-26
        // but never wired. Strict dependency order: a8 and ζ8 both
        // consume the doubling identity. The doubling block's
        // strand-doubling *interpretation* was refuted (the algebraic
        // identity stands); see its historical-note section.
        "cyclotomic-strand-doubling",
        "cyclotomic-strand-doubling-proof",
        "a8-partition-function-identity",
        "a8-partition-function-identity-proof",
        "zeta8-witness-level2-su2",
        "zeta8-witness-level2-su2-proof",
      ],
    }),


    // ═══ ARCHIMEDEAN FACE ═══════════════════════════════════════
    // Substrate binding, LP-dual, spectral sequence, Plancherel,
    // α_k derivation, Wenzl bridge, derivation audit.
    section({
      title: "Substrate binding setup",
      label: "sec:substrate-binding-setup",
      blocks: [
        "nuclear-binding-beta-stability-intro",
        "confined-knot-binding",
        "confined-knot-binding-proof",
        "molecular-bond-binding-from-trefoil-insertion",
        "jet-filtered-knot-factor",
        "jet-convergence-classical-limit",
        "wigner-np-pairing",
        "wigner-np-pairing-proof",
        // Reeb-flow pn-bond magnitude (2026-07-07): the proved
        // exchange-criticality algebra + the open CWF linking postulate
        // behind the ²H reeb-flow tier (owner ruling: NEAR-MATCH label).
        "reeb-pn-magnitude-criticality",
        "reeb-linking-cwf-normalization",
        "knot-factor-frobenius-pairing",
        "wedderburn-weight-canonical",
        "hook-weight-derivation",
        "hook-weight-derivation-proof",
        "wigner-coefficient-derivation",
        "wigner-coefficient-derivation-proof",
        "mass-coefficient-shadow-price",
        "mass-coefficient-shadow-price-proof",
        "unified-iterative-correction",
        "unified-iterative-correction-proof",
        "unified-iterative-correction-table-data",
        "frobenius-self-duality-forces-lp-dual-extraction",
        "frobenius-self-duality-forces-lp-dual-extraction-proof",
        "frobenius-self-duality-forces-lp-dual-extraction-interpretation",
      ],
    }),

    section({
      title: "LP-dual and Jucys-Murphy central elements",
      label: "sec:lp-dual-jucys-murphy",
      blocks: [
        "intro-lp-dual-jucys-murphy",
        "jucys-murphy-central-elements-qou",
        "jucys-murphy-central-elements-qou-proof",
        "jucys-murphy-central-elements-qou-interpretation",
        // Piece A of Identity I, promoted 2026-08-24 from two unregistered
        // .md drafts that had sat at the paper root since the 52c68267f2
        // bulk import (bean qou-cauj listed them as "probably not blocks";
        // the owner ruled otherwise). The Specht/JM trace pair reads the
        // JM prop directly above; the corner induction is the alternative
        // route to the same identity.
        "piece-a-hook-content-identity",
        "piece-a-specht-character-trace",
        "piece-a-specht-character-trace-proof",
        "piece-a-corner-removal-obligation",
        "piece-a-corner-removal-obligation-proof",
        // def:spin-involution relocated to knots-particles-confinement §7
        // (2026-08-09, decision 5): three of its four consumers are the
        // EW-triplet charge/spin blocks there, and it has `uses: []` so it
        // drags no dependency forward. The lp-dual-invariance arc below is
        // the fourth consumer and now reads BACKWARD into Ch 8 for the
        // definition.
        "spin-involution-lp-dual-invariance",
        "spin-involution-lp-dual-invariance-proof",
        "spin-involution-lp-dual-invariance-interpretation",
        "lp-dual-scaling-conjecture",
        "wigner-2-coefficient",
        "wigner-2-coefficient-proof",
        "wigner-2-coefficient-interpretation",
        "mass-endomorphism-tower",
        "mass-endomorphism-tower-proof",
        "mass-endomorphism-jet-tower",
        "mass-endomorphism-jet-tower-table1-data",
      ],
    }),

    section({
      title: "Spectral sequence, chirality, and confinement-NF structure",
      label: "sec:spectral-sequence-chirality-confinement",
      blocks: [
        "intro-spectral-sequence-chirality-confinement",
        "jet-prefix-gb-filtration",
        "jet-prefix-gb-filtration-evidence",
        "frobenius-self-pairing-chirality",
        "chirality-from-frobenius-self-pairing",
        "chirality-from-frobenius-self-pairing-scope",
        "hecke-curvature-2-cocycle",
        "curvature-rank",
        "curvature-rank-gb-stratification",
        "curvature-rank-gb-stratification-proof",
        "curvature-rank-gb-stratification-interpretation",
        "curvature-rank-gb-stratification-table-data",
        // Algebraic shortcut of KS ind-constructibility via the Diamond Lemma.
        "ks-finiteness-via-diamond-lemma",
        "spectral-sequence-collapse",
        "spectral-sequence-collapse-proof",
        "delta-q-decoration",
        "q-dimension-layer",
        "alpha-basis-knot-delta-q",
        "torus-knot-delta-q-writhe",
        "force-carrier-intertwining-correspondence",
        "alpha-shift-torus-knot",
        "alpha-shift-torus-knot-proof",
        "alpha-shift-torus-knot-table-data",
      ],
    }),

    section({
      title: "Confinement-NF forcing and the per-nucleon shift",
      label: "sec:spectral-sequence-chirality-confinement-per-nucleon-shift",
      blocks: [
        "spectral-sequence-chirality-confinement-per-nucleon-shift-intro",
        "per-nucleon-shift-additive-linearity",
        "per-nucleon-shift-additive-linearity-proof",
        "per-nucleon-shift-additive-linearity-table2-data",
        "per-nucleon-shift-additive-linearity-table1-data",
        "confinement-nf-structure-forcing",
        "confinement-nf-structure-forcing-table-data",
        "lp-duality-hypothesis-class",
        "confinement-nf-partial-proof",
        "bound-state-frobenius-self-dual-channel",
        "confinement-categorical",
        "confinement-categorical-proof",
        "exterior-square-borromean",
        "exterior-square-borromean-proof",
      ],
    }),

    section({
      title: "Plancherel-$\\\\alpha$ spectral foundations",
      label: "sec:plancherel-alpha-spectral",
      blocks: [
        "intro-plancherel-alpha-ribbon",
        "alpha-em-categorical-trace",
        "plancherel-term-7-formulation",
        "plancherel-term-7-formulation-proof",
        "unified-curvature-rank-mass-formula",
        "unified-curvature-rank-mass-formula-proof",
        "unified-curvature-rank-mass-formula-table-data",
        "plancherel-weight-boundedness",
        "plancherel-weight-boundedness-proof",
        "plancherel-weight-boundedness-interpretation",
        "plancherel-weight-boundedness-table-data",
        "chirality-residue-mass-term",
        "chirality-residue-mass-term-proof",
        "chirality-residue-mass-term-interpretation",
        "e-infinity-page-identifications",
        "e-infinity-page-identifications-table-data",
        "spectral-sequence-h3-explicit",
        "chirality-writhe-ribbon-derivation",
        "gram-matrix-spectral-connection",
        // Re-homed from the weak-spectral/isospin collection: weak-sector
        // spectral completeness belongs with the Plancherel-alpha foundations.
        "weak-spectral-completeness",
      ],
    }),

    section({
      title: "Plancherel: knot-factor and mass-tower closure",
      label: "sec:plancherel-knot-factor-mass-tower",
      blocks: [
        "plancherel-knot-factor-mass-tower-intro",
        "knot-factor-spectral-derivation",
        "knot-factor-spectral-derivation-proof",
        "knot-factor-amphicheiral",
        "knot-factor-amphicheiral-proof",
        "knot-factor-borromean-composite",
        "knot-factor-borromean-composite-proof",
        "knot-factor-shell-closed",
        "knot-factor-shell-closed-proof",
        "knot-factor-spectral-summary",
        "pauli-factor-wedderburn",
        "pauli-factor-wedderburn-proof",
        "mass-tower-coefficient-stratification",
        "mass-tower-coefficient-stratification-proof",
        "mass-tower-coefficient-stratification-table1-data",
        "mass-tower-coefficient-stratification-table2-data",
        "flavor-dressing-functor",
        // Re-homed from the staircase/character collection: the staircase
        // EW-residual (Weinberg angle) belongs with the mass-tower closure.
        "staircase-ew-residual",
      ],
    }),

    section({
      title: "$\\\\alpha_k$ derivation procedure",
      label: "sec:alpha-k-procedure",
      blocks: [
        "intro-alpha-k-procedure",
        "flavor-dressed-mass-from-substrate-split",
        "flavor-mass-splitting-bound",
        "flavor-mass-splitting-bound-proof",
        "alpha-k-derivation-procedure",
        "alpha-k-derivation-procedure-proof",
        "alpha-k-categorical-closure",
        "chi-lambda-w0-sign-weighting",
        "chi-lambda-w0-sign-weighting-proof",
        "atom-knot-mass-derivation",
        "atom-knot-mass-derivation-table1-data",
      ],
    }),

    section({
      title: "Joint-tower SDP and closed-form weights",
      label: "sec:alpha-k-procedure-atom-knot-mass",
      blocks: [
        "alpha-k-procedure-atom-knot-mass-intro",
        "atom-knot-mass-derivation-table2-data",
        "atom-knot-mass-derivation-table3-data",
        "atom-knot-mass-derivation-proof",
        "joint-tower-sdp-confinement",
        "joint-tower-sdp-confinement-table2-data",
        "joint-tower-sdp-confinement-table1-data",
        "y-lambda-closed-form-wenzl-bridge",
        "y-lambda-closed-form-wenzl-bridge-proof",
        "y-lambda-closed-form-wenzl-bridge-table1-data",
        "y-lambda-closed-form-wenzl-bridge-table2-data",
        "y-lambda-closed-form-wenzl-bridge-table3-data",
      ],
    }),

    section({
      title: "Wenzl bridge, cyclotomic factorisation, and explicit $\\\\alpha_k$",
      label: "sec:wenzl-bridge-cyclotomic",
      blocks: [
        "intro-wenzl-bridge-cyclotomic",
        "y-lambda-cyclotomic-factorization",
        "y-lambda-cyclotomic-factorization-proof",
        "y-lambda-recipe-from-partition",
        "graded-hecke-energy-truncation-bound",
        "graded-hecke-energy-truncation-bound-proof",
        "graded-hecke-energy-truncation-bound-table-data",
        "descent-rate-probe-sim",
        "multi-level-jet-sum-sim",
        "macdonald-hook-telescope",
        "demazure-fiber-markov-trace",
        "wenzl-bridge-applicability-qou",
        "wenzl-bridge-applicability-qou-proof",
      ],
    }),

    section({
      title: "The LR-tensor character bridge",
      label: "sec:wenzl-bridge-cyclotomic-lr-tensor-character",
      blocks: [
        "wenzl-bridge-cyclotomic-lr-tensor-character-intro",
        "lr-tensor-character-bridge",
        "lr-tensor-character-bridge-proof",
        "wenzl-qmn-synergy",
        "explicit-alpha-k-h3",
        "explicit-alpha-k-h3-proof",
        "explicit-alpha-k-h4",
        "explicit-alpha-k-h4-proof",
        "wedderburn-bratteli-recursion",
        "wedderburn-bratteli-recursion-proof",
        "y-lambda-sign-pattern",
        "terms-2-6-higher-operations",
        "terms-2-6-higher-operations-table2-data",
        "terms-2-6-higher-operations-table1-data",
      ],
    }),

    section({
      title: "Mass and Binding Derivation",
      label: "sec:derivation-audit",
      blocks: [
        "derivation-audit-intro",
        "pre-archimedean-derivation-chain",
        "pre-archimedean-derivation-chain-table2-data",
        "pre-archimedean-derivation-chain-table1-data",
        "conj-canonical-knot-id-sdp",
        "conj-rho-prefactor-structural",
        "frobenius-cocasimir-refuted-deuteron",
      ],
    }),


    // ═══ PHYSICAL FACE ═════════════════════════════════════════
    // Parity classification, six-term formula, mass predictions.
    section({
      title: "Parity classification, atomic atlas, and discrepancy resolution",
      label: "sec:parity-classification-discrepancy",
      blocks: [
        "intro-parity-classification-discrepancy",
        "mn-classical-parity-blind",
        "mn-classical-parity-blind-table-data",
        "q-character-closes-parity-gap",
        "frobenius-codim-universal",
        "frobenius-codim-universal-proof",
        "frobenius-codim-universal-interpretation",
        "frobenius-limits-substrate-cost",
        "knot-mass-formula-unified",
        "content-scaling-correspondence",
      ],
    }),

    section({
      title: "The partition-sum proton residual",
      label: "sec:parity-classification-discrepancy-partition-sum-proton",
      blocks: [
        "parity-classification-discrepancy-partition-sum-proton-intro",
        "partition-sum-proton-residual",
        "partition-sum-proton-residual-table5-data",
        "partition-sum-proton-residual-table4-data",
        "partition-sum-proton-residual-table3-data",
        "partition-sum-proton-residual-table2-data",
        "partition-sum-proton-residual-table1-data",
        "np-discrepancy-resolution",
        "mass-formula-regime-switching",
        "mass-formula-regime-switching-table2-data",
        "mass-formula-regime-switching-table1-data",
      ],
    }),

    section({
      title: "Six-term mass formula and crystal isospin",
      label: "sec:six-term-crystal-isospin-chirality",
      blocks: [
        "intro-six-term-crystal-isospin-chirality",
        "six-term-mass-formula-complete",
        "six-term-mass-formula-complete-table-data",
        "six-term-per-derivation-weights",
        "six-term-per-derivation-weights-proof",
        "six-term-per-derivation-weights-table1-data",
        "six-term-per-derivation-weights-table2-data",
        "six-term-per-derivation-weights-table3-data",
        "crystal-isospin-degeneracy",
        "crystal-isospin-degeneracy-proof",
        "crystal-isospin-degeneracy-table-data",
        "isospin-mass-split-em-localisation",
        // Re-homed from the weak-spectral/isospin collection: isospin from the
        // canonical bowtie belongs with crystal isospin.
        "isospin-from-canonical-bowtie",
      ],
    }),

    section({
      title: "Option E: crystal bases and chirality duality",
      label: "sec:six-term-crystal-isospin-chirality-option-e-isospin",
      blocks: [
        "six-term-crystal-isospin-chirality-option-e-isospin-intro",
        "option-e-isospin-test",
        "crystal-bases-path-a",
        "crystal-bases-path-a-table3-data",
        "crystal-bases-path-a-table2-data",
        "crystal-bases-path-a-table1-data",
        "chirality-dual-space-derivation",
        "chirality-dual-space-derivation-table3-data",
        "chirality-dual-space-derivation-table2-data",
        "chirality-dual-space-derivation-table1-data",
        "frobenius-antipode-unifies-chirality-and-tower",
        "frobenius-antipode-neutron-tower-closure",
        "frobenius-antipode-unifies-chirality-and-tower-interpretation",
      ],
    }),

    // §physical: mass formulas, baryon/meson, binding energy, predictions
    section({
      title:
        "Physical face: mass, binding ($\\operatorname{Re}\\mathfrak{V}$), and decay ($\\operatorname{Im}\\mathfrak{V}$)",
      label: "sec:mass-physical-face",
      blocks: [
                "mass-physical-face-intro",
"neutron-proton-splitting",
        // Ledger §5 orphan integration (2026-07-12): H_4 alternating-
        // channel Habiro-element conjecture for the Δ_pn residual.
        "flavor-split-habiro-derivation",
        "borromean-baryon-mass-formula",
        "borromean-baryon-interpretation",
        "q-integer-mass-formula",
        "lambda-scale-substrate-form",
        "lambda-scale-substrate-form-proof",
        "topological-mass-trefoil",
        // Re-homed orphan: kaon/pion mass ratio from Hecke χ^{(2,1)}(σ_1^5)
        // + Seifert volumes (structured near-match, ~290 ppm vs PDG).
        "meson-kaon-pion-hecke-seifert",
        "meson-kaon-pion-hecke-seifert-proof",
        // Gen-3 extension: φ(1020) = T(2,7), m_φ/m_π ≈ 7.320 (2167 ppm vs
        // PDG); the torus tower tracks the strange-vector line, not the η.
        "gen3-meson-phi-hecke-seifert",
        "tower-binding-energy",
        "tower-binding-energy-table-data",
        "mass-table-z1-20",
        "mass-table-z1-20-table-data",
      ],
    }),


    // ═══ OPEN PROBLEMS ═════════════════════════════════════════
    // ── §open: mass-tower open problems and crystal-basis directions ──
    // Consolidated from predicted-spectra (2026-05-27).
    section({
      title: "Open problems: mass-tower structure and crystal basis",
      label: "sec:mass-open-problems",
      blocks: [
                "mass-open-problems-intro",
"terminal-resolution",
        "mass-from-generators",
        "volume-tower-decomposition",
        "mass-tower-open-problems-classes",
        "crystal-basis-resolves-mass-tower-open-problems",
        "crystal-basis-resolves-mass-tower-open-problems-context",
        "mass-tower-deeper-fillers",
        "complex-mass-constituent-functional",
      ],
    }),


    // ═══ ORPHAN RECONNECTS ═════════════════════════════════════
    section({
      title: "Weak-spectral and isospin lemmas",
      label: "sec:mass-theory-orphan-reconnect",
      blocks: [
        "mass-theory-orphan-reconnect-intro",
        "categorical-higgs-mechanism",
        "interface-knot-markov-z",
        "interface-knot-markov-z-proof",
        "rho-k-h3a-refinement",
        "rho-k-h3a-refinement-interpretation",
        "s4-s3-half-symmetric-projection",
        "s4-s3-half-symmetric-projection-proof",
        "weak-symmetric-normalization",
        "z-eq-n-rho-correction",
        // Re-homed (high-confidence): borromean-bloch-group-element ->
        // sec:mutant-jones-bloch-group; isospin-from-canonical-bowtie ->
        // sec:six-term-crystal-isospin-chirality; weak-spectral-completeness
        // -> sec:plancherel-alpha-spectral.
      ],
    }),

    section({
      title: "Trace and staircase lemmas",
      label: "sec:mass-application-orphan-reconnect",
      blocks: [
        "mass-application-orphan-reconnect-intro",
      ],
      // De-dup + over-weight split: 19-block reconnected-orphan grab-bag
      // retitled (was a second "Reconnected orphan blocks (Phase 7)",
      // duplicating sec:mass-theory-orphan-reconnect) and split into 2
      // reading-order sub-arcs. A deeper re-home of these blocks into
      // thematic sections elsewhere is a follow-up.
      subsections: [
        section({
          title: "Trace and operator lemmas",
          label: "sec:mass-application-trace-operator-lemmas",
          blocks: [
            "block-multiplicativity-v-free",
            "wenzl-A-operator",
            "crystal-r-matrix-sub-lemma",
            "operator-valued-combiner-convergence",
            "depth-stratified-frobenius-reciprocity",
            "eigenvalue-product-expansion",
            "eigenvalue-product-expansion-proof",
            "knot-operator-lp-selection",
            // Re-homed: borromean-markov-trace-closed-form ->
            // sec:mass-algebraic-markov-gram; hoefsmit-ew-cell-content (+2
            // tables) -> sec:hoefsmit-convergence-construction.
          ],
        }),
        section({
          title: "Staircase and character lemmas",
          label: "sec:mass-application-staircase-hoefsmit",
          blocks: [
            "knot-operator-transition",
            "qmn-recursive-memoized",
            "sigma-shell-from-beta-chain-derivation",
            "sigma-shell-from-beta-chain-derivation-table-data",
            "staircase-partition",
            "staircase-corner-hook",
            "staircase-corner-hook-proof",
            "symbolic-character-table",
            "outro-mass-theory",
            // Re-homed: staircase-ew-residual ->
            // sec:plancherel-knot-factor-mass-tower.
          ],
        }),
      ],
    }),

  ],
});
