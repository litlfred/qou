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
        "transfer-matrix-level-independence",
        "tmli-constituent-composite-agreement",
        "tmli-constituent-composite-agreement-proof",
        "transfer-matrix-level-independence-proof",
        "topological-mass-formula",
        "motivic-mass-measure",
        "hecke-mass-element",
        "hecke-mass-trace",
        "hecke-generator-poly-reduction",
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
        "two-tier-scaling-pq",
        "three-calibration-inputs",
        "three-parameters-wedderburn",
        "wedderburn-trace-identity",
        "binding-scale-catalan",
        "binding-error-amplification",
        "wedderburn-mass-formula",
        "frobenius-s-classification",
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
        "derived-mass-formula-light-isotopes",
        "derived-mass-formula-light-isotopes-table1-data",
        "derived-mass-formula-light-isotopes-table2-data",
        "hoefsmit-seminormal-form",
        "figure-eight-branching-rule",
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
            "pentagon-uv-commutation",
            "transfer-matrix-operator",
            "transfer-matrix-identities",
            "skein-polynomial-transfer-matrix",
            "beta-decay-transfer-matrix",
            "ground-state-ordering",
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
            "mass-ordering-corrected",
            "frobenius-gram-matrix",
            "gram-determinant-plancherel-ratio",
            "archimedean-functor-uniqueness",
            "em-spectral-completeness",
            "reidemeister-mass-invariance",
            // Re-homed from the trace/operator collection: the Borromean
            // Markov-trace closed form belongs with the Markov corrections.
            "borromean-markov-trace-closed-form",
          ],
        }),
        section({
          title:
            "Complex-volume precision ladder: $\\operatorname{Re}(\\mathfrak{V})$ \\& $\\operatorname{Im}(\\mathfrak{V})$",
          label: "sec:mass-algebraic-complex-volume-ladder",
          blocks: [
            "complex-volume-ladder-intro",
            "q-beta-categorical-precision-ladder",
            "q-beta-c3-hopf-three-fold-markov",
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
            "q-zero-complex-extension",
            "two-filtration-bridge-general",
            "two-filtration-bridge",
            "hq-bi-filtration",
            "joint-galois-braid-action",
            "adelic-substrate",
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
        "sdp-degeneracy-at-metallic-coincidence",
        "universal-braid-branching",
        "hoefsmit-scattering-pipeline",
        "hecke-convergence-bound",
        "algebraic-quantum-volume",
        "habiro-ring",
        "habiro-expansion-atomic",
        "z-habiro-ring",
        "brane-tower-z-habiro",
        "brane-tower-z-habiro-table1-data",
        // Re-homed from the trace/operator collection: the Hoefsmit extended-
        // Wedderburn cell content belongs with the construction.
        "hoefsmit-ew-cell-content",
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
            "he4-channel-active-set",
            "he4-two-row-dominance",
            "markov-trace-frobenius-selection",
            "pn-averaging-uniqueness",
            "averaging-resonance-rule",
            "meson-color-tube-uniqueness",
            "bring-residue-resolvent",
            "binding-alpha-shift-extension",
            "magic-A-binding-formula",
          ],
        }),
        section({
          title: "Binding generating function and closure",
          label: "sec:hoefsmit-binding-genfun-closure",
          blocks: [
            "bond-order-eq-jet-degree",
            "bond-order-eq-jet-degree-proof",
            "binding-manybody-jet-filtration",
            "binding-genfun-qdifference",
            "binding-genfun-qdifference-proof",
            "binding-closure-conditional",
            "binding-closure-conditional-proof",
          ],
        }),
        section({
          title: "q-difference prolongation and periods",
          label: "sec:hoefsmit-qdifference-prolongation",
          blocks: [
            "qdifference-kernel-prolongation-symbol",
            "prolonged-periods-fixed-depth",
            "prolonged-periods-fixed-depth-proof",
            "sl2-prolongation-recurrence",
            "sl2-prolongation-recurrence-proof",
          ],
        }),
        section({
          title: "Substrate cohomology calibration",
          label: "sec:hoefsmit-substrate-cohomology-calibration",
          blocks: [
            "substrate-cohomology-calibration-story",
            "electron-period-base",
            "electron-period-base-proof",
            "calibration-cohomology-alignment",
            "calibration-cohomology-alignment-proof",
            "bar-parity-split",
            "bar-parity-split-proof",
            "lr-coefficient-hecke",
            "hecke-1d-irrep-closed-form-character",
            "hoefsmit-V21-cos-symmetrization",
          ],
        }),
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
        "vertex-operator-dictionary",
        "vertex-operator-dictionary-table-data",
        "q-reeb-flow-on-coral-coords",
        "six-canonical-knot-operators",
        "six-canonical-knot-operators-table-data",
        "garside-as-compound-flow",
        "garside-flow-explicit-closed-form",
        "ramified-disc-fusion",
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
        "markov-trace-product-interpretation",
        "hecke-markov-transition",
        "hecke-markov-interpretation",
        "hecke-markov-interpretation-table-data",
        "markov-lambda-knot-operations",
        "markov-chain-fluctuations",
        "q-gaussian-obstruction-at-q0",
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
        "qz-bicompletion",
        "quantum-dilogarithm-stratified",
        "quantum-dilogarithm-stratified-proof",
        "q-pochhammer-partial-product",
        "phi-q-categorical-truncation",
        "phi-q-categorical-truncation-proof",
        // Re-homed from the geometric-bridges collection: the pentagon
        // identities belong with the quantum dilogarithm.
        "pachner-pentagon-borromean",
        "q-rogers-pentagon-archimedean",
      ],
    }),
    section({
      title: "Archimedean realization and Kashaev volume",
      label: "sec:archimedean-realization-kashaev",
      blocks: [
        "intro-archimedean-realization-kashaev",
        "archimedean-realization-functor",
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
        "kashaev-volume-conjecture",
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
        "crossed-module-euler-characteristic",
        "geom-bridge-status",
        "tau-all-orders-bridge",
        "dim-master-pentagon",
        "geometric-invariant-piecewise",
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
        "mass-volume-factorization",
        "frobenius-packing-density",
        "crossing-graded-mass-expansion",
        "crossing-graded-mass-expansion-table-data",
        "lifted-crossing-locality",
        "mass-categorical-descent",
        "descended-level-zero",
        "jet-tower-convergence",
        "delta-max-uniform-bound",
        "mass-tower-syt-cells",
        "markov-pair-z2",
      ],
    }),

    section({
      title: "Mutant Jones falsifiability and Bloch group closure",
      label: "sec:mutant-jones-bloch-group",
      blocks: [
        "intro-mutant-jones-bloch-group",
        "knot-indexed-convolution-grid",
        "knot-indexed-convolution-grid-table2-data",
        "knot-indexed-convolution-grid-table1-data",
        "conway-kt-vol-injectivity-test",
        "jones-faithfulness-crossing-8",
        "wedderburn-as-noncomm-fourier",
        "degree-one-braid-trivial-volume",
        "pieri-photon-shift",
        "phi-q-tower-jsj-bridge",
        "dilogarithm-archimedean-limit",
        "phi-q-wkb-greens-function",
        "algebraic-geometric-dilog-equivalence",
        "shared-denominator-cusp-holonomy",
        "quantum-bloch-group",
        "degree-two-baryon-weight",
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
            // Algebraic shortcut of KS Thm 8 (multiplicative invariant) via the Markov property.
            "ks-multiplicativity-via-markov",
            "markov-trace-ratio-exact",
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
          ],
        }),
        section({
          title: "Schur-Weyl decomposition and positivity",
          label: "sec:phi-q-schur-weyl-positivity",
          blocks: [
            "schur-weyl-mass-decomposition",
            "gb-residue-spectral-sum",
            "categorical-mass-positivity",
            "mass-spectrum-generating-function",
            "graded-markov-trace-from-gs-filtration",
            "residue-at-root",
          ],
        }),
      ],
    }),

    section({
      title: "$\\\\varphi_q$ resummation: residue and Habiro identifications",
      label: "sec:phi-q-markov-residue-habiro",
      blocks: [
        "phi-q-markov-residue-habiro-intro",
        "vhat-pair-commutation-trace",
        "tower-pair-equality-fixed-level",
        "jet-tower-uniform-delta-max",
        "topological-mass-formula-algebraic",
        "residue-as-braid-holonomy",
        "graded-trace-residue-split",
        "term6-binding-density",
        "term6-binding-density-table2-data",
        "term6-binding-density-table1-data",
        "full-pole-structure-mass-trace",
        "habiro-residue-sum-equivalence",
      ],
    }),

    section({
      title: "Cyclotomic depth-3 trilog identities",
      label: "sec:cyclotomic-depth-3-trilog",
      blocks: [
        "intro-cyclotomic-depth-3-trilog",
        "bring-trilog-depth-3-witness",
        "bring-trilog-imaginary-tate-rational",
        "cl3-zeta5-orbit-sum-identity",
        "cyclotomic-trilog-imaginary-closed-form",
        "cyclotomic-trilog-imaginary-closed-form-table-data",
        "cyclotomic-cl3-orbit-sum-general",
        "cyclotomic-cl3-orbit-sum-general-table-data",
        "cyclotomic-depth3-dimension-synthesis",
        "cyclotomic-depth3-dimension-synthesis-table2-data",
        "cyclotomic-depth3-dimension-synthesis-table1-data",
        "jonquiere-cyclotomic-tate-rationality",
        "cyclotomic-orbit-sum-all-depths",
        "cyclotomic-orbit-sum-all-depths-table2-data",
        "cyclotomic-orbit-sum-all-depths-table1-data",
        "cyclotomic-dimension-synthesis-all-depths",
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
        "jet-filtered-knot-factor",
        "jet-convergence-classical-limit",
        "wigner-np-pairing",
        "unified-iterative-correction",
        "unified-iterative-correction-table-data",
        "knot-factor-frobenius-pairing",
        "wedderburn-weight-canonical",
        "hook-weight-derivation",
        "wigner-coefficient-derivation",
        "mass-coefficient-shadow-price",
        "frobenius-self-duality-forces-lp-dual-extraction",
      ],
    }),

    section({
      title: "LP-dual and Jucys-Murphy central elements",
      label: "sec:lp-dual-jucys-murphy",
      blocks: [
        "intro-lp-dual-jucys-murphy",
        "jucys-murphy-central-elements-qou",
        "spin-involution-lp-dual-invariance",
        "lp-dual-scaling-conjecture",
        "wigner-2-coefficient",
        "mass-endomorphism-tower",
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
        "chirality-from-frobenius-self-pairing",
        "curvature-rank-gb-stratification",
        "curvature-rank-gb-stratification-table-data",
        // Algebraic shortcut of KS ind-constructibility via the Diamond Lemma.
        "ks-finiteness-via-diamond-lemma",
        "spectral-sequence-collapse",
        "delta-q-decoration",
        "alpha-basis-knot-delta-q",
        "torus-knot-delta-q-writhe",
        "force-carrier-intertwining-correspondence",
        "alpha-shift-torus-knot",
        "alpha-shift-torus-knot-table-data",
      ],
    }),

    section({
      title: "Confinement-NF forcing and the per-nucleon shift",
      label: "sec:spectral-sequence-chirality-confinement-per-nucleon-shift",
      blocks: [
        "spectral-sequence-chirality-confinement-per-nucleon-shift-intro",
        "per-nucleon-shift-additive-linearity",
        "per-nucleon-shift-additive-linearity-table2-data",
        "per-nucleon-shift-additive-linearity-table1-data",
        "confinement-nf-structure-forcing",
        "confinement-nf-structure-forcing-table-data",
        "lp-duality-hypothesis-class",
        "confinement-nf-partial-proof",
        "bound-state-frobenius-self-dual-channel",
        "confinement-categorical",
        "exterior-square-borromean",
      ],
    }),

    section({
      title: "Plancherel-$\\\\alpha$ spectral foundations",
      label: "sec:plancherel-alpha-spectral",
      blocks: [
        "intro-plancherel-alpha-ribbon",
        "alpha-em-categorical-trace",
        "plancherel-term-7-formulation",
        "plancherel-weight-boundedness",
        "plancherel-weight-boundedness-table-data",
        "unified-curvature-rank-mass-formula",
        "unified-curvature-rank-mass-formula-table-data",
        "chirality-residue-mass-term",
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
        "knot-factor-amphicheiral",
        "knot-factor-borromean-composite",
        "knot-factor-shell-closed",
        "knot-factor-spectral-summary",
        "pauli-factor-wedderburn",
        "mass-tower-coefficient-stratification",
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
        "confinement-sdp",
        "flavor-dressed-mass-from-substrate-split",
        "flavor-mass-splitting-bound",
        "alpha-k-derivation-procedure",
        "alpha-k-categorical-closure",
        "chi-lambda-w0-sign-weighting",
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
        "y-lambda-recipe-from-partition",
        "graded-hecke-energy-truncation-bound",
        "graded-hecke-energy-truncation-bound-table-data",
        "descent-rate-probe-sim",
        "multi-level-jet-sum-sim",
        "macdonald-hook-telescope",
        "demazure-fiber-markov-trace",
        "wenzl-bridge-applicability-qou",
      ],
    }),

    section({
      title: "The LR-tensor character bridge",
      label: "sec:wenzl-bridge-cyclotomic-lr-tensor-character",
      blocks: [
        "wenzl-bridge-cyclotomic-lr-tensor-character-intro",
        "lr-tensor-character-bridge",
        "wenzl-qmn-synergy",
        "explicit-alpha-k-h3",
        "explicit-alpha-k-h4",
        "wedderburn-bratteli-recursion",
        "y-lambda-sign-pattern",
        "terms-2-6-higher-operations",
        "terms-2-6-higher-operations-table2-data",
        "terms-2-6-higher-operations-table1-data",
      ],
    }),

    section({
      title: "Pre-Archimedean Derivation Chain and Audit",
      label: "sec:derivation-audit",
      blocks: [
        "derivation-audit-intro",
        "pre-archimedean-derivation-chain",
        "pre-archimedean-derivation-chain-table2-data",
        "pre-archimedean-derivation-chain-table1-data",
        "conj-canonical-knot-id-sdp",
        "conj-rho-prefactor-structural",
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
        "frobenius-limits-substrate-cost",
        "knot-mass-formula-unified",
        "nuclear-knot-classification",
        "geom-yekutieli-alignment",
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
        "six-term-per-derivation-weights-table1-data",
        "six-term-per-derivation-weights-table2-data",
        "six-term-per-derivation-weights-table3-data",
        "crystal-isospin-degeneracy",
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
        "borromean-baryon-mass-formula",
        "borromean-baryon-interpretation",
        "q-integer-mass-formula",
        "lambda-scale-substrate-form",
        "topological-mass-trefoil",
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
        "mass-tower-deeper-fillers",
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
        "rho-k-h3a-refinement",
        "s4-s3-half-symmetric-projection",
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
            "staircase-corner-hook",
            "staircase-partition",
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
