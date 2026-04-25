import { chapter } from "../../schema/builders";

export default chapter({
  label: "app:qvalues",
  title: "Q-Value Predictions from $q$",
  sections: [
    {
      title: "Transfer matrix Q-values",
      blocks: [
        "qvalue-derivation-chain",
        "qvalue-benchmark-table",
      ],
    },
  ],
});
