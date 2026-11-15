import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-action",
  title: "Categorical action",
  tags: ["action", "categorical", "compositional", "string-diagram"],
  lean: {
    decl: "QOU.CategoricalAction",
    validation: "not_checked",
  },
  uses: ["def:quantum-observable-universe"],
  examples: ["ex:categorical-action-notation-su2", "rem:physicist-translation", "ex:photon-wavefront"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-action-0.svg", blockIndex: 0, hash: "b6d49acff466" },
    { mime: "image/svg+xml", url: "rendered/categorical-action-1.svg", blockIndex: 1, hash: "a935ae35ebfa" },
  ],

});
