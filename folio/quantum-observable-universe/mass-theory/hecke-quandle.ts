import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-quandle",
  title:
    "The Hecke quandle $Q_H(q)$ and flavour-parameterised crossing rules",
  interprets: "prop:markov-trace-axiomatic-closed-form",
  uses: [
    "rem:operator-valued-magnitude-budget",
    "rem:archimedean-image-table",
  ],
  cites: [
    "joyce1982",
    "matveev1982",
    "jones1987",
  ],
  tags: [
    "quandle",
    "hecke-algebra",
    "crossing-rule",
    "flavour",
    "complete-invariant",
    "optimization",
  ],
});
