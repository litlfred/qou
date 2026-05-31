import { chapter } from "../../schema/builders";

export default chapter({
  label: "app:qvalues",
  title: "Q-Value Predictions from $q$",
  sections: [
    {
      title: "Transfer matrix Q-values",
      blocks: [
        "qvalue-derivation-chain",
        "qbeta-ck-truncation-canonical",
        "qvalue-benchmark-table",
        "qvalue-benchmark-table-table-data",
      ],
    },
  ],
});
