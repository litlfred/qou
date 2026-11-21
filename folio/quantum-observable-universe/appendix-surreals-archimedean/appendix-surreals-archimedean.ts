import { chapter } from "../../schema/builders";

/**
 * Archimedean lobe of the surreal-number appendix.
 *
 * Houses surreal-arithmetic content that is intrinsically pinned to
 * the substrate parameter q_0 (numerical evaluation, real-line
 * inequalities, archimedean / fixed-q_0 regime). The categorical
 * surreal-number theory (generic-R / symbolic regime, Conway normal
 * form, birthday grading, blow-up calculus) stays in the original
 * `appendix-surreals` chapter.
 *
 * Authoring history: split out 2026-06-01 from appendix-surreals per
 * q-usage audit Policy A (chapter refactor option). See
 * docs/audits/2026-06-01-q-usage-dispensation-plan.md §Policy A for
 * the rationale and the block-selection criteria.
 */
export default chapter({
  label: "app:surreals-archimedean",
  title: "Surreal-number lift at the substrate (archimedean appendix)",
  sections: [
    {
      title: "Substrate-pinned algebraic structure",
      label: "sec:surreals-archimedean-algebraic",
      blocks: [
        "algebraic-core-survives",
        "ecalle-borel-resummation",
        "analytic-obstructions",
        "analytic-obstructions-table1-data",
        "analytic-obstructions-table2-data",
        "ecalle-borel-resurgence-vocabulary",
        "habiro-tail-archimedean-action",
        "standard-part-functor",
        "st-is-median-resummation",
        "standard-part-classical-limit",
        "archimedean-functor-trace-commutativity",
      ],
    },
    {
      title: "Speculative reformulations at q_0",
      label: "sec:surreals-archimedean-speculative",
      blocks: [
        "diophantine-birthday",
        "diophantine-birthday-trajectory",
        "infinitesimal-frobenius",
        "surreal-limit-transfer",
      ],
    },
    {
      title: "Characteristic-p companion at substrate",
      label: "sec:surreals-archimedean-char-p",
      blocks: [
        "on-p-modular-hecke",
        "on-p-modular-hecke-table-data",
        "on-p-modular-hecke-significance",
      ],
    },
    {
      title: "Substrate-positivity and millennium bounds",
      label: "sec:surreals-archimedean-millennium",
      blocks: [
        "wenzl-positivity-implies-substrate-positivity",
        "collatz-hausdorff-comparison",
        "collatz-hausdorff-comparison-table-data",
      ],
    },
  ],
});
