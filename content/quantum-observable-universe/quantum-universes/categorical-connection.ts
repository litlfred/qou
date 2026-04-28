import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-connection",
  title: "Categorical connection and curvature",
  lean: { ref: "qou:QOU.CategoricalConnection",
    validation: "not_checked",
  },
  uses: ["def:higher-forms"],
  examples: ["ex:connection-su2"],
  tags: ["connection", "curvature"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-connection-0.svg", blockIndex: 0, hash: "c99fb28bf175" },
    { mime: "image/svg+xml", url: "rendered/categorical-connection-1.svg", blockIndex: 1, hash: "8f8ed636851b" },
  ],

});
