import { chapter, section } from "../../schema/builders";

/**
 * Chapter 18 — Stochastic Mechanics.
 *
 * The Markov trace $\mathrm{tr}_M$ that packages braid-word combinatorics
 * also admits an interpretation as a transition kernel of a stochastic
 * dynamics on the categorical state space. This chapter develops the
 * Nelson-style stochastic mechanics that emerges from the Markov trace,
 * including Itô / Fokker-Planck representations, diffusion processes on
 * the brane, and the classical limit recovering Brownian motion.
 *
 * Part IV chapter (Dynamics, Information, and Emergence). Consolidates
 * ~250 blocks of Markov / stochastic content currently scattered across
 * braids-and-knots and other chapters.
 *
 * Phase 6 scaffold (2026-05-25): chapter directory + manifest exist but
 * blocks not yet migrated.
 */
export default chapter({
  title: "Stochastic Mechanics",
  label: "chap:stochastic-mechanics",
  sections: [
    section({
      title: "Introduction",
      label: "sec:stochastic-mechanics-intro",
      blocks: ["intro"],
    }),
    section({
      title: "Markov axioms and braid-link enumeration",
      label: "sec:markov-axioms-braid-link",
      blocks: [
        "intro-markov-axioms-braid-link",
        "q-beta-categorical-precision-ladder-table1-data",
        "q-beta-categorical-precision-ladder-table2-data",
        "q-beta-categorical-precision-ladder-table3-data",
        "bar-involution-table1-data",
        "bar-involution-table2-data",
        "bar-involution-table3-data",
        "bar-involution-table4-data",
        "bar-involution-table5-data",
        "bar-involution-table6-data",
        "bar-involution-table7-data",
        "bar-involution-table8-data",
        "polynomial-bar-involution",
        // Merged from the former auto-split "... : generation" [4] — an
        // over-split that cut polynomial-bar-involution-table-data off
        // its own block (polynomial-bar-involution). Small,
        // strongly-related continuation -> merge (13+4=17, in band).
        "markov-axioms-braid-link-li2q-phiq-bar-intro",
        "polynomial-bar-involution-table-data",
        "c5-involution-leibniz-decomposition",
        "c5-involution-leibniz-decomposition-proof",
        "braid-group-n-strand-table3-data",
      ],
    }),
    section({
      title: "The Markov closure map and $c_k$ extraction",
      label: "sec:markov-axioms-braid-link-markov-closure-map",
      blocks: [
        "markov-axioms-braid-link-markov-closure-map-intro",
        "braid-group-n-strand-table2-data",
        "braid-group-n-strand-table1-data",
        "markov-closure-map-axiomatic",
        "F3-eps6-leading-eq-neg-2b-cubed",
        "q-beta-gamma-gamma-canonical-derivation",
        "ck-extraction-from-algebraic-rules-table2-data",
        "ck-extraction-from-algebraic-rules-table1-data",
      ],
    }),
    section({
      title: "Classical limit: construction",
      label: "sec:classical-limit-construction",
      blocks: [
        "classical-limit-intro",
        "classical-limit-functor",
        "quantum-gap-collapse",
        "classical-limit-obstruction",
        "qou-obstruction-reduction",
        "qou-obstruction-reduction-table4-data",
        "qou-obstruction-reduction-table3-data",
        "qou-obstruction-reduction-table2-data",
        "qou-obstruction-reduction-table1-data",
        "surreal-notation-cheat-sheet",
        "surreal-notation-cheat-sheet-table-data",
        "reeb-epsilon",
        "q-from-epsilon",
        "joint-galois-braid-figure-8-verified",
        "joint-galois-braid-figure-8-verified-proof",
        "joint-galois-braid-discharged",
        "joint-galois-braid-discharged-proof",
      ],
    }),
    section({
      title: "Classical limit: implications",
      label: "sec:classical-limit-implications",
      blocks: [
        "classical-limit-implications-intro",
        "graded-baer-star-Hq",
        "two-filtration-bridge-small-cases",
        "two-filtration-bridge-small-cases-table-data",
        "two-filtration-bridge-general-table-data",
        "classical-riemann-zeta",
        "classical-riemann-hypothesis",
        "macroscopic-stability-equivalence",
        "adelic-reeb-restricted-product",
        "adelic-reeb-restricted-product-proof",
        "adelic-tate-squeeze",
        "outro-braids-and-knots",
      ],
    }),
    section({
      title: "Reconnected orphan blocks (Phase 7)",
      label: "sec:stochastic-mechanics-orphan-reconnect",
      blocks: [
        "stochastic-mechanics-orphan-reconnect-intro",
        "lusztig-canonical-basis-q-eq-1",
        "phi-q-aj-machinery-identification",
        "reverse-limit-q-to-infinity",
        "outro-stochastic-mechanics",
      ],
    }),
  ],
});
