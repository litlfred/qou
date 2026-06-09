import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ground-state-ordering",
  lean: { ref: "qou:QOU.ParticleInteractions.ground_state_ordering", validation: "not_checked" },
  title: "Ground-state ordering from transfer matrix eigenvalues",
  uses: ["def:typed-crossing-operator"],
  tags: [
    "ground-state",
    "transfer-matrix",
    "eigenvalue",
    "ordering",
    "nuclear",
    "shell-model",
  ],
});
