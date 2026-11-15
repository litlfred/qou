import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-reduction-three",
  title: "Reduction at dimension 3",
  tags: ["descent", "dimension-reduction", "reeb", "contact"],
  uses: [
    "ex:q-reeb-vector-field",
    "prop:brings-is-qou",
    "rem:descent-reduction-two",
  ],
});
