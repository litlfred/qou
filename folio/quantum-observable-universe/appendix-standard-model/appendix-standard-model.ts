import { chapter, section } from "../../schema/builders";

/**
 * Annex C: Standard Model Parameter and Categorical Gauge Ledger.
 *
 * Assembles the route from categorical gauge action groupoids to the Standard
 * Model gauge sector and the 26-parameter epistemic status ledger, cross-linked
 * with Annex A Master Reference Tables A.1–A.2.
 */
export default chapter({
  tabLabel: "C",
  title: "Standard Model Parameter and Categorical Gauge Ledger",
  label: "app:standard-model",
  sections: [
    section({
      title: "Scope and categorical gauge symmetry",
      label: "sec:sm-gauge-symmetry",
      blocks: [
        "sm-intro",
        "gauge-action-groupoid",
        "sm-lagrangian-selection-rules",
      ],
    }),
    section({
      title: "Hecke realization and hypercharge invariant",
      label: "sec:sm-hecke-realization",
      blocks: [
        "gauge-hecke-realization",
        "sm-gauge-truncation",
        "sm-hypercharge-invariant",
      ],
    }),
    section({
      title: "Archimedean truncation and colour--orbital gates",
      label: "sec:sm-truncation",
      blocks: [
        "strand-twist-datum",
        "strand-twist-datum-remark",
        "sm-colour-stabilizer-action",
        "su5-hypercharge-n3-gate",
        "neutral-lepton-fixes-charges",
        "fermi-pair-wedge",
        "cal2-higgs-knot-coupling",
        "a5-orbital-degeneracy-fracture",
      ],
    }),
    section({
      title: "The 26 parameters of the Standard Model",
      label: "sec:sm-parameters",
      blocks: [
        "sm-params-intro",
        "sm-params-lepton-masses",
        "sm-params-quark-masses",
        "sm-params-ckm",
        "sm-params-gauge-couplings",
        "sm-params-higgs",
        "sm-params-theta-qcd",
        "sm-params-neutrino",
      ],
    }),
    section({
      title: "Results surface, gating objects, and open problems",
      label: "sec:sm-open-problems",
      blocks: [
        "sm-results-index",
        "sm-gating-objects",
        "sm-open-problems",
      ],
    }),
  ],
});
