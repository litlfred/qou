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

    // Detangler P5 split (2026-05-23): 19-block sec:categorical-braiding
    // split into braid-action + Hecke-eigenbasis.
    section({
      title: "Categorical origin of braiding: the braid action",
      label: "sec:categorical-braiding-action",
      blocks: [
        "categorical-braiding-intro",
        "braid-action-tensor",
        "braid-action-tensor-proof",
        "why-b3",
        "categorical-boson-fermion",
        "symmetric-quotient-colour",
        "braid-base-field",
        "braid-lifting-compatibility",
      ],
    }),
    section({
      title: "Categorical braiding: Hecke quotient and knot eigenbasis",
      label: "sec:categorical-braiding-hecke-eigenbasis",
      blocks: [
        "categorical-braiding-hecke-eigenbasis-intro",
        "jones-markov-trace",
        "trm-hopf-sigma1-sq-closed-form",
        "trm-hopf-sigma1-sq-closed-form-table2-data",
        "trm-hopf-sigma1-sq-closed-form-table1-data",
        "hecke-log-decomposition-table-data",
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
        "knot-notation-convention-table2-data",
        "knot-notation-convention-table1-data",
      ],
    }),

    section({
      title: "$\\mathrm{SU}(2)$ and $\\mathrm{SO}(3)$ framework",
      label: "sec:su2-so3",
      blocks: [
        "su2-so3-intro",
        "su2-basis",
        "first-order-taylor",
        // su2-generators relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "so3-generators",
        "quaternion-so3-motivation",
      ],
    }),

    section({
      title: "Braid involutions and holonomy",
      label: "sec:braid-involutions",
      blocks: [
        "braid-involutions-intro",
        // prop:lagrange-resolvent-transform moved here from
        // archimedean-universe/sec:bring-algebraic-substructure per
        // detangler P37 (2026-05-22). 6 H1 fwd-refs cleared.
        // Emits new H2 to def:brings-surface @ archimedean-universe
        // (accepted §5).
        "lagrange-resolvent-transform",
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

    // ── Vertex factorisation through E_p ──────────────────────────────
    // Detangler P6 split (2026-05-23): 23-block sec:vertex-factorisation
    // split into vertex/Markov + Feynman identifications.
    section({
      title: "Vertex factorisation: exceptional divisor + Markov trace",
      label: "sec:vertex-factorisation-markov",
      blocks: [
        "vertex-factorisation-intro",
        "vertex-is-exceptional-divisor",
        "vertex-is-exceptional-divisor-proof",
        // Bridge from the six-canonical-knot-operators table
        // (sec:exceptional-divisor-reeb) into the vertex-
        // factorisation specialisation.
        "six-operators-via-vertex-factorisation",
        "six-operators-via-vertex-factorisation-table-data",
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
        "hecke-markov-interpretation-table-data",
        "markov-lambda-knot-operations",
        "markov-chain-fluctuations",
      ],
    }),
    section({
      title: "Vertex factorisation: Feynman identifications",
      label: "sec:vertex-factorisation-feynman",
      blocks: [
        "vertex-factorisation-feynman-intro",
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
        "feynman-qou-dictionary-table-data",
        "feynman-classical-limit",
        "feynman-classical-limit-interpretation",
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

        "vertex-algebra-relations-table1-data",
        "vertex-algebra-relations-table2-data",
        "vertex-algebra-relations-table3-data",
        "vertex-algebra-jet-relations",

        "vertex-algebra-jet-relations-table1-data",
        "vertex-algebra-jet-relations-table2-data",
        "vertex-algebra-jet-relations-table3-data",
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
        // def:atomic-braid moved here from
        // particle-interactions/sec:atomic-braid-mass per detangler
        // P32 (2026-05-22). 8 H1 fwd-refs cleared. Emits new H2 to
        // def:transfer-matrix-operator + def:derived-atom @
        // particle-interactions (accepted §5).
        "atomic-braid",
        "atomic-braid-table1-data",
        "skein-generation",
        "skein-mass-from-linking",
        "skein-mass-from-linking-proof",
        "skein-generation-proof",
        "knot-particle-generation",
        "knot-particle-generation-table-data",
      ],
    }),
    section({
      title: "Skein Generation and Particle Correspondence : generation",
      label: "sec:skein-particle-generation-knot-particle-generation",
      blocks: [
        "skein-particle-generation-knot-particle-generation-intro",
        "knot-particle-generation-interpretation",
        "knot-particle-correspondence",
        "knot-particle-dictionary",

        "knot-particle-dictionary-table1-data",
        "knot-particle-dictionary-table2-data",
        "knot-particle-dictionary-table3-data",
        "knot-particle-dictionary-table4-data",
        "binding-knots-visual-inventory",
        "binding-knots-visual-inventory-table2-data",
        "binding-knots-visual-inventory-table1-data",
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
        "sorting-color-energy-table-data",
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
        "fermion-boson-knot-link-table-data",
        "reidemeister-mass-invariance",
        "shell-transition-knot",

        "shell-transition-knot-table1-data",
        "shell-transition-knot-table2-data",
        "shell-transition-knot-table3-data",
        "shell-transition-knot-interpretation",
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
        "intro-markov-axioms-braid-link",
        "q-beta-categorical-precision-ladder",

        "q-beta-categorical-precision-ladder-table1-data",
        "q-beta-categorical-precision-ladder-table2-data",
        "q-beta-categorical-precision-ladder-table3-data",
        "bar-involution",

        "bar-involution-table1-data",
        "bar-involution-table2-data",
        "bar-involution-table3-data",
        "bar-involution-table4-data",
        "bar-involution-table5-data",
        "bar-involution-table6-data",
        "bar-involution-table7-data",
        "bar-involution-table8-data",
        "q-zero-complex-extension",
        "lusztig-vs-hermitian-bar",
        "polynomial-bar-involution",
      ],
    }),
    section({
      title: "Markov axioms and braid-link enumeration : generation",
      label: "sec:markov-axioms-braid-link-li2q-phiq-bar",
      blocks: [
        "markov-axioms-braid-link-li2q-phiq-bar-intro",
        "polynomial-bar-involution-table-data",
        "c5-involution-leibniz-decomposition",
        "markov-axioms-primitive",
        "markov-trace-inductive-limit",
        "braid-link-types",
        "braid-group-n-strand",
        "braid-group-n-strand-table3-data",
      ],
    }),
    section({
      title: "Markov axioms and braid-link enumeration (continued) : generation",
      label: "sec:markov-axioms-braid-link-markov-closure-map",
      blocks: [
        "markov-axioms-braid-link-markov-closure-map-intro",
        "braid-group-n-strand-table2-data",
        "braid-group-n-strand-table1-data",
        "markov-closure-map-axiomatic",
        "F3-eps6-leading-eq-neg-2b-cubed",
        "q-beta-c3-hopf-three-fold-markov",
        "q-beta-gamma-gamma-canonical-derivation",
        "typed-b3-sub-braid-extraction",
        "ck-extraction-from-algebraic-rules",
        "ck-extraction-from-algebraic-rules-table2-data",
        "ck-extraction-from-algebraic-rules-table1-data",
        "h3-hecke-idempotents",
      ],
    }),

    // §C3 — Kashiwara-Jones interpretations and quantum-dilogarithm
    section({
      title: "Kashiwara-Jones interpretations and quantum-dilogarithm",
      label: "sec:kashiwara-jones-quantum-dilog",
      blocks: [
        "intro-kashiwara-jones-quantum-dilog",
        // prop:sw-period-thimble-equivalence moved here from
        // archimedean-universe/sec:topological-mass-spectrum per
        // detangler P36 (2026-05-22). 6 H1 fwd-refs cleared.
        // New H2 to rem:picard-lefschetz-thimble,
        // prop:baryon-product-from-alt + 1 more @ archimedean-universe
        // (accepted §5).
        "kashiwara-jones-alternation-interpretation",
        "hopf-jones-c3-categorical",
        "kashiwara-jones-c4-categorical",
        "borromean-baryon-interpretation",
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
      ],
    }),

    // §D — Archimedean realization (functor + Kashaev volume bridge)
    section({
      title: "Archimedean realization and Kashaev volume",
      label: "sec:archimedean-realization-kashaev",
      blocks: [
        "intro-archimedean-realization-kashaev",
        "archimedean-realization-functor",
        "archimedean-image-table",
        "archimedean-image-table-table2-data",
        "archimedean-image-table-table1-data",
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
        // Graded-Mikusiński depth-period correspondence: keystone
        // conjecture relating GS-depth filtration to Goncharov
        // periods. Moved here (was sec:classical-limit) so its
        // downstream consumers (vc-as-depth-2-instance,
        // bring-figure-eight-depth-2-witness, and the rest of the
        // graded-Mikusiński machinery in this chapter) sit AFTER
        // the conjecture they reference. Detangler P35 (2026-05-22).
        "gb-depth-period-correspondence",
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
        "intro-cyclotomic-depth-3-trilog",
        "bring-trilog-depth-3-witness",
        // Im Li_3(ζ_5) = 4π³/125 (Tate-rational, Kummer reflection).
        "bring-trilog-imaginary-tate-rational",
        // Cl_3(2π/5) + Cl_3(4π/5) = -(12/25)ζ(3) — orbit-sum identity.
        "cl3-zeta5-orbit-sum-identity",
        // PSLQ certifies Cl_3(2π/5) - Cl_3(4π/5) is irreducible at 10^8.
        "cl3-zeta5-pslq-independence",
        // General cyclotomic theorems generalising rounds 10-11.
        "cyclotomic-trilog-imaginary-closed-form",
        "cyclotomic-trilog-imaginary-closed-form-table-data",
        "cyclotomic-cl3-orbit-sum-general",
        "cyclotomic-cl3-orbit-sum-general-table-data",
        // Dimension synthesis: (K-3)/2 genuinely-new at each prime K.
        "cyclotomic-depth3-dimension-synthesis",
        "cyclotomic-depth3-dimension-synthesis-table2-data",
        "cyclotomic-depth3-dimension-synthesis-table1-data",
        // General-depth theorems: Jonquière Tate-rationality + orbit-sum + dim.
        "jonquiere-cyclotomic-tate-rationality",
        "cyclotomic-orbit-sum-all-depths",
        "cyclotomic-orbit-sum-all-depths-table2-data",
        "cyclotomic-orbit-sum-all-depths-table1-data",
        "cyclotomic-dimension-synthesis-all-depths",
      ],
    }),

    // §F — Hecke-Baer-star foundation and chirality pairing
    section({
      title: "Hecke-Baer-star foundation and chirality pairing",
      label: "sec:hecke-baer-star-chirality",
      blocks: [
        // Hecke-algebra Baer-* foundation (generic q).
        "intro-hecke-baer-star-chirality",
        "hecke-baer-star-generic",
        // Explicit central primitive idempotents via Murphy elements.
        "explicit-central-idempotent",
        // Bar involution → period chirality structure.
        "chirality-period-pairing",
        // Bring-embeddable knots: genus-bounded falsifiability targets.
        "bring-embeddable-knots",
        "bring-embeddable-knots-table-data",
      ],
    }),

    // §G — Mutant Jones falsifiability and Bloch group closure
    section({
      title: "Mutant Jones falsifiability and Bloch group closure",
      label: "sec:mutant-jones-bloch-group",
      blocks: [
        // Placement of paper's existing knot-indexed convolutions in
        "intro-mutant-jones-bloch-group",
        // the bi-filtration grid.
        "knot-indexed-convolution-grid",
        "knot-indexed-convolution-grid-table2-data",
        "knot-indexed-convolution-grid-table1-data",
        // Conway-KT mutant pair: B1 Vol-injectivity sanity check.
        "conway-kt-vol-injectivity-test",
        // Tightening of Q3: Jones-faithfulness theorem at crossing ≤ 10.
        "jones-faithfulness-crossing-8",
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
        "intro-confinement-level",
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
        "intro-pair-production-anyon",
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
        "intro-confined-particles-shells",
        "confined-particle",
        "confinement-category",
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
        "intro-atom-isotope-knots",
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
        "intro-magic-shells",
        "ilp-solution-count-unwrap",
        "shell-schur-weyl-self-duality",
        "compound-beta-shell-calibration",
        "compound-beta-shell-calibration-table3-data",
        "compound-beta-shell-calibration-table2-data",
        "compound-beta-shell-calibration-table1-data",
        "magic-shell-coupling-kappa",
        "magic-shell-coupling-kappa-table-data",
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
        "unified-iterative-correction-table-data",
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
        "intro-lp-dual-jucys-murphy",
        "jucys-murphy-central-elements-qou",
        "alpha-5-jm-central-empirical-findings",
        "spin-involution-lp-dual-invariance",
        "lp-dual-scaling-conjecture",
        "wigner-2-coefficient",
        "mass-endomorphism-tower",
        "mass-endomorphism-jet-tower",
        "mass-endomorphism-jet-tower-table1-data",
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
      title: "Parity classification, atomic atlas, and discrepancy resolution : generation",
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

    // §E2 — Spectral sequence, chirality, and confinement-NF structure
    section({
      title: "Spectral sequence, chirality, and confinement-NF structure",
      label: "sec:spectral-sequence-chirality-confinement",
      blocks: [
        "intro-spectral-sequence-chirality-confinement",
        "jet-prefix-gb-filtration",
        "chirality-from-frobenius-self-pairing",
        "curvature-rank-gb-stratification",
        "curvature-rank-gb-stratification-table-data",
        "spectral-sequence-collapse",
        "delta-q-decoration",
        "force-carrier-intertwining-correspondence",
        "alpha-shift-torus-knot",
        // Detangler R3 (2026-05-23): 6-row witness summary extracted
        // from alpha-shift-torus-knot.md.
        "alpha-shift-torus-knot-table-data",
      ],
    }),
    section({
      title: "Spectral sequence, chirality, and confinement-NF structure : generation",
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

    // §F — Plancherel, alpha, ribbon, knot-factor
    // Detangler P10 split (2026-05-23): 19-block
    // sec:plancherel-alpha-ribbon split into spectral + knot-factor.
    section({
      title: "Plancherel-$\\alpha$ spectral foundations",
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
        "intro-alpha-k-procedure",
        // prop:confinement-sdp moved here from
        // particle-interactions/sec:confinement-selection per
        // detangler P33 (2026-05-22). 7 H1 fwd-refs cleared.
        // New H2 to prop:confinement-lp (accepted §5).
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
      title: "$\\alpha_k$ derivation procedure : generation",
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

    // §G2 — Wenzl bridge, cyclotomic factorisation, and explicit alpha_k
    section({
      title: "Wenzl bridge, cyclotomic factorisation, and explicit $\\alpha_k$",
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
      title: "Wenzl bridge, cyclotomic factorisation, and explicit $\\alpha_k$ : generation",
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

    // §G3 — Six-term, crystal, isospin, and chirality
    section({
      title: "Six-term mass formula, crystal, isospin, and chirality",
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
      ],
    }),
    section({
      title: "Six-term mass formula, crystal, isospin, and chirality : generation",
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

    // §G4 — Beta stability closure
    section({
      title: "Beta stability closure",
      label: "sec:beta-stability-closure",
      blocks: [
        "intro-beta-stability-closure",
        "deuteron-first-principles",

        "deuteron-first-principles-table1-data",
        "deuteron-first-principles-table2-data",
        "deuteron-first-principles-table3-data",
        "deuteron-first-principles-table4-data",
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
        "derivation-audit-intro",
        "pre-archimedean-derivation-chain",
        "pre-archimedean-derivation-chain-table2-data",
        "pre-archimedean-derivation-chain-table1-data",
        "derivation-audit-report",
        "derivation-audit-report-table2-data",
        "derivation-audit-report-table1-data",
        "conj-canonical-knot-id-sdp",
        "conj-chirality-ribbon-frobenius",
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
        // hyperelliptic-quintic relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "hyperelliptic-z5-classification",
        // x5-z5-automorphism relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "bring-z5-descent",
        // x5-bring-weight-identification relocated to archimedean-universe/ (PR #823 fit-section-chapter audit)
        "x5-bring-prym-jacobian",
        "weight-identification-consequences",
        // u1-equivariant-reduction relocated to quantum-observable-universes/ (PR #823 fit-section-chapter audit)
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
    // Detangler P11 split (2026-05-22): the 23-block
    // sec:classical-limit was split into construction (the
    // functor + obstruction + joint-Galois-braid machinery) and
    // implications (graded Baer-star + two-filtration bridge +
    // classical zeta/RH + adelic squeeze + chapter outro). Each
    // new section sits in the 3-18 block band.
    section({
      title: "Classical limit: construction",
      label: "sec:classical-limit-construction",
      blocks: [
        "classical-limit-intro",
        "adelic-substrate",
        "classical-limit-functor",
        "quantum-gap-collapse",
        "classical-limit-obstruction",
        "qou-obstruction-reduction",
        "qou-obstruction-reduction-table4-data",
        "qou-obstruction-reduction-table3-data",
        "qou-obstruction-reduction-table2-data",
        "qou-obstruction-reduction-table1-data",
        // Surreal error calculus (substrate-level — see appendix
        // for the full surreal formalism). The cheat-sheet remark
        // immediately below is for first-time readers of $\omega$
        // and $\varepsilon$ notation; it points to app:surreals
        // for the Conway construction, sign sequences, standard-part
        // functor, etc.
        "surreal-notation-cheat-sheet",
        "surreal-notation-cheat-sheet-table-data",
        "reeb-epsilon",
        "q-from-epsilon",
        // Graded-Mikusiński / joint-Galois-braid machinery.
        // (conj:gb-depth-period-correspondence moved earlier to
        // sec:archimedean-realization-kashaev per detangler P35;
        // its downstream consumers here now reference it backward.)
        "hq-bi-filtration",
        "joint-galois-braid-action",
        "joint-galois-braid-figure-8-verified",
        "joint-galois-braid-discharged",
      ],
    }),
    section({
      title: "Classical limit: implications",
      label: "sec:classical-limit-implications",
      blocks: [
        "classical-limit-implications-intro",
        "graded-baer-star-Hq",
        "two-filtration-bridge",
        "two-filtration-bridge-small-cases",
        "two-filtration-bridge-small-cases-table-data",
        "two-filtration-bridge-general",
        "two-filtration-bridge-general-table-data",
        "cl3-zeta5-geometric-realization",
        // Classical (q = 1) zeta + RH statement.
        "classical-riemann-zeta",
        "classical-riemann-hypothesis",
        "macroscopic-stability-equivalence",
        // Adelic Tate squeeze — surreal-bound infrastructure used
        // by the appendix-surreal Millennium bounds; lives here as
        // the bridge to those bounds.
        "adelic-tate-squeeze",
        "outro-braids-and-knots",
      ],
    }),
  ],
});
