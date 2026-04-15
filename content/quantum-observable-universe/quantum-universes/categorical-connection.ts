import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-connection",
  title: "Categorical connection and curvature",
  lean: {
    decl: "QOU.CategoricalConnection",
    validation: "not_checked",
  },
  uses: ["def:higher-forms"],
  examples: ["ex:connection-su2"],
  tags: ["connection", "curvature"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-connection-0.svg", blockIndex: 0, hash: "36d70138d58f" },
    { mime: "image/svg+xml", url: "rendered/categorical-connection-1.svg", blockIndex: 1, hash: "8f8ed636851b" },
  ],

});
