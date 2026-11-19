import { chapter, section } from "../../schema/builders";

/**
 * Chapter 11: Nuclear Interactions and Binding.
 *
 * Computational engine: Gröbner–Shirshov reduction, LP/SDP optimization,
 * beta decay transfer matrices, atomic braid mass formulas, branching
 * Q-values. Consumes particle definitions from Ch 9 (Knots, Particles,
 * and Confinement).
 *
 * Split from the former particle-interactions chapter (Phase 1,
 * eightfold-way-chapter-2026-08-03).
 */
export default chapter({
  title: "Nuclear Interactions and Binding",
  label: "chap:nuclear-interactions",
  sections: [
    // ── §1. The Gröbner–Shirshov reduction engine ────────────────
    section({
      title: "The Gröbner–Shirshov reduction engine",
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
        // thm:markov-trace-factorization moved earlier to
        // braids-and-knots/sec:phi-q-markov-schur-weyl-tower per
        // detangler P31 (2026-05-22). Acceptance note: the move
        // emits 1 new H2 forward edge back to
        // prop:generator-volume-decomposition (this section),
        // accepted as wontfix:architectural per
        // docs/coordination/2026-05-19-detangler-architectural-acceptances.md §5.
      ],
    }),

    // ── §2. Confinement operator selection ────────────────────────
    section({
      title: "Confinement operator selection",
      label: "sec:confinement-selection",
      blocks: [
        "confinement-selection-intro",
      ],
      subsections: [
        section({
          title: "Operator selection by LP",
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
            // prop:confinement-sdp moved earlier to
            // braids-and-knots/sec:alpha-k-procedure per detangler P33.
            // New H2 → confinement-lp accepted §5.
            "confinement-sdp-spectral-gap",
            "confinement-sdp-multi-operator",
          ],
        }),
        section({
          title: "Which constraints survive",
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
            "algebraic-primality-remark",
            "n-equals-1-vacuous-magic",
            "n-equals-1-vacuous-magic-context",
            "n-equals-1-vacuous-magic-proof",
            // prop:operator-selection-lp moved earlier to
            // braids-and-knots/sec:hoefsmit-convergence-atomic per
            // detangler P28. New H2 → confinement-lp accepted §5.
            "q-beta-cos-resummation",
            "q-beta-cos-resummation-comparison",
            "q-beta-cos-resummation-table-data",
          ],
        }),
      ],
    }),

    // ── §3. Nuclear binding and magic numbers ────────────────────
    section({
      title: "Nuclear binding and magic numbers",
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

    // ── §3b. The NN channel: isospin selection and the interface band ──
    // Decision 7 homes all three nuclear Lean results here — isospin
    // selection, the band separation, the colour-tube floor — because they
    // are one connected argument and none of them had any exposition.
    // Reading order: select the channel → refute the alternative → define
    // the map → state the branching → measure the gap → close the
    // colour-tube route. Placement AFTER §3 is the least disruptive
    // insertion; siting it right after §2 sec:confinement-selection (also
    // operator selection, and upstream of §3's (Z,N) magic-number work) is
    // arguably the better read and is left as an owner call. Decision 4
    // forbids CHAPTER moves, not section ordering inside a chapter.
    section({
      title: "Isospin selection and the interface band",
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
        "nucleon-pair-isospin-channel-remark",
        "isospin-selection-class-inhabited",
        "branching-identity-isospin-weights",
        "interface-band-between-isospin-weights",
        "interface-never-realises-isospin-weight",
        "colour-tube-floor-overshoots-deuteron",
      ],
    }),

    // ── §4. Derived atom examples ────────────────────────────────
    section({
      title: "Derived atom examples",
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

    // ── §5. Typed Garside element and Gram-weighted Q-value ──────
    section({
      title: "Typed Garside element and Gram-weighted $\\\\mathcal{Q}_q$-value",
      label: "sec:garside-gram",
      blocks: [
        "garside-gram-intro",
        "typed-garside-element",
        "typed-garside-element-adjacent-comparison",
        "gram-weighted-qvalue",
        "gram-weight-eigenstructure",
      ],
    }),

    // ── §6. Transfer matrices and beta decay ─────────────────────
    section({
      title: "Transfer matrices and beta decay",
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
        // Merged from the former auto-split "Transfer matrices and beta
        // decay : vs" (small base, strongly-related continuation — the
        // spectral Q_beta route to the same observable; reorg policy:
        // strongly-related -> merge). The transition block below opens
        // the spectral-bridge half.
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

    // ── §7. Atomic braid and Wedderburn mass formula: foundations ─
    section({
      title: "Atomic braid and Wedderburn mass formula: foundations",
      label: "sec:atomic-braid-mass-foundations",
      blocks: [
        "atomic-braid-mass-intro",
        // def:atomic-braid moved earlier to
        // braids-and-knots/sec:skein-particle-generation per
        // detangler P32.
        "atomic-lp-stability",
        "atomic-lp-stability-dressing",
        // wedderburn-mass-formula is referenced from braids-and-knots.ts
        // (its canonical home as thm:wedderburn-mass-formula).
        "universal-ilp-algorithm",
        "universal-ilp-algorithm-example",
        "universal-ilp-algorithm-remark",
        "gram-matrix-h3-symbolic",
        "gram-matrix-h3-symbolic-eval-role",
        "color-pairing-binding",
        "atomic-nf-witness",
        "atomic-nf-witness-procedure",
        "step-lp-verification",
        "groebner-reduction-methods",
      ],
    }),

    // ── §8. Atomic braid mass: crossing-graded, locality, CPT ────
    section({
      title: "Atomic braid mass: crossing-graded, locality, CPT",
      label: "sec:atomic-braid-mass-crossing-locality-cpt",
      blocks: [
        "atomic-braid-mass-crossing-locality-cpt-intro",
        "q-holonomy-locality-derivation",
        "cpt-orbit-closure-density",
        "bar-involution-invariance",
        "bar-involution-invariance-proof",
        "bar-involution-invariance-significance",
        "soft-confinement-at-q0",
        "soft-confinement-at-q0-table-data",
      ],
    }),

    // ── §9. Branching Q-value derivation ─────────────────────────
    section({
      title: "Branching Q-value derivation",
      label: "sec:branching-qvalue",
      blocks: [
        "branching-qvalue-intro",
        "per-nucleon-channel-decomposition",
        "per-nucleon-channel-decomposition-example",
        "per-nucleon-channel-decomposition-remark",
        "spectator-normalization",
        "spectator-normalization-remark",
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

    // ── §10. Pair production and anyon collapse ───────────────────
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

    // ── §11. Beta stability closure ──────────────────────────────
    section({
      title: "Beta stability closure",
      label: "sec:beta-stability-closure",
      blocks: [
        "intro-beta-stability-closure",
        "skein-binding-lagrangian",
        "skein-binding-lagrangian-remark",
        "skein-binding-lagrangian-derivation",
        "beta-stability",
        "beta-stability-interpretation",
      ],
    }),

    // ── §12. Varying Euler characteristic and the mirror bundle ──
    section({
      title: "Varying Euler Characteristic and the Mirror Bundle",
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
      ],
    }),

    // ── §13. Reconnected computational blocks ────────────────────
    // Non-definitional blocks from the former orphan-reconnect section.
    // Symmetry identifications (CPT, spin, Weinberg angle, Wigner
    // supermultiplet) that consume particle definitions from Ch 9.
    section({
      title: "Symmetry identifications and geometric universality",
      label: "sec:symmetry-identifications",
      blocks: [
        "particle-interactions-orphan-reconnect-intro",
        "geom-universality",
        "q-zero-stokes-region-identification",
        "cpt-d6-d7-d8-closure",
        "t-from-trace-cyclicity",
        "spin-from-so3-fiber",
        "type-b-folding-cpt",
        "weinberg-angle-categorical",
        "wigner-su4-from-spin-isospin",
        "alpha-wigner-supermultiplet-context",
        "outro-particle-interactions",
      ],
    }),
  ],
});
