import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confined-knot-binding",
  title:
    "Confined knot binding mechanism: character ratio decomposition per jet level",
  lean: { ref: "qou:QOU.BraidKnot.confined_knot_binding",
    validation: "not_checked",
  },
  uses: ["prop:nuclear-knot-classification"],
  tags: [
    "binding-mechanism",
    "character-ratio",
    "wedderburn",
    "extremal-cancellation",
    "confined-knot",
  ],
  computation: {
    engine: "python",
    script: "computations/jet_knot_invariants.py",
    witness: [
      "computations/confined-knot-binding.witness.json",
      "computations/intermediate-knot-detection.witness.json",
      "computations/jet-knot-invariants.witness.json",
    ],
    status: "experimental",
  },
});
