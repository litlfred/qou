import { chapter, section } from "../../schema/builders";

/**
 * Appendix: Toward the Standard Model.
 *
 * Assembles the framework's route from the categorical gauge
 * symmetry of extended (knotted) objects to the Standard Model
 * gauge sector, with per-claim epistemic tiers:
 *
 *  - gauge symmetry as an action groupoid of topological states
 *    (definition + proved basic lemmas, Lean sorry-free);
 *  - its conjectured faithful realization in the Hecke algebra;
 *  - the conjectured archimedean truncation containing
 *    SU(3) x SU(2) x U(1);
 *  - the action functional as selection rule (interpretive remark);
 *  - an honest open-problems ledger closing the appendix.
 *
 * Nothing in this appendix is wired into the compute layer; the
 * conjecture classes carry no instances (open state, AGENTS.md
 * §3b-tax).
 */
export default chapter({
  tabLabel: "SM",
  title: "Toward the Standard Model",
  label: "app:standard-model",
  sections: [
    section({
      title: "Scope and epistemic status",
      label: "sec:sm-scope",
      blocks: ["sm-intro"],
    }),
    section({
      title: "The categorical gauge symmetry",
      label: "sec:sm-gauge-symmetry",
      blocks: ["gauge-action-groupoid", "sm-lagrangian-selection-rules"],
    }),
    section({
      title: "Hecke realization",
      label: "sec:sm-hecke-realization",
      blocks: ["gauge-hecke-realization"],
    }),
    section({
      title: "Archimedean truncation to the Standard Model group",
      label: "sec:sm-truncation",
      blocks: ["sm-gauge-truncation"],
    }),
    section({
      title: "Open problems",
      label: "sec:sm-open-problems",
      blocks: ["sm-open-problems"],
    }),
  ],
});
