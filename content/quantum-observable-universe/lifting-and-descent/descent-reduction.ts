import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:mass-identity",
  label: "rem:descent-reduction",
  title: "Reduction at dimension 1",
  tags: ["descent", "dimension-reduction", "u1"],
  uses: [
    "rem:algebraic-filter",
    "rem:descent-reduction-zero",
  ],
});
