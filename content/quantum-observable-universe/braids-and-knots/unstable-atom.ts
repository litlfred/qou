import { definition } from "../../schema/builders";

export default definition({
  label: "def:unstable-atom",
  title: "Unstable atom (ILP infeasibility)",
  lean: { ref: "qou:QOU.BraidKnot.UnstableAtom",
    validation: "not_checked",
  },
  cites: [],
  tags: [
    "instability",
    "decay",
    "ilp",
    "atom",
    "phase-boundary",
  ],
});
