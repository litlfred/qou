import { definition } from "../../schema/builders";

export default definition({
  label: "def:unstable-atom",
  title: "Unstable atom (failure of normal-form positivity)",
  lean: { ref: "qou:QOU.BraidKnot.UnstableAtom",
    validation: "not_checked",
  },
  cites: [],
  uses: [
    // Defined as the negation of this condition, so it carries no content of
    // its own until the reader has the positive case.
    "def:stable-atom",
  ],
  tags: [
    "instability",
    "decay",
    "ilp",
    "atom",
    "phase-boundary",
  ],
});
