import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-dilog-heat-partition",
  interprets: "def:q-dilogarithm",
  title: "$\\mathrm{Li}_2^q$ as the $q$-heat partition function",
  tags: ["hopf-algebra", "dilogarithm", "q-heat", "partition-function"],
  uses: [
    "def:q-dilogarithm",
    "def:categorical-laplace",
    "prop:q-heat-kernel-peter-weyl",
  ],
});
