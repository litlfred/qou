import { proposition } from "../../schema/builders";

/**
 * Removes the Georgi-Glashow slot assignment as an input: the four quark slots
 * are the four shapes of even subsets meeting colour once or twice, and the
 * Standard Model charges force the assignment. The dual flag (chirality sign)
 * stays an input.
 */
export default proposition({
  label: "prop:slot-from-even-shape",
  title: "The quark slot is the shape of an even strand subset",
  uses: ["prop:even-strand-generation", "prop:strand-slot-separates-gen1"],
  cites: ["baez-huerta2010"],
  lean: {
    ref: "qou:QOU.EightfoldWay.SlotFromEvenShape.slot_forced",
  },
  tags: ["appendix", "standard-model", "chirality", "charge-quantisation"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "Sorry-free (`SlotFromEvenShape.lean`). Derives the slot map of " +
        "`prop:strand-slot-separates-gen1` from the even part. Input left: the " +
        "dual flag, i.e. the chirality sign. Bean qou-h0zz.",
    },
  ],
});
