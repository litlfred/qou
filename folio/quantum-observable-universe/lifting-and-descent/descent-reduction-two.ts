import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-reduction-two",
  title: "Reduction at dimension 2",
  tags: ["descent", "dimension-reduction", "surface", "brings-surface"],
  uses: [
    "ex:q-reeb-vector-field",
    "prop:brings-is-qou",
    "rem:descent-reduction",
  ],
});
