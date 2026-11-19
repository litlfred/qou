import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confined-knot-binding",
  title:
    "Confined knot binding mechanism: character ratio decomposition per jet level",
  lean: { ref: "qou:QOU.BraidKnot.confined_knot_binding.confined_knot_extremal_cancellation",
    validation: "leanok",
  },
  uses: ["conj:nuclear-knot-classification"],
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
      "computations/probes/the_nuclear_jet_level_is_the_retired_all_pairs_object_probe.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: the_nuclear_jet_level_is_the_retired_all_pairs_object_probe.py.",
    },
  ],
});
