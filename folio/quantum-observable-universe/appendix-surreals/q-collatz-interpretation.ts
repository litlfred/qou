import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-collatz-interpretation",
  title:
    "Skein-Collatz interpretation: the $(p_1^{k_1}, p_2^{k_2})$ family and uniqueness of $(2,3)$",
  interprets: "conj:q-collatz",
  uses: ["conj:collatz-contact-boundary"],
  tags: [
    "collatz",
    "skein-module",
    "contraction-gap",
    "uniqueness",
    "q-integer",
    "family",
    "monomial",
  ],
  cites: ["collatz1937", "lagarias2010"],
});
