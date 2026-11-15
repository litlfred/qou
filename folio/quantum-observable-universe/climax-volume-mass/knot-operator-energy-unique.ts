import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-energy-unique",
  title: "Uniqueness of the knot operator energy",
  lean: { ref: "qou:QOU.BraidKnot.KnotOperatorEnergy.shadowPrice_unique",
    validation: "not_checked",
  },
  uses: ["prop:knot-operator-energy-exists"],
  tags: ["uniqueness", "knot-operator", "shadow-price"],
});
