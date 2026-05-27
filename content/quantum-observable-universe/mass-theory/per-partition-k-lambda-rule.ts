import { remark } from "../../schema/builders";

export default remark({
  label: "rem:per-partition-k-lambda-rule",
  title:
    "Per-partition $k_\\lambda$ rule — the open structural form of $n_\\star$",
  interprets: "prop:brane-tower-z-habiro",
  lean: {
    ref: "qou:QOU.BraidKnot.PerPartitionKLambda.candidateRule",
    validation: "not_checked",
  },
  uses: [
    "prop:brane-tower-z-habiro",
  ],
  tags: [
    "brane-tower",
    "n-star",
    "per-partition",
    "wedderburn",
    "multiplicity-refinement",
    "open-question",
    "operator-valued",
  ],
});
