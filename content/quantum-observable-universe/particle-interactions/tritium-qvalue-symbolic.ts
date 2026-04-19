import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tritium-qvalue-symbolic",
  title:
    "Symbolic Q-value for tritium beta decay",
  tags: [
    "tritium",
    "q-value",
    "symbolic",
    "closed-form",
    "beta-decay",
  ],
  lean: {
    decl: "QOU.ParticleInteractions.tritium_qvalue_symbolic",
    file: "QOU/ParticleInteractions.lean",
    validation: "not_checked",
  },
  uses: [
    "prop:branching-qvalue-factorization",
  ],
});
