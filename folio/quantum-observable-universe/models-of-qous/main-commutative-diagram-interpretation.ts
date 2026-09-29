import { remark } from "../../schema/builders";

export default remark({
  label: "rem:main-commutative-diagram-interpretation",
  title: "Reading the main commutative diagram edge-by-edge",
  interprets: "prop:main-commutative-diagram",
  uses: ["prop:main-commutative-diagram"],
  tags: ["commutative-diagram", "interpretation"],
});
