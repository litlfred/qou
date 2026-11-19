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
      blocks: [
        "sm-gauge-truncation",
        "sm-hypercharge-invariant",
        "strand-twist-datum",
        "strand-twist-datum-remark",
        "sm-colour-stabilizer-action",
        // The SU(5) scope note. Placed after both blocks it uses
        // (truncation, hypercharge) so its uses[] edges run backward.
        "su5-hypercharge-n3-gate",
        "cal2-higgs-knot-coupling",
        "a5-orbital-degeneracy-fracture",
      ],
    }),
    section({
      title: "The 26 parameters of the Standard Model",
      label: "sec:sm-parameters",
      blocks: ["sm-params-intro"],
    }),
    section({
      title: "Charged-lepton masses (3)",
      label: "sec:sm-params-leptons",
      blocks: ["sm-params-lepton-masses"],
    }),
    section({
      title: "Quark masses (6)",
      label: "sec:sm-params-quarks",
      blocks: ["sm-params-quark-masses"],
    }),
    section({
      title: "Quark mixing (4)",
      label: "sec:sm-params-ckm",
      blocks: ["sm-params-ckm"],
    }),
    section({
      title: "Gauge couplings (3)",
      label: "sec:sm-params-gauge-couplings",
      blocks: ["sm-params-gauge-couplings"],
    }),
    section({
      title: "Higgs sector (2)",
      label: "sec:sm-params-higgs",
      blocks: ["sm-params-higgs"],
    }),
    section({
      title: "The strong-CP angle (1)",
      label: "sec:sm-params-theta",
      blocks: ["sm-params-theta-qcd"],
    }),
    section({
      title: "Neutrino sector (7)",
      label: "sec:sm-params-neutrinos",
      blocks: ["sm-params-neutrino"],
    }),
    section({
      title: "The results surface and what gates the rest",
      label: "sec:sm-results-surface",
      blocks: ["sm-results-index", "sm-gating-objects"],
    }),
    section({
      title: "Open problems",
      label: "sec:sm-open-problems",
      blocks: ["sm-open-problems"],
    }),
  ],
});
