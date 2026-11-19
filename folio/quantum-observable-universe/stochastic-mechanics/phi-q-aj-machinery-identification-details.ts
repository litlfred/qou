import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-aj-machinery-identification-details",
  title:
    "$\\Phi_q$/AJ identification — full AJ statement, significance, and Lean structure",
  interprets: "prop:phi-q-aj-machinery-identification",
  uses: [
    "prop:phi-q-aj-machinery-identification",
  ],
  tags: [
    "aj-conjecture",
    "faddeev-dilogarithm",
    "rogers-dilogarithm",
    "quantum-a-polynomial",
    "stochastic-mechanics",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "Lean sibling `phi-q-aj-machinery-identification.lean` proves the unconditional q-Weyl backbone, solution-space linearity, and saddle-regime disjointness under conjectural AJ and Faddeev/Rogers classes.",
    },
  ],
});
