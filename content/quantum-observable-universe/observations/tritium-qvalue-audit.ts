import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tritium-qvalue-audit",
  title: "Audit of tritium Q-value derivation",
  computation: {
    engine: "mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
  tags: [
    "tritium",
    "q-value",
    "audit",
    "verification",
    "channel-sums",
  ],
  interprets: "prop:tritium-qvalue-symbolic",
  uses: ["prop:branching-qvalue-factorization"],
});
