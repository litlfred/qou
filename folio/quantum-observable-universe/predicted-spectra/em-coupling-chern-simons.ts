import { remark } from "../../schema/builders";

export default remark({
  label: "rem:em-coupling-chern-simons",
  interprets: "prop:em-coupling-projection",
  title:
    "Conjectured Chern-Simons correction form $1/\\alpha = q[9]_q[10]_q\\cdot\\bigl(1+\\delta_{CS}/(1-\\delta_{CS}\\kappa)\\bigr)$ (Gram-determinant $\\kappa$ unproved)",
  lean: {
    ref: "qou:QOU.ArchimedeanUniverse.ChernSimonsCorrectionConjecture",
    validation: "not_checked",
  },
  uses: [
    "prop:em-coupling-projection",
    "prop:quantum-observable-universe-exists",
  ],
  tags: [
    "fine-structure",
    "chern-simons",
    "brings-surface",
    "genus-4",
    "torus-knot",
    "gram-matrix",
    "conjecture",
    "kappa-unproved",
  ],
});
