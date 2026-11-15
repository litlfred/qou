import { definition } from "../../schema/builders";

export default definition({
  label: "def:stable-atom",
  title: "Stable atom (Frobenius positivity of the normal form)",
  lean: { ref: "qou:QOU.BraidKnot.StableAtom",
    validation: "not_checked",
  },
  uses: [
    "def:atom-knot",
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
