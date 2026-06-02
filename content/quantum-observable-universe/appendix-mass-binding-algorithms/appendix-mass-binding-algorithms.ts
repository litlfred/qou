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
        // Step 3 — Markov trace (template / first block).
        // Steps 1, 2, 4–11 land in subsequent commits.
        "mba-step03-markov-trace",
      ],
    }),
  ],
});
