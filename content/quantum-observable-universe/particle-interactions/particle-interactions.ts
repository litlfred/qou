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
        "nucleon-ordering-factorization",
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
        "algebraic-primality",
        "algebraic-primality-equals-empirical-at-q0",
        "confinement-lp",
        "confinement-nucleon-unit",
        "confinement-operator-selection",
        "confinement-frobenius-reciprocity",
        // prop:confinement-sdp moved earlier to
        // braids-and-knots/sec:alpha-k-procedure per detangler P33.
        // New H2 → confinement-lp accepted §5.
        "confinement-sdp-spectral-gap",
        "confinement-sdp-multi-operator",
        "confinement-sdp-vs-lp",
        "confinement-misdp",
        "confinement-topological",
        "lp-dual-stability",
        "n-equals-1-vacuous-magic",
        // prop:operator-selection-lp moved earlier to
        // braids-and-knots/sec:hoefsmit-convergence-atomic per
        // detangler P28. New H2 → confinement-lp accepted §5.
        // Absorbed from former Ch `encounter`: SDP-as-thimble-flow
        // interprets `prop:operator-selection-lp` (now in
        // braids-and-knots).
        "sdp-as-thimble-flow",
        "q-beta-cos-resummation",
      ],
    }),

    // ── §3. Nucleon derivation from pair production ──────────────
    section({
      title: "Nucleon derivation from pair production",
      label: "sec:nucleon-derivation",
      blocks: [
        "nucleon-derivation-intro",
        "four-term-pair-nucleon",
        "confinement-universality",
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
        "deuterium-derived-nf",
        "deuterium-derived-binding",
        "helium4-derived-nf",
        "li6-derived-nf",
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
        "skein-polynomial-transfer-matrix",
        "transfer-matrix-operator",
        "beta-decay-transfer-matrix",
        "ground-state-ordering",
        "transfer-matrix-identities",
        "neutron-qvalue-symbolic",
        "q-beta-spectral-bridge",
        "q-beta-form-a-n1-symbolic",
        "silver-ratio-beta-decay-null",
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
        "q-integer-mass-formula",
        "universal-ilp-algorithm",
        "neutron-proton-splitting",
        "color-pairing-binding",
        "mass-table-z1-20",
        "mass-table-z1-20-table-data",
        "atomic-nf-witness",
        "step-lp-verification",
        "groebner-reduction-methods",
        "tower-binding-energy",
        // Detangler R3 (2026-05-23): 7-row Z=1-20 binding-energy
        // predictions extracted from tower-binding-energy.md.
        "tower-binding-energy-table-data",
        "mass-categorical-descent",
      ],
    }),
    section({
      title: "Atomic braid mass: crossing-graded, locality, CPT",
      label: "sec:atomic-braid-mass-crossing-locality-cpt",
      blocks: [
        "atomic-braid-mass-crossing-locality-cpt-intro",
        "thurston-volume-additivity",
        "mass-volume-factorization",
        "crossing-graded-mass-expansion",
        "crossing-graded-mass-expansion-table-data",
        "lifted-crossing-locality",
        "q-holonomy-locality-derivation",
        "frobenius-packing-density",
        "cpt-orbit-closure-density",
        "bar-involution-invariance",
        "soft-confinement-at-q0",
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
        "parity-regime-selection",
        "corrected-markov-trace",
        "mass-ordering-corrected",
        "positron-correction",
        "tritium-qvalue-symbolic",
        "frobenius-positivity-filter",
        "categorical-quantity-map",
        "b3-local-minimum",
        "outro-particle-interactions",
      ],
    }),
  ],
});
