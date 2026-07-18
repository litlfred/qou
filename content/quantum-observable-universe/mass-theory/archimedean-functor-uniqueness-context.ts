import { remark } from "../../schema/builders";

export default remark({
  label: "rem:archimedean-functor-uniqueness-context",
  title:
    "Pre-archimedean separation, corollaries, and open problems for the archimedean functor uniqueness",
  interprets: "prop:archimedean-functor-uniqueness",
  tags: [
    "archimedean",
    "realization-functor",
    "bloch-wigner",
    "pentagon-identity",
    "pre-archimedean",
    "alpha-em",
  ],
  uses: ["prop:archimedean-functor-uniqueness"],
  cites: ["suslin1991", "bloch2000"],
});
