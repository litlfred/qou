import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:mostow-confinement",
  label: "rem:encounter-literature-bridge",
  title: "Literature precedents for the geometric encounter picture",
  uses: [
    "conj:gb-reduction-pl-thimble-bijection",
    "conj:algebraic-geometric-dilog-equivalence",
  ],
  cites: [
    "mostow1968",
    "thurston1978",
    "neumann-zagier1985",
    "witten2011",
    "yekutieli2015",
    "kashaev1997",
  ],
  tags: [
    "literature-review",
    "bridge",
    "mostow-rigidity",
    "neumann-zagier",
    "witten-rigid-phase",
    "encounter",
  ],
});
