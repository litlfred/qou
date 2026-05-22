import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:em-coupling-chern-simons",
  title:
    "Conjectured Chern-Simons correction form $1/\\alpha = q[9]_q[10]_q\\cdot(1+\\delta_{CS}+\\kappa\\,\\delta_{CS}^2)$ (Gram-determinant $\\kappa$ unproved)",
  lean: {
    ref: "qou:QOU.DescartesUniverse.ChernSimonsCorrectionConjecture",
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
