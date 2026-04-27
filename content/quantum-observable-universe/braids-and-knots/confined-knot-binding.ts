import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confined-knot-binding",
  title:
    "Confined knot binding mechanism: character ratio decomposition per jet level",
  lean: { ref: "qou:QOU.BraidKnot.confined_knot_binding",
    validation: "not_checked",
  },
  uses: [
    "prop:three-parameters-wedderburn",
    "prop:nuclear-knot-classification",
    "def:atomic-braid",
  ],
  tags: [
    "binding-mechanism",
    "character-ratio",
    "wedderburn",
    "extremal-cancellation",
    "confined-knot",
  ],
});
