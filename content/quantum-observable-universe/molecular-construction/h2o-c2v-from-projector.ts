import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:h2o-molecular-braid",
  label: "rem:h2o-c2v-from-projector",
  title: "$C_{2v}$ as the stabiliser of the H₂O assembly projector",
  tags: [
    "water",
    "H2O",
    "c2v",
    "assembly-projector",
    "molecular-symmetry",
  ],
  uses: ["def:h2o-molecular-braid", "def:molecular-assembly-projector"],
});
