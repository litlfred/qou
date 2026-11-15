import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-logarithm-properties",
  interprets: "def:q-logarithm",
  title: "Realisations of $\\log_q$: base ring, three contexts, Habiro ring, and Reeb-flow rapidity",
  tags: ["hopf-algebra", "primitive", "q-logarithm", "adjoint"],
  uses: [
    "def:q-logarithm",
    "rem:q-exp-finite-field-obstruction",
    "rem:q-exp-p-adic",
    "def:habiro-ring",
    "prop:q-exponential-taylor",
  ],
});
