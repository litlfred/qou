import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-operator-selection",
  lean: { ref: "qou:QOU.ParticleInteractions.confinement_operator_selection", validation: "not_checked" },
  title: "Confinement operator selection via minimum action",
  tags: [
    "confinement",
    "borromean",
    "frobenius-dual",
    "gram-matrix",
    "minimum-action",
    "operator-selection",
    "beta-decay",
  ],
  uses: ["prop:frobenius-gram-matrix"],
  computation: {
    engine: "python",
    script: "computations/confinement_operator_selection.py",
    witness: [
      "computations/confinement-operator-selection.witness.json",
    ],
    status: "experimental",
  },
});
