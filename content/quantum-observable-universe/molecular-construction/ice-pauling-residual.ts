import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ice-pauling-residual",
  proofs: ["prf:ice-pauling-residual"],
  title: "Pauling residual entropy of ice: $W_1 = 3/2$",
  lean: {
    ref: "qou:QOU.Molecular.pauling_multiplicity",
    validation: "not_checked",
  },
  uses: ["def:h2o-molecular-braid"],
  tags: ["ice", "pauling", "residual-entropy", "hydrogen-bond", "combinatorics"],
});
