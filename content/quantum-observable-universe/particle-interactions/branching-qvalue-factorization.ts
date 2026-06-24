import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:branching-qvalue-factorization",
  proofs: ["prf:branching-qvalue-factorization"],
  title:
    "Exact factorization of the branching Q-value",
  tags: [
    "factorization",
    "q-value",
    "character-sum",
    "exact",
    "branching",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.branching_qvalue_factorization",
    validation: "not_checked",
  },
  uses: ["def:spectator-normalization"],
});
