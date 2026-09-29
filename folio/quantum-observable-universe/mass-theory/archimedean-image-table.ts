import { remark } from "../../schema/builders";

export default remark({
  label: "rem:archimedean-image-table",
  title:
    "Per-structure action of the archimedean realisation $\\tau$",
  interprets: "def:archimedean-realization-functor",
  uses: ["prop:markov-trace-axiomatic-closed-form"],
  tags: [
    "archimedean",
    "realization-functor",
    "algebraic-infrastructure",
    "mass-tower",
    "homflypt",
  ],
});
