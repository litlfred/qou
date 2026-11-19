import { remark } from "../../schema/builders";

export default remark({
  label: "rem:fivefold-sheets-golden-ratio",
  title: "Five sheets of $\\Sigma_4$ and the golden-ratio phase transition",
  tags: [
    "five-fold",
    "bring-surface",
    "golden-ratio",
    "monodromy",
    "phase-transition",
  ],
  interprets: "def:quantum-universe",
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/toffoli_qand_convention_d_derivation.py",
    witness: ["computations/probes/toffoli-qand-convention-d-derivation.witness.json"],
    status: "verified",
  },
});
