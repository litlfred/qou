import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-action",
  title: "Categorical action",
  tags: ["action", "categorical", "compositional", "string-diagram"],
  lean: {
    decl: "QOU.CategoricalAction",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "def:rigid-monoidal-category",
  ],
});
