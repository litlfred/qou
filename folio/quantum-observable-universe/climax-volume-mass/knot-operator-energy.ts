import { definition } from "../../schema/builders";

export default definition({
  label: "def:knot-operator-energy",
  title: "Knot operator energy (LP-dual shadow price)",
  lean: { ref: "qou:QOU.BraidKnot.KnotOperatorEnergy",
    validation: "not_checked",
  },
  uses: ["def:stable-atom", "prop:operator-selection-lp"],
  cites: [],
  tags: [
    "knot-operator",
    "shadow-price",
    "lp-dual",
    "energy-functional",
  ],
});
