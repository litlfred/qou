import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-point",
  title: "Categorical point",
  tags: ["point", "categorical"],
  lean: {
    decl: "QOU.CategoricalPoint",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:quantum-universe"],
});
