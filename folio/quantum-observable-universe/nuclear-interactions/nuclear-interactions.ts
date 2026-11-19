import { chapter, section } from "../../schema/builders";

/**
 * Chapter 11: Nuclear Interactions and Binding.
 *
 * Computational many-body nuclear engine:
 *   1. Gröbner–Shirshov normal-form reduction in H_A(q)
 *   2. Confinement LP/SDP operator selection
 *   3. Nucleon–nucleon isospin selection, Wigner SU(4), and mirror symmetry
 *   4. Transfer matrices and beta-decay transitions
 *   5. Composite atomic braid and Wedderburn binding
 *   6. Branching Q-values, pair production, and beta-stability closure
 */
export default chapter({
  title: "Nuclear Interactions and Binding",
  label: "chap:nuclear-interactions",
  sections: [
    // ── §1. Gröbner–Shirshov normal-form reduction ───────────────
    section({
      title: "The Gröbner–Shirshov Reduction Engine",
      label: "sec:groebner-engine",
      blocks: [
        "particle-interactions-intro",
        "nuclear-groebner-reduction",
        "nuclear-groebner-reduction-proof",
        "nuclear-groebner-reduction-computational",
        "groebner-shirshov-energy",
        "groebner-shirshov-energy-proof",
        "groebner-shirshov-energy-interpretation",
        "inductive-gb-reduction",
        "inductive-gb-reduction-proof",
        "nuclear-reduction-algorithm",
        "nucleon-ordering-factorization",
        "nucleon-ordering-factorization-proof",
        "box-braid-irreducibility",
        "box-braid-irreducibility-proof",
        "box-braid-irreducibility-interpretation",
        "generator-volume-decomposition",
        "generator-volume-decomposition-proof",
      ],
    }),

    // ── §2. Confinement LP/SDP operator selection ────────────────
    section({
      title: "Confinement Operator Selection",
      label: "sec:confinement-selection",
      blocks: [
        "confinement-selection-intro",
      ],
      subsections: [
        section({
          title: "Operator selection by linear programming",
          label: "sec:confinement-selection-lp",
          blocks: [
            "confinement-lp",
            "confinement-nucleon-unit",
            "confinement-operator-selection",
            "confinement-operator-selection-proof",
            "confinement-operator-selection-interpretation",
            "confinement-operator-selection-table2-data",
            "confinement-operator-selection-table1-data",
            "confinement-frobenius-reciprocity",
            "confinement-frobenius-reciprocity-interpretation",
            "confinement-sdp-spectral-gap",
            "confinement-sdp-multi-operator",
          ],
        }),
        section({
          title: "Semidefinite selection and dual stability",
          label: "sec:confinement-selection-confinement-sdp-vs",
          blocks: [
            "confinement-selection-confinement-sdp-vs-intro",
            "confinement-sdp-vs-lp",
            "confinement-misdp",
            "confinement-topological",
            "confinement-topological-proof",
            "confinement-topological-interpretation",
            "lp-stable",
            "lp-confined",
            "lp-dual-stability",
            "lp-dual-stability-confinement-reading",
            "lp-dual-stability-table-data",
            "algebraic-primality",
            "n-equals-1-vacuous-magic",
            "n-equals-1-vacuous-magic-context",
            "n-equals-1-vacuous-magic-proof",
            "q-beta-cos-resummation",
            "q-beta-cos-resummation-comparison",
            "q-beta-cos-resummation-table-data",
          ],
        }),
      ],
    }),

    // ── §3. Nucleon–nucleon isospin, Wigner SU(4), and magic numbers ──
    section({
      title: "Isospin Selection, Wigner $SU(4)$ Supermultiplets, and the Interface Band",
      label: "sec:nn-isospin-interface",
      blocks: [
        "nn-isospin-interface-intro",
        "isospin-singlet-binds-more",
        "isospin-singlet-binds-more-two-nucleon-reading",
        "isospin-singlet-binds-more-proof",
        "content-keyed-interface-refuted",
        "markov-stabilisation-needs-a-fresh-generator",
        "binding-functional-is-the-log",
        "nucleon-pair-isospin-channel",
        "isospin-selection-class-inhabited",
        "branching-identity-isospin-weights",
        "interface-band-between-isospin-weights",
        "interface-never-realises-isospin-weight",
        "colour-tube-floor-overshoots-deuteron",
        "spin-from-so3-fiber",
        "wigner-su4-from-spin-isospin",
        "alpha-wigner-supermultiplet-context",
        "weinberg-angle-categorical",
      ],
    }),

    section({
      title: "Nuclear Binding Regimes and Magic Numbers",
      label: "sec:nuclear-binding",
      blocks: [
        "nuclear-binding-intro",
        "demand-profile",
        "demand-stability",
        "nuclear-operator-regimes",
        "nuclear-operator-regimes-interpretation",
        "periodic-table-demand-conjecture",
      ],
    }),

    section({
      title: "Derived Light-Atom Normal Forms",
      label: "sec:derived-atoms",
      blocks: [
        "derived-atoms-intro",
        "hydrogen-derived-nf",
        "hydrogen-derived-nf-table1-data",
        "hydrogen-derived-nf-table2-data",
        "helium4-derived-nf",
        "li6-derived-nf",
        "li6-derived-nf-table-data",
        "o16-derived-nf",
      ],
    }),

    // ── §4. Transfer matrices and beta-decay transitions ─────────
    section({
      title: "Typed Garside Element and Gram-Weighted $\\mathcal{Q}_q$-Value",
      label: "sec:garside-gram",
      blocks: [
        "garside-gram-intro",
        "typed-garside-element",
        "typed-garside-element-adjacent-comparison",
        "gram-weighted-qvalue",
        "gram-weight-eigenstructure",
      ],
    }),

    section({
      title: "Transfer Matrices and Beta-Decay Transitions",
      label: "sec:transfer-beta-decay",
      blocks: [
        "transfer-beta-decay-intro",
        "ground-state-ordering-table2-data",
        "ground-state-ordering-table1-data",
        "energy-scale-planck",
        "neutron-qvalue-symbolic",
        "qbeta-counit-closed-form",
        "qbeta-counit-transition",
        "qbeta-trace-counit-convergence",
        "delta-pre-archimedean",
        "transfer-beta-decay-q-beta-spectral-intro",
        "q-beta-spectral-bridge",
        "q-beta-spectral-bridge-proof",
        "archimedean-remainder-exponential-decay",
        "q-beta-spectral-bridge-table-data",
        "q-beta-form-a-n1-symbolic-table-data",
        "silver-ratio-beta-decay-null",
        "silver-ratio-beta-decay-null-interpretation",
        "beta-decay-interpretation",
        "nucleon-nf-observability",
        "beta-decay-energy-scale",
        "negative-debt-confinement",
        "beta-decay-braid-visualizer",
      ],
    }),

    // ── §5. Composite atomic braid and Wedderburn binding ────────
    section({
      title: "Composite Atomic Braid and Wedderburn Binding Foundations",
      label: "sec:atomic-braid-mass-foundations",
      blocks: [
        "atomic-braid-mass-intro",
        "atomic-lp-stability",
        "atomic-lp-stability-dressing",
        "universal-ilp-algorithm",
        "gram-matrix-h3-symbolic",
        "gram-matrix-h3-symbolic-eval-role",
        "color-pairing-binding",
        "atomic-nf-witness",
        "atomic-nf-witness-procedure",
        "step-lp-verification",
        "groebner-reduction-methods",
      ],
    }),

    section({
      title: "Atomic Braid Mass: Crossing-Graded Locality and CPT Closure",
      label: "sec:atomic-braid-mass-crossing-locality-cpt",
      blocks: [
        "atomic-braid-mass-crossing-locality-cpt-intro",
        "q-holonomy-locality-derivation",
        "cpt-orbit-closure-density",
        "cpt-d6-d7-d8-closure",
        "t-from-trace-cyclicity",
        "type-b-folding-cpt",
        "bar-involution-invariance",
        "bar-involution-invariance-proof",
        "bar-involution-invariance-significance",
        "soft-confinement-at-q0",
        "soft-confinement-at-q0-table-data",
      ],
    }),

    // ── §6. Branching Q-values and beta-stability closure ────────
    section({
      title: "Branching $Q$-Value Factorisation",
      label: "sec:branching-qvalue",
      blocks: [
        "branching-qvalue-intro",
        "per-nucleon-channel-decomposition",
        "spectator-normalization",
        "branching-qvalue-factorization",
        "branching-qvalue-factorization-proof",
        "parity-regime-selection",
        "parity-regime-selection-proof",
        "positron-correction",
        "tritium-qvalue-symbolic",
        "frobenius-positivity-filter",
        "frobenius-positivity-filter-context",
        "categorical-quantity-map",
        "b3-local-minimum",
      ],
    }),

    section({
      title: "Pair Production and Anyon Collapse",
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

    section({
      title: "Beta-Stability Closure",
      label: "sec:beta-stability-closure",
      blocks: [
        "intro-beta-stability-closure",
        "skein-binding-lagrangian",
        "skein-binding-lagrangian-derivation",
        "beta-stability",
        "beta-stability-interpretation",
      ],
    }),

    section({
      title: "Varying Euler Characteristic, Mirror Bundle, and Geometric Universality",
      label: "sec:varying-euler-mirror",
      blocks: [
        "varying-euler-intro",
        "genus-2-intro",
        "hyperelliptic-z5-classification",
        "hyperelliptic-z5-classification-proof",
        "hyperelliptic-z5-classification-interpretation",
        "bring-z5-descent",
        "x5-bring-prym-jacobian",
        "u1-phase-tube",
        "weight-identification-consequences",
        "descent-mirror-intro",
        "e-minus-one",
        "particle-interactions-orphan-reconnect-intro",
        "geom-universality",
        "q-zero-stokes-region-identification",
        "outro-particle-interactions",
      ],
    }),
  ],
});
