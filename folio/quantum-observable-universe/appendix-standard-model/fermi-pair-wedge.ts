import { proposition } from "../../schema/builders";

/**
 * Splits the matter-content input of prop:neutral-lepton-fixes-charges.
 * Fermi exchange on a strand pair forces the pair into Lambda^2 5; the
 * cubic Y0 trace pairs 5bar with Lambda^2 5 one to one. Both Fermi exchange
 * and anomaly cancellation are stated inputs.
 */
export default proposition({
  label: "prop:fermi-pair-wedge",
  title: "Fermi exchange puts a strand pair in the exterior square",
  uses: ["prop:neutral-lepton-fixes-charges"],
  lean: {
    ref: "qou:QOU.EightfoldWay.FermiPairWedge.fermi_ext",
  },
  tags: ["appendix", "standard-model", "hypercharge", "fermi-statistics"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`FermiPairWedge.lean`). Inputs stated: Fermi exchange, " +
        "one strand for 5bar and one strand pair for Lambda^2 5, and vanishing " +
        "cubic trace. Why matter has this strand count stays open. Bean qou-h0zz.",
    },
  ],
});
