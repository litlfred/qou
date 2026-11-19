import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:nuclear-knot-classification",
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
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
