import { chapter, section } from "../../schema/builders";

/**
 * Appendix: Mass and Binding Algorithms.
 *
 * Self-contained bridge between the categorical derivation chain
 * (`prose:pre-archimedean-derivation-chain`) and the executable
 * compute layer (`qou-mass`, `pyhecke`, `pyhecke-native`,
 * `qou-substrate`, `hecke-engine`).
 *
 * Each algorithm block names:
 *  - the step in the substrate → observable chain it realises,
 *  - the propositions that justify it,
 *  - the canonical Python API entry point (and the witness JSON
 *    written for cross-language reproducibility),
 *  - the precision regime under which the result is valid (L1 vs L2,
 *    1ppQ compute vs ≤ σ_exp/100 per-observable).
 *
 * Sidecar algorithms (Δ_λ closure ansätze, c_k truncation ladder,
 * LP/SDP dual emission, witness-JSON pipeline) appear after the 11
 * canonical chain steps.
 */
export default chapter({
  tabLabel: "MBA",
  title: "Mass and Binding Algorithms",
  label: "app:mass-binding-algorithms",
  sections: [
    section({
      title: "Scope and conventions",
      label: "sec:mba-scope",
      blocks: [
        "mba-intro",
      ],
    }),
    section({
      title: "From propositions to compute — the chain map",
      label: "sec:mba-chain-map",
      blocks: [
        "mba-chain-map",
      ],
    }),
    section({
      title: "Canonical chain — algorithms",
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
      title: "Sidecar algorithms",
      label: "sec:mba-sidecars",
      blocks: [
        "mba-sidecar-delta-lambda-closure",
        "mba-remark-tjon-universality-external",
        "mba-sidecar-mirror-cancellation",
        "mba-sidecar-isovector-chiral-residue",
        "mba-sidecar-ck-truncation-ladder",
        "mba-sidecar-lp-sdp-dual-emission",
        "mba-sidecar-witness-json-pipeline",
      ],
    }),
  ],
});
