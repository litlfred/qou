import { remark } from "../../schema/builders";

export default remark({
  label: "rem:descent-reduction",
  title: "Reduction at dimension 1",
  tags: ["descent", "dimension-reduction", "u1"],
  uses: [
    "def:q-reeb-vector-field",
    "rem:algebraic-filter",
    "rem:descent-reduction-zero",
  ],
});
