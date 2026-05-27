import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ground-state-ordering",
  lean: { ref: "qou:QOU.ParticleInteractions.ground_state_ordering", validation: "not_started" },
  title: "Ground-state ordering from transfer matrix eigenvalues",
  uses: [
    "prop:beta-decay-transfer-matrix",
    "def:typed-crossing-operator",
    "prop:frobenius-gram-matrix",
  ],
  tags: [
    "ground-state",
    "transfer-matrix",
    "eigenvalue",
    "ordering",
    "nuclear",
    "shell-model",
  ],
});
