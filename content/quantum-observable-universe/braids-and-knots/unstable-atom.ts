import { definition } from "../../schema/builders";

export default definition({
  label: "def:unstable-atom",
  title: "Unstable atom (ILP infeasibility)",
  lean: {
    decl: "QOU.BraidKnot.UnstableAtom",
    validation: "not_checked",
  },
  uses: [
    "def:stable-atom",
    "def:atom-knot",
    "def:knot-operator-energy",
  ],
  cites: [],
  tags: [
    "instability",
    "decay",
    "ilp",
    "atom",
    "phase-boundary",
  ],
});
