import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:toffoli-transfer-matrix",
  label: "rem:toffoli-transfer-matrix-interpretation",
  title: "Explicit q-AND amplitudes at the aether value $q_0$",
  uses: [
    "prop:toffoli-transfer-matrix",
    "prop:local-substrate-q",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: [
      "computations/toffoli-lp-stability.witness.json",
      "computations/probes/toffoli-qand-convention-d-derivation.witness.json",
    ],
    status: "verified",
  },
});
