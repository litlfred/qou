import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:nuclear-knot-classification",
  title:
    "Nuclear knot classification: braid closure type determines binding scale",
  lean: { ref: "qou:QOU.BraidKnot.nuclear_knot_classification",
    validation: "not_checked",
  },
  uses: [
    "def:atomic-braid",
    "thm:topological-mass",
    "prop:topological-mass-formula",
    "def:hecke-mass-element",
    "prop:hook-weight-derivation",
  ],
  tags: [
    "knot-classification",
    "hyperbolic",
    "figure-eight",
    "borromean",
    "binding-scale",
  ],
});
