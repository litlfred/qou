import { chapter, section } from "../../schema/builders";

/**
 * Chapter 11: Particle Interactions and Nuclear Structure.
 *
 * Derives particle binding, nuclear structure, and atomic construction
 * from the Gröbner–Shirshov reduction engine and LP optimization.
 * Separates the HOW (interactions, binding, decay) from the WHAT
 * (particle definitions in Ch 10).
 *
 * Derivations are symbolic in q; witness evaluations at q₀ provide
 * numerical verification.
 */
export default chapter({
  title: "Particle Interactions and Nuclear Structure",
  label: "chap:particle-interactions",
  sections: [
    // ── §1. The Gröbner–Shirshov reduction engine ────────────────
    section({
      title: "The Gröbner–Shirshov reduction engine",
      label: "sec:groebner-engine",
      blocks: [
        "particle-interactions-intro",
        "nuclear-groebner-reduction",
        "nuclear-reduction-algorithm",
        "groebner-shirshov-energy",
        "inductive-gb-reduction",
        "inductive-gb-reduction-proof",
        "nucleon-ordering-factorization",
        "nucleon-ordering-factorization-proof",
        "box-braid-irreducibility",
        "generator-volume-decomposition",
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
      // Structural reorg (docs/structural-framework.md): the section's
      // own LP/SDP machinery + the chapter-restructure auto-split
      // "Confinement operator selection : vs" become two subsections
      // (P2 needs >= 2 — a lone subsection is flagged). Block reading
      // order is preserved, so the detangler forward-ref check is
      // unaffected (P6).
      subsections: [
        section({
          title: "Operator selection by LP",
          label: "sec:confinement-selection-lp",
          blocks: [
            "confinement-lp",
            "confinement-nucleon-unit",
            "confinement-operator-selection",
            "confinement-operator-selection-table2-data",
            "confinement-operator-selection-table1-data",
            "confinement-frobenius-reciprocity",
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
            "lp-dual-stability",
            "lp-dual-stability-table-data",
            "algebraic-primality",
            "n-equals-1-vacuous-magic",
            "n-equals-1-vacuous-magic-proof",
            // prop:operator-selection-lp moved earlier to
            // braids-and-knots/sec:hoefsmit-convergence-atomic per
            // detangler P28. New H2 → confinement-lp accepted §5.
            // Absorbed from former Ch `encounter`: SDP-as-thimble-flow
            // interprets `prop:operator-selection-lp` (now in
            // braids-and-knots).
            "q-beta-cos-resummation",
            "q-beta-cos-resummation-table-data",
          ],
        }),
      ],
    }),

    // ── §3. Nucleon derivation from pair production ──────────────
    section({
      title: "Nucleon derivation from pair production",
      label: "sec:nucleon-derivation",
      blocks: [
        "nucleon-derivation-intro",
        // Quark sector re-homed from predicted-spectra (Ch13) per the
        // cross-chapter triage (author decision: quarks before protons) —
        // nucleons are built from quarks, so the quark defs are prior.
        "up-quark",
        "up-quark-properties",
        "down-quark",
        "down-quark-properties",
        "quark-antiquark-production",
        "four-term-pair-nucleon",

        "four-term-pair-nucleon-table1-data",
        "four-term-pair-nucleon-table2-data",
        "four-term-pair-nucleon-table3-data",
        "confinement-universality",
        "confinement-universality-proof",
        "derived-atom",
        "nucleon-from-photons-summary",
      ],
    }),

    // ── §4. Nuclear binding and magic numbers ────────────────────
    section({
      title: "Nuclear binding and magic numbers",
      label: "sec:nuclear-binding",
      blocks: [
        "nuclear-binding-intro",
        "nuclear-operator-regimes",
        "demand-stability",
        "periodic-table-demand-conjecture",
      ],
    }),

    // ── §5. Derived atom examples ────────────────────────────────
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

    // ── §6. Typed Garside element and Gram-weighted Q-value ───────
    section({
      title: "Typed Garside element and Gram-weighted $\\mathcal{Q}_q$-value",
      label: "sec:garside-gram",
      blocks: [
        "garside-gram-intro",
        "typed-garside-element",
        "gram-weighted-qvalue",
        "gram-weight-eigenstructure",
      ],
    }),

    // ── §7. Transfer matrices and beta decay ─────────────────────
    section({
      title: "Transfer matrices and beta decay",
      label: "sec:transfer-beta-decay",
      blocks: [
        "transfer-beta-decay-intro",
        "ground-state-ordering-table2-data",
        "ground-state-ordering-table1-data",
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
        "q-beta-spectral-bridge-table-data",
        "q-beta-form-a-n1-symbolic-table-data",
        "silver-ratio-beta-decay-null",
        "silver-ratio-beta-decay-null-proof",
        "beta-decay-interpretation",
        "nucleon-nf-observability",
        "beta-decay-energy-scale",
        "negative-debt-confinement",
        "beta-decay-braid-visualizer",
      ],
    }),
    // ── §8. Atomic braid and Wedderburn mass formula ───────────
    // Detangler P16 split (2026-05-23): 21-block sec:atomic-braid-mass
    // split into LP/mass-formula foundations + crossing-locality-CPT.
    section({
      title: "Atomic braid and Wedderburn mass formula: foundations",
      label: "sec:atomic-braid-mass-foundations",
      blocks: [
        "atomic-braid-mass-intro",
        // def:atomic-braid moved earlier to
        // braids-and-knots/sec:skein-particle-generation per
        // detangler P32.
        "atomic-lp-stability",
        // wedderburn-mass-formula is referenced from braids-and-knots.ts
        // (its canonical home as thm:wedderburn-mass-formula).
        "universal-ilp-algorithm",
        "gram-matrix-h3-symbolic",
        "color-pairing-binding",
        "atomic-nf-witness",
        "step-lp-verification",
        "groebner-reduction-methods",
        // Detangler R3 (2026-05-23): 7-row Z=1-20 binding-energy
        // predictions extracted from tower-binding-energy.md.
      ],
    }),
    section({
      title: "Atomic braid mass: crossing-graded, locality, CPT",
      label: "sec:atomic-braid-mass-crossing-locality-cpt",
      blocks: [
        "atomic-braid-mass-crossing-locality-cpt-intro",
        "q-holonomy-locality-derivation",
        "cpt-orbit-closure-density",
        "bar-involution-invariance",
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
        "spectator-normalization",
        "branching-qvalue-factorization",
        "branching-qvalue-factorization-proof",
        "parity-regime-selection",
        "parity-regime-selection-proof",
        "positron-correction",
        "tritium-qvalue-symbolic",
        "tritium-qvalue-symbolic-proof",
        "frobenius-positivity-filter",
        "categorical-quantity-map",
        "b3-local-minimum",
      ],
    }),
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
    section({
      title: "Skein Generation and Particle Correspondence",
      label: "sec:skein-particle-generation",
      blocks: [
        "skein-particle-generation-intro",
        "atomic-braid",
        "atomic-braid-table1-data",
        "knot-particle-generation",
        "knot-particle-generation-table-data",
        // Merged from the former auto-split "Skein Generation and
        // Particle Correspondence : generation" (small base,
        // strongly-related continuation — the knot-particle dictionary;
        // reorg policy: strongly-related -> merge).
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
    section({
      title: "Borromean Baryons and Reidemeister Invariance",
      label: "sec:borromean-reidemeister",
      blocks: [
        "borromean-reidemeister-intro",
        "borromean-baryon",
        "borromean-topological-confinement",
        "brunnian-property-of-borromean",
        "delta-skein-substrate-identity",
        "figure-8-muon-mass-cross-check",
        "typed-crossing-operator",
        "nucleon-hecke-element",
        "hadron-proton-example",
        "fermion-boson-knot-link",
        "fermion-boson-knot-link-table-data",
        "shell-transition-knot",
        "shell-transition-knot-table1-data",
        "shell-transition-knot-table2-data",
        "shell-transition-knot-table3-data",
        "shell-transition-knot-interpretation",
      ],
    }),
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
    section({
      title: "Lepton–meson structural parallel",
      label: "sec:lepton-meson-structural-parallel",
      blocks: [
        "lepton-meson-parallel",
        "lepton-meson-torus-knot-dictionary",
        "lepton-meson-torus-knot-dictionary-proof",
        "c-equals-bar-iff-all-1dim",
        "c-equals-bar-iff-all-1dim-proof",
      ],
    }),
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
    section({
      title: "Magic shells and the $\\\\kappa$ coupling",
      label: "sec:magic-shells",
      blocks: [
        "intro-magic-shells",
        "ilp-solution-count-unwrap",
        "shell-schur-weyl-self-duality",
        "shell-schur-weyl-self-duality-proof",
        "compound-beta-shell-calibration",
        "compound-beta-shell-calibration-table3-data",
        "compound-beta-shell-calibration-table2-data",
        "compound-beta-shell-calibration-table1-data",
        "magic-shell-coupling-kappa",
        "magic-shell-coupling-kappa-table-data",
        "quantum-dilogarithm-disambiguation",
      ],
    }),
    section({
      title: "Beta stability closure",
      label: "sec:beta-stability-closure",
      blocks: [
        "intro-beta-stability-closure",
        "energy-scale-planck",
        "skein-binding-lagrangian",
        "beta-stability",
        "beta-stability-interpretation",
      ],
    }),
    section({
      title: "Varying Euler Characteristic and the Mirror Bundle",
      label: "sec:varying-euler-mirror",
      blocks: [
        "varying-euler-intro",
        "genus-2-intro",
        "hyperelliptic-z5-classification",
        "bring-z5-descent",
        "x5-bring-prym-jacobian",
        "weight-identification-consequences",
        "u1-phase-tube",
        "descent-mirror-intro",
        "e-minus-one",
      ],
    }),
    section({
      title: "Reconnected orphan blocks (Phase 7)",
      label: "sec:particle-interactions-orphan-reconnect",
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
        "categorical-proton",
        "categorical-neutron",
        "categorical-meson",
        "outro-particle-interactions",
      ],
    }),
  ],
});
