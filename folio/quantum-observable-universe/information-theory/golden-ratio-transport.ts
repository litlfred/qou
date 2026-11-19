import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:golden-ratio-degeneration",
  label: "rem:golden-ratio-transport",
  title:
    "Parallel transport of a golden-ratio parallelogram to $q_{\\mathrm{gold}}$",
  tags: [
    "golden-ratio",
    "parallel-transport",
    "q-connection",
    "elliptic-curve",
    "information-theory",
    "degeneration",
  ],
  uses: [
    "rem:golden-ratio-degeneration",
    "def:categorical-q-connection",
    "ex:q-reeb-flow",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/pentagon_to_borromean_h4_probe.py",
    witness: [
      "computations/pentagon-to-borromean-h4-probe.witness.json",
      "computations/q-pinning-50-digit.witness.json",
    ],
    status: "verified",
  },
});
