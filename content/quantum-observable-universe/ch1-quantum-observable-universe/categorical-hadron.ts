import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-hadron",
  title: "Categorical hadron",
  lean: {
    decl: "QOU.CategoricalHadron",
    validation: "not_checked",
  },
  uses: [
    "def:rigid-monoidal-category",
    "rem:simple-objects-V",
    "def:frobenius-pairing",
  ],
  tags: ["hadron", "categorical", "vector", "composite"],
});
