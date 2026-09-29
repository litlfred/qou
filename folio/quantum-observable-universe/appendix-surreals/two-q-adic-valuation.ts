import { definition } from "../../schema/builders";

export default definition({
  label: "def:two-q-adic-valuation",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.TwoQAdicValuation",
    validation: "not_checked",
  },
  title:
    "The $[2]_q$-adic valuation on the Skein module",
  uses: [
    "conj:q-collatz",
  ],
  tags: [
    "collatz",
    "contact-order",
    "adic-valuation",
    "skein-module",
    "divisor",
  ],
});
