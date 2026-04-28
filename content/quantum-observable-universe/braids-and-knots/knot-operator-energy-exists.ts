import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:knot-operator-energy-exists",
  title: "Existence of the knot operator energy",
  lean: { ref: "qou:QOU.BraidKnot.KnotOperatorEnergy.exists",
    validation: "not_checked",
  },
  uses: ["def:knot-operator-energy"],
  tags: ["existence", "knot-operator", "shadow-price", "lp-dual"],
});
