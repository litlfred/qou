import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:hadron",
  label: "rem:knot-factorization",
  title: "Knot factorization through tensor powers of $V$",
  uses: [
    "def:hadron",
    "prop:pawlowski-leitner-basis",
  ],
  tags: ["knot", "factorization", "vector", "tensor-generation"],
});
