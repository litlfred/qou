import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ring-closure-barrier",
  title: "Ring-closure energy barrier from braid rearrangement",
  tags: [
    "ring-closure",
    "energy-barrier",
    "braid",
    "rearrangement",
    "activation-energy",
    "topological",
    "crossing-energy",
  ],
  lean: { ref: "qou:QOU.Organic.alexanderWeightDifference",
    validation: "not_checked",
  },
  uses: ["def:molecular-hopf-ring"],
});
