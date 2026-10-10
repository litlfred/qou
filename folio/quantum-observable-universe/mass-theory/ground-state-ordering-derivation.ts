import { remark } from "../../schema/builders";

export default remark({
  label: "rem:ground-state-ordering-derivation",
  title: "Ground-state ordering: eigenvalue derivation and verification",
  interprets: "prop:ground-state-ordering",
  tags: [
    "ground-state",
    "transfer-matrix",
    "eigenvalue",
    "ordering",
    "nuclear",
    "shell-model",
  ],
  uses: [
    "prop:ground-state-ordering",
    "def:typed-crossing-operator",
  ],
});
