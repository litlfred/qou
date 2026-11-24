import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lean-lib-compact-quantum-metrics",
  title:
    "Community Library 4 (CompactQuantumMetrics): Ordered-field Rieffel Lipschitz seminorms and Kantorovich duality",
  interprets: "tbl:lean-community-libraries-dag",
  uses: ["tbl:lean-community-libraries-dag", "rem:lean-lib-twisted-frobenius-hopf"],
  cites: ["rieffel1999", "rieffel2004", "connes1994"],
  tags: ["lean-infrastructure", "reservoir", "noncommutative-geometry", "quantum-metrics", "appendix"],
});
