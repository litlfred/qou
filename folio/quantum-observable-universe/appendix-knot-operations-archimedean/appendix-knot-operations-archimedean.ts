import { chapter, section } from "../../schema/builders";

/**
 * Archimedean lobe of the Knot Operation Actions appendix.
 *
 * Houses substrate-q_0-pinned numeric content: particle normal-form
 * tables evaluated at the substrate parameter, and the gluon-model
 * comparison table with experimental Q-value benchmarks. The
 * categorical Hecke operations + knot-operator basis content stays
 * in `appendix-knot-operations` (sibling, generic-R / symbolic).
 *
 * Authoring history: split out 2026-06-02 from
 * `appendix-knot-operations` per q-usage audit Policy A (the two
 * blocks are heavy-numeric and were repeatedly flagged
 * `q-usage-fixed-q0-leak` + `q-usage-archimedean-in-categorical-chapter`
 * — Policy C/2 minimal-strip is not appropriate here because the
 * numeric tables ARE the content). See PR #1640 §Policy A for the
 * chapter-refactor rationale and PR #1656 for the precedent.
 */
export default chapter({
  tabLabel: "K′",
  title: "Knot Operations Dictionary — archimedean evaluations at the aether parameter",
  label: "app:knot-operations-archimedean",
  sections: [
    section({
      title: "Particle normal forms at the aether parameter",
      label: "sec:knot-ops-archi-particle-nf",
      blocks: [
        "particle-nf-table",
        "particle-nf-table-table-data",
      ],
    }),
    section({
      title: "Gluon-model comparison vs experimental Q-values",
      label: "sec:knot-ops-archi-gluon-model",
      blocks: [
        "gluon-model-comparison",
      ],
    }),
  ],
});
