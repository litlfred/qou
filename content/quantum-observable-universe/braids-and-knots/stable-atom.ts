import { definition } from "../../schema/builders";

export default definition({
  label: "def:stable-atom",
  title: "Stable atom (ILP feasibility)",
  lean: { ref: "qou:QOU.BraidKnot.StableAtom",
    validation: "not_checked",
  },
  uses: [
    "def:atom-knot",
    "def:hecke-normal-form",
    "prop:atomic-lp-stability",
    "prop:bw-coefficient-shadow-price",
    "prop:mass-endomorphism-tower",
    "def:confinement-level",
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
