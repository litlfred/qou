import { chapter } from "../../schema/builders";

export default chapter({
  label: "app:qvalues",
  title:
    "Imaginary part of the complex volume: $Q$-values from $q$",
  sections: [
    {
      title: "Transfer matrix Q-values",
      blocks: [
        "im-complex-volume-intro",
        "qvalue-derivation-chain",
        "qbeta-ck-truncation-canonical",
        "qvalue-benchmark-table",
        "qvalue-benchmark-table-table-data",
      ],
    },
    {
      title: "Substrate evaluations",
      blocks: [
        "proton-mass-substrate-identity",
        "per-observable-100x-status-dashboard",
      ],
    },
  ],
});
