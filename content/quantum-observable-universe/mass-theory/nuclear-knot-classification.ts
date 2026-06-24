import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-knot-classification",
  proofs: ["prf:nuclear-knot-classification"],
  title:
    "Nuclear knot classification: braid closure type determines binding scale",
  lean: { ref: "qou:QOU.BraidKnot.nuclear_knot_classification",
    validation: "not_checked",
  },
  uses: ["def:hecke-mass-element"],
  tags: [
    "knot-classification",
    "hyperbolic",
    "figure-eight",
    "borromean",
    "binding-scale",
  ],
});
