import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:algebraic-filter-classification",
  label: "rem:algebraic-filter",
  title: "The algebraic filter",
  tags: ["fermion", "boson", "algebraic-filter", "curvature"],
  uses: [
    "rem:q-harmonic-basis-brane",
    "def:substrate-parameter",
    "rem:weight-space-decomposition",
    "prop:algebraic-filter-classification",
  ],
});
