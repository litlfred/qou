import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-action",
  title: "Categorical action",
  tags: ["action", "categorical", "compositional", "string-diagram"],
  lean: { ref: "qou:QOU.CategoricalAction",
    validation: "not_checked",
  },
  uses: ["def:quantum-observable-universe"],
  defines: ["categorical-action"],
  examples: ["ex:categorical-action-notation-su2", "rem:physicist-translation", "ex:photon-wavefront"],
});
