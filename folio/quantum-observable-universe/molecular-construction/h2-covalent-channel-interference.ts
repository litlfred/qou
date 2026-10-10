import { remark } from "../../schema/builders";

/**
 * Interpretive follow-on to def:h2-molecular-braid: the q²-vs-q¹⁰ covalent
 * eigenvalue-ratio interference reading (covalent channel has less destructive
 * interference) and the LP-dual selection of the interleaved
 * [p1, e2, p2, e1] strand ordering.
 */
export default remark({
  label: "rem:h2-covalent-channel-interference",
  title: "Covalent channel eigenvalue ratio and optimal strand ordering",
  interprets: "def:h2-molecular-braid",
  uses: ["def:h2-molecular-braid"],
  tags: ["hydrogen", "H2", "covalent-channel", "eigenvalue-ratio", "strand-ordering"],
});
