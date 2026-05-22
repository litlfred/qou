import { definition } from "../../schema/builders";

export default definition({
  label: "def:stable-atom",
  title: "Stable atom (ILP feasibility)",
  lean: { ref: "qou:QOU.BraidKnot.StableAtom",
    validation: "not_checked",
  },
  uses: [
    "def:atom-knot",
    "prop:mass-tower-operator-valued",
  ],
  cites: [],
  tags: [
    "stability",
    "ilp",
    "lp-dual",
    "atom",
    "frobenius-positivity",
  ],
});
