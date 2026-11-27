import { proposition } from "../../schema/builders";

/**
 * Supplies the label that ChiralityIndependentOfCrossing (V9, bean qou-wqto)
 * leaves open: the strand slot of 5bar + Lambda^2 5, plus a dual flag,
 * separates the eight first-generation quark states and reproduces their
 * charges. The slot assignment is the Georgi-Glashow embedding, an input.
 */
export default proposition({
  label: "prop:strand-slot-separates-gen1",
  title: "The strand slot separates the first-generation quark states",
  uses: ["prop:fermi-pair-wedge"],
  cites: ["baez-huerta2010"],
  lean: {
    ref: "qou:QOU.EightfoldWay.StrandSlotSeparatesGen1.slot_dual_injective",
  },
  tags: ["appendix", "standard-model", "chirality", "charge-quantisation"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`StrandSlotSeparatesGen1.lean`). The slot assignment is " +
        "the Georgi-Glashow embedding, stated as a definition, not derived. " +
        "Closes the open label of V9 (bean qou-wqto) conditionally. Bean qou-h0zz.",
    },
  ],
});
