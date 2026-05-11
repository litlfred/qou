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
        "markov-trace-factorization",
      ],
    }),

    // ── §2. Confinement operator selection ────────────────────────
    section({
      title: "Confinement operator selection",
      label: "sec:confinement-selection",
      blocks: [
        "algebraic-primality",
        "algebraic-primality-equals-empirical-at-q0",
        "confinement-lp",
        "confinement-nucleon-unit",
        "confinement-operator-selection",
        "confinement-frobenius-reciprocity",
        "confinement-sdp",
        "confinement-sdp-spectral-gap",
        "confinement-sdp-multi-operator",
        "confinement-sdp-vs-lp",
        "confinement-misdp",
        "confinement-topological",
        "lp-dual-stability",
        "n-equals-1-vacuous-magic",
        "operator-selection-lp",
      ],
    }),

    // ── §3. Nucleon derivation from pair production ──────────────
    section({
      title: "Nucleon derivation from pair production",
      label: "sec:nucleon-derivation",
      blocks: [
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
        "skein-polynomial-transfer-matrix",
        "transfer-matrix-operator",
        "beta-decay-transfer-matrix",
        "ground-state-ordering",
        "transfer-matrix-identities",
        "neutron-qvalue-symbolic",
        "q-beta-spectral-bridge",
        "beta-decay-interpretation",
        "nucleon-nf-observability",
        "beta-decay-energy-scale",
        "negative-debt-confinement",
        "beta-decay-braid-visualizer",
      ],
    }),
    // ── §8. Atomic braid and Wedderburn mass formula ───────────
    section({
      title: "Atomic braid and Wedderburn mass formula",
      label: "sec:atomic-braid-mass",
      blocks: [
        "atomic-braid",
        "atomic-lp-stability",
        // wedderburn-mass-formula is referenced from braids-and-knots.ts
        // (its canonical home as thm:wedderburn-mass-formula). Listing
        // it here too caused a multiply-defined label because the
        // pipeline keys block records by rootName.
        "q-integer-mass-formula",
        "universal-ilp-algorithm",
        "neutron-proton-splitting",
        "color-pairing-binding",
        "mass-table-z1-20",
        "atomic-nf-witness",
        "step-lp-verification",
        "groebner-reduction-methods",
        "tower-binding-energy",
        "bw-categorical-descent",
        "thurston-volume-additivity",
        "mass-volume-factorization",
        "crossing-graded-mass-expansion",
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
      ],
    }),
  ],
});
