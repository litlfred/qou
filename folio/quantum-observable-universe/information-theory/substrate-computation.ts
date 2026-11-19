import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:toffoli-transfer-matrix",
  label: "rem:substrate-computation",
  title: "Substrate-independence of computation",
  tags: [
    "computation",
    "universality",
    "planck-time",
    "combinatorics",
    "substrate-parameter",
    "classical-limit",
  ],
  uses: ["rem:toffoli-q-and"],
  cites: ["thooft2016"],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/toffoli_qand_convention_d_derivation.py",
    witness: ["computations/probes/toffoli-qand-convention-d-derivation.witness.json"],
    status: "verified",
  },
});
