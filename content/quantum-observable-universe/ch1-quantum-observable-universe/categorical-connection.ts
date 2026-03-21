import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-connection",
  title: "Categorical connection and curvature",
  lean: {
    decl: "QOU.CategoricalConnection",
    validation: "not_checked",
  },
  status: "not_started",
  uses: ["def:quantum-universe", "def:higher-forms"],
  examples: ["ex:connection-su2"],
  tags: ["connection", "curvature"],
});
