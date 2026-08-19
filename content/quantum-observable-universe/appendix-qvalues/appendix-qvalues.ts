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
        "habiro-tail-star-identity",
        "qvalue-benchmark-table",
        "qvalue-benchmark-table-table-data",
      ],
    },
    {
      title: "The $5_2$ lane: trace field and saddle closure",
      blocks: [
        "fivetwo-trace-field",
        "fivetwo-saddle-sum-rule",
        "fivetwo-bar-odd-arithmetic-home",
        "fivetwo-dt-spectrum-split",
        "fivetwo-stokes-unimodular",
        "fivetwo-level-seven-ladder",
        "fivetwo-three-sevens",
        "fivetwo-envelope-transport",
      ],
    },
    {
      title: "Substrate evaluations",
      blocks: [
        "proton-borromean-assembly",
        "proton-mass-substrate-identity",
        "proton-mass-substrate-identity-derivation",
        "per-observable-100x-status-dashboard",
      ],
    },
  ],
});
