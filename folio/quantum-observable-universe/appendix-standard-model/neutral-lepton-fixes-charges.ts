import { proposition } from "../../schema/builders";

/**
 * Owner ruling 2026-11-22: "Needs to derive the q_i". This block derives
 * every first-generation charge from one neutral lepton, on the given
 * matter content 5bar + Lambda^2 5 over 5 = colour + isospin. The matter
 * content itself is imported (Georgi-Glashow / Baez-Huerta), and the block
 * says so.
 */
export default proposition({
  label: "prop:neutral-lepton-fixes-charges",
  title: "One neutral lepton fixes every first-generation charge",
  uses: ["def:quantum-observable-universe"],
  cites: ["baez-huerta2010"],
  lean: {
    ref: "qou:QOU.EightfoldWay.NeutralLeptonFixesCharges.neutral_lepton_iff",
  },
  tags: ["appendix", "standard-model", "hypercharge", "charge-quantisation"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`NeutralLeptonFixesCharges.lean`). Conditional on the " +
        "matter content 5bar + Lambda^2 5, which is imported, not derived " +
        "(rem:su5-hypercharge-n3-gate). Bean qou-h0zz, epic qou-x08k.",
    },
  ],
});
