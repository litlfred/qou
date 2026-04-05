import { chapter } from "../../schema/builders";

export default chapter({
  label: "app:qvalues",
  title: "Q-Value Predictions from $q$",
  sections: [
    {
      heading: "Transfer matrix Q-values",
      blocks: [
        "rem:qvalue-derivation-chain",
        "ex:qvalue-benchmark-table",
      ],
    },
  ],
});
