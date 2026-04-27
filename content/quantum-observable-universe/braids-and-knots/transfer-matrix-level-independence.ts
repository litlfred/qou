import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:transfer-matrix-level-independence",
  lean: { ref: "qou:QOU.transfer_matrix_level_independence",
    validation: "not_checked",
  },
  title: "Transfer matrix level independence",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "markov-trace", "level-independence",
  ],
  uses: [
    "def:categorical-transfer-matrix",
    "def:bundle-isotopy-equivalence",
  ],
  proofs: ["prf:transfer-matrix-level-independence"],
});
