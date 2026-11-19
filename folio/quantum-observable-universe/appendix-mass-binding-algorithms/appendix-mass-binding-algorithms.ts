import { chapter, section } from "../../schema/builders";

/**
 * Appendix: Mass and Binding Algorithms.
 *
 * Self-contained mathematical specification of the symbolic, combinatorial,
 * convex-optimization, and arbitrary-precision numerical algorithms mapping
 * the categorical quantum observable universe (C, A, tau) and balancing twist
 * parameter q_0 to particle masses, electroweak and weak-decay observables,
 * and multi-scale nuclear binding energies.
 */
export default chapter({
  tabLabel: "MBA",
  title: "Mass and Binding Algorithms",
  label: "app:mass-binding-algorithms",
  sections: [
    section({
      title: "Scope and arithmetic conventions",
      label: "sec:mba-scope",
      blocks: [
        "mba-intro",
      ],
    }),
    section({
      title: "Canonical evaluation chain: summary map",
      label: "sec:mba-chain-map",
      blocks: [
        "mba-chain-map",
      ],
    }),
    section({
      title: "Canonical chain algorithms",
      label: "sec:mba-canonical-chain",
      blocks: [
        "mba-step01-categorical-action",
        "mba-step02-gs-reduction",
        "mba-step03-markov-trace",
        "mba-step04-bring-brane",
        "mba-step05-wedderburn",
        "mba-step06-frobenius-pairing",
        "mba-step07-gb-filtration",
        "mba-step08-jet-prefix",
        "mba-step09a-mass-identity",
        "mba-step09b-per-isotope-binding",
        "mba-step10-confinement-sdp",
        "mba-step11-q-beta-truncation",
      ],
    }),
    section({
      title: "Auxiliary structural algorithms and obstructions",
      label: "sec:mba-sidecars",
      blocks: [
        "mba-sidecar-delta-lambda-closure",
        "mba-remark-tjon-universality-external",
        "mba-sidecar-mirror-cancellation",
        "mba-sidecar-isovector-chiral-residue",
        "mba-sidecar-ck-truncation-ladder",
      ],
    }),
  ],
});
