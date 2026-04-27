import { remark } from "../../schema/builders";

export default remark({
  label: "rem:tritium-qvalue-audit",
  title: "Audit of tritium Q-value derivation",
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
