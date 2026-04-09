import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ground-state-ordering",
  title: "Ground-state ordering from transfer matrix eigenvalues",
  uses: [
    "prop:beta-decay-transfer-matrix",
    "def:typed-crossing-operator",
    "descartes-universe:prop:frobenius-gram-matrix",
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
