import { definition } from "../../schema/builders";

export default definition({
  label: "def:transfer-matrix-operator",
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: break each loop): ([building blocks](#rem:building-block-knots))" },
  ],
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
});
