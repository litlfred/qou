import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:markov-trace-product",
  label: "rem:markov-trace-product-interpretation",
  title: "Connection to the vertex operator algebra",
  tags: [
    "markov-trace",
    "vertex-operator",
    "correlation-function",
    "factorization",
  ],
  uses: ["thm:markov-trace-product"],
});
