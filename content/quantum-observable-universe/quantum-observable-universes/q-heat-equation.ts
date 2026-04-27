import { definition } from "../../schema/builders";

export default definition({
  label: "def:q-heat-equation",
  title: "$q$-Heat equation",
  tags: ["q-laplacian", "heat-equation", "reeb-flow", "evolution"],
  lean: { ref: "qou:QOU.QHeatEquation",
    validation: "not_checked",
  },
  uses: [
    "rem:q-laplacian-expansion",
    "prop:substrate-radial-coordinate",
    "rem:base-field-independence",
  ],
});
