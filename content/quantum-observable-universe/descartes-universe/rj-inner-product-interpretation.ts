import { remark } from "../../schema/builders";

export default remark({
  label: "rem:rj-inner-product-interpretation",
  title:
    "The Rosso--Jones inner product as archimedean descent of the categorical trace",
  interprets: "prop:rj-canonical-inner-product",
  tags: [
    "rosso-jones",
    "categorical-trace",
    "markov-trace",
    "inner-product",
    "action",
    "shell-correction",
  ],
  uses: ["cor:spectral-decomposition-qvalue"],
});
