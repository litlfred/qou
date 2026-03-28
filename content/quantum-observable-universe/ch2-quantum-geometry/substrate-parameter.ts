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
});
