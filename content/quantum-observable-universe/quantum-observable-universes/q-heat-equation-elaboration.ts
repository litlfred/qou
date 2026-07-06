import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-heat-equation",
  label: "rem:q-heat-equation-elaboration",
  title:
    "$q$-heat equation: two times, categorical formulation, and base-ring independence",
  tags: ["q-laplacian", "heat-equation", "reeb-flow", "base-ring-independence"],
  uses: [
    "def:q-heat-equation",
    "rem:q-laplacian-expansion",
    "rem:base-field-independence",
  ],
});
