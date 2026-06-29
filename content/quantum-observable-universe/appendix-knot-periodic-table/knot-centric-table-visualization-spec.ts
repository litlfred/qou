import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:shell-transition-knot",
  label: "rem:knot-centric-table-visualization-spec",
  title:
    "Interactive visualization specification for the knot-centric periodic table",
  tags: [
    "periodic-table",
    "knot-centric",
    "visualization",
    "simulator",
    "appendix",
  ],
  uses: [
    "prop:shell-structure-eigenvalues",
    "rem:knot-atom-diagrams",
  ],
});
