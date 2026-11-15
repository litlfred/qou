import { definition } from "../../schema/builders";

export default definition({
  label: "def:h2o-molecular-braid",
  title: "Water $H_2O$ as a molecular braid",
  lean: { ref: "qou:QOU.Molecular.waterParts", validation: "not_checked" },
  uses: ["def:molecular-assembly-projector", "def:molecular-strand-partition"],
  tags: [
    "water",
    "H2O",
    "molecular-braid",
    "assembly-projector",
    "c2v",
    "lone-pair",
  ],
});
