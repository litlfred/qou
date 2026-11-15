import { definition } from "../../schema/builders";

export default definition({
  label: "def:categorical-reeb",
  title: "Categorical Reeb derivation",
  lean: {
    decl: "QOU.CategoricalReeb",
    validation: "not_checked",
  },
  uses: ["def:weight-decomposition"],
  examples: ["ex:reeb-su2", "ex:connection-su2"],
  tags: ["reeb", "derivation"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/categorical-reeb-0.svg", blockIndex: 0, hash: "5aaad9614e38" },
  ],

});
