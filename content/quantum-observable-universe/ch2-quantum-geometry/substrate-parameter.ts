import { definition } from "../../schema/builders";

export default definition({
  label: "def:substrate-parameter",
  cites: ["lusztig1993"],
  title: "Substrate parameter",
  tags: ["substrate", "deformation", "fibre-coordinate"],
  lean: {
    decl: "QOU.SubstrateParameter",
    validation: "leanok",
  },
  uses: ["def:categorical-reeb"],
  examples: ["ex:substrate-parameter-su2"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/substrate-parameter-0.svg", blockIndex: 0, hash: "6a4120f43ca8" },
  ],

});
