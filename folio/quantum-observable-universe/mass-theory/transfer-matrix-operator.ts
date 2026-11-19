import { definition } from "../../schema/builders";

export default definition({
  label: "def:transfer-matrix-operator",
  title:
    "Transfer Matrix Operator for Nuclear Braid Interactions",
  tags: [
    "transfer-matrix",
    "operator",
    "hecke-algebra",
    "groebner",
    "hadron",
    "knot",
    "crossing",
    "universal",
    "interaction",
  ],
  lean: { ref: "qou:QOU.Archimedean.TransferMatrixOperator",
    validation: "not_checked",
  },
  uses: [],
  examples: ["ex:transfer-matrix-operator-nuclear-crossings"],
});
