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
  computation: {
    engine: "python",
    script: "folio-assistant/computations/jet_knot_invariants.py",
    witness: [
      "folio-assistant/computations/confined-knot-binding.witness.json",
      "folio-assistant/computations/intermediate-knot-detection.witness.json",
      "folio-assistant/computations/jet-knot-invariants.witness.json",
    ],
    status: "experimental",
  },
});
