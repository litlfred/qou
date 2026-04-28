import { definition } from "../../schema/builders";

export default definition({
  label: "def:substrate-parameter",
  cites: ["lusztig1993"],
  title: "Substrate parameter",
  tags: ["substrate", "deformation", "fibre-coordinate"],
  lean: { ref: "qou:QOU.SubstrateParameter",
    validation: "leanok",
  },
  uses: ["def:categorical-reeb"],
  examples: ["ex:substrate-parameter-su2"],
});
