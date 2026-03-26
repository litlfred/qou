import { remark } from "../../schema/builders";

export default remark({
  label: "rem:knot-factorization",
  title: "Knot factorization through tensor powers of $V$",
  uses: [
    "def:hadron",
    "rem:simple-objects-V",
    "prop:pawlowski-leitner-basis",
  ],
  tags: ["knot", "factorization", "vector", "tensor-generation"],
});
