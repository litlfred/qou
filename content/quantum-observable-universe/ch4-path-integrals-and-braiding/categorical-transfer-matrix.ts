import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-transfer-matrix",
  lean: { decl: "QOU.CategoricalTransferMatrix", validation: "not_checked" },
  title: "Categorical transfer matrix",
  tags: [
    "transfer-matrix", "hadron", "vertex-operator",
    "equivalence-class", "braiding",
  ],
  uses: [
    "def:hadron",
    "def:vertex-operator",
    "def:exceptional-divisor",
    "rem:knot-factorization",
    "def:localized-hadron",
  ],
});
