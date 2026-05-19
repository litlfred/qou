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
        "trm-hopf-sigma1-sq-closed-form",
        "hecke-log-decomposition",
        "hecke-algebra-from-braiding",
        "hecke-normal-form",
        "dark-vision-strand-bandwidth",
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
        "mobius-energy-intro",
        "mobius-energy",
        "mobius-energy-frobenius-kernel",
        "mobius-energy-frobenius-kernel-proof",
        "mobius-energy-proof",
        "non-self-intersection",
        "nsi-q-deformed-kernel",
        "nsi-q-deformed-kernel-proof",
        "non-self-intersection-proof",
      ],
    }),

    // ── Crossing energy and stability ───────────────────────────────────
    section({
      title: "Crossing energy and Coulomb charge",
      label: "sec:crossing-energy",
      blocks: [
        "crossing-energy-intro",
        "crossing-energy",
        "crossing-energy-trefoil",
        "commutative-crossing-energy",
        "coulomb-charge",
        "skein-crossing-asymmetry-prop",
        "skein-crossing-asymmetry",
        "skein-bar-antisymmetry",
      ],
    }),

    // ── Lagrange resolvents (categorical DFT) ─────────────────────────
    section({
      title: "Lagrange Resolvents and $q$-Deformed Kinematics",
      label: "sec:lagrange-q-kinematics",
      blocks: [
        "lagrange-q-kinematics-intro",
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
        "exceptional-divisor-reeb-intro",
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
        "vertex-factorisation-intro",
        "vertex-is-exceptional-divisor",
        "vertex-is-exceptional-divisor-proof",
        // Photon polarisation states as Hecke generators on the exceptional divisor
        "breit-wheeler-vertex",
        // Literature alignment: Bilson--Thompson preons, Hecke parity, photonic hopfions
        "breit-wheeler-vertex-literature",
        // Product factorization of the Markov trace
        "markov-trace-product",
        "markov-trace-product-interpretation",
        // Markov chain interpretation of the algebraic framework
        "hecke-markov-transition",
        "hecke-markov-interpretation",
        "markov-lambda-knot-operations",
        "markov-chain-fluctuations",
        // Feynman path integrals as categorical traces
        "feynman-eigenbasis-decomposition",
        "feynman-eigenbasis-decomposition-proof",
        "feynman-trace-collapse",
        "feynman-trace-collapse-proof",
        "feynman-markov-identification",
        "feynman-markov-identification-proof",
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
        "braiding-relations-intro",
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
        "hadron-algebra-intro",
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
        "skein-particle-generation-intro",
        "skein-generation",
        "skein-mass-from-linking",
        "skein-mass-from-linking-proof",
        "skein-generation-proof",
        "knot-particle-generation",
        "knot-particle-generation-interpretation",
        "knot-particle-correspondence",
        "knot-particle-dictionary",
        "binding-knots-visual-inventory",
      ],
    }),

    // ── Bundle structure and observation ───────────────────────────────
    section({
      title: "Bundle Structure and Observation",
      label: "sec:bundle-observation",
      blocks: [
        "bundle-observation-intro",
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
        "borromean-reidemeister-intro",
        "borromean-baryon",
        "borromean-baryon-interpretation",
        "borromean-baryon-mass-formula",
        "lambda-scale-substrate-form",
        "delta-skein-substrate-identity",
        "figure-8-muon-mass-cross-check",
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
        "categorical-mass-foundations-intro",
        "topological-mass",
        "topological-mass-cat-eigenspace",
        "topological-mass-cat-eigenspace-proof",
        "topological-mass-cat-descended",
        "topological-mass-cat-descended-proof",
        "topological-mass-cat-transient",
        "topological-mass-cat-transient-proof",
        "topological-mass-categorical-proof",
        "categorical-mass-markov",
        "atomic-mass-gb-nf",
        "rho-k-graded-expansion",
        "hecke-branching-trace-decomposition",
        "operator-valued-magnitude-budget",
        "q-hecke-seminormal-character-closure",
        "recomputed-low-isotope-mass-table",
        "markov-trace-antipode-polynomial-symmetry",
        "markov-trace-axiomatic-closed-form",
        "markov-trace-recursive-reducer",
        "markov-z-reconciliation",
        "mass-endomorphism-conjecture",
        "categorical-neutrality-saturated-shells",
        "phi-n-global-section",
      ],
    }),

    // ── Calibration and algebraic mass formula ──────────────────────────
    // ── Calibration and algebraic mass formula (P2 split 2026-05-19,
    //    phase 1): the 134-block sec:calibration-algebraic-mass
    //    (7.4× over the 3-18 band) split into 7 topical sub-sections
    //    following the mass-formula pedagogy: derivation → Hoefsmit
    //    & convergence → q-beta precision ladder → Archimedean
    //    realization → cyclotomic depth-3 → Hecke-Baer-star →
    //    mutant Jones falsifiability. The existing
    //    calibration-algebraic-mass-intro stays at the top of A as
    //    the umbrella narrative. Phase-1 densities 15/19/37/12/10/4/13.
    //    Section C (37) remains over the upper bound; phase-2
    //    follow-up will internal-split.

    // §A — Mass-formula derivation
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
        "wedderburn-mass-formula",
        "frobenius-s-classification",
        "commutative-chirality-vanishes",
        "derived-mass-formula-light-isotopes",
        "deuteron-binding-frobenius-codim",
        "hoefsmit-seminormal-form",
        "figure-eight-branching-rule",
      ],
    }),

    // §B — Hoefsmit, convergence, and atomic-shell evidence
    section({
      title: "Hoefsmit, convergence, and atomic-shell evidence",
      label: "sec:hoefsmit-convergence-atomic",
      blocks: [
        "universal-braid-branching",
        "hoefsmit-scattering-pipeline",
        "hecke-convergence-bound",
        "algebraic-quantum-volume",
        "habiro-ring",
        "habiro-expansion-atomic",
        "z-habiro-ring",
        "brane-tower-z-habiro",
        "per-partition-k-lambda-rule",
        "conj-magic-shell-stabilization",
        "two-row-stratum",
        "he4-channel-active-set",
        "he4-two-row-dominance",
        "he4-magic-shell-fingerprint",
        "schur-weyl-vanishing",
        "sw-3root-rational-integrand",
        "markov-trace-frobenius-selection",
        "hecke-1d-irrep-closed-form-character",
        "hoefsmit-V21-cos-symmetrization",
      ],
    }),

    // §C — q-beta precision ladder (PHASE-2 split 2026-05-19): the
    //   37-block sec:q-beta-precision-ladder from the phase-1
    //   calibration-algebraic-mass split is split into 3 topical
    //   sub-sections (Markov + braid-link foundations / chi-character
    //   closed-forms / Kashiwara-Jones interpretations and quantum-
    //   dilogarithm). The 12/13/12 densities all land in the 3-18 band.

    // §C1 — Markov axioms and braid-link enumeration
    section({
      title: "Markov axioms and braid-link enumeration",
      label: "sec:markov-axioms-braid-link",
      blocks: [
        "q-beta-categorical-precision-ladder",
        "c5-involution-leibniz-decomposition",
        "bar-symmetric-three-layer-synthesis",
        "markov-axioms-primitive",
        "markov-trace-inductive-limit",
        "braid-link-types",
        "braid-group-n-strand",
        "markov-closure-map-axiomatic",
        "F3-eps6-leading-eq-neg-2b-cubed",
        "q-beta-c3-hopf-three-fold-markov",
        "q-beta-gamma-gamma-canonical-derivation",
        "typed-b3-sub-braid-extraction",
        "ck-extraction-from-algebraic-rules",
        "h3-hecke-idempotents",
      ],
    }),

    // §C2 — Hecke u-coordinate, chi-character closed-forms
    section({
      title: "Hecke $u$-coordinate, $\\chi$-character closed-forms",
      label: "sec:hecke-chi-closed-forms",
      blocks: [
        "u-coordinate-discharges",
        "multi-link-jones-q1-extension",
        "per-wedderburn-block-c5-c6",
        "post-pr665-open-rd-inventory",
        "hecke-algebra-type-scaffold",
        "markov-trace-operator-construction",
        "chi-v3-closed-form-proof",
        "chi-per-irrep-cyclotomic-closed-forms",
        "per-block-hopf-jones-absorption-pattern",
        "conj-qbeta-c-k-closed-forms",
        "chi-v111-via-sign-substitution",
        "chi-v21-hoefsmit-matrix-derivation",
        "phi-d-syt-count-conjecture",
        "categorical-chain-convergence-mechanisms",
        "tau-M-asymptotic-rep-theory",
      ],
    }),

    // §C3 — Kashiwara-Jones interpretations and quantum-dilogarithm
    section({
      title: "Kashiwara-Jones interpretations and quantum-dilogarithm",
      label: "sec:kashiwara-jones-quantum-dilog",
      blocks: [
        "kashiwara-jones-alternation-interpretation",
        "hopf-jones-c3-categorical",
        "kashiwara-jones-c4-categorical",
        "borromean-baryon-interpretation",
        "canonical-braid-interface-composition",
        "prop-rigid-monoidal-structural-gap-invariance",
        "qz-bicompletion",
        "quantum-dilogarithm-stratified",
        "quantum-dilogarithm-stratified-proof",
        "q-pochhammer-partial-product",
        "phi-q-categorical-truncation",
        "phi-q-categorical-truncation-proof",
        "algebraic-quantum-volume-specialization",
      ],
    }),

    // §D — Archimedean realization (functor + Kashaev volume bridge)
    section({
      title: "Archimedean realization and Kashaev volume",
      label: "sec:archimedean-realization-kashaev",
      blocks: [
        "archimedean-realization-functor",
        // Absorbed from former Ch `encounter`: pre-tau-vs-post-tau
        // interprets `def:archimedean-realization-functor` directly
        // above and explains the τ-wall semantically.
        "pre-tau-vs-post-tau",
        "vol-through-tau",
        "vol-as-motivic-period",
        "kashaev-volume-density",
        "kashaev-as-archimedean-realization",
        "phi-q-piece",
        "phi-q-tower-algebraic-stratification",
        "kashaev-volume-conjecture",
        "figure-8-archimedean-illustration",
        // Graded-Mikusiński depth-2 instance: VC = depth-2 case of
        // conj:gb-depth-period-correspondence.
        "vc-as-depth-2-instance",
        // 50-digit numerical witness on the Bring-figure-8 embedding.
        "bring-figure-eight-depth-2-witness",
      ],
    }),

    // §E — Cyclotomic depth-3 trilog identities
    section({
      title: "Cyclotomic depth-3 trilog identities",
      label: "sec:cyclotomic-depth-3-trilog",
      blocks: [
        // 50-digit functional-equation cross-validated depth-3 witness.
        "bring-trilog-depth-3-witness",
        // Im Li_3(ζ_5) = 4π³/125 (Tate-rational, Kummer reflection).
        "bring-trilog-imaginary-tate-rational",
        // Cl_3(2π/5) + Cl_3(4π/5) = -(12/25)ζ(3) — orbit-sum identity.
        "cl3-zeta5-orbit-sum-identity",
        // PSLQ certifies Cl_3(2π/5) - Cl_3(4π/5) is irreducible at 10^8.
        "cl3-zeta5-pslq-independence",
        // General cyclotomic theorems generalising rounds 10-11.
        "cyclotomic-trilog-imaginary-closed-form",
        "cyclotomic-cl3-orbit-sum-general",
        // Dimension synthesis: (K-3)/2 genuinely-new at each prime K.
        "cyclotomic-depth3-dimension-synthesis",
        // General-depth theorems: Jonquière Tate-rationality + orbit-sum + dim.
        "jonquiere-cyclotomic-tate-rationality",
        "cyclotomic-orbit-sum-all-depths",
        "cyclotomic-dimension-synthesis-all-depths",
      ],
    }),

    // §F — Hecke-Baer-star foundation and chirality pairing
    section({
      title: "Hecke-Baer-star foundation and chirality pairing",
      label: "sec:hecke-baer-star-chirality",
      blocks: [
        // Hecke-algebra Baer-* foundation (generic q).
        "hecke-baer-star-generic",
        // Explicit central primitive idempotents via Murphy elements.
        "explicit-central-idempotent",
        // Bar involution → period chirality structure.
        "chirality-period-pairing",
        // Bring-embeddable knots: genus-bounded falsifiability targets.
        "bring-embeddable-knots",
      ],
    }),

    // §G — Mutant Jones falsifiability and Bloch group closure
    section({
      title: "Mutant Jones falsifiability and Bloch group closure",
      label: "sec:mutant-jones-bloch-group",
      blocks: [
        // Placement of paper's existing knot-indexed convolutions in
        // the bi-filtration grid.
        "knot-indexed-convolution-grid",
        // Conway-KT mutant pair: B1 Vol-injectivity sanity check.
        "conway-kt-vol-injectivity-test",
        // Tightening of Q3: Jones-faithfulness theorem at crossing ≤ 10.
        "jones-faithfulness-crossing-8",
        "archimedean-remainder-exponential-decay",
        "wedderburn-as-noncomm-fourier",
        "degree-one-braid-trivial-volume",
        "pieri-photon-shift",
        "phi-q-tower-jsj-bridge",
        "dilogarithm-archimedean-limit",
        "algebraic-geometric-dilog-equivalence",
        "shared-denominator-cusp-holonomy",
        "quantum-bloch-group",
        "degree-two-baryon-weight",
      ],
    }),

    // ── Atom, isotope, and confinement levels (P1 split 2026-05-19):
    //    the 43-block sec:atom-isotope-confinement is split into six
    //    topical sub-sections following the natural pedagogy:
    //    energy → confinement → pair production → particles & shells →
    //    atoms & isotopes → magic shells. The existing
    //    atom-isotope-confinement-intro stays at the top of A and
    //    previews all six sub-sections as an umbrella narrative.

    // §A — Knot-operator energy: the foundational invariant
    section({
      title: "Knot-operator energy",
      label: "sec:knot-operator-energy",
      blocks: [
        "atom-isotope-confinement-intro",
        "knot-operator-energy",
        "knot-operator-energy-exists",
        "knot-operator-energy-unique",
        "local-shadow-ordering",
      ],
    }),

    // §B — Confinement level: when knots stabilise into bound states
    section({
      title: "Confinement level and the cemetery group",
      label: "sec:confinement-level",
      blocks: [
        "confinement-level",
        "confinement-level-exists",
        "confinement-level-unique",
        "cemetery-group",
        "crystal-graph-realization",
        "confinement-grading-correspondence",
        "confinement-grading-correspondence-conditional",
        "cemetery-group-emergence",
        "ontological-agnosticism",
      ],
    }),

    // §C — Pair production and anyon collapse: operations on confined states
    section({
      title: "Pair production and anyon collapse",
      label: "sec:pair-production-anyon",
      blocks: [
        "symmetric-crystal-pair-production",
        "two-photon-pair-production",
        "hecke-anyonic-substrate",
        "root-of-unity-mtc-truncation",
        "kazhdan-lusztig-classical-limit",
        "anyon-observation-collapse",
      ],
    }),

    // §D — Confined particles and shells: the typed particle inventory
    section({
      title: "Confined particles and shells",
      label: "sec:confined-particles-shells",
      blocks: [
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
      ],
    }),

    // §E — Atom and isotope knots: compound bound states
    section({
      title: "Atom and isotope knots",
      label: "sec:atom-isotope-knots",
      blocks: [
        "atom-knot",
        "atom-knot-exists",
        "atom-knot-unique",
        "isotope-knot",
        "isotope-knot-equivalence",
        "stable-atom",
        "stable-atom-decidable",
        "unstable-atom",
        "unstable-atom-decay-channel",
      ],
    }),

    // §F — Magic shells: special-case stability under shell coupling
    section({
      title: "Magic shells and the $\\kappa$ coupling",
      label: "sec:magic-shells",
      blocks: [
        "ilp-solution-count-unwrap",
        "shell-schur-weyl-self-duality",
        "compound-beta-shell-calibration",
        "magic-shell-coupling-kappa",
        "quantum-dilogarithm-disambiguation",
      ],
    }),

    // ── Nuclear binding and beta stability ──────────────────────────────
    // ── Nuclear binding and beta stability (P2 split 2026-05-19,
    //    phase 1): the paper's largest section (sec:nuclear-binding-
    //    beta-stability, 134 blocks, 7.4× over the 3-18 band) split
    //    into 7 topical sub-sections following the substrate-binding
    //    pedagogy: setup → LP-dual → phi_q/Markov/Schur-Weyl tower →
    //    GS axiomatic backing → Frobenius nuclear structure →
    //    Plancherel/alpha/ribbon → alpha_k/Wenzl bridge. The
    //    existing nuclear-binding-beta-stability-intro stays at the
    //    top of A as the umbrella narrative for the whole 7-section
    //    arc. Densities 12/9/18/6/27/18/46. Sections E (27) and G
    //    (46) remain over the upper bound; phase 2 follow-up will
    //    apply internal splits to each.

    // §A — Substrate binding setup
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
        "knot-factor-frobenius-pairing",
        "wedderburn-weight-canonical",
        "hook-weight-derivation",
        "wigner-coefficient-derivation",
        "mass-coefficient-shadow-price",
        "frobenius-self-duality-forces-lp-dual-extraction",
      ],
    }),

    // §B — LP-dual and Jucys-Murphy central elements
    section({
      title: "LP-dual and Jucys-Murphy central elements",
      label: "sec:lp-dual-jucys-murphy",
      blocks: [
        "jucys-murphy-central-elements-qou",
        "mass-formula-iterative-lp-dual",
        "alpha-5-jm-central-empirical-findings",
        "lp-dual-isospin-invariance",
        "spin-involution-lp-dual-invariance",
        "lp-dual-scaling-conjecture",
        "wigner-2-coefficient",
        "mass-endomorphism-tower",
        "mass-endomorphism-jet-tower",
      ],
    }),

    // §C — phi_q resummation, Markov trace, Schur-Weyl tower
    section({
      title: "$\\varphi_q$ resummation, Markov trace, and Schur-Weyl tower",
      label: "sec:phi-q-markov-schur-weyl-tower",
      blocks: [
        "phi-q-resums-trace-series",
        "markov-axiom-recursive-ascent",
        "per-braid-mass-tower",
        "schur-weyl-mass-decomposition",
        "gb-residue-spectral-sum",
        "categorical-mass-positivity",
        "mass-spectrum-generating-function",
        "graded-markov-trace-from-gs-filtration",
        "residue-at-root",
        "vhat-pair-commutation-trace",
        "tower-pair-equality-fixed-level",
        "jet-tower-uniform-delta-max",
        "topological-mass-formula-algebraic",
        "residue-as-braid-holonomy",
        "graded-trace-residue-split",
        "term6-binding-density",
        "full-pole-structure-mass-trace",
        "habiro-residue-sum-equivalence",
      ],
    }),

    // §D — Gröbner-Shirshov axiomatic backing
    section({
      title: "Gröbner-Shirshov axiomatic backing",
      label: "sec:gs-axiomatic-backing",
      blocks: [
        // GAP 13a — explicit conjectures backing GS noncomputable opaque axioms
        "gs-graded-markov-trace-existence",
        "gs-residue-at-root-existence",
        "gs-spectral-decomposition-existence",
        "gs-spectral-sum-finite",
        "gs-archimedean-agreement-trace",
        "gs-archimedean-agreement-residue",
      ],
    }),

    // §E — Frobenius nuclear structure (PHASE-2 split 2026-05-19):
    //   the 27-block sec:frobenius-nuclear-structure from the phase-1
    //   nuclear-binding split is split into 2 sub-sections: parity-
    //   classification-and-discrepancy (~12) and spectral-sequence-
    //   chirality-and-confinement (~15). Both within the 3-18 band.

    // §E1 — Parity classification, atomic atlas, and discrepancy resolution
    section({
      title: "Parity classification, atomic atlas, and discrepancy resolution",
      label: "sec:parity-classification-discrepancy",
      blocks: [
        "mn-classical-parity-blind",
        "q-character-closes-parity-gap",
        "frobenius-codim-universal",
        "frobenius-limits-substrate-cost",
        "knot-mass-formula-unified",
        "nuclear-knot-classification",
        "geom-yekutieli-alignment",
        "content-scaling-correspondence",
        "partition-sum-proton-residual",
        "np-discrepancy-resolution",
        "mass-formula-regime-switching",
      ],
    }),

    // §E2 — Spectral sequence, chirality, and confinement-NF structure
    section({
      title: "Spectral sequence, chirality, and confinement-NF structure",
      label: "sec:spectral-sequence-chirality-confinement",
      blocks: [
        "jet-prefix-gb-filtration",
        "chirality-from-frobenius-self-pairing",
        "gb-spectral-sequence",
        "curvature-rank-gb-stratification",
        "spectral-sequence-collapse",
        "delta-q-decoration",
        "force-carrier-intertwining-correspondence",
        "alpha-shift-torus-knot",
        "per-nucleon-shift-additive-linearity",
        "confinement-nf-structure-forcing",
        "lp-duality-hypothesis-class",
        "confinement-nf-partial-proof",
        "bound-state-frobenius-self-dual-channel",
        "confinement-categorical",
        "exterior-square-borromean",
      ],
    }),

    // §F — Plancherel, alpha, ribbon, knot-factor
    section({
      title: "Plancherel, $\\alpha$, ribbon, and knot-factor",
      label: "sec:plancherel-alpha-ribbon",
      blocks: [
        "alpha-em-categorical-trace",
        "plancherel-term-7-formulation",
        "plancherel-weight-boundedness",
        "unified-curvature-rank-mass-formula",
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
        "flavor-dressing-functor",
      ],
    }),

    // §G — alpha_k derivation, Wenzl bridge, beta stability (PHASE-2
    //   split 2026-05-19): the 43-block sec:alpha-k-wenzl-bridge from
    //   the phase-1 nuclear-binding split is split into 4 sub-sections:
    //   alpha_k procedure (~9) / Wenzl bridge & cyclotomic (~13) /
    //   crystal & isospin & chirality (~9) / beta-stability closure
    //   (~12). All within the 3-18 band.

    // §G1 — alpha_k derivation procedure
    section({
      title: "$\\alpha_k$ derivation procedure",
      label: "sec:alpha-k-procedure",
      blocks: [
        "flavor-dressed-mass-from-substrate-split",
        "flavor-mass-splitting-bound",
        "alpha-k-derivation-procedure",
        "alpha-k-categorical-closure",
        "chi-lambda-w0-sign-weighting",
        "averaging-resonance-rule",
        "atom-knot-mass-derivation",
        "atom-knot-mass-derivation-proof",
        "joint-tower-sdp-confinement",
        "y-lambda-closed-form-wenzl-bridge",
      ],
    }),

    // §G2 — Wenzl bridge, cyclotomic factorisation, and explicit alpha_k
    section({
      title: "Wenzl bridge, cyclotomic factorisation, and explicit $\\alpha_k$",
      label: "sec:wenzl-bridge-cyclotomic",
      blocks: [
        "y-lambda-cyclotomic-factorization",
        "y-lambda-recipe-from-partition",
        "graded-hecke-energy-truncation-bound",
        "descent-rate-probe-sim",
        "multi-level-jet-sum-sim",
        "macdonald-hook-telescope",
        "demazure-fiber-markov-trace",
        "wenzl-bridge-applicability-qou",
        "explicit-alpha-k-h3",
        "explicit-alpha-k-h4",
        "wedderburn-bratteli-recursion",
        "y-lambda-sign-pattern",
        "terms-2-6-higher-operations",
      ],
    }),

    // §G3 — Six-term, crystal, isospin, and chirality
    section({
      title: "Six-term mass formula, crystal, isospin, and chirality",
      label: "sec:six-term-crystal-isospin-chirality",
      blocks: [
        "six-term-mass-formula-complete",
        "six-term-per-derivation-weights",
        "shell-correction-term-seven",
        "crystal-isospin-degeneracy",
        "isospin-mass-split-em-localisation",
        "option-e-isospin-test",
        "crystal-bases-path-a",
        "chirality-dual-space-derivation",
        "frobenius-antipode-unifies-chirality-and-tower",
      ],
    }),

    // §G4 — Beta stability closure
    section({
      title: "Beta stability closure",
      label: "sec:beta-stability-closure",
      blocks: [
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

    // ── Derivation audit and pre-Archimedean framework ────────────────
    section({
      title: "Pre-Archimedean Derivation Chain and Audit",
      label: "sec:derivation-audit",
      blocks: [
        "pre-archimedean-derivation-chain",
        "derivation-audit-report",
        "conj-canonical-knot-id-sdp",
        "conj-chirality-ribbon-frobenius",
        "conj-brane-level-selection",
        "conj-rho-prefactor-structural",
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

    // ── Classical limit and the macroscopic continuum ─────────────────
    // Absorbed from former `algebraic-substrate / sec:classical-limit`
    // (now dissolved). The classical-limit machinery (motivic + adelic
    // substrate, joint Galois-braid action, two-filtration bridge,
    // classical Riemann zeta / RH statement) is heavy braid-coupled
    // (32 uses → braids, 13 reverse) and belongs adjacent to the rest
    // of the braid content.
    //
    // NOTE: surreal-bound formalism (BSD, Collatz, P-vs-NP, RH,
    // Yang-Mills surreal bounds + millennium-unification + the
    // graded-Mikusiński unification remark) is in
    // `appendix-surreals/sec:millennium-bounds-via-surreals`, joining
    // the rest of the surreal-formalism story. Cheat-sheet remark for
    // first-time surreal notation should sit at the head of this
    // section's surreal-flavored sub-block (reeb-epsilon / q-from-epsilon).
    section({
      title: "Classical limit and the macroscopic continuum",
      label: "sec:classical-limit",
      blocks: [
        "classical-limit-intro",
        "motivic-substrate",
        "adelic-substrate",
        "classical-limit-functor",
        "quantum-gap-collapse",
        "classical-limit-obstruction",
        "qou-obstruction-reduction",
        // Surreal error calculus (substrate-level — see appendix
        // for the full surreal formalism). The cheat-sheet remark
        // immediately below is for first-time readers of $\omega$
        // and $\varepsilon$ notation; it points to app:surreals
        // for the Conway construction, sign sequences, standard-part
        // functor, etc.
        "surreal-notation-cheat-sheet",
        "reeb-epsilon",
        "q-from-epsilon",
        // Graded-Mikusiński / joint-Galois-braid machinery.
        "gb-depth-period-correspondence",
        "hq-bi-filtration",
        "joint-galois-braid-action",
        "joint-galois-braid-figure-8-verified",
        "joint-galois-braid-discharged",
        "graded-baer-star-Hq",
        "two-filtration-bridge",
        "two-filtration-bridge-small-cases",
        "two-filtration-bridge-general",
        "cl3-zeta5-geometric-realization",
        // Classical (q = 1) zeta + RH statement.
        "classical-riemann-zeta",
        "classical-riemann-hypothesis",
        "macroscopic-stability-equivalence",
        // Adelic Tate squeeze — surreal-bound infrastructure used
        // by the appendix-surreal Millennium bounds; lives here as
        // the bridge to those bounds.
        "adelic-tate-squeeze",
      ],
    }),
  ],
});
